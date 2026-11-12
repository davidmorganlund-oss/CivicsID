import json, re
from pathlib import Path
from urllib.parse import urljoin
import requests
S = requests.Session(); S.headers["User-Agent"] = "CivicsID/0.1 (BarNone nonprofit civic calendar; contact via barnoneinc.org)"
OUT = {}
def get(u, **kw):
    try:
        r = S.get(u, timeout=25, **kw); return r.status_code, r.url, r.text
    except Exception as e:
        return 0, u, f"ERR {e}"[:200]
def text(h):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S | re.I)
    return " ".join(re.sub(r"<[^>]+>", " ", h).split())
for k, u in {
  "simbli nampa": "https://simbli.eboardsolutions.com/SB_Meetings/SB_MeetingListing.aspx?S=36031905",
  "simbli d91": "https://simbli.eboardsolutions.com/SB_Meetings/SB_MeetingListing.aspx?S=36032118",
  "simbli d25": "https://simbli.eboardsolutions.com/SB_Meetings/SB_MeetingListing.aspx?S=36031884",
  "d25 board": "https://www.sd25.us/district/board",
  "westada home": "https://www.westada.org/",
  "cda home": "https://www.cdaschools.org/",
  "boise sd home": "https://www.boiseschools.org/",
  "ifpl docs": "https://www.ifpl.org/index.php/library-board-meeting-documents/",
  "boarddocs boise": "https://go.boarddocs.com/id/boise/Board.nsf/Public",
  "boarddocs d25": "https://go.boarddocs.com/id/pcsd25/Board.nsf/Public",
}.items():
    c, f, h = get(u)
    OUT[k] = {"status": c, "final": f, "len": len(h),
              "simbli": sorted(set(re.findall(r"https?://simbli[^\"' <]+", h)))[:6],
              "diligent": sorted(set(re.findall(r"https?://[\w.-]*(?:highbond|diligent)[^\"' <]+", h)))[:6],
              "boarddocs": sorted(set(re.findall(r"https?://go\.boarddocs[^\"' <]+", h)))[:6],
              "feeds": sorted(set(re.findall(r"[^\"' <]*(?:\.ics|ical|/rss|feed)[^\"' <]*", h, re.I)))[:12],
              "board_links": sorted(set(urljoin(f, x) for x in re.findall(r'href="([^"#]+)"', h) if re.search(r"board|trustee", x, re.I)))[:15],
              "text": text(h)[:1500]}
for k, v in OUT.items(): print("=" * 6, k); print(json.dumps(v, indent=0)[:2200])
Path("probe/report2.json").write_text(json.dumps(OUT, indent=1))
