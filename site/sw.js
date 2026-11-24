/* CivicsID service worker.
   Pages, scripts and styles: served from cache right away, refreshed in the
   background. Calendar data (data/*.json): network first, so it's never stale
   when you're online, with the last copy as the fallback offline. */
var VERSION = 'civicsid-v10';
var SHELL = ['/', '/index.html', '/styles.css', '/app.js', '/engage.html', '/legislature.html', '/legislature.js',
  '/reps.html', '/reps.js', '/districts.js', '/privacy.html', '/es/', '/es/index.html', '/es/engage.html', '/es/reps.html',
  '/fonts/inter-latin-400-normal.woff2', '/fonts/inter-latin-600-normal.woff2', '/fonts/source-serif-4-latin-700-normal.woff2',
  '/fonts/barlow-condensed-latin-500-normal.woff2', '/icon-192.png', '/barnone-phoenix.png'];

self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(VERSION).then(function (c) { return c.addAll(SHELL); }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener('activate', function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k !== VERSION; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

self.addEventListener('fetch', function (e) {
  var req = e.request;
  var url = new URL(req.url);
  if (req.method !== 'GET' || url.origin !== location.origin) return;  // other sites (agendas, Census) go straight to the network
  if (url.pathname.indexOf('/data/') === 0) {
    e.respondWith(fetch(req).then(function (res) {
      // Keep only good copies, so an outage page never replaces the last real data.
      if (res.ok) { var copy = res.clone(); caches.open(VERSION).then(function (c) { c.put(req, copy); }); }
      return res.ok ? res : caches.match(req).then(function (hit) { return hit || res; });
    }).catch(function () { return caches.match(req); }));
    return;
  }
  e.respondWith(caches.match(req).then(function (hit) {
    var fresh = fetch(req).then(function (res) {
      if (res.ok) { var copy = res.clone(); caches.open(VERSION).then(function (c) { c.put(req, copy); }); }
      return res;
    }).catch(function () {
      if (hit) return hit;
      // Offline on a page we haven't saved: show the calendar in the same
      // language. Images, scripts and the like just fail as usual.
      if (req.mode === 'navigate') return caches.match(url.pathname.indexOf('/es/') === 0 ? '/es/index.html' : '/index.html');
      return Response.error();
    });
    return hit || fresh;
  }));
});
