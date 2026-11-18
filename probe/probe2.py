"""Probe: Blackfoot Agenda Center categories, and Lewis County robots/page."""
import json, re, sys
from datetime import date
from pathlib import Path
from zoneinfo import ZoneInfo
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests
out = {}
try:
    h = build.get("https://www.cityofblackfoot.org/AgendaCenter").text
    out["blackfoot-cats"] = re.findall(r'id="cat(\d+)"[^>]*>\s*<h2[^>]*>(.*?)</h2>', h, re.S)[:20] or re.findall(r'id="cat(\d+)".{0,300}', h, re.S)[:5]
    for cat, name in out["blackfoot-cats"][:12] if isinstance(out["blackfoot-cats"][0], tuple) else []:
        src = {"id": "bf", "name": "Blackfoot", "area": "Blackfoot", "site": "https://www.cityofblackfoot.org", "category": int(cat)}
        ev = build.normalize_agendacenter(src, h, ZoneInfo("America/Boise"))
        out[f"bf-{cat}"] = [(e["start"][:16], e["title"][:60]) for e in ev if e["start"][:10] >= date.today().isoformat()][:5]
except Exception as exc:
    out["blackfoot-error"] = repr(exc)[:300]
for u in ["https://www.lewiscountyid.us/robots.txt", "http://www.lewiscountyid.us/robots.txt", "https://lewiscountyid.us/robots.txt"]:
    try:
        r = requests.get(u, headers={"User-Agent": build.UA}, timeout=45)
        out[u] = {"status": r.status_code, "type": r.headers.get("Content-Type"), "text": r.text[:800]}
    except Exception as exc:
        out[u] = {"error": repr(exc)[:200]}
build._robots_cache.clear()
for u in ["http://www.lewiscountyid.us/Elected-Officials/Commissioners/Meeting-Agendas"]:
    try:
        build.check_robots(u); out["lewis-check"] = "allowed"
    except Exception as exc:
        out["lewis-check"] = repr(exc)[:300]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1)[:4000])
