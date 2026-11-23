"""District round 2: more domain patterns; plus PDF schedules for three districts."""
import io, json, re, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests, pypdf, sweeplib
from sweeplib import scan_site, text
UA = {"User-Agent": build.UA}
miss = json.load(open(Path(__file__).with_name("missing_districts.json")))
def slug(s): return re.sub(r"[^a-z]", "", s.lower())
def guess(r):
    name = r["name"]; city = (r.get("city") or "").title()
    base = re.sub(r"\b(joint|school|district|independent|county|public|schools|no|elementary|unified|isd)\b|#|\d+|\.", " ", name, flags=re.I).split()
    s = slug("".join(base)); first = slug(base[0]) if base else s; c = slug(city)
    nums = []
    cands = []
    for k in {s, first, c}:
        if not k: continue
        cands += [f"https://www.{k}schools.net/", f"https://{k}.k12.id.us/", f"https://www.{k}schools.com/", f"https://www.{k}sd.net/", f"https://www.{k}schooldistrict.com/",
                  f"https://www.{k}schools.us/", f"https://www.{k}sd.us/", f"https://www.{k}.k12.id.us/", f"https://www.{k}schools.org/", f"https://www.{k}sd.org/", f"https://www.{k}district.org/",
                  f"https://www.{k}jsd.org/", f"https://www.{k}school.org/", f"https://{k}.org/"]
    for u in cands:
        try:
            rr = requests.get(u, headers=UA, timeout=8, allow_redirects=True)
            if rr.status_code != 200: continue
            t = text(rr.text[:200000])
            if re.search(r"school", t, re.I) and (city.lower() in t.lower()) and re.search(r"\bIdaho\b|\bID\s*8\d{4}", t):
                return u
        except Exception:
            continue
    return None
def do(r):
    site = guess(r); rec = dict(r)
    if site: rec.update(scan_site(site))
    return rec
with ThreadPoolExecutor(10) as ex:
    res = list(ex.map(do, miss))
pdfs = {}
for k, u in [("mountainview", "https://files.smartsites.parentsquare.com/10900/board_meeting_schedule_2026-2027.pdf"), ("kendrick", "https://content.myconnectsuite.com/api/documents/f732f6045a50474e9b0fb7d5db743e13.pdf"),
             ("kamiah", "https://kamiahsd.org/board-of-trustees/2026-board-meeting-schedule/"), ("bruneau", "https://wsos-cdn.s3.us-west-2.amazonaws.com/uploads/sites/73/NOTICE-OF-SCHEDULE-OF-REGULAR-TUESDAY-MEETINGS-2026-2027-3.docx.pdf")]:
    try:
        build.check_robots(u); rr = requests.get(u, headers=UA, timeout=40)
        if u.endswith(".pdf"):
            pdfs[k] = " ".join(" ".join((p.extract_text() or "") for p in pypdf.PdfReader(io.BytesIO(rr.content)).pages).split())[:2500]
        else:
            pdfs[k] = text(rr.text)[:3000]
    except Exception as exc:
        pdfs[k] = repr(exc)[:200]
Path(__file__).with_name("report2.json").write_text(json.dumps({"districts": res, "pdfs": pdfs}, indent=1))
print("missing", len(miss), "found", sum(1 for r in res if r.get("final")))
