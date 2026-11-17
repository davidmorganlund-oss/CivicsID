import io, json, re
from pathlib import Path
import requests, pypdf
r = requests.get("https://archive.sos.idaho.gov/blue_book/blue_book_2025-2026.pdf", headers={"User-Agent": "CivicsID/0.1 (BarNone nonprofit civic calendar)"}, timeout=120)
print(r.status_code, len(r.content))
reader = pypdf.PdfReader(io.BytesIO(r.content))
pages = [(i, p.extract_text() or "") for i, p in enumerate(reader.pages)]
print("pages", len(pages))
keep = {i: t for i, t in pages if re.search(r"Commissioner|Mayor|Council", t)}
Path("probe/report2.json").write_text(json.dumps({"n": len(pages), "pages": keep}, indent=0))
print("kept", len(keep), sorted(keep)[:80])
