"""Probe: why did Jerome's CivicPlus page come back empty today?"""
import json, re, sys
from datetime import date, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build
out = {}
start, end = date.today(), date.today() + timedelta(days=60)
site = "https://www.ci.jerome.id.us"
for label, params in [("range", {"CID": 14, "startDate": start.strftime("%m/%d/%Y"), "endDate": end.strftime("%m/%d/%Y")}),
                      ("month12", {"CID": 14, "month": 12, "year": 2026})]:
    try:
        r = build.get(site + "/Calendar.aspx", params)
        h = r.text
        i = h.find("eventTitle_")
        out[label] = {"status": r.status_code, "url": r.url, "len": len(h), "titles": h.count("eventTitle_"),
                      "grid": "showDetailsBox" in h, "dates": re.findall(r'class="date">([^<]{0,60})', h)[:6],
                      "parsed": [(e["start"], e["title"]) for e in build.normalize_civicplus({"id": "jerome", "name": "Jerome", "area": "Jerome"}, h, ZoneInfo("America/Boise"), site, 14)][:8],
                      "snippet": h[max(0, i - 200): i + 900] if i >= 0 else h[:1500]}
    except Exception as exc:
        out[label] = {"error": repr(exc)[:300]}
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != "snippet"} for k, v in out.items()}, indent=1))
