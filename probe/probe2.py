"""Probe: run existing connectors against school districts; find Tyler/BoardDocs/HighBond details; schedule text."""
import json, re, sys
from pathlib import Path
from datetime import date
from zoneinfo import ZoneInfo
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build
tz = ZoneInfo("America/Boise"); a, b = date(2026, 11, 22), date(2027, 1, 21)
out = {}
def run(name, fn, src):
    try:
        ev = fn(src, a, b, tz)
        out[name] = {"n": len(ev), "sample": [(e["start"][:16], e["title"][:50], e.get("location", "")[:40]) for e in ev[:6]]}
    except Exception as exc:
        out[name] = {"error": (type(exc).__name__ + ": " + str(exc))[:200]}
base = {"county": "X", "area": "X", "category": "school"}
for name, s in [("middleton", "36030890"), ("emmett", "36030867"), ("lewiston", "36031908"), ("fremont", "36031552"), ("caldwell", "36031513")]:
    run("simbli " + name, build.fetch_simbli, dict(base, id=name, name=name, listing=f"https://simbli.eboardsolutions.com/SB_Meetings/SB_MeetingListing.aspx?S={s}"))
for name, org in [("bonneville93", 1349), ("minidoka331", 2041)]:
    run("boardbook " + name, build.fetch_boardbook, dict(base, id=name, name=name, organization=org))
# Tyler Meeting Manager links on district pages
for u in ["https://www.d93schools.org/board-meetings", "https://www.tfsd.org/page/school-board", "https://www.d93schools.org/school-board"]:
    try:
        h = build.get(u).text
        out["tyler " + u] = sorted(set(re.findall(r"https?://[a-z0-9.-]*tylerapp\.com/[^\"' <]*", h)))[:6]
    except Exception as exc:
        out["tyler " + u] = str(exc)[:150]
# BoardDocs robots and meetings list
for site in ["bcsd61", "csd132"]:
    u = f"https://go.boarddocs.com/id/{site}/Board.nsf/BD-GetMeetingsList?open"
    try:
        build.check_robots(u)
        import requests
        r = requests.post(u, data={"current_committee_id": ""}, headers={"User-Agent": build.UA}, timeout=60)
        out["boarddocs " + site] = f"{r.status_code} {r.text[:600]}"
    except Exception as exc:
        out["boarddocs " + site] = (type(exc).__name__ + ": " + str(exc))[:200]
# HighBond / Diligent portals and schedule text on remaining district pages
PAGES = {
 "moscow": "https://www.msd281.org/page/board-meetings-minutes-notices", "cassia": "https://www.cassiaschools.org/",
 "vallivue": "https://www.vallivue.org/apps/pages/index.jsp?uREC_ID=1166963&type=d", "vallivue_home": "https://www.vallivue.org/",
 "kuna": "https://www.kunaschools.org/boardagendas", "madison": "https://www.msd321.com/page/board-of-trustees",
 "lakeland": "https://www.lakelandsd.org/apps/pages/index.jsp?uREC_ID=1031548&type=d", "lakeland_home": "https://www.lakelandsd.org/",
 "postfalls": "https://www.pfsd.com/board-of-trustees/board-of-trustees-meeting-notices",
 "blackfoot": "https://www.sd55.org/board-meetings", "lposd": "https://www.lposd.org/board-of-trustees", "lposd_ag": "https://www.lposd.org/board-of-trustees/agendas",
 "jerome": "https://www.jeromeschools.org/", "kimberly": "https://www.kimberly.edu/", "snakeriver": "https://www.snakeriver.org/",
 "shelley": "https://www.shelleyschools.org/", "preston": "https://www.prestonschools.org/", "twinfalls": "https://www.tfsd.org/page/school-board",
 "bonnersferry": "https://www.bcsd101.com/", "madison_home": "https://www.msd321.com/", "jefferson": "https://sd251.org/", "mtnhome": "https://mhsd193.org/",
}
for k, u in PAGES.items():
    try:
        build.check_robots(u)
        r = build.get(u); h = r.text
        txt = " ".join(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", h)).split())
        sched = re.findall(r"[^.]{0,140}(?:regular(?:ly)? (?:board )?(?:meeting|meetings)|board meets|meets on|meetings are held|meeting is held)[^.]{0,180}\.", txt, re.I)[:4]
        links = [x for x in re.findall(r'href="([^"]+)"', h) if re.search(r"board|trustee|agenda|meeting|highbond|diligent|boarddocs|simbli|boardbook|tylerapp", x, re.I)]
        out["page " + k] = {"final": r.url, "sched": sched, "links": sorted(set(links))[:14]}
    except Exception as exc:
        out["page " + k] = {"error": (type(exc).__name__ + ": " + str(exc))[:150]}
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print("done")
