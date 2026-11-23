import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests
from sweeplib import scan_site, text
out = {}
for org in [2093, 2127, 2607, 1566]:
    try:
        h = build.get(f"https://meetings.boardbook.org/Public/Organization/{org}").text
        out[f"bb {org}"] = text((re.search(r"<title>(.*?)</title>", h, re.S) or [None, ""])[1])
    except Exception as exc:
        out[f"bb {org}"] = repr(exc)[:150]
for site in ["https://filerschools.org/", "https://www.buhlschools.org/", "https://www.bcsd101.com/board/meeting-schedule", "https://mdsd.org/o/mdsd/page/board-of-trustees"]:
    try:
        r = scan_site(site); out[site] = {k: r.get(k) for k in ("final", "platform", "sched", "pdfs", "error")}
    except Exception as exc:
        out[site] = repr(exc)[:200]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
