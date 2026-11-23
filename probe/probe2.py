import json, re, sys, html as H
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests
u = "https://en.wikipedia.org/wiki/List_of_cities_in_Idaho"
build.check_robots(u)
h = requests.get(u, headers={"User-Agent": build.UA}, timeout=60).text
out = {}
for tbl in re.findall(r'<table class="wikitable.*?</table>', h, re.S):
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", tbl, re.S):
        cells = [" ".join(H.unescape(re.sub(r"<[^>]+>", " ", c)).split()) for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.S)]
        if len(cells) >= 2:
            out.setdefault("rows", []).append(cells)
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print(len(out.get("rows", [])))
