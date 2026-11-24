/* CivicsID "Who represents you" lookup.
   The address goes straight from the visitor's browser to the U.S. Census
   Bureau geocoder, which returns the districts it sits in. CivicsID has no
   server, so it never receives or stores the address. Names come from
   data/officials.json, rebuilt nightly. */
(function () {
  'use strict';

  var GEOCODER = 'https://geocoding.geo.census.gov/geocoder/geographies/onelineaddress';
  var LEG_FINDER = 'https://legislature.idaho.gov/legislators/whosmylegislator/';

  // Local governments with a council or commission page we have checked.
  var LOCAL = {
    places: {
      Boise: { label: 'Boise public meetings', url: 'https://www.cityofboise.org/departments/city-clerk/public-meetings/', note: 'Council and commission meetings, agendas and how to take part' },
      Meridian: { label: 'Meridian public meetings', url: 'https://meridiancity.org/publicmeeting', note: 'How to watch and testify at council and planning meetings' }
    },
    counties: {
      Ada: { label: 'Ada County Board of Commissioners', url: 'https://adacounty.id.gov/commissioners/', note: 'Members, agendas and county boards' },
      Kootenai: { label: 'Kootenai County Board of County Commissioners', url: 'https://www.kcgov.us/487/Board-of-County-Commissioners', note: 'Members and meetings' }
    }
  };


  // English and Spanish wording. The page under /es/ sets <html lang="es">.
  // Names, phone numbers and districts come from the data and stay as they are.
  var LANG = document.documentElement.lang === 'es' ? 'es' : 'en';
  var BASE = LANG === 'es' ? '../' : '';
  var S = {
    en: {
      seat: 'Seat ', district: 'District ', website: 'Website', official: 'Official website', clerk: 'No city website: how to reach the city clerk',
      boards: 'Boards and committees', commissionersLink: 'Commissioners (they appoint board members)', meetings: 'Meetings and agendas',
      mayor: 'Mayor', source: 'Source', mayorPage: 'Mayor’s page', council: 'City council members',
      commissioners: 'County Commissioners', noCommissioners: 'No commissioners listed.',
      allThree: 'Every voter in the county elects all three commissioners. Each one must live in the district they represent.',
      otherOfficers: 'Other elected county officers', fromThe: 'From the ', blueBook: '2025–2026 Idaho Blue Book',
      blueBookNote: '. County officers elected in November 2026 take office in January 2027, so confirm with the county before you call.',
      elsewhere: function (s) { return 'That address is in ' + s + '. CivicsID only covers Idaho.'; },
      showing: function (a) { return 'Showing results for ' + a + '.'; },
      city: 'City', cityOf: function (c) { return 'City of ' + c; }, outside: 'Outside city limits',
      cityFallback: 'Your mayor and council members are listed on the city’s website. We have not added a direct link for this city yet.',
      unincorporated: 'This address is in an unincorporated area, so the county is your local government.',
      county: 'County', countyOf: function (c) { return c + ' County'; },
      countyFallback: 'Your three county commissioners are listed on the county’s website. We have not added a direct link for this county yet.',
      legislature: 'State Legislature', ld: function (n) { return 'Legislative District ' + n; }, noLd: 'Legislative district not found',
      senator: 'State Senator', noSenator: 'No senator listed.', reps: 'State Representatives', noReps: 'No representatives listed.',
      noRoster: 'We could not load the member list.',
      confirm: 'Every district has one senator and two representatives, in House seats A and B. Members elected in November take office December 1, and this list can lag by a few weeks. Confirm current members with the Legislature’s ',
      finder: 'Who’s My Legislator',
      congress: 'Congress', cd: function (n) { return 'Congressional District ' + n; }, noCd: 'Congressional district not found',
      usRep: 'U.S. Representative', noUsRep: 'No representative listed.', usSens: 'U.S. Senators', noUsSens: 'No senators listed.',
      tooShort: 'Enter a street address with a city or ZIP code, like 700 W Jefferson St, Boise.',
      looking: 'Looking up your districts…',
      notFound: 'We could not find that address. Check the spelling, include the city or ZIP code, and leave off apartment numbers.',
      down: 'The address lookup is not responding right now. You can use the Legislature’s ', downEnd: ' page instead.',
      party: {}, office: {},
      dEyebrow: 'Your districts', dTitle: 'Every district you live in',
      dCongress: 'U.S. House', dLeg: 'State Legislature', dLegNote: 'You elect one state senator and two state representatives from this district.',
      dSchool: 'School district', dSchoolNote: 'Elected trustees run your public schools.',
      dTribal: 'Tribal land', dTribalNote: 'This address is on tribal land. The tribe’s own government serves its members here.',
      dLooking: 'Looking up fire, ambulance, highway, library and other special districts…',
      dFailed: 'The special district lookup did not respond, so this list is missing fire, highway, library and other districts. Try again in a few minutes.',
      dSource: function (tca, c) { return 'Special districts come from the Idaho State Tax Commission’s taxing district maps' + (tca ? ' (tax code area ' + tca + (c ? ' in ' + c + ' County' : '') + ', the number on a property tax notice)' : '') + '. They show districts that levy a property tax.'; },
      dMissing: 'Not listed here: county commissioner districts, city council districts, voting precincts, highway district subdistricts, irrigation districts and soil and water conservation districts. Your county clerk can tell you those.'
    },
    es: {
      seat: 'Escaño ', district: 'Distrito ', website: 'Sitio web', official: 'Sitio web oficial', clerk: 'La ciudad no tiene sitio web: cómo comunicarse con el secretario municipal',
      boards: 'Juntas y comités', commissionersLink: 'Comisionados (nombran a los miembros de las juntas)', meetings: 'Reuniones y agendas',
      mayor: 'Alcalde o alcaldesa', source: 'Fuente', mayorPage: 'Página de la alcaldía', council: 'Miembros del concejo municipal',
      commissioners: 'Comisionados del condado', noCommissioners: 'No hay comisionados en la lista.',
      allThree: 'Todos los votantes del condado eligen a los tres comisionados. Cada uno debe vivir en el distrito que representa.',
      otherOfficers: 'Otros funcionarios electos del condado', fromThe: 'Según el ', blueBook: 'Idaho Blue Book 2025–2026 (en inglés)',
      blueBookNote: '. Los funcionarios del condado elegidos en noviembre de 2026 asumen el cargo en enero de 2027, así que confirme con el condado antes de llamar.',
      elsewhere: function (s) { return 'Esa dirección está en ' + s + '. CivicsID solo cubre Idaho.'; },
      showing: function (a) { return 'Resultados para ' + a + '.'; },
      city: 'Ciudad', cityOf: function (c) { return 'Ciudad de ' + c; }, outside: 'Fuera de los límites de la ciudad',
      cityFallback: 'Su alcalde o alcaldesa y los miembros del concejo aparecen en el sitio web de la ciudad. Todavía no hemos agregado un enlace directo para esta ciudad.',
      unincorporated: 'Esta dirección está en un área no incorporada, así que el condado es su gobierno local.',
      county: 'Condado', countyOf: function (c) { return 'Condado de ' + c; },
      countyFallback: 'Sus tres comisionados del condado aparecen en el sitio web del condado. Todavía no hemos agregado un enlace directo para este condado.',
      legislature: 'Legislatura estatal', ld: function (n) { return 'Distrito legislativo ' + n; }, noLd: 'No se encontró el distrito legislativo',
      senator: 'Senador o senadora estatal', noSenator: 'No hay senador en la lista.', reps: 'Representantes estatales', noReps: 'No hay representantes en la lista.',
      noRoster: 'No pudimos cargar la lista de miembros.',
      confirm: 'Cada distrito tiene un senador y dos representantes, en los escaños A y B de la Cámara. Los miembros elegidos en noviembre asumen el cargo el 1 de diciembre, y esta lista puede tardar unas semanas en actualizarse. Confirme los miembros actuales en la página de la Legislatura ',
      finder: 'Who’s My Legislator (en inglés)',
      congress: 'Congreso', cd: function (n) { return 'Distrito congresional ' + n; }, noCd: 'No se encontró el distrito congresional',
      usRep: 'Representante federal', noUsRep: 'No hay representante en la lista.', usSens: 'Senadores federales', noUsSens: 'No hay senadores en la lista.',
      tooShort: 'Escriba una dirección con la ciudad o el código postal, como 700 W Jefferson St, Boise.',
      looking: 'Buscando sus distritos…',
      notFound: 'No pudimos encontrar esa dirección. Revise la ortografía, incluya la ciudad o el código postal y omita el número de apartamento.',
      down: 'La búsqueda de direcciones no responde en este momento. Puede usar la página de la Legislatura ', downEnd: '.',
      party: { Republican: 'Partido Republicano', Democrat: 'Partido Demócrata', Independent: 'Independiente' },
      office: { Assessor: 'Tasador(a)', Clerk: 'Secretario(a) del condado', Coroner: 'Médico forense', Prosecutor: 'Fiscal', Sheriff: 'Sheriff', Treasurer: 'Tesorero(a)' },
      dEyebrow: 'Sus distritos', dTitle: 'Todos los distritos donde vive',
      dCongress: 'Cámara de Representantes federal', dLeg: 'Legislatura estatal', dLegNote: 'Usted elige a un senador estatal y a dos representantes estatales de este distrito.',
      dSchool: 'Distrito escolar', dSchoolNote: 'Fideicomisarios electos dirigen sus escuelas públicas.',
      dTribal: 'Tierra tribal', dTribalNote: 'Esta dirección está en tierra tribal. El gobierno de la tribu atiende a sus miembros aquí.',
      dLooking: 'Buscando distritos de bomberos, ambulancia, carreteras, bibliotecas y otros distritos especiales…',
      dFailed: 'La búsqueda de distritos especiales no respondió, así que faltan los distritos de bomberos, carreteras, bibliotecas y otros. Intente de nuevo en unos minutos.',
      dSource: function (tca, c) { return 'Los distritos especiales vienen de los mapas de distritos fiscales de la Comisión de Impuestos del Estado de Idaho' + (tca ? ' (área de código fiscal ' + tca + (c ? ' en el condado de ' + c : '') + ', el número que aparece en el aviso del impuesto a la propiedad)' : '') + '. Muestran los distritos que cobran un impuesto a la propiedad.'; },
      dMissing: 'No aparecen aquí: distritos de comisionados del condado, distritos del concejo municipal, precintos electorales, subdistritos de carreteras, distritos de riego y distritos de conservación de suelos y agua. La secretaría del condado puede indicárselos.'
    }
  }[LANG];

  var officials = null;
  var localData = null;
  var countyOfficials = null;
  var $ = function (id) { return document.getElementById(id); };

  function el(tag, cls, text) {
    var node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text != null) node.textContent = text;
    return node;
  }
  function safeUrl(url) { return /^https?:\/\//i.test(url || '') ? url : ''; }
  function link(href, text) {
    var a = el('a', null, text);
    a.href = href;
    a.rel = 'noopener';
    return a;
  }

  function geocode(address) {
    return new Promise(function (resolve, reject) {
      var name = '__civicsid_geo_' + Date.now();
      var script = document.createElement('script');
      var timer = setTimeout(function () { finish(); reject(new Error('timeout')); }, 20000);
      function finish() { clearTimeout(timer); delete window[name]; script.remove(); }
      window[name] = function (data) { finish(); resolve(data); };
      script.onerror = function () { finish(); reject(new Error('network')); };
      script.src = GEOCODER + '?address=' + encodeURIComponent(address) +
        '&benchmark=Public_AR_Current&vintage=Current_Current&layers=all&format=jsonp&callback=' + name;
      document.head.appendChild(script);
    });
  }

  // Layer names carry a year or Congress number ("2026 State Legislative
  // Districts - Upper"), so match on the stable part of the name.
  function layer(geographies, pattern) {
    var key = Object.keys(geographies).filter(function (k) { return pattern.test(k); })[0];
    var rows = key ? geographies[key] : null;
    return rows && rows[0] ? rows[0].BASENAME : '';
  }

  function names(geographies, pattern) {
    var out = [];
    Object.keys(geographies).filter(function (k) { return pattern.test(k); }).forEach(function (k) {
      (geographies[k] || []).forEach(function (row) {
        if (row.NAME && out.indexOf(row.NAME) < 0) out.push(row.NAME);
      });
    });
    return out;
  }

  function districtItem(list, d) {
    var li = el('li', 'district');
    li.appendChild(el('strong', null, d.label + ': '));
    li.appendChild(document.createTextNode(d.name));
    if (d.note) li.appendChild(el('span', 'muted', d.note));
    list.appendChild(li);
  }

  // One card listing every district the address sits in. The districts the
  // Census lookup already named show right away; special districts come from
  // the Idaho State Tax Commission's map service, which gets only the map point.
  function districtsCard(g, match, parts) {
    var card = section(S.dEyebrow, S.dTitle);
    var list = el('ul', 'districts');
    card.appendChild(list);
    var add = function (d) { districtItem(list, d); };
    if (parts.cd) add({ label: S.dCongress, name: S.cd(parts.cd) });
    if (parts.ld) add({ label: S.dLeg, name: S.ld(parts.ld), note: S.dLegNote });
    if (parts.county) add({ label: S.county, name: S.countyOf(parts.county) });
    add({ label: S.city, name: parts.city ? S.cityOf(parts.city) : S.outside });
    names(g, /School Districts/).forEach(function (n) {
      add({ label: S.dSchool, name: n, note: S.dSchoolNote });
    });
    names(g, /American Indian Reservations|Off-Reservation Trust Lands/).forEach(function (n) {
      add({ label: S.dTribal, name: n, note: S.dTribalNote });
    });

    var status = el('p', 'muted', S.dLooking);
    card.appendChild(status);
    var D = window.CivicsIDDistricts;
    var c = match.coordinates || {};
    if (!D || typeof c.x !== 'number' || typeof c.y !== 'number') {
      status.textContent = S.dFailed;
      return card;
    }
    D.lookup(c.x, c.y, parts.county, LANG).then(function (r) {
      if (!r) { status.textContent = S.dFailed; return; }
      r.districts.forEach(add);
      status.textContent = S.dSource(r.taxCodeArea, parts.county);
      card.appendChild(el('p', 'muted', S.dMissing));
    });
    return card;
  }

  function person(p) {
    var li = el('li', 'person');
    li.appendChild(el('strong', null, p.name));
    if (p.seat) li.appendChild(el('span', 'muted', ' · ' + S.seat + p.seat));
    if (p.party) li.appendChild(el('span', 'muted', ' · ' + (S.party[p.party] || p.party)));
    var contact = el('div', 'contact');
    if (p.phone) contact.appendChild(link('tel:' + p.phone.replace(/[^\d+]/g, ''), p.phone));
    if (p.email) contact.appendChild(link('mailto:' + p.email, p.email));
    if (safeUrl(p.url)) contact.appendChild(link(p.url, S.website));
    if (contact.children.length) li.appendChild(contact);
    return li;
  }

  function section(title, subtitle) {
    var card = el('section', 'card');
    card.appendChild(el('span', 'eyebrow', title));
    if (subtitle) card.appendChild(el('h3', null, subtitle));
    return card;
  }

  function people(card, list, emptyText) {
    if (list && list.length) {
      var ul = el('ul', 'people');
      list.forEach(function (p) { ul.appendChild(person(p)); });
      card.appendChild(ul);
    } else {
      card.appendChild(el('p', 'muted', emptyText));
    }
  }

  // Official website and boards page for counties and the larger cities,
  // from data/local.json (the same list the Engage guides' "Near you" boxes use).
  function extraLinks(card, place) {
    if (!place) return;
    var p = el('p');
    if (safeUrl(place.site)) p.appendChild(link(place.site, S.official));
    else if (safeUrl(place.clerk)) p.appendChild(link(place.clerk, S.clerk));
    var second = place.boards ? [place.boards, S.boards]
      : place.commissioners ? [place.commissioners, S.commissionersLink]
      : place.meetings ? [place.meetings, S.meetings] : null;
    if (second && safeUrl(second[0])) {
      if (p.childNodes.length) p.appendChild(document.createTextNode(' · '));
      p.appendChild(link(second[0], second[1]));
    }
    if (p.childNodes.length) card.appendChild(p);
  }

  // Mayors confirmed on each city's own website (data/local.json), with a
  // link to the council members page where we found one.
  function addMayor(card, place) {
    if (!place || !place.mayor) return;
    card.appendChild(el('h4', null, S.mayor));
    people(card, [{ name: place.mayor.name, url: place.mayor.source }], '');
    var links = card.querySelector('ul.people:last-of-type .contact a');
    if (links) links.textContent = /eastidahonews|kivitv|news/i.test(place.mayor.source) ? S.source : S.mayorPage;
    if (place.mayor.note) card.appendChild(el('p', 'muted', place.mayor.note));
    if (safeUrl(place.council)) {
      var p = el('p');
      p.appendChild(link(place.council, S.council));
      card.appendChild(p);
    }
  }

  function localCard(kind, name, entry, fallback, place) {
    var card = section(kind === 'city' ? S.city : S.county, name);
    if (kind === 'city') addMayor(card, place);
    if (!entry && place) { extraLinks(card, place); return card; }
    if (entry) {
      var p = el('p');
      p.appendChild(link(entry.url, entry.label));
      p.appendChild(document.createTextNode(': ' + entry.note + '.'));
      card.appendChild(p);
    } else {
      card.appendChild(el('p', 'muted', fallback));
    }
    extraLinks(card, place);
    return card;
  }

  // County commissioners and officers, from the Idaho Blue Book
  // (data/county_officials.json). Every county voter elects all three
  // commissioners; each one must live in the district they run for.
  function addCountyOfficials(card, county) {
    var c = countyOfficials && countyOfficials.counties && countyOfficials.counties[county];
    if (!c) return;
    card.appendChild(el('h4', null, S.commissioners));
    people(card, c.commissioners.map(function (o) {
      return { name: o.name, seat: null, party: o.party, phone: o.phone, district: o.district };
    }), S.noCommissioners);
    var items = card.querySelectorAll('ul.people li.person');
    c.commissioners.forEach(function (o, i) {
      if (items[i]) items[i].insertBefore(el('span', 'muted', ' · ' + S.district + o.district), items[i].children[1] || null);
    });
    card.appendChild(el('p', 'muted', S.allThree));
    var more = el('details', 'more-officials');
    more.appendChild(el('summary', null, S.otherOfficers));
    var ul = el('ul', 'people');
    c.officers.forEach(function (o) {
      var li = person({ name: o.name, party: o.party, phone: o.phone });
      li.insertBefore(el('span', 'office', (S.office[o.office] || o.office) + ': '), li.firstChild);
      ul.appendChild(li);
    });
    more.appendChild(ul);
    card.appendChild(more);
    var src = el('p', 'muted small-print');
    src.appendChild(document.createTextNode(S.fromThe));
    src.appendChild(link(countyOfficials.source_url, S.blueBook));
    src.appendChild(document.createTextNode(S.blueBookNote));
    card.appendChild(src);
  }

  function render(match) {
    var g = match.geographies;
    var out = $('results');
    out.textContent = '';

    var state = layer(g, /^States$/);
    if (state && state !== 'Idaho') {
      out.appendChild(el('p', 'empty', S.elsewhere(state)));
      return;
    }

    var city = layer(g, /Incorporated Places/);
    if (city === 'Boise City') city = 'Boise';  // the Census Bureau's formal name for Boise
    var county = layer(g, /^Counties$/);
    var ld = layer(g, /State Legislative Districts - Upper/);
    var cd = layer(g, /Congressional Districts/);

    out.appendChild(el('p', 'muted', S.showing(match.matchedAddress)));
    out.appendChild(districtsCard(g, match, { city: city, county: county, ld: ld, cd: cd }));
    if (window.CivicsIDLocal && county) {
      // Remember only the county and city, so the Engage guides can show local links.
      window.CivicsIDLocal.save({ county: county, city: localData && localData.cities[city] ? city : '' });
    }

    out.appendChild(city
      ? localCard('city', S.cityOf(city), LANG === 'en' ? LOCAL.places[city] : null, S.cityFallback, localData && localData.cities[city])
      : localCard('city', S.outside, null, S.unincorporated));

    if (county) {
      var cc = localCard('county', S.countyOf(county), LANG === 'en' ? LOCAL.counties[county] : null, S.countyFallback, localData && localData.counties[county]);
      addCountyOfficials(cc, county);
      out.appendChild(cc);
    }

    var seats = (officials && officials.legislators && officials.legislators[ld]) || null;
    var leg = section(S.legislature, ld ? S.ld(ld) : S.noLd);
    if (seats) {
      leg.appendChild(el('h4', null, S.senator));
      people(leg, seats.senate, S.noSenator);
      leg.appendChild(el('h4', null, S.reps));
      people(leg, seats.house, S.noReps);
    } else {
      leg.appendChild(el('p', 'muted', S.noRoster));
    }
    var confirm = el('p', 'muted');
    confirm.appendChild(document.createTextNode(S.confirm));
    confirm.appendChild(link(LEG_FINDER, S.finder));
    confirm.appendChild(document.createTextNode('.'));
    leg.appendChild(confirm);
    out.appendChild(leg);

    var congress = (officials && officials.congress) || { senators: [], house: {} };
    var fed = section(S.congress, cd ? S.cd(cd) : S.noCd);
    fed.appendChild(el('h4', null, S.usRep));
    people(fed, congress.house[cd] ? [congress.house[cd]] : [], S.noUsRep);
    fed.appendChild(el('h4', null, S.usSens));
    people(fed, congress.senators, S.noUsSens);
    out.appendChild(fed);
  }

  $('lookup').addEventListener('submit', function (ev) {
    ev.preventDefault();
    var address = $('address').value.trim();
    var out = $('results');
    out.textContent = '';
    if (address.length < 6) {
      out.appendChild(el('p', 'empty', S.tooShort));
      return;
    }
    out.appendChild(el('p', 'empty', S.looking));
    geocode(/\bid\b|idaho/i.test(address) ? address : address + ', ID').then(function (data) {
      var matches = data && data.result && data.result.addressMatches;
      if (!matches || !matches.length) {
        out.textContent = '';
        out.appendChild(el('p', 'empty', S.notFound));
        return;
      }
      render(matches[0]);
    }).catch(function () {
      out.textContent = '';
      var p = el('p', 'empty');
      p.appendChild(document.createTextNode(S.down));
      p.appendChild(link(LEG_FINDER, S.finder));
      p.appendChild(document.createTextNode(S.downEnd));
      out.appendChild(p);
    });
  });

  fetch(BASE + 'data/local.json').then(function (r) { return r.json(); }).then(function (d) { localData = d; }).catch(function () {});
  fetch(BASE + 'data/county_officials.json').then(function (r) { return r.json(); }).then(function (d) { countyOfficials = d; }).catch(function () {});
  fetch(BASE + 'data/officials.json').then(function (r) { return r.json(); }).then(function (d) { officials = d; }).catch(function () {});
})();
