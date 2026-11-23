import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests
out = {}
for u in ["https://legislature.idaho.gov/feeds/my-calendar-ics/", "https://legislature.idaho.gov/feed/my-calendar-ics/", "https://legislature.idaho.gov/?feed=my-calendar-ics",
          "https://legislature.idaho.gov/my-calendar-ics/", "https://legislature.idaho.gov/calendar/?format=ical", "https://legislature.idaho.gov/calendar/"]:
    try:
        build.check_robots(u); r = requests.get(u, headers={"User-Agent": build.UA}, timeout=40)
        out[u] = f"{r.status_code} {r.headers.get('content-type')} {r.text[:300]!r}"
        if u.endswith("/calendar/"):
            out["cal_links"] = sorted(set(re.findall(r'href="([^"]*(?:ics|ical|feed|my-calendar)[^"]*)"', r.text)))[:20]
            out["mc"] = "my-calendar" in r.text, len(r.text)
    except Exception as exc:
        out[u] = repr(exc)[:200]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
