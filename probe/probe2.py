import io, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, requests, pypdf
out = {}
u = "https://libraries.idaho.gov/files/Table%203%20-%20Idaho%20Public%20Libraries%20by%20Name.pdf"
try:
    build.check_robots(u); r = requests.get(u, headers={"User-Agent": build.UA}, timeout=60)
    out["status"] = r.status_code; out["ctype"] = r.headers.get("content-type")
    if "pdf" in (r.headers.get("content-type") or ""):
        out["text"] = "\n".join(p.extract_text() or "" for p in pypdf.PdfReader(io.BytesIO(r.content)).pages)[:40000]
    else:
        out["text"] = r.text[:500]
except Exception as exc:
    out["err"] = repr(exc)[:300]
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
