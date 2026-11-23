"""Probe: district board schedule pages and schedule PDFs (text)."""
import io, json, re, sys
from pathlib import Path
from urllib.parse import urljoin
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build, pypdf
PAGES = {
 "madison": "https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/2804/Msd321/fc59d3b2-dbfb-4f9b-a47c-8e67a8abbc61/2026-School-Board-Meeting-Schedule.pdf?disposition=inline",
 "blackfoot": "https://docs.sd55.org/MeetingMinutes/2026.School.Board.Meeting.Schedule.8.10.26-1.pdf",
 "postfalls": "https://www.pfsd.com/board-of-trustees/board-of-trustees-meeting-notices",
 "lposd": "https://www.lposd.org/board-of-trustees/trustee-meeting-schedule",
 "jerome": "https://www.jeromeschools.org/boardmeetings", "snakeriver": "https://www.snakeriver.org/board-meetings",
 "shelley": "https://www.shelleyschools.org/school-board-business", "preston": "https://www.prestonschools.org/boe/boe-meetings",
 "kuna": "https://www.kunaschools.org/boardhome", "kimberly": "https://www.kimberly.edu/board-trustees",
 "blaine": "https://www.blaineschools.org/school-board/board-homepage",
 "caldwell": "https://www.caldwellschools.org/apps/pages/index.jsp?uREC_ID=453519&type=d&pREC_ID=979297",
}
def text_of(r):
    if r.headers.get("content-type", "").startswith("application/pdf") or r.url.split("?")[0].endswith(".pdf"):
        return "PDF: " + " ".join(" ".join((p.extract_text() or "") for p in pypdf.PdfReader(io.BytesIO(r.content)).pages).split())[:2500]
    h = r.text
    return " ".join(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", h)).split())
out = {}
for k, u in PAGES.items():
    try:
        build.check_robots(u); r = build.get(u); t = text_of(r)
        rec = {"final": r.url, "text": t[:2500] if t.startswith("PDF") else ""}
        if not t.startswith("PDF"):
            rec["sched"] = re.findall(r"[^.]{0,160}(?:regular(?:ly)?|meets?|meetings? (?:are|will be) held|schedule)[^.]{0,200}\.", t, re.I)[:6]
            pdfs = [(urljoin(r.url, h.replace("&amp;", "&")), re.sub(r"<[^>]+>|\s+", " ", x).strip()) for h, x in re.findall(r'href="([^"]+)"[^>]*>(.*?)</a>', r.text, re.S)
                    if re.search(r"schedule|calendar|2026|2027", h + x, re.I) and re.search(r"board|meeting|schedule", h + x, re.I)]
            rec["links"] = pdfs[:10]
            for pu, label in pdfs[:3]:
                if re.search(r"schedule", pu + label, re.I):
                    try:
                        build.check_robots(pu); rr = build.get(pu); rec.setdefault("follow", []).append({pu: text_of(rr)[:1800]})
                    except Exception as exc:
                        rec.setdefault("follow", []).append({pu: "ERR " + str(exc)[:100]})
        out[k] = rec
    except Exception as exc:
        out[k] = {"error": (type(exc).__name__ + ": " + str(exc))[:150]}
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print("done")
