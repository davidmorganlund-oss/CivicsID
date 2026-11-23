import json, re, sys
from pathlib import Path
from urllib.parse import urljoin
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build
out = {}
for home in ["https://www.cityofkamiah.org/", "https://www.oakleyidaho.org/", "https://www.duboisidaho.gov/"]:
    try:
        h = build.get(home).text
        out[home] = {"gen": re.findall(r'<meta[^>]+generator[^>]+>', h)[:3], "powered": re.findall(r"[Pp]owered by[^<]{0,80}|catalis|govoffice|municipalimpact|revize|civicplus|thrillshare|apptegy|edlio|wix|squarespace|govstack|granicus|vision|govpilot|seamlessdocs", h)[:6],
                     "links": sorted({urljoin(home, a) for a in re.findall(r'href="([^"#]+)"', h) if re.search(r"agenda|meeting|calendar|event|council|feed|ics|rss", a, re.I)})[:25]}
    except Exception as exc:
        out[home] = repr(exc)[:200]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
