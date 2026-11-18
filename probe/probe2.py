"""Probe: Blaine County's new site through the CivicPlus reader."""
import json, sys
from datetime import date, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build
src = {"id": "blaine-county", "name": "Blaine County", "area": "countywide", "county": "Blaine",
       "site": "https://www.blainecountyid.gov", "categories": [23, 25, 14], "default_category": "council"}
out = {}
try:
    ev = build.fetch_civicplus(src, date.today(), date.today() + timedelta(days=60), ZoneInfo("America/Boise"))
    out["events"] = [(e["start"][:16], e["end"] and e["end"][11:16], e["title"][:60], e["location"][:50], e["url"]) for e in ev]
except Exception as exc:
    out["error"] = f"{type(exc).__name__}: {exc}"[:400]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1)[:5000])
