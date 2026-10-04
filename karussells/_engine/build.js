const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const HANDLE = '@mentalexikon';
const THEMES = { beige: ['#E3DCCB', '#16140F', '#8E8776'], hell: ['#F1EEE7', '#16140F', '#9A958A'], schwarz: ['#101010', '#F4F1EA', '#77736B'] };
const [BG, FG, MUTED] = THEMES[process.argv[4] || 'beige'];
const OUT = process.argv[2] || 'out';
const slides = JSON.parse(fs.readFileSync(process.argv[3] || 'slides.json', 'utf8'));
const f = w => 'data:font/woff2;base64,' + fs.readFileSync(
  path.join(__dirname, `node_modules/@fontsource/sofia-sans-condensed/files/sofia-sans-condensed-latin-${w}-normal.woff2`)).toString('base64');

const html = (paras, i, n) => `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:S;font-weight:500;src:url(${f(500)})}
@font-face{font-family:S;font-weight:800;src:url(${f(800)})}
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1440px;background:${BG};color:${FG};font-family:S;font-weight:500;position:relative}
.t{position:absolute;left:120px;right:120px;top:0;bottom:150px;display:flex;flex-direction:column;justify-content:center;gap:58px}
p{font-size:82px;line-height:1.1;letter-spacing:-0.5px;text-wrap:balance;max-width:800px}
b{font-weight:800}
.f{position:absolute;left:120px;right:120px;bottom:92px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:1px;color:${MUTED}}
</style></head><body><div class="t">${paras.map(p => `<p>${p}</p>`).join('')}</div>
<div class="f"><span>${String(i).padStart(2, '0')}/${String(n).padStart(2, '0')}</span><span>${HANDLE}</span><span>${i < n ? '→' : '&nbsp;&nbsp;'}</span></div></body></html>`;

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }).catch(() => chromium.launch());
  const pg = await b.newPage({ viewport: { width: 1080, height: 1440 } });
  for (let i = 0; i < slides.length; i++) {
    await pg.setContent(html(slides[i], i + 1, slides.length));
    await pg.evaluate(() => document.fonts.ready);
    const over = await pg.evaluate(() => { const t = document.querySelector('.t'); return t.scrollHeight > t.clientHeight + 1 || [...document.querySelectorAll('p')].some(p => p.scrollWidth > p.clientWidth + 1); });
    if (over) console.log('UEBERLAUF Slide', i + 1);
    await pg.screenshot({ path: path.join(OUT, `${String(i + 1).padStart(2, '0')}.jpg`), type: 'jpeg', quality: 95 });
  }
  await b.close();
  console.log('ok', slides.length);
})();
