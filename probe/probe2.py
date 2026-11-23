import json, re, sys
from pathlib import Path
from datetime import date
from zoneinfo import ZoneInfo
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build
out = {}
for name, home in [("nampa", "https://nampalibrary.org/"), ("kuna", "https://kunalibrary.org/"), ("mtnhome", "https://mhlibrary.org/"), ("comlib", "https://comlib.org/")]:
    try:
        h = build.get(home).text
        hosts = sorted(set(re.findall(r"([a-z0-9-]+\.libcal\.com)", h)))
        out[name] = {"hosts": hosts}
        for host in hosts[:1]:
            try:
                ev = build.fetch_libcal({"id": name, "name": name, "county": "X", "area": "X", "host": host, "civic_only": True}, date(2026, 11, 22), date(2027, 1, 21), ZoneInfo("America/Boise"))
                out[name]["civic"] = [(e["start"][:16], e["title"][:60]) for e in ev[:8]]
                out[name]["n"] = len(ev)
            except Exception as exc:
                out[name]["err"] = repr(exc)[:200]
    except Exception as exc:
        out[name] = repr(exc)[:200]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print("done")
