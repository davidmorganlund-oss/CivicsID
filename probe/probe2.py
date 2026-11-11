import json, io, re
from pathlib import Path
import requests, pypdf
S = requests.Session(); S.headers["User-Agent"] = "CivicsID/0.1 (BarNone nonprofit civic calendar; contact via barnoneinc.org)"
OUT = {}
for name in ["11-9 & 10-26 Commissioner Agenda.pdf", "11-02 & 03-26 Commissioner Agenda.pdf", "10-26 & 27-26 Commissioner Agenda.pdf"]:
    r = S.get("https://www.gemcounty.org/" + name, timeout=30)
    try:
        t = "\n".join(p.extract_text() or "" for p in pypdf.PdfReader(io.BytesIO(r.content)).pages)
    except Exception as e:
        t = f"ERR {e}"
    OUT[name] = {"status": r.status_code, "final": r.url, "text": t[:4000]}
    print("=" * 8, name, r.status_code); print(t[:4000])
Path("probe/report2.json").write_text(json.dumps(OUT, indent=1))
