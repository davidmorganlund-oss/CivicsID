"""Generator for CivicsID's static pages (guides, Engage, reps, calendar shell).
Run: python3 tools/pages/gen.py  -- writes plain HTML into site/."""
import html, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import guides_a, guides_b, guides_c

SITE = Path(__file__).resolve().parents[2] / "site"
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600&family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap" rel="stylesheet">')
NOTICE = '<div class="notice">A project of BarNone, a nonprofit. Not affiliated with any government agency.</div>'
BY = ('<p class="by-barnone"><a href="https://barnoneinc.org"><img src="{up}barnone-phoenix.png" alt="" width="28" height="28">'
      '<span>A service of <strong>BarNone, Inc.</strong></span></a> An independent nonprofit. CivicsID is not a government website, '
      'is not affiliated with any government agency, and does not speak for any public office.</p>')


def head(title, up, desc, share=None):
    share = share or title.split(" | ")[0]
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<meta property="og:site_name" content="CivicsID">
<meta property="og:title" content="{html.escape(share, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary">
{FONTS}
<link rel="stylesheet" href="{up}styles.css">
</head>
<body>'''


def top(up, current):
    def a(href, label, key, short=None):
        cur = ' aria-current="page"' if key == current else ""
        if short:  # a shorter label on phones; the full name stays for screen readers
            return f'    <a href="{up}{href}"{cur} aria-label="{label}"><span class="full">{label}</span><span class="short">{short}</span></a>'
        return f'    <a href="{up}{href}"{cur}>{label}</a>'
    return f'''{NOTICE}

<header class="top"><div class="wrap">
  <a class="brand" href="{up}index.html">Civics<span>ID</span></a>
  <nav aria-label="Main">
{a("index.html", "Community Calendar", "calendar", "Calendar")}
{a("engage.html", "Engage", "engage")}
{a("reps.html", "My representatives", "reps", "My reps")}
  </nav>
</div></header>'''


def footer(up, first):
    return f'''<footer><div class="wrap">
  <p>{first}</p>
  {BY.format(up=up)}
</div></footer>'''


# ---------- guides ----------
ALL = {**guides_a.G, **guides_b.G, **guides_c.G}
for slug, g in ALL.items():
    sources = "\n".join(f'    <li><a href="{html.escape(u, quote=True)}" rel="noopener">{html.escape(t)}</a></li>' for u, t in g["sources"])
    script = '\n<script src="../local.js"></script>' if 'class="near-you"' in g["body"] else ""
    page = f'''{head(g["title"] + " | CivicsID", "../", g["lede"])}
<a class="skip" href="#guide">Skip to guide</a>
{top("../", "engage")}

<main class="wrap narrow guide" id="guide">
  <p class="eyebrow"><a href="../engage.html">Engage</a> · {g["cat"]}</p>
  <h1>{html.escape(g["title"])}</h1>
  <p class="lede">{html.escape(g["lede"])}</p>
{g["body"].strip(chr(10))}

  <h2>Sources</h2>
  <ul class="sources-list">
{sources}
  </ul>
  <p class="muted">Last reviewed November 2026. This guide is general information, not legal advice. Rules change, so check the linked sources before you rely on a deadline.</p>
</main>

{footer("../", "Every guide lists its sources so you can check them yourself.")}{script}
</body>
</html>
'''
    (SITE / "guides" / f"{slug}.html").write_text(page)

# ---------- engage ----------
SECTIONS = [
    ("Start here", [
        ("reps.html", "Who represents you", "Enter your address to see your city, county, state and federal representatives."),
        ("guides/contact-your-representatives.html", None, "Picking the right office and writing a message that gets read."),
    ]),
    ("Your city and county", [
        ("guides/local-government.html", None, "Counties, cities, school districts and the special districts that run roads, fire, water and more."),
        ("guides/speak-at-a-public-meeting.html", None, "What Idaho's open meetings law gives you, what it doesn't, and how to use two minutes well."),
        ("guides/open-meeting-law.html", None, "Notice, agendas, closed sessions, your right to record, and what to do when a body breaks the rules."),
        ("guides/public-records-requests.html", None, "How to ask for emails, contracts and reports, what it costs, the deadlines, and what to do if they say no."),
        ("guides/your-neighborhood.html", None, "Getting problems fixed, finding out what's planned and getting neighbors organized."),
        ("guides/local-ballot-measures.html", None, "Bonds, levies, and why a school bond can get 60 percent and still fail."),
    ]),
    ("The State of Idaho", [
        ("guides/legislature.html", None, "Who's in it, the session calendar, how a bill moves, and where your voice counts."),
        ("guides/weigh-in-on-a-state-bill.html", None, "Four ways to tell the Legislature what you think, and the timing that catches people."),
        ("guides/state-budgets.html", None, "The yearly cycle, the committee that writes it, and when each step is open to you."),
        ("guides/boards-and-commissions.html", None, "How residents get appointed to state, county and city boards."),
        ("guides/campaign-finance.html", None, "Who gives to Idaho candidates, what the limits are and where to look it up."),
        ("guides/state-agencies.html", None, "A short directory for the most common needs, and what to do when you're stuck."),
        ("guides/running-for-office.html", None, "Which offices are up when, how filing works, and campaign finance basics."),
        ("guides/state-initiatives.html", None, "How voters put a law on the ballot, the signature rules and the deadlines."),
    ]),
    ("The federal government", [
        ("guides/federal-offices.html", None, "The House, Senate and President, and the Constitution's requirements for each."),
        ("guides/courts.html", None, "Idaho's state courts and the federal courts, side by side."),
        ("guides/constitution.html", None, "The U.S. and Idaho constitutions, and how each one changes."),
        ("guides/federal-agencies.html", None, "Casework, public land decisions, commenting on rules and requesting records."),
        ("guides/federal-budget.html", None, "Appropriations, the fiscal year, and community project requests."),
    ]),
    ("Skills and everyday", [
        ("guides/two-minute-pitch.html", None, "A simple shape for making your case in the time you get."),
        ("guides/read-a-bill-or-agenda.html", None, "Bill numbers, underlines and strike-throughs, action items and packets."),
        ("guides/media-literacy.html", "Media literacy", "Quick habits for sorting good information from bad."),
        ("guides/volunteer-and-public-service.html", None, "Where to find volunteer roles and government jobs."),
        ("guides/problem-to-policy.html", None, "Finding the right level of government and shaping a specific ask."),
    ]),
]
blocks, listed = [], set()
for i, (heading, items) in enumerate(SECTIONS):
    style = ' style="margin-top: 20px"' if i else ""
    rows = []
    for href, label, blurb in items:
        if href.startswith("guides/"):
            slug = href[7:-5]
            listed.add(slug)
            label = label or ALL[slug]["title"]
        rows.append(f'    <li><a href="{href}">{html.escape(label)}<span>{html.escape(blurb)}</span></a></li>')
    blocks.append(f'  <h2{style}>{heading}</h2>\n  <ul class="guide-links">\n' + "\n".join(rows) + "\n  </ul>")
assert listed == set(ALL), (listed ^ set(ALL))
(SITE / "engage.html").write_text(f'''{head("Engage | CivicsID", "", "Plain-language guides to how government works in Idaho and where you can step in.")}
<a class="skip" href="#guides">Skip to guides</a>
{top("", "engage")}

<section class="hero plain"><div class="wrap">
  <h1>Engage: how to take part, from your block to Congress.</h1>
  <p class="lede">Plain-language guides to how government works in Idaho and where you can step in. Every guide lists its sources so you can check them yourself.</p>
</div></section>

<main class="wrap" id="guides" style="padding-block: 32px 64px; display: flex; flex-direction: column; gap: 20px">
{chr(10).join(chr(10) + b if i else b for i, b in enumerate(blocks))}
</main>

{footer("", "Guides are written in plain language, list their sources, and are built to work with screen readers.")}
</body>
</html>
''')

# ---------- calendar ----------
(SITE / "index.html").write_text(f'''{head("Get Engaged, Idaho | CivicsID", "", "See what your city council, county commissioners, library board and the Idaho Legislature are deciding this week, and how to make your voice heard.", "Get Engaged, Idaho: what your community is deciding this week")}
<a class="skip" href="#events">Skip to events</a>
{top("", "calendar")}

<section class="hero"><div class="wrap">
  <p class="eyebrow light">Community Calendar</p>
  <h1>Find out what your community is deciding this week.</h1>
  <p class="lede">City councils, county commissioners, public hearings and the Legislature, from across Idaho, in one calendar. Pick where you live and we'll show you what's near you.</p>
  <form class="search" id="search" onsubmit="return false">
    <div class="field">
      <label for="county">County</label>
      <select id="county"><option value="">All of Idaho</option></select>
    </div>
    <div class="field">
      <label for="city">City</label>
      <select id="city" disabled><option value="">Pick a county</option></select>
    </div>
  </form>
  <p class="small"><span id="coverage">Covering more of Idaho every month.</span> No account needed, and your choice stays in your browser.</p>
</div></section>

<div class="wrap layout">
  <main class="main" id="events">
    <div class="heading">
      <h2 id="heading">Coming up across Idaho</h2>
      <span id="range"></span>
    </div>
    <p class="muted" id="place-msg" role="status" hidden></p>
    <div class="find">
      <label for="q">Search meetings and agendas</label>
      <input id="q" type="search" placeholder="Try zoning, library, budget, schools" autocomplete="off">
    </div>
    <div class="chips" role="group" aria-label="Filter by type" id="chips"></div>
    <div class="list" id="list" aria-live="polite"><p class="empty">Loading events…</p></div>
    <button class="more" id="more" type="button" hidden>Show two more weeks</button>
  </main>

  <aside class="side">
    <div class="card">
      <h2>Get it on your phone</h2>
      <p id="subscribe-text">Subscribe once and these meetings show up in the calendar app you already use.</p>
      <a class="link" id="subscribe" href="data/ics/statewide.ics">Subscribe to Idaho Legislature committee meetings</a>
    </div>
    <div class="card">
      <h2>Two time zones</h2>
      <p>Each meeting is listed in its own local time: Mountain for most of Idaho, Pacific for the Panhandle and the north-central counties.</p>
    </div>
    <div class="card">
      <h2>The Legislature, day by day</h2>
      <p>Committee hearings with their agendas and bills, and how to sign up to testify. Session opens January 11.</p>
      <a class="link" href="legislature.html">See this week at the Statehouse</a>
    </div>
    <div class="card warm">
      <span class="eyebrow">Engage</span>
      <h2>First time at a public meeting?</h2>
      <p>What Idaho law lets you do, what to say in two minutes, and what happens after you speak.</p>
      <a class="link" href="guides/speak-at-a-public-meeting.html">Read the guide</a>
    </div>
  </aside>
</div>

{footer("", 'Listings come straight from public agency calendars and are refreshed every night. <span id="updated"></span> Schedules change, so confirm with the host before you go.')}

<script src="app.js"></script>
</body>
</html>
''')

# ---------- representatives ----------
(SITE / "reps.html").write_text(f'''{head("Who represents you | CivicsID", "", "Enter an Idaho street address to see your state legislators and members of Congress, plus where to find your city and county officials.")}
<a class="skip" href="#results">Skip to results</a>
{top("", "reps")}

<section class="hero"><div class="wrap">
  <h1>Find who represents you.</h1>
  <p class="lede">Enter an Idaho street address to see your state legislators and members of Congress and how to reach them, plus where to find your city and county officials.</p>
  <form class="search" id="lookup">
    <div class="field wide">
      <label for="address">Street address</label>
      <input id="address" name="address" type="text" autocomplete="street-address" placeholder="700 W Jefferson St, Boise">
    </div>
    <button class="btn" type="submit">Look up</button>
  </form>
  <p class="small">Your address is sent from your browser to the U.S. Census Bureau's address lookup to find your districts. CivicsID never receives or stores it. Your browser remembers only your county and city, so the Engage guides can show local links.</p>
</div></section>

<main class="wrap narrow" style="padding-block: 40px 64px">
  <div class="list" id="results" aria-live="polite">
    <p class="empty">Your representatives will show up here.</p>
  </div>
  <p class="muted" style="margin-top: 24px">Not sure what to say once you have a name? Read <a href="guides/contact-your-representatives.html">how to contact the people who represent you</a>.</p>
</main>

{footer("", "State legislators come from Open States, a public roster built from the Idaho Legislature's member pages, and members of Congress from a public roster. Both are refreshed nightly. County links cover all 44 counties where we could confirm a website, and city links cover some of Idaho's larger cities.")}

<script src="local.js"></script>
<script src="reps.js"></script>
</body>
</html>
''')
print(len(ALL), "guides written")

(SITE / "legislature.html").write_text(f'''{head("The Idaho Legislature, day by day | CivicsID", "", "Every Idaho Legislature committee meeting coming up, with agendas, the bills on them, and how to testify in person or remotely.", "The Idaho Legislature, day by day")}
<a class="skip" href="#hearings">Skip to hearings</a>
{top("", "calendar")}

<section class="hero"><div class="wrap">
  <p class="eyebrow light">Idaho Legislature</p>
  <h1>What the Legislature is hearing, day by day.</h1>
  <p class="lede">Every committee meeting on the Legislature's calendar, with its agenda and the bills it will take up. Most committees take public testimony, in person at the Capitol or remotely.</p>
  <p class="small" id="session-note">The 2027 session opens Monday, January 11. Until then, these are interim committees, which study issues between sessions.</p>
</div></section>

<div class="wrap layout">
  <main class="main" id="hearings">
    <div class="heading">
      <h2 id="leg-heading">Coming up at the Legislature</h2>
      <span id="leg-range"></span>
    </div>
    <div class="list" id="leg-list" aria-live="polite"><p class="empty">Loading hearings…</p></div>
  </main>

  <aside class="side">
    <div class="card">
      <h2>How to testify</h2>
      <ol class="tight">
        <li>Find the bill on a committee's agenda below. Agendas usually post a few days ahead.</li>
        <li>Open the committee's page and use its <strong>Testimony Registration</strong> link to sign up to speak in person or remotely, or to submit written testimony.</li>
        <li>Keep it short: who you are, where you live, and how the bill would affect you. Committees often limit each person to a few minutes.</li>
      </ol>
      <a class="link" href="https://legislature.idaho.gov/resources/committeetestimony/" rel="noopener">The Legislature's testimony guide</a>
    </div>
    <div class="card">
      <h2>Other ways to weigh in</h2>
      <p>Email or call your own legislators, especially before a committee vote or a floor vote.</p>
      <a class="link" href="reps.html">Find your legislators</a>
      <p style="margin-top: 12px">Committee meetings and floor sessions stream live, and recordings are kept.</p>
      <a class="link" href="https://legislature.idaho.gov/calendar/#collapse6" rel="noopener">Watch live</a>
    </div>
    <div class="card warm">
      <span class="eyebrow">Engage</span>
      <h2>New to the Legislature?</h2>
      <p>Who's in it, how a bill moves, and the four ways to make your voice heard.</p>
      <a class="link" href="guides/weigh-in-on-a-state-bill.html">Read the guide</a>
    </div>
  </aside>
</div>

{footer("", "Committee meetings, agendas and bill lists come from the Idaho Legislature's own calendar and agendas, refreshed nightly. Agendas can change; check the committee's page before you go.")}

<script src="legislature.js"></script>
</body>
</html>
''')
