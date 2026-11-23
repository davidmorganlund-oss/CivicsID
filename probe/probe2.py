"""City sweep round 2: more domain patterns for cities not found."""
import json, re, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests, sweeplib
from sweeplib import scan_site, text
sweeplib.SCHED = re.compile(r"[^.]{0,200}(?:council (?:meets|will meet|holds|meetings? (?:are|is) held)|regular(?:ly)? (?:scheduled )?(?:city )?(?:council |commission )?meetings? (?:are|is|will be) (?:held|scheduled)|meets? (?:on )?the (?:first|second|third|fourth|last|1st|2nd|3rd|4th)|(?:first|second|third|fourth|last|1st|2nd|3rd|4th)(?: and (?:first|second|third|fourth|last|1st|2nd|3rd|4th))? (?:Monday|Tuesday|Wednesday|Thursday|Friday)s? of (?:each|every|the) month)[^.]{0,220}\.", re.I)
UA = {"User-Agent": build.UA}
miss = json.load(open(Path(__file__).with_name("missing_cities.json")))
def slug(s): return re.sub(r"[^a-z]", "", s.lower())
def guess(name):
    s = slug(name); h = re.sub(r"[^a-z]+", "-", name.lower()).strip("-")
    cands = [f"https://{s}.municipalimpact.com/", f"https://www.{s}.id.gov/", f"https://{s}.idaho.gov/", f"https://www.cityof{s}idaho.com/", f"https://www.{s}idaho.com/",
             f"https://www.cityof{s}.net/", f"https://www.{s}.net/", f"https://www.{s}city.com/", f"https://www.cityof{h}.org/", f"https://www.{s}id.us/",
             f"https://www.cityof{s}id.com/", f"https://www.{s}idaho.net/", f"https://www.townof{s}.org/", f"https://www.{s}.com/", f"https://www.cityof{s}.gov/"]
    for c in cands:
        try:
            rr = requests.get(c, headers=UA, timeout=8, allow_redirects=True)
            if rr.status_code != 200: continue
            t = text(rr.text[:200000])
            if re.search(rf"\b(city|town) of {re.escape(name)}\b", t, re.I) and re.search(r"\bIdaho\b|\bID\s*8\d{4}", t):
                return c
        except Exception:
            continue
    return None
def do(name):
    site = guess(name); rec = {"name": name}
    if site: rec.update(scan_site(site))
    return rec
with ThreadPoolExecutor(10) as ex:
    res = list(ex.map(do, miss))
Path(__file__).with_name("report2.json").write_text(json.dumps(res, indent=1))
print("missing", len(miss), "found", sum(1 for r in res if r.get("final")))
