"""Checks the connectors against records shaped like the real feeds.

Most samples carry over from the Washington site this pipeline began as;
the connectors are the same, so the samples still exercise them.
"""
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pipeline"))
import build  # noqa: E402

TZ = ZoneInfo("America/Los_Angeles")


def test_legistar():
    src = {"id": "olympia", "name": "City of Olympia", "area": "Olympia"}
    rows = [{"EventId": 7068, "EventBodyName": "Planning Commission", "EventDate": "2026-11-16T00:00:00",
             "EventTime": "6:30 PM", "EventLocation": "Online Only",
             "EventAgendaFile": "https://example.org/a.pdf", "EventInSiteURL": "https://example.org/m",
             "EventComment": None},
            {"EventId": 1, "EventBodyName": "City Council", "EventDate": "2026-11-17T00:00:00",
             "EventTime": None, "EventLocation": None, "EventComment": "Meeting cancelled"}]
    a, b = build.normalize_legistar(src, rows, TZ)
    assert a["start"] == "2026-11-16T18:30:00-08:00" and a["category"] == "council"
    assert a["agenda_url"].endswith("a.pdf") and not a["cancelled"]
    assert b["all_day"] and b["cancelled"]


def test_civicclerk_times_are_local():
    src = {"id": "lacey", "name": "City of Lacey", "area": "Lacey", "tenant": "laceywa"}
    rows = [{"id": 1580, "eventName": "City Council Meeting ", "startDateTime": "2026-12-01T18:00:00Z",
             "eventLocation": {"address1": "Lacey City Hall Council Chambers", "city": None}},
            {"id": 2, "eventName": "Gone", "startDateTime": "2026-12-01T18:00:00Z", "isDeleted": True}]
    (e,) = build.normalize_civicclerk(src, rows, TZ)
    assert e["start"] == "2026-12-01T18:00:00-08:00"
    assert e["title"] == "City Council Meeting" and e["location"].startswith("Lacey City Hall")


def test_ics_expands_repeats():
    src = {"id": "tc", "name": "Thurston County", "area": "countywide", "homepage": "https://example.org"}
    ics = b"""BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
UID:abc
SUMMARY:BoCC Business Meeting
DTSTART;TZID=America/Los_Angeles:20261103T140000
DTEND;TZID=America/Los_Angeles:20261103T160000
RRULE:FREQ=WEEKLY;UNTIL=20261215T220000Z
LOCATION:Atrium Room 110
END:VEVENT
BEGIN:VEVENT
UID:hidden
SUMMARY:Busy
DTSTART:20261118T180000Z
END:VEVENT
BEGIN:VEVENT
UID:hear
SUMMARY:Public Hearing on the 2027 Budget
DTSTART:20261119T020000Z
END:VEVENT
END:VCALENDAR
"""
    events = build.normalize_ics(src, ics, date(2026, 11, 10), date(2026, 11, 30), TZ)
    titles = [e["title"] for e in events]
    assert titles.count("BoCC Business Meeting") == 3  # Nov 10, 17, 24
    assert "Busy" not in titles
    hearing = next(e for e in events if "Hearing" in e["title"])
    assert hearing["category"] == "hearing" and hearing["start"] == "2026-11-18T18:00:00-08:00"


def test_cancelled_prefix_is_dropped():
    src = {"id": "tc", "name": "Thurston County", "area": "countywide"}
    from datetime import datetime
    e = build.make_event(src, title="Canceled: Board Work Session", start=datetime(2026, 11, 17, 9, 0, tzinfo=TZ))
    assert e["cancelled"] and e["title"] == "Board Work Session"


def test_library_feed_keeps_only_civic_events():
    src = {"id": "trl", "name": "Timberland Regional Library", "area": "countywide",
           "city_areas": {"Olympia": "Olympia"}}
    xml = """<rss xmlns:bc="http://bibliocommons.com/rss/1.0/modules/event/" version="2.0"><channel>
    <item><title><![CDATA[TRL Board of Trustees Special Meeting - Budget Committee]]></title>
      <link>https://example.org/e/1</link><guid>https://example.org/e/1</guid>
      <category><![CDATA[Board Meetings]]></category><category><![CDATA[Adults]]></category>
      <bc:start_date_local>2026-11-12T16:30</bc:start_date_local><bc:end_date_local>2026-11-12T17:30</bc:end_date_local>
      <bc:is_cancelled>false</bc:is_cancelled><bc:is_virtual>true</bc:is_virtual></item>
    <item><title>Birth to Five Storytime</title><link>https://example.org/e/2</link>
      <category>Storytime</category><bc:start_date_local>2026-11-12T10:15</bc:start_date_local>
      <bc:location><bc:id>OL</bc:id><bc:name>Olympia</bc:name><bc:number>313</bc:number>
        <bc:street>8th Avenue SE</bc:street><bc:city>Olympia</bc:city></bc:location></item>
    <item><title>Friends of the Library Meeting</title><link>https://example.org/e/3</link>
      <category>Friends of the Library</category><bc:start_date_local>2026-11-14T12:30</bc:start_date_local>
      <bc:location><bc:id>OL</bc:id><bc:name>Olympia</bc:name><bc:number>313</bc:number>
        <bc:street>8th Avenue SE</bc:street><bc:city>Olympia</bc:city></bc:location></item>
    <item><title>Budget Hearing</title><link>https://example.org/e/4</link><category>Board Meetings</category>
      <bc:start_date_local>2026-11-18T16:30</bc:start_date_local></item>
    </channel></rss>"""
    events = build.normalize_bibliocommons(src, xml, TZ)
    assert [e["title"] for e in events] == ["TRL Board of Trustees Special Meeting - Budget Committee",
                                            "Friends of the Library Meeting", "Budget Hearing"]
    board, friends, hearing = events
    assert board["category"] == "council" and board["area"] == "countywide" and board["location"] == "Online"
    assert board["start"] == "2026-11-12T16:30:00-08:00" and board["end"] == "2026-11-12T17:30:00-08:00"
    assert friends["category"] == "library" and friends["area"] == "Olympia"
    assert friends["location"] == "Olympia, 313 8th Avenue SE, Olympia"
    assert hearing["category"] == "hearing"


def test_municode_table():
    src = {"id": "tumwater", "name": "City of Tumwater", "area": "Tumwater",
           "url": "https://tumwater-wa.municodemeetings.com/"}
    html = """<table><tr><th>Date</th></tr>
    <tr class="odd"> <td data-th="Date"> <span class="date-display-single" property="dc:date" datatype="xsd:dateTime" content="2026-11-17T19:00:00-08:00">11/17/2026 7:00 pm</span> </td> <td class="views-field views-field-title" data-th="Meeting"> City Council </td> <td class="views-field views-field-field-agendas" data-th="Agenda"> <a href="https://example.org/MEET-Agenda-4d47.pdf" title="PDF Agenda"></a> <a href="https://meetings.municode.com/adaHtmlDocument/index?cc=TUMWATER&amp;me=4d47&amp;ip=False"></a> </td> <td class="views-field views-field-field-minutes"> </td> <td class="views-field views-field-view-node" data-th="View"> <a href="/bc-cc/page/city-council-102" target="_blank">View Details</a> </td> </tr>
    <tr class="even"> <td data-th="Date"> <span class="date-display-single" content="2026-11-18T11:00:00-08:00">x</span> </td> <td class="views-field views-field-title"> General Government Committee </td> <td class="views-field views-field-field-agendas"> </td> <td class="views-field views-field-view-node"> <a href="/bc-gg/page/general-government-committee-48">View Details</a> </td> </tr></table>"""
    council, committee = build.normalize_municode(src, html, TZ)
    assert council["title"] == "City Council" and council["start"] == "2026-11-17T19:00:00-08:00"
    assert council["agenda_url"] == "https://example.org/MEET-Agenda-4d47.pdf"
    assert council["url"] == "https://tumwater-wa.municodemeetings.com/bc-cc/page/city-council-102"
    assert committee["agenda_url"] == "" and committee["category"] == "council"


def test_port_feed_titles():
    src = {"id": "port", "name": "Port of Olympia", "area": "countywide",
           "default_location": "Percival Plaza", "default_location_marker": "Olympics Room"}
    def item(title, day, desc="Percival Plaza &#8211; Olympics Room626 Columbia"):
        return (f"<item><title>{title}</title><link>https://example.org/{day}</link>"
                f"<description><![CDATA[{desc}]]></description><mec:startDate>{day}</mec:startDate></item>")
    xml = ('<rss xmlns:mec="http://webnus.net/rss/mec/" version="2.0"><channel>'
           + item("November 16, 2026 Commission Work Session:  4:00 PM", "2026-11-16")
           + item("CANCELLED:  September 21, 2026 Commission Work Session:  4:00 PM", "2026-09-21")
           + item("October 6, 2026 Special Meeting Notice &#8211; Port Commission Retreat: 5:00 &#8211; 7:00 PM", "2026-10-06", "Elsewhere")
           + item("September 28, 2026 Commission Meeting:  4:00 PM &#8211; meeting held in City of Bucoda", "2026-09-28", "Bucoda")
           + item("August 18, 2026 &#8211; Commission Notice of Potential Quorum", "2026-08-18", "x")
           + "</channel></rss>")
    a, b, c, d, e = build.normalize_mec_rss(src, xml, TZ)
    assert a["title"] == "Commission Work Session" and a["start"] == "2026-11-16T16:00:00-08:00"
    assert a["location"] == "Percival Plaza" and not a["cancelled"]
    assert b["title"] == "Commission Work Session" and b["cancelled"]
    assert c["title"] == "Special Meeting Notice – Port Commission Retreat" and c["start"].startswith("2026-10-06T17:00")
    assert c["location"] == ""
    assert d["title"] == "Commission Meeting – meeting held in City of Bucoda" and d["start"].startswith("2026-09-28T16:00")
    assert e["title"] == "Commission Notice of Potential Quorum" and e["all_day"]


def test_city_calendar_feed_titles():
    src = {"id": "tumwater", "name": "City of Tumwater", "area": "Tumwater"}
    def item(title, n):
        return f"<item><title>{title}</title><link>https://example.org/Event/{n}/</link></item>"
    xml = ('<rss version="2.0"><channel><title>Calendar RSS Feed</title>'
           + item("City Council (11/17/2026 7:00 p.m. - 10:00 p.m.)", 1)
           + item("LEOFF 1 - CANCELLED (11/12/2026 11:00 a.m. - 12:00 p.m.)", 2)
           + item("Veterans' Day - city offices closed (11/11/2026)", 3)
           + item("Something with no date", 4) + "</channel></rss>")
    council, leoff, holiday = build.normalize_govaccess_rss(src, xml, TZ)
    assert council["title"] == "City Council" and council["start"] == "2026-11-17T19:00:00-08:00"
    assert council["end"] == "2026-11-17T22:00:00-08:00" and council["category"] == "council"
    assert leoff["title"] == "LEOFF 1" and leoff["cancelled"] and leoff["start"].startswith("2026-11-12T11:00")
    assert holiday["all_day"] and holiday["title"] == "Veterans' Day - city offices closed"


def test_officials_parsers():
    import officials
    text = ("id,name,current_party,current_district,current_chamber,email,links,capitol_voice,district_voice\n"
            "x1,Sam Sample,Democratic,16,upper,sam@example.org,https://legislature.idaho.gov/s;https://x.org,208-555-0100,\n"
            "x2,Bea Seat,Republican,16B,lower,,,,208-555-0102\n"
            "x3,Al Seat,Republican,16A,lower,al@example.org,,208-555-0101,\n"
            "x4,No District,Republican,,lower,,,,\n")
    leg = officials.parse_legislators(text)
    assert list(leg) == ["16"]
    assert leg["16"]["senate"][0] == {"name": "Sam Sample", "party": "Democrat", "phone": "208-555-0100",
                                      "email": "sam@example.org"}
    assert [(m["seat"], m["name"]) for m in leg["16"]["house"]] == [("A", "Al Seat"), ("B", "Bea Seat")]
    assert leg["16"]["house"][1]["phone"] == "208-555-0102"
    rows = [{"name": {"official_full": "A Senator"}, "terms": [{"type": "sen", "state": "ID", "party": "Republican"}]},
            {"name": {"first": "B", "last": "Rep"}, "terms": [{"type": "rep", "state": "ID", "district": 2}]},
            {"name": {"official_full": "Other"}, "terms": [{"type": "rep", "state": "OR", "district": 1}]}]
    c = officials.parse_congress(rows)
    assert c["senators"][0]["name"] == "A Senator" and c["house"]["2"]["name"] == "B Rep" and len(c["house"]) == 1


def test_source_rules():
    def ev(cat):
        return {"category": cat, "title": cat}
    kept = build.apply_source_rules({"drop_uncategorized": True}, [ev("council"), ev("other"), ev("hearing")])
    assert [e["category"] for e in kept] == ["council", "hearing"]
    filed = build.apply_source_rules({"default_category": "council"}, [ev("other"), ev("hearing")])
    assert [e["category"] for e in filed] == ["council", "hearing"]
    assert len(build.apply_source_rules({}, [ev("other")])) == 1


def test_govaccess_long_dates():
    src = {"id": "shoreline", "name": "City of Shoreline", "area": "Shoreline", "county": "King"}
    xml = """<rss><channel><title>Calendar RSS Feed</title>
    <item><title>November 16, 2026 City Council Regular Meeting (November 16, 2026 7:00 pm - 10:00 pm)</title><link>https://example.org/1</link></item>
    <item><title>Greenhouse Winter Market (November 14, 2026 - November 15, 2026)</title><link>https://example.org/2</link></item>
    </channel></rss>"""
    council, market = build.normalize_govaccess_rss(src, xml, TZ)
    assert council["start"] == "2026-11-16T19:00:00-08:00" and council["county"] == "King"
    assert market["all_day"] and market["start"].startswith("2026-11-14")


def test_civicplus_closures_and_primegov():
    assert build.CLOSURE_TITLE.search("Thanksgiving Day") and build.CLOSURE_TITLE.search("City Hall closed")
    assert not build.CLOSURE_TITLE.search("Board of County Commissioners Meeting")
    src = {"id": "renton", "name": "City of Renton", "area": "Renton", "county": "King", "tenant": "renton"}
    rows = [{"id": 483, "dateTime": "2026-11-17T16:00:00", "title": "Special Civil Service Commission Meeting ",
             "location": "", "documentList": [{"templateId": 2234, "templateName": "HTML Agenda"}]}]
    (e,) = build.normalize_primegov(src, rows, TZ)
    assert e["start"] == "2026-11-17T16:00:00-08:00" and e["title"].endswith("Meeting")
    assert e["agenda_url"].endswith("meetingTemplateId=2234") and e["category"] == "council"


def test_civicweb():
    src = {"id": "sammamish", "name": "City of Sammamish", "area": "Sammamish", "county": "King", "tenant": "sammamishwa"}
    rows = [{"Id": 4840, "MeetingDateTime": "2026-12-17 18:30", "MeetingLocation": "City Hall",
             "Name": "Planning Commission - Dec 17 2026"},
            {"Id": 1, "MeetingDateTime": "2026-12-21 17:30", "MeetingLocation": "",
             "Name": "CANCELLED- City Council Regular Meeting - 21 Dec 2026"}]
    a, b = build.normalize_civicweb(src, rows, TZ)
    assert a["title"] == "Planning Commission" and a["start"] == "2026-12-17T18:30:00-08:00"
    assert b["cancelled"] and b["title"] == "City Council Regular Meeting"


def test_schedule():
    sched = {"id": "achd", "name": "Ada County Highway District", "area": "countywide", "county": "Ada",
             "meetings": [{"title": "Commission", "when": "4th Wednesday", "time": "18:00", "skip_months": [12]}]}
    got = build.fetch_schedule(sched, date(2026, 11, 1), date(2027, 1, 31), ZoneInfo("America/Boise"))
    assert [e["start"] for e in got] == ["2026-11-25T18:00:00-07:00", "2027-01-27T18:00:00-07:00"]
    assert "regular meeting schedule" in got[0]["note"] and got[0]["tz"] == "MT"
    assert not got[0]["cancelled"]


def test_boise_agenda_feed():
    src = {"id": "boise", "name": "City of Boise", "area": "Boise", "county": "Ada"}
    xml = """<rss version="2.0"><channel><title>RSS Feed</title>
    <item><title>City Council - Agenda - Nov 10, 2026 6:00 PM</title>
      <link>https://BoiseCityID.IQM2.com/Citizens/Detail_Meeting.aspx?ID=5476</link></item>
    <item><title>City Council - Minutes - Nov 10, 2026 6:00 PM</title>
      <link>https://BoiseCityID.IQM2.com/Citizens/Detail_Meeting.aspx?ID=5476</link></item>
    <item><title>Planning & Zoning Commission - Agenda - Nov 9, 2026 12:00 PM</title>
      <link>https://BoiseCityID.IQM2.com/Citizens/Detail_Meeting.aspx?ID=5470</link></item>
    <item><title>Something else entirely</title><link>https://example.org</link></item>
    </channel></rss>"""
    council, pz = build.normalize_iqm2_rss(src, xml, ZoneInfo("America/Boise"))
    assert council["title"] == "City Council" and council["start"] == "2026-11-10T18:00:00-07:00"
    assert council["url"].endswith("ID=5476") and council["category"] == "council"
    assert pz["title"] == "Planning & Zoning Commission" and pz["start"] == "2026-11-09T12:00:00-07:00"
    kc = build.make_event(src, title="Planning & Zoning Commission ||CANCELLED", start=build.datetime(2026, 11, 19, 13, 30))
    assert kc["title"] == "Planning & Zoning Commission" and kc["cancelled"]


def test_legislature_calendar_and_time_zones():
    ics = b"""BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
UID:mc-2670
SUMMARY:Joint Finance-Appropriations Committee
DTSTART;TZID=America/Boise:20261110T150000
DTEND;TZID=America/Boise:20261110T160000
URL:https://legislature.idaho.gov/?p=18021&#038;mc_id=2670
END:VEVENT
END:VCALENDAR
"""
    src = {"id": "legislature", "name": "Idaho Legislature", "area": "statewide", "county": "Statewide",
           "force_category": "legislature", "timezone": "America/Boise"}
    (e,) = build.apply_source_rules(src, build.normalize_ics(src, ics, date(2026, 11, 1), date(2026, 11, 30),
                                                              ZoneInfo("America/Boise")))
    assert e["start"] == "2026-11-10T15:00:00-07:00" and e["category"] == "legislature" and e["tz"] == "MT"
    assert e["url"] == "https://legislature.idaho.gov/?p=18021&mc_id=2670"
    north = {"id": "pf", "name": "City of Post Falls", "area": "Post Falls", "county": "Kootenai",
             "timezone": "America/Los_Angeles"}
    (n,) = build.normalize_civicclerk(dict(north, tenant="x"), [{"id": 1, "eventName": "City Council Meeting",
                                      "startDateTime": "2026-12-01T18:00:00Z"}], ZoneInfo("America/Los_Angeles"))
    assert n["start"] == "2026-12-01T18:00:00-08:00" and n["tz"] == "PT"
    assert build.categorize("Library Board of Trustees") == "council" and build.categorize("Library storytime") == "library"


def test_highlights_skip_procedure():
    olympia = ["CALL TO ORDER", "ROLL CALL", "APPROVAL OF AGENDA", "APPROVAL OF MINUTES",
               "Approval of the October 28, 2026 Heritage Commission Meeting Minutes", "PUBLIC COMMENT",
               "ANNOUNCEMENTS", "BUSINESS ITEMS", "Recommend Approval for Evergreen Inn Special Tax Valuation",
               "Public Hearing and Decision- Evergreen Inn Heritage Register Listing", "REPORTS", "ADJOURNMENT", "Upcoming"]
    assert build.pick_highlights(olympia) == ["Recommend Approval for Evergreen Inn Special Tax Valuation",
                                              "Public Hearing and Decision- Evergreen Inn Heritage Register Listing"]
    lacey = ["<strong>Transportation Benefit District Presentation</strong><br>Shannon Kelley-Fong",
             "<strong>Recent Acquisitions*</strong><br>Erin Quinn Valcho, Museum Curator", "Approval of the Agenda*"]
    assert build.pick_highlights(lacey) == ["Transportation Benefit District Presentation", "Recent Acquisitions"]
    e = {}
    build.add_highlights(e, ["One item here", "Two item here", "Three item here", "Four item here"])
    assert len(e["highlights"]) == 3 and e["highlights_more"] == 1


def test_alerts_pick_long_failures():
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pipeline"))
    import alerts
    status = {"sources": [
        {"name": "A", "state": "failing", "failing_since": "2026-11-08"},
        {"name": "B", "state": "failing", "failing_since": "2026-11-10"},
        {"name": "C", "state": "ok", "failing_since": ""}]}
    assert [s["name"] for s in alerts.stuck_sources(status, date(2026, 11, 11))] == ["A"]


def test_schedule_dates_and_agenda_links():
    pt = ZoneInfo("America/Los_Angeles")
    src = {"id": "r", "name": "City of Rathdrum", "area": "Rathdrum", "county": "Kootenai", "timezone": "America/Los_Angeles",
           "meetings": [{"title": "City Council Meeting", "dates": [date(2026, 12, 9), "2027-03-01"], "time": "17:30"},
                        {"title": "Council", "when": "1st, 3rd Tuesday", "until": "2026-12-15", "time": "18:00"}]}
    got = build.fetch_schedule(src, date(2026, 11, 11), date(2027, 1, 10), pt)
    assert [e["start"][:16] for e in got] == ["2026-12-09T17:30", "2026-11-17T18:00", "2026-12-01T18:00", "2026-12-15T18:00"]
    page = '''<li><a href="/media/hrybgkzc/packet110326web.pdf" target="_blank">November 3,2026</a></li>
              <li><a href="https://www.cdaid.org/media/x/packet-100626-web.pdf">October 6, 2026</a></li>'''
    found = build.dated_agendas(page, "https://www.cdaid.org/government/mayor-and-council/council-agendas/")
    assert found[date(2026, 11, 3)] == "https://www.cdaid.org/media/hrybgkzc/packet110326web.pdf" and date(2026, 10, 6) in found


def test_boardbook():
    src = {"id": "hayden", "name": "City of Hayden", "area": "Hayden", "county": "Kootenai",
           "organization": 2366, "timezone": "America/Los_Angeles"}
    page = '''<table><tr class="header"> <th> Meeting </th> </tr>
    <tr class=" row-for-unit-4328 row-for-unit"> <td> <div> November 12, 2026 at 3:00 PM - ARTS COMMISSION MEETING </div>
      <div class="margin-top-10"> <b>Meeting Type:</b> Commission (Arts Commission) </div> </td>
      <td> <div><span id="location15441-773366-description">Hayden City Hall Council Chambers</span><br>
      <span id="location15441-773366-line1">8930 N. Government Way</span><br><span id="location15441-773366-csz">Hayden, ID 83835</span></div> </td>
      <td class="nowrap"> <ul> <li> <a href="/Public/Agenda/2366?meeting=773366">Agenda</a> </li> </ul> </td> </tr>
    <tr class=" row-for-board"> <td> <div> November 19, 2026 at 4:00 PM - CANCELLED Veterans Commission Meeting </div> </td>
      <td></td><td></td> </tr></table>'''
    arts, vets = build.normalize_boardbook(src, page, ZoneInfo("America/Los_Angeles"))
    assert arts["title"] == "Arts Commission Meeting" and arts["start"] == "2026-11-12T15:00:00-08:00" and arts["tz"] == "PT"
    assert arts["location"] == "Hayden City Hall Council Chambers, 8930 N. Government Way"
    assert arts["url"].endswith("/Public/Agenda/2366?meeting=773366") and arts["category"] == "council"
    assert vets["cancelled"] and vets["title"] == "Veterans Commission Meeting"

    def row(i, parent, kids, text):
        return (f'<tr class="agenda-item-information agenda-item-children-of-{parent}" data-agendaitemid="{i}"> <td> '
                f'<input type="hidden" class="hasChildren" name="hasChildren" value="{kids}"> <div style="padding-left: 0em"> '
                f'<div class="form-check"> <i class="fa"></i> {text} </div> </div> </td> </tr>')
    agenda = "".join([
        row(1, 0, "true", "2. CONSENT CALENDAR <em>All items are Action Items</em>"),
        row(2, 1, "false", "2.A. Approval of Bills for Payment"),
        row(3, 0, "false", "3. VISITOR/PUBLIC COMMENT (3-minutes maximum)"),
        row(4, 0, "true", "4. PUBLIC HEARING (Public Testimony will be received for these items)"),
        row(5, 4, "false", "4.A. ACTION ITEM PZE-24-0013 Hazelnut Glen Phased Subdivision Preliminary Plat"),
        row(6, 0, "true", "5. UNFINISHED BUSINESS"),
        row(7, 6, "false", "5.A. ACTION ITEM Automatic License Plate Readers Policy Discussion"),
        row(8, 0, "true", "7. REPORTS"), row(9, 8, "false", "7.B. Finance"),
        row(10, 0, "false", "10. ADJOURNMENT")])
    assert build.boardbook_items(agenda) == [
        "Public hearing: PZE-24-0013 Hazelnut Glen Phased Subdivision Preliminary Plat",
        "Automatic License Plate Readers Policy Discussion"]


def test_libcal_libraries():
    pt = ZoneInfo("America/Los_Angeles")
    cln = {"id": "cln", "name": "Community Library Network", "area": "countywide", "county": "Kootenai",
           "timezone": "America/Los_Angeles", "civic_only": True,
           "campus_areas": {"Hayden": "Hayden", "Pinehurst": "Pinehurst"}, "campus_counties": {"Pinehurst": "Shoshone"}}
    rows = [
        {"id": 1, "title": "Veterans Day", "startdt": "2026-11-11 00:00:00", "all_day": True, "categories": "Closures and Notices"},
        {"id": 2, "title": "Board of Trustees Regular Meeting", "startdt": "2026-11-19 14:00:00", "enddt": "2026-11-19 16:00:00",
         "categories": "Board Meetings", "campus": "Post Falls", "location": "Meeting Room 1, Meeting Room 2",
         "url": "https://communitylibrary.libcal.com/event/2"},
        {"id": 3, "title": "Preschool Storytime", "startdt": "2026-11-18 10:30:00", "categories": "Youth Programs", "campus": "Hayden"},
        {"id": 4, "title": "Meet Your Legislators", "startdt": "2026-11-20 17:00:00", "enddt": "2026-11-20 18:00:00",
         "categories": "Adult Programs > Civil/Social", "campus": "Pinehurst", "location": "Meeting Room"},
        {"id": 6, "title": "Fiction Book Club", "startdt": "2026-11-20 17:00:00", "categories": "Adult Programs > Civil/Social", "campus": "Hayden"},
        {"id": 7, "title": "Board of Trustees Regular Meeting", "startdt": "2026-11-19 14:00:00", "categories": "Board Meetings", "campus": "Post Falls"},
        {"id": 5, "title": "Voter Registration Help", "startdt": "2026-11-21 11:00:00", "categories": "Adult Programs", "campus": "Hayden"}]
    assert not build.libcal_is_civic("Tween STEAM: Cardboard Kingdom", "Make > Arts/Crafts")
    board, renter, voter = build.normalize_libcal(cln, rows, pt)
    assert board["category"] == "council" and board["area"] == "countywide" and board["county"] == "Kootenai"
    assert board["start"] == "2026-11-19T14:00:00-08:00" and board["location"] == "Post Falls Library, Meeting Room 1, Meeting Room 2"
    assert renter["category"] == "library" and renter["county"] == "Shoshone" and renter["area"] == "Pinehurst"
    assert voter["area"] == "Hayden" and voter["end"] is None
    city = {"id": "c", "name": "City of Coeur d'Alene", "area": "Coeur d'Alene", "county": "Kootenai",
            "timezone": "America/Los_Angeles", "only_categories": ["City Meeting"], "skip_titles": "^city council meeting",
            "default_category": "council", "default_location": "Coeur d'Alene Public Library"}
    rows = [{"id": 1, "title": "City Council Meeting", "startdt": "2026-11-17 18:00:00", "categories": "City Meeting"},
            {"id": 2, "title": "Planning Commission", "startdt": "2026-11-10 17:30:00", "categories": "City Meeting",
             "location": "Community Room (Room 116)"},
            {"id": 3, "title": "Planning Commission setup", "startdt": "2026-11-10 16:30:00", "categories": "City Meeting Prep"}]
    (pc,) = build.normalize_libcal(city, rows, pt)
    assert pc["title"] == "Planning Commission" and pc["location"] == "Community Room (Room 116)" and pc["category"] == "council"


def test_mec_library_feed():
    src = {"id": "latah", "name": "Latah County Library District", "area": "countywide", "county": "Latah",
           "timezone": "America/Los_Angeles", "branches": ["Moscow", "Genesee"]}
    xml = """<rss><channel><title>Events</title>
    <item><title>Closed on Veterans Day</title><link>https://x.org/a</link>
      <mec:startDate>2026-11-11</mec:startDate><mec:startHour>All Day</mec:startHour></item>
    <item><title>Moscow &#8211; Babes &#038; Books</title><link>https://x.org/b</link>
      <mec:startDate>2026-11-12</mec:startDate><mec:startHour>10:30 am</mec:startHour></item>
    <item><title>Moscow &#8211; Citizenship Class</title><link>https://x.org/c</link>
      <mec:startDate>2026-11-12</mec:startDate><mec:startHour>5:30 pm</mec:startHour>
      <mec:endDate>2026-11-12</mec:endDate><mec:endHour>6:30 pm</mec:endHour><mec:location>Moscow Library</mec:location></item>
    <item><title>Board of Trustees Meeting</title><link>https://x.org/d</link>
      <mec:startDate>2026-11-18</mec:startDate><mec:startHour>4:00 pm</mec:startHour></item>
    </channel></rss>"""
    cls, board = build.normalize_mec_library(src, xml, ZoneInfo("America/Los_Angeles"))
    assert cls["title"] == "Citizenship Class" and cls["area"] == "Moscow" and cls["category"] == "library"
    assert cls["start"] == "2026-11-12T17:30:00-08:00" and cls["end"] == "2026-11-12T18:30:00-08:00"
    assert board["category"] == "council" and board["area"] == "countywide"


def test_new_county_connectors():
    mt, pt = ZoneInfo("America/Boise"), ZoneInfo("America/Los_Angeles")
    evo = {"id": "bonner", "name": "Bonner County", "area": "countywide", "county": "Bonner", "site": "https://www.bonnercountyid.gov"}
    (e,) = build.normalize_evo(evo, [{"id": 5, "title": "Bonner County - Business Meeting", "start_date": "11/17/2026 @ 09:00AM",
        "is_all_day": False, "location": "Bonner County Administrative Building", "location_street_address_1": "1500 Hwy 2",
        "location_city": "Sandpoint", "detail_link": '<a href="https://www.bonnercountyid.gov/events/5/">x</a>',
        "agenda_links": ['<a target="_blank" href="/meetingfiles/5/agendas/a.pdf">a.pdf</a>']}], pt)
    assert e["start"] == "2026-11-17T09:00:00-08:00" and e["agenda_url"] == "https://www.bonnercountyid.gov/meetingfiles/5/agendas/a.pdf"
    assert e["url"].endswith("/events/5/") and e["location"].startswith("Bonner County Administrative Building, 1500 Hwy 2")
    rev = {"id": "madison", "name": "Madison County", "area": "countywide", "county": "Madison", "calendars": ["Board of County Commissioners"]}
    (r,) = build.normalize_revize(rev, [
        {"title": "Commissioner's Meeting", "primary_calendar_name": "Board of County Commissioners", "start": "2026-12-14T08:30:00",
         "end": "2026-12-14T13:30:00", "url": "https://goo.gl/maps/x", "location": "Commissioners Meeting Room", "id": "1"},
        {"title": "Rodeo", "primary_calendar_name": "Community", "start": "2026-12-15T08:30:00"}], mt)
    assert r["start"] == "2026-12-14T08:30:00-07:00" and r["url"] == "" and r["category"] == "council"
    tribe = {"id": "bannock", "name": "Bannock County", "area": "countywide", "county": "Bannock", "categories": ["Board of County Commissioners"]}
    (b,) = build.normalize_tribe(tribe, [
        {"id": 1, "title": "Bannock County Commissioners&#8217; Meeting (action items)", "start_date": "2026-11-10 09:00:00",
         "end_date": "2026-11-10 10:00:00", "categories": [{"name": "Board of County Commissioners"}],
         "venue": {"venue": "Bannock County Courthouse, room 119"}, "url": "https://x.org/1"},
        {"id": 2, "title": "Veterans Coffee", "start_date": "2026-11-10 09:00:00", "categories": [{"name": "Veterans Event"}]}], mt)
    assert b["title"] == "Bannock County Commissioners\u2019 Meeting" and b["location"] == "Bannock County Courthouse, room 119"
    ac = {"id": "jerome", "name": "Jerome County", "area": "countywide", "county": "Jerome", "site": "https://www.jeromecountyid.us", "category": 2}
    page = ('<div id="category-panel-2" > <table><tr class="catAgendaRow"><td><h3><strong aria-label="Agenda for November 10, 2026">Nov 10, 2026</strong></h3>'
            '<p><a id="x" name="1726" href="/AgendaCenter/ViewFile/Agenda/_11102026-1726" target="_blank"> Commissioners Meeting </a></p></td></tr></table></div>'
            '<div id="category-panel-3" ><strong aria-label="Agenda for November 12, 2026"></strong><a href="/AgendaCenter/ViewFile/Agenda/_x">P&Z</a></div>')
    (j,) = build.normalize_agendacenter(ac, page, mt)
    assert j["all_day"] and j["start"].startswith("2026-11-10") and j["agenda_url"].endswith("_11102026-1726") and j["title"] == "Commissioners Meeting"
    canyon = {"id": "canyon", "name": "Canyon County", "area": "countywide", "county": "Canyon", "site": "https://agenda.canyoncounty.id.gov"}
    blk = lambda t1, t2, h, body: (f'<div class="cell-header">Start Time</div> <div class="cell-data">{t1}</div> </div> <div><div class="cell-header">End Time</div> '
                                   f'<div class="cell-data">{t2}</div> </div> <div class="col-lg mb-2"> <div class="cell-header">{h}</div> <div class="cell-data"> <pre>{body}</pre> </div>')
    page = blk("08:00 AM", "05:00 PM", "Ministerial, Administrative acts, and action items including but not limited to:", "x") + \
           blk("09:30 AM", "10:30 AM", "Meeting with County Attorneys for a Legal Staff Update", "y") + blk("11:00 AM", "11:30 AM", "Meeting with DSD for General Business", "z")
    (c,) = build.normalize_canyon_day(canyon, page, date(2026, 11, 12), mt)
    assert c["start"] == "2026-11-12T09:30:00-07:00" and c["highlights"] == ["Meeting with County Attorneys for a Legal Staff Update", "Meeting with DSD for General Business"]
    jev = {"id": "payette", "name": "Payette County", "area": "countywide", "county": "Payette"}
    xml = ("<rss><channel><item><title>11 Nov 2026 08:00 : Holiday Closure</title><link>https://x/1</link></item>"
           "<item><title>16 Nov 2026 09:00 : Commissioners Meeting </title><link>https://x/2</link></item></channel></rss>")
    (p,) = build.normalize_jevents(jev, xml, mt)
    assert p["title"] == "Commissioners Meeting" and p["start"] == "2026-11-16T09:00:00-07:00"
    sched = {"id": "s", "name": "Butte County", "area": "countywide", "county": "Butte",
             "meetings": [{"title": "Commissioners", "when": "2nd, 4th Monday"}]}
    got = build.fetch_schedule(sched, date(2026, 11, 1), date(2026, 11, 30), mt)
    assert [g["start"][:10] for g in got] == ["2026-11-09", "2026-11-23"] and all(g["all_day"] for g in got)


def test_drupal_meetings():
    src = {"id": "lincoln", "name": "Lincoln County", "area": "countywide", "county": "Lincoln", "site": "https://www.lincolncountyid.gov"}
    page = ('<tbody> <tr> <td headers="view-field-smart-date-table-column" class="x"><strong class="tablesaw-cell-label" aria-hidden="true">Date</strong> '
            '<span class="tablesaw-cell-content">Nov 9, 2026 | 10am </span></td> <td headers="view-title-table-column" class="x">'
            '<strong class="tablesaw-cell-label" aria-hidden="true">Meeting</strong> <span>Board of Commissioners Meeting </span></td> '
            '<td headers="view-nothing-1-table-column"><a href="https://mccmeetings.blob.core.usgovcloudapi.net/a.pdf">Agenda</a></td> '
            '<td headers="view-view-node-table-column"><a href="/commissioners/meeting/board-commissioners-meeting-85">View</a></td> </tr></tbody>')
    (e,) = build.normalize_drupal_meetings(src, page, ZoneInfo("America/Boise"))
    assert e["title"] == "Board of Commissioners Meeting" and e["start"] == "2026-11-09T10:00:00-07:00"
    assert e["url"].endswith("/board-commissioners-meeting-85") and e["agenda_url"].endswith("a.pdf")


def test_ics_skips_broken_repeat_rules():
    ics = ("BEGIN:VCALENDAR\r\nVERSION:2.0\r\n"
           "BEGIN:VEVENT\r\nUID:a\r\nSUMMARY:Veterans Day\r\nDTSTART:20261111T090000Z\r\nRRULE:FREQ=YEARLY;BYMONTH=11;COUNT=0\r\nEND:VEVENT\r\n"
           "BEGIN:VEVENT\r\nUID:b\r\nSUMMARY:Commissioners Meeting\r\nDTSTART:20261116T160000Z\r\nEND:VEVENT\r\n"
           "END:VCALENDAR\r\n")
    src = {"id": "benewah", "name": "Benewah County", "area": "countywide", "county": "Benewah"}
    tz = ZoneInfo("America/Los_Angeles")
    evs = build.normalize_ics(src, ics, date(2026, 11, 1), date(2026, 12, 31), tz)
    assert [e["title"] for e in evs] == ["Commissioners Meeting"]


def test_pdf_agenda_and_next_meeting():
    src = {"id": "gem", "name": "Gem County", "area": "countywide", "county": "Gem"}
    text = ("DATE: Monday, November 16, 2026 \n8:30 A.M. REVIEW AGENDA \u2013 ACTION ITEM \n9:30 A.M. TAX DEED PUBLIC HEARING \u2013 ACTION \nITEM \n"
            "10:30 A.M. PUBLIC WALK-IN \nNOON LUNCH \nDATE: Tuesday, November 17, 2026 \n9:00 A.M. ADMINISTRATIVE TIME \nOTHER MEETINGS: x")
    tz = ZoneInfo("America/Boise")
    (e,) = build.normalize_pdf_agenda(src, text, "https://x/a.pdf", date(2026, 11, 11), date(2027, 1, 1), tz)
    assert e["start"] == "2026-11-16T08:30:00-07:00" and e["highlights"] == ["Tax deed public hearing"]
    page = "<div>BOARD OF LEWIS COUNTY COMMISSIONERS - MEETING AGENDA</div><p>Monday, November 16, 2026 - Regular Business Meeting</p><p>Agenda coming soon.</p><div>Public Records Request</div>"
    (m,) = build.normalize_next_meeting({"id": "lewis", "name": "Lewis County", "area": "countywide", "county": "Lewis",
                                          "meeting_title": "Board of Lewis County Commissioners"}, page, "http://p", tz)
    assert m["title"] == "Board of Lewis County Commissioners (Regular Business Meeting)" and m["all_day"] and not m["agenda_url"]


def test_ada_daily_agenda():
    src = {"id": "ada", "name": "Ada County", "area": "countywide", "county": "Ada", "homepage": "https://h",
           "default_location": "Room 3255", "hearing_location": "1st Floor Public Hearing Room"}
    text = ("IV. NEW BUSINESS \n 9:00 AM \u2022 Open Business Meeting (see separate agenda) * \n 9:15 AM   \u2022     Emergency Medical Services District Open Business Meeting  \n"
            "   (see separate agenda) * \n 9:30 AM \u2022 Legal Staff/Executive Session \n 6:00 PM \u2022 Public Hearing - Public Hearing Room (see separate agenda) * \nV. ADJOURNMENT")
    files = {"11-17-26_Open_Business_Mtg.pdf": "https://a/obm", "11-17-26_Public_Hearing_with_Staff_Links.pdf": "https://a/ph"}
    evs = build.normalize_ada_daily(src, text, date(2026, 11, 17), files, ZoneInfo("America/Boise"))
    assert [e["title"] for e in evs] == ["Board of County Commissioners: Open Business Meeting",
                                         "Board of County Commissioners: Emergency Medical Services District Open Business Meeting",
                                         "Board of County Commissioners: Public Hearing"]
    assert evs[0]["agenda_url"] == "https://a/obm" and evs[2]["location"] == "1st Floor Public Hearing Room" and evs[2]["start"].endswith("18:00:00-07:00")
    hearing = "1. 202300532-MSP-TE, KM ENGINEERING: Board-level Time Extension request to complete improvements. The property is"
    assert build.HEARING_ITEM.findall(hearing) == ["Board-level Time Extension request to complete improvements."]


def test_schedule_holiday_moves_to_tuesday():
    src = {"id": "n", "name": "Nampa", "area": "Nampa", "county": "Canyon",
           "meetings": [{"title": "City Council", "when": "1st, 3rd Monday", "time": "17:00", "holiday_moves_to_next_day": True}]}
    evs = build.fetch_schedule(src, date(2027, 1, 1), date(2027, 1, 31), ZoneInfo("America/Boise"))
    assert [e["start"][:10] for e in evs] == ["2027-01-04", "2027-01-19"]  # MLK Day, Jan 18, moves to Tuesday


def test_escribe():
    src = {"id": "boise", "name": "City of Boise", "area": "Boise", "county": "Ada", "site": "https://pub-cityofboise.escribemeetings.com"}
    rows = [{"MeetingName": "Ethics Commission", "StartDate": "2026/11/12 15:30:15", "EndDate": "2026/11/12 16:30:15", "ID": "a",
             "Location": "City Hall", "Url": "", "MeetingDocumentLink": [{"Title": "Meeting Cancelled - Click for Details", "Type": "AdditionalDocuments", "Url": "/FileStream.ashx?DocumentId=913"}]},
            {"MeetingName": "Library Board of Trustees", "StartDate": "2026/12/09 11:30:00", "EndDate": "2026/12/09 13:00:00", "ID": "b", "Location": "Main Library",
             "Url": "https://x/Meeting?Id=b", "MeetingDocumentLink": [{"Title": "Agenda Full Package (HTML)", "Type": "Agenda", "Format": "HTML", "Url": "/Meeting.aspx?Id=b&Agenda=Agenda"}]}]
    a, b = build.normalize_escribe(src, rows, ZoneInfo("America/Boise"))
    assert a["cancelled"] and not b["cancelled"] and b["start"] == "2026-12-09T11:30:00-07:00"
    assert b["agenda_url"] == "https://pub-cityofboise.escribemeetings.com/Meeting.aspx?Id=b&Agenda=Agenda"
    page = '<div class="AgendaItemTitle">1.</div><div class="AgendaItemTitle">CALL TO ORDER</div><div class="AgendaItemTitle">2.1</div><div class="AgendaItemTitle"><a>2026 YMCA Christmas Run (10 minutes)</a></div>'
    assert build.escribe_items(page) == ["2026 YMCA Christmas Run (10 minutes)"]


def test_simbli():
    src = {"id": "d91", "name": "Idaho Falls School District 91", "area": "Idaho Falls", "county": "Bonneville", "listing": "https://l"}
    page = ("<tr><td>12/09/2026 - 05:30 PM</td><td>Board Business Meeting</td><td>UnPublished</td><td>Board Business Meeting</td></tr>"
            "<tr><td>11/04/2026 - 12:00 PM</td><td>Notice of Quorum</td><td>UnPublished</td><td>Notice of Quorum</td></tr>")
    (e,) = build.normalize_simbli(src, page, date(2026, 11, 1), date(2027, 1, 1), ZoneInfo("America/Boise"))
    assert e["title"] == "Board Business Meeting" and e["start"] == "2026-12-09T17:30:00-07:00"


def test_notice_page():
    src = {"id": "bsd", "name": "Boise School District", "area": "Boise", "county": "Ada", "page": "https://www.boiseschools.org/boardmeetingnotice", "category": "school"}
    page = ("<p>BOARD WORKSHOP</p><p>Date: November 9, 2026</p><p>Time: 5:40 PM</p><p>Location: District Service Center</p><p>8169 W Victory Rd</p><p><a href='/a1.pdf'>Agenda</a></p>"
            "<p>REGULAR BOARD MEETING</p><p>Date: November 9, 2026</p><p>Time: 6:00 PM</p><p>Location: District Service Center 8169 W Victory Rd Boise, Idaho</p><p><a href=\"/a2.pdf\">Agenda</a></p>")
    a, b = build.normalize_notice_page(src, page.replace("'", '"'), ZoneInfo("America/Boise"))
    assert b["title"] == "Board of Trustees: Regular Board Meeting" and b["start"] == "2026-11-09T18:00:00-07:00"
    assert b["agenda_url"] == "https://www.boiseschools.org/a2.pdf" and b["location"].startswith("District Service Center")


def test_legislature_links_and_bills():
    page = ("<article id='mc_calendar_18_2676-calendar-2676' class='x'><p><a href=\"https://legislature.idaho.gov/wp-content/uploads/a.pdf\" target=\"_blank\">Agenda "
            "<span>(PDF)</span></a><br /><a href=\"https://legislature.idaho.gov/sessioninfo/2026/joint/jloc\">Committee Information</a></p></article>")
    assert build.legislature_links(page) == {"2676": ("https://legislature.idaho.gov/wp-content/uploads/a.pdf", "https://legislature.idaho.gov/sessioninfo/2026/joint/jloc")}
    text = "AGENDA\nH 12   Relating to sales tax on groceries   Rep. Smith\nS 1045aa   Relating to school facilities\nMINUTES"
    assert build.legislature_bills(text) == ["H 12: Relating to sales tax on groceries   Rep. Smith".replace("   ", " "), "S 1045aa: Relating to school facilities"]


def test_upkeep_items():
    import alerts
    cfg = {"sources": [
        {"id": "f", "name": "Fremont County", "homepage": "h", "meetings": [{"title": "BOCC", "dates": ["2026-11-16", "2026-11-23"]}]},
        {"id": "r", "name": "Rathdrum", "meetings": [{"title": "Council", "when": "2nd Wednesday"}]},
        {"id": "b", "name": "Boise", "review_by": "2027-01-13", "review_note": "move"}]}
    items = alerts.upkeep_items(cfg, date(2026, 11, 17))
    assert len(items) == 1 and "Fremont County" in items[0] and "2026-11-23" in items[0]
    assert len(alerts.upkeep_items(cfg, date(2026, 12, 30))) == 2


def test_sanity_checks():
    import checks
    events = [{"source": "a", "start": "2026-11-20T18:00:00-07:00", "title": "Council", "all_day": False},
              {"source": "a", "start": "2026-11-20T18:00:00-07:00", "title": "Council ", "all_day": False},
              {"source": "b", "start": "2026-11-21T03:00:00-07:00", "title": "Board", "all_day": False, "tz": "MT"}]
    status = {"sources": [{"id": "c", "name": "C", "count": 0, "state": "quiet"}]}
    out = checks.sanity(events, status, {"sources": [{"id": "c", "count": 9}]})
    assert any("Listed twice" in x for x in out) and any("Odd hour" in x for x in out) and any("Went quiet" in x for x in out)


def test_whats_new_feed(tmp_path):
    seen = {}
    e = {"id": "x1", "title": "City Council", "host": "City of Boise", "start": "2026-11-23T18:00:00-07:00", "all_day": False,
         "tz": "MT", "location": "City Hall", "url": "https://u", "agenda_url": "", "county": "Ada"}
    assert [k for k, _, _ in build.update_seen([e], seen, "2026-11-17")] == ["new"]
    assert build.update_seen([e], seen, "2026-11-18") == []
    e2 = dict(e, agenda_url="https://a.pdf")
    news = build.update_seen([e2], seen, "2026-11-19")
    assert [k for k, _, _ in news] == ["agenda"]
    build.write_feed(tmp_path / "f.xml", "T", news, "https://civicsid.org/", "2026-11-19T00:00:00")
    feed = (tmp_path / "f.xml").read_text()
    assert "Agenda posted: City Council (2026-11-23 18:00)" in feed and 'href="https://a.pdf"' in feed
    from xml.dom import minidom
    minidom.parseString(feed)


# --- Security: event text comes from outside sites and is never trusted ---

def test_safe_link_rejects_non_web_schemes():
    for bad in ["javascript:alert(1)", "JaVaScRiPt:alert(1)", "data:text/html,x", "mailto:a@b.c",
                "vbscript:x", "https://x.org/a b", 'https://x.org/"onmouseover=1', ""]:
        assert build.safe_link(bad) == "", bad
    assert build.safe_link("https://x.org/a?b=1") == "https://x.org/a?b=1"
    assert build.safe_link("/Calendar.aspx?EID=5", "https://city.org") == "https://city.org/Calendar.aspx?EID=5"
    assert build.safe_link("javascript:alert(1)", "https://city.org") == ""


def test_clean_event_strips_control_chars_and_fills_link():
    e = {"title": "Council\x0b Meeting", "url": "javascript:alert(1)", "agenda_url": "/a.pdf",
         "highlights": ["Item\x00 one"], "location": "Hall\x1f"}
    build.clean_event(e, {"site": "https://city.org", "homepage": "https://city.org/council"})
    assert e["title"] == "Council Meeting" and e["location"] == "Hall" and e["highlights"] == ["Item one"]
    assert e["url"] == "https://city.org/council"
    assert e["agenda_url"] == "https://city.org/a.pdf"


def test_feed_escapes_quotes_and_markup(tmp_path):
    import xml.etree.ElementTree as ET
    e = {"id": "x1", "title": 'A <b>"quoted"</b> & \x0c title', "host": "City", "start": "2026-12-01T18:00:00-07:00",
         "all_day": False, "tz": "MT", "location": "", "url": 'https://x.org/?a="1"><script>', "agenda_url": ""}
    build.write_feed(tmp_path / "f.xml", "T", [("new", "2026-11-19", e)], "https://civicsid.org/", "2026-11-19T00:00:00Z")
    root = ET.parse(tmp_path / "f.xml").getroot()  # must still be well-formed XML
    ns = "{http://www.w3.org/2005/Atom}"
    entry = root.find(ns + "entry")
    assert "<b>" in entry.find(ns + "title").text  # shown as text, not markup
    assert entry.find(ns + "link").get("href") == "https://civicsid.org/"  # unsafe link replaced


def test_ics_folds_long_lines_and_marks_cancellations(tmp_path):
    from datetime import datetime, timezone
    e = {"id": "x2", "title": "Ü" * 80, "host": "City", "start": "2026-12-01T18:00:00-07:00", "end": None,
         "all_day": False, "cancelled": True, "location": "Hall; Room 1, upstairs\nside door", "url": "https://x.org/e"}
    path = tmp_path / "c.ics"
    build.write_ics([e], path, datetime(2026, 11, 19, tzinfo=timezone.utc))
    raw = path.read_bytes()
    assert all(len(line) <= 75 for line in raw.split(b"\r\n"))
    text = raw.decode("utf-8")
    assert "STATUS:CANCELLED" in text
    assert r"LOCATION:Hall\; Room 1\, upstairs\nside door" in text.replace("\r\n ", "")
    import icalendar
    cal = icalendar.Calendar.from_ical(text)
    ev = cal.walk("VEVENT")[0]
    assert str(ev["SUMMARY"]).startswith("CANCELLED: " + "Ü" * 10)


CIVICPLUS_PAGE = """<div><h2 class="title">Main Calendar</h2></div><ol>
<li>
  <h3> <a id="eventTitle_793" href="/Calendar.aspx?EID=793&month=11&year=2026&day=17&calType=0"><span>City Council Meeting</span></a></h3>
</a></h3>
<div class="subHeader"><div class="date">November&nbsp;17,&nbsp;2026,&nbsp;5:30 PM&thinsp;-&thinsp;8:00 PM</div><div class="eventLocation fr-element fr-view">@ <div class="name"><p>Jerome Council Chambers</p></div></div></div>
<div class="hidden" itemscope itemtype="http://schema.org/Event"><span itemprop="name">City Council Meeting</span><span itemprop="startDate" class="hidden">2026-11-17T17:30:00</span><p itemprop="description"></p>
<span itemprop="location" itemscope itemtype="http://schema.org/Place">
<span itemprop="name"><p>Jerome Council Chambers</p></span><span class="hidden" itemprop="address" itemscope itemtype="http://schema.org/PostalAddress"><span itemprop="streetAddress">100 E Avenue A</span></span></span></div><p></p>
<a href="/Calendar.aspx?EID=793&month=11&year=2026&day=17&calType=0">More Details</a>
</li>
<li>
  <h3> <a id="eventTitle_718" href="/Calendar.aspx?EID=718"><span>Planning &amp; Zoning Meeting - CANCELLED</span></a></h3>
<div class="subHeader"><div class="date">December&nbsp;8,&nbsp;2026,&nbsp;6:00 PM</div></div>
<div class="hidden" itemscope itemtype="http://schema.org/Event"><span itemprop="name">Planning &amp; Zoning Meeting - CANCELLED</span><span itemprop="startDate" class="hidden">2026-12-08T18:00:00</span></div>
</li>
<li>
  <h3> <a id="eventTitle_900" href="/Calendar.aspx?EID=900"><span>Thanksgiving - City Offices Closed</span></a></h3>
<div class="subHeader"><div class="date">November&nbsp;26,&nbsp;2026</div></div>
<div class="hidden" itemscope itemtype="http://schema.org/Event"><span itemprop="name">Thanksgiving - City Offices Closed</span><span itemprop="startDate" class="hidden">2026-11-26T00:00:00</span></div>
</li></ol>"""


def test_civicplus_calendar_page():
    src = {"id": "jerome", "name": "City of Jerome", "area": "Jerome", "timezone": "America/Boise"}
    tz = ZoneInfo("America/Boise")
    events = build.normalize_civicplus(src, CIVICPLUS_PAGE, tz, "https://www.ci.jerome.id.us", 14)
    assert [e["title"] for e in events] == ["City Council Meeting", "Planning & Zoning Meeting",
                                             "Thanksgiving - City Offices Closed"]
    council, pz, holiday = events
    assert council["start"] == "2026-11-17T17:30:00-07:00" and council["end"] == "2026-11-17T20:00:00-07:00"
    assert council["location"] == "Jerome Council Chambers, 100 E Avenue A"
    assert council["url"] == "https://www.ci.jerome.id.us/Calendar.aspx?EID=793"
    assert pz["cancelled"] and pz["end"] is None and not pz["all_day"]
    assert holiday["all_day"]
    assert build.CLOSURE_TITLE.search(holiday["title"])  # fetch_civicplus drops these


def test_robots_gate(monkeypatch):
    class Resp:
        def __init__(self, status, text=""):
            self.status_code, self.text, self.ok = status, text, status < 400
            self.headers = {"Content-Type": "text/plain"}
    robots = ("User-agent: GPTBot\nDisallow: /calendar.aspx\n"
              "User-agent: *\nDisallow: /common/modules/icalendar/\nDisallow: /Search\n")
    import requests
    monkeypatch.setattr(requests, "get", lambda url, **kw: Resp(200, robots))
    build._robots_cache.clear()
    build.check_robots("https://city.gov/Calendar.aspx?CID=14")          # allowed for us
    for blocked in ["https://city.gov/common/modules/iCalendar/iCalendar.aspx?catID=1",  # case-insensitive
                    "https://city.gov/search?q=x"]:
        try:
            build.check_robots(blocked)
            assert False, blocked
        except build.RobotsBlocked:
            pass
    monkeypatch.setattr(requests, "get", lambda url, **kw: Resp(404))
    build._robots_cache.clear()
    build.check_robots("https://other.gov/anything")  # no robots.txt: everything allowed
    monkeypatch.setattr(requests, "get", lambda url, **kw: Resp(503))
    build._robots_cache.clear()
    try:
        build.check_robots("https://down.gov/x")
        assert False
    except build.RobotsUnavailable:
        pass
    build._robots_cache.clear()


def test_carry_over_seen_keeps_history_when_ids_change():
    old = [{"id": "old1", "source": "kc", "start": "2026-12-01T09:00:00-08:00", "title": "Board Meeting"}]
    new = [{"id": "new1", "source": "kc", "start": "2026-12-01T09:00:00-08:00", "title": "Board  meeting"}]
    seen = {"old1": {"first": "0000-00-00"}}
    build.carry_over_seen(new, old, seen)
    assert seen["new1"] == {"first": "0000-00-00"}
    assert build.update_seen(new, seen, "2026-11-18") == []


# Star: list layout without schema.org markup
CIVICPLUS_PLAIN_LIST = """<div id="CID22" class="calendar"><div><h2 class="title">City Council Meetings</h2></div><ol>
<li>
  <h3> <a id="eventTitle_343" href="/Calendar.aspx?EID=343&month=11&year=2026&day=17&calType=0"><span>City Council Meeting</span></a></h3>
</a></h3>
<div class="subHeader"><div class="date">December&nbsp;1,&nbsp;2026,&nbsp;7:00 PM</div></div>
<p></p>
<a aria-labelledby="eventTitle_343 calendarEvent343"id="calendarEvent343" href="/Calendar.aspx?EID=343">More Details</a>
</li>
<li>
  <h3> <a id="eventTitle_393" href="/Calendar.aspx?EID=393"><span>City Council Meeting</span></a></h3>
<div class="subHeader"><div class="date">December&nbsp;15,&nbsp;2026,&nbsp;7:00 PM</div></div>
</li></ol></div>"""

# Kootenai County: month grid, each event with a pop-up and a hidden schema block
CIVICPLUS_GRID = """<a href="/Calendar.aspx?EID=4883"><span itemprop="name">BOCC: Status Update || CANCELLED</span></a>
<div style="display:none;" name="showDetailsBox" id="showDetails4883_2" class="detailsTooltip"><div class="tooltipInner">
<h3 id="eventTitle_4883" class="dim">BOCC: Status Update || CANCELLED</h3><dl><dt>When:</dt><dd>10:00 AM&thinsp;-&thinsp;11:00 AM</dd></dl>
<a aria-labelledby="eventTitle_4883 calendarEvent4883"id="calendarEvent4883" href="/Calendar.aspx?EID=4883">More Details</a></div></div>
<div style="display: none;" class="hidden"><div class="subHeader"><div class="date">November&nbsp;3,&nbsp;2026,&nbsp;10:00 AM&thinsp;-&thinsp;11:00 AM</div></div>
<div class="hidden" itemscope itemtype="http://schema.org/Event"><span itemprop="name">BOCC: Status Update || CANCELLED</span><span itemprop="startDate" class="hidden">2026-11-03T10:00:00</span>
<span itemprop="location" itemscope itemtype="http://schema.org/Place"><span itemprop="name">Event Location</span><span class="hidden" itemprop="address" itemscope><span itemprop="streetAddress">451 Government Way</span></span></span></div></div>
<h3 id="eventTitle_4890" class="dim">Planning Commission</h3>
<div class="subHeader"><div class="date">November&nbsp;12,&nbsp;2026,&nbsp;6:00 PM</div></div>
<span itemprop="location"><span itemprop="name">Ketchum City Hall</span><span itemprop="streetAddress">P.O. Box 2315</span></span>"""


def test_civicplus_other_layouts():
    tz = ZoneInfo("America/Boise")
    src = {"id": "star", "name": "City of Star", "area": "Star"}
    plain = build.normalize_civicplus(src, CIVICPLUS_PLAIN_LIST, tz, "https://www.staridaho.org", 22)
    assert [(e["start"], e["title"]) for e in plain] == [
        ("2026-12-01T19:00:00-07:00", "City Council Meeting"), ("2026-12-15T19:00:00-07:00", "City Council Meeting")]
    src = {"id": "kootenai-county", "name": "Kootenai County", "area": "countywide"}
    grid = build.normalize_civicplus(src, CIVICPLUS_GRID, ZoneInfo("America/Los_Angeles"), "https://www.kcgov.us", 22)
    assert len(grid) == 2
    bocc, pc = grid
    assert bocc["title"] == "BOCC: Status Update" and bocc["cancelled"]
    assert bocc["end"] == "2026-11-03T11:00:00-08:00" and bocc["location"] == "451 Government Way"
    assert pc["location"] == "Ketchum City Hall"  # P.O. box isn't a place to go


def test_civicplus_new_calendar_json():
    items = [
        {"id": "746", "title": "City Council Meeting", "start": "2026-12-01T17:30:00", "end": None, "allDay": False,
         "extendedProps": {"location": "Jerome Council Chambers", "time": "5:30p - 8p",
                           "navigationUrl": "/m/calendar/event/detail/746"}},
        {"id": "718", "title": "Planning & Zoning Meeting - CANCELLED", "start": "2026-12-08T18:00:00", "end": None,
         "allDay": False, "extendedProps": {"location": "", "time": "6p", "navigationUrl": "/m/calendar/event/detail/718"}},
        {"id": "900", "title": "Christmas", "start": "2026-12-25T00:00:00", "end": None, "allDay": True, "extendedProps": {}},
    ]
    src = {"id": "jerome", "name": "City of Jerome", "area": "Jerome"}
    ev = build.normalize_civicplus_json(src, items, ZoneInfo("America/Boise"), "https://www.ci.jerome.id.us")
    council, pz, xmas = ev
    assert council["start"] == "2026-12-01T17:30:00-07:00" and council["end"] == "2026-12-01T20:00:00-07:00"
    assert council["url"] == "https://www.ci.jerome.id.us/m/calendar/event/detail/746"
    assert pz["title"] == "Planning & Zoning Meeting" and pz["cancelled"] and pz["end"] is None
    assert xmas["all_day"]
    # Same uid scheme as the classic calendar, so a site switching over keeps its ids
    old = build.make_event(src, title="City Council Meeting", start=datetime(2026, 12, 1, 17, 30, tzinfo=ZoneInfo("America/Boise")),
                           uid="civicplus-746")
    assert old["id"] == council["id"]


def test_tyler_meeting_manager():
    items = [
        {"id": "a1", "meetingTypeId": 3, "meetingTitle": "Board of Commissioners Regular Meeting",
         "actualStartDate": "2026-11-24 00:00:00.0", "startTime": "09:00 AM", "endTime": "10:00 AM",
         "location": "Commissioners Hearing Room, Bonneville County Courthouse", "canceled": False,
         "agendaItemTitles": ["Review/Approval of Claims, as needed", "Review/Decision on Stop-Loss Reinsurance (ACTION ITEM)"]},
        {"id": "a2", "meetingTypeId": 3, "meetingTitle": "Board of Commissioners Regular Meeting",
         "actualStartDate": "2026-11-25 00:00:00.0", "startTime": "9:00 AM", "endTime": "12:00 PM", "agendaItemTitles": None},
        {"id": "a3", "meetingTypeId": 9, "meetingTitle": "Rotary Club", "actualStartDate": "2026-11-25 00:00:00.0",
         "startTime": "12:00 PM", "endTime": "1:00 PM"},
        {"id": "a4", "meetingTypeId": 4, "meetingTitle": "Planning & Zoning Commission", "actualStartDate": "2026-12-03 00:00:00.0",
         "startTime": "7:00 PM", "endTime": "09:00 PM", "canceled": True},
    ]
    src = {"id": "bonneville-county", "name": "Bonneville County", "area": "countywide",
           "meeting_types": [3, 4], "agenda_only": [3], "homepage": "https://example.gov/calendar"}
    ev = build.normalize_tyler_mm(src, items, ZoneInfo("America/Boise"))
    assert [e["title"] for e in ev] == ["Board of Commissioners Regular Meeting", "Planning & Zoning Commission"]
    bocc, pz = ev
    assert bocc["start"] == "2026-11-24T09:00:00-07:00" and bocc["end"] == "2026-11-24T10:00:00-07:00"
    assert bocc["highlights"][1].startswith("Review/Decision on Stop-Loss")
    assert pz["cancelled"] and pz["start"] == "2026-12-03T19:00:00-07:00"


TF_AGENDA = """Executive Sessions may be held pursuant to Idaho Code §74-206 as needed during regularly scheduled meetings.  The
purpose of such sessions shall be announced at the time such sessions are called.  **ACTION ITEM**
Agenda
Tuesday, November 24, 2026
Items marked with ** indicate an Action Item.
Call to Order.
7:00 a.m. Commissioner Hawkins to attend a Rotary meeting.
  9:00 a.m. **Consider approval of the canvass of the November 3 election.
 10:15 a.m. **Public hearing: Rezone request, 3600 N Rd.
 1:30 p.m. Commissioners to attend a tour of the Valley House properties.
"""


def test_twin_falls_daily_agenda():
    src = {"id": "twin-falls-county", "name": "Twin Falls County", "area": "countywide",
           "default_location": "630 Addison Ave W., Twin Falls", "homepage": "https://twinfallscounty.org/commissioners/agenda/"}
    tz = ZoneInfo("America/Boise")
    ev = build.normalize_daily_agenda(src, TF_AGENDA, date(2026, 11, 24), "https://twinfallscounty.org/a.pdf", tz)
    assert len(ev) == 1
    assert ev[0]["start"] == "2026-11-24T09:00:00-07:00"
    assert ev[0]["highlights"] == ["Consider approval of the canvass of the November 3 election",
                                   "Public hearing: Rezone request, 3600 N Rd"]
    quiet = TF_AGENDA.replace("**Consider", "Consider").replace("**Public", "Public")
    assert build.normalize_daily_agenda(src, quiet, date(2026, 11, 24), "u", tz) == []
