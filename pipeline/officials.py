"""Build site/data/officials.json: who holds each Idaho legislative and
congressional seat, for the "Who represents you" lookup.

Sources (both public and meant for reuse):
  - Open States current-legislators file for Idaho (public domain data,
    gathered from the Idaho Legislature's member pages)
  - unitedstates/congress-legislators (public-domain roster of Congress)

Idaho has 35 legislative districts. Each elects one senator and two
representatives, in House seats A and B.

Members elected in November take office December 1, but Open States can take
weeks to list them. From that day, pipeline/elected_2026.csv (the winners on
the Idaho Secretary of State's official 2026 general election results) fills
any seat where Open States still shows someone else. A seat where Open States
already names the winner keeps its Open States entry, so once Open States has
caught up the override changes nothing. It stops on ELECTED_UNTIL, so a later
appointment to fill a vacancy is never overwritten for long.

Never fails the nightly run: if a source is down, the last good file is kept.
"""
from __future__ import annotations

import csv
import io
import json
import re
import sys
import unicodedata
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

OUT = Path(__file__).resolve().parent.parent / "site" / "data" / "officials.json"
UA = "CivicsID/0.1 (BarNone nonprofit civic calendar; contact via barnoneinc.org)"
LEGISLATORS = "https://data.openstates.org/people/current/id.csv"
CONGRESS = "https://raw.githubusercontent.com/unitedstates/congress-legislators/gh-pages/legislators-current.json"
PARTY = {"Democratic": "Democrat"}
ELECTED = Path(__file__).resolve().parent / "elected_2026.csv"
ELECTED_FROM = date(2026, 12, 1)    # Idaho Code 67-404: legislators take office December 1
ELECTED_UNTIL = date(2027, 3, 1)    # safety stop; Open States has always caught up well before this


def parse_legislators(csv_text: str) -> dict:
    """{district: {"senate": [...], "house": [...]}} from the Open States CSV.

    Senate districts are numbered "16"; House seats are "16A" and "16B".
    """
    districts: dict[str, dict] = {}
    for row in csv.DictReader(io.StringIO(csv_text)):
        m = re.match(r"^\s*0*(\d+)\s*([A-Za-z]?)\s*$", row.get("current_district") or "")
        chamber = {"upper": "senate", "lower": "house"}.get((row.get("current_chamber") or "").strip())
        name = (row.get("name") or "").strip()
        if not m or not chamber or not name:
            continue
        entry = {
            "name": name,
            "party": PARTY.get(row.get("current_party", ""), row.get("current_party", "")),
            "phone": (row.get("capitol_voice") or row.get("district_voice") or "").strip(),
            "email": (row.get("email") or "").strip(),
        }
        if chamber == "house" and m.group(2):
            entry["seat"] = m.group(2).upper()
        districts.setdefault(m.group(1), {"senate": [], "house": []})[chamber].append(entry)
    for seats in districts.values():
        seats["senate"].sort(key=lambda p: p["name"])
        seats["house"].sort(key=lambda p: (p.get("seat", ""), p["name"]))
    return districts


def name_key(name: str) -> str:
    """First initial and last name, lowercased, without accents, nicknames or suffixes.

    The results page and Open States spell some names differently
    ('Richard (Rick) Cheatum', 'Doug "Doug O" Okuniewicz'), so a seat's holder
    is compared by first initial and last name. The initial matters: in 2026
    Jane Sauter won the House seat Mark Sauter held.
    """
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    name = re.sub(r'"[^"]*"|\([^)]*\)', " ", name)
    words = [w for w in re.findall(r"[a-z'-]+", name) if w not in {"jr", "sr", "ii", "iii", "iv"}]
    while len(words) > 1 and len(words[0]) == 1:  # 'C. Scott Grow' goes by Scott
        words = words[1:]
    return f"{words[0][0]} {words[-1]}" if words else ""


def apply_elected(legislators: dict, elected_csv: str) -> tuple[dict, int]:
    """Put the November winners in any seat where the roster still shows someone else.

    Returns the updated roster and how many seats changed. New entries have no
    phone or email: the Legislature assigns those when members take office, and
    Open States brings them in when it lists the new members.
    """
    out = json.loads(json.dumps(legislators))
    changed = 0
    for row in csv.DictReader(io.StringIO(elected_csv)):
        district, chamber, seat = row["district"].strip(), row["chamber"].strip(), row["seat"].strip().upper()
        name = row["name"].strip()
        seats = out.setdefault(district, {"senate": [], "house": []})
        members = seats[chamber]
        here = [p for p in members if chamber == "senate" or p.get("seat") == seat]
        if here and name_key(here[0]["name"]) == name_key(name):
            continue
        entry = {"name": name, "party": PARTY.get(row["party"], row["party"]), "phone": "", "email": ""}
        if chamber == "house":
            entry["seat"] = seat
        seats[chamber] = [p for p in members if p not in here] + [entry]
        seats["senate"].sort(key=lambda p: p["name"])
        seats["house"].sort(key=lambda p: (p.get("seat", ""), p["name"]))
        changed += 1
    return out, changed


def parse_congress(rows: list, state: str = "ID") -> dict:
    out = {"senators": [], "house": {}}
    for person in rows:
        term = person["terms"][-1]
        if term.get("state") != state:
            continue
        entry = {
            "name": person["name"].get("official_full")
                    or f"{person['name'].get('first', '')} {person['name'].get('last', '')}".strip(),
            "party": term.get("party", ""),
            "phone": term.get("phone", ""),
            "url": term.get("url", ""),
        }
        if term["type"] == "sen":
            out["senators"].append(entry)
        else:
            out["house"][str(term.get("district"))] = entry
    out["senators"].sort(key=lambda m: m["name"])
    return out


def get(url, params=None):
    import requests
    from build import check_robots  # same robots.txt rule as the calendar
    check_robots(url)
    resp = requests.get(url, params=params, headers={"User-Agent": UA}, timeout=45)
    resp.raise_for_status()
    return resp


def main() -> int:
    now = datetime.now(ZoneInfo("America/Boise"))
    try:
        previous = json.loads(OUT.read_text())
    except Exception:
        previous = {}
    data = {"generated": now.isoformat(timespec="seconds"),
            "legislators": previous.get("legislators", {}),
            "congress": previous.get("congress", {"senators": [], "house": {}})}

    try:
        found = parse_legislators(get(LEGISLATORS).content.decode("utf-8-sig"))
        if len(found) >= 30:  # a short file means the source is mid-update; keep the last good one
            data["legislators"] = found
        print(f"legislators: {sum(len(s['senate']) + len(s['house']) for s in found.values())} "
              f"in {len(found)} districts")
    except Exception as exc:
        print(f"[warn] legislators: {type(exc).__name__}: {exc}"[:300], file=sys.stderr)

    if ELECTED_FROM <= now.date() < ELECTED_UNTIL:
        try:
            elected, changed = apply_elected(data["legislators"], ELECTED.read_text(encoding="utf-8"))
            data["legislators"] = elected
            print(f"members elected in 2026: {changed} seats filled from {ELECTED.name}")
        except Exception as exc:
            print(f"[warn] elected 2026: {type(exc).__name__}: {exc}"[:300], file=sys.stderr)

    try:
        congress = parse_congress(get(CONGRESS).json())
        if congress["senators"]:
            data["congress"] = congress
        print(f"congress: {len(congress['senators'])} senators, {len(congress['house'])} representatives")
    except Exception as exc:
        print(f"[warn] congress: {type(exc).__name__}: {exc}"[:300], file=sys.stderr)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
