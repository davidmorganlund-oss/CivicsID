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

  var officials = null;
  var localData = null;
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

  function person(p) {
    var li = el('li', 'person');
    li.appendChild(el('strong', null, p.name));
    if (p.seat) li.appendChild(el('span', 'muted', ' · Seat ' + p.seat));
    if (p.party) li.appendChild(el('span', 'muted', ' · ' + p.party));
    var contact = el('div', 'contact');
    if (p.phone) contact.appendChild(link('tel:' + p.phone.replace(/[^\d+]/g, ''), p.phone));
    if (p.email) contact.appendChild(link('mailto:' + p.email, p.email));
    if (safeUrl(p.url)) contact.appendChild(link(p.url, 'Website'));
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
    if (safeUrl(place.site)) p.appendChild(link(place.site, 'Official website'));
    var second = place.boards ? [place.boards, 'Boards and committees']
      : place.commissioners ? [place.commissioners, 'Commissioners (they appoint board members)']
      : place.meetings ? [place.meetings, 'Meetings and agendas'] : null;
    if (second && safeUrl(second[0])) {
      if (p.childNodes.length) p.appendChild(document.createTextNode(' · '));
      p.appendChild(link(second[0], second[1]));
    }
    if (p.childNodes.length) card.appendChild(p);
  }

  function localCard(title, name, entry, fallback, place) {
    var card = section(title, name);
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

  function render(match) {
    var g = match.geographies;
    var out = $('results');
    out.textContent = '';

    var state = layer(g, /^States$/);
    if (state && state !== 'Idaho') {
      out.appendChild(el('p', 'empty', 'That address is in ' + state + '. CivicsID only covers Idaho.'));
      return;
    }

    var city = layer(g, /Incorporated Places/);
    if (city === 'Boise City') city = 'Boise';  // the Census Bureau's formal name for Boise
    var county = layer(g, /^Counties$/);
    var ld = layer(g, /State Legislative Districts - Upper/);
    var cd = layer(g, /Congressional Districts/);

    out.appendChild(el('p', 'muted', 'Showing results for ' + match.matchedAddress + '.'));
    if (window.CivicsIDLocal && county) {
      // Remember only the county and city, so the Engage guides can show local links.
      window.CivicsIDLocal.save({ county: county, city: localData && localData.cities[city] ? city : '' });
    }

    out.appendChild(city
      ? localCard('City', 'City of ' + city, LOCAL.places[city], 'Your mayor and council members are listed on the city’s website. We have not added a direct link for this city yet.', localData && localData.cities[city])
      : localCard('City', 'Outside city limits', null, 'This address is in an unincorporated area, so the county is your local government.'));

    if (county) {
      out.appendChild(localCard('County', county + ' County', LOCAL.counties[county], 'Your three county commissioners are listed on the county’s website. We have not added a direct link for this county yet.', localData && localData.counties[county]));
    }

    var seats = (officials && officials.legislators && officials.legislators[ld]) || null;
    var leg = section('State Legislature', ld ? 'Legislative District ' + ld : 'Legislative district not found');
    if (seats) {
      leg.appendChild(el('h4', null, 'State Senator'));
      people(leg, seats.senate, 'No senator listed.');
      leg.appendChild(el('h4', null, 'State Representatives'));
      people(leg, seats.house, 'No representatives listed.');
    } else {
      leg.appendChild(el('p', 'muted', 'We could not load the member list.'));
    }
    var confirm = el('p', 'muted');
    confirm.appendChild(document.createTextNode('Every district has one senator and two representatives, in House seats A and B. Members elected in November take office December 1, and this list can lag by a few weeks. Confirm current members with the Legislature’s '));
    confirm.appendChild(link(LEG_FINDER, 'Who’s My Legislator'));
    confirm.appendChild(document.createTextNode('.'));
    leg.appendChild(confirm);
    out.appendChild(leg);

    var congress = (officials && officials.congress) || { senators: [], house: {} };
    var fed = section('Congress', cd ? 'Congressional District ' + cd : 'Congressional district not found');
    fed.appendChild(el('h4', null, 'U.S. Representative'));
    people(fed, congress.house[cd] ? [congress.house[cd]] : [], 'No representative listed.');
    fed.appendChild(el('h4', null, 'U.S. Senators'));
    people(fed, congress.senators, 'No senators listed.');
    out.appendChild(fed);
  }

  $('lookup').addEventListener('submit', function (ev) {
    ev.preventDefault();
    var address = $('address').value.trim();
    var out = $('results');
    out.textContent = '';
    if (address.length < 6) {
      out.appendChild(el('p', 'empty', 'Enter a street address with a city or ZIP code, like 700 W Jefferson St, Boise.'));
      return;
    }
    out.appendChild(el('p', 'empty', 'Looking up your districts…'));
    geocode(/\bid\b|idaho/i.test(address) ? address : address + ', ID').then(function (data) {
      var matches = data && data.result && data.result.addressMatches;
      if (!matches || !matches.length) {
        out.textContent = '';
        out.appendChild(el('p', 'empty', 'We could not find that address. Check the spelling, include the city or ZIP code, and leave off apartment numbers.'));
        return;
      }
      render(matches[0]);
    }).catch(function () {
      out.textContent = '';
      var p = el('p', 'empty');
      p.appendChild(document.createTextNode('The address lookup is not responding right now. You can use the Legislature’s '));
      p.appendChild(link(LEG_FINDER, 'Who’s My Legislator'));
      p.appendChild(document.createTextNode(' page instead.'));
      out.appendChild(p);
    });
  });

  fetch('data/local.json').then(function (r) { return r.json(); }).then(function (d) { localData = d; }).catch(function () {});
  fetch('data/officials.json').then(function (r) { return r.json(); }).then(function (d) { officials = d; }).catch(function () {});
})();
