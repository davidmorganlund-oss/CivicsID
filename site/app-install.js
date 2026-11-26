/* CivicsID: register the service worker so the site can be added to a home
   screen and still open (with the last calendar it saw) without a signal.
   On the home page, the "Use it like an app" note hides once the site is
   running as an installed app, and gets a one-tap Install button where the
   browser offers one (Chrome and Edge on Android and computers). */
if ('serviceWorker' in navigator && location.protocol === 'https:') {
  window.addEventListener('load', function () {
    navigator.serviceWorker.register('/sw.js').catch(function () { /* the site works without it */ });
  });
}
(function () {
  var installed = function () { return window.matchMedia('(display-mode: standalone)').matches || navigator.standalone === true; };
  var tip = function () { return document.getElementById('app-tip'); };
  var prompt = null;
  function hideIfInstalled() { var t = tip(); if (t && installed()) t.hidden = true; }
  function offerButton() {
    var t = tip();
    if (!t || !prompt || installed() || t.querySelector('.btn')) return;
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'btn';
    b.style.marginTop = '12px';
    b.textContent = document.documentElement.lang === 'es' ? 'Instalar la aplicación' : 'Install the app';
    b.addEventListener('click', function () {
      if (!prompt) return;
      prompt.prompt();
      prompt.userChoice.then(function () { prompt = null; b.remove(); });
    });
    t.appendChild(b);
  }
  window.addEventListener('beforeinstallprompt', function (e) { e.preventDefault(); prompt = e; offerButton(); });
  window.addEventListener('appinstalled', function () { var t = tip(); if (t) t.hidden = true; });
  document.addEventListener('DOMContentLoaded', function () { hideIfInstalled(); offerButton(); });
})();
