/* CivicsID calendar page. Reads data/events.json and data/status.json,
   which the nightly pipeline writes. Everything runs in the browser. */
(function () {
  'use strict';

  // English and Spanish wording. Pages under /es/ set <html lang="es">.
  // Meeting names and agendas come from the hosts, so they stay in English.
  var LANG = document.documentElement.lang === 'es' ? 'es' : 'en';
  var BASE = LANG === 'es' ? '../' : '';
  var S = {
    en: {
      all: 'All', council: 'Councils and commissions', hearing: 'Public hearings', legislature: 'Idaho Legislature',
      school: 'School boards', library: 'Library programs', other: 'Other', locale: 'en-US',
      noTime: 'Time not listed', noTimeRegular: 'Time not posted', pacific: 'Pacific', mountain: 'Mountain',
      cancelled: 'Cancelled', usually: 'Usually meets', onAgenda: 'On the agenda',
      more: function (n) { return 'and ' + n + ' more ' + (n === 1 ? 'item' : 'items'); },
      regularPosted: 'From the host’s regular schedule. The host has posted an agenda for this date.',
      regularNote: 'From the host’s regular schedule, not a posted agenda. Check the host’s page before you go.',
      details: 'Details from the host', agenda: 'Agenda', addCal: 'Add to my calendar', openLink: 'Open link',
      matches: function (n, q) { return n + (n === 1 ? ' match' : ' matches') + ' for “' + q + '” in all upcoming meetings'; },
      range: function (a, b, n) { return a + ' to ' + b + ' · ' + n + (n === 1 ? ' event' : ' events'); },
      heading: function (city, county) { return 'Coming up ' + (city ? 'in and around ' + city : county ? 'in ' + county + ' County' : 'across Idaho'); },
      subCounty: function (c) { return 'Subscribe to ' + c + ' County meetings'; },
      subLeg: 'Subscribe to Idaho Legislature committee meetings',
      subCountyText: function (c) { return 'Subscribe once and ' + c + ' County meetings show up in the calendar app you already use.'; },
      subLegText: 'Pick your county above to subscribe to its meetings. Or follow the Legislature’s committee meetings in your own calendar app.',
      noneType: 'Nothing of this type is listed for these dates. Try another filter or show more weeks.',
      noneLoaded: 'No events are loaded yet. The calendar fills in after its first nightly run.',
      noneSearch: function (q) { return 'No upcoming meetings mention “' + q + '” here. Agendas post a few days ahead, so check back, or try a broader word or all of Idaho.'; },
      allIdaho: 'All of Idaho', county: function (c) { return c + ' County'; }, linksOnly: ' (links only)',
      coverage: function (n) { return 'Meetings from ' + n + ' of Idaho’s 44 counties so far, and links for the rest.'; },
      cantRead: function (c) { return 'We can’t read ' + c + ' County’s meeting calendar yet'; },
      cantReadText: 'The county posts its commissioners’ meetings and agendas on its own website. Until we can add them here, that’s the place to check. Idaho law requires an agenda to be posted at least 48 hours before a regular meeting.',
      countyMeetings: function (c) { return c + ' County meetings and agendas'; },
      anywhere: function (c) { return 'Anywhere in ' + c + ' County'; }, pickCounty: 'Pick a county',
      report: 'Report a problem', reportSubject: 'CivicsID: problem with a meeting listing',
      reportBody: 'What looks wrong (time moved, cancelled, wrong place, something else)?\n\n\n',
      refreshed: 'Last refreshed ', loadFail: 'The calendar could not be loaded. Please try again later.'
    },
    es: {
      all: 'Todo', council: 'Concejos y comisiones', hearing: 'Audiencias públicas', legislature: 'Legislatura de Idaho',
      school: 'Juntas escolares', library: 'Bibliotecas', other: 'Otros', locale: 'es-US',
      noTime: 'Hora no indicada', noTimeRegular: 'Hora no publicada', pacific: 'Pacífico', mountain: 'Montaña',
      cancelled: 'Cancelada', usually: 'Reunión habitual', onAgenda: 'En la agenda',
      more: function (n) { return 'y ' + n + (n === 1 ? ' punto más' : ' puntos más'); },
      regularPosted: 'Según el calendario habitual de la entidad. La entidad ya publicó una agenda para esta fecha.',
      regularNote: 'Según el calendario habitual de la entidad, no una agenda publicada. Confirme en la página de la entidad antes de ir.',
      details: 'Detalles de la entidad', agenda: 'Agenda (en inglés)', addCal: 'Agregar a mi calendario', openLink: 'Abrir enlace',
      matches: function (n, q) { return n + (n === 1 ? ' resultado' : ' resultados') + ' para “' + q + '” en todas las reuniones próximas'; },
      range: function (a, b, n) { return 'Del ' + a + ' al ' + b + ' · ' + n + (n === 1 ? ' reunión' : ' reuniones'); },
      heading: function (city, county) { return 'Próximamente ' + (city ? 'en ' + city + ' y sus alrededores' : county ? 'en el condado de ' + county : 'en todo Idaho'); },
      subCounty: function (c) { return 'Suscribirse a las reuniones del condado de ' + c; },
      subLeg: 'Suscribirse a las reuniones de comités de la Legislatura',
      subCountyText: function (c) { return 'Suscríbase una vez y las reuniones del condado de ' + c + ' aparecerán en la aplicación de calendario que ya usa.'; },
      subLegText: 'Elija su condado arriba para suscribirse a sus reuniones, o siga las reuniones de comités de la Legislatura en su propio calendario.',
      noneType: 'No hay reuniones de este tipo en estas fechas. Pruebe otro filtro o muestre más semanas.',
      noneLoaded: 'Todavía no hay reuniones cargadas. El calendario se llena después de su primera actualización nocturna.',
      noneSearch: function (q) { return 'Ninguna reunión próxima menciona “' + q + '” aquí. Las agendas se publican unos días antes, así que vuelva a revisar, o pruebe una palabra más general o todo Idaho. Las agendas están en inglés.'; },
      allIdaho: 'Todo Idaho', county: function (c) { return 'Condado de ' + c; }, linksOnly: ' (solo enlaces)',
      coverage: function (n) { return 'Reuniones de ' + n + ' de los 44 condados de Idaho, y enlaces para los demás.'; },
      cantRead: function (c) { return 'Todavía no podemos leer el calendario del condado de ' + c; },
      cantReadText: 'El condado publica las reuniones y agendas de sus comisionados en su propio sitio web. Hasta que podamos agregarlas aquí, revise allí. La ley de Idaho exige publicar la agenda al menos 48 horas antes de una reunión ordinaria.',
      countyMeetings: function (c) { return 'Reuniones y agendas del condado de ' + c; },
      anywhere: function (c) { return 'Cualquier lugar del condado de ' + c; }, pickCounty: 'Elija condado',
      report: 'Reportar un problema', reportSubject: 'CivicsID: problema con una reunión',
      reportBody: '¿Qué está mal (cambió la hora, se canceló, lugar equivocado, otra cosa)?\n\n\n',
      refreshed: 'Última actualización: ', loadFail: 'No se pudo cargar el calendario. Inténtelo de nuevo más tarde.'
    }
  }[LANG];

  var CATEGORIES = [
    { id: 'all', label: S.all },
    { id: 'council', label: S.council },
    { id: 'hearing', label: S.hearing },
    { id: 'legislature', label: S.legislature },
    { id: 'school', label: S.school },
    { id: 'library', label: S.library },
    { id: 'other', label: S.other }
  ];
  var LABELS = { legislature: S.legislature, council: S.council, hearing: S.hearing, school: S.school, library: S.library, other: S.other };

  // The visitor's county and city, shared with the Engage guides' "Near you"
  // boxes and the representatives lookup. Kept in this browser only.
  var KEY = 'civicsid.place';
  function loadPlace() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
  function savePlace(p) { try { localStorage.setItem(KEY, JSON.stringify(p)); } catch (e) { /* private mode */ } }
  function slug(c) { return c.toLowerCase().replace(/[^a-z]+/g, '-').replace(/^-|-$/g, ''); }

  var state = { events: [], sources: [], local: {}, connected: null, cat: 'all', county: '', city: '', days: 14, q: '' };
  var $ = function (id) { return document.getElementById(id); };

  function el(tag, cls, text) {
    var node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text != null) node.textContent = text;
    return node;
  }
  function safeUrl(url) { return /^https?:\/\//i.test(url || '') ? url : ''; }

  // Event times arrive as local wall-clock ISO strings (Mountain time for most
  // of Idaho, Pacific in the north); read the parts directly so the page shows
  // the meeting's own local time wherever the visitor is. Each event carries
  // a "tz" label, MT or PT, shown under the time.
  function parts(iso) {
    var m = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})/.exec(iso);
    return { y: +m[1], mo: +m[2], d: +m[3], h: +m[4], mi: +m[5], key: m[1] + '-' + m[2] + '-' + m[3] };
  }
  function clock(p) {
    var h = p.h % 12 || 12;
    return h + (p.mi ? ':' + String(p.mi).padStart(2, '0') : '') + (p.h < 12 ? ' AM' : ' PM');
  }
  function dayLabel(p) {
    return new Date(p.y, p.mo - 1, p.d).toLocaleDateString(S.locale, { weekday: 'long', month: 'long', day: 'numeric' });
  }
  function todayKey() {
    var s = new Date().toLocaleDateString('en-CA', { timeZone: 'America/Boise' });
    return s.slice(0, 10);
  }
  function addDays(key, n) {
    var d = new Date(key + 'T12:00:00Z');
    d.setUTCDate(d.getUTCDate() + n);
    return d.toISOString().slice(0, 10);
  }

  // Search looks at everything we have (about two months), not just the
  // weeks shown, and matches every word typed.
  function matches(e, words) {
    var hay = [e.title, e.host, e.location, (e.highlights || []).join(' '), LABELS[e.category]].join(' ').toLowerCase();
    return words.every(function (w) { return hay.indexOf(w) !== -1; });
  }

  function visible() {
    var from = todayKey(), to = state.q ? '9999-12-31' : addDays(from, state.days);
    var words = state.q.toLowerCase().split(/\s+/).filter(Boolean);
    return state.events.filter(function (e) {
      var key = e.start.slice(0, 10);
      if (key < from || key > to) return false;
      if (words.length && !matches(e, words)) return false;
      if (state.cat !== 'all' && e.category !== state.cat) return false;
      // Legislature meetings belong to everyone: they show statewide, and in a
      // county view when the "Idaho Legislature" filter is on.
      if (e.county === 'Statewide') return !state.county || state.cat === 'legislature';
      if (state.county && e.county !== state.county) return false;
      if (state.city && e.area !== 'countywide' && e.area !== state.city) return false;
      return true;
    });
  }

  function icsLink(e) {
    var p = parts(e.start);
    var stamp = function (q) { return '' + q.y + String(q.mo).padStart(2, '0') + String(q.d).padStart(2, '0'); };
    var esc = function (s) { return String(s || '').replace(/([\\;,])/g, '\\$1').replace(/\r\n?|\n/g, '\\n'); };
    var now = new Date().toISOString().replace(/[-:]/g, '').replace(/\.\d+/, '');
    var lines = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//CivicsID//EN', 'BEGIN:VEVENT', 'UID:' + e.id + '@civicsid', 'DTSTAMP:' + now];
    if (e.all_day) {
      lines.push('DTSTART;VALUE=DATE:' + stamp(p));
    } else {
      var t = function (q) { return stamp(q) + 'T' + String(q.h).padStart(2, '0') + String(q.mi).padStart(2, '0') + '00'; };
      var zone = e.tz === 'PT' ? 'America/Los_Angeles' : 'America/Boise';
      lines.push('DTSTART;TZID=' + zone + ':' + t(p));
      if (e.end) lines.push('DTEND;TZID=' + zone + ':' + t(parts(e.end)));
    }
    lines.push('SUMMARY:' + esc(e.title + ' (' + e.host + ')'), 'LOCATION:' + esc(e.location), 'URL:' + (safeUrl(e.url) || '').replace(/\s/g, ''), 'END:VEVENT', 'END:VCALENDAR');
    return 'data:text/calendar;charset=utf-8,' + encodeURIComponent(lines.join('\r\n'));
  }

  // Hosts often paste a raw web address into the note ("Register to Attend:
  // https://us02web.zoom.us/..."). Show it as a short link so it can't spill
  // across the card, and keep long notes to a couple of lines.
  function noteNode(note) {
    var p = el('p', 'note');
    var budget = 220;
    // Dial-in boilerplate ("Join by telephone: Dial ... +1 253 205 0468 or ...")
    // crowds out anything useful; the host's page has the call-in details.
    note = note.replace(/(join by (tele)?phone|dial)[^.]*?(\+?1?[ (]*\d{3}[ )-]*\d{3}[ -]?\d{4}[\s,or]*)+(\.\.\.|…)?/gi, '').replace(/^[.\s]+/, '').trim();
    if (!note) return p;
    note.split(/(https?:\/\/[^\s<>"']+)/).forEach(function (part) {
      if (!part) return;
      if (/^https?:\/\//.test(part)) {
        var url = part.replace(/[.,;:)\]]+$/, '');
        var host = '';
        try { host = new URL(url).hostname.replace(/^www\./, ''); } catch (err) { return; }
        var a = el('a', null, S.openLink + ' (' + host + ')');
        a.href = url;
        a.rel = 'noopener';
        p.appendChild(a);
        return;
      }
      if (budget <= 0) return;
      var text = part.length > budget ? part.slice(0, budget - 1) + '…' : part;
      budget -= text.length;
      p.appendChild(document.createTextNode(text));
    });
    return p;
  }

  // Meetings entered from a host's published regular schedule ("2nd and 4th
  // Mondays") rather than a posted meeting. They look lighter and say so.
  var REGULAR_NOTE = /^From the regular meeting schedule the host publishes\. Meetings can be cancelled or moved, so check the host's page before you go\.\s*/;

  function card(e) {
    var p = parts(e.start);
    var art = el('article', 'event' + (e.cancelled ? ' is-cancelled' : '') + (e.regular ? ' is-regular' : ''));
    var when = el('div', 'when', e.all_day ? (e.regular ? S.noTimeRegular : S.noTime) : clock(p));
    if (!e.all_day) when.appendChild(el('small', null, e.tz === 'PT' ? S.pacific : S.mountain));
    art.appendChild(when);

    var what = el('div', 'what');
    var tags = el('div', 'tags');
    tags.appendChild(el('span', 'tag' + (e.cancelled ? ' cancelled' : ''), e.cancelled ? S.cancelled : (LABELS[e.category] || S.other)));
    if (e.regular && !e.cancelled) tags.appendChild(el('span', 'tag regular', S.usually));
    what.appendChild(tags);
    what.appendChild(el('h3', null, e.title));
    what.appendChild(el('p', 'meta', e.host + (e.location ? ' · ' + e.location : '')));
    if (e.highlights && e.highlights.length) {
      var box = el('div', 'agenda');
      box.appendChild(el('p', 'agenda-label', S.onAgenda));
      var ul = el('ul');
      e.highlights.forEach(function (h) { ul.appendChild(el('li', null, h)); });
      if (e.highlights_more) ul.appendChild(el('li', 'more-items', S.more(e.highlights_more)));
      box.appendChild(ul);
      what.appendChild(box);
    }
    if (e.regular) {
      what.appendChild(el('p', 'note regular-note', safeUrl(e.agenda_url)
        ? S.regularPosted : S.regularNote));
      var extra = (e.note || '').replace(REGULAR_NOTE, '');
      if (extra) what.appendChild(noteNode(extra));
    } else if (e.note) what.appendChild(noteNode(e.note));
    art.appendChild(what);

    var actions = el('div', 'actions');
    var link = function (href, text, download) {
      var a = el('a', null, text);
      a.href = href;
      a.setAttribute('aria-label', text + ': ' + e.title + ', ' + dayLabel(p));
      if (download) a.download = download; else a.rel = 'noopener';
      actions.appendChild(a);
    };
    if (safeUrl(e.url)) link(safeUrl(e.url), S.details);
    if (safeUrl(e.agenda_url)) link(safeUrl(e.agenda_url), S.agenda);
    if (!e.cancelled) link(icsLink(e), S.addCal, 'civicsid-event.ics');
    // A prefilled email to BarNone, so clerks and residents can flag a change.
    var body = S.reportBody + '----\n' + e.title + '\n' + dayLabel(p) + (e.all_day ? '' : ', ' + clock(p)) + '\n' + (e.host || '') +
      '\nSource: ' + (e.source || '') + (safeUrl(e.url) ? '\n' + e.url : '');
    var rep = el('a', 'report', S.report);
    rep.href = 'mailto:admin@barnoneinc.org?subject=' + encodeURIComponent(S.reportSubject) + '&body=' + encodeURIComponent(body);
    rep.setAttribute('aria-label', S.report + ': ' + e.title + ', ' + dayLabel(p));
    actions.appendChild(rep);
    art.appendChild(actions);
    return art;
  }

  function render() {
    var list = $('list');
    list.textContent = '';
    // Within each day: meetings with a posted time first, in time order; then
    // posted meetings with no time; then ones from a regular schedule.
    var rank = function (e) { return e.regular ? 2 : e.all_day ? 1 : 0; };
    var rows = visible().sort(function (a, b) {
      var da = a.start.slice(0, 10), db = b.start.slice(0, 10);
      if (da !== db) return da < db ? -1 : 1;
      if (rank(a) !== rank(b)) return rank(a) - rank(b);
      return a.start < b.start ? -1 : a.start > b.start ? 1 : 0;
    });
    var from = todayKey(), to = addDays(from, state.days);
    var fmt = function (k) { return new Date(k + 'T12:00:00').toLocaleDateString(S.locale, { month: 'short', day: 'numeric' }); };
    $('range').textContent = state.q
      ? S.matches(rows.length, state.q)
      : S.range(fmt(from), fmt(to), rows.length);
    $('heading').textContent = S.heading(state.city, state.county);
    // One county is the useful subscription. With no county picked, offer the
    // Legislature, which matters to everyone.
    var sub = $('subscribe'), connected = state.county && (!state.connected || state.connected[state.county]);
    sub.href = BASE + 'data/ics/' + (connected ? slug(state.county) : 'statewide') + '.ics';
    sub.textContent = connected ? S.subCounty(state.county) : S.subLeg;
    if ($('feed')) $('feed').href = BASE + 'data/feeds/' + (connected ? slug(state.county) : 'statewide') + '.xml';
    $('subscribe-text').textContent = connected
      ? S.subCountyText(state.county) : S.subLegText;
    renderStatus();

    if (state.county && state.connected && !state.connected[state.county]) {
      list.appendChild(notConnected());
    } else if (!rows.length) {
      list.appendChild(el('p', 'empty', state.events.length
        ? S.noneType : S.noneLoaded));
      if (state.q && state.events.length) list.lastChild.textContent = S.noneSearch(state.q);
    }
    var lastDay = '';
    rows.forEach(function (e) {
      var p = parts(e.start);
      if (p.key !== lastDay) { list.appendChild(el('h3', 'day', dayLabel(p))); lastDay = p.key; }
      list.appendChild(card(e));
    });

    var lastKey = state.events.length ? state.events[state.events.length - 1].start.slice(0, 10) : from;
    $('more').hidden = !!state.q || to >= lastKey;
    Array.prototype.forEach.call($('chips').children, function (b) {
      b.setAttribute('aria-pressed', String(b.dataset.cat === state.cat));
    });
  }

  function setup() {
    CATEGORIES.forEach(function (c) {
      var b = el('button', 'chip', c.label);
      b.type = 'button';
      b.dataset.cat = c.id;
      b.addEventListener('click', function () { state.cat = c.id; render(); });
      $('chips').appendChild(b);
    });
    // Pressing Enter in the search box shouldn't reload the page.
    if ($('search')) $('search').addEventListener('submit', function (ev) { ev.preventDefault(); });
    $('more').addEventListener('click', function () { state.days += 14; render(); });
    var timer;
    $('q').value = state.q;
    $('q').addEventListener('input', function () {
      clearTimeout(timer);
      timer = setTimeout(function () {
        state.q = $('q').value.trim();
        try { history.replaceState(null, '', state.q ? '?q=' + encodeURIComponent(state.q) : location.pathname); } catch (e) {}
        render();
      }, 200);
    });
    $('county').addEventListener('change', function () {
      state.county = $('county').value; state.city = '';
      savePlace({ county: state.county }); fillCities(); render();
    });
    $('city').addEventListener('change', function () {
      state.city = $('city').value;
      savePlace({ county: state.county, city: state.city }); render();
    });
  }

  // Counties and cities come from the sources we read, so the lists only
  // offer places that have meetings here.
  function fillCounties() {
    var counties = {};
    state.sources.forEach(function (s) { if (s.county && s.county !== 'Statewide') counties[s.county] = true; });
    var all = Object.keys(state.local.counties || {});
    if (!all.length) all = Object.keys(counties);
    var sel = $('county');
    sel.textContent = '';
    sel.appendChild(new Option(S.allIdaho, ''));
    all.sort().forEach(function (c) {
      sel.appendChild(new Option(S.county(c) + (counties[c] ? '' : S.linksOnly), c, false, c === state.county));
    });
    if (all.indexOf(state.county) === -1) state.county = '';
    sel.value = state.county;
    state.connected = counties;
    $('coverage').textContent = S.coverage(Object.keys(counties).length);
  }

  // For a county whose calendar we can't read yet, point to its own page.
  function notConnected() {
    var c = state.county, info = (state.local.counties || {})[c] || {};
    var box = el('div', 'card notice-card');
    box.appendChild(el('h3', null, S.cantRead(c)));
    box.appendChild(el('p', null, S.cantReadText));
    var href = safeUrl(info.meetings || info.site);
    if (href) {
      var a = el('a', 'link', S.countyMeetings(c));
      a.href = href; a.rel = 'noopener';
      box.appendChild(a);
    }
    return box;
  }
  function fillCities() {
    var cities = {};
    state.events.forEach(function (e) { if (e.county === state.county && e.area !== 'countywide') cities[e.area] = true; });
    var sel = $('city');
    sel.textContent = '';
    sel.appendChild(new Option(state.county ? S.anywhere(state.county) : S.pickCounty, ''));
    Object.keys(cities).sort().forEach(function (c) { sel.appendChild(new Option(c, c, false, c === state.city)); });
    if (!cities[state.city]) state.city = '';
    sel.value = state.city;
    sel.disabled = !state.county;
  }

  function renderStatus() {
    var status = state.status;
    if (!status) return;
    var when = new Date(status.generated);
    if (!isNaN(when)) $('updated').textContent = S.refreshed + when.toLocaleDateString(S.locale, { month: 'long', day: 'numeric', year: 'numeric', timeZone: 'America/Boise' }) + '.';
  }

  var place = loadPlace();
  var wanted = (location.search.match(/[?&]cat=([a-z]+)/) || [])[1];
  if (wanted && CATEGORIES.some(function (c) { return c.id === wanted; })) state.cat = wanted;
  var asked = (location.search.match(/[?&]q=([^&]*)/) || [])[1];
  if (asked) { try { state.q = decodeURIComponent(asked.replace(/\+/g, ' ')).slice(0, 80); } catch (e) {} }
  state.county = place.county || '';
  state.city = place.city || '';
  setup();
  Promise.all([
    fetch(BASE + 'data/events.json').then(function (r) { return r.json(); }),
    fetch(BASE + 'data/status.json').then(function (r) { return r.json(); }).catch(function () { return { sources: [] }; }),
    fetch(BASE + 'data/local.json').then(function (r) { return r.json(); }).catch(function () { return {}; })
  ]).then(function (res) {
    state.local = res[2] || {};
    state.events = res[0].events || [];
    state.status = res[1];
    state.sources = res[1].sources || [];
    fillCounties();
    fillCities();
    render();
  }).catch(function () {
    $('list').textContent = '';
    $('list').appendChild(el('p', 'empty', S.loadFail));
  });
})();
