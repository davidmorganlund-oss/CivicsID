"""Probe: CivicPlus calendar-page reader on every CivicPlus source, plus Lewis County robots.txt."""
import json, sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, yaml, requests
cfg = yaml.safe_load((Path(__file__).parent / "pipeline" / "sources.yml").read_text())
now = datetime.now(ZoneInfo(cfg["timezone"]))
start, end = now.date(), now.date() + timedelta(days=cfg["window_days"])
out = {}
for src in cfg["sources"]:
    if src["type"] != "civicplus":
        continue
    src.setdefault("timezone", cfg["timezone"])
    try:
        found = build.CONNECTORS["civicplus"](src, start, end, ZoneInfo(src["timezone"]))
        found = [e for e in found if start <= datetime.fromisoformat(e["start"]).date() <= end]
        found = build.apply_source_rules(src, found)
        out[src["id"]] = {"count": len(found), "last": max([e["start"][:10] for e in found], default=""),
                          "sample": [(e["start"][:16], e["end"] and e["end"][11:16], e["all_day"], e["title"][:50], e["location"][:45], e["cancelled"]) for e in found[:5]]}
    except Exception as exc:
        out[src["id"]] = {"error": f"{type(exc).__name__}: {exc}"[:300]}
    print(src["id"], out[src["id"]].get("count", out[src["id"]].get("error")), out[src["id"]].get("last"), flush=True)
r = requests.get("http://www.lewiscountyid.us/robots.txt", headers={"User-Agent": build.UA}, timeout=20)
out["lewis-robots"] = {"status": r.status_code, "text": r.text[:1500]}
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
