/* CivicsID special-district lookup.
   Takes the map point the Census Bureau returned for an address and asks the
   Idaho State Tax Commission's public taxing district map which districts
   that point falls in: fire, ambulance, highway, library, cemetery, water,
   sewer, recreation, community college and other districts.
   Only the map coordinates are sent, never the address, and nothing is kept.
   The service answers JSONP, so this works from a static site with no key. */
(function (root) {
  'use strict';

  var SERVICE = 'https://services.arcgis.com/91hXl6NfvLGEi8x5/ArcGIS/rest/services/Idaho_City_Taxing_Districts/FeatureServer/query';

  // Layer ids in the Tax Commission's service, in the order we list them.
  // Left out on purpose: annexations (0), bond layers (4, 8, 15, 22),
  // cities (6), counties (7) and school districts (23), which the Census
  // lookup already names, and urban renewal areas (27), which aren't
  // governments you live under.
  var TYPES = {
    9:  { en: ['Fire', 'Fire and emergency response, run by elected fire commissioners.'],
          es: ['Bomberos', 'Bomberos y respuesta a emergencias, a cargo de comisionados electos.'] },
    2:  { en: ['Ambulance', 'Ambulance and paramedic service, paid for by a property tax here.'],
          es: ['Ambulancia', 'Servicio de ambulancia y paramédicos, pagado con un impuesto a la propiedad.'] },
    11: { en: ['Roads', 'Builds and maintains local roads, run by elected highway commissioners.'],
          es: ['Carreteras', 'Construye y mantiene las carreteras locales, a cargo de comisionados electos.'] },
    12: { en: ['Hospital', 'A public hospital district with its own board.'],
          es: ['Hospital', 'Un distrito hospitalario público con su propia junta.'] },
    17: { en: ['Library', 'Run by elected library trustees.'],
          es: ['Biblioteca', 'A cargo de una junta directiva electa (trustees).'] },
    14: { en: ['Community college', 'Elected trustees run the college. Residents here pay in-district tuition.'],
          es: ['Colegio comunitario', 'Una junta directiva electa (trustees) dirige el colegio. Los residentes de aquí pagan la matrícula reducida para residentes del distrito.'] },
    21: { en: ['Recreation', 'Runs local parks, pools or recreation programs.'],
          es: ['Recreación', 'Administra parques, piscinas o programas recreativos locales.'] },
    28: { en: ['Water', 'Runs local water service.'],
          es: ['Agua', 'Administra el servicio local de agua.'] },
    24: { en: ['Sewer', 'Runs local sewer service.'],
          es: ['Alcantarillado', 'Administra el servicio local de alcantarillado.'] },
    26: { en: ['Water and sewer', 'Runs local water and sewer service.'],
          es: ['Agua y alcantarillado', 'Administra el servicio local de agua y alcantarillado.'] },
    25: { en: ['Trash', 'Pays for garbage collection or the local landfill.'],
          es: ['Basura', 'Paga la recolección de basura o el vertedero local.'] },
    5:  { en: ['Cemetery', 'Looks after local cemeteries.'],
          es: ['Cementerio', 'Cuida los cementerios locales.'] },
    10: { en: ['Flood control', 'Pays for flood protection and drainage.'],
          es: ['Control de inundaciones', 'Paga la protección contra inundaciones y el drenaje.'] },
    16: { en: ['Levee', 'Maintains levees along a river.'],
          es: ['Diques', 'Mantiene los diques a lo largo de un río.'] },
    30: { en: ['Watershed', 'Works on erosion and water quality in a watershed.'],
          es: ['Cuenca', 'Trabaja en la erosión y la calidad del agua de una cuenca.'] },
    18: { en: ['Mosquito control', 'Sprays and traps to keep mosquitoes down.'],
          es: ['Control de mosquitos', 'Fumiga y pone trampas para controlar los mosquitos.'] },
    19: { en: ['Pest control', 'Controls crop and range pests.'],
          es: ['Control de plagas', 'Controla las plagas de cultivos y pastizales.'] },
    29: { en: ['Weed control', 'Controls noxious weeds.'],
          es: ['Control de malezas', 'Controla las malezas nocivas.'] },
    3:  { en: ['Convention center', 'An elected board runs a convention or events center, paid for by a tax on hotel stays.'],
          es: ['Centro de convenciones', 'Una junta electa administra un centro de convenciones, pagado con un impuesto a las estadías en hoteles.'] },
    20: { en: ['Port', 'Elected port commissioners oversee port facilities and economic development.'],
          es: ['Puerto', 'Comisionados electos supervisan las instalaciones portuarias y el desarrollo económico.'] },
    13: { en: ['Community infrastructure', 'Pays for roads, water lines and other public works in a new development, through a levy on property there.'],
          es: ['Infraestructura comunitaria', 'Paga calles, tuberías y otras obras públicas en un desarrollo nuevo, con un impuesto a esas propiedades.'] },
    31: { en: ['Weather modification', 'Pays for cloud seeding to add to the snowpack.'],
          es: ['Modificación del clima', 'Paga la siembra de nubes para aumentar la nieve acumulada.'] }
  };
  var ORDER = [9, 2, 11, 12, 17, 14, 21, 28, 24, 26, 25, 5, 10, 16, 30, 18, 19, 29, 3, 20, 13, 31];
  var TCA_LAYER = 1;

  // Short forms the Tax Commission uses in district names.
  var WORDS = {
    Cnty: 'County', Co: 'County', Svc: 'Service', Svcs: 'Services', Cem: 'Cemetery', Dist: 'District', Distr: 'District',
    Distri: 'District', Abate: 'Abatement', Abatemt: 'Abatement', Hwy: 'Highway', Rec: 'Recreation', Amb: 'Ambulance',
    Mosq: 'Mosquito', Wtr: 'Water', Swr: 'Sewer', Lib: 'Library', Ems: 'EMS', Fpd: 'Fire Protection District',
    Sw: 'Southwest', Se: 'Southeast', Nw: 'Northwest', Ne: 'Northeast', Mtn: 'Mountain', Jr: 'Junior', Twp: 'Township',
    Of: 'of', And: 'and', The: 'the'
  };

  // "SW ADA CO MOSQUITO ABATE" -> "Southwest Ada County Mosquito Abatement District",
  // "FLOOD CONTROL #10" -> "Flood Control District No. 10",
  // "COUNTY WIDE HIGHWAY" in Ada County -> "Ada County Highway District".
  function prettyName(raw, county) {
    var s = String(raw || '').replace(/\s+/g, ' ').trim();
    if (!s) return '';
    var num = '';
    s = s.replace(/\s*#\s*(\d+)\s*/, function (m, n) { num = n; return ' '; }).trim();
    // "HIGHWAY #4 (WORLEY)": the place in parentheses goes first.
    s = s.replace(/^(.*?)\s*\(([^)]+)\)\s*(.*)$/, '$2 $1 $3').trim();
    s = s.toLowerCase().replace(/[a-z]+/g, function (w) {
      var t = w.charAt(0).toUpperCase() + w.slice(1);
      return WORDS.hasOwnProperty(t) ? WORDS[t] : t;
    });
    s = s.replace(/\bMc([a-z])/g, function (m, c) { return 'Mc' + c.toUpperCase(); });
    s = s.charAt(0).toUpperCase() + s.slice(1);
    if (county) s = s.replace(/^County ?Wide\b/i, county + ' County');
    if (!/\b(District|College|Authority)\b/.test(s)) s += ' District';
    if (num) s += ' No. ' + num;
    return s.replace(/\s{2,}/g, ' ');
  }

  function jsonp(url, timeoutMs) {
    return new Promise(function (resolve, reject) {
      var name = '__civicsid_d' + Date.now() + Math.floor(Math.random() * 1e6);
      var script = document.createElement('script');
      var timer = setTimeout(function () { finish(); reject(new Error('timeout')); }, timeoutMs || 15000);
      function finish() { clearTimeout(timer); delete root[name]; script.remove(); }
      root[name] = function (data) { finish(); resolve(data); };
      script.onerror = function () { finish(); reject(new Error('network')); };
      script.src = url + (url.indexOf('?') < 0 ? '?' : '&') + 'callback=' + name;
      document.head.appendChild(script);
    });
  }

  // Turn the service's multi-layer answer into a list of districts.
  function fromTax(response, county, lang) {
    var out = [];
    var tca = '';
    var seen = {};
    if (!response || !response.layers) throw new Error('bad response');
    response.layers.forEach(function (layer) {
      (layer.features || []).forEach(function (f) {
        var a = f.attributes || {};
        if (layer.id === TCA_LAYER) { if (a.TCA) tca = String(a.TCA).trim(); return; }
        var t = TYPES[layer.id];
        var name = t && prettyName(a.NAME, county);
        if (!name || seen[name]) return;
        seen[name] = true;
        var words = t[lang === 'es' ? 'es' : 'en'];
        out.push({ layer: layer.id, label: words[0], name: name, note: words[1] });
      });
    });
    out.sort(function (a, b) { return ORDER.indexOf(a.layer) - ORDER.indexOf(b.layer); });
    return { districts: out, taxCodeArea: tca };
  }

  function lookup(x, y, county, lang) {
    var defs = {};
    [TCA_LAYER].concat(ORDER).forEach(function (id) { defs[id] = '1=1'; });
    var url = SERVICE + '?layerDefs=' + encodeURIComponent(JSON.stringify(defs)) +
      '&geometry=' + encodeURIComponent(x + ',' + y) + '&geometryType=esriGeometryPoint&inSR=4326' +
      '&spatialRel=esriSpatialRelIntersects&returnGeometry=false&outFields=NAME,TCA&f=json';
    return jsonp(url).then(function (r) { return fromTax(r, county, lang); })
      .catch(function () { return null; });
  }

  var api = { lookup: lookup, fromTax: fromTax, prettyName: prettyName };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.CivicsIDDistricts = api;
})(typeof window !== 'undefined' ? window : this);
