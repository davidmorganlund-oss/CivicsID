import csv
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pipeline"))
from officials import ELECTED, apply_elected, name_key  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def test_name_key_ignores_nicknames_and_accents():
    assert name_key('Doug "Doug O" Okuniewicz') == name_key("Doug Okuniewicz")
    assert name_key("Richard (Rick) Cheatum") == name_key("Rick Cheatum")
    assert name_key("Soñia Galaviz") == "s galaviz"
    assert name_key("Jane Sauter") != name_key("Mark Sauter")
    assert name_key("C. Scott Grow") == name_key("Scott Grow")


def test_elected_file_has_every_seat():
    rows = list(csv.DictReader(io.StringIO(ELECTED.read_text(encoding="utf-8"))))
    seats = {(r["chamber"], r["district"], r["seat"]) for r in rows}
    assert len(rows) == len(seats) == 105
    for d in range(1, 36):
        assert {("senate", str(d), ""), ("house", str(d), "A"), ("house", str(d), "B")} <= seats


def test_new_members_replace_old_and_returning_members_keep_contacts():
    roster = {
        "16": {"senate": [{"name": "Ali Rabe", "party": "Democrat", "phone": "1", "email": "a@x"}],
               "house": [{"name": "Soñia Galaviz", "party": "Democrat", "phone": "2", "email": "s@x", "seat": "A"},
                         {"name": "Steve Berch", "party": "Democrat", "phone": "3", "email": "b@x", "seat": "B"}]},
    }
    elected = ("chamber,district,seat,name,party\n"
               "senate,16,,Soñia Galaviz,Democratic\n"
               "house,16,A,Megan Woller,Democratic\n"
               "house,16,B,Steve Berch,Democratic\n")
    out, changed = apply_elected(roster, elected)
    assert changed == 2
    assert out["16"]["senate"] == [{"name": "Soñia Galaviz", "party": "Democrat", "phone": "", "email": ""}]
    assert out["16"]["house"][0] == {"name": "Megan Woller", "party": "Democrat", "phone": "", "email": "", "seat": "A"}
    assert out["16"]["house"][1]["phone"] == "3"
    assert roster["16"]["senate"][0]["name"] == "Ali Rabe"  # input left as it was
    again, changed_again = apply_elected(out, elected)
    assert changed_again == 0 and again == out


def test_current_roster_gets_three_members_per_district():
    roster = json.loads((ROOT / "site" / "data" / "officials.json").read_text())["legislators"]
    out, changed = apply_elected(roster, ELECTED.read_text(encoding="utf-8"))
    assert changed <= 105
    for d in range(1, 36):
        seats = out[str(d)]
        assert len(seats["senate"]) == 1
        assert sorted(p["seat"] for p in seats["house"]) == ["A", "B"]
