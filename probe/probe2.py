import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests
out = {}
H = {"User-Agent": build.UA}
for host in ["https://msd281.community.diligentoneplatform.com", "https://fruitland.community.highbond.com", "https://go.boarddocs.com"]:
    try:
        r = requests.get(host + "/robots.txt", headers=H, timeout=30); out["robots " + host] = f"{r.status_code} {r.text[:600]}"
    except Exception as exc:
        out["robots " + host] = repr(exc)[:200]
for base in ["https://msd281.community.diligentoneplatform.com", "https://fruitland.community.highbond.com"]:
    for path in ["/Services/MeetingsService.svc/meetings?from=2026-11-01&to=2027-01-31&loadall=false", "/Portal/MeetingTypeList.aspx", "/Portal/"]:
        u = base + path
        try:
            build.check_robots(u)
            r = requests.get(u, headers=H, timeout=45)
            out[u] = f"{r.status_code} {r.headers.get('content-type')} {r.text[:900]}"
        except Exception as exc:
            out[u] = repr(exc)[:200]
for site in ["bcsd61", "csd132"]:
    u = f"https://go.boarddocs.com/id/{site}/Board.nsf/Public"
    try:
        build.check_robots(u); r = requests.get(u, headers=H, timeout=45)
        h = r.text
        out[u] = {"status": r.status_code, "committee": re.findall(r"committee[^\"']{0,40}[\"']([A-Z0-9]{8,20})[\"']", h, re.I)[:5],
                  "ids": sorted(set(re.findall(r"\b[A-Z0-9]{12}\b", h)))[:10], "snip": re.findall(r".{0,80}GetMeetingsList.{0,200}", h)[:2]}
        for cid in out[u]["committee"][:1] + out[u]["ids"][:3]:
            rr = requests.post(f"https://go.boarddocs.com/id/{site}/Board.nsf/BD-GetMeetingsList?open", data={"current_committee_id": cid}, headers=H, timeout=45)
            out[f"{site} meetings {cid}"] = f"{rr.status_code} {rr.text[:500]}"
    except Exception as exc:
        out[u] = repr(exc)[:200]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print("done")
