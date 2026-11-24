/* CivicsID "Near you" box. Any element with class "near-you" becomes a
   county and city picker that shows that place's own pages. The choice is
   remembered in this browser only (localStorage), and the address lookup
   on reps.html fills it in too. Data: data/local.json. Pages under /es/
   set <html lang="es">, and the box then speaks Spanish. */
(function () {
  'use strict';

  var KEY = 'civicsid.place';
  var STATE_BOARDS = 'https://gov.idaho.gov/appointments/';
  var SDE_DIRECTORY = 'https://www.sde.idaho.gov/school-districts/';
  var ES = document.documentElement.lang === 'es';
  // Place names (Ada, Boise) stay as they are; only our own wording changes.
  var T = ES ? {
    cityBoards: function (c) { return 'Juntas y comisiones de la ciudad de ' + c; },
    cityBoardsNote: 'Vacantes, solicitudes y qué hace cada junta.',
    city: function (c) { return 'Ciudad de ' + c; },
    cityNoBoards: 'La ciudad no tiene sus juntas en una sola página que podamos enlazar. Busque en las secciones del secretario municipal (City Clerk), del alcalde (Mayor) o de gobierno (Government), o pregunte al secretario por las vacantes.',
    countyBoards: function (c) { return 'Juntas y comités del condado de ' + c; },
    countyBoardsNote: 'Las juntas asesoras del condado y cómo solicitar un puesto.',
    countyCommissioners: function (c) { return 'Comisionados del condado de ' + c; },
    countyNoBoards: 'Este condado no tiene sus juntas en una sola página. Los tres comisionados hacen los nombramientos, así que pregunte en su oficina por las vacantes.',
    stateBoards: 'Juntas, comisiones y consejos estatales',
    stateBoardsNote: 'La página de nombramientos del Gobernador: la lista de juntas, las vacantes actuales y la solicitud (en inglés).',
    citySite: 'Sitio web oficial: alcalde y concejo, departamentos y solicitudes de servicio (en inglés).',
    county: function (c) { return 'Condado de ' + c; },
    countySite: 'Sitio web oficial: comisionados, secretario, departamentos y servicios (en inglés).',
    meetingsIn: function (c) { return 'Reuniones públicas en el condado de ' + c; },
    meetingsInNote: 'El calendario de CivicsID, con su condado seleccionado.',
    cityMeetings: function (c) { return 'Reuniones de la ciudad de ' + c; },
    cityMeetingsNote: 'Las agendas del concejo están en el sitio web de la ciudad (en inglés).',
    countyMeetings: function (c) { return 'Reuniones del condado de ' + c; },
    countyMeetingsNote: 'Las agendas de los comisionados están en el sitio web del condado (en inglés).',
    near: 'Cerca de usted', countyLabel: 'Condado', chooseCounty: 'Escoja su condado', countyName: function (c) { return 'Condado de ' + c; },
    cityLabel: 'Ciudad o pueblo', notSure: '¿No sabe en qué condado o ciudad está? ', lookUp: 'Busque su dirección',
    remember: '. Guardamos su selección solo en este dispositivo.',
    otherTown: 'Otro pueblo, o fuera de los límites de la ciudad', countyFirst: 'Primero escoja un condado',
    noCity: 'La mayoría de las ciudades y pueblos publican sus juntas en su propio sitio web, por lo general en la sección del ayuntamiento (City Hall) o de gobierno (Government). Si vive fuera de los límites de una ciudad, el condado es su gobierno local.',
    home: 'es/index.html', reps: 'es/reps.html',
    schoolsNote: 'Sitio web del distrito: reuniones de la junta escolar (trustees), agendas y elecciones (en inglés).',
    sdeDirectory: 'Directorio de distritos escolares de Idaho',
    sdeDirectoryNote: 'El Departamento de Educación del Estado (SDE) enumera todos los distritos (en inglés).',
    districtNotes: {
      port: 'Distrito portuario: comisionados electos. Reuniones y agendas (en inglés).',
      library: 'Biblioteca: reuniones y agendas de la junta directiva (en inglés).',
      utility: 'Servicio público: reuniones y agendas de la junta (en inglés).',
      transit: 'Agencia de transporte público: reuniones de la junta y cambios de servicio (en inglés).',
      hospital: 'Distrito hospitalario: reuniones y agendas de la junta (en inglés).',
      highway: 'Distrito de carreteras: comisionados electos que mantienen los caminos locales. Reuniones y agendas (en inglés).',
      fire: 'Distrito de bomberos: comisionados electos. Reuniones y agendas (en inglés).',
      other: 'Las reuniones y agendas de la junta están en su sitio web (en inglés).'
    }
  } : {
    cityBoards: function (c) { return 'City of ' + c + ' boards and commissions'; },
    cityBoardsNote: 'Openings, applications and what each board does.',
    city: function (c) { return 'City of ' + c; },
    cityNoBoards: 'The city does not list its boards on one page we could link. Look under City Clerk, Mayor or Government, or ask the clerk about openings.',
    countyBoards: function (c) { return c + ' County boards and committees'; },
    countyBoardsNote: 'County advisory boards and how to apply.',
    countyCommissioners: function (c) { return c + ' County commissioners'; },
    countyNoBoards: 'This county does not list its boards on one page. The three commissioners make the appointments, so ask their office about openings.',
    stateBoards: 'State boards, commissions and councils',
    stateBoardsNote: 'The Governor’s appointments page: the list of boards, current vacancies and the application.',
    citySite: 'Official website: mayor and council, departments and service requests.',
    county: function (c) { return c + ' County'; },
    countySite: 'Official website: commissioners, clerk, departments and services.',
    meetingsIn: function (c) { return 'Public meetings in ' + c + ' County'; },
    meetingsInNote: 'The CivicsID calendar, set to your county.',
    cityMeetings: function (c) { return 'City of ' + c + ' meetings'; },
    cityMeetingsNote: 'Council agendas are on the city’s website.',
    countyMeetings: function (c) { return c + ' County meetings'; },
    countyMeetingsNote: 'Commissioners’ agendas are on the county’s website.',
    near: 'Near you', countyLabel: 'County', chooseCounty: 'Choose your county', countyName: function (c) { return c + ' County'; },
    cityLabel: 'City or town', notSure: 'Not sure which county or city you’re in? ', lookUp: 'Look up your address',
    remember: '. We remember your choice on this device only.',
    otherTown: 'Another town, or outside city limits', countyFirst: 'Choose a county first',
    noCity: 'Most cities and towns post their boards on their own website, usually under City Hall or Government. If you live outside city limits, the county is your local government.',
    home: 'index.html', reps: 'reps.html',
    schoolsNote: 'District website: school board (trustee) meetings, agendas and elections.',
    sdeDirectory: 'Idaho school district directory',
    sdeDirectoryNote: 'The State Department of Education lists every district.',
    districtNotes: {
      port: 'Port district: elected commissioners. Meetings and agendas.',
      library: 'Library: board of trustees meetings and agendas.',
      utility: 'Public utility: board meetings and agendas.',
      transit: 'Transit agency: board meetings, agendas and service changes.',
      hospital: 'Hospital district: board meetings and agendas.',
      highway: 'Highway district: elected commissioners who maintain local roads. Meetings and agendas.',
      fire: 'Fire district: elected commissioners. Meetings and agendas.',
      other: 'Board meetings and agendas are on its website.'
    }
  };

  function base() {
    var s = document.querySelector('script[src$="local.js"]');
    return s ? s.getAttribute('src').replace(/local\.js$/, '') : '';
  }
  function load() {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; }
  }
  function save(place) {
    try { localStorage.setItem(KEY, JSON.stringify(place)); } catch (e) { /* private mode */ }
  }
  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function item(list, href, text, note) {
    var li = el('li');
    var a = el('a', null, text);
    a.href = href;
    a.rel = 'noopener';
    if (note) a.appendChild(el('span', null, note));
    li.appendChild(a);
    list.appendChild(li);
  }
  function option(select, value, text, selected) {
    var o = el('option', null, text);
    o.value = value;
    if (selected) o.selected = true;
    select.appendChild(o);
  }

  function links(data, show, place) {
    var ul = el('ul', 'guide-links near-links');
    var county = data.counties[place.county];
    var city = place.city && data.cities[place.city];
    show.forEach(function (kind) {
      if (kind === 'boards') {
        if (city && city.boards) item(ul, city.boards, T.cityBoards(place.city), T.cityBoardsNote);
        else if (city && city.site) item(ul, city.site, T.city(place.city), T.cityNoBoards);
        if (county && county.boards) item(ul, county.boards, T.countyBoards(place.county), T.countyBoardsNote);
        else if (county && (county.commissioners || county.site)) item(ul, county.commissioners || county.site, T.countyCommissioners(place.county), T.countyNoBoards);
        item(ul, STATE_BOARDS, T.stateBoards, T.stateBoardsNote);
      }
      if (kind === 'site') {
        if (city && city.site) item(ul, city.site, T.city(place.city), T.citySite);
        if (county && county.site) item(ul, county.site, T.county(place.county), T.countySite);
      }
      if (kind === 'schools') {
        ((county && county.schools) || []).forEach(function (d) { item(ul, d.site, d.name, T.schoolsNote); });
        item(ul, SDE_DIRECTORY, T.sdeDirectory, T.sdeDirectoryNote);
      }
      if (kind === 'districts') {
        ((county && county.districts) || []).forEach(function (d) { item(ul, d.site, d.name, T.districtNotes[d.kind] || T.districtNotes.other); });
      }
      if (kind === 'meetings') {
        if (place.county) item(ul, base() + T.home, T.meetingsIn(place.county), T.meetingsInNote);
        if (city && (city.meetings || city.site)) item(ul, city.meetings || city.site, T.cityMeetings(place.city), T.cityMeetingsNote);
        if (county && (county.meetings || county.site)) item(ul, county.meetings || county.site, T.countyMeetings(place.county), T.countyMeetingsNote);
      }
    });
    return ul;
  }

  function build(box, data) {
    var show = (box.getAttribute('data-show') || 'boards').split(',');
    var place = load();
    if (!data.counties[place.county]) place = {};

    box.textContent = '';
    box.appendChild(el('h2', null, box.getAttribute('data-title') || T.near));
    var form = el('div', 'near-pick');
    var cl = el('label', null, T.countyLabel);
    var cs = el('select');
    cs.id = 'near-county-' + Math.random().toString(36).slice(2, 7);
    cl.htmlFor = cs.id;
    option(cs, '', T.chooseCounty, !place.county);
    Object.keys(data.counties).sort().forEach(function (c) { option(cs, c, T.countyName(c), c === place.county); });
    var tl = el('label', null, T.cityLabel);
    var ts = el('select');
    ts.id = cs.id.replace('county', 'city');
    tl.htmlFor = ts.id;
    [cl, cs, tl, ts].forEach(function (n) { form.appendChild(n); });
    box.appendChild(form);
    var out = el('div', 'near-out');
    box.appendChild(out);
    var help = el('p', 'muted');
    help.appendChild(document.createTextNode(T.notSure));
    var a = el('a', null, T.lookUp);
    a.href = base() + T.reps;
    help.appendChild(a);
    help.appendChild(document.createTextNode(T.remember));
    box.appendChild(help);

    function fillCities() {
      ts.textContent = '';
      var names = Object.keys(data.cities).filter(function (n) { return data.cities[n].county === cs.value; }).sort();
      option(ts, '', cs.value ? T.otherTown : T.countyFirst, !place.city);
      names.forEach(function (n) { option(ts, n, n, n === place.city); });
      ts.disabled = !cs.value;
    }
    function draw() {
      out.textContent = '';
      if (!place.county) return;
      out.appendChild(links(data, show, place));
      if (!place.city && show.indexOf('boards') !== -1) {
        out.appendChild(el('p', 'muted', T.noCity));
      }
    }
    cs.addEventListener('change', function () { place = { county: cs.value }; save(place); fillCities(); draw(); });
    ts.addEventListener('change', function () { place = { county: cs.value, city: ts.value }; save(place); draw(); });
    fillCities();
    draw();
  }

  window.CivicsIDLocal = { save: save, load: load };
  var boxes = document.querySelectorAll('.near-you');
  if (!boxes.length) return;
  fetch(base() + 'data/local.json').then(function (r) { return r.json(); }).then(function (data) {
    Array.prototype.forEach.call(boxes, function (b) { build(b, data); });
  }).catch(function () {
    Array.prototype.forEach.call(boxes, function (b) { b.hidden = true; });
  });
})();
