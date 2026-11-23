import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests
out = {}
H = {"User-Agent": build.UA}
s = requests.Session(); s.headers.update(H)
for site in ["bcsd61"]:
    u = f"https://go.boarddocs.com/id/{site}/Board.nsf/Public"
    r = s.get(u, timeout=45); h = r.text
    out["len"] = len(h)
    out["committee_snips"] = [m[:300] for m in re.findall(r".{0,150}ommittee.{0,150}", h)][:12]
    out["scripts"] = re.findall(r'<script[^>]+src="([^"]+)"', h)[:15]
    out["head"] = h[:1500]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print("done")
