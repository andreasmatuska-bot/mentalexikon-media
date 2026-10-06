// Baut die kurzen Listen Videos für Mindsetologie (grauer Papier Hintergrund, goldene Überschrift, Liste).
// Aufruf in karussells/_engine:  node listen_video.js <plan.json> <Ausgabeordner> [slug ...]
// Je Eintrag entstehen <slug>.mp4 (6 Sekunden: kurz der Hook, dann die ganze Liste), <slug>_hook.jpg und <slug>_liste.jpg.
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const f = (fam, w, st) => 'data:font/woff2;base64,' + fs.readFileSync(
  path.join(__dirname, `node_modules/@fontsource/${fam}/files/${fam}-latin-${w}-${st}.woff2`)).toString('base64');
const GOLD = '#D2B45A';
const css = `
@font-face{font-family:P;font-weight:400;src:url(${f('playfair-display', 400, 'normal')})}
@font-face{font-family:P;font-weight:400;font-style:italic;src:url(${f('playfair-display', 400, 'italic')})}
@font-face{font-family:P;font-weight:900;src:url(${f('playfair-display', 900, 'normal')})}
@font-face{font-family:M;font-weight:800;src:url(${f('montserrat', 800, 'normal')})}
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:P;color:#151515;
 background:radial-gradient(ellipse 75% 55% at 55% 30%,#f4f4f4 0%,#dcdcdc 45%,#b4b4b4 100%)}
svg.n{position:absolute;inset:0;width:100%;height:100%;opacity:.38;mix-blend-mode:multiply}
.w{position:absolute;left:112px;right:112px;top:200px;bottom:310px;display:flex;flex-direction:column;justify-content:center}
h1{font-weight:900;font-size:calc(var(--s)*1.16);line-height:1.5;text-transform:uppercase;letter-spacing:.2px;margin-bottom:calc(var(--s)*1.15)}
h1 span{background:${GOLD};padding:.12em .28em;box-decoration-break:clone;-webkit-box-decoration-break:clone;box-shadow:6px 6px 0 rgba(0,0,0,.14)}
.i{display:flex;gap:calc(var(--s)*.7);font-size:var(--s);line-height:1.34;margin-bottom:calc(var(--s)*var(--g))}
.i .m{flex:none;width:calc(var(--s)*1.05);color:${GOLD};font-weight:900;text-shadow:1px 1px 0 rgba(0,0,0,.18)}
.i b,.p b,.z b{font-weight:900}
.p{font-size:var(--s);line-height:1.4;margin-bottom:calc(var(--s)*1.05)}
.t{display:flex;justify-content:space-between;gap:20px;font-size:var(--s);line-height:1.3;margin-bottom:calc(var(--s)*var(--g))}
.t .l{display:flex;gap:calc(var(--s)*.6)} .t .l i{font-style:normal;color:${GOLD};font-weight:900} .t .r{font-weight:900;text-align:right;white-space:nowrap}
.gr{display:grid;grid-template-columns:1fr 1fr;gap:calc(var(--s)*1.1) 40px}
.gr h2{font-size:calc(var(--s)*.92);font-weight:900;letter-spacing:.5px;text-transform:uppercase;border-bottom:2px solid rgba(0,0,0,.35);display:inline-block;margin-bottom:8px}
.gr div div{font-size:var(--s);line-height:1.32}
.z{font-weight:900;font-size:var(--s);line-height:1.35;margin-top:calc(var(--s)*.3);border-left:6px solid ${GOLD};padding-left:18px}
.q{font-style:italic;font-size:calc(var(--s)*.95);text-align:center;margin-top:calc(var(--s)*1.2);color:#2a2a2a}
.c{font-weight:900;font-size:calc(var(--s)*1.12);text-align:center;margin-top:calc(var(--s)*.5)}
.hook{position:absolute;left:90px;right:90px;top:0;bottom:120px;display:flex;align-items:center;justify-content:center;text-align:center}
.hook p{font-family:M;font-weight:800;font-size:62px;line-height:1.62;text-transform:uppercase;letter-spacing:1px}
.hook span{background:rgba(120,120,120,.38);border-radius:14px;padding:.12em .34em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
`;
const noise = `<svg class="n" xmlns="http://www.w3.org/2000/svg"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3" seed="7"/><feColorMatrix values="0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .9 0"/></filter><rect width="100%" height="100%" filter="url(#g)"/></svg>`;

function body(e) {
  let h = `<h1><span>${e.kopf}</span></h1>`;
  if (e.typ === 'nummern') h += e.punkte.map((p, i) => `<div class="i"><span class="m">${i + 1}.</span><span>${p}</span></div>`).join('');
  else if (e.typ === 'liste') h += e.punkte.map(p => `<div class="i"><span class="m">●</span><span>${p}</span></div>`).join('');
  else if (e.typ === 'story') h += e.punkte.map(p => `<div class="p">${p}</div>`).join('');
  else if (e.typ === 'tabelle') h += e.punkte.map(p => `<div class="t"><span class="l"><i>●</i>${p[0]}</span><span class="r">${p[1]}</span></div>`).join('');
  else if (e.typ === 'gruppen') h += `<div class="gr">` + e.punkte.map(g => `<div><h2>${g.titel}</h2>${g.zeilen.map(z => `<div>${z}</div>`).join('')}</div>`).join('') + `</div>`;
  else throw new Error('typ ' + e.typ);
  if (e.schluss) h += `<div class="z">${e.schluss}</div>`;
  if (e.frage) h += `<div class="q">${e.frage}</div>`;
  h += `<div class="c">${e.cta || 'Folg uns für mehr davon.'}</div>`;
  return h;
}
const page = inner => `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>${noise}${inner}</body></html>`;

(async () => {
  const plan = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const OUT = process.argv[3]; const nur = process.argv.slice(4);
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }).catch(() => chromium.launch());
  const pg = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  for (const e of plan) {
    if (nur.length && !nur.includes(e.slug)) continue;
    const base = path.join(OUT, e.slug);
    await pg.setContent(page(`<div class="hook"><p><span>${e.kopf}</span></p></div>`));
    await pg.evaluate(() => document.fonts.ready);
    await pg.screenshot({ path: base + '_hook.jpg', type: 'jpeg', quality: 93 });
    await pg.setContent(page(`<div class="w" style="--s:44px;--g:.78">${body(e)}</div>`));
    await pg.evaluate(() => document.fonts.ready);
    // Schrift so groß wie möglich, bis alles in den sicheren Bereich passt
    const s = await pg.evaluate(() => {
      const w = document.querySelector('.w');
      for (let s = 48; s >= 24; s -= 1) for (const g of [.85, .7, .55]) {
        w.style.setProperty('--s', s + 'px'); w.style.setProperty('--g', g);
        if (w.scrollHeight <= w.clientHeight + 1 && w.scrollWidth <= w.clientWidth + 1) return s;
      }
      return 0;
    });
    if (!s) console.log('UEBERLAUF', e.slug);
    await pg.screenshot({ path: base + '_liste.jpg', type: 'jpeg', quality: 93 });
    // 6 Sekunden: 0,7 s Hook, kurze Blende, dann die Liste. Stille Tonspur, damit Instagram die Datei sicher annimmt.
    execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-loop', '1', '-t', '0.9', '-i', base + '_hook.jpg', '-loop', '1', '-t', '5.4', '-i', base + '_liste.jpg',
      '-f', 'lavfi', '-t', '6', '-i', 'anullsrc=r=44100:cl=stereo',
      '-filter_complex', '[0:v]fps=30,format=yuv420p[a];[1:v]fps=30,format=yuv420p[b];[a][b]xfade=transition=fade:duration=0.3:offset=0.6[v]',
      '-map', '[v]', '-map', '2:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '96k', '-t', '6', '-movflags', '+faststart', base + '.mp4']);
    console.log('ok', e.slug, 'schrift', s);
  }
  await b.close();
})();
