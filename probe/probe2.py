import json, re, sys, html as H
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests
out = {}
out["robots"] = requests.get("https://www.oakleyidaho.org/robots.txt", headers={"User-Agent": build.UA}, timeout=30).text[:500]
for u in ["https://www.oakleyidaho.org/agendas", "https://www.oakleyidaho.org/calendar-of-events", "https://www.cityofkamiah.org/meeting-agendas-and-minutes", "https://www.duboisidaho.gov/agendas"]:
    try:
        h = build.get(u).text
        body = re.sub(r"(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", h)
        out[u] = {"text": " ".join(H.unescape(re.sub(r"<[^>]+>", " ", body)).split())[:2500],
                  "links": re.findall(r'href="([^"]+)"[^>]*>([^<]{0,80})<', body)[:40],
                  "scripts": [s[:300] for s in re.findall(r"<script[^>]*>(.*?)</script>", h, re.S) if re.search(r"event|agenda|calendar", s, re.I)][:3],
                  "apis": sorted(set(re.findall(r"[\"'](/api/[^\"']+|https://[^\"']*municipalimpact[^\"']*)[\"']", h)))[:15]}
    except Exception as exc:
        out[u] = repr(exc)[:200]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
