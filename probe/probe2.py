"""Probe: run every source's connector (with the robots.txt gate) and report."""
import json, sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, yaml
cfg = yaml.safe_load((Path(__file__).parent / "pipeline" / "sources.yml").read_text())
now = datetime.now(ZoneInfo(cfg["timezone"]))
start, end = now.date(), now.date() + timedelta(days=cfg["window_days"])
out = {}
for src in cfg["sources"]:
    src.setdefault("timezone", cfg["timezone"])
    tz = ZoneInfo(src["timezone"])
    try:
        found = build.CONNECTORS[src["type"]](src, start, end, tz)
        found = [e for e in found if start <= datetime.fromisoformat(e["start"]).date() <= end]
        found = build.apply_source_rules(src, found)
        out[src["id"]] = {"type": src["type"], "count": len(found),
                          "sample": [(e["start"][:16], e["title"][:60], e["url"][:90], e.get("location", "")[:50], e["cancelled"]) for e in found[:4]]}
    except Exception as exc:
        out[src["id"]] = {"type": src["type"], "error": f"{type(exc).__name__}: {exc}"[:300]}
    print(src["id"], out[src["id"]].get("count", out[src["id"]].get("error")), flush=True)
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
