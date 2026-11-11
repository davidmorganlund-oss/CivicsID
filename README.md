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
including Nampa, Ada County and Canyon County.

Counties with no readable calendar yet show a link to the county's own
meetings page instead, from `site/data/local.json`.

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
