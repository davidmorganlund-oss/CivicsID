import json, re, sys, time, html as H
from pathlib import Path
from urllib.parse import urljoin
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build
out = {"libraries": {}, "districts_pages": {}}
listings = set()
for cat in ["public-library", "district-library"]:
    for page in range(1, 25):
        u = f"https://libraries.idaho.gov/idaho-library-directory/categories/{cat}/?_page={page}&sort="
        try:
            h = build.get(u).text
        except Exception:
            break
        found = set(re.findall(r'href="(https://libraries\.idaho\.gov/idaho-library-directory/listing/[^"]+/)"', h))
        if not found - listings and page > 1:
            break
        listings |= found
        time.sleep(0.3)
out["n_listings"] = len(listings)
for u in sorted(listings):
    try:
        h = build.get(u).text
        name = H.unescape((re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S) or [None, ""])[1])
        name = re.sub(r"<[^>]+>|\s+", " ", name).strip()
        text = " ".join(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", h)).split())
        sites = [a for a in re.findall(r'href="(https?://[^"]+)"', h) if not re.search(r"libraries\.idaho\.gov|facebook|twitter|instagram|google|youtube|linkedin|wp\.com|gravatar|w\.org|fonts|cdn", a)]
        city = (re.search(r"([A-Z][A-Za-z .']+),\s*(?:ID|Idaho)\s+8\d{4}", text) or [None, ""])[1]
        out["libraries"][u] = {"name": name, "sites": sites[:3], "city": city.strip()}
        time.sleep(0.2)
    except Exception as exc:
        out["libraries"][u] = {"error": str(exc)[:100]}
for u in ["https://idaho.gov/education/school-districts", "https://www.sde.idaho.gov/schools.html"]:
    try:
        build.check_robots(u); r = build.get(u)
        out["districts_pages"][u] = [(a, re.sub(r"<[^>]+>|\s+", " ", t).strip()[:60]) for a, t in re.findall(r'href="(https?://[^"#]+)"[^>]*>(.*?)</a>', r.text, re.S)][:400]
    except Exception as exc:
        out["districts_pages"][u] = repr(exc)[:200]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print("done", len(listings))
