"""Generator for CivicsID's static pages (guides, Engage, reps, calendar shell).
Run: python3 tools/pages/gen.py  -- writes plain HTML into site/."""
import html, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import guides_a, guides_b, guides_c, guides_es

SITE = Path(__file__).resolve().parents[2] / "site"
FONTS = ('<link rel="preload" href="{up}fonts/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>\n'
         '<link rel="preload" href="{up}fonts/source-serif-4-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>')
SITE_URL = "https://civicsid.org/"
# The reps page also loads the Idaho State Tax Commission's district map (JSONP).
REPS_SCRIPTS = " https://services.arcgis.com"
REPORT = "admin@barnoneinc.org"
NOTICE = '<aside class="notice" aria-label="About CivicsID">A project of BarNone, a nonprofit. Not affiliated with any government agency.</aside>'
BY = ('<p class="by-barnone"><a href="https://barnoneinc.org"><img src="{up}barnone-phoenix.png" alt="" width="28" height="28">'
      '<span>A service of <strong>BarNone, Inc.</strong></span></a> An independent nonprofit. CivicsID is not a government website, '
      'is not affiliated with any government agency, and does not speak for any public office.</p>')


def head(title, up, desc, share=None, lang="en", scripts=""):
    """scripts: extra hosts this page may load scripts from, for its CSP."""
    share = share or title.split(" | ")[0]
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' https://geocoding.geo.census.gov{scripts}; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; manifest-src 'self'; worker-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<meta property="og:site_name" content="CivicsID">
<meta property="og:title" content="{html.escape(share, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{SITE_URL}{"share-es.png" if lang == "es" else "share.png"}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{"CivicsID: Participa, Idaho." if lang == "es" else "CivicsID: Get Engaged, Idaho."}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#7A1F2E">
<link rel="manifest" href="{up}manifest.webmanifest">
<link rel="icon" href="{up}favicon.ico" sizes="32x32">
<link rel="icon" href="{up}icon-192.png" type="image/png">
<link rel="apple-touch-icon" href="{up}apple-touch-icon.png">
{FONTS.format(up=up)}
<link rel="stylesheet" href="{up}styles.css">
<script src="{up}app-install.js" defer></script>
</head>
<body>'''


NAV = {"en": ("Community Calendar", "Calendar", "Engage", "My representatives", "My reps", "Main"),
       "es": ("Calendario comunitario", "Calendario", "Participa", "Mis representantes", "Mis reps", "Principal")}


def top(up, current, lang="en", alt=None, reps_up=None):
    """alt: link to this page in the other language."""
    cal, cal_s, eng, reps, reps_s, main = NAV[lang]
    notice = NOTICE if lang == "en" else '<aside class="notice" aria-label="Acerca de CivicsID">Un proyecto de BarNone, una organización sin fines de lucro. No está afiliado a ninguna agencia de gobierno.</aside>'
    switch = (f'\n  <a class="lang-switch" href="{alt}" lang="{"es" if lang == "en" else "en"}" hreflang="{"es" if lang == "en" else "en"}">{"Español" if lang == "en" else "English"}</a>' if alt else "")
    def a(href, label, key, short=None):
        cur = ' aria-current="page"' if key == current else ""
        if short:  # a shorter label on phones; the full name stays for screen readers
            return f'    <a href="{up}{href}"{cur} aria-label="{label}"><span class="full">{label}</span><span class="short">{short}</span></a>'
        return f'    <a href="{up}{href}"{cur}>{label}</a>'
    reps_href = (reps_up or up) + "reps.html"
    reps_link = a("reps.html", reps, "reps", reps_s).replace(f'href="{up}reps.html"', f'href="{reps_href}"')
    return f'''{notice}

<header class="top"><div class="wrap">
  <a class="brand" href="{up}index.html">Civics<span>ID</span></a>{switch}
  <nav aria-label="{main}">
{a("index.html", cal, "calendar", cal_s)}
{a("engage.html", eng, "engage")}
{reps_link}
  </nav>
</div></header>'''


def footer(up, first):
    return f'''<footer><div class="wrap">
  <p>{first}</p>
  {BY.format(up=up)}
  <p class="footer-links"><a href="mailto:{REPORT}?subject=CivicsID%3A%20report%20a%20problem">Report a problem or a missing meeting</a> · <a href="{up}privacy.html">Privacy</a></p>
</div></footer>'''


# ---------- guides ----------
ALL = {**guides_a.G, **guides_b.G, **guides_c.G}
for slug, g in ALL.items():
    sources = "\n".join(f'    <li><a href="{html.escape(u, quote=True)}" rel="noopener">{html.escape(t)}</a></li>' for u, t in g["sources"])
    script = '\n<script src="../local.js"></script>' if 'class="near-you"' in g["body"] else ""
    page = f'''{head(g["title"] + " | CivicsID", "../", g["lede"])}
<a class="skip" href="#guide">Skip to guide</a>
{top("../", "engage", alt=("../es/guides/" + slug + ".html") if slug in guides_es.G else "../es/engage.html")}

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
{top("", "engage", alt="es/engage.html")}

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
{top("", "calendar", alt="es/index.html")}

<section class="hero"><div class="wrap">
  <p class="eyebrow light">Community Calendar</p>
  <h1>Find out what your community is deciding this week.</h1>
  <p class="lede">City councils, county commissioners, public hearings and the Legislature, from across Idaho, in one calendar. Pick where you live and we'll show you what's near you.</p>
  <form class="search" id="search">
    <div class="field">
      <label for="county">County</label>
      <select id="county"><option value="">All of Idaho</option></select>
    </div>
    <div class="field">
      <label for="city">City</label>
      <select id="city" disabled><option value="">Pick a county first</option></select>
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
      <label for="q">Search meetings</label>
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
      <p style="margin-top: 14px">Want to hear when something changes? The <a id="feed" href="data/feeds/statewide.xml">what's-new feed</a> lists new meetings, newly posted agendas and cancellations. Add it to a feed reader, or to a free feed-to-email service to get it by email.</p>
    </div>
    <div class="card">
      <h2>Use it like an app</h2>
      <p>Add CivicsID to your home screen and it opens like an app, even without a signal. On iPhone, tap Share, then <strong>Add to Home Screen</strong>. On Android, tap the menu, then <strong>Install app</strong> or <strong>Add to Home screen</strong>.</p>
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
(SITE / "reps.html").write_text(f'''{head("Who represents you | CivicsID", "", "Enter an Idaho street address to see every district you live in, your state legislators and members of Congress, plus where to find your city and county officials.", scripts=REPS_SCRIPTS)}
<a class="skip" href="#results">Skip to results</a>
{top("", "reps", alt="es/reps.html")}

<section class="hero"><div class="wrap">
  <h1>Find who represents you.</h1>
  <p class="lede">Enter an Idaho street address to see every district you live in, from Congress down to your fire and library districts, plus your state legislators and members of Congress and how to reach them.</p>
  <form class="search" id="lookup">
    <div class="field wide">
      <label for="address">Street address</label>
      <input id="address" name="address" type="text" autocomplete="street-address" placeholder="700 W Jefferson St, Boise">
    </div>
    <button class="btn" type="submit">Look up</button>
  </form>
  <p class="small">Your address is sent from your browser to the U.S. Census Bureau's address lookup to find your districts. Only the map point it returns, not your address, goes to the Idaho State Tax Commission's public map to find special districts. CivicsID never receives or stores either. Your browser remembers only your county and city, so the Engage guides can show local links.</p>
</div></section>

<main class="wrap narrow" style="padding-block: 40px 64px">
  <div class="list" id="results" aria-live="polite">
    <p class="empty">Your representatives will show up here.</p>
  </div>
  <p class="muted" style="margin-top: 24px">Not sure what to say once you have a name? Read <a href="guides/contact-your-representatives.html">how to contact the people who represent you</a>.</p>
</main>

{footer("", "State legislators come from Open States, a public roster built from the Idaho Legislature's member pages, and members of Congress from a public roster. Both are refreshed nightly. County links cover all 44 counties where we could confirm a website, and city links cover some of Idaho's larger cities.")}

<script src="local.js"></script>
<script src="districts.js"></script>
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


# ---------- Spanish (site/es/) ----------
ES = SITE / "es"
(ES / "guides").mkdir(parents=True, exist_ok=True)
FOOT_ES = ('<p class="by-barnone"><a href="https://barnoneinc.org"><img src="{up}barnone-phoenix.png" alt="" width="28" height="28">'
           '<span>Un servicio de <strong>BarNone, Inc.</strong></span></a> Una organización independiente sin fines de lucro. CivicsID no es un sitio '
           'de gobierno, no está afiliado a ninguna agencia de gobierno y no habla en nombre de ningún cargo público.</p>')


def footer_es(up, first):
    return f'''<footer><div class="wrap">
  <p>{first}</p>
  {FOOT_ES.format(up=up)}
  <p class="footer-links"><a href="mailto:{REPORT}?subject=CivicsID%3A%20reportar%20un%20problema">Reportar un problema o una reunión que falta</a> · <a href="{up}es/privacy.html">Privacidad</a></p>
</div></footer>'''


for slug, g in guides_es.G.items():
    sources = "\n".join(f'    <li><a href="{html.escape(u, quote=True)}" rel="noopener">{html.escape(t)}</a></li>' for u, t in g["sources"])
    script = '\n<script src="../../local.js"></script>' if 'class="near-you"' in g["body"] else ""
    (ES / "guides" / f"{slug}.html").write_text(f'''{head(g["title"] + " | CivicsID", "../../", g["lede"], lang="es")}
<a class="skip" href="#guide">Ir a la guía</a>
{top("../", "engage", lang="es", alt="../../guides/" + slug + ".html")}

<main class="wrap narrow guide" id="guide">
  <p class="eyebrow"><a href="../engage.html">Participa</a> · {g["cat"]}</p>
  <h1>{html.escape(g["title"])}</h1>
  <p class="lede">{html.escape(g["lede"])}</p>
{g["body"].strip(chr(10))}

  <h2>Fuentes</h2>
  <ul class="sources-list">
{sources}
  </ul>
  <p class="muted">Revisado en noviembre de 2026. Esta guía es información general, no asesoría legal. Las reglas cambian, así que revise las fuentes antes de depender de un plazo.</p>
</main>

{footer_es("../../", "Cada guía cita sus fuentes para que usted pueda verificarlas.")}{script}
</body>
</html>
'''.replace('href="../../styles.css"', 'href="../../styles.css"'))

# Same sections and order as the English Engage page.
ES_SECTIONS = [
    ("Empiece aquí", [
        ("reps.html", "Quién le representa", "Escriba su dirección para ver a sus representantes de la ciudad, el condado, el estado y el gobierno federal."),
        ("guides/contact-your-representatives.html", None, "Cómo escoger la oficina correcta y escribir un mensaje que sí se lea."),
    ]),
    ("Su ciudad y su condado", [
        ("guides/local-government.html", None, "Condados, ciudades, distritos escolares y los distritos especiales que manejan caminos, bomberos, agua y más."),
        ("guides/speak-at-a-public-meeting.html", None, "Lo que la ley de Idaho le permite, lo que no, y cómo aprovechar dos minutos."),
        ("guides/open-meeting-law.html", None, "Avisos, agendas, sesiones a puerta cerrada, su derecho a grabar y qué hacer cuando no se cumple la ley."),
        ("guides/public-records-requests.html", None, "Cómo pedir correos, contratos e informes, cuánto cuesta, los plazos y qué hacer si le dicen que no."),
        ("guides/your-neighborhood.html", None, "Cómo lograr que arreglen problemas, enterarse de lo que se planea y organizar a sus vecinos."),
        ("guides/local-ballot-measures.html", None, "Bonos, impuestos locales (levies), y por qué un bono escolar puede sacar 60 por ciento y aun así no aprobarse."),
    ]),
    ("El estado de Idaho", [
        ("guides/legislature.html", None, "Quiénes la forman, el calendario de la sesión, cómo avanza un proyecto de ley y dónde cuenta su voz."),
        ("guides/weigh-in-on-a-state-bill.html", None, "Cuatro maneras de decirle a la Legislatura lo que usted piensa, y los tiempos que toman a la gente por sorpresa."),
        ("guides/state-budgets.html", None, "El ciclo anual, el comité que lo escribe y cuándo puede participar en cada paso."),
        ("guides/boards-and-commissions.html", None, "Cómo se nombra a residentes en juntas estatales, del condado y de la ciudad."),
        ("guides/campaign-finance.html", None, "Quién les da dinero a los candidatos de Idaho, cuáles son los límites y dónde consultarlo."),
        ("guides/state-agencies.html", None, "Un directorio corto para las necesidades más comunes, y qué hacer cuando se atora."),
        ("guides/running-for-office.html", None, "Qué cargos se eligen y cuándo, cómo inscribirse como candidato y lo básico del financiamiento de campañas."),
        ("guides/state-initiatives.html", None, "Cómo los votantes ponen una ley en la boleta, las reglas de las firmas y los plazos."),
    ]),
    ("El gobierno federal", [
        ("guides/federal-offices.html", None, "La Cámara de Representantes, el Senado y la Presidencia, y lo que la Constitución exige para cada uno."),
        ("guides/courts.html", None, "Las cortes estatales de Idaho y las cortes federales, lado a lado."),
        ("guides/constitution.html", None, "Las constituciones de Estados Unidos y de Idaho, y cómo se cambia cada una."),
        ("guides/federal-agencies.html", None, "Ayuda con casos, decisiones sobre tierras públicas, comentarios sobre reglamentos y solicitudes de registros."),
        ("guides/federal-budget.html", None, "Las asignaciones, el año fiscal y las solicitudes de proyectos comunitarios."),
    ]),
    ("Habilidades y vida diaria", [
        ("guides/two-minute-pitch.html", None, "Una forma sencilla de presentar su caso en el tiempo que le dan."),
        ("guides/read-a-bill-or-agenda.html", None, "Números de proyectos de ley, subrayados y tachados, puntos de acción y paquetes de la reunión."),
        ("guides/media-literacy.html", "Cómo evaluar la información", "Hábitos rápidos para distinguir la buena información de la mala."),
        ("guides/volunteer-and-public-service.html", None, "Dónde encontrar puestos de voluntario y empleos en el gobierno."),
        ("guides/problem-to-policy.html", None, "Cómo encontrar el nivel de gobierno correcto y armar una petición concreta."),
    ]),
]
es_blocks, es_listed = [], set()
for i, (heading, items) in enumerate(ES_SECTIONS):
    style = ' style="margin-top: 20px"' if i else ""
    rows = []
    for href, label, blurb in items:
        if href.startswith("guides/"):
            slug = href[7:-5]
            es_listed.add(slug)
            label = label or guides_es.G[slug]["title"]
        rows.append(f'    <li><a href="{href}">{html.escape(label)}<span>{html.escape(blurb)}</span></a></li>')
    es_blocks.append(f'  <h2{style}>{heading}</h2>\n  <ul class="guide-links">\n' + "\n".join(rows) + "\n  </ul>")
assert es_listed == set(guides_es.G), (es_listed ^ set(guides_es.G))
(ES / "engage.html").write_text(f'''{head("Participa | CivicsID", "../", "Guías en lenguaje sencillo sobre cómo funciona el gobierno en Idaho y dónde puede participar.", lang="es")}
<a class="skip" href="#guides">Ir a las guías</a>
{top("", "engage", lang="es", alt="../engage.html")}

<section class="hero plain"><div class="wrap">
  <h1>Participa: cómo tomar parte, desde su cuadra hasta el Congreso.</h1>
  <p class="lede">Guías en lenguaje sencillo sobre cómo funciona el gobierno en Idaho y dónde puede participar. Cada guía cita sus fuentes para que usted pueda verificarlas. Muchas de las páginas oficiales que citamos están solo en inglés.</p>
</div></section>

<main class="wrap" id="guides" style="padding-block: 32px 64px; display: flex; flex-direction: column; gap: 20px">
{chr(10).join(es_blocks)}
</main>

{footer_es("../", "Las guías están escritas en lenguaje sencillo, citan sus fuentes y funcionan con lectores de pantalla.")}
</body>
</html>
'''.replace('href="styles.css"', 'href="../styles.css"').replace('src="barnone-phoenix.png"', 'src="../barnone-phoenix.png"'))

(ES / "index.html").write_text(f'''{head("Participa en Idaho | CivicsID", "../", "Vea lo que deciden esta semana su concejo municipal, los comisionados del condado, la junta de la biblioteca y la Legislatura de Idaho, y cómo hacerse escuchar.", "Participa en Idaho: lo que su comunidad decide esta semana", lang="es")}
<a class="skip" href="#events">Ir a las reuniones</a>
{top("", "calendar", lang="es", alt="../index.html")}

<section class="hero"><div class="wrap">
  <p class="eyebrow light">Calendario comunitario</p>
  <h1>Entérese de lo que su comunidad decide esta semana.</h1>
  <p class="lede">Concejos municipales, comisionados del condado, audiencias públicas y la Legislatura, de todo Idaho, en un solo calendario. Elija dónde vive y le mostraremos lo que hay cerca.</p>
  <form class="search" id="search">
    <div class="field">
      <label for="county">Condado</label>
      <select id="county"><option value="">Todo Idaho</option></select>
    </div>
    <div class="field">
      <label for="city">Ciudad</label>
      <select id="city" disabled><option value="">Primero elija un condado</option></select>
    </div>
  </form>
  <p class="small"><span id="coverage"></span> No necesita cuenta, y su elección se guarda solo en su navegador.</p>
</div></section>

<div class="wrap layout">
  <main class="main" id="events">
    <div class="heading">
      <h2 id="heading">Próximas reuniones en todo Idaho</h2>
      <span id="range"></span>
    </div>
    <p class="muted">Los nombres de las reuniones y las agendas vienen de cada entidad y están en inglés.</p>
    <div class="find">
      <label for="q">Buscar reuniones (en inglés)</label>
      <input id="q" type="search" placeholder="Pruebe zoning, library, budget, school" autocomplete="off">
    </div>
    <div class="chips" role="group" aria-label="Filtrar por tipo" id="chips"></div>
    <div class="list" id="list" aria-live="polite"><p class="empty">Cargando reuniones…</p></div>
    <button class="more" id="more" type="button" hidden>Mostrar dos semanas más</button>
  </main>

  <aside class="side">
    <div class="card">
      <h2>En su teléfono</h2>
      <p id="subscribe-text">Suscríbase una vez y estas reuniones aparecerán en la aplicación de calendario que ya usa.</p>
      <a class="link" id="subscribe" href="../data/ics/statewide.ics">Suscribirse a las reuniones de comités de la Legislatura</a>
      <p style="margin-top: 14px">¿Quiere saber cuándo cambia algo? El <a id="feed" href="../data/feeds/statewide.xml">canal de novedades</a> muestra reuniones nuevas, agendas recién publicadas y cancelaciones. Agréguelo a un lector de noticias o a un servicio gratuito que lo envíe por correo.</p>
    </div>
    <div class="card">
      <h2>Úselo como aplicación</h2>
      <p>Agregue CivicsID a su pantalla de inicio y se abrirá como una aplicación, incluso sin señal. En iPhone, toque Compartir y luego <strong>Agregar a pantalla de inicio</strong>. En Android, toque el menú y luego <strong>Instalar aplicación</strong>.</p>
    </div>
    <div class="card">
      <h2>Dos zonas horarias</h2>
      <p>Cada reunión aparece en su hora local: hora de la Montaña para casi todo Idaho, hora del Pacífico para el norte del estado.</p>
    </div>
    <div class="card warm">
      <span class="eyebrow">Participa</span>
      <h2>¿Primera vez en una reunión pública?</h2>
      <p>Lo que la ley de Idaho le permite, qué decir en dos minutos y qué pasa después.</p>
      <a class="link" href="guides/speak-at-a-public-meeting.html">Leer la guía</a>
    </div>
  </aside>
</div>

{footer_es("../", 'Las reuniones vienen directamente de los calendarios públicos de cada agencia y se actualizan cada noche. <span id="updated"></span> Los horarios cambian, así que confirme con la entidad antes de ir.')}

<script src="../app.js"></script>
</body>
</html>
'''.replace('href="styles.css"', 'href="../styles.css"').replace('src="barnone-phoenix.png"', 'src="../barnone-phoenix.png"'))
print("Spanish pages written:", len(guides_es.G) + 2)


# ---------- Privacy (English and Spanish) ----------
PRIV_EN = """
  <h2>The short version</h2>
  <p>CivicsID has no accounts, no ads, no cookies and no tracking or analytics. We don't collect your name, email or address.</p>
  <h2>What stays on your device</h2>
  <ul>
    <li><strong>Your county and city.</strong> When you pick them, your browser remembers them so the calendar opens there next time. That choice is stored only in your browser. Clearing your browser data removes it.</li>
    <li><strong>The app.</strong> If you add CivicsID to your home screen, your device keeps a copy of the pages and the latest calendar so it works without a signal.</li>
  </ul>
  <h2>What leaves your device</h2>
  <ul>
    <li><strong>Address lookups.</strong> When you look up your representatives, your browser sends the address straight to the U.S. Census Bureau's public geocoder to find your districts. Your browser then sends only the map point the Census Bureau returns, not the address, to the Idaho State Tax Commission's public map service to find fire, library and other special districts. Neither passes through us, and we never see or store them.</li>
    <li><strong>Hosting.</strong> The site is hosted on GitHub Pages. Like any web host, GitHub keeps standard server logs, such as IP addresses, for security. We don't get or use those logs.</li>
    <li><strong>Links you follow.</strong> Meeting details, agendas and guide sources open on government and other websites, which have their own privacy policies.</li>
    <li><strong>Problem reports.</strong> If you email us a correction, it goes to BarNone's inbox ({REPORT}). We use it only to fix the site.</li>
  </ul>
  <p class="muted">Updated November 2026. Questions: {REPORT}.</p>
"""
PRIV_ES = """
  <h2>En resumen</h2>
  <p>CivicsID no tiene cuentas, anuncios, cookies, rastreo ni analítica. No recopilamos su nombre, correo ni dirección.</p>
  <h2>Lo que se queda en su dispositivo</h2>
  <ul>
    <li><strong>Su condado y ciudad.</strong> Cuando los elige, su navegador los recuerda para que el calendario abra allí la próxima vez. Esa elección se guarda solo en su navegador.</li>
    <li><strong>La aplicación.</strong> Si agrega CivicsID a su pantalla de inicio, su dispositivo guarda una copia de las páginas y del calendario más reciente para que funcione sin señal.</li>
  </ul>
  <h2>Lo que sale de su dispositivo</h2>
  <ul>
    <li><strong>Búsqueda por dirección.</strong> Cuando busca a sus representantes, su navegador envía la dirección directamente al servicio público de la Oficina del Censo de EE. UU. Después envía solo el punto en el mapa que devuelve el Censo, no la dirección, al servicio de mapas público de la Comisión de Impuestos del Estado de Idaho para encontrar los distritos especiales, como los de bomberos y bibliotecas. Nada de esto pasa por nosotros y nunca lo vemos ni lo guardamos.</li>
    <li><strong>Alojamiento.</strong> El sitio está en GitHub Pages. Como cualquier servidor web, GitHub guarda registros estándar, como direcciones IP, por seguridad. Nosotros no recibimos ni usamos esos registros.</li>
    <li><strong>Enlaces.</strong> Los detalles de reuniones, agendas y fuentes abren en sitios de gobierno y otros sitios, que tienen sus propias políticas de privacidad.</li>
    <li><strong>Reportes de problemas.</strong> Si nos envía una corrección por correo, llega a la bandeja de BarNone ({REPORT}). Solo la usamos para corregir el sitio.</li>
  </ul>
  <p class="muted">Actualizado en noviembre de 2026. Preguntas: {REPORT}.</p>
"""
(SITE / "privacy.html").write_text(f'''{head("Privacy | CivicsID", "", "CivicsID has no accounts, no ads, no cookies and no tracking.")}
<a class="skip" href="#privacy">Skip to content</a>
{top("", "", alt="es/privacy.html")}
<main class="wrap narrow guide" id="privacy">
  <h1>Privacy</h1>
{PRIV_EN.format(REPORT=REPORT)}
</main>
{footer("", "CivicsID is free to use and asks nothing of you.")}
</body>
</html>
''')
(ES / "privacy.html").write_text(f'''{head("Privacidad | CivicsID", "../", "CivicsID no tiene cuentas, anuncios, cookies ni rastreo.", lang="es")}
<a class="skip" href="#privacy">Ir al contenido</a>
{top("", "", lang="es", alt="../privacy.html")}
<main class="wrap narrow guide" id="privacy">
  <h1>Privacidad</h1>
{PRIV_ES.format(REPORT=REPORT)}
</main>
{footer_es("../", "CivicsID es gratis y no le pide nada.")}
</body>
</html>
'''.replace('href="styles.css"', 'href="../styles.css"').replace('src="barnone-phoenix.png"', 'src="../barnone-phoenix.png"'))
print("privacy pages written")

(ES / "reps.html").write_text(f'''{head("Quién le representa | CivicsID", "../", "Escriba una dirección de Idaho para ver todos los distritos donde vive, sus legisladores estatales y miembros del Congreso, y dónde encontrar a los funcionarios de su ciudad y condado.", lang="es", scripts=REPS_SCRIPTS)}
<a class="skip" href="#results">Ir a los resultados</a>
{top("", "reps", lang="es", alt="../reps.html")}

<section class="hero"><div class="wrap">
  <h1>Encuentre quién le representa.</h1>
  <p class="lede">Escriba una dirección de Idaho para ver todos los distritos donde vive, desde el Congreso hasta sus distritos de bomberos y bibliotecas, además de sus legisladores estatales y miembros del Congreso y cómo comunicarse con ellos.</p>
  <form class="search" id="lookup">
    <div class="field wide">
      <label for="address">Dirección</label>
      <input id="address" name="address" type="text" autocomplete="street-address" placeholder="700 W Jefferson St, Boise">
    </div>
    <button class="btn" type="submit">Buscar</button>
  </form>
  <p class="small">Su navegador envía la dirección al servicio de búsqueda de direcciones de la Oficina del Censo de EE. UU. para encontrar sus distritos. Solo el punto en el mapa que devuelve, no su dirección, va al mapa público de la Comisión de Impuestos del Estado de Idaho para encontrar los distritos especiales. CivicsID nunca recibe ni guarda ninguno de los dos. Su navegador recuerda solo su condado y ciudad, para que las guías puedan mostrar enlaces locales.</p>
</div></section>

<main class="wrap narrow" style="padding-block: 40px 64px">
  <div class="list" id="results" aria-live="polite">
    <p class="empty">Sus representantes aparecerán aquí.</p>
  </div>
  <p class="muted" style="margin-top: 24px">¿No sabe qué decir cuando ya tiene un nombre? Lea <a href="guides/contact-your-representatives.html">cómo comunicarse con quienes le representan</a>.</p>
</main>

{footer_es("../", "Los legisladores estatales vienen de Open States, una lista pública basada en las páginas de miembros de la Legislatura de Idaho, y los miembros del Congreso de una lista pública. Ambas se actualizan cada noche. Los enlaces de condados cubren los 44 condados donde pudimos confirmar un sitio web, y los de ciudades cubren algunas de las ciudades más grandes de Idaho. Los sitios enlazados están en inglés.")}

<script src="../local.js"></script>
<script src="../districts.js"></script>
<script src="../reps.js"></script>
</body>
</html>
'''.replace('href="styles.css"', 'href="../styles.css"').replace('src="barnone-phoenix.png"', 'src="../barnone-phoenix.png"'))
print("Spanish reps page written")




# Every page's intro band is a named region, so screen reader users can jump
# to it and nothing on the page sits outside a landmark.
for page in SITE.rglob("*.html"):
    text = page.read_text()
    label = "Introducción" if '<html lang="es">' in text else "Introduction"
    fixed = re.sub(r'<section class="hero', f'<section aria-label="{label}" class="hero', text)
    if fixed != text:
        page.write_text(fixed)


# Search engines: each page names its one true address (canonical), points to
# its translation (hreflang), and the home pages say who runs the site. Then a
# sitemap lists every page, and robots.txt points to it.
def page_url(rel):
    rel = rel.replace("\\", "/")
    if rel == "index.html":
        return SITE_URL
    if rel.endswith("/index.html"):
        return SITE_URL + rel[: -len("index.html")]
    return SITE_URL + rel


def twin(rel):
    """The same page in the other language, or None if it isn't translated."""
    other = rel[3:] if rel.startswith("es/") else "es/" + rel
    return other if (SITE / other).exists() else None


ORG = {
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "WebSite", "@id": SITE_URL + "#site", "name": "CivicsID", "url": SITE_URL,
         "inLanguage": ["en", "es"], "publisher": {"@id": "https://barnoneinc.org/#org"},
         "description": "A free calendar of what Idaho's city councils, county commissions, school and library boards and the Legislature are deciding, with plain-language guides to taking part."},
        {"@type": "NGO", "@id": "https://barnoneinc.org/#org", "name": "BarNone", "url": "https://barnoneinc.org",
         "logo": SITE_URL + "barnone-phoenix.png"},
    ],
}

pages = sorted(p.relative_to(SITE).as_posix() for p in SITE.rglob("*.html") if p.name != "404.html")
MARK = "<!-- seo -->"
for rel in pages:
    page = SITE / rel
    text = re.sub(re.escape(MARK) + r".*?" + re.escape(MARK) + "\n", "", page.read_text(), flags=re.S)
    tags = [f'<link rel="canonical" href="{page_url(rel)}">',
            f'<meta property="og:url" content="{page_url(rel)}">']
    other = twin(rel)
    if other:
        en, es = (other, rel) if rel.startswith("es/") else (rel, other)
        tags += [f'<link rel="alternate" hreflang="en" href="{page_url(en)}">',
                 f'<link rel="alternate" hreflang="es" href="{page_url(es)}">',
                 f'<link rel="alternate" hreflang="x-default" href="{page_url(en)}">']
    if rel in ("index.html", "es/index.html"):
        tags.append('<script type="application/ld+json">' + json.dumps(ORG).replace("</", "<\\/") + "</script>")
    block = MARK + "\n" + "\n".join(tags) + "\n" + MARK + "\n"
    page.write_text(text.replace("</head>", block + "</head>", 1))

entries = []
for rel in pages:
    links = ""
    other = twin(rel)
    if other:
        en, es = (other, rel) if rel.startswith("es/") else (rel, other)
        links = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{page_url(r)}"/>'
                        for l, r in (("en", en), ("es", es), ("x-default", en)))
    entries.append(f"  <url>\n    <loc>{page_url(rel)}</loc>{links}\n  </url>")
(SITE / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    + "\n".join(entries) + "\n</urlset>\n")
(SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n")
print(f"search pieces written: {len(pages)} pages in the sitemap")


# ---------- page not found ----------
# GitHub Pages serves 404.html for any address that doesn't exist, at any
# depth, so every link in it starts from the site root. Written last so it
# stays out of the sitemap and carries no canonical address.
(SITE / "404.html").write_text(f'''{head("Page not found | CivicsID", "/", "That page isn't here. Head back to the CivicsID calendar, guides or representatives lookup.").replace("</head>", '<meta name="robots" content="noindex">' + chr(10) + "</head>")}
<a class="skip" href="#notfound">Skip to content</a>
{top("/", "", alt="/es/index.html")}
<main class="wrap narrow guide" id="notfound">
  <h1>We can't find that page.</h1>
  <p>The address may be mistyped, or the page may have moved. Here's where most people are headed:</p>
  <ul>
    <li><a href="/index.html">Community Calendar</a>: what your city, county, school board and the Legislature are deciding.</li>
    <li><a href="/engage.html">Engage</a>: plain-language guides to taking part.</li>
    <li><a href="/reps.html">My representatives</a>: who represents you, by address.</li>
  </ul>
  <p lang="es">¿Busca la versión en español? Vaya al <a href="/es/index.html" hreflang="es">calendario en español</a>.</p>
  <p class="muted">Followed a link on this site to get here? <a href="mailto:{REPORT}?subject=CivicsID%3A%20broken%20link">Tell us</a> and we'll fix it.</p>
</main>
{footer("/", "CivicsID is free to use and asks nothing of you.")}
</body>
</html>
''')
print("404 page written")
