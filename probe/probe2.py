import json, sys
from datetime import date
from zoneinfo import ZoneInfo
from pathlib import Path
sys.path.insert(0, "probe"); import build
src = {"id": "gem-county", "name": "Gem County", "area": "countywide", "county": "Gem",
       "list_url": "https://www.gemcounty.org/government/county_commissioners/previous_agendas.php", "link_match": "Commissioner Agenda"}
ev = build.fetch_pdf_agendas(src, date(2026, 10, 20), date(2026, 12, 31), ZoneInfo("America/Boise"))
out = [(e["start"], e["title"], e.get("highlights"), e["agenda_url"]) for e in ev]
print(json.dumps(out, indent=1)); Path("probe/report2.json").write_text(json.dumps(out, indent=1))
