"""City sweep: every incorporated Idaho city - find site, platform, stated council schedule."""
import json, re, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests
import sweeplib
from sweeplib import scan_site, text
sweeplib.SCHED = re.compile(r"[^.]{0,200}(?:council (?:meets|will meet|holds|meetings? (?:are|is) held)|regular(?:ly)? (?:scheduled )?(?:city )?(?:council |commission )?meetings? (?:are|is|will be) (?:held|scheduled)|meets? (?:on )?the (?:first|second|third|fourth|last|1st|2nd|3rd|4th)|(?:first|second|third|fourth|last|1st|2nd|3rd|4th)(?: and (?:first|second|third|fourth|last|1st|2nd|3rd|4th))? (?:Monday|Tuesday|Wednesday|Thursday|Friday)s? of (?:each|every|the) month)[^.]{0,220}\.", re.I)
UA = {"User-Agent": build.UA}
gz = "https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2023_Gazetteer/2023_gaz_place_16.txt"
build.check_robots(gz)
lines = requests.get(gz, headers=UA, timeout=60).text.splitlines()
hdr = lines[0].split("\t")
cities = []
for ln in lines[1:]:
    f = dict(zip([h.strip() for h in hdr], ln.split("\t")))
    n = f.get("NAME", "")
    if n.endswith(" city"):
        cities.append((n[:-5].replace("Boise City", "Boise"), float(f.get("ALAND_SQMI", 0) or 0), ""))
print("cities parsed", len(cities), cities[:3])
def slug(s): return re.sub(r"[^a-z]", "", s.lower())
def guess(name):
    s = slug(name)
    cands = [f"https://{s}.id.gov/", f"https://www.cityof{s}.org/", f"https://www.cityof{s}.com/", f"https://www.{s}idaho.gov/", f"https://www.{s}idaho.org/", f"https://www.{s}idaho.us/",
             f"https://www.cityof{s}.us/", f"https://www.ci.{s}.id.us/", f"https://www.{s}.org/", f"https://www.{s}id.gov/", f"https://www.cityof{s}id.org/", f"https://www.{s}city.org/",
             f"https://www.cityof{s}idaho.org/", f"https://www.{s}id.org/", f"https://www.{s}.id.us/", f"https://www.{s}.us/"]
    for c in cands:
        try:
            rr = requests.get(c, headers=UA, timeout=8, allow_redirects=True)
            if rr.status_code != 200: continue
            t = text(rr.text[:200000])
            if re.search(rf"\b{re.escape(name)}\b", t, re.I) and re.search(r"\bIdaho\b|\bID\s*8\d{4}", t) and re.search(r"city|council|mayor", t, re.I):
                return c
        except Exception:
            continue
    return None
def do(c):
    name, pop, county = c
    site = guess(name)
    rec = {"name": name, "pop": pop, "county": county}
    if site: rec.update(scan_site(site))
    return rec
with ThreadPoolExecutor(10) as ex:
    res = list(ex.map(do, cities))
Path(__file__).with_name("report2.json").write_text(json.dumps(res, indent=1))
print("cities", len(res), "found", sum(1 for r in res if r.get("final")))
