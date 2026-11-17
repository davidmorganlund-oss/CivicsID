import json, re
from pathlib import Path
from urllib.parse import urljoin
import requests
S = requests.Session(); S.headers["User-Agent"] = "CivicsID/0.1 (BarNone nonprofit civic calendar; contact via barnoneinc.org)"
def get(u):
    try:
        r = S.get(u, timeout=25); return r.status_code, r.url, r.text
    except Exception as e:
        return 0, u, ""
def text(h):
    h = re.sub(r"<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", h, flags=re.S | re.I)
    return " ".join(re.sub(r"<[^>]+>", " ", h).split())
cities = json.load(open("site/data/local.json"))["cities"] if Path("site/data/local.json").exists() else {}
sites = {k: v.get("site") for k, v in cities.items()}
sites.update({"Lewiston": "https://www.cityoflewiston.org/", "Moscow": "https://www.ci.moscow.id.us/"})
OUT = {}
for city, site in sites.items():
    if not site: continue
    c, f, h = get(site)
    cand = []
    for href, label in re.findall(r'href="([^"#]+)"[^>]*>(.*?)</a>', h, re.S):
        lab = " ".join(re.sub(r"<[^>]+>", " ", label).split())
        if re.search(r"mayor|city council|council members|elected officials|meet the council", lab + " " + href, re.I):
            cand.append(urljoin(f, href))
    cand = list(dict.fromkeys(cand))[:4]
    snippets = {}
    for u in cand:
        cc, ff, hh = get(u)
        t = text(hh)
        wins = [t[max(0, m.start() - 60): m.start() + 220] for m in re.finditer(r"Mayor|Council (?:President|Member|Seat|Woman|Man)|Councilmember|Councilor|Seat \d", t)][:14]
        snippets[u] = {"status": cc, "wins": wins}
    OUT[city] = {"status": c, "cands": cand, "snips": snippets}
    print("=====", city, c, cand)
Path("probe/report2.json").write_text(json.dumps(OUT, indent=1))
