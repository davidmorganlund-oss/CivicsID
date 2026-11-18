"""Probe: why do some CivicPlus calendar pages come back empty?"""
import json, re, sys
from datetime import date, timedelta
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, yaml
cfg = yaml.safe_load((Path(__file__).parent / "pipeline" / "sources.yml").read_text())
by = {s["id"]: s for s in cfg["sources"]}
out = {}
start, end = date.today(), date.today() + timedelta(days=60)
for sid in ["kootenai-county", "star", "minidoka-county", "blackfoot", "blackfoot-library", "jerome"]:
    src = by[sid]
    for cat in src["categories"][:3]:
        try:
            r = build.get(src["site"] + "/Calendar.aspx", {"CID": cat, "startDate": start.strftime("%m/%d/%Y"), "endDate": end.strftime("%m/%d/%Y")})
            h = r.text
            i = h.find("eventTitle_")
            out[f"{sid}:{cat}"] = {"url": r.url, "len": len(h), "titles": h.count("eventTitle_"), "starts": h.count('itemprop="startDate"'),
                                   "h2": re.findall(r'<h2[^>]*>([^<]{0,60})</h2>', h)[:6],
                                   "noevents": bool(re.search(r"no events|There are no", h, re.I)),
                                   "snippet": h[max(0, i - 300): i + 1500] if i >= 0 else h[h.find("<ol"): h.find("<ol") + 600]}
        except Exception as exc:
            out[f"{sid}:{cat}"] = {"error": repr(exc)[:300]}
# Sandpoint: is the Municode meetings site open to us?
for u in ["https://meetings.municode.com/robots.txt", "https://www.sandpointidaho.gov/robots.txt"]:
    try:
        import requests
        r = requests.get(u, headers={"User-Agent": build.UA}, timeout=20)
        out[u] = {"status": r.status_code, "text": r.text[:600]}
    except Exception as exc:
        out[u] = {"error": repr(exc)}
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != "snippet"} for k, v in out.items()}, indent=1))
