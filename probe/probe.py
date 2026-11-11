"""One-off survey of Idaho county websites: what platform each runs, which
calendar feeds it publishes, what robots.txt allows, and any regular meeting
schedule stated on the commissioners' pages. Writes probe/report.json."""
import concurrent.futures as cf
import json, re, sys
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib import robotparser
import requests

UA = "CivicsID/0.1 (BarNone nonprofit civic calendar; contact via barnoneinc.org)"
ROOT = Path(__file__).resolve().parent.parent
LOCAL = json.loads((ROOT / "site/data/local.json").read_text())
S = requests.Session(); S.headers["User-Agent"] = UA
DAY = r"(Monday|Tuesday|Wednesday|Thursday|Friday)s?"


def get(url, **kw):
    try:
        r = S.get(url, timeout=25, allow_redirects=True, **kw)
        return r.status_code, r.url, r.text
    except Exception as exc:
        return 0, url, f"ERR {type(exc).__name__}: {exc}"[:200]


def text_of(html):
    html = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", html)
    return " ".join(re.sub(r"<[^>]+>", " ", html).replace("&nbsp;", " ").replace("&amp;", "&").split())


def schedule_sentences(html):
    t = text_of(html)
    out = []
    for m in re.finditer(r"[^.]{0,220}\b(1st|2nd|3rd|4th|first|second|third|fourth|last|every|each)\b[^.]{0,60}\b" + DAY + r"[^.]{0,160}\.", t, re.I):
        s = m.group(0).strip()
        if re.search(r"meet|session|commission|board", s, re.I) and s not in out:
            out.append(s[:380])
    return out[:6]


def links(html, base, pattern):
    out = []
    for href, label in re.findall(r'<a\b[^>]*href="([^"#]+)"[^>]*>(.*?)</a>', html, re.S | re.I):
        lab = text_of(label)[:60]
        if re.search(pattern, href + " " + lab, re.I):
            u = urljoin(base, href.replace("&amp;", "&"))
            if (lab, u) not in out:
                out.append((lab, u))
    return out[:40]


def platform(html):
    marks = {"civicplus": r"CivicPlus|/AgendaCenter|CivicEngage", "revize": r"revize", "govoffice": r"govoffice|Catalis",
             "municipalone": r"Municipal One", "wordpress": r"wp-content", "tribe": r"tribe-events|tribe_events",
             "mec": r"modern-events-calendar", "squarespace": r"squarespace", "wix": r"wix\.com|_wixCIDX",
             "granicus": r"granicus", "civicclerk": r"civicclerk", "boardbook": r"boardbook", "escribe": r"escribemeetings",
             "legistar": r"legistar", "iqm2": r"iqm2", "primegov": r"primegov", "novus": r"novusagenda",
             "libcal": r"libcal", "googlecal": r"calendar\.google\.com", "outlookcal": r"outlook\.office365\.com/owa/calendar",
             "ics": r"\.ics\b|webcal:", "municode": r"municodemeetings", "drupal": r"Drupal", "govstack": r"govstack|govAccess|Granicus govAccess"}
    return [k for k, p in marks.items() if re.search(p, html, re.I)]


def robots_for(base):
    rp = robotparser.RobotFileParser()
    code, _, txt = get(urljoin(base, "/robots.txt"))
    if code == 200 and "<html" not in txt[:200].lower():
        rp.parse(txt.splitlines())
    else:
        rp.parse([])
    return rp, (txt[:800] if code == 200 else f"status {code}")


def probe_county(name, info):
    out = {"county": name, "site": info.get("site", "")}
    site = info.get("site")
    if not site:
        return out
    code, final, html = get(site)
    out.update(status=code, final=final, platform=platform(html) if code else [], title=(re.search(r"<title>(.*?)</title>", html, re.S | re.I) or [None, ""])[1].strip()[:120])
    if not code:
        out["error"] = html; return out
    base = f"{urlparse(final).scheme}://{urlparse(final).netloc}"
    rp, robots = robots_for(base)
    out["robots"] = robots
    out["links"] = links(html, final, r"agenda|meeting|calendar|commissioner|board|event")
    pages = [u for lab, u in out["links"] if re.search(r"commission|meeting|agenda", lab, re.I) and urlparse(u).netloc == urlparse(final).netloc][:4]
    for extra in [info.get("commissioners"), info.get("meetings")]:
        if extra and extra not in pages:
            pages.insert(0, extra)
    out["schedule"] = schedule_sentences(html)
    out["pages"] = {}
    for p in pages[:5]:
        c, f, h = get(p)
        out["pages"][p] = {"status": c, "schedule": schedule_sentences(h) if c == 200 else [],
                           "links": links(h, f, r"agenda|calendar|\.ics|ical|rss|feed|escribe|civicclerk|boardbook|meeting")[:15] if c == 200 else [],
                           "platform": platform(h) if c == 200 else []}
        out["schedule"] += [s for s in out["pages"][p]["schedule"] if s not in out["schedule"]]
    feeds = {}
    if "civicplus" in out["platform"] or re.search(r"/Calendar\.aspx|/AgendaCenter", html, re.I):
        c, f, h = get(urljoin(base, "/iCalendar.aspx"))
        feeds["civicplus_ical"] = {"status": c, "allowed": rp.can_fetch(UA, urljoin(base, "/common/modules/iCalendar/iCalendar.aspx?catID=1&feed=calendar")),
                                   "cats": re.findall(r"catID=(\d+)[^>]*>.*?</a>.*?|", "") or
                                   [(cid, text_of(lbl)[:60]) for lbl, cid in re.findall(r"(?is)<(?:td|li|div|span|h\d)[^>]*>([^<]{2,80})</(?:td|li|div|span|h\d)>(?:(?!catID).){0,600}?catID=(\d+)", h)][:40]}
        if not feeds["civicplus_ical"]["cats"]:
            feeds["civicplus_ical"]["raw_ids"] = sorted(set(re.findall(r"catID=(\d+)", h)))[:40]
        c, f, h = get(urljoin(base, "/rss.aspx"))
        feeds["civicplus_rss"] = {"status": c, "agenda_feeds": [(text_of(l)[:60], urljoin(base, u.replace("&amp;", "&"))) for u, l in re.findall(r'href="([^"]*RSSFeed\.aspx\?ModID=65[^"]*)"[^>]*>(.*?)</a>', h, re.S)][:30],
                                  "calendar_feeds": [(text_of(l)[:60], urljoin(base, u.replace("&amp;", "&"))) for u, l in re.findall(r'href="([^"]*RSSFeed\.aspx\?ModID=58[^"]*)"[^>]*>(.*?)</a>', h, re.S)][:30]}
    if "wordpress" in out["platform"]:
        for key, path in [("tribe_api", "/wp-json/tribe/events/v1/events?per_page=5"), ("events_feed", "/events/feed/"),
                          ("tribe_ical", "/events/?ical=1"), ("mec_feed", "/feed/?post_type=mec-events")]:
            c, f, h = get(urljoin(base, path))
            feeds[key] = {"status": c, "url": f, "allowed": rp.can_fetch(UA, f), "sample": h[:300] if c == 200 else ""}
    if "revize" in out["platform"]:
        for lab, u in out["links"]:
            if "calendar" in u.lower():
                c, f, h = get(u)
                feeds["revize_calendar"] = {"url": u, "status": c, "hints": sorted(set(re.findall(r"[\w/\.\-]*(?:calendar_data|\.ics|rss|feed)[\w/\.\-\?=&]*", h)))[:15]}
                break
    if "govoffice" in out["platform"]:
        sec = re.search(r"index\.asp\?SEC=([0-9A-F\-]{36})[^\"]*\"[^>]*>\s*(?:See All Events|Calendar|Events)", html, re.I)
        feeds["govoffice"] = {"section": sec.group(1) if sec else "", "allowed": rp.can_fetch(UA, urljoin(base, "/admin/dm/Item/GetUpcomingEvents/"))}
    out["feeds"] = feeds
    return out


def guess_tenants(name):
    slug = re.sub(r"[^a-z]", "", name.lower())
    res = {}
    for key, url in [("civicclerk", f"https://{slug}countyid.api.civicclerk.com/v1/Events?$top=1&$orderby=startDateTime%20desc"),
                     ("civicclerk2", f"https://{slug}coid.api.civicclerk.com/v1/Events?$top=1&$orderby=startDateTime%20desc"),
                     ("escribe", f"https://pub-{slug}county.escribemeetings.com/"),
                     ("legistar", f"https://webapi.legistar.com/v1/{slug}county/events?$top=1"),
                     ("primegov", f"https://{slug}county.primegov.com/api/v2/PublicPortal/ListUpcomingMeetings")]:
        c, f, h = get(url)
        res[key] = {"status": c, "sample": h[:200] if c == 200 else ""}
    return res


def main():
    counties = LOCAL["counties"]
    with cf.ThreadPoolExecutor(8) as ex:
        sites = dict(zip(counties, ex.map(lambda kv: probe_county(*kv), counties.items())))
        tenants = dict(zip(counties, ex.map(guess_tenants, counties)))
    for c in sites:
        sites[c]["tenants"] = {k: v for k, v in tenants[c].items() if v["status"] == 200}
    (ROOT / "probe/report.json").write_text(json.dumps(sites, indent=1))
    for c, r in sites.items():
        print(f"{c:12} {r.get('status')} {','.join(r.get('platform', []))[:60]:60} feeds={list(r.get('feeds', {}))} tenants={list(r['tenants'])}")


if __name__ == "__main__":
    main()
