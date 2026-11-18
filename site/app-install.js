/* CivicsID: register the service worker so the site can be added to a home
   screen and still open (with the last calendar it saw) without a signal. */
if ('serviceWorker' in navigator && location.protocol === 'https:') {
  window.addEventListener('load', function () {
    navigator.serviceWorker.register('/sw.js').catch(function () { /* the site works without it */ });
  });
}
