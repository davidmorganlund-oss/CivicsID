"""Probe: Idaho library districts - board schedules and event platforms."""
import json, re, sys
from pathlib import Path
from urllib.parse import urljoin
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build
L = {
 "Meridian Library District": ["https://www.mld.org/"], "Nampa Public Library": ["https://www.nampalibrary.org/"],
 "Caldwell Public Library": ["https://www.caldwellpubliclibrary.org/", "https://library.cityofcaldwell.org/"],
 "Idaho Falls Public Library": ["https://www.ifpl.org/"], "Eagle Public Library": ["https://www.eaglepubliclibrary.org/"],
 "Garden City Public Library": ["https://www.gardencitylibrary.org/"], "Kuna Library District": ["https://www.kunalibrary.org/"],
 "Madison Library District": ["https://www.madisonlib.org/"], "Portneuf District Library": ["https://www.portneuflibrary.org/"],
 "Lewiston City Library": ["https://www.lewistonlibrary.org/", "https://www.cityoflewiston.org/library"],
 "Mountain Home Public Library": ["https://www.mhlibrary.org/", "https://mhpl.org/"], "The Community Library (Ketchum)": ["https://www.comlib.org/"],
 "Hailey Public Library": ["https://www.haileypubliclibrary.org/"], "Jerome Public Library": ["https://www.jeromepubliclibrary.org/", "https://jerome.lib.id.us/"],
 "Blackfoot Public Library": ["https://www.blackfootlibrary.org/", "https://www.blackfootpubliclibrary.org/"],
 "Emmett Public Library": ["https://www.emmettpubliclibrary.org/", "https://emmettlibrary.org/"],
 "Burley Public Library": ["https://www.burleypubliclibrary.org/", "https://burley.lib.id.us/"],
 "Rupert DL Evans Bicknell": ["https://www.rupertlibrary.org/"], "Star Library": ["https://www.starlibrary.org/"],
 "Bonneville County Library District": ["https://www.bonnevillelibrary.org/", "https://bclid.org/"],
 "Payette Public Library": ["https://www.payettepubliclibrary.org/"], "Weiser Public Library": ["https://www.weiserlibrary.org/"],
 "Salmon Public Library": ["https://www.salmonpubliclibrary.org/"], "Sandpoint (East Bonner)": [],
}
PLAT = {"libcal": r"libcal\.com", "bibliocommons": r"bibliocommons", "communico": r"communico|libraryc\.org", "librarymarket": r"librarymarket|lm-events",
        "assabet": r"assabetinteractive|libraryinsight", "tribe": r"tribe-events|/wp-json/tribe", "mec": r"modern-events-calendar|mec-", "wordpress": r"wp-content",
        "evanced": r"evanced|spaces\.evanced", "boardbook": r"boardbook", "simbli": r"simbli"}
out = {}
for name, urls in L.items():
    rec = []
    for u in urls:
        r = {"url": u}
        try:
            build.check_robots(u); resp = build.get(u); h = resp.text
            r["final"] = resp.url
            r["platform"] = [k for k, v in PLAT.items() if re.search(v, h, re.I)]
            links = []
            for href, txt in re.findall(r'href="([^"#]+)"[^>]*>(.*?)</a>', h, re.S | re.I):
                t = re.sub(r"<[^>]+>|\s+", " ", txt).strip()
                if re.search(r"board|trustee|agenda|governance|about", t + " " + href, re.I):
                    a = urljoin(resp.url, href.replace("&amp;", "&"))
                    if a not in links: links.append(a)
            r["links"] = links[:8]
            for a in links[:5]:
                try:
                    build.check_robots(a); hh = build.get(a).text
                    txt = " ".join(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", hh)).split())
                    s = re.findall(r"[^.]{0,160}(?:board (?:of trustees )?meets|regular(?:ly)? (?:board )?meetings?|meets? (?:on )?the (?:first|second|third|fourth|last|1st|2nd|3rd|4th)|meetings are held)[^.]{0,200}\.", txt, re.I)[:3]
                    if s: r.setdefault("sched", []).append({a: s})
                except Exception as exc:
                    pass
            rec.append(r); break
        except Exception as exc:
            r["error"] = (type(exc).__name__ + ": " + str(exc))[:120]; rec.append(r)
    out[name] = rec
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print("done")
