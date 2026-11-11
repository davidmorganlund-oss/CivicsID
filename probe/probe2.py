import json, re
from pathlib import Path
import requests
S = requests.Session(); S.headers["User-Agent"] = "CivicsID/0.1 (BarNone nonprofit civic calendar; contact via barnoneinc.org)"
OUT = {}
def get(u, **kw):
    try:
        r = S.get(u, timeout=25, **kw); return r.status_code, r.text
    except Exception as e:
        return 0, f"ERR {e}"[:200]
def text(h):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S | re.I)
    return " ".join(re.sub(r"<[^>]+>", " ", h).split())
c, h = get("https://www.maladidaho.org/wp-json/tribe/events/v1/events", params={"per_page": 50, "start_date": "2026-11-01", "end_date": "2027-01-15"})
try:
    j = json.loads(h); OUT["malad"] = {"status": c, "total": j.get("total"), "events": [(e["start_date"], e["title"], [x["name"] for x in e.get("categories", [])], (e.get("venue") or {}).get("venue") if isinstance(e.get("venue"), dict) else "") for e in j["events"]]}
except Exception as ex:
    OUT["malad"] = {"status": c, "err": str(ex), "head": h[:400]}
c, h = get("https://www.maladidaho.org/wp-json/tribe/events/v1/categories", params={"per_page": 50})
OUT["malad cats"] = h[:3000]
c, h = get("https://maladidaho.org/city-council-calendar/"); OUT["malad council page"] = text(h)[:2500]
c, h = get("https://www.gemcounty.org/government/county_commissioners/agendas_and_minutes.php")
t = text(h); i = t.find("Agenda")
OUT["gem text"] = t[t.find("Board of County Commissioners"):][:3000]
OUT["gem pdfs"] = re.findall(r'href="([^"]+\.pdf)"[^>]*>([^<]*)<', h)[:40]
c, h = get("https://www.cityofemmett.org/meeting-information"); OUT["emmett meeting info"] = text(h)[:3000]
c, h = get("https://www.cityofnezperce.gov/"); OUT["nezperce api"] = sorted(set(re.findall(r'["\'](/api/[^"\']+|https://[^"\']*api[^"\']*)["\']', h)))[:20]
c, h = get("https://www.cityofnezperce.gov/calendar"); OUT["nezperce calendar"] = (c, text(h)[:1500])
for k, v in OUT.items(): print("=" * 8, k); print(json.dumps(v, indent=1)[:3000])
Path("probe/report2.json").write_text(json.dumps(OUT, indent=1))
