"""Probe: remaining districts."""
import io, json, re, sys
from pathlib import Path
from datetime import date
from urllib.parse import urljoin
from zoneinfo import ZoneInfo
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, pypdf
out = {}
try:
    ev = build.fetch_boardbook({"id": "lakeland", "name": "x", "county": "Kootenai", "area": "Rathdrum", "organization": 2129, "default_category": "school"}, date(2026, 11, 22), date(2027, 1, 21), ZoneInfo("America/Los_Angeles"))
    out["boardbook 2129"] = [(e["start"][:16], e["title"][:40], e.get("location", "")[:40]) for e in ev[:5]]
except Exception as exc:
    out["boardbook 2129"] = repr(exc)[:200]
def text_of(r):
    if r.url.split("?")[0].lower().endswith(".pdf") or "pdf" in r.headers.get("content-type", ""):
        return "PDF: " + " ".join(" ".join((p.extract_text() or "") for p in pypdf.PdfReader(io.BytesIO(r.content)).pages).split())[:2500]
    return " ".join(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", r.text)).split())
PAGES = {
 "jefferson": "https://www.jeffersonsd251.org/", "mtnhome": "https://www.mtnhomesd.org/Page/44",
 "mtnhome_notice": "https://www.mtnhomesd.org/cms/lib/ID50010914/Centricity/Domain/4/NOTICE OF CHANGE OF SCHEDULE of Regular Board Meetings - Jun 17 25.pdf",
 "kimberly": "https://www.kimberly.edu/", "preston": "https://www.prestonschools.org/boe/board-of-education-information",
 "kuna_cal": "https://www.kunaschools.org/12218_4",
}
for k, u in PAGES.items():
    try:
        build.check_robots(u); r = build.get(u); t = text_of(r)
        rec = {"final": r.url}
        if t.startswith("PDF"): rec["text"] = t
        else:
            rec["sched"] = re.findall(r"[^.]{0,160}(?:regular(?:ly)? (?:board )?meeting|board meets|meets on|meetings? (?:are|will be) held|of each month|of every month)[^.]{0,200}\.", t, re.I)[:6]
            rec["links"] = [(urljoin(r.url, h.replace("&amp;", "&")), re.sub(r"<[^>]+>|\s+", " ", x).strip()[:50]) for h, x in re.findall(r'href="([^"]+)"[^>]*>(.*?)</a>', r.text, re.S)
                            if re.search(r"board|trustee|meeting|schedule", h + x, re.I)][:15]
        out[k] = rec
    except Exception as exc:
        out[k] = {"error": (type(exc).__name__ + ": " + str(exc))[:150]}
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print("done")
