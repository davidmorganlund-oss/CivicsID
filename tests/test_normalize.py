"""Checks the connectors against records shaped like the real feeds.

Most samples carry over from the Washington site this pipeline began as;
the connectors are the same, so the samples still exercise them.
"""
import sys
from datetime import date
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
