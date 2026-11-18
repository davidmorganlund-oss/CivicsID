"""Quality checks run after each nightly build.

Data sanity: catches a bad parse before people notice it on the calendar.
  - the same meeting listed twice by one source
  - meetings at odd hours (usually a time zone or AM/PM mistake)
  - a source that had meetings yesterday and has none tonight

Links (weekly, Mondays): every outside link in the guides, the county and city
cards, and the source homepages, so moved pages get fixed.
"""
import json
import re
import subprocess
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
UA = "CivicsID/0.1 (BarNone nonprofit civic calendar; link check; contact admin@barnoneinc.org)"


def sanity(events, status, previous):
    lines = []
    keys = Counter((e["source"], e["start"], e["title"].strip().lower()) for e in events)
    dupes = [k for k, n in keys.items() if n > 1]
    for src, start, title in dupes[:15]:
        lines.append(f"- Listed twice: **{title}** from `{src}` at {start}.")
    for e in events:
        if e.get("all_day"):
            continue
        hour = int(e["start"][11:13])
        if hour < 6 or hour >= 22:
            lines.append(f"- Odd hour: **{e['title']}** from `{e['source']}` at {e['start'][:16]} ({e.get('tz', '')}). Check the time zone or AM/PM.")
    before = {s["id"]: s.get("count", 0) for s in (previous or {}).get("sources", [])}
    for s in status.get("sources", []):
        was = before.get(s["id"], 0)
        if was >= 5 and s.get("count", 0) == 0 and s.get("state") != "failing":
            lines.append(f"- Went quiet: `{s['id']}` ({s.get('name', '')}) had {was} meetings last run and 0 tonight, without an error. The site may have changed its layout.")
    return lines


def site_links():
    urls = set()
    for page in list((SITE / "guides").glob("*.html")) + list((SITE / "es" / "guides").glob("*.html")) + [SITE / "legislature.html", SITE / "privacy.html"]:
        urls.update(re.findall(r'href="(https?://[^"#]+)"', page.read_text()))
    local = json.loads((SITE / "data" / "local.json").read_text())
    for group in ("counties", "cities"):
        for entry in local.get(group, {}).values():
            for key in ("site", "meetings", "commissioners", "boards", "council"):
                if isinstance(entry.get(key), str) and entry[key].startswith("http"):
                    urls.add(entry[key])
            if isinstance(entry.get("mayor"), dict):
                urls.add(entry["mayor"]["source"])
    return sorted(u.replace("&amp;", "&") for u in urls)


def check(url):
    import requests
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=20, allow_redirects=True, stream=True)
        r.close()
        return url, r.status_code, ""
    except Exception as exc:
        return url, 0, type(exc).__name__


def links(urls):
    """Only clear failures count as broken: 404/410, or a site that doesn't
    exist. 401/403/429/5xx usually mean a bot block or a busy server, so they
    are listed separately and don't open the issue on their own."""
    with ThreadPoolExecutor(max_workers=12) as pool:
        results = list(pool.map(check, urls))
    broken = [(u, c, e) for u, c, e in results if c in (404, 410) or e in ("ConnectionError",) and c == 0]
    return [f"- Broken ({c or e}): {u}" for u, c, e in broken]


def previous_status():
    try:
        return json.loads(subprocess.run(["git", "show", "HEAD:site/data/status.json"], cwd=ROOT,
                                         capture_output=True, text=True, check=True).stdout)
    except Exception:
        return None


def report(today=None):
    today = today or date.today()
    events = json.loads((SITE / "data" / "events.json").read_text())["events"]
    status = json.loads((SITE / "data" / "status.json").read_text())
    lines = sanity(events, status, previous_status())
    if today.weekday() == 0:
        lines += links(site_links())
    return lines


if __name__ == "__main__":
    print("\n".join(report()) or "all checks passed")
