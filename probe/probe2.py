import json, sys
from pathlib import Path
sys.path.insert(0, "probe"); import checks
checks.SITE = Path("site")
urls = checks.site_links()
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=12) as pool:
    res = list(pool.map(checks.check, urls))
bad = [r for r in res if r[1] not in (200,) ]
Path("probe/report2.json").write_text(json.dumps({"n": len(urls), "bad": bad}, indent=1))
print(len(urls), len(bad))
