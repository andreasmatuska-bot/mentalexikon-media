// node build_post.js posts/wang.json mentalexikon|mindsetologie
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const P = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const TH = { mentalexikon: { name: 'Mentalexikon', handle: '@mentalexikon', bg: '#0E0E0E', ac: '#F4C700', tx: '#F4F1EA', gr: '#8A857B', glow: '244,199,0', cover: 'round' },
  mindsetologie: { name: 'Mindsetologie', handle: '@mindsetologie', bg: '#0A1220', ac: '#FF8A1F', tx: '#EEF2F7', gr: '#8492A6', glow: '255,138,31', cover: 'rect' } };
const T = TH[process.argv[3] || 'mentalexikon'];
const OUT = path.join(__dirname, 'out', `${T.name}_${P.slug}`); fs.mkdirSync(OUT, { recursive: true });
const d = (f, m) => `data:${m};base64,` + fs.readFileSync(path.join(__dirname, f)).toString('base64');
const font = w => d(`node_modules/@fontsource/sofia-sans-condensed/files/sofia-sans-condensed-latin-${w}-normal.woff2`, 'font/woff2');
const photo = d(P.photo, 'image/jpeg');
const S = P.slides;
const fmt = t => t.replace(/<y>/g, '<span class="y">').replace(/<\/y>/g, '</span>');
const css = `
@font-face{font-family:S;font-weight:500;src:url(${font(500)})}
@font-face{font-family:S;font-weight:800;src:url(${font(800)})}
@font-face{font-family:S;font-weight:900;src:url(${font(900)})}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1440px;background:${T.bg};color:${T.tx};font-family:S;font-weight:500;position:relative;overflow:hidden}
b{font-weight:800;color:#fff}.y{color:${T.ac}}
.bar{width:84px;height:10px;background:${T.ac}}
.foot{position:absolute;left:96px;right:96px;bottom:64px;display:flex;justify-content:space-between;align-items:center;font-size:30px;color:${T.gr};letter-spacing:1px}
.arrow{color:${T.ac};font-weight:800;font-size:40px}
.wrap{position:absolute;left:96px;right:96px;top:120px;bottom:150px;display:flex;flex-direction:column}
.body{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;gap:.62em;line-height:1.16}
.big{font-weight:900;color:${T.ac};font-size:230px;line-height:.9;letter-spacing:-4px;margin-top:40px;white-space:nowrap}
.sub{font-size:38px;color:${T.gr};text-transform:uppercase;letter-spacing:2px;margin-top:14px;line-height:1.15}
.cov{position:absolute;left:96px;right:96px;top:800px;bottom:170px;display:flex;flex-direction:column;justify-content:center;gap:.34em;line-height:1.04;font-weight:800;color:#fff}
.credit{position:absolute;left:96px;bottom:118px;font-size:20px;color:${T.gr};opacity:.7;letter-spacing:.5px}
.ava{width:230px;height:230px;border-radius:50%;overflow:hidden;border:5px solid ${T.ac};margin-top:36px;flex:none}
.ctah{font-weight:900;color:#fff;line-height:1.02}
.li{display:flex;gap:22px;align-items:baseline}
.box{background:${T.ac};color:${T.bg};font-weight:800;padding:34px 40px;border-radius:10px;line-height:1.1}
.ph{font-weight:800;color:#fff;font-size:64px;line-height:1.06}
.shot{display:block;border-radius:18px;border:3px solid ${T.ac};box-shadow:0 18px 60px rgba(0,0,0,.6)}
.tag{display:inline-block;background:${T.ac};color:${T.bg};font-weight:800;font-size:26px;letter-spacing:2px;padding:6px 14px;border-radius:6px;text-transform:uppercase}
.note{font-size:26px;color:${T.gr};line-height:1.2}
`;
function html(s, i) {
  const n = S.length;
  const foot = `<div class="foot"><span>${i + 1}/${n}</span><span>${T.handle}</span><span class="arrow">${i < n - 1 ? '→' : ''}</span></div>`;
  if (s.type === 'cover') {
    const pic = T.cover === 'round'
      ? `<div style="position:absolute;left:210px;top:110px;width:660px;height:660px;border-radius:50%;border:8px solid ${T.ac};overflow:hidden;box-shadow:0 0 140px rgba(${T.glow},.28)"><img src="${photo}" style="${P.photoPos.cover}"></div>`
      : `<div style="position:absolute;left:96px;top:96px;width:888px;height:660px;border-radius:44px;border:6px solid ${T.ac};overflow:hidden;box-shadow:0 0 140px rgba(${T.glow},.25)"><img src="${photo}" style="width:888px;margin-top:-150px"></div>`;
    return `<style>${css}</style><div style="position:absolute;inset:0 0 540px 0;background:radial-gradient(800px 640px at 50% 50%,rgba(${T.glow},.20) 0%,rgba(${T.glow},.05) 55%,transparent 80%)"></div>
${pic}<div class="cov fit" data-max="100" data-min="60">${s.lines.map(l => `<div>${fmt(l)}</div>`).join('')}</div>
<div class="credit">${P.credit}</div>${foot}`;
  }
  if (s.type === 'cta') {
    return `<style>${css}</style><div class="wrap"><div class="bar"></div><div class="body fit" data-max="76" data-min="48">
      <div class="ctah" style="font-size:1.32em">${s.head}</div>
      <div style="color:${T.gr};font-size:.72em;text-transform:uppercase;letter-spacing:2px;margin-top:.2em">${s.lead}</div>
      ${s.list.map((l, k) => `<div class="li"><span class="y" style="font-weight:900">${k + 1}.</span><span>${l}</span></div>`).join('')}
      <div><b>${s.close}</b></div>
      <div class="box">${s.cta}</div></div></div>${foot}`;
  }
  if (s.type === 'proof') {
    const im = a => (a || []).map(x => `<img class="shot" src="${d(x.src, 'image/png')}" style="width:${x.w}px">`).join('');
    return `<style>${css}</style><div class="wrap"><div style="display:flex;align-items:center;gap:24px"><div class="bar"></div><span class="tag">Beweis</span></div>
      <div class="body" style="gap:44px">
      <div class="ph">${fmt(s.head)}</div>${im(s.imgs)}
      ${s.head2 ? `<div class="ph" style="margin-top:14px">${fmt(s.head2)}</div>${im(s.imgs2)}` : ''}
      ${s.line ? `<div class="ph" style="font-size:104px;line-height:1.02">${fmt(s.line)}</div>` : ''}
      <div class="note">${s.note}</div></div></div>${foot}`;
  }
  const ava = s.ava ? `<div class="ava"><img src="${photo}" style="${P.photoPos.ava}"></div>` : s.avaSrc ? `<div class="ava" style="width:300px;height:300px"><img src="${d(s.avaSrc, 'image/jpeg')}" style="width:100%"></div>` : '';
  const big = s.big ? `<div class="big">${s.big}</div><div class="sub">${s.sub}</div>` : '';
  return `<style>${css}</style><div class="wrap"><div class="bar"></div>${ava}${big}<div class="body fit" data-max="${s.big ? 72 : 84}" data-min="44">${s.p.map(l => `<div>${fmt(l)}</div>`).join('')}</div></div>${foot}`;
}
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }).catch(() => chromium.launch());
  const pg = await b.newPage({ viewport: { width: 1080, height: 1440 } });
  for (let i = 0; i < S.length; i++) {
    await pg.setContent(html(S[i], i));
    await pg.evaluate(() => document.fonts.ready);
    const res = await pg.evaluate(() => {
      const el = document.querySelector('.fit');
      if (!el) { const b = document.querySelector('.body'); const r = [...b.children].map(c => c.getBoundingClientRect()); const h = r.reduce((a, x) => a + x.height, 0) + 30 * (r.length - 1); return h <= b.clientHeight ? 'ok ' + Math.round(h) + '/' + b.clientHeight : 'UEBERLAUF ' + Math.round(h) + '/' + b.clientHeight; }
      const max = +el.dataset.max, min = +el.dataset.min;
      const kids = () => { const r = [...el.children].map(c => c.getBoundingClientRect()); const gap = parseFloat(getComputedStyle(el).rowGap) || 0; return r.reduce((a, b) => a + b.height, 0) + gap * (r.length - 1); };
      for (let f = max; f >= min; f -= 2) { el.style.fontSize = f + 'px'; if (kids() <= el.clientHeight - 4) return f; }
      return 'UEBERLAUF';
    });
    await pg.screenshot({ path: path.join(OUT, `slide_${String(i + 1).padStart(2, '0')}.jpg`), type: 'jpeg', quality: 92 });
    console.log(i + 1, res);
  }
  fs.writeFileSync(path.join(OUT, 'caption.txt'), P.caption);
  await b.close();
})();
