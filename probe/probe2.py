import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests
out = {}
h = build.get("https://libraries.idaho.gov/idaho-library-directory/listing/aberdeen-district-library/").text
i = h.find("Aberdeen District Library", h.find("<h1"))
out["snip"] = re.sub(r"\s+", " ", h[i:i+6000])
for u in ["https://educationdata.urban.org/api/v1/school-districts/ccd/directory/2022/?fips=16&page=1",
          "https://educationdata.urban.org/api/v1/school-districts/ccd/directory/2021/?fips=16"]:
    try:
        build.check_robots(u); r = requests.get(u, headers={"User-Agent": build.UA}, timeout=60)
        j = r.json(); res = j.get("results", [])
        out[u] = {"count": j.get("count"), "keys": list(res[0].keys()) if res else [], "sample": res[:2]}
    except Exception as exc:
        out[u] = repr(exc)[:300]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print("done")
