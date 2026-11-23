"""Library pass 2: websites from the state library table; scan gently."""
import io, json, re, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests, pypdf
from sweeplib import scan_site
r = requests.get("https://libraries.idaho.gov/files/Table%203%20-%20Idaho%20Public%20Libraries%20by%20Name.pdf", headers={"User-Agent": build.UA}, timeout=60)
txt = "\n".join(p.extract_text() or "" for p in pypdf.PdfReader(io.BytesIO(r.content)).pages)
libs = {}
for line in txt.split("\n"):
    m = re.match(r"^([A-Z][A-Z .'&/-]+?(?:DISTRICT|PUBLIC|LIBRARY|CITY|COMMUNITY|FREE|CO\b)[A-Z .'&/-]*?)\s+[A-Z][a-z]", line)
    if not m: continue
    name = m.group(1).strip()
    city = (re.search(r"([A-Z][A-Z .']+), ID 8\d{3,4}", line) or [None, ""])[1].strip()
    sites = [s for s in re.findall(r"\b([a-z0-9.-]+\.(?:org|us|net|com|gov)(?:/[^\s]*)?)", line) if "@" not in s and not re.search(r"cableone|ida\.net|gmail|yahoo|hotmail|msn|dcdi|imbris|turbonet|smgazette|ctcweb|atcnet|mtida|rtci|safelink|silverstar|custertel|direcway|wildblue|frontier", s)]
    if " - " in name or "BRANCH" in name: continue
    libs.setdefault(name, {"name": name, "city": city, "sites": sites})
def go(rec):
    for s in rec["sites"][:1]:
        try:
            rec.update(scan_site("https://" + s.rstrip("/") + "/"))
        except Exception as exc:
            rec["error"] = str(exc)[:100]
    return rec
with ThreadPoolExecutor(4) as ex:
    res = list(ex.map(go, libs.values()))
Path(__file__).with_name("report2.json").write_text(json.dumps(res, indent=1))
print("libraries", len(res), "with site", sum(1 for x in res if x.get("final")))
