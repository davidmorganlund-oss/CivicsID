"""Open (or update, or close) one GitHub issue listing calendar sources that
have failed for three days or more, or answered with no meetings for seven
days or more. GitHub emails the repository owner when the issue opens, so a
broken or stalled city calendar doesn't go unnoticed.

Runs after build.py in the nightly workflow; needs the gh CLI and GH_TOKEN.
"""
import json
import re
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

TITLE = "Calendar feeds needing attention"
OLD_TITLES = ("Calendar sources need attention",)  # earlier name; an open one is renamed
UPKEEP_TITLE = "Hand-entered schedules need new dates"
ROOT = Path(__file__).resolve().parent.parent
STATUS = ROOT / "site" / "data" / "status.json"
SOURCES = ROOT / "pipeline" / "sources.yml"
DAYS = 3
QUIET_DAYS = 7  # a source can list nothing for a week (holidays, agendas posted late)
AHEAD = 21  # warn this many days before a hand-entered date list runs out


def gh(*args):
    return subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout


def stuck_sources(status, today):
    cutoff = (today - timedelta(days=DAYS - 1)).isoformat()
    return [s for s in status["sources"]
            if s.get("state") == "failing" and s.get("failing_since") and s["failing_since"] <= cutoff]


def quiet_sources(status, today, quiet_ok=()):
    """Sources that answered with no meetings every night for QUIET_DAYS or
    more (status.json's quiet_since). Sources marked quiet_ok in sources.yml,
    like the Legislature between sessions, are left out."""
    cutoff = (today - timedelta(days=QUIET_DAYS - 1)).isoformat()
    return [s for s in status["sources"]
            if s.get("state") == "quiet" and s.get("quiet_since") and s["quiet_since"] <= cutoff
            and s["id"] not in quiet_ok]


def body(stuck, quiet=()):
    lines = []
    if stuck:
        lines += ["**Failing.** These calendars have not answered for three days or more. CivicsID keeps showing the "
                  "last meetings it read from them, so their listings are going stale.", ""]
        for s in stuck:
            lines.append(f"- **{s['name']}** (`{s['id']}`, {s.get('county', '')} County), failing since {s['failing_since']}. "
                         f"Last good read: {s.get('last_success') or 'never'}. Error: `{s.get('error', '')[:200]}`")
        lines.append("")
    if quiet:
        lines += [f"**Quiet.** These calendars answer but have listed no meetings for {QUIET_DAYS} days or more. "
                  "That can be a holiday break or agendas posted late, or a moved calendar or a changed page layout.", ""]
        for s in quiet:
            lines.append(f"- **{s['name']}** (`{s['id']}`, {s.get('county', '')} County), no meetings since "
                         f"{s['quiet_since']}. Check {s.get('homepage') or 'the source'}.")
        lines.append("")
    lines += ["If a site now refuses automated readers, remove it from `pipeline/sources.yml` "
              "rather than working around the block. A source that is quiet by design can be marked "
              "`quiet_ok: true` there. This issue closes itself when the list is empty."]
    return "\n".join(lines)


def upkeep_items(cfg, today):
    """Hand-entered schedules whose list of dates runs out soon, and sources
    with a 'review_by' date (a planned change, like a portal move) that is due."""
    horizon = today + timedelta(days=AHEAD)
    items = []
    for src in cfg["sources"]:
        review = src.get("review_by")
        if review and date.fromisoformat(str(review)) <= horizon:
            items.append(f"- **{src['name']}** (`{src['id']}`): {src.get('review_note', 'planned change due')} (by {review}).")
        ruled = {m["title"] for m in src.get("meetings", []) if m.get("when")}
        for mtg in src.get("meetings", []):
            if mtg.get("one_off"):
                continue  # a single special meeting, not a series that needs more dates
            if mtg.get("dates") and mtg["title"] in ruled:
                continue  # the dates bridge a gap; a regular rule for the same meeting takes over
            last = max([date.fromisoformat(str(d)) for d in mtg.get("dates", [])], default=None)
            until = mtg.get("until") and date.fromisoformat(str(mtg["until"]))
            end = last if (last and not mtg.get("when")) else until
            if end and end <= horizon:
                when = "ran out" if end < today else "runs out"
                items.append(f"- **{src['name']}**, {mtg['title']} (`{src['id']}`): listed dates {when} {end}. "
                             f"Add the next dates from {mtg.get('url') or src.get('homepage', '')}.")
    return items


def quiet_text(text):
    """Meeting names come from outside sites; keep a stray "@name" in one
    from pinging a real GitHub user."""
    return re.sub(r"@(?=[A-Za-z0-9])", "@\u2060", text)


def sync_issue(title, lines, closing):
    lines = [quiet_text(line) for line in lines]
    found = json.loads(gh("issue", "list", "--state", "open", "--search", f'"{title}" in:title',
                          "--json", "number,title"))
    issue = next((i["number"] for i in found if i["title"] == title), None)
    if lines and issue is None:
        gh("issue", "create", "--title", title, "--body", "\n".join(lines))
        print(f"opened: {title}")
    elif lines:
        gh("issue", "edit", str(issue), "--body", "\n".join(lines))
        print(f"updated #{issue}: {title}")
    elif issue is not None:
        gh("issue", "close", str(issue), "--comment", closing)
        print(f"closed #{issue}")


def main():
    import yaml
    cfg = yaml.safe_load(SOURCES.read_text())
    items = upkeep_items(cfg, date.today())
    roster = ROOT / "site" / "data" / "county_officials.json"
    if roster.exists():
        meta = json.loads(roster.read_text())
        if meta.get("review_by") and date.fromisoformat(meta["review_by"]) <= date.today() + timedelta(days=AHEAD):
            items.append(f"- **County officials roster** (`site/data/county_officials.json`): {meta.get('review_note', '')} (by {meta['review_by']}).")
    sync_issue(UPKEEP_TITLE, (["These hand-entered schedules or planned changes need a human look in the next "
                               f"{AHEAD} days. Once their meetings pass, the calendar quietly goes empty for them.", ""]
                              + items) if items else [], "Every hand-entered schedule has dates for the next three weeks.")
    import checks
    found = checks.report()
    sync_issue("Data or link problems to look at", (["The nightly checks found these. Listings that look wrong may be a parsing or time zone "
                                                   "problem; broken links are pages that moved (checked Mondays).", ""] + found) if found else [],
               "Tonight's data and link checks came back clean.")
    status = json.loads(STATUS.read_text())
    stuck = stuck_sources(status, date.today())
    quiet_ok = {s["id"] for s in cfg["sources"] if s.get("quiet_ok")}
    quiet = quiet_sources(status, date.today(), quiet_ok)
    issue = None
    for title in (TITLE, *OLD_TITLES):
        found = json.loads(gh("issue", "list", "--state", "open", "--search", f'"{title}" in:title',
                              "--json", "number,title"))
        issue = next((i["number"] for i in found if i["title"] == title), None)
        if issue is not None:
            break
    text = quiet_text(body(stuck, quiet))
    if (stuck or quiet) and issue is None:
        gh("issue", "create", "--title", TITLE, "--body", text)
        print(f"opened an issue for {len(stuck)} failing and {len(quiet)} quiet source(s)")
    elif stuck or quiet:
        gh("issue", "edit", str(issue), "--title", TITLE, "--body", text)
        print(f"updated issue #{issue}: {len(stuck)} failing and {len(quiet)} quiet source(s)")
    elif issue is not None:
        gh("issue", "close", str(issue), "--comment", "Every calendar source is answering and listing meetings again.")
        print(f"closed issue #{issue}")
    else:
        print(f"no source failing {DAYS}+ days or quiet {QUIET_DAYS}+ days")
    return 0


if __name__ == "__main__":
    sys.exit(main())
