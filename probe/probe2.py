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
KEY = re.compile(r"[^.]{0,220}(?:regular(?:ly)? (?:board )?meeting|meets? (?:on|every|the|monthly)|(?:1st|2nd|3rd|4th|first|second|third|fourth|last|every) (?:and (?:1st|2nd|3rd|4th|first|second|third|fourth) )?(?:Monday|Tuesday|Wednesday|Thursday|Friday))[^.]{0,220}\.?", re.I)
pages = {
 "BPL board": "https://www.boisepubliclibrary.org/about-us/board-of-trustees/",
 "BPL schedule news": "https://www.boisepubliclibrary.org/news/boise-public-library-board-of-trustees-sets-meeting-schedule-and-locations-for-year/",
 "Ada lib board": "https://adalib.org/board-of-trustees/",
 "IFPL board": "https://www.ifpl.org/library-board/",
 "TF lib board": "https://www.twinfallspubliclibrary.org/libraryboard",
 "TF lib calendar": "https://www.twinfallspubliclibrary.org/calendar",
 "Marshall board": "https://marshallpl.org/board-of-trustees/",
 "Marshall calendar": "https://marshallpl.org/calendar/",
 "Boise SD board": "https://www.boiseschools.org/board-of-trustees",
 "Boise SD board2": "https://www.boiseschools.org/our_district/board_of_trustees",
 "West Ada board": "https://www.westada.org/o/wasd/page/board-of-trustees",
 "Nampa SD board": "https://www.nsd131.org/board-of-trustees",
 "CdA SD board": "https://www.cdaschools.org/page/board-of-trustees",
 "D91 board": "https://www.ifschools.org/our-district/board-of-trustees",
 "D91 records": "https://www.ifschools.org/our-district/board-of-trustees/board-meeting-records",
 "D25 board": "https://www.sd25.us/district/board",
 "boarddocs robots": "https://go.boarddocs.com/robots.txt",
 "simbli robots": "https://simbli.eboardsolutions.com/robots.txt",
}
for k, u in pages.items():
    c, f, h = get(u)
    links = sorted(set(urljoin(f, x) for x in re.findall(r'href="([^"#]+)"', h) if re.search(r"agenda|meeting|boarddocs|simbli|eboard|highbond|diligent|boardbook|libcal|calendar|\.ics|ical|minutes", x, re.I)))[:30]
    OUT[k] = {"status": c, "final": f, "sched": [m.strip() for m in KEY.findall(text(h))][:8], "links": links, "head": text(h)[:300] if "robots" in k else ""}
tz = ZoneInfo("America/Boise")
for sid, src in {
  "ada-lib": {"id": "ada-library", "name": "Ada Community Library", "area": "x", "county": "Ada", "site": "https://adalib.org", "civic_only": True},
  "ifpl": {"id": "ifpl", "name": "IFPL", "area": "x", "county": "Bonneville", "site": "https://www.ifpl.org", "civic_only": True},
  "chubbuck": {"id": "chubbuck", "name": "Chubbuck", "area": "x", "county": "Bannock", "site": "https://cityofchubbuck.us"},
  "hailey": {"id": "hailey", "name": "Hailey", "area": "x", "county": "Blaine", "site": "https://haileycityhall.org"}}.items():
    try:
        ev = build.fetch_tribe(src, date(2026, 11, 11), date(2027, 1, 10), tz)
        OUT["tribe " + sid] = [(e["start"][:16], e["title"]) for e in ev][:25]
    except Exception as e:
        OUT["tribe " + sid] = f"ERR {e}"
try:
    ev = build.fetch_libcal({"id": "bpl", "name": "BPL", "area": "x", "county": "Ada", "host": "boisepubliclibrary.libcal.com", "calendar": 12885, "civic_only": True}, date(2026, 11, 11), date(2027, 1, 10), tz)
    OUT["libcal bpl"] = [(e["start"][:16], e["title"]) for e in ev][:30]
except Exception as e:
    OUT["libcal bpl"] = f"ERR {e}"
for k, v in OUT.items(): print("=" * 6, k); print(json.dumps(v, indent=0)[:2500])
Path("probe/report2.json").write_text(json.dumps(OUT, indent=1))
