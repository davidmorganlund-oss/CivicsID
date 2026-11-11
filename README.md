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
| City of Boise | Ada | IQM2 agenda feed | `iqm2_rss` | Reaches about a week ahead. Boise is moving to a new portal through January 2027, so this one will need replacing |
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

`inventory/sources.csv` lists what was checked and what is still to do,
including Nampa and Ada County.

Counties with no readable calendar yet show a link to the county's own
meetings page instead, from `site/data/local.json`.

## County coverage

41 of 44 counties are connected. Hand-entered schedules come only from schedules the county or city publishes, and are marked on the site as coming from a standing schedule.

| County | How | Sources | Notes |
|---|---|---|---|
| Ada | Live feed + schedule | City of Boise (IQM2 feed); City of Meridian (CivicClerk); City of Kuna (CivicPlus calendar); City of Star (CivicPlus calendar); Ada County Highway District (published schedule) |  |
| Adams | Published schedule | Adams County (published schedule) |  |
| Bannock | Live feed | City of Pocatello (CivicPlus calendar); Bannock County (WordPress events feed) |  |
| Bear Lake | Published schedule | Bear Lake County (published schedule) |  |
| Benewah | Live feed | Benewah County (calendar feed) | Agendas post a few days ahead, so the calendar is often quiet |
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
| Gem | Link only |  | County calendar is out of date and no regular schedule is published; Emmett's meeting page lists no dates |
| Gooding | Live feed + schedule | Gooding County (CivicPlus Agenda Center); Gooding County (published schedule) |  |
| Idaho | Published schedule | Idaho County (published schedule) |  |
| Jefferson | Live feed | Jefferson County (CivicPlus calendar) |  |
| Jerome | Live feed | Jerome County (CivicPlus Agenda Center) | Agendas post a few days ahead, so the calendar is often quiet |
| Kootenai | Live feed + schedule | Kootenai County (CivicPlus calendar); City of Coeur d'Alene (published schedule); City of Coeur d'Alene (LibCal); Coeur d'Alene Public Library (LibCal); Community Library Network (LibCal); City of Hayden (BoardBook); City of Rathdrum (published schedule); City of Dalton Gardens (published schedule); City of Post Falls (CivicPlus calendar) |  |
| Latah | Live feed | Latah County Library District (events feed); City of Moscow (CivicClerk) |  |
| Lemhi | Live feed | Lemhi County (CivicPlus calendar) |  |
| Lewis | Link only |  | County website's security certificate fails, so it can't be read safely; no published schedule found |
| Lincoln | Link only |  | County meetings page turns away automated readers; linked from the county card |
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
