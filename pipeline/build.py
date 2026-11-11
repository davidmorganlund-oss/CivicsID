"""CivicsID pipeline: read each public calendar source, normalize the events,
and write the files the site reads.

Idaho has two time zones. Each source can set its own "timezone" in
sources.yml; the default is Mountain time (America/Boise) and the ten
northern counties use Pacific (America/Los_Angeles). Event times are kept
as local wall-clock times with a "tz" label ("MT" or "PT").

Outputs (in site/data/):
  events.json    upcoming events, soonest first
  status.json    per-source health, so a quiet or broken source is visible
  ics/*.ics      subscribable calendars: statewide, the Legislature, one per county

Run:  python pipeline/build.py
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import date, datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "data"
UA = "CivicsID/0.1 (BarNone nonprofit civic calendar; contact via barnoneinc.org)"
TIMEOUT = 45


# ---------- shared helpers ----------

CATEGORY_RULES = [
    ("hearing", r"\bhearing"),
    ("school", r"\bschool\b"),
    ("council", r"council|commission|board|committee|authority|district|agency|panel|work ?session|study session"),
    ("library", r"\blibrary\b"),
]


def categorize(text: str) -> str:
    low = (text or "").lower()
    for cat, pattern in CATEGORY_RULES:
        if re.search(pattern, low):
            return cat
    return "other"


def is_cancelled(*texts: str) -> bool:
    return any(re.search(r"cancel", t or "", re.I) for t in texts)


def make_event(src, *, title, start, end=None, all_day=False, location="", url="",
               agenda_url="", note="", uid="", category="", area="", cancelled=False):
    key = f"{src['id']}|{uid or title}|{start.isoformat()}"
    cancelled = cancelled or is_cancelled(title, note)
    # Hosts often prefix the title ("Canceled: Board Work Session"); the site
    # shows its own Cancelled tag, so drop the prefix.
    title = re.sub(r"^[\s*]*cancel+ed[\s*]*(?:[:\-–]\s*|\s+(?=\S))", "", title or "", flags=re.I)
    title = re.sub(r"\s*(?:[-–:(]|\|+)\s*cancel+ed\s*\)?\s*$", "", title, flags=re.I)
    # Some calendars put HTML or stray separators in the location field.
    location = re.sub(r"<[^>]+>", " ", location or "")
    location = re.sub(r"^[\s\-–,]+|[\s\-–,]+$", "", " ".join(location.split()))
    return {
        "id": hashlib.sha1(key.encode()).hexdigest()[:12],
        "title": " ".join((title or "").split()),
        "host": src["name"],
        "source": src["id"],
        "area": area or src["area"],
        "county": src.get("county", ""),
        "tz": "PT" if src.get("timezone") == "America/Los_Angeles" else "MT",
        "category": category or categorize(title),
        "start": start.isoformat(),
        "end": end.isoformat() if end else None,
        "all_day": all_day,
        "location": " ".join((location or "").split()),
        "url": url or src.get("homepage", ""),
        "agenda_url": agenda_url or "",
        "note": " ".join((note or "").split()),
        "cancelled": cancelled,
    }


def get(url, params=None):
    import requests
    resp = requests.get(url, params=params, headers={"User-Agent": UA}, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp


# ---------- agenda highlights ----------
# For systems that publish agenda items, show the few substantive ones so a
# listing says what is being decided, not just that a meeting exists.

PROCEDURAL = re.compile(
    r"^(call(ed)? to order|roll call|pledge|flag salute|land acknowledg|we, the city|approval of (the )?"
    r"(agenda|minutes|.*minutes$)|approve the (agenda|minutes)|adopt(ion of)? (the )?(agenda|minutes)|"
    r"public comment|citizen comment|adjourn|recess|good of the order|executive session|vote requested|"
    r"hybrid meeting|connecting to|webinar|see attached|this meeting (has been|will be)|properly noticed|"
    r"item no|agenda review|adoption of (the )?(introduction|consent|agenda)|join (the )?(meeting|zoom)|"
    r"the .{0,80}meeting scheduled for|the public can (participate|attend|watch)|excused absences|"
    r"confirm(ation of)? (the )?agenda|minutes of|calendar ?/ ?correspondence|page break|reminder|"
    r"record of hearing|approval of (the )?.*(agenda|minutes)$|(city )?council action updates?|"
    r"(intergovernmental|outside|committee|staff|board|member|commissioner)s?(/[a-z ]+)? (committee )?updates?$|"
    r"administrative items|public access time|issue briefing$)", re.I)
TIME_PREFIX = re.compile(r"^\d{1,2}(:\d{2})?\s*[ap]\.?m\.?(\s*[–-]\s*\d{1,2}(:\d{2})?\s*[ap]\.?m\.?)?\s*[–:-]?\s*", re.I)
# Section headings that only count as procedure when they are the whole item.
HEADING = re.compile(
    r"^((regular |special )?minutes|public (comment|testimony)|announcements?|(staff )?reports?|"
    r"(chair|director|commissioners?|council ?members?|mayor|manager|staff|council)('?s)?( (report|comments|update)s?)?|"
    r"other (topics|business|items)|upcoming|consent (agenda|calendar)|introduction and referral( calendar)?|"
    r"items of interest|correspondence|(unfinished|old|new) business|business items|action items|"
    r"discussion items|public hearings?|work session|study session|introductions?( of members)?|committee discussion|wrap[- ]up|next steps|closing remarks|welcome( and introductions)?)$", re.I)
HIGHLIGHT_WINDOW_DAYS = 21
HIGHLIGHT_COUNT = 3


def clean_item(text: str) -> str:
    import html as htmllib
    text = re.split(r"<br\s*/?>|\r|\n", text or "", maxsplit=1)[0]
    text = htmllib.unescape(re.sub(r"<[^>]+>", " ", text))
    text = " ".join(text.replace("*", " ").split()).strip(" :.-")
    text = TIME_PREFIX.sub("", text)
    if len(text) > 140:
        text = text[:140].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return text


def pick_highlights(titles):
    picked = []
    for t in titles:
        t = clean_item(t)
        shouting = t.isupper() and len(t.split()) <= 4 and not re.search(r"\d", t)  # an all-caps heading
        if len(t) < 6 or shouting or PROCEDURAL.match(t) or HEADING.match(t) or t in picked:
            continue
        picked.append(t)
    return picked


def add_highlights(event, titles):
    items = pick_highlights(titles)
    if items:
        event["highlights"] = items[:HIGHLIGHT_COUNT]
        event["highlights_more"] = max(0, len(items) - HIGHLIGHT_COUNT)


def soon(event, start_day):
    return datetime.fromisoformat(event["start"]).date() <= start_day + timedelta(days=HIGHLIGHT_WINDOW_DAYS)


def legistar_highlights(src, events, start_day):
    for e in events:
        if e["cancelled"] or not soon(e, start_day) or not e.get("_eid"):
            continue
        try:
            items = get(f"https://webapi.legistar.com/v1/{src['client']}/events/{e['_eid']}/eventitems",
                        {"AgendaNote": 1, "MinutesNote": 0, "Attachments": 0}).json()
        except Exception as exc:
            print(f"[info] {src['id']}: no agenda items for {e['_eid']}: {exc}", file=sys.stderr)
            continue
        # When an agenda has items tied to legislative files (bills, resolutions,
        # hearings), those are the decisions; the rest are headings and notices.
        filed = [i for i in items if i.get("EventItemMatterFile")]
        items = sorted(filed or items, key=lambda i: i.get("EventItemAgendaSequence") or 0)
        add_highlights(e, [i.get("EventItemTitle") or "" for i in items
                           if (i.get("EventItemMatterType") or "").lower() != "minutes"])


def civicclerk_highlights(src, events, start_day):
    for e in events:
        if e["cancelled"] or not soon(e, start_day) or not e.get("_agenda"):
            continue
        try:
            meeting = get(f"https://{src['tenant']}.api.civicclerk.com/v1/Meetings/{e['_agenda']}").json()
        except Exception as exc:
            print(f"[info] {src['id']}: no agenda for {e['_agenda']}: {exc}", file=sys.stderr)
            continue
        if not meeting.get("agendaIsPublish"):
            continue  # draft agendas are not public yet
        titles = []

        def walk(items, section=""):
            for i in items or []:
                name = i.get("agendaObjectItemName") or ""
                if i.get("isSection"):
                    walk(i.get("childItems"), name)
                    continue
                if re.search(r"report|minutes|consent", section, re.I):
                    continue
                titles.append(name)
                walk(i.get("childItems"), section)

        walk(meeting.get("items"))
        add_highlights(e, titles)


# ---------- connectors ----------

def parse_clock(text: str):
    """'5:30 PM' -> time(17, 30). Returns None when there is no usable time."""
    m = re.match(r"\s*(\d{1,2})(?::(\d{2}))?\s*([AaPp])\.?[Mm]\.?", text or "")
    if not m:
        return None
    hour = int(m.group(1)) % 12 + (12 if m.group(3).lower() == "p" else 0)
    return time(hour, int(m.group(2) or 0))


def normalize_legistar(src, rows, tz):
    events = []
    for r in rows:
        day = datetime.fromisoformat(r["EventDate"]).date()
        clock = parse_clock(r.get("EventTime"))
        start = datetime.combine(day, clock or time(0, 0), tz)
        events.append(make_event(
            src,
            title=r.get("EventBodyName") or "Public meeting",
            start=start,
            all_day=clock is None,
            location=r.get("EventLocation") or "",
            url=r.get("EventInSiteURL") or "",
            agenda_url=r.get("EventAgendaFile") or "",
            note=r.get("EventComment") or "",
            uid=str(r.get("EventId", "")),
        ))
        events[-1]["_eid"] = r.get("EventId")
    return events


def fetch_legistar(src, start_day, end_day, tz):
    flt = (f"EventDate ge datetime'{start_day.isoformat()}' and "
           f"EventDate le datetime'{end_day.isoformat()}'")
    rows = get(f"https://webapi.legistar.com/v1/{src['client']}/events",
               {"$filter": flt, "$orderby": "EventDate"}).json()
    events = normalize_legistar(src, rows, tz)
    legistar_highlights(src, events, start_day)
    return events


def normalize_civicclerk(src, rows, tz):
    events = []
    for r in rows:
        if r.get("isDeleted") or r.get("isPublished") is False:
            continue
        # CivicClerk labels its times "Z" but they are local wall-clock times
        # (Lacey's 6 p.m. council meetings come through as 18:00:00Z).
        raw = (r.get("startDateTime") or "")[:19]
        if not raw:
            continue
        start = datetime.fromisoformat(raw).replace(tzinfo=tz)
        loc = r.get("eventLocation") or {}
        place = ", ".join(p for p in [loc.get("address1"), loc.get("address2"), loc.get("city")]
                          if p) if isinstance(loc, dict) else ""
        tenant = src["tenant"]
        events.append(make_event(
            src,
            title=r.get("eventName") or r.get("categoryName") or "Public meeting",
            start=start,
            location=place,
            url=f"https://{tenant}.portal.civicclerk.com/event/{r['id']}/overview",
            note=r.get("eventDescription") or "",
            uid=str(r["id"]),
        ))
        events[-1]["_agenda"] = r.get("agendaId")
    return events


def fetch_civicclerk(src, start_day, end_day, tz):
    flt = (f"startDateTime ge {start_day.isoformat()}T00:00:00Z and "
           f"startDateTime le {end_day.isoformat()}T23:59:59Z")
    url = f"https://{src['tenant']}.api.civicclerk.com/v1/Events"
    params = {"$filter": flt, "$orderby": "startDateTime asc"}
    rows = []
    for _ in range(20):  # follow paging, with a hard stop
        data = get(url, params).json()
        rows.extend(data.get("value", []))
        url, params = data.get("@odata.nextLink"), None
        if not url:
            break
    events = normalize_civicclerk(src, rows, tz)
    civicclerk_highlights(src, events, start_day)
    return events


def normalize_ics(src, ics_text, start_day, end_day, tz):
    import html as htmllib
    import icalendar
    import recurring_ical_events

    cal = icalendar.Calendar.from_ical(ics_text)
    window_start = datetime.combine(start_day, time(0, 0), tz)
    window_end = datetime.combine(end_day, time(23, 59), tz)
    events = []
    for comp in recurring_ical_events.of(cal).between(window_start, window_end):
        raw_start = comp["DTSTART"].dt
        raw_end = comp["DTEND"].dt if comp.get("DTEND") else None
        all_day = not isinstance(raw_start, datetime)

        def local(value):
            if value is None:
                return None
            if not isinstance(value, datetime):
                return datetime.combine(value, time(0, 0), tz)
            return value.astimezone(tz) if value.tzinfo else value.replace(tzinfo=tz)

        title = str(comp.get("SUMMARY", "")).strip()
        if not title or title.lower() in {"busy", "free", "tentative"}:
            continue  # published Outlook calendars can hide titles
        events.append(make_event(
            src,
            title=title,
            start=local(raw_start),
            end=local(raw_end),
            all_day=all_day,
            location=str(comp.get("LOCATION", "")),
            url=htmllib.unescape(str(comp.get("URL", ""))) or src.get("homepage", ""),
            uid=str(comp.get("UID", "")),
        ))
    return events


def fetch_ics(src, start_day, end_day, tz):
    return normalize_ics(src, get(src["url"]).content, start_day, end_day, tz)


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def fields(element) -> dict:
    """Child elements of an XML node as {name: text}; repeated names become lists."""
    out: dict = {}
    for child in element:
        name, text = local(child.tag), (child.text or "").strip()
        if name in out:
            out[name] = (out[name] if isinstance(out[name], list) else [out[name]]) + [text]
        else:
            out[name] = text
    return out


def rss_items(xml_text):
    import xml.etree.ElementTree as ET
    return [el for el in ET.fromstring(xml_text).iter() if local(el.tag) == "item"]


# --- BiblioCommons library events (RSS) ---

CIVIC_TITLE = re.compile(
    r"civic|\bvot(e|er|ers|ing)\b|election|ballot|legislat|city council|town hall|candidate|"
    r"citizenship|naturalization|government|public comment|public hearing|budget hearing|"
    r"board of trustees|community forum|listening session|advocacy", re.I)


def library_event_is_civic(title: str, categories: list) -> bool:
    if "Board Meetings" in categories or CIVIC_TITLE.search(title or ""):
        return True
    return "Friends of the Library" in categories and "meeting" in (title or "").lower()


def normalize_bibliocommons(src, xml_text, tz):
    events = []
    areas = src.get("city_areas", {})
    for item in rss_items(xml_text):
        f = fields(item)
        cats = f.get("category", [])
        cats = cats if isinstance(cats, list) else [cats]
        title = f.get("title", "")
        raw = f.get("start_date_local", "")
        if not raw or not library_event_is_civic(title, cats):
            continue
        all_day = "T" not in raw
        start = datetime.fromisoformat(raw if not all_day else raw + "T00:00").replace(tzinfo=tz)
        end_raw = f.get("end_date_local", "")
        end = datetime.fromisoformat(end_raw).replace(tzinfo=tz) if "T" in end_raw else None
        loc_el = next((c for c in item if local(c.tag) == "location"), None)
        loc = fields(loc_el) if loc_el is not None else {}
        virtual = f.get("is_virtual") == "true"
        place = ", ".join(p for p in [
            loc.get("name", ""),
            " ".join(p for p in [loc.get("number", ""), loc.get("street", "")] if p),
            loc.get("city", "")] if p)
        board = "Board Meetings" in cats or re.search(r"trustees|budget hearing", title, re.I)
        events.append(make_event(
            src, title=title, start=start, end=end, all_day=all_day,
            location=("Online" + (" and " + place if place else "")) if virtual else place,
            url=f.get("link", ""), uid=f.get("guid", "") or f.get("link", ""),
            category=("hearing" if re.search(r"hearing", title, re.I) else "council") if board else "library",
            area="countywide" if board else areas.get(loc.get("city", ""), loc.get("city", "") or "countywide"),
            cancelled=f.get("is_cancelled") == "true",
        ))
    return events


def fetch_bibliocommons(src, start_day, end_day, tz):
    import time as clock
    base = f"https://gateway.bibliocommons.com/v2/libraries/{src['library']}/rss/events"
    queries = [{"locations": ",".join(src["locations"])}] + [{"q": q} for q in src.get("searches", [])]
    found = {}
    for query in queries:
        for page in range(1, 31):  # 25 events a page, soonest first
            xml_text = get(base, {**query, "page": page}).text
            items = rss_items(xml_text)
            for e in normalize_bibliocommons(src, xml_text, tz):
                found[e["id"]] = e
            starts = [fields(i).get("start_date_local", "")[:10] for i in items]
            if len(items) < 25 or (starts and min(s for s in starts[-5:] if s) > end_day.isoformat()):
                break
            clock.sleep(1)  # be gentle with the library's server
    return list(found.values())


# --- Municode Meetings portal (HTML table of meetings) ---

def normalize_municode(src, html_text, tz):
    import html as htmllib
    events = []
    for row in re.findall(r"<tr\b.*?</tr>", html_text, re.S):
        when = re.search(r'class="date-display-single"[^>]*content="([^"]+)"', row)
        title = re.search(r'views-field-title"[^>]*>(.*?)</td>', row, re.S)
        if not when or not title:
            continue
        start = datetime.fromisoformat(when.group(1)).astimezone(tz)
        agenda = re.search(r'views-field-field-agendas".*?href="([^"]+\.pdf)"', row, re.S)
        detail = re.search(r'views-field-view-node".*?href="([^"]+)"', row, re.S)
        name = htmllib.unescape(re.sub(r"<[^>]+>", " ", title.group(1)))
        url = htmllib.unescape(detail.group(1)) if detail else ""
        events.append(make_event(
            src, title=name, start=start,
            url=(src["url"].rstrip("/") + url) if url.startswith("/") else url,
            agenda_url=htmllib.unescape(agenda.group(1)) if agenda else "",
            uid=url or name,
        ))
    return events


def fetch_municode(src, start_day, end_day, tz):
    return normalize_municode(src, get(src["url"]).text, tz)


# --- WordPress "Modern Events Calendar" RSS (dates in mec:startDate, time in the title) ---

TIME_IN_TITLE = re.compile(r"\b\d{1,2}(?::\d{2})?\s*[ap]\.?m\.?", re.I)
TIME_RANGE = re.compile(r"\b(\d{1,2}(?::\d{2})?)\s*([ap]\.?m\.?)?\s*[–-]\s*\d{1,2}(?::\d{2})?\s*([ap]\.?m\.?)", re.I)
LEADING_DATE = re.compile(r"^[A-Z][a-z]+ \d{1,2}(?:\s*[–-]\s*[A-Z][a-z]+ \d{1,2})?, \d{4}\s*[–-]?\s*")


def normalize_mec_rss(src, xml_text, tz):
    import html as htmllib
    events = []
    for item in rss_items(xml_text):
        f = fields(item)
        day = f.get("startDate", "")
        if not day:
            continue
        raw_title = htmllib.unescape(f.get("title", ""))
        cancelled = bool(re.search(r"cancel", raw_title, re.I))
        title = re.sub(r"^\s*(cancel+ed|updated)\s*:\s*", "", raw_title, flags=re.I)
        title = LEADING_DATE.sub("", title)
        span = TIME_RANGE.search(title)  # "5:00 – 7:00 PM": the start borrows the end's am/pm
        if span:
            clock = parse_clock(f"{span.group(1)} {span.group(2) or span.group(3)}")
        else:
            clock_match = TIME_IN_TITLE.search(title)
            clock = parse_clock(clock_match.group(0)) if clock_match else None
        # drop ": 4:00 PM" or ": 5:00 – 7:00 PM" but keep any trailing note about where it is held
        title = re.sub(r":?\s*\d{1,2}(?::\d{2})?\s*(?:[ap]\.?m\.?)?\s*(?:[–-]\s*\d{1,2}(?::\d{2})?\s*)?[ap]\.?m\.?",
                       "", title, count=1, flags=re.I).strip(" :–-")
        description = htmllib.unescape(f.get("description", ""))
        default_place = src.get("default_location", "")
        events.append(make_event(
            src, title=title or raw_title,
            start=datetime.combine(date.fromisoformat(day), clock or time(0, 0), tz),
            all_day=clock is None,
            location=default_place if default_place and src.get("default_location_marker", "") in description else "",
            url=f.get("link", ""), uid=f.get("guid", "") or f.get("link", ""),
            cancelled=cancelled,
        ))
    return events


def fetch_mec_rss(src, start_day, end_day, tz):
    return normalize_mec_rss(src, get(src["url"]).text, tz)


# --- Granicus govAccess city sites: calendar RSS, with the date and time in the title ---
# e.g. "City Council (11/17/2026 7:00 p.m. - 10:00 p.m.)"

GOVACCESS_TITLE = re.compile(
    r"^(?P<name>.*?)\s*\((?P<day>\d{1,2}/\d{1,2}/\d{4}|[A-Z][a-z]+ \d{1,2}, \d{4})"
    r"(?:\s+(?P<start>\d{1,2}:\d{2}\s*[ap]\.?m\.?)(?:\s*-\s*(?P<end>\d{1,2}:\d{2}\s*[ap]\.?m\.?))?)?"
    r"(?:\s*-\s*[A-Z][a-z]+ \d{1,2}, \d{4})?\)\s*$", re.I)


def govaccess_day(text: str) -> date:
    for fmt in ("%m/%d/%Y", "%B %d, %Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            pass
    raise ValueError(text)


def normalize_govaccess_rss(src, xml_text, tz):
    import html as htmllib
    events = []
    for item in rss_items(xml_text):
        f = fields(item)
        m = GOVACCESS_TITLE.match(htmllib.unescape(f.get("title", "")))
        if not m:
            continue
        day = govaccess_day(m.group("day"))
        start_clock = parse_clock(m.group("start")) if m.group("start") else None
        end_clock = parse_clock(m.group("end")) if m.group("end") else None
        name = m.group("name")
        cancelled = bool(re.search(r"cancel", name, re.I))
        name = re.sub(r"\s*[-–]\s*cancel+ed\s*$", "", name, flags=re.I)
        events.append(make_event(
            src, title=name,
            start=datetime.combine(day, start_clock or time(0, 0), tz),
            end=datetime.combine(day, end_clock, tz) if end_clock else None,
            all_day=start_clock is None,
            url=f.get("link", ""), uid=f.get("link", "") or name,
            cancelled=cancelled,
        ))
    return events


def fetch_govaccess_rss(src, start_day, end_day, tz):
    return normalize_govaccess_rss(src, get(src["url"]).text, tz)


# --- CivicPlus (CivicEngage) county and city sites: one iCal feed per calendar category ---
# Categories are picked by hand in sources.yml; holidays and office closures
# that the sites copy into every category are dropped.

CLOSURE_TITLE = re.compile(r"holiday|clos(ed|ure)|thanksgiving|christmas|new year|day observed|\bday$", re.I)


def fetch_civicplus(src, start_day, end_day, tz):
    site = src["site"].rstrip("/")
    seen, events = set(), []
    for cat in src["categories"]:
        ics = get(f"{site}/common/modules/iCalendar/iCalendar.aspx", {"catID": cat, "feed": "calendar"}).content
        for e in normalize_ics(src, ics, start_day, end_day, tz):
            if e["id"] in seen or CLOSURE_TITLE.search(e["title"]):
                continue
            seen.add(e["id"])
            if not e["url"] or e["url"] == src.get("homepage", ""):
                e["url"] = src.get("homepage", "") or f"{site}/Calendar.aspx"
            events.append(e)
    return events


# --- PrimeGov public portals (upcoming meetings list) ---

def normalize_primegov(src, rows, tz):
    tenant = src["tenant"]
    events = []
    for r in rows:
        raw = (r.get("dateTime") or "")[:19]
        if not raw:
            continue
        start = datetime.fromisoformat(raw).replace(tzinfo=tz)  # local wall-clock time
        agenda = ""
        for d in r.get("documentList") or []:
            if d.get("templateName", "").lower().endswith("agenda") and d.get("templateId"):
                agenda = f"https://{tenant}.primegov.com/Portal/Meeting?meetingTemplateId={d['templateId']}"
                break
        events.append(make_event(
            src, title=(r.get("title") or "Public meeting").strip(), start=start,
            location=r.get("location") or "",
            url=f"https://{tenant}.primegov.com/public/portal",
            agenda_url=agenda, uid=str(r.get("id", "")),
        ))
    return events


def fetch_primegov(src, start_day, end_day, tz):
    rows = get(f"https://{src['tenant']}.primegov.com/api/v2/PublicPortal/ListUpcomingMeetings").json()
    return normalize_primegov(src, rows, tz)


# --- CivicWeb (iCompass) portals: the meeting schedule's JSON service ---

def normalize_civicweb(src, rows, tz):
    tenant = src["tenant"]
    events = []
    for r in rows:
        raw = r.get("MeetingDateTime") or ""
        if not raw:
            continue
        start = datetime.strptime(raw[:16], "%Y-%m-%d %H:%M").replace(tzinfo=tz)
        # Names end with the date ("Planning Commission - Dec 17 2026"); the site shows its own.
        name = re.sub(r"\s*-\s*\d{1,2} [A-Z][a-z]{2} \d{4}$|\s*-\s*[A-Z][a-z]{2} \d{1,2} \d{4}$", "", r.get("Name") or "")
        events.append(make_event(
            src, title=name or "Public meeting", start=start,
            location=r.get("MeetingLocation") or "",
            url=f"https://{tenant}.civicweb.net/Portal/MeetingInformation.aspx?Org=Cal&Id={r.get('Id')}",
            uid=str(r.get("Id", "")),
        ))
    return events


def fetch_civicweb(src, start_day, end_day, tz):
    rows = get(f"https://{src['tenant']}.civicweb.net/Services/MeetingsService.svc/meetings",
               {"from": start_day.isoformat(), "to": end_day.isoformat(), "loadmore": "false"}).json()
    return normalize_civicweb(src, rows, tz)


# --- Regular schedules entered by hand ("2nd and 4th Wednesday, 2 p.m.") ---
# For public bodies that publish a standing schedule but no feed. Each event
# says it comes from the regular schedule, so people check before they go.

WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
SCHEDULE_NOTE = ("From the regular meeting schedule the host publishes. Meetings can be cancelled "
                 "or moved, so check the host's page before you go.")


def schedule_dates(rule: str, start_day: date, end_day: date):
    """'2nd, 4th Wednesday' or 'last Monday' -> matching dates in the window."""
    m = re.match(r"\s*(?P<nths>[\w ,and]+?)\s+(?P<wd>monday|tuesday|wednesday|thursday|friday|saturday|sunday)\s*$",
                 rule, re.I)
    if not m:
        raise ValueError(f"bad schedule rule: {rule}")
    weekday = WEEKDAYS.index(m.group("wd").lower())
    wanted = set()
    for word in re.findall(r"1st|2nd|3rd|4th|5th|first|second|third|fourth|fifth|last", m.group("nths").lower()):
        wanted.add({"1st": 1, "first": 1, "2nd": 2, "second": 2, "3rd": 3, "third": 3,
                    "4th": 4, "fourth": 4, "5th": 5, "fifth": 5, "last": -1}[word])
    day = start_day
    while day <= end_day:
        if day.weekday() == weekday:
            nth = (day.day - 1) // 7 + 1
            last = (day + timedelta(days=7)).month != day.month
            if nth in wanted or (-1 in wanted and last):
                yield day
        day += timedelta(days=1)


DATED_LINK = re.compile(r'<a[^>]+href="([^"]+\.pdf)"[^>]*>\s*([A-Z][a-z]+ \d{1,2},\s*\d{4})\s*</a>')


def dated_agendas(page_html, base):
    """{date: pdf address} from a page that lists agenda packets as dated links
    ("November 3,2026")."""
    from urllib.parse import urljoin
    found = {}
    for href, label in DATED_LINK.findall(page_html):
        try:
            day = datetime.strptime(re.sub(r",\s*", ", ", label), "%B %d, %Y").date()
        except ValueError:
            continue
        found.setdefault(day, urljoin(base, href))
    return found


def link_dated_agendas(events):
    """For scheduled meetings whose host posts agenda packets on one page,
    attach the packet for that date once it is posted."""
    pages = {}
    for e in events:
        page = e.get("_agenda_page")
        if not page:
            continue
        if page not in pages:
            try:
                pages[page] = dated_agendas(get(page).text, page)
            except Exception as exc:
                print(f"[info] {e['source']}: agenda page not read: {exc}", file=sys.stderr)
                pages[page] = {}
        e["agenda_url"] = pages[page].get(datetime.fromisoformat(e["start"]).date(), "")


def fetch_schedule(src, start_day, end_day, tz):
    events = []
    for mtg in src["meetings"]:
        hh, mm = (int(x) for x in mtg["time"].split(":"))
        end = None
        if mtg.get("end"):
            eh, em = (int(x) for x in mtg["end"].split(":"))
        if mtg.get("dates"):  # a published list of dates, for bodies whose schedule has exceptions
            days = [d if isinstance(d, date) else date.fromisoformat(str(d)) for d in mtg["dates"]]
            days = [d for d in days if start_day <= d <= end_day]
        else:
            days = list(schedule_dates(mtg["when"], start_day, end_day))
            if mtg.get("until"):  # the host has only published its schedule this far
                last = mtg["until"] if isinstance(mtg["until"], date) else date.fromisoformat(str(mtg["until"]))
                days = [d for d in days if d <= last]
        for day in days:
            if day.month in mtg.get("skip_months", []):
                continue
            start = datetime.combine(day, time(hh, mm), tz)
            if mtg.get("end"):
                end = datetime.combine(day, time(eh, em), tz)
            events.append(make_event(
                src, title=mtg["title"], start=start, end=end,
                location=mtg.get("location", ""), url=mtg.get("url", ""),
                note=SCHEDULE_NOTE + (" " + mtg["note"] if mtg.get("note") else ""),
                uid=f"{mtg['title']}|{day.isoformat()}", category=mtg.get("category", ""),
            ))
            events[-1]["cancelled"] = False  # the note's wording ("can be cancelled") is not a cancellation
            events[-1]["_agenda_page"] = mtg.get("agenda_page", "")
    link_dated_agendas(events)
    return events


# --- IQM2 (Granicus) meeting portals: the calendar RSS feed ---
# Items are published agendas and minutes, titled like
# "City Council - Agenda - Nov 10, 2026 6:00 PM". A meeting shows up once its
# agenda is posted, so this feed only reaches a week or so ahead.

IQM2_TITLE = re.compile(
    r"^(?P<body>.+?)\s+-\s+(?P<kind>Agenda|Minutes|Agenda Packet|Summary)\s+-\s+"
    r"(?P<day>[A-Z][a-z]{2} \d{1,2}, \d{4})\s+(?P<clock>\d{1,2}:\d{2}\s*[AP]M)\s*$")


def normalize_iqm2_rss(src, xml_text, tz):
    import html as htmllib
    found = {}
    # The feed is not always well-formed XML (bare "&" in titles), so read the
    # items with a pattern instead of an XML parser.
    def tag(block, name):
        m = re.search(rf"<{name}>\s*(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?\s*</{name}>", block, re.S)
        return htmllib.unescape(m.group(1)).strip() if m else ""

    for block in re.findall(r"<item\b.*?</item>", xml_text, re.S):
        m = IQM2_TITLE.match(tag(block, "title"))
        if not m:
            continue
        day = datetime.strptime(m.group("day"), "%b %d, %Y").date()
        start = datetime.combine(day, parse_clock(m.group("clock")), tz)
        link = tag(block, "link")
        e = make_event(src, title=m.group("body"), start=start, url=link, uid=link or m.group("body"))
        # An agenda and its minutes are two items for one meeting; keep one.
        found.setdefault(e["id"], e)
    return list(found.values())


def fetch_iqm2_rss(src, start_day, end_day, tz):
    return normalize_iqm2_rss(src, get(src["url"]).text, tz)


# --- BoardBook Premier public pages (a table of posted meetings, each with an agenda page) ---
# Meetings appear when their agenda is posted, so this reaches a week or so ahead.

BOARDBOOK = "https://meetings.boardbook.org"
BOARDBOOK_ROW = re.compile(
    r"<tr class=\"[^\"]*row-for-[^\"]*\">\s*<td>\s*<div>\s*(?P<day>[A-Z][a-z]+ \d{1,2}, \d{4}) at "
    r"(?P<clock>\d{1,2}:\d{2} [AP]M)\s*-\s*(?P<title>.*?)</div>(?P<rest>.*?)</tr>", re.S)
BOARDBOOK_ITEM = re.compile(
    r'<tr class="agenda-item-information agenda-item-children-of-(?P<parent>\d+)"\s+data-agendaitemid="(?P<id>\d+)">'
    r'.*?name="hasChildren" value="(?P<kids>true|false)".*?<div class="form-check">(?P<text>.*?)</div>', re.S)
BOARDBOOK_SKIP = re.compile(r"consent|report|executive session|presentation|call to order|pledge|adjourn|"
                            r"public comment|future agenda", re.I)


def boardbook_text(fragment):
    import html as htmllib
    return " ".join(htmllib.unescape(re.sub(r"<[^>]+>", " ", fragment)).split())


def tidy_caps(text):
    """'CITY COUNCIL MEETING' -> 'City Council Meeting'; mixed-case text is left alone."""
    if text != text.upper():
        return text
    small = {"and", "of", "the", "for", "to", "in", "on", "at", "a"}
    words = [w.lower() if w.lower() in small and i else w.capitalize() for i, w in enumerate(text.split())]
    return " ".join(words)


def normalize_boardbook(src, page, tz):
    events = []
    for m in BOARDBOOK_ROW.finditer(page):
        raw = boardbook_text(m.group("title"))
        start = datetime.combine(datetime.strptime(m.group("day"), "%B %d, %Y").date(),
                                 parse_clock(m.group("clock")), tz)
        rest = m.group("rest")
        place = [boardbook_text(x) for x in re.findall(r"<span[^>]*id=[\"']?location[^\"'>]*-(?:description|line1)[\"']?[^>]*>(.*?)</span>", rest, re.S)]
        agenda = re.search(r'href="(/Public/Agenda/\d+\?meeting=(\d+))"', rest)
        e = make_event(
            src, title=tidy_caps(raw), start=start, location=", ".join(p for p in place if p),
            url=(BOARDBOOK + agenda.group(1)) if agenda else f"{BOARDBOOK}/Public/Organization/{src['organization']}",
            uid=agenda.group(2) if agenda else raw, cancelled=is_cancelled(raw),
        )
        e["_agenda"] = (BOARDBOOK + agenda.group(1)) if agenda else ""
        events.append(e)
    return events


def boardbook_items(page):
    """The decisions on a BoardBook agenda: items under hearings and business
    headings, with the numbering and "ACTION ITEM" labels removed. Hearing
    items are marked as such."""
    rows = [(m.group("id"), m.group("parent"), m.group("kids") == "true", boardbook_text(m.group("text")))
            for m in BOARDBOOK_ITEM.finditer(page)]
    sections = {i: text for i, parent, kids, text in rows if parent == "0"}
    out = []
    for i, parent, kids, text in rows:
        heading = sections.get(parent, "")
        if kids or (parent == "0") or BOARDBOOK_SKIP.search(heading):
            continue
        text = re.sub(r"^\d+(\.[A-Za-z0-9]+)*\.?\s*", "", text)
        text = re.sub(r"^\(?ACTION ITEM\)?[:\s-]*", "", text).strip()
        text = re.sub(r"[\s-]*\(?ACTION ITEM\)?$", "", text).strip()
        if not text:
            continue
        out.append(f"Public hearing: {text}" if re.search(r"public hearing", heading, re.I) else text)
    return out


def fetch_boardbook(src, start_day, end_day, tz):
    events = normalize_boardbook(src, get(f"{BOARDBOOK}/Public/Organization/{src['organization']}").text, tz)
    for e in events:
        day = datetime.fromisoformat(e["start"]).date()
        if e["cancelled"] or not e.get("_agenda") or not (start_day <= day) or not soon(e, start_day):
            continue
        try:
            add_highlights(e, boardbook_items(get(e["_agenda"]).text))
        except Exception as exc:
            print(f"[info] {src['id']}: no agenda items for {e['_agenda']}: {exc}", file=sys.stderr)
    return events


CONNECTORS = {"legistar": fetch_legistar, "civicclerk": fetch_civicclerk, "ics": fetch_ics,
              "bibliocommons": fetch_bibliocommons, "municode": fetch_municode, "mec_rss": fetch_mec_rss,
              "govaccess_rss": fetch_govaccess_rss, "civicplus": fetch_civicplus,
              "primegov": fetch_primegov, "civicweb": fetch_civicweb,
              "schedule": fetch_schedule, "iqm2_rss": fetch_iqm2_rss, "boardbook": fetch_boardbook}


# ---------- outputs ----------

def ics_escape(text: str) -> str:
    return (text or "").replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def write_ics(events, path: Path, stamp: datetime, name: str = "Idaho"):
    utc = ZoneInfo("UTC")
    fmt = "%Y%m%dT%H%M%SZ"
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//CivicsID//Public meetings//EN",
             f"X-WR-CALNAME:CivicsID {name}"]
    for e in events:
        start = datetime.fromisoformat(e["start"])
        lines += ["BEGIN:VEVENT", f"UID:{e['id']}@civicsid", f"DTSTAMP:{stamp.astimezone(utc).strftime(fmt)}"]
        if e["all_day"]:
            lines += [f"DTSTART;VALUE=DATE:{start.strftime('%Y%m%d')}"]
        else:
            end = datetime.fromisoformat(e["end"]) if e["end"] else start + timedelta(hours=1)
            lines += [f"DTSTART:{start.astimezone(utc).strftime(fmt)}",
                      f"DTEND:{end.astimezone(utc).strftime(fmt)}"]
        summary = ("CANCELLED: " if e["cancelled"] else "") + f"{e['title']} ({e['host']})"
        lines += [f"SUMMARY:{ics_escape(summary)}", f"LOCATION:{ics_escape(e['location'])}",
                  f"URL:{e['url']}", "END:VEVENT"]
    lines.append("END:VCALENDAR")
    path.write_text("\r\n".join(lines) + "\r\n", encoding="utf-8")


def apply_source_rules(src, events):
    """Per-source tidying set in sources.yml.

    drop_uncategorized: leave out anything that doesn't read as a meeting or
      hearing (office closures, conferences, staff events on a shared calendar).
    default_category: for feeds that only carry meetings, file the ones whose
      names don't say so under this category.
    force_category: file everything from this source under one category
      (the Legislature's own calendar).
    """
    if src.get("force_category"):
        for e in events:
            e["category"] = src["force_category"]
    if src.get("default_category"):
        for e in events:
            if e["category"] == "other":
                e["category"] = src["default_category"]
    if src.get("drop_uncategorized"):
        events = [e for e in events if e["category"] != "other"]
    return events


def county_slug(county: str) -> str:
    return re.sub(r"[^a-z]+", "-", county.lower()).strip("-")


def load_previous_status() -> dict:
    try:
        return {s["id"]: s for s in json.loads((OUT / "status.json").read_text())["sources"]}
    except Exception:
        return {}


def main() -> int:
    cfg = yaml.safe_load((Path(__file__).parent / "sources.yml").read_text())
    default_tz = cfg["timezone"]
    now = datetime.now(ZoneInfo(default_tz))
    start_day, end_day = now.date(), now.date() + timedelta(days=cfg["window_days"])
    previous = load_previous_status()
    try:
        old_events = json.loads((OUT / "events.json").read_text())["events"]
    except Exception:
        old_events = []

    all_events, statuses = [], []
    for src in cfg["sources"]:
        status = {"id": src["id"], "name": src["name"], "homepage": src.get("homepage", ""),
                  "county": src["county"],
                  "checked": now.isoformat(timespec="seconds")}
        src.setdefault("timezone", default_tz)
        tz = ZoneInfo(src["timezone"])
        try:
            found = CONNECTORS[src["type"]](src, start_day, end_day, tz)
            found = [e for e in found if start_day <= datetime.fromisoformat(e["start"]).date() <= end_day]
            found = apply_source_rules(src, found)
            status.update(ok=True, count=len(found), last_success=status["checked"], error="", failing_since="")
            # A source that answers but lists nothing is suspicious, not fine.
            status["state"] = "ok" if found else "quiet"
        except Exception as exc:  # one bad source must not sink the rest
            # Keep showing what we had, so a one-night outage doesn't blank a city.
            found = [e for e in old_events if e["source"] == src["id"]
                     and datetime.fromisoformat(e["start"]).date() >= start_day]
            status.update(ok=False, count=len(found), state="failing",
                          failing_since=previous.get(src["id"], {}).get("failing_since") or now.date().isoformat(),
                          last_success=previous.get(src["id"], {}).get("last_success", ""),
                          error=f"{type(exc).__name__}: {exc}"[:300])
            print(f"[warn] {src['id']}: {status['error']}", file=sys.stderr)
        all_events.extend(found)
        statuses.append(status)

    for e in all_events:
        for k in [k for k in e if k.startswith("_")]:
            del e[k]
    unique = {e["id"]: e for e in all_events}
    events = sorted(unique.values(), key=lambda e: (e["start"], e["host"], e["title"]))

    OUT.mkdir(parents=True, exist_ok=True)
    stamp = now.isoformat(timespec="seconds")
    (OUT / "events.json").write_text(json.dumps({"generated": stamp, "events": events}, indent=1))
    (OUT / "status.json").write_text(json.dumps({"generated": stamp, "sources": statuses}, indent=1))
    # One subscribable calendar per county, one for the Legislature
    # (statewide.ics) and one with everything (idaho.ics).
    (OUT / "ics").mkdir(exist_ok=True)
    write_ics(events, OUT / "ics" / "idaho.ics", now, "Idaho")
    for county in sorted({e["county"] for e in events} | {s["county"] for s in statuses}):
        mine = [e for e in events if e["county"] == county]
        label = "Idaho Legislature" if county == "Statewide" else f"{county} County"
        write_ics(mine, OUT / "ics" / f"{county_slug(county)}.ics", now, label)

    for s in statuses:
        print(f"{s['state']:8} {s['count']:4}  {s['name']}")
    print(f"total {len(events)} events through {end_day}")
    # Fail the run only when every source failed, so the nightly job goes red.
    return 1 if statuses and not any(s["ok"] for s in statuses) else 0


if __name__ == "__main__":
    sys.exit(main())
