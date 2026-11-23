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

