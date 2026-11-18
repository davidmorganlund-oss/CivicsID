/* CivicsID: the Idaho Legislature's committee meetings, day by day.
   Reads data/events.json (the Legislature's meetings are county "Statewide"). */
(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  function el(tag, cls, text) { var n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; }
  function safeUrl(u) { return /^https?:\/\//i.test(u || '') ? u : ''; }
  function parts(iso) { var m = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})/.exec(iso); return { y: +m[1], mo: +m[2], d: +m[3], h: +m[4], mi: +m[5], key: m[1] + '-' + m[2] + '-' + m[3] }; }
  function clock(p) { var h = p.h % 12 || 12; return h + (p.mi ? ':' + String(p.mi).padStart(2, '0') : '') + (p.h < 12 ? ' AM' : ' PM'); }
  function dayLabel(p) { return new Date(p.y, p.mo - 1, p.d).toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' }); }
  var today = new Date().toLocaleDateString('en-CA', { timeZone: 'America/Boise' }).slice(0, 10);

  function card(e) {
    var p = parts(e.start);
    var art = el('article', 'event' + (e.cancelled ? ' is-cancelled' : ''));
    var when = el('div', 'when', e.all_day ? 'Time not listed' : clock(p));
    if (!e.all_day) when.appendChild(el('small', null, 'Mountain'));
    art.appendChild(when);
    var what = el('div', 'what');
    if (e.cancelled) what.appendChild(el('span', 'tag cancelled', 'Cancelled'));
    what.appendChild(el('h3', null, e.title));
    if (e.location) what.appendChild(el('p', 'meta', e.location));
    if (e.highlights && e.highlights.length) {
      var box = el('div', 'agenda');
      box.appendChild(el('p', 'agenda-label', 'On the agenda'));
      var ul = el('ul');
      e.highlights.forEach(function (h) { ul.appendChild(el('li', null, h)); });
      if (e.highlights_more) ul.appendChild(el('li', 'more-items', 'and ' + e.highlights_more + ' more'));
      box.appendChild(ul);
      what.appendChild(box);
    } else if (!safeUrl(e.agenda_url)) {
      what.appendChild(el('p', 'note regular-note', 'No agenda posted yet. Committees usually post agendas a few days ahead.'));
    }
    art.appendChild(what);
    var actions = el('div', 'actions');
    var add = function (href, text) { var a = el('a', null, text); a.href = href; a.rel = 'noopener'; a.setAttribute('aria-label', text + ': ' + e.title + ', ' + dayLabel(p)); actions.appendChild(a); };
    if (safeUrl(e.agenda_url)) add(e.agenda_url, 'Agenda');
    if (safeUrl(e.url) && /sessioninfo|committees/.test(e.url)) add(e.url, 'Committee page and testimony sign-up');
    else if (safeUrl(e.url)) add(e.url, 'Details');
    var rep = el('a', 'report', 'Report a problem');
    rep.href = 'mailto:admin@barnoneinc.org?subject=' + encodeURIComponent('CivicsID: problem with a Legislature listing') +
      '&body=' + encodeURIComponent('What looks wrong?\n\n\n----\n' + e.title + '\n' + dayLabel(p) + (e.all_day ? '' : ', ' + clock(p)));
    actions.appendChild(rep);
    art.appendChild(actions);
    return art;
  }

  fetch('data/events.json').then(function (r) { return r.json(); }).then(function (d) {
    var rows = (d.events || []).filter(function (e) { return e.county === 'Statewide' && e.start.slice(0, 10) >= today; })
      .sort(function (a, b) { return a.start < b.start ? -1 : 1; });
    var list = $('leg-list');
    list.textContent = '';
    $('leg-range').textContent = rows.length + (rows.length === 1 ? ' meeting' : ' meetings') + ' on the calendar';
    if (today >= '2027-01-11') $('session-note').textContent = 'The 2027 session is underway. Standing committees meet most weekday mornings; check each agenda for the bills being heard.';
    if (!rows.length) { list.appendChild(el('p', 'empty', 'No committee meetings are on the Legislature’s calendar right now.')); return; }
    var last = '';
    rows.forEach(function (e) {
      var p = parts(e.start);
      if (p.key !== last) { list.appendChild(el('h3', 'day', dayLabel(p))); last = p.key; }
      list.appendChild(card(e));
    });
  }).catch(function () {
    $('leg-list').textContent = '';
    $('leg-list').appendChild(el('p', 'empty', 'The hearings could not be loaded. Please try again later.'));
  });
})();
