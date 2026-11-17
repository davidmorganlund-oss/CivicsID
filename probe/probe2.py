import json, re, subprocess
from pathlib import Path
import requests
r = requests.get("https://archive.sos.idaho.gov/blue_book/blue_book_2025-2026.pdf", headers={"User-Agent": "CivicsID/0.1 (BarNone nonprofit civic calendar)"}, timeout=300)
Path("/tmp/bb.pdf").write_bytes(r.content)
subprocess.run(["sudo", "apt-get", "install", "-y", "-qq", "poppler-utils"], check=False, capture_output=True)
subprocess.run(["pdftotext", "-layout", "/tmp/bb.pdf", "/tmp/bb.txt"], check=True)
pages = Path("/tmp/bb.txt").read_text(errors="replace").split("\f")
keep = {i: t for i, t in enumerate(pages) if re.search(r"Commissioner|Mayor", t)}
Path("probe/report2.json").write_text(json.dumps({"n": len(pages), "pages": keep}, indent=0))
print(len(pages), len(keep), sorted(keep))
