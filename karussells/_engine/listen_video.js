// Baut die kurzen Listen Videos für Mindsetologie im Stil der bisherigen Reels der Seite:
// cremefarbener Hintergrund, goldener Kasten mit der Überschrift, Liste in Liberation Sans, Wasserzeichen MINDSETOLOGIE.
// Das Video ist ein Standbild (wie die Originale, rund 4 Sekunden) mit eigener kurzer Musik.
// Aufruf in karussells/_engine:  node listen_video.js <plan.json> <Ausgabeordner> [slug ...]
// Je Eintrag entstehen <slug>.mp4 und <slug>.jpg (Titelbild = dasselbe Bild).
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const GOLD = '#C8B163', BG = '#F4F1EA', INK = '#1E2021';
const css = `
*{margin:0;box-sizing:border-box}
body{width:720px;height:1280px;position:relative;overflow:hidden;background:${BG};color:${INK};font-family:'Liberation Sans',Arial,sans-serif}
.w{position:absolute;left:74px;right:74px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center}
h1{background:${GOLD};padding:16px 23px 17px;font-weight:700;font-size:var(--h);line-height:1.1;letter-spacing:-.7px;text-transform:uppercase}
.r{border-top:1px solid #D9D6CE;margin-top:27px}
.r2{border-top:1px solid #D9D6CE;margin-top:19px}
.l{padding-top:19px}
.i{display:flex;font-size:var(--s);line-height:1.5;letter-spacing:.17px;margin-bottom:var(--g)}
.i:last-child{margin-bottom:0}
.i .d{flex:none;width:21px;color:${GOLD};font-weight:700;font-size:1.25em;line-height:1.2}
.i .n{flex:none;width:47px;color:${GOLD};font-weight:700;font-size:calc(var(--s)*.8);padding-top:.1em}
.i b,.p b{font-weight:700}
.sh{font-size:calc(var(--s)*1.1);font-weight:700;line-height:1.5;margin:4px 0 8px}
.p{font-size:var(--s);line-height:1.5;letter-spacing:.17px;margin-bottom:var(--g)}
.t{display:flex;justify-content:space-between;gap:16px;font-size:var(--s);line-height:1.5;margin-bottom:var(--g)}
.t .a{display:flex}.t .a i{font-style:normal;flex:none;width:21px;color:${GOLD};font-weight:700}.t .b{font-weight:700;text-align:right;white-space:nowrap}
.z{font-size:var(--s);line-height:1.5;font-weight:700;margin-top:var(--g)}
.q{font-weight:700;font-size:18px;line-height:1.4;text-align:center;margin-top:16px}
.q img{height:19px;vertical-align:-3px;margin-left:4px}
.wm{position:absolute;right:42px;bottom:21px;font-size:14px;font-weight:700;letter-spacing:3.4px;color:#DEDBD4}
`;
function body(e) {
  let h = `<h1>${e.kopf}</h1><div class="r"></div><div class="l">`;
  const it = (m, p) => `<div class="i">${m}<span>${p}</span></div>`;
  if (e.typ === 'nummern') h += e.punkte.map((p, i) => it(`<span class="n">${i + 1}.</span>`, p)).join('');
  else if (e.typ === 'liste') h += e.punkte.map(p => it(`<span class="d">•</span>`, p)).join('');
  else if (e.typ === 'story') h += e.punkte.map(p => `<div class="p">${p}</div>`).join('');
  else if (e.typ === 'tabelle') h += e.punkte.map(p => `<div class="t"><span class="a"><i>•</i>${p[0]}</span><span class="b">${p[1]}</span></div>`).join('');
  else if (e.typ === 'gruppen') h += e.punkte.map(g => `<div class="sh">${g.titel}:</div>` + g.zeilen.map(z => it(`<span class="d">•</span>`, z)).join('')).join('');
  else throw new Error('typ ' + e.typ);
  if (e.schluss) h += `<div class="z">${e.schluss}</div>`;
  h += `</div><div class="r2"></div><div class="q">${e.frage} 👇</div>`;
  return h;
}
const page = e => `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><div class="w" style="--s:21px;--g:15.8px;--h:32px">${body(e)}</div><div class="wm">MINDSETOLOGIE</div></body></html>`;

(async () => {
  const plan = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const OUT = process.argv[3]; const nur = process.argv.slice(4);
  const musik = fs.readdirSync(path.join(__dirname, 'musik')).filter(f => f.endsWith('.wav')).sort();
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }).catch(() => chromium.launch());
  const pg = await b.newPage({ viewport: { width: 720, height: 1280 }, deviceScaleFactor: 1.5 });
  let k = 0;
  for (const e of plan) {
    k++;
    if (nur.length && !nur.includes(e.slug)) continue;
    const base = path.join(OUT, e.slug);
    await pg.setContent(page(e));
    await pg.evaluate(() => document.fonts.ready);
    // Standard ist die Größe der Originale (21 px). Nur wenn der Text nicht passt, wird verkleinert.
    const s = await pg.evaluate(() => {
      const w = document.querySelector('.w');
      for (const [s, g, h] of [[21, 15.8, 32], [20, 14, 32], [19, 13, 31], [18, 11, 30], [17, 10, 29], [16, 9, 28], [15, 8, 27], [14, 7, 26]]) {
        w.style.setProperty('--s', s + 'px'); w.style.setProperty('--g', g + 'px'); w.style.setProperty('--h', h + 'px');
        const hgt = [...w.children].reduce((a, c) => a + c.getBoundingClientRect().height + parseFloat(getComputedStyle(c).marginTop), 0);
        if (hgt <= 1280 - 2 * 150) return s;
      }
      return 0;
    });
    if (!s) console.log('UEBERLAUF', e.slug);
    await pg.screenshot({ path: base + '.jpg', type: 'jpeg', quality: 95 });
    const m = path.join(__dirname, 'musik', musik[(parseInt(e.nr, 10) || k) % musik.length]);
    execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-loop', '1', '-framerate', '30', '-i', base + '.jpg', '-i', m,
      '-t', '4.13', '-vf', 'scale=1080:1920,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-r', '30',
      '-c:a', 'aac', '-b:a', '160k', '-af', 'volume=6dB,alimiter=limit=0.89,afade=t=in:d=0.03,afade=t=out:st=3.75:d=0.38', '-movflags', '+faststart', base + '.mp4']);
    console.log('ok', e.slug, 'schrift', s, path.basename(m));
  }
  await b.close();
})();
