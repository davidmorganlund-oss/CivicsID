import json, re, io
from pathlib import Path
from urllib.parse import urljoin
import requests, pypdf
S = requests.Session(); S.headers["User-Agent"] = "CivicsID/0.1 (BarNone nonprofit civic calendar; contact via barnoneinc.org)"
OUT = {}
def get(u, **kw):
    try:
        r = S.get(u, timeout=25, **kw); return r.status_code, r.url, r.text
    except Exception as e:
        return 0, u, f"ERR {e}"[:200]
PLAT = {"civicplus": r"Calendar\.aspx|AgendaCenter|civicplus", "civicclerk": r"civicclerk", "legistar": r"legistar", "boardbook": r"boardbook",
        "boarddocs": r"boarddocs", "simbli": r"simbli|eboardsolutions", "libcal": r"libcal", "bibliocommons": r"bibliocommons", "tribe": r"tribe-events|wp-json/tribe",
        "granicus": r"granicus", "primegov": r"primegov", "iqm2": r"iqm2", "novus": r"novusagenda", "municode": r"municodemeetings", "civicweb": r"civicweb",
        "assabet": r"assabetinteractive", "localist": r"localist", "communico": r"communico|evanced|librarymarket|libnet", "google": r"calendar\.google\.com",
        "ical": r"\.ics|ical=1|feed=my-calendar|iCalendar", "diligent": r"diligent|community\.highbond", "swagit": r"swagit", "meetings_gov": r"/meetings\b"}
sites = {
 "ACHD": "https://achdidaho.org/", "Boise Public Library": "https://www.boisepubliclibrary.org/", "Ada Community Library": "https://www.adalib.org/",
 "Idaho Falls Public Library": "https://www.ifpl.org/", "Twin Falls Public Library": "https://www.twinfallspubliclibrary.org/", "Marshall Public Library": "https://www.marshallpl.org/",
 "Boise SD": "https://www.boiseschools.org/", "West Ada SD": "https://www.westada.org/", "Nampa SD": "https://www.nsd131.org/", "CdA SD": "https://www.cdaschools.org/",
 "Idaho Falls D91": "https://www.d91.k12.id.us/", "Pocatello D25": "https://www.sd25.us/",
 "Eagle": "https://www.cityofeagle.org/", "Garden City": "https://gardencityidaho.org/", "Ammon": "https://www.cityofammon.us/", "Chubbuck": "https://www.cityofchubbuck.us/",
 "Rexburg": "https://www.rexburg.org/", "Blackfoot": "https://www.cityofblackfoot.org/", "Mountain Home": "https://www.mountain-home.us/", "Burley": "https://www.burleyidaho.org/",
 "Sandpoint": "https://www.sandpointidaho.gov/", "Hailey": "https://www.haileycityhall.org/", "Emmett": "https://www.cityofemmett.org/meeting-information", "Jerome": "https://www.ci.jerome.id.us/",
}
for k, u in sites.items():
    c, f, h = get(u)
    hits = {p: len(re.findall(rx, h, re.I)) for p, rx in PLAT.items() if re.search(rx, h, re.I)}
    links = sorted(set(urljoin(f, x) for x in re.findall(r'href="([^"#]+)"', h) if re.search(r"agenda|meeting|calendar|board|event|trustee|council|ics|boarddocs|boardbook|libcal|civicclerk|legistar|granicus|simbli", x, re.I)))[:45]
    robots = get(urljoin(f, "/robots.txt"))[2][:300] if c == 200 else ""
    OUT[k] = {"status": c, "final": f, "len": len(h), "hits": hits, "links": links, "robots": robots, "title": (re.findall(r"<title[^>]*>(.*?)</title>", h, re.S) or [""])[0].strip()[:80]}
    print("=" * 6, k, c, f, hits); print("\n".join(links[:30]))
# Nampa civicplus
c, f, h = get("https://www.cityofnampa.us/Calendar.aspx")
OUT["nampa cal"] = {"status": c, "cats": sorted(set(re.findall(r'value="(\d+)"[^>]*>\s*([^<]{3,60})<', h)))[:60]}
c, f, h = get("https://www.cityofnampa.us/common/modules/iCalendar/iCalendar.aspx?catID=27&feed=calendar")
OUT["nampa ical27"] = {"status": c, "head": h[:300], "titles": sorted(set(re.findall(r"SUMMARY:(.*)", h)))[:15]}
# Ada daily agenda
u = "https://apps.adacounty.id.gov/AdaFileBrowse/Home/OpenDocument"
for doc in ["\\2026\\11 November\\11-17-26_Daily.pdf", "\\2026\\11 November\\11-18-26_Daily.pdf", "\\2026\\11 November\\11-18-26_Public_Hearing_with_Staff_Links.pdf", "\\2026\\2026 ANNUAL REGULAR MEETING NOTICE.pdf"]:
    r = S.get(u, params={"papp": "BOCCAgendas", "doc": doc, "puid": "null"}, timeout=30)
    try: t = "\n".join(p.extract_text() or "" for p in pypdf.PdfReader(io.BytesIO(r.content)).pages)
    except Exception as e: t = f"ERR {e} {r.status_code} {r.text[:200]}"
    OUT["ada " + doc] = {"status": r.status_code, "text": t[:3500]}
c, f, h = get("https://apps.adacounty.id.gov/AdaFileBrowse/?papp=BOCCAgendas")
OUT["ada list"] = {"status": c, "len": len(h), "sample": re.findall(r'"filterPath":\s*"([^"]*11 November[^"]*)",\s*"hasChild":\s*\w+,\s*"id":\s*"\d+",\s*"isFile":\s*true,\s*"name":\s*"([^"]+)"', h)[:5]}
c, f, h = get("https://apps.adacounty.id.gov/AdaFileBrowse/?papp=DS_Agendas")
OUT["ada DS"] = {"status": c, "names": re.findall(r'"name":\s*"([^"]+)"', h)[:40]}
for k in [x for x in OUT if not x.startswith(tuple(sites))]: print("=" * 6, k); print(json.dumps(OUT[k], indent=0)[:3000])
Path("probe/report2.json").write_text(json.dumps(OUT, indent=1))
