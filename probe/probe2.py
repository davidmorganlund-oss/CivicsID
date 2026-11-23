import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests
out = {}
for u in ["https://www.sde.idaho.gov/wp-json/wp/v2/pages?search=directory&per_page=20&_fields=link,title",
          "https://www.sde.idaho.gov/wp-json/wp/v2/media?search=directory&per_page=30&_fields=source_url,title",
          "https://nces.ed.gov/ccd/districtsearch/district_detail.asp?ID2=1600030"]:
    try:
        build.check_robots(u); r = requests.get(u, headers={"User-Agent": build.UA}, timeout=60)
        t = r.text
        out[u] = t[:3000] if "nces" not in u else re.findall(r".{0,200}[Ww]ebsite.{0,300}", t)[:3]
    except Exception as exc:
        out[u] = repr(exc)[:300]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
