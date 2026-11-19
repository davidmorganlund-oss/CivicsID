// Renders the share cards and app icons from HTML, in the site's own fonts.
// Run from the repo root: node tools/brand/render.js
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
// Fonts are embedded as data URLs: a page made with setContent can't load file:// fonts.
const font = (f) => 'data:font/woff2;base64,' + fs.readFileSync(path.resolve('site/fonts', f)).toString('base64');
const C = { wheat: '#F3E3C8', garnet: '#7A1F2E', garnetDark: '#5C1522', brown: '#8A5A22', ink: '#2E1D1A', tan: '#B8874A' };
const face = `
@font-face{font-family:Inter;font-weight:400;src:url(${font('inter-latin-400-normal.woff2')})}
@font-face{font-family:Inter;font-weight:500;src:url(${font('inter-latin-500-normal.woff2')})}
@font-face{font-family:SourceSerif;font-weight:700;src:url(${font('source-serif-4-latin-700-normal.woff2')})}
@font-face{font-family:BarlowCond;font-weight:600;src:url(${font('barlow-condensed-latin-600-normal.woff2')})}
*{margin:0;box-sizing:border-box} body{width:var(--w);height:var(--h);overflow:hidden}`;
const card = (eyebrow, title, body) => `<style>${face}
body{--w:1200px;--h:630px;background:${C.wheat};position:relative;font-family:Inter;color:${C.ink}}
.top{position:absolute;left:80px;right:80px;top:84px;display:flex;justify-content:space-between;align-items:center}
.logo{font:700 40px SourceSerif;color:${C.garnet}} .logo span{color:#fff;background:#C8102E;border-radius:6px;padding:0 7px;margin-left:4px}
.url{font:600 28px BarlowCond;letter-spacing:.08em;color:${C.garnetDark}}
.eye{position:absolute;left:80px;top:198px;font:600 28px BarlowCond;letter-spacing:.1em;text-transform:uppercase;color:${C.brown}}
h1{position:absolute;left:80px;top:240px;font:700 104px/1.05 SourceSerif;letter-spacing:-.015em;color:${C.garnetDark}}
p{position:absolute;left:80px;top:378px;width:760px;font:400 28px/1.5 Inter;color:${C.ink}}
.arc{position:absolute;right:-180px;bottom:-260px;width:520px;height:520px;border-radius:50%;border:56px solid rgb(122 31 46 / .12)}
.bar{position:absolute;left:0;right:0;bottom:0;height:18px;background:${C.garnet}}
</style><div class=top><div class=logo>Civics<span>ID</span></div><div class=url>CIVICSID.ORG</div></div>
<div class=eye>${eyebrow}</div><h1>${title}</h1><p>${body}</p><div class=arc></div><div class=bar></div>`;
const icon = (size) => `<style>${face}
body{--w:${size}px;--h:${size}px;background:${C.wheat};display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative}
.a{font:700 ${size*0.19}px/1 SourceSerif;color:${C.ink};margin-top:-${size*0.05}px}
.b{font:700 ${size*0.36}px/1 SourceSerif;color:#fff;background:#C8102E;border-radius:${size*0.05}px;padding:${size*0.03}px ${size*0.06}px ${size*0.045}px;margin-top:${size*0.04}px;letter-spacing:-.01em}
.bar{position:absolute;left:0;right:0;bottom:0;height:${size*0.055}px;background:${C.garnet}}
</style><div class=a>Civics</div><div class=b>ID</div><div class=bar></div>`;
(async () => {
  const b = await chromium.launch();
  const jobs = [
    ['site/share.png', 1200, 630, card('Community calendar', 'Get Engaged, Idaho.', 'See what your city council, county, school board and the Legislature are deciding this week, and how to make your voice heard.')],
    ['site/share-es.png', 1200, 630, card('Calendario comunitario', 'Participa, Idaho.', 'Vea lo que deciden esta semana su concejo municipal, su condado, su junta escolar y la Legislatura, y cómo hacerse escuchar.')],
    ['site/icon-512.png', 512, 512, icon(512)], ['site/icon-192.png', 192, 192, icon(192)], ['site/apple-touch-icon.png', 180, 180, icon(180)],
  ];
  for (const [out, w, h, html] of jobs) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.setContent(html); await p.evaluate(async () => { await document.fonts.ready; return [...document.fonts].map(f => f.status); }); await p.waitForTimeout(200);
    await p.screenshot({ path: out }); await p.close();
  }
  await b.close();
})();
