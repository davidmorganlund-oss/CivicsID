"""Second pass: dig into the specific calendar systems the first pass found."""
import json, re
from pathlib import Path
from datetime import date, timedelta
import requests

UA = "CivicsID/0.1 (BarNone nonprofit civic calendar; contact via barnoneinc.org)"
S = requests.Session(); S.headers["User-Agent"] = UA
OUT = {}


def get(url, **kw):
    try:
        r = S.get(url, timeout=25, **kw); return r.status_code, r.url, r.text
    except Exception as e:
        return 0, url, f"ERR {e}"[:200]


def note(key, val):
    OUT[key] = val; print("=" * 8, key); print(json.dumps(val, indent=1)[:3000])


# CivicPlus calendar categories (CID values in the calendar page's filter)
for name, base in [("Power", "https://www.powercounty.gov"), ("Lemhi", "https://www.lemhicountyidaho.org"),
                   ("Clark", "https://www.clark-co.id.gov"), ("Jefferson", "https://www.jcgov.us"),
                   ("Gooding", "https://www.goodingcounty.org"), ("Minidoka", "https://www.minidoka.id.us"),
                   ("Washington", "https://www.co.washington.id.us"), ("Jerome", "https://www.jeromecountyid.us")]:
    c, f, h = get(base + "/Calendar.aspx")
    cats = sorted(set(re.findall(r'(?:value|CID=)"?(\d+)"?[^>]*>\s*([^<]{3,60})<', h)))
    ical = {}
    for cid, label in cats[:20]:
        c2, f2, h2 = get(base + f"/common/modules/iCalendar/iCalendar.aspx?catID={cid}&feed=calendar")
        ev = re.findall(r"SUMMARY:(.*)", h2)
        dt = re.findall(r"DTSTART[^:]*:(\d{8})", h2)
        ical[f"{cid} {label.strip()}"] = {"status": c2, "n": len(ev), "future": sum(d >= date.today().strftime("%Y%m%d") for d in dt),
                                         "titles": sorted(set(e.strip() for e in ev))[:12]}
    note(f"civicplus {name}", {"status": c, "cats": ical})

# Bannock: The Events Calendar REST API
c, f, h = get("https://www.bannockcounty.gov/wp-json/tribe/events/v1/events", params={"per_page": 50})
try:
    j = json.loads(h)
    note("tribe Bannock", [[e["start_date"], e["title"], [x["name"] for x in e.get("categories", [])],
                            (e.get("venue") or {}).get("venue", "") if isinstance(e.get("venue"), dict) else ""] for e in j["events"]])
except Exception as e:
    note("tribe Bannock", {"status": c, "err": str(e), "h": h[:300]})

# WordPress events feeds (Butte, Camas, Elmore, Idaho, Owyhee)
for name, url in [("Butte", "https://buttecountyid.us/events/feed/"), ("Camas", "https://camascounty.id.gov/events/feed/"),
                  ("Elmore", "https://elmorecounty.org/events/feed/"), ("Idaho", "https://idahocounty.org/events/feed/"),
                  ("Owyhee", "https://owyheecounty.net/events/feed/"), ("Owyhee ical", "https://owyheecounty.net/events/?ical=1"),
                  ("Owyhee api", "https://owyheecounty.net/wp-json/tribe/events/v1/events?per_page=20&start_date=2026-11-01")]:
    c, f, h = get(url)
    items = re.findall(r"<item>(.*?)</item>", h, re.S)
    note(f"wp {name}", {"status": c, "url": f, "n": len(items), "head": h[:250],
                        "items": [re.sub(r"\s+", " ", re.sub(r"<(content:encoded|description)>.*?</\1>", "", i, flags=re.S))[:500] for i in items[:4]],
                        "ical": re.findall(r"SUMMARY:(.*)", h)[:10]})

# Platform behind cassia.gov / bonnercountyid.gov / valleycountyid.gov / payettecounty.org / bonnevillecountyidaho.gov
for name, url in [("Cassia", "https://www.cassia.gov/meetings"), ("Bonner", "https://www.bonnercountyid.gov/meetings"),
                  ("Valley", "https://www.valleycountyid.gov/calendar/72/"), ("Payette", "https://www.payettecounty.org/calendar"),
                  ("Bonneville", "https://www.bonnevillecountyidaho.gov/calendar"), ("Nez Perce", "https://www.co.nezperce.id.us/Elected-Officials/Commissioners/Commissioner-Agendas")]:
    c, f, h = get(url)
    note(f"page {name}", {"status": c, "url": f, "gen": re.findall(r'<meta name="generator" content="([^"]+)', h),
                          "feedlinks": sorted(set(re.findall(r'(?:href|src|data-[\w-]+)="([^"]*(?:ical|\.ics|rss|feed|webcal|calendar/\d+|getevents|api/)[^"]*)"', h, re.I)))[:30],
                          "scripts": sorted(set(re.findall(r'<script[^>]+src="([^"]+)"', h)))[:15],
                          "sample": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h))[600:1600]})

# Revize calendars: Google Calendar feeds behind data-google-feed
for name, url in [("Madison", "https://www.madisoncountyid.gov/calendar.php"), ("Franklin", "https://www.franklincountyidaho.org/calendar.php"),
                  ("Clearwater", "https://www.clearwatercounty.org/calendar.php"), ("Caribou", "https://www.cariboucounty.us/calendar.php"),
                  ("Gem", "https://www.gemcounty.org/calendar.php"), ("Teton revize", "https://www.tetoncountyidaho.gov/calendar.php")]:
    c, f, h = get(url)
    note(f"revize {name}", {"status": c, "google": sorted(set(re.findall(r'data-google-feed="([^"]*)"', h))),
                            "gcal": sorted(set(re.findall(r'[\w.\-]+@group\.calendar\.google\.com|[\w.\-]+%40group\.calendar\.google\.com', h)))[:10],
                            "hints": sorted(set(re.findall(r'(?:src|href|data-[\w-]+)="([^"]*(?:calendar|events|json|ical|feed)[^"]*)"', h, re.I)))[:25]})

# Teton eScribe calendar service
try:
    r = S.post("https://pub-tetoncounty.escribemeetings.com/MeetingsCalendarView.aspx/GetCalendarMeetings",
               json={"calendarStartDate": date.today().isoformat(), "calendarEndDate": (date.today() + timedelta(60)).isoformat()}, timeout=25)
    note("escribe Teton", {"status": r.status_code, "body": r.text[:2500]})
except Exception as e:
    note("escribe Teton", str(e))

# Canyon County's own agenda system, one day at a time
for d in [date.today() + timedelta(i) for i in range(0, 8)]:
    c, f, h = get("https://agenda.canyoncounty.id.gov/Agenda/Index", params={"date": d.isoformat()})
    t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style).*?</\1>", "", h)))
    note(f"canyon {d}", {"status": c, "text": t[:700]})

Path("probe/report2.json").write_text(json.dumps(OUT, indent=1))
