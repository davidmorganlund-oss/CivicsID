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
import html as HH
build.check_robots("https://en.wikipedia.org/wiki/List_of_cities_in_Idaho")
wh = requests.get("https://en.wikipedia.org/wiki/List_of_cities_in_Idaho", headers=UA, timeout=60).text
tbl = wh[wh.find('<table class="wikitable'):]
tbl = tbl[:tbl.find('</table>')]
cities = []
for row in re.findall(r"<tr>(.*?)</tr>", tbl, re.S):
    cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.S)
    if len(cells) < 3: continue
    name = HH.unescape(re.sub(r"<[^>]+>", "", cells[0])).strip()
    name = re.sub(r"\[.*?\]|†|\*", "", name).strip()
    county = HH.unescape(re.sub(r"<[^>]+>", "", cells[1] if len(cells) > 1 else "")).strip()
    nums = [int(x.replace(",", "")) for x in re.findall(r"\b\d{1,3}(?:,\d{3})+\b|\b\d{2,6}\b", re.sub(r"<[^>]+>", " ", " ".join(cells[2:4])))]
    if name and not name.lower().startswith("name"):
        cities.append((name, nums[0] if nums else 0, county))
cities.sort(key=lambda x: -x[1])
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
