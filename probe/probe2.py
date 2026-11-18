"""Probe: Twin Falls County daily agenda PDFs; Bonneville Tyler Meeting Manager; Latah agendas."""
import io, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests, pypdf
out = {}
try:
    page = build.get("https://twinfallscounty.org/commissioners/agenda/").text
    links = re.findall(r'href="(https://twinfallscounty.org/wp-content/uploads/[A-Za-z]+-\d{1,2}\.\d{1,2}\.\d{2}[^"]*\.pdf)"', page)
    out["tf_links"] = links
    for u in links[1:3]:
        r = pypdf.PdfReader(io.BytesIO(build.get(u).content))
        out[u] = "\n".join(p.extract_text() or "" for p in r.pages)[:2500]
except Exception as exc:
    out["tf_error"] = repr(exc)[:300]
try:
    u = "https://bonnevillecountyid.meetingmanager.tylerapp.com/tylermmcalendar5189bonnevillecountyid/meetingInformation/getMeetingInformationByDate"
    build.check_robots(u)
    r = requests.post(u, json={"startDate": "11/18/2026", "endDate": "01/17/2027", "meetingTypeIds": []}, headers={"User-Agent": build.UA}, timeout=60)
    out["bonneville"] = f"{r.status_code} {len(r.json()) if r.ok else r.text[:200]}"
except Exception as exc:
    out["bonneville_error"] = repr(exc)[:300]
try:
    h = build.get("https://latahcountyid.gov/commissioners/").text
    out["latah_agenda_links"] = re.findall(r'href="([^"]+)"[^>]*>([^<]{0,60}(?:Agenda|agenda)[^<]{0,40})<', h)[:12]
except Exception as exc:
    out["latah_error"] = repr(exc)[:300]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1)[:9000])
