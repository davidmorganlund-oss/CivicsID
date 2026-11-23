# CivicsID

A civic calendar, Engage guides and a "who represents you" lookup for Idaho.
A project of BarNone, an independent nonprofit. Not affiliated with any
government agency. Sister site to CivicsWA (civicswa.org).

**Status: first build, November 2026. Site address: civicsid.org.**

## How it works

- `pipeline/sources.yml` lists the public calendars the site reads.
- `pipeline/build.py` reads each one and writes `site/data/events.json`,
  `site/data/status.json` and the subscribable calendars in `site/data/ics/`.
- `pipeline/officials.py` writes `site/data/officials.json` (legislators and
  members of Congress) for the lookup page.
- `.github/workflows/refresh.yml` runs both every night, saves the result and
  publishes the site with GitHub Pages.
- `site/` is a plain static site that reads those files. No accounts, no tracking.

## Two time zones

Most of Idaho is on Mountain time and the north is on Pacific. Each source
has a `timezone` (Mountain unless it says otherwise), each event carries a
`tz` label, and the site shows every meeting in its own local time.

## Sources (November 2026)

| Source | County | Platform | Connector | Notes |
|---|---|---|---|---|
| Idaho Legislature | Statewide | Its own calendar feed | `ics` | Interim committees now, standing committees in session |
| City of Meridian | Ada | CivicClerk | `civicclerk` | |
| City of Kuna | Ada | CivicPlus | `civicplus` | |
| City of Star | Ada | CivicPlus | `civicplus` | |
| Ada County Highway District | Ada | Published regular schedule | `schedule` | Marked on the site as coming from a standing schedule |
| City of Caldwell | Canyon | CivicClerk | `civicclerk` | |
| City of Idaho Falls | Bonneville | CivicPlus | `civicplus` | Ten boards and commissions |
| City of Pocatello | Bannock | CivicPlus | `civicplus` | Shared city calendar, filtered to meetings |
| City of Twin Falls | Twin Falls | CivicClerk | `civicclerk` | |
| City of McCall | Valley | CivicPlus | `civicplus` | |
| Kootenai County | Kootenai | CivicPlus | `civicplus` | Pacific time |
| City of Post Falls | Kootenai | CivicPlus | `civicplus` | Pacific time |
| City of Coeur d'Alene | Kootenai | Published council schedule | `schedule` | Council only; links the agenda packet once posted |
| City of Hayden | Kootenai | BoardBook | `boardbook` | Shows a meeting once its agenda is posted, with agenda highlights |
| City of Rathdrum | Kootenai | Entered by hand | `schedule` | Site turns away automated readers; update each January |
| City of Dalton Gardens | Kootenai | Entered by hand | `schedule` | No feed; update monthly from the city calendar |
| Coeur d'Alene city boards | Kootenai | Library's LibCal calendar | `libcal` | City boards that meet at the library |
| Coeur d'Alene Public Library | Kootenai | LibCal | `libcal` | Civic programs only |
| Community Library Network | Kootenai, Shoshone | LibCal | `libcal` | Seven libraries; civic programs only |
| East Bonner County Library District | Bonner | Events feed | `mec_library` | Civic programs only |
| Latah County Library District | Latah | Events feed | `mec_library` | Civic programs only |
| City of Lewiston | Nez Perce | CivicClerk | `civicclerk` | Pacific time |
| City of Moscow | Latah | CivicClerk | `civicclerk` | Pacific time |
| City of Boise | Ada | eScribe | `escribe` | Council, commissions and the Library Board of Trustees; council stays on IQM2 (`iqm2_rss`) until Jan. 12, 2027 |
| Ada County | Ada | Daily agenda PDFs in the county file browser | `ada_agendas` | Lists the meetings the agenda marks public and streamed; public-hearing highlights |
| City of Nampa | Canyon | Published council schedule | `schedule` | Calendar turns away automated readers; 1st and 3rd Mondays, 5 p.m. |
| Chubbuck | Bannock | WordPress events feed | `tribe` | |
| Mountain Home | Elmore | CivicPlus | `civicplus` | Council calendar |
| City of Eagle | Ada | Published regular schedules | `schedule` | Granicus agenda site asks automated readers to stay out |
| City of Blackfoot | Bingham | CivicPlus Agenda Center | `agendacenter` | Council and P&Z |
| City of Burley | Cassia | CivicPlus Agenda Center + published schedule | `agendacenter`, `schedule` | Council and P&Z |
| City of Jerome | Jerome | CivicPlus (newer calendar) | `civicplus` | Council, P&Z, urban renewal |
| Bonneville County | Bonneville | Tyler Meeting Manager | `tyler_mm` | Board meetings and P&Z; commissioners' outside meetings left out |
| Twin Falls County | Twin Falls | Daily agenda PDFs | `daily_agendas` | Listed on days with action items |
| Blaine, Latah and Oneida counties | various | Published schedules | `schedule` | Blaine and Oneida turn automated readers away; read by a person |
| City of Sandpoint | Bonner | Published dates and schedule | `schedule` | Site turns automated readers away; read by a person from its own pages |
| Rexburg, Ammon, Garden City (P&Z), Hailey, Emmett | various | Published schedules | `schedule` | Garden City doesn't publish its council meeting time |
| City of Kimberly | Twin Falls | CivicPlus Agenda Center + published schedule | `agendacenter`, `schedule` | Council |
| Middleton, Payette, Fruitland, Rupert, Weiser, Preston, Rigby, Shelley, American Falls, Buhl, St. Anthony, Gooding, Heyburn, Grangeville, Orofino, Salmon, Soda Springs | various | Published regular schedules | `schedule` | Read from each city's own pages (Nov 2026); agendas stay on the city's site. American Falls doesn't publish its council start time. Grangeville and Orofino are on Pacific time |
| Boise School District | Ada | Board meeting notice page | `notice_page` | Shows the next posted meeting |
| West Ada, Nampa, Idaho Falls D91, Pocatello/Chubbuck D25, Middleton, Emmett, Lewiston, Fremont County school districts | various | Simbli | `simbli` | Nampa also shows its published 2026 calendar until each meeting posts |
| Bonneville D93, Minidoka County and Lakeland 272 school districts | various | BoardBook | `boardbook` | |
| Twin Falls, Madison, Blackfoot, Lake Pend Oreille, Shelley, Caldwell, Vallivue, Moscow, Post Falls, Jefferson 251, Blaine County and Lewiston (until posted) school districts | various | Published board schedules and dates | `schedule` | Read from each district's own pages (Nov 2026); recheck each January |
| Coeur d'Alene Public Schools | Kootenai | Published schedule | `schedule` | Its meetings portal asks automated readers to stay away |
| Ada Community, Twin Falls and Marshall (Pocatello) libraries | various | Published board schedules | `schedule` | Boise Public Library's board comes through Boise's eScribe |
| Nampa, Kuna and The Community Library (Ketchum) | various | LibCal | `libcal` | Board meetings and civic programs only |
| Meridian, Eagle, Caldwell and Mountain Home libraries | various | Published board schedules | `schedule` | |

`inventory/sources.csv` lists what was checked and what is still to do,
including Nampa and Ada County.

Counties with no readable calendar yet show a link to the county's own
meetings page instead, from `site/data/local.json`.

## County coverage

All 44 counties are connected. Hand-entered schedules come only from schedules the county or city publishes, and are marked on the site as coming from a standing schedule.

| County | How | Sources | Notes |
|---|---|---|---|
| Ada | Live feed + schedule | City of Boise (IQM2 feed); City of Meridian (CivicClerk); City of Kuna (CivicPlus calendar); City of Star (CivicPlus calendar); Ada County Highway District (published schedule) |  |
| Adams | Published schedule | Adams County (published schedule) |  |
| Bannock | Live feed | City of Pocatello (CivicPlus calendar); Bannock County (WordPress events feed) |  |
| Bear Lake | Published schedule | Bear Lake County (published schedule) |  |
| Benewah | Live feed | Benewah County (calendar feed) | Connected, but the county calendar lists no upcoming meetings right now |
| Bingham | Published schedule | Bingham County (published schedule) |  |
| Blaine | Live feed | City of Ketchum (CivicPlus calendar) | County site turns away automated readers; covered through Ketchum |
| Boise | Published schedule | Boise County (published schedule) |  |
| Bonner | Live feed | East Bonner County Library District (events feed); Bonner County (meeting calendar) |  |
| Bonneville | Live feed | City of Idaho Falls (CivicPlus calendar) |  |
| Boundary | Published schedule | Boundary County (published schedule) |  |
| Butte | Published schedule | Butte County (published schedule) |  |
| Camas | Published schedule | Camas County (published schedule) |  |
| Canyon | Live feed | City of Caldwell (CivicClerk); Canyon County (county agenda system) |  |
| Caribou | Published schedule | Caribou County (published schedule) |  |
| Cassia | Live feed + schedule | Cassia County (meeting calendar); Cassia County (published schedule) |  |
| Clark | Live feed | Clark County (CivicPlus Agenda Center) | Agendas post a few days ahead, so the calendar is often quiet |
| Clearwater | Live feed + schedule | Clearwater County (Revize calendar); Clearwater County (published schedule) |  |
| Custer | Published schedule | Custer County (published schedule) |  |
| Elmore | Published schedule | Elmore County (published schedule) |  |
| Franklin | Live feed + schedule | Franklin County (Revize calendar); Franklin County (published schedule) |  |
| Fremont | Published schedule | Fremont County (published schedule) | County site turns away automated readers; posted dates entered by hand |
| Gem | Live feed | Gem County (weekly agenda PDFs) | Shows each week's meetings once the agenda posts, usually the Friday before, with agenda highlights |
| Gooding | Live feed + schedule | Gooding County (CivicPlus Agenda Center); Gooding County (published schedule) |  |
| Idaho | Published schedule | Idaho County (published schedule) |  |
| Jefferson | Live feed | Jefferson County (CivicPlus calendar) |  |
| Jerome | Live feed | Jerome County (CivicPlus Agenda Center) | Agendas post a few days ahead, so the calendar is often quiet |
| Kootenai | Live feed + schedule | Kootenai County (CivicPlus calendar); City of Coeur d'Alene (published schedule); City of Coeur d'Alene (LibCal); Coeur d'Alene Public Library (LibCal); Community Library Network (LibCal); City of Hayden (BoardBook); City of Rathdrum (published schedule); City of Dalton Gardens (published schedule); City of Post Falls (CivicPlus calendar) |  |
| Latah | Live feed | Latah County Library District (events feed); City of Moscow (CivicClerk) |  |
| Lemhi | Live feed | Lemhi County (CivicPlus calendar) |  |
| Lewis | Live feed | Lewis County (next-meeting notice) | The https certificate fails, so this reads the same page over http; shows the next regular meeting |
| Lincoln | Published schedule | Lincoln County (published schedule) | First four Mondays at 10 a.m., from the county's Commissioners page; moves to Tuesday on Monday holidays |
| Madison | Live feed | Madison County (Revize calendar) |  |
| Minidoka | Live feed | Minidoka County (CivicPlus calendar) |  |
| Nez Perce | Live feed + schedule | City of Lewiston (CivicClerk); Nez Perce County (published schedule) |  |
| Oneida | Published schedule | Malad City (published schedule) | County site behind a bot challenge; covered through Malad City's council |
| Owyhee | Published schedule | Owyhee County (published schedule) |  |
| Payette | Live feed | Payette County (events feed) |  |
| Power | Live feed | Power County (CivicPlus calendar) |  |
| Shoshone | Published schedule | Shoshone County (published schedule) |  |
| Teton | Live feed + schedule | Teton County (Revize calendar); Teton County (published schedule) |  |
| Twin Falls | Live feed | City of Twin Falls (CivicClerk) |  |
| Valley | Live feed | City of McCall (CivicPlus calendar); Valley County (meeting calendar) |  |
| Washington | Live feed | Washington County (CivicPlus calendar) |  |

## Spanish

`site/es/` has the calendar and four guides in Spanish (speaking at a public meeting, the Open Meeting Law, public records requests, contacting your representatives). The calendar script reads `<html lang="es">` and switches its wording; meeting names and agendas stay in English because they come from the hosts. Spanish guides live in `tools/pages/guides_es.py` under the same slugs as the English ones, and every page links to its counterpart. Regenerate pages with `python3 tools/pages/gen.py`.

## Reading only what sites allow

Every request the pipeline makes checks the site's robots.txt first (`check_robots` in
`pipeline/build.py`, cached per run, compared without regard to case). A source whose address
is disallowed fails with a clear message, shows nothing, and is listed in the upkeep issue; if
robots.txt can't be read at all, nothing is fetched that night and last night's listings stay up.

CivicPlus sites have asked all automated readers to stay out of their iCalendar feeds since
October 2026, so the `civicplus` connector reads each site's public calendar page
(`Calendar.aspx?CID=...&startDate=...&endDate=...`), which they still allow. Both page layouts
(list and month grid) are handled, and sites that have moved to CivicPlus's newer calendar
(`/m/calendar`) are read from the JSON it loads (`/m/calendar/Home/MonthEvents`).

### Meeting portals we don't read

Diligent Community (formerly HighBond/iCompass) portals, used by Moscow, Cassia and Blaine County schools and the City of Fruitland, publish a robots.txt that disallows all automated readers. CivicsID doesn't read them; those bodies are covered, where possible, from schedules on their own websites.

## Security

- The site is static: no logins, no database, no server code, nothing a visitor types is stored by us.
- Everything about a meeting comes from outside sites, so the pipeline treats it as untrusted.
  `clean_event` in `pipeline/build.py` keeps only full `http(s)` links (completing relative ones
  against the host's site) and strips control characters before anything is written. The browser
  code inserts all of it as plain text, never as HTML, and checks links again.
- A Content-Security-Policy on every page lets scripts load only from this site and the Census
  geocoder (which the representatives lookup needs; it doesn't support a plain fetch).
- The workflow gives each job only the permissions it needs, pins GitHub Actions to exact commits
  and Python packages to exact versions. Bump them on purpose and let the tests run.
- Tests in `tests/test_normalize.py` cover the link checks and feed/calendar escaping.

## Run it yourself

    pip install -r requirements.txt
    python -m pytest -q tests
    python pipeline/build.py
    python pipeline/officials.py
    python -m http.server --directory site 8000

## Adding a city or county

If it runs CivicClerk, add its tenant name to `sources.yml`. A CivicPlus site
(the address ends in `/calendar.aspx`) needs its calendar category numbers,
listed at `/iCalendar.aspx` on that site. A site with an iCal feed uses the
`ics` connector. Anything else needs a new connector in `build.py`.

## Look

Colors and typefaces come from the brand sheet supplied in November 2026:
blue #002676, gold #FDB515, with Inter, Source Serif 4 and Barlow Condensed.
They are set as variables at the top of `site/styles.css`.
