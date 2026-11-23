"""Sweep: every Idaho school district and public library - find site, platform, stated board schedule."""
import json, re, sys, html as H
from pathlib import Path
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests
build.TIMEOUT = 20
UA = {"User-Agent": build.UA}

def fetch(u):
    build.check_robots(u)
    r = requests.get(u, headers=UA, timeout=20, allow_redirects=True)
    r.raise_for_status()
    return r

def text(h):
    h = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", h)
    return " ".join(H.unescape(re.sub(r"<[^>]+>", " ", h)).split())

PLAT = {"simbli": r"simbli\.eboardsolutions\.com/[^\"' ]*?[Ss]=(\d{8})", "boardbook": r"meetings\.boardbook\.org/Public/Organization/(\d+)",
        "libcal": r"([a-z0-9-]+\.libcal\.com)", "tyler": r"([a-z0-9-]+\.meetingmanager\.tylerapp\.com/[a-z0-9]+)", "agendacenter": r"/(AgendaCenter)\b",
        "civicclerk": r"([a-z0-9-]+)\.portal\.civicclerk\.com", "diligent": r"([a-z0-9-]+\.community\.(?:highbond|diligentoneplatform)\.com)",
        "bibliocommons": r"([a-z0-9-]+)\.bibliocommons\.com", "tribe": r"(tribe-events)", "mec": r"(modern-events-calendar)"}
SCHED = re.compile(r"[^.]{0,200}(?:board (?:of (?:trustees|directors) )?(?:meets|will meet|holds)|regular(?:ly)? (?:scheduled )?(?:board |monthly )?meetings? (?:are|is|will be) (?:held|scheduled)|meets? (?:on )?the (?:first|second|third|fourth|last|1st|2nd|3rd|4th)|meetings are held (?:on )?the|(?:first|second|third|fourth|last|1st|2nd|3rd|4th) (?:Monday|Tuesday|Wednesday|Thursday|Friday) of (?:each|every|the) month)[^.]{0,220}\.", re.I)

def scan_site(home):
    rec = {"site": home, "platform": {}, "sched": [], "pdfs": [], "pages": []}
    try:
        r = fetch(home)
    except Exception as exc:
        rec["error"] = (type(exc).__name__ + ": " + str(exc))[:120]; return rec
    rec["final"] = r.url; rec["title"] = text((re.search(r"<title[^>]*>(.*?)</title>", r.text, re.S | re.I) or [None, ""])[1])[:90]
    pages = [(r.url, r.text)]
    links = []
    for a, t in re.findall(r'href="([^"#]+)"[^>]*>(.*?)</a>', r.text, re.S | re.I):
        tt = text(t)
        if re.search(r"board|trustee|agenda|meeting|governance|about", tt + " " + a, re.I) and not re.search(r"\.(jpg|png|css|js)$|mailto:|tel:|facebook|twitter|instagram|youtube", a, re.I):
            u = urljoin(r.url, H.unescape(a))
            if urlparse(u).netloc.replace("www.", "") == urlparse(r.url).netloc.replace("www.", "") and u not in links:
                links.append(u)
    links.sort(key=lambda u: 0 if re.search(r"board|trustee", u, re.I) else 1)
    for u in links[:7]:
        try:
            rr = fetch(u)
            if "html" in rr.headers.get("content-type", ""):
                pages.append((rr.url, rr.text)); rec["pages"].append(rr.url)
        except Exception:
            pass
    for u, h in pages:
        for k, v in PLAT.items():
            for m in re.findall(v, h, re.I):
                rec["platform"].setdefault(k, [])
                if m not in rec["platform"][k]: rec["platform"][k].append(m)
        for s in SCHED.findall(text(h)):
            s = s.strip()
            if s not in [x[1] for x in rec["sched"]] and len(rec["sched"]) < 8:
                rec["sched"].append([u, s[:420]])
        for a, t in re.findall(r'href="([^"]+)"[^>]*>(.*?)</a>', h, re.S | re.I):
            tt = text(t)
            if re.search(r"schedule|calendar", tt + a, re.I) and re.search(r"board|meeting", tt + a, re.I) and re.search(r"202[67]", tt + a):
                x = [urljoin(u, H.unescape(a)), tt[:80]]
                if x not in rec["pdfs"] and len(rec["pdfs"]) < 5: rec["pdfs"].append(x)
    return rec

def slug(s): return re.sub(r"[^a-z]", "", s.lower())

# ---- school districts from NCES (regular districts) ----
rows = []
for page in range(1, 5):
    j = requests.get(f"https://educationdata.urban.org/api/v1/school-districts/ccd/directory/2022/?fips=16&page={page}", headers=UA, timeout=60).json()
    rows += j.get("results", [])
    if not j.get("next"): break
districts = [r for r in rows if r.get("agency_type") in (1, 2) and r.get("agency_charter_indicator") != 1]

def guess_district(r):
    name = r["lea_name"]; num = (re.search(r"(\d{1,3})\s*$", name) or re.search(r"#\s*(\d+)", name) or [None, ""])[1]
    if not num:
        num = re.sub(r"\D", "", r.get("state_leaid", ""))[-3:].lstrip("0")
    base = re.sub(r"\b(joint|school|district|independent|county|public|schools|no|elementary|unified)\b|#|\d+", " ", name, flags=re.I)
    s = slug(base)
    first = slug(base.split()[0]) if base.split() else s
    cands = [f"https://www.sd{num}.org/", f"https://www.sd{num}.us/", f"https://www.sd{num}.k12.id.us/", f"https://www.d{num}.k12.id.us/", f"https://www.{s}sd.org/",
             f"https://www.{s}schools.org/", f"https://www.{s}.k12.id.us/", f"https://www.{s}sd{num}.org/", f"https://www.{s}{num}.org/", f"https://www.{first}sd.org/",
             f"https://www.{first}schools.org/", f"https://www.{s}.org/", f"https://www.{s}district.org/", f"https://www.district{num}.org/", f"https://www.{first}.k12.id.us/",
             f"https://www.{s}schooldistrict.org/", f"https://www.{s}.us/"]
    city = (r.get("city_location") or "").title()
    for c in cands:
        try:
            rr = requests.get(c, headers=UA, timeout=8, allow_redirects=True)
            if rr.status_code != 200: continue
            t = text(rr.text[:200000])
            if (num and re.search(rf"(?:#|No\.?\s*|District\s*|SD\s*|D)\s*{num}\b", t, re.I)) and (re.search(r"\bID\b|Idaho", t) or city.lower() in t.lower()):
                return c
            if city and city.lower() in t.lower() and re.search(r"\bID\s*8\d{4}|Idaho", t) and re.search(r"school", t, re.I):
                return c
        except Exception:
            continue
    return None

def do_district(r):
    site = guess_district(r)
    rec = {"name": r["lea_name"], "city": r.get("city_location"), "county": r.get("county_name"), "enrollment": r.get("enrollment"), "leaid": r.get("leaid")}
    if site: rec.update(scan_site(site))
    return rec

# ---- libraries from ICfL directory ----
def lib_listings():
    seen = set()
    for cat in ["public-library", "district-library"]:
        for page in range(1, 25):
            h = requests.get(f"https://libraries.idaho.gov/idaho-library-directory/categories/{cat}/?_page={page}&sort=", headers=UA, timeout=30).text
            f = set(re.findall(r'href="(https://libraries\.idaho\.gov/idaho-library-directory/listing/[^"]+/)"', h))
            if not f - seen and page > 1: break
            seen |= f
    return sorted(seen)

def do_library(u):
    h = requests.get(u, headers=UA, timeout=30).text
    name = text((re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S) or [None, ""])[1])
    t = text(h)
    county = (re.search(r"/locations/([a-z-]+)-county/", h) or [None, ""])[1].replace("-", " ").title()
    city = (re.search(r"([A-Z][A-Za-z .']+),\s*(?:ID|Idaho)\s+8\d{4}", t) or [None, ""])[1].strip()
    sites = [a for a, x in re.findall(r'href="(https?://[^"]+)"[^>]*>\s*(https?://[^<]+?)\s*<', h) if a.rstrip("/") == x.strip().rstrip("/")]
    rec = {"name": name, "county": county, "city": city, "listing": u}
    if sites: rec.update(scan_site(sites[0]))
    return rec

out = {}
with ThreadPoolExecutor(12) as ex:
    out["districts"] = list(ex.map(do_district, districts))
    out["libraries"] = list(ex.map(do_library, lib_listings()))
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print("districts", len(out["districts"]), "found", sum(1 for d in out["districts"] if d.get("site")), "libraries", len(out["libraries"]))
