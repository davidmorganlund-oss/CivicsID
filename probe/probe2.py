"""Probe: Idaho school district board meeting systems."""
import json, re, sys
from pathlib import Path
from urllib.parse import urljoin
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build
D = {
 "Bonneville 93": ["https://www.d93schools.org/"], "Vallivue 139": ["https://www.vallivue.org/"],
 "Kuna 3": ["https://www.kunaschools.org/"], "Twin Falls 411": ["https://www.tfsd.org/"],
 "Caldwell 132": ["https://www.caldwellschools.org/"], "Madison 321": ["https://www.msd321.com/"],
 "Lakeland 272": ["https://www.lakelandsd.org/"], "Post Falls 273": ["https://www.pfsd.com/"],
 "Middleton 134": ["https://www.msd134.org/"], "Jefferson 251": ["https://www.sd251.org/"],
 "Blackfoot 55": ["https://www.d55.k12.id.us/", "https://www.blackfootschools.org/"], "Minidoka 331": ["https://www.minidokaschools.org/", "https://www.msd331.org/"],
 "Cassia 151": ["https://www.cassiaschools.org/"], "Lake Pend Oreille 84": ["https://www.lposd.org/", "https://www.lposchools.org/"],
 "Mountain Home 193": ["https://www.mhsd193.org/"], "Jerome 261": ["https://www.jeromeschools.org/"],
 "Emmett 221": ["https://www.emmettschools.org/"], "Moscow 281": ["https://www.msd281.org/"],
 "Lewiston 340": ["https://www.lewistonschools.net/"], "Blaine 61": ["https://www.blaineschools.org/"],
 "Kimberly 414": ["https://www.kimberly.edu/"], "Fremont 215": ["https://www.sd215.net/"],
 "Snake River 52": ["https://www.snakeriver.org/"], "Shelley 60": ["https://www.shelleyschools.org/"],
 "Rigby/Jefferson alt": [], "Preston 201": ["https://www.prestonschools.org/"], "Gooding 231": ["https://www.goodingschools.org/"],
 "Bonners Ferry 101": ["https://www.bcsd101.com/"], "Sugar-Salem 322": ["https://www.sugarsalem.com/"],
}
PLAT = {"simbli": r"simbli\.eboardsolutions\.com[^\"' ]*S=\d+", "boardbook": r"meetings\.boardbook\.org/Public/Organization/\d+",
        "boarddocs": r"go\.boarddocs\.com/[^\"' ]+", "apptegy": r"thrillshare|apptegy", "finalsite": r"finalsite", "edlio": r"edlio",
        "civicplus": r"AgendaCenter", "diligent": r"diligent|highbond", "bbloomerang": r"blackboard|schoolmessenger|bbk12", "wordpress": r"wp-content",
        "meetingmanager": r"meetingmanager|tylerapp", "granicus": r"granicus|iqm2", "escribe": r"escribemeetings"}
def scan(h):
    found = {}
    for k, v in PLAT.items():
        m = re.findall(v, h, re.I)
        if m: found[k] = sorted(set(m))[:4]
    return found
out = {}
for name, urls in D.items():
    rec = []
    for u in urls:
        r = {"url": u}
        try:
            build.check_robots(u)
            resp = build.get(u); h = resp.text
            r["final"] = resp.url; r["platform"] = scan(h)
            board = []
            for href, txt in re.findall(r'href="([^"#]+)"[^>]*>(.*?)</a>', h, re.S | re.I):
                t = re.sub(r"<[^>]+>|\s+", " ", txt).strip()
                if re.search(r"board|trustee|agenda|meeting", t + " " + href, re.I):
                    a = urljoin(resp.url, href.replace("&amp;", "&"))
                    if a not in board: board.append(a)
            r["board_links"] = board[:10]
            for a in board[:4]:
                if re.search(r"simbli|boardbook|boarddocs", a): continue
                try:
                    build.check_robots(a); hh = build.get(a).text
                    f = scan(hh)
                    txt = " ".join(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", hh)).split())
                    sched = re.findall(r"[^.]{0,120}(?:regular(?:ly)? (?:board )?meetings?|board meets|meets on)[^.]{0,160}\.", txt, re.I)[:3]
                    r.setdefault("sub", []).append({"url": a, "platform": {k: v for k, v in f.items() if k in ("simbli", "boardbook", "boarddocs", "meetingmanager", "granicus", "escribe", "diligent")}, "sched": sched})
                except Exception as exc:
                    r.setdefault("sub", []).append({"url": a, "error": str(exc)[:100]})
            rec.append(r); break
        except Exception as exc:
            r["error"] = (type(exc).__name__ + ": " + str(exc))[:150]; rec.append(r)
    out[name] = rec
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print("done")
