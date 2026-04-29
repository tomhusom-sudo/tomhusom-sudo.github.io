var CACHE_NAME = 'honesttom-v4';
self.addEventListener('install', function(e) { self.skipWaiting(); });
self.addEventListener('activate', function(e) {
  e.waitUntil(caches.keys().then(function(names){
    return Promise.all(names.map(function(n){ return caches.delete(n); }));
  }).then(function(){ return clients.claim(); }));
});
self.addEventListener('fetch', function(e) {
  if (e.request.method !== 'GET') return;
  // Always fetch fresh for HTML and JS - never use cache
  var url = e.request.url;
  if (url.endsWith('.html') || url.endsWith('.js') || url.endsWith('/')) {
    e.respondWith(fetch(e.request, {cache: 'no-store'}));
    return;
  }
  e.respondWith(fetch(e.request).catch(function(){ return caches.match(e.request); }));
});