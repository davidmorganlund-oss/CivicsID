import json, re, requests
from pathlib import Path
h = requests.get("https://www.gemcounty.org/government/county_commissioners/previous_agendas.php", headers={"User-Agent": "CivicsID/0.1"}, timeout=30).text
i = h.find("Commissioner")
out = {"base": re.findall(r"<base[^>]*>", h, re.I), "around": h[max(0, i-400): i+300], "pdf_hrefs": re.findall(r'href=.{0,120}?\.pdf', h, re.I)[:8]}
print(json.dumps(out, indent=1)); Path("probe/report2.json").write_text(json.dumps(out, indent=1))
