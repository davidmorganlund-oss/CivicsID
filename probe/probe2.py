import json, re
from pathlib import Path
from urllib.parse import urljoin
import requests
S = requests.Session(); S.headers["User-Agent"] = "CivicsID/0.1 (BarNone nonprofit civic calendar; contact via barnoneinc.org)"
def get(u):
    try:
        r = S.get(u, timeout=25); return r.status_code, r.url, r.text
    except Exception:
        return 0, u, ""
def text(h):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S | re.I)
    return " ".join(re.sub(r"<[^>]+>", " ", h).split())
sites = {"Idaho Falls": "https://www.idahofallsidaho.gov/", "Pocatello": "https://www.pocatello.gov/", "Kuna": "https://www.kunacity.id.gov/",
         "Lewiston": "https://www.cityoflewiston.org/", "McCall": "https://www.mccall.id.us/", "Moscow": "https://www.ci.moscow.id.us/",
         "Mountain Home": "https://www.mountain-home.us/", "Rexburg": "https://www.rexburg.org/", "Star": "https://www.staridaho.org/",
         "Twin Falls": "https://www.tfid.org/", "Hailey": "https://haileycityhall.org/", "Dalton Gardens": "https://daltongardens.com/",
         "Meridian": "https://meridiancity.org/mayors-office/meet-mayor/"}
extra = {"Idaho Falls": ["/193/Mayor", "/Directory.aspx?DID=4"], "Pocatello": ["/162/Mayor", "/193/Mayors-Office"], "Twin Falls": ["/152/City-Council", "/158/Mayor"],
         "Moscow": ["/167/Mayor", "/170/City-Council"], "Lewiston": ["/220/City-Council", "/158/Mayor"], "Star": ["/150/Mayor", "/149/City-Council"],
         "Mountain Home": ["/166/City-Council", "/167/Mayor"], "McCall": ["/government/mayor_and_city_council/index.php", "/government/city_council/index.php"],
         "Rexburg": ["/page/mayor", "/page/city-council"], "Kuna": ["/government/mayor_and_city_council/index.php"], "Hailey": ["/mayor/", "/boards-and-commissions/city-council/"],
         "Dalton Gardens": ["/mayor", "/citycouncil"]}
OUT = {}
for city, site in sites.items():
    c, f, h = get(site)
    cand = [urljoin(f, href) for href, lab in re.findall(r'href="([^"#]+)"[^>]*>(.*?)</a>', h, re.S)
            if re.search(r"mayor|council", re.sub(r"<[^>]+>", " ", lab) + href, re.I) and "Calendar.aspx" not in href and "CivicAlerts" not in href]
    cand = list(dict.fromkeys(cand + [urljoin(f or site, x) for x in extra.get(city, [])]))[:7]
    res = {}
    for u in cand:
        cc, ff, hh = get(u)
        t = text(hh)
        title = (re.findall(r"<title[^>]*>(.*?)</title>", hh, re.S) or [""])[0].strip()[:80]
        names = re.findall(r"Mayor\s+([A-Z][a-z]+(?:\s+[A-Z]\.?)?\s+[A-Z][A-Za-z'’-]+)", t)
        ctx = [t[max(0, m.start() - 80): m.start() + 200] for m in re.finditer(r"Mayor\s+[A-Z][a-z]+\s+[A-Z]", t)][:2]
        res[u] = {"status": cc, "title": title, "names": sorted(set(names))[:6], "ctx": ctx}
    OUT[city] = {"status": c, "pages": res}
    print("=====", city, c)
    for u, r in res.items(): print("  ", r["status"], u, r["title"][:50], r["names"][:4])
Path("probe/report2.json").write_text(json.dumps(OUT, indent=1))
