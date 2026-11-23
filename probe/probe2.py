import json, re, sys
from pathlib import Path
from urllib.parse import urljoin
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build
out = {}
for u in ["https://sde.idaho.gov/ed-directory.html", "https://libraries.idaho.gov/idaho-library-directory/", "https://libraries.idaho.gov/idaho-library-directory/categories/public-library/"]:
    try:
        build.check_robots(u); r = build.get(u); h = r.text
        out[u] = {"len": len(h), "links": [(urljoin(r.url, a), re.sub(r"<[^>]+>|\s+", " ", t).strip()[:60]) for a, t in re.findall(r'href="([^"#]+)"[^>]*>(.*?)</a>', h, re.S)
                  if re.search(r"xls|csv|directory|district|library|json|export|download", a + t, re.I)][:60]}
    except Exception as exc:
        out[u] = repr(exc)[:200]
for u in ["https://libraries.idaho.gov/wp-json/wp/v2/types", "https://libraries.idaho.gov/wp-json/"]:
    try:
        build.check_robots(u); r = build.get(u); out[u] = r.text[:3000]
    except Exception as exc:
        out[u] = repr(exc)[:200]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print("done")
