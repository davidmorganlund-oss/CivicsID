"""Probe 2: meeting schedules and mayors on 18 Idaho city pages."""
import json, re, sys, html as H
from pathlib import Path
from datetime import date, timedelta
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build
PAGES = {
 "Middleton": ["https://middleton.id.gov/departments/city-council", "https://middleton.id.gov/public-meetings", "https://middleton.id.gov/city-government/elected-officials", "https://middleton.id.gov/departments/planning-zoning"],
 "Payette": ["https://cityofpayette.com/index.asp?SEC=3E868623-D11C-4F30-A389-C51A121FB9A7&Type=B_BASIC", "https://cityofpayette.com/index.asp?SEC=EC229BCB-6752-46F1-A3D6-8AE9E7492111&Type=B_BASIC", "https://cityofpayette.com/index.asp?SEC=FC3FE281-A929-4014-A2B8-A405AF79FB7D&Type=B_BASIC", "https://cityofpayette.com/index.asp?SEC=16FAD3A1-7F4A-4474-A68C-E88153492ED6&Type=B_BASIC"],
 "Fruitland": ["https://www.fruitland.org/council", "https://www.fruitland.org/index.asp?SEC=116126E2-E6E0-4AE0-9EEE-9157CD7F70D5", "https://www.fruitland.org/council-agendas", "https://www.fruitland.org/planning-zoning"],
 "Rupert": ["https://rupert-idaho.com/news/council-meeting-schedule", "https://rupert-idaho.com/government", "https://rupert-idaho.com/government/agendas-minutes"],
 "Weiser": ["https://www.cityofweiser.net/agendas", "https://www.cityofweiser.net/city-council-members", "https://www.cityofweiser.net/mayors-corner", "https://www.cityofweiser.net/planning-zoning-commission"],
 "Preston": ["https://www.prestonidaho.net/government/mayor___city_council/index.php", "https://www.prestonidaho.net/government/mayor___city_council/council_meeting_agendas___minutes.php", "https://www.prestonidaho.net/government/planning___zoning/index.php"],
 "Rigby": ["https://cityofrigby.gov/mayor-and-city-council/", "https://cityofrigby.gov/city-council-agendas/", "https://cityofrigby.gov/planning-and-zoning-commission/"],
 "Kimberly": ["https://www.cityofkimberly.org/AgendaCenter", "https://www.cityofkimberly.org/27/Government", "https://www.cityofkimberly.org/Directory.aspx"],
 "Shelley": ["https://cityofshelley.org/meetings/", "https://cityofshelley.org/", "https://cityofshelley.org/city-departments/planning-and-zoning/"],
 "American Falls": ["https://americanfallsid.gov/mayor-and-council/", "https://americanfallsid.gov/planning-and-zoning/", "https://americanfallsid.gov/"],
 "Buhl": ["https://www.cityofbuhl.us/city-council.html", "https://www.cityofbuhl.us/mayor.html", "https://www.cityofbuhl.us/council-meeting-documents.html", "https://www.cityofbuhl.us/planning--zoning-commission-meetings.html"],
 "St. Anthony": ["https://www.cityofstanthony.org/page/city-council", "https://stanthony.municipalcodeonline.com/"],
 "Gooding": ["https://www.goodingidaho.org/pages/elected-officials", "https://www.goodingidaho.org/agendas", "https://www.goodingidaho.org/pages/city-info"],
 "Heyburn": ["https://heyburn.id.gov/index.asp?SEC=3231C763-F07B-4646-AF04-ABF4316E02E6", "https://heyburn.id.gov/government", "https://heyburn.id.gov/agendas", "https://heyburn.id.gov/index.asp?SEC=CED04F24-BC21-4DD9-84F1-BB7EDE4F2910"],
 "Grangeville": ["https://grangeville.us/mayor-and-city-council/", "https://grangeville.us/city-council-agendas/", "https://grangeville.us/mayor-and-city-council/planning-and-zoning-commission/"],
 "Orofino": ["https://cityoforofino.org/"],
 "Salmon": ["https://www.cityofsalmon.com/page/mayor-and-council", "https://www.cityofsalmon.com/page/meeting-schedules", "https://www.cityofsalmon.com/documents/city-council-meeting-agendas/23937884"],
 "Soda Springs": ["https://www.sodaspringsid.com/city/mayor_and_council/index.php", "https://www.sodaspringsid.com/city/city_council.php", "https://www.sodaspringsid.com/city/publicmeetings.php", "https://www.sodaspringsid.com/city/planning_and_zoning.php"],
}
KEY = re.compile(r"(meet|Monday|Tuesday|Wednesday|Thursday|Friday|Mayor|p\.m\.|PM|\bpm\b|Council Chambers|City Hall)", re.I)
def text(h):
    h = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>|</(p|div|li|h\d|tr|td)>", "\n", h)
    t = H.unescape(re.sub(r"<[^>]+>", " ", h))
    return [l for l in (re.sub(r"\s+", " ", x).strip() for x in t.split("\n")) if l]
out = {}
for city, urls in PAGES.items():
    out[city] = {}
    for u in urls:
        try:
            build.check_robots(u)
            r = build.get(u)
            lines = text(r.text)
            hits = [l[:220] for l in lines if KEY.search(l) and len(l) < 400]
            links = re.findall(r'href="([^"]+\.pdf[^"]*)"', r.text, re.I)[:8]
            out[city][u] = {"hits": hits[:30], "pdfs": links}
        except Exception as exc:
            out[city][u] = {"error": (type(exc).__name__ + ": " + str(exc))[:160]}
# Revize calendars
for name, site, ws, cms in [("Preston", "https://www.prestonidaho.net", "prestonid", "cms3"), ("Soda Springs", "https://www.sodaspringsid.com", "sodasprings", "cms5")]:
    try:
        rows = build.get(site + "/_assets_/plugins/revizeCalendar/calendar_data_handler.php", {"webspace": ws, "relative_revize_url": f"//{cms}.revize.com", "protocol": "https:"}).json()
        fut = [r for r in rows if str(r.get("start", ""))[:10] >= "2026-11-22"]
        out[name]["revize"] = {"n": len(rows), "future": [{k: r.get(k) for k in ("title", "start", "rrule", "categories")} for r in fut[:15]]}
    except Exception as exc:
        out[name]["revize"] = {"error": repr(exc)[:200]}
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print("done")
