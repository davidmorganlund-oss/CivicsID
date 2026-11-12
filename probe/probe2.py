import json, re, sys
from datetime import date
from zoneinfo import ZoneInfo
from pathlib import Path
from urllib.parse import urljoin
import requests
sys.path.insert(0, "probe"); import build
S = requests.Session(); S.headers["User-Agent"] = build.UA
OUT = {}
def get(u, **kw):
    try:
        r = S.get(u, timeout=25, **kw); return r.status_code, r.url, r.text
    except Exception as e:
        return 0, u, f"ERR {e}"[:200]
def text(h):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S | re.I)
    return " ".join(re.sub(r"<[^>]+>", " ", h).split())
tz = ZoneInfo("America/Boise")
for name, sid in {"nampa": 36031905, "d91": 36032118, "d25": 36031884, "westada": 36031062}.items():
    src = {"id": name, "name": name, "area": "x", "county": "x", "listing": f"https://simbli.eboardsolutions.com/SB_Meetings/SB_MeetingListing.aspx?S={sid}"}
    try:
        c, f, h = get(src["listing"])
        OUT["simbli " + name] = {"status": c, "title": (re.findall(r"<title>(.*?)</title>", h, re.S) or [""])[0].strip(),
                                 "events": [(e["start"][:16], e["title"]) for e in build.normalize_simbli(src, h, date(2026, 11, 11), date(2027, 1, 10), tz)],
                                 "rows_all": build.SIMBLI_ROW.findall(text(h))[:6]}
    except Exception as e:
        OUT["simbli " + name] = f"ERR {e}"
base = "https://cdaschools.community.diligentoneplatform.com"
for p in ["/Portal/MeetingTypeList.aspx", "/Services/MeetingsService.svc/meetings?from=2026-11-11&to=2027-01-10&loadall=false", "/Portal/MeetingInformation.aspx", "/robots.txt"]:
    c, f, h = get(base + p)
    OUT["cda " + p] = {"status": c, "final": f, "head": (h[:1500] if "Services" in p or "robots" in p else text(h)[:1500])}
c, f, h = get("https://www.boiseschools.org/sitemap.xml")
OUT["boise sd sitemap"] = {"status": c, "board": sorted(set(re.findall(r"<loc>([^<]*(?:board|trustee)[^<]*)</loc>", h, re.I)))[:20]}
for u in ["https://www.ifpl.org/board/", "https://www.westada.org/o/wasd/page/board-of-trustees", "https://www.cdaschools.org/page/board-of-trustees"]:
    c, f, h = get(u)
    OUT[u] = {"status": c, "text": text(h)[:2500], "links": sorted(set(urljoin(f, x) for x in re.findall(r'href="([^"#]+)"', h) if re.search(r"simbli|diligent|meeting|agenda|board", x, re.I)))[:20]}
for k, v in OUT.items(): print("=" * 6, k); print(json.dumps(v, indent=0)[:2500])
Path("probe/report2.json").write_text(json.dumps(OUT, indent=1))
