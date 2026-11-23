import json, re, sys
from pathlib import Path
from datetime import date
from zoneinfo import ZoneInfo
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build
out = {}
for site in ["https://www.bonnersferry.id.gov", "https://www.cityofhazelton.com", "https://www.parma.id.gov"]:
    try:
        h = build.get(site + "/AgendaCenter").text
        out[site] = [(cid, re.sub(r"<[^>]+>|\s+", " ", t).strip()[:60], len(re.findall(r'aria-label="Agenda for', body))) for cid, t, body in
                     re.findall(r'id="category-panel-(\d+)".*?<h2[^>]*>(.*?)</h2>(.*?)(?=id="category-panel-|\Z)', h, re.S)]
    except Exception as exc:
        out[site] = repr(exc)[:200]
try:
    ev = build.fetch_civicclerk({"id": "carey", "name": "Carey", "county": "Blaine", "area": "Carey", "tenant": "careyid"}, date(2026, 11, 22), date(2027, 1, 21), ZoneInfo("America/Boise"))
    out["carey"] = [(e["start"][:16], e["title"]) for e in ev[:6]]
except Exception as exc:
    out["carey"] = repr(exc)[:200]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
