"""Open (or update, or close) one GitHub issue listing calendar sources that
have failed for three days or more. GitHub emails the repository owner when
the issue opens, so a broken city calendar doesn't go unnoticed.

Runs after build.py in the nightly workflow; needs the gh CLI and GH_TOKEN.
"""
import json
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

TITLE = "Calendar sources need attention"
UPKEEP_TITLE = "Hand-entered schedules need new dates"
ROOT = Path(__file__).resolve().parent.parent
STATUS = ROOT / "site" / "data" / "status.json"
SOURCES = ROOT / "pipeline" / "sources.yml"
DAYS = 3
AHEAD = 21  # warn this many days before a hand-entered date list runs out


def gh(*args):
    return subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout


def stuck_sources(status, today):
    cutoff = (today - timedelta(days=DAYS - 1)).isoformat()
    return [s for s in status["sources"]
            if s.get("state") == "failing" and s.get("failing_since") and s["failing_since"] <= cutoff]


def body(stuck):
    lines = ["These calendars have not answered for three days or more. CivicsID keeps showing the "
             "last meetings it read from them, so their listings are going stale.", ""]
    for s in stuck:
        lines.append(f"- **{s['name']}** ({s.get('county', '')} County), failing since {s['failing_since']}. "
                     f"Last good read: {s.get('last_success') or 'never'}. Error: `{s.get('error', '')[:200]}`")
    lines += ["", "If a site now refuses automated readers, remove it from `pipeline/sources.yml` "
              "rather than working around the block. This issue closes itself when every source answers again."]
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
        for mtg in src.get("meetings", []):
            if mtg.get("one_off"):
                continue  # a single special meeting, not a series that needs more dates
            last = max([date.fromisoformat(str(d)) for d in mtg.get("dates", [])], default=None)
            until = mtg.get("until") and date.fromisoformat(str(mtg["until"]))
            end = last if (last and not mtg.get("when")) else until
            if end and end <= horizon:
                when = "ran out" if end < today else "runs out"
                items.append(f"- **{src['name']}**, {mtg['title']} (`{src['id']}`): listed dates {when} {end}. "
                             f"Add the next dates from {mtg.get('url') or src.get('homepage', '')}.")
    return items


def sync_issue(title, lines, closing):
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
    items = upkeep_items(yaml.safe_load(SOURCES.read_text()), date.today())
    sync_issue(UPKEEP_TITLE, (["These hand-entered schedules or planned changes need a human look in the next "
                               f"{AHEAD} days. Once their meetings pass, the calendar quietly goes empty for them.", ""]
                              + items) if items else [], "Every hand-entered schedule has dates for the next three weeks.")
    stuck = stuck_sources(json.loads(STATUS.read_text()), date.today())
    found = json.loads(gh("issue", "list", "--state", "open", "--search", f'"{TITLE}" in:title',
                          "--json", "number,title"))
    issue = next((i["number"] for i in found if i["title"] == TITLE), None)
    if stuck and issue is None:
        gh("issue", "create", "--title", TITLE, "--body", body(stuck))
        print(f"opened an issue for {len(stuck)} source(s)")
    elif stuck:
        gh("issue", "edit", str(issue), "--body", body(stuck))
        print(f"updated issue #{issue}: {len(stuck)} source(s)")
    elif issue is not None:
        gh("issue", "close", str(issue), "--comment", "Every calendar source is answering again.")
        print(f"closed issue #{issue}")
    else:
        print("all sources healthy or failing for less than three days")
    return 0


if __name__ == "__main__":
    sys.exit(main())
