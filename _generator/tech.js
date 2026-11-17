/* ===================================================================
   TECHNIK-BAUSTEINE (ergänzen lib.js)
   =================================================================== */
const visible = el => { const s = el.closest('.station'); return !s || !s.hidden; };
const fmtU = v => numDE(v, v < 10 ? 2 : 1) + ' V';
const fmtI = v => !isFinite(v) ? '∞' : v >= 1 ? numDE(v, 2) + ' A' : numDE(v * 1000, v < 0.01 ? 1 : 0) + ' mA';
const fmtR = v => !isFinite(v) ? '∞' : v >= 1e6 ? numDE(v / 1e6, 2) + ' MΩ' : v >= 1000 ? numDE(v / 1000, v < 1e4 ? 2 : 1) + ' kΩ' : numDE(v, 1) + ' Ω';
const fmtP = v => numDE(v, v < 10 ? 2 : 1) + ' W';
/* Animationsschleife, die nur läuft, solange die Station sichtbar ist. step(dt in s) */
function animLoop(root, step) {
  let last = performance.now();
  function f(now) {
    const dt = Math.min(.1, (now - last) / 1000); last = now;
    if (visible(root)) step(dt);
    requestAnimationFrame(f);
  }
  requestAnimationFrame(f);
}
function readout(el, cells) { el.innerHTML = cells.map(([k, v]) => `<div><small>${k}</small><b>${v}</b></div>`).join(''); }
function slider(label, min, max, step, val, unit = '') {
  return `<label>${label} <input type="range" min="${min}" max="${max}" step="${step}" value="${val}"> <span class="tk-val"></span>${unit ? '' : ''}</label>`;
}

/* ---------- Schaltzeichen (SVG-Strings) ---------- */
const SY = {
  wire: (pts) => `<path class="w" d="M${pts.map(p => p.join(' ')).join(' L')}"/>`,
  lamp: (x, y, b = 0) => `<circle class="glow" cx="${x}" cy="${y}" r="${18 + 14 * Math.min(1, b)}" opacity="${Math.min(1, b).toFixed(2)}"/><circle class="sym" cx="${x}" cy="${y}" r="15"/><path class="thin" stroke-width="2.2" d="M${x - 10.6} ${y - 10.6}L${x + 10.6} ${y + 10.6}M${x + 10.6} ${y - 10.6}L${x - 10.6} ${y + 10.6}"/>`,
  res: (x, y, v) => v ? `<rect class="sym" x="${x - 9}" y="${y - 23}" width="18" height="46"/>` : `<rect class="sym" x="${x - 23}" y="${y - 9}" width="46" height="18"/>`,
  /* Batterie, Pluspol oben (senkrechte Leitung) */
  bat: (x, y) => `<rect x="${x - 26}" y="${y - 5}" width="52" height="10" fill="var(--surface)"/><path class="w" d="M${x - 22} ${y - 6}H${x + 22}"/><path class="w" stroke-width="7" d="M${x - 11} ${y + 6}H${x + 11}"/><text x="${x + 28}" y="${y - 8}" class="sm">+</text><text x="${x + 28}" y="${y + 16}" class="sm">−</text>`,
  /* Batterie in waagerechter Leitung, Pluspol links */
  batH: (x, y) => `<rect x="${x - 5}" y="${y - 26}" width="10" height="52" fill="var(--surface)"/><path class="w" d="M${x - 6} ${y - 20}V${y + 20}"/><path class="w" stroke-width="7" d="M${x + 6} ${y - 10}V${y + 10}"/>`,
  /* Schalter in waagerechter Leitung */
  sw: (x, y, closed, id, v) => `<g class="click" data-sw="${id}" tabindex="0" role="button" aria-label="Schalter ${closed ? 'schließen' : 'öffnen'}"${v ? ` transform="rotate(90 ${x} ${y})"` : ''}><rect x="${x - 26}" y="${y - 24}" width="52" height="34" fill="var(--surface)" opacity=".01"/><rect x="${x - 17}" y="${y - 3}" width="34" height="6" fill="var(--surface)"/><circle class="sym" cx="${x - 17}" cy="${y}" r="3.5"/><circle class="sym" cx="${x + 17}" cy="${y}" r="3.5"/><path class="w" d="M${x - 17} ${y}L${closed ? `${x + 17} ${y}` : `${x + 13} ${y - 17}`}"/></g>`,
  meter: (x, y, t) => `<circle class="sym" cx="${x}" cy="${y}" r="15"/><text x="${x}" y="${y + 5.5}" text-anchor="middle">${t}</text>`,
  led: (x, y, on, v) => `<g${v ? ` transform="rotate(90 ${x} ${y})"` : ''}><circle cx="${x}" cy="${y}" r="${on ? 24 : 0}" class="glow" opacity="${on ? .9 : 0}"/><rect x="${x - 14}" y="${y - 14}" width="28" height="28" fill="var(--surface)"/><path class="sym" d="M${x - 10} ${y - 12}L${x + 10} ${y}L${x - 10} ${y + 12}Z"/><path class="w" d="M${x + 10} ${y - 12}V${y + 12}"/><path class="thin" d="M${x + 2} ${y - 16}l8 -8m-5 0h5v5M${x + 9} ${y - 12}l8 -8m-5 0h5v5"/></g>`
};

/* ---------- Stromkreis-Simulator ----------
   circuit(root, {mode:'series'|'parallel', loads:[{t:'lamp'|'res', R, name}], U, uMax, editR, rMax, branchSw, short, unom, show:[…], note})
   show: 'U','I','R','P', 'U1','I1','P1', … (je Verbraucher) */
function circuit(root, o = {}) {
  const loads = o.loads.map((l, i) => ({...l, R0: l.R, on: true, broken: false, name: l.name || (l.t === 'lamp' ? 'L' : 'R') + (i + 1)}));
  const n = loads.length, par = o.mode === 'parallel';
  let U = o.U ?? 4.5, closed = o.closed ?? true, shorted = false;
  const unom = o.unom ?? 4.5;
  root.classList.add('tk-circ');
  root.innerHTML = `<div class="tk-fig"><svg class="sch" viewBox="0 0 560 310" role="img" aria-label="Schaltplan"></svg></div>
    <div class="tk-row">${o.uMax ? `<label>Spannung U <input type="range" data-k="U" min="${o.uMin ?? 0}" max="${o.uMax}" step="${o.uStep ?? 0.5}" value="${U}"> <span class="tk-val" data-o="U"></span></label>` : ''}
    ${o.editR ? loads.map((l, i) => `<label>${l.name} <input type="range" data-k="R${i}" min="${o.rMin ?? 1}" max="${o.rMax ?? 100}" step="1" value="${l.R}"> <span class="tk-val" data-o="R${i}"></span></label>`).join('') : ''}
    ${o.short ? '<button class="btn" data-k="short">Kurzschluss-Brücke</button>' : ''}${loads.some(l => l.t === 'lamp') && o.burn !== false ? '<button class="btn" data-k="fix" hidden>Lampe ersetzen</button>' : ''}</div>
    <div class="tk-readout"></div><p class="status" aria-live="polite"></p>`;
  const svg = $('svg', root), ro = $('.tk-readout', root), st = $('.status', root);
  function solve() {
    const r = loads.map(l => (l.broken || (par && !l.on)) ? Infinity : l.R);
    let I = 0, Rg = Infinity, Ui = loads.map(() => 0), Ii = loads.map(() => 0);
    if (closed) {
      if (shorted) { Rg = 0.15; I = U / Rg; }
      else if (!par) { Rg = r.reduce((a, b) => a + b, 0); I = isFinite(Rg) ? U / Rg : 0; Ii = loads.map(() => I); Ui = r.map(x => isFinite(x) ? x * I : (isFinite(Rg) ? 0 : 0)); if (!isFinite(Rg)) { Ui = r.map(x => isFinite(x) ? 0 : U); } }
      else { const g = r.reduce((a, b) => a + (isFinite(b) ? 1 / b : 0), 0); Rg = g ? 1 / g : Infinity; I = U * g; Ui = r.map(x => isFinite(x) ? U : U); Ii = r.map(x => isFinite(x) ? U / x : 0); }
    }
    return {I, Rg, Ui, Ii, P: Ii.map((x, k) => x * Ui[k])};
  }
  function draw() {
    const s = solve(); let g = '';
    const bright = k => loads[k].t === 'lamp' && !loads[k].broken ? s.P[k] / (unom * unom / loads[k].R) : 0;
    loads.forEach((l, k) => { if (l.t === 'lamp' && o.burn !== false && closed && !shorted && bright(k) > 2.2) l.broken = true; });
    const s2 = solve();
    const flow = closed && s2.I > 1e-6;
    if (!par) {
      g += SY.wire([[60, 150], [60, 45], [500, 45], [500, 255], [60, 255], [60, 150]]);
      if (o.short) g += `<path class="w${shorted ? '' : ' thin'}" ${shorted ? '' : 'stroke-dasharray="6 6"'} d="M110 45V14H450V45"/>`;
      if (flow) g += `<path class="flow${shorted ? ' hot' : ''}" d="M60 140V45H${shorted ? '110V14H450V45' : ''}500V255H60V160"/>`;
      g += SY.bat(60, 150) + `<text x="18" y="205" class="sm">U</text>`;
      const xs = n === 1 ? [280] : n === 2 ? [210, 370] : [170, 280, 390];
      loads.forEach((l, k) => {
        const x = xs[k];
        g += l.t === 'lamp' ? SY.lamp(x, 45, s2.Ii[k] > 0 ? bright(k) : 0) : SY.res(x, 45);
        if (l.broken) g += `<path class="w hot" d="M${x - 12} 33l24 24M${x + 12} 33l-24 24"/>`;
        g += `<text x="${x}" y="${o.short ? 92 : 86}" text-anchor="middle">${l.name}</text><text x="${x}" y="${o.short ? 108 : 102}" text-anchor="middle" class="sm">${fmtR(l.R)}</text>`;
      });
      g += SY.sw(280, 255, closed, 'main');
      g += `<text x="280" y="290" text-anchor="middle" class="sm">Schalter S</text>`;
    } else {
      const xs = n === 2 ? [290, 440] : [240, 350, 460];
      const xr = xs[n - 1];
      g += SY.wire([[60, 150], [60, 45], [xr, 45]]) + SY.wire([[60, 150], [60, 255], [xr, 255]]);
      xs.forEach(x => g += SY.wire([[x, 45], [x, 255]]) + `<circle cx="${x}" cy="45" r="4" class="fillw"/><circle cx="${x}" cy="255" r="4" class="fillw"/>`);
      if (flow) {
        loads.forEach((l, k) => { if (s2.Ii[k] > 0) g += `<path class="flow" d="M60 140V45H${xs[k]}V255H60V160"/>`; });
      }
      g += SY.bat(60, 150) + SY.sw(150, 45, closed, 'main') + `<text x="150" y="80" text-anchor="middle" class="sm">S</text>`;
      loads.forEach((l, k) => {
        const x = xs[k];
        if (o.branchSw) g += SY.sw(x, 95, l.on, 'b' + k, true) + `<text x="${x + 30}" y="100" class="sm">S${k + 1}</text>`;
        g += l.t === 'lamp' ? SY.lamp(x, 175, s2.Ii[k] > 0 ? bright(k) : 0) : SY.res(x, 175, true);
        if (l.broken) g += `<path class="w hot" d="M${x - 12} 163l24 24M${x + 12} 163l-24 24"/>`;
        g += `<text x="${x + 24}" y="172" >${l.name}</text><text x="${x + 24}" y="190" class="sm">${fmtR(l.R)}</text>`;
      });
    }
    svg.innerHTML = g;
    const show = o.show || ['U', 'I', 'R'];
    const cell = key => {
      const m = key.match(/^([UIP])(\d)$/);
      if (m) { const k = +m[2] - 1, v = m[1] === 'U' ? fmtU(s2.Ui[k]) : m[1] === 'I' ? fmtI(s2.Ii[k]) : fmtP(s2.P[k]); return [`${m[1]} an ${loads[k].name}`, v]; }
      return {U: ['Spannung U', fmtU(U)], I: ['Stromstärke I', fmtI(s2.I)], R: ['Gesamtwiderstand', fmtR(s2.Rg)], P: ['Leistung P', fmtP(U * s2.I)]}[key];
    };
    readout(ro, show.map(cell));
    $$('[data-o]', root).forEach(e => { const k = e.dataset.o; e.textContent = k === 'U' ? fmtU(U) : fmtR(loads[+k.slice(1)].R); });
    const fix = $('[data-k="fix"]', root); if (fix) fix.hidden = !loads.some(l => l.broken);
    st.innerHTML = !closed ? 'Der Stromkreis ist <b>offen</b> – es fließt kein Strom.'
      : shorted ? '<b class="bad">Kurzschluss!</b> Der Strom fließt am Verbraucher vorbei, die Stromstärke wird sehr groß, Leitungen werden heiß. Eine Sicherung würde jetzt auslösen.'
        : loads.some(l => l.broken) ? '<b class="bad">Die Lampe ist durchgebrannt</b> – die Spannung war zu groß. Der Stromkreis ist an dieser Stelle unterbrochen.'
          : s2.I < 1e-6 ? 'Der Stromkreis ist unterbrochen – es fließt kein Strom.' : (o.note ? o.note(s2, U, loads) : 'Der Stromkreis ist <b>geschlossen</b> – es fließt Strom.');
  }
  root.addEventListener('input', e => { const k = e.target.dataset.k; if (!k) return; if (k === 'U') U = +e.target.value; else loads[+k.slice(1)].R = +e.target.value; draw(); });
  root.addEventListener('click', e => {
    const sw = e.target.closest('[data-sw]'), b = e.target.closest('[data-k]');
    if (sw) { const id = sw.dataset.sw; if (id === 'main') closed = !closed; else loads[+id.slice(1)].on = !loads[+id.slice(1)].on; draw(); return; }
    if (b && b.dataset.k === 'short') { shorted = !shorted; b.classList.toggle('err', shorted); draw(); }
    if (b && b.dataset.k === 'fix') { loads.forEach(l => l.broken = false); draw(); }
  });
  root.addEventListener('keydown', e => { const sw = e.target.closest('[data-sw]'); if (sw && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); sw.dispatchEvent(new MouseEvent('click', {bubbles: true})); } });
  draw();
  return {set(p) { if ('U' in p) U = p.U; draw(); }, solve};
}

/* ---------- Liniendiagramm ----------
   plot(root, {x:[min,max], y:[min,max], xl, yl, xs, ys, series:[{pts:[[x,y]…], cls:'s0', name}], marks:[{x,y,t}], vl:[{x,t}], hl:[{y,t}], area:[[x,y]…]}) */
function plot(root, o = {}) {
  root.classList.add('plot');
  const W = 560, H = 320, L = 62, R = 18, T = 34, B = 50;
  function draw() {
    const [x0, x1] = o.x, [y0, y1] = o.y, X = v => L + (v - x0) / (x1 - x0) * (W - L - R), Y = v => H - B - (v - y0) / (y1 - y0) * (H - T - B);
    const xs = o.xs || niceStep((x1 - x0) / 6), ys = o.ys || niceStep((y1 - y0) / 5);
    let s = '';
    for (let v = Math.ceil(x0 / xs) * xs; v <= x1 + 1e-9; v += xs) s += `<line class="gl" x1="${X(v)}" x2="${X(v)}" y1="${T}" y2="${H - B}"/><text x="${X(v)}" y="${H - B + 18}" text-anchor="middle">${numDE(v, 2)}</text>`;
    for (let v = Math.ceil(y0 / ys) * ys; v <= y1 + 1e-9; v += ys) s += `<line class="gl" x1="${L}" x2="${W - R}" y1="${Y(v)}" y2="${Y(v)}"/><text x="${L - 7}" y="${Y(v) + 4}" text-anchor="end">${numDE(v, 2)}</text>`;
    if (o.area && o.area.length) s += `<path class="area" d="M${o.area.map(([a, b]) => `${X(a)},${Y(clamp(b, y0, y1))}`).join(' L')}Z"/>`;
    (o.bands || []).forEach(b => s += `<rect x="${X(b[0])}" width="${Math.max(0, X(b[1]) - X(b[0]))}" y="${H - B - 8}" height="8" fill="${b[2] || 'var(--bad)'}" opacity=".7"/>`);
    s += `<line class="ax" x1="${L}" x2="${W - R}" y1="${H - B}" y2="${H - B}"/><line class="ax" x1="${L}" x2="${L}" y1="${T - 6}" y2="${H - B}"/>`;
    (o.hl || []).forEach(h => s += `<line x1="${L}" x2="${W - R}" y1="${Y(h.y)}" y2="${Y(h.y)}" stroke="var(--ink-2)" stroke-dasharray="5 4"/><text x="${W - R - 4}" y="${Y(h.y) - 6}" text-anchor="end" class="lab">${h.t || ''}</text>`);
    (o.vl || []).forEach(h => s += `<line y1="${T}" y2="${H - B}" x1="${X(h.x)}" x2="${X(h.x)}" stroke="var(--ink-2)" stroke-dasharray="5 4"/><text x="${X(h.x) + 5}" y="${T + 14}" class="lab">${h.t || ''}</text>`);
    (o.series || []).forEach((se, i) => { if (se.pts.length) s += `<path class="${se.cls || 's' + i}" d="M${se.pts.map(([a, b]) => `${X(a).toFixed(1)},${Y(clamp(b, y0 - (y1 - y0) * .02, y1)).toFixed(1)}`).join(' L')}"/>`; });
    (o.marks || []).forEach(m => s += `<circle cx="${X(m.x)}" cy="${Y(m.y)}" r="5" fill="var(--accent)" stroke="var(--surface)" stroke-width="2"/>${m.t ? `<text x="${X(m.x) + 8}" y="${Y(m.y) - 8}" class="lab">${m.t}</text>` : ''}`);
    const named = (o.series || []).filter(se => se.name);
    named.forEach((se, i) => s += `<g class="lg"><path class="${se.cls}" d="M${W - R - 150 * (named.length - i) + 12} ${T - 24}h22"/><text x="${W - R - 150 * (named.length - i) + 40}" y="${T - 20}" class="lab">${se.name}</text></g>`);
    s += `<text x="${W - R}" y="${H - 8}" text-anchor="end" class="lab">${o.xl || ''}</text><text x="${L - 4}" y="${T - 20}" class="lab" text-anchor="start">↑ ${o.yl || ''}</text>`;
    root.innerHTML = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${o.title || 'Diagramm'}">${s}</svg>`;
  }
  draw();
  return {set(p) { Object.assign(o, p); draw(); }};
}

/* ---------- Getriebe ----------
   gears(root, {type:'zahnrad'|'riemen'|'kette', z1, z2, idler:false, n1:600, edit:true}) */
function gearPath(cx, cy, z, m) {
  const r = m * z / 2, ra = r + m * .9, rf = r - m * 1.1, s = 2 * Math.PI / z, P = (rr, a) => `${(cx + rr * Math.cos(a)).toFixed(1)},${(cy + rr * Math.sin(a)).toFixed(1)}`;
  let d = '';
  for (let i = 0; i < z; i++) { const a = i * s; d += `${i ? 'L' : 'M'}${P(rf, a + .05 * s)} L${P(rf, a + .4 * s)} L${P(ra, a + .58 * s)} L${P(ra, a + .87 * s)} L${P(rf, a + 1.05 * s)} `; }
  return d + 'Z';
}
function gears(root, o = {}) {
  let z1 = o.z1 || 12, z2 = o.z2 || 24, z3 = o.z3 || 10, n1 = o.n1 || 60, idl = !!o.idler, th = 0;
  const type = o.type || 'zahnrad', toothed = type !== 'riemen';
  const lab = toothed ? 'Zähne' : 'Ø';
  root.innerHTML = `<div class="tk-fig"><svg class="gear-svg" viewBox="0 0 600 300" role="img" aria-label="Getriebe"></svg></div>
    <div class="tk-row">${o.edit !== false ? `<label>Antrieb ${toothed ? 'z₁' : 'd₁'} <input type="range" data-k="z1" min="${toothed ? 8 : 20}" max="${toothed ? 40 : 120}" step="${toothed ? 1 : 10}" value="${z1}"> <span class="tk-val" data-o="z1"></span></label>
    <label>Abtrieb ${toothed ? 'z₂' : 'd₂'} <input type="range" data-k="z2" min="${toothed ? 8 : 20}" max="${toothed ? 40 : 120}" step="${toothed ? 1 : 10}" value="${z2}"> <span class="tk-val" data-o="z2"></span></label>` : ''}
    <label>Drehzahl n₁ <input type="range" data-k="n1" min="10" max="120" step="10" value="${n1}"> <span class="tk-val" data-o="n1"></span></label>
    ${type === 'zahnrad' && o.idlerBtn ? '<button class="btn" data-k="idl">Zwischenrad</button>' : ''}</div>
    <div class="tk-readout"></div>`;
  const svg = $('svg', root), ro = $('.tk-readout', root);
  function geom() {
    if (!toothed) { const r1 = z1 * .9, r2 = z2 * .9; return {r1, r2, x1: 160, x2: 160 + Math.max(r1 + r2 + 40, 260), y: 150}; }
    const m = Math.min(5.5, 230 / (z1 + z2 + (idl ? 2 * z3 : 0)));
    const r1 = m * z1 / 2, r2 = m * z2 / 2, r3 = m * z3 / 2;
    const x1 = 300 - (r1 + r2 + (idl ? 2 * r3 : 0)) / 2 + (r1 - r2) / 2 * 0, X1 = Math.max(r1 + 16, x1);
    if (type === 'kette') { return {m, r1, r2, x1: 170, x2: 170 + Math.max(r1 + r2 + 60, 250), y: 150}; }
    return {m, r1, r2, r3, x1: X1, x3: X1 + r1 + r3, x2: X1 + r1 + (idl ? 2 * r3 : 0) + r2, y: 150};
  }
  function belt(x1, r1, x2, r2, y) {
    const D = x2 - x1, b = Math.asin((r1 - r2) / D), sb = Math.sin(b), cb = Math.cos(b);
    const t1u = [x1 + r1 * sb, y - r1 * cb], t2u = [x2 + r2 * sb, y - r2 * cb], t2l = [x2 + r2 * sb, y + r2 * cb], t1l = [x1 + r1 * sb, y + r1 * cb];
    return `M${t1u} L${t2u} A${r2} ${r2} 0 ${b < 0 ? 1 : 0} 1 ${t2l} L${t1l} A${r1} ${r1} 0 ${b > 0 ? 1 : 0} 1 ${t1u}`;
  }
  function draw() {
    const G = geom(), i = z2 / z1, deg = a => a * 180 / Math.PI;
    let s = '';
    if (toothed && type === 'zahnrad') {
      const s1 = 2 * Math.PI / z1, s2 = 2 * Math.PI / z2, s3 = 2 * Math.PI / z3;
      const a1 = th - .73 * s1;
      if (idl) {
        const a3 = Math.PI - .23 * s3 - th * z1 / z3;
        const a2 = Math.PI - .23 * s2 + th * z1 / z2 + (z3 % 2 ? 0 : 0);
        s += `<path class="g" d="${gearPath(0, 0, z1, G.m)}" transform="translate(${G.x1} ${G.y}) rotate(${deg(a1)})"/><path class="g g2" d="${gearPath(0, 0, z3, G.m)}" transform="translate(${G.x3} ${G.y}) rotate(${deg(a3)})" opacity=".85"/><path class="g" d="${gearPath(0, 0, z2, G.m)}" transform="translate(${G.x2} ${G.y}) rotate(${deg(a2 + Math.PI + .5 * s2 - 2 * Math.PI / z3 * 0)})"/>`;
        s += `<circle class="hub" cx="${G.x3}" cy="${G.y}" r="5"/>`;
      } else {
        const a2 = Math.PI - .27 * s2 - th * z1 / z2;
        s += `<path class="g" d="${gearPath(0, 0, z1, G.m)}" transform="translate(${G.x1} ${G.y}) rotate(${deg(a1)})"/><path class="g" d="${gearPath(0, 0, z2, G.m)}" transform="translate(${G.x2} ${G.y}) rotate(${deg(a2)})"/>`;
      }
    } else {
      s += `<path class="belt" d="${belt(G.x1, G.r1, G.x2, G.r2, G.y)}" style="stroke-dashoffset:${(-th * G.r1).toFixed(1)}${type === 'kette' ? ';stroke-dasharray:4 3;stroke-width:7' : ''}"/>`;
      if (type === 'kette') s += `<path class="g" d="${gearPath(0, 0, z1, 2 * G.r1 / z1)}" transform="translate(${G.x1} ${G.y}) rotate(${deg(th)})"/><path class="g" d="${gearPath(0, 0, z2, 2 * G.r2 / z2)}" transform="translate(${G.x2} ${G.y}) rotate(${deg(th * z1 / z2)})"/>`;
      else s += `<circle class="g" cx="${G.x1}" cy="${G.y}" r="${G.r1}"/><circle class="g" cx="${G.x2}" cy="${G.y}" r="${G.r2}"/>`;
    }
    // Markierungen zum Mitzählen
    const dir2 = (toothed && type === 'zahnrad' && !idl) ? -1 : 1;
    const m1 = th, m2 = dir2 * th * z1 / z2;
    s += `<circle class="hub" cx="${G.x1}" cy="${G.y}" r="7"/><circle class="hub" cx="${G.x2}" cy="${G.y}" r="7"/>`;
    s += `<circle class="mark" cx="${G.x1 + G.r1 * .55 * Math.cos(m1)}" cy="${G.y + G.r1 * .55 * Math.sin(m1)}" r="5"/><circle class="mark" cx="${G.x2 + G.r2 * .55 * Math.cos(m2)}" cy="${G.y + G.r2 * .55 * Math.sin(m2)}" r="5"/>`;
    s += `<text x="${G.x1}" y="${G.y + G.r1 + 30}" text-anchor="middle">Antrieb</text><text x="${G.x2}" y="${G.y + G.r2 + 30}" text-anchor="middle">Abtrieb</text>`;
    const arr = (x, y, r, cw) => `<path d="M${x + r * .7} ${y - r * .7} A${r} ${r} 0 0 ${cw ? 1 : 0} ${x + r * .7 * (cw ? 1 : -1) * 0 + (cw ? r : -r) * .0 + x * 0 + (cw ? x + r : x - r) - x} ${y}" fill="none" stroke="var(--accent)" stroke-width="3"/>`;
    svg.innerHTML = s;
    const n2 = n1 / i, same = !(toothed && type === 'zahnrad') || idl;
    readout(ro, [['Übersetzung i', `${numDE(i, 2)} : 1`], ['Drehzahl n₂', numDE(n2, 1) + ' 1/min'], ['Drehrichtung', same ? 'gleich' : 'entgegengesetzt'], ['Drehmoment', i > 1 ? `${numDE(i, 2)}-fach` : i < 1 ? `nur ${numDE(i, 2)}-fach` : 'gleich'], [i > 1 ? 'Art' : i < 1 ? 'Art' : 'Art', i > 1 ? 'ins Langsame' : i < 1 ? 'ins Schnelle' : '1 : 1']]);
    $$('[data-o]', root).forEach(e => { const k = e.dataset.o; e.textContent = k === 'n1' ? n1 + ' 1/min' : toothed ? ({z1, z2})[k] : ({z1, z2})[k] + ' mm'; });
  }
  root.addEventListener('input', e => { const k = e.target.dataset.k; if (!k) return; if (k === 'z1') z1 = +e.target.value; if (k === 'z2') z2 = +e.target.value; if (k === 'n1') n1 = +e.target.value; draw(); });
  root.addEventListener('click', e => { const b = e.target.closest('[data-k="idl"]'); if (b) { idl = !idl; b.classList.toggle('ok', idl); draw(); } });
  draw();
  if (!RM.matches) animLoop(root, dt => { th += dt * n1 / 60 * 2 * Math.PI * .25; draw(); });
}

/* ---------- Würfelkörper mit Ansichten (Dreitafelbild) ----------
   cubes: [[x, y, z], …]  x nach rechts, y nach hinten, z nach oben */
function voxDims(c) { return [0, 1, 2].map(k => Math.max(...c.map(v => v[k])) + 1); }
function voxDraw(cubes, proj, sc = 34) {
  const kab = proj !== 'iso', c30 = Math.cos(Math.PI / 6), s30 = .5;
  const P = (x, y, z) => kab ? [x + .5 * y * Math.SQRT1_2, -z - .5 * y * Math.SQRT1_2] : [(x + y) * c30, (x - y) * s30 - z];
  const sorted = cubes.slice().sort((a, b) => kab ? (b[1] - a[1]) || (a[2] - b[2]) || (a[0] - b[0]) : (b[1] - a[1]) || (a[0] - b[0]) || (a[2] - b[2]));
  const has = new Set(cubes.map(v => v.join(',')));
  const H = (x, y, z) => has.has(`${x},${y},${z}`);
  let polys = [], minX = 1e9, minY = 1e9, maxX = -1e9, maxY = -1e9;
  const face = (pts, cls) => { const q = pts.map(p => P(...p)); q.forEach(([a, b]) => { minX = Math.min(minX, a); maxX = Math.max(maxX, a); minY = Math.min(minY, b); maxY = Math.max(maxY, b); }); polys.push([q, cls]); };
  for (const [x, y, z] of sorted) {
    if (!H(x, y - 1, z)) face([[x, y, z], [x + 1, y, z], [x + 1, y, z + 1], [x, y, z + 1]], 'f-front');
    if (!H(x, y, z + 1)) face([[x, y, z + 1], [x + 1, y, z + 1], [x + 1, y + 1, z + 1], [x, y + 1, z + 1]], 'f-top');
    if (!H(x + 1, y, z)) face([[x + 1, y, z], [x + 1, y + 1, z], [x + 1, y + 1, z + 1], [x + 1, y, z + 1]], 'f-side');
  }
  const pad = .3, w = (maxX - minX + 2 * pad) * sc, h = (maxY - minY + 2 * pad) * sc;
  const body = polys.map(([q, cls]) => `<polygon class="${cls}" points="${q.map(([a, b]) => `${((a - minX + pad) * sc).toFixed(1)},${((b - minY + pad) * sc).toFixed(1)}`).join(' ')}"/>`).join('');
  return `<svg viewBox="0 0 ${w.toFixed(0)} ${h.toFixed(0)}" role="img" aria-label="Körper">${body}</svg>`;
}
/* Ansicht: 'v' Vorderansicht, 'd' Draufsicht, 's' Seitenansicht von links. Kanten dort, wo die Tiefe wechselt. */
function voxView(cubes, which, sc = 22, dims) {
  const [X, Y, Z] = dims || voxDims(cubes);
  let W, Hh, depth;
  if (which === 'v') { W = X; Hh = Z; depth = (u, v) => { let d = Infinity; cubes.forEach(([x, y, z]) => { if (x === u && z === Hh - 1 - v) d = Math.min(d, y); }); return d; }; }
  else if (which === 'd') { W = X; Hh = Y; depth = (u, v) => { let d = Infinity; cubes.forEach(([x, y, z]) => { if (x === u && y === Hh - 1 - v) d = Math.min(d, -z); }); return d; }; }
  else { W = Y; Hh = Z; depth = (u, v) => { let d = Infinity; cubes.forEach(([x, y, z]) => { if (y === W - 1 - u && z === Hh - 1 - v) d = Math.min(d, x); }); return d; }; }
  const D = []; for (let v = 0; v < Hh; v++) { D.push([]); for (let u = 0; u < W; u++) D[v].push(depth(u, v)); }
  const p = 3; let s = '';
  for (let v = 0; v < Hh; v++) for (let u = 0; u < W; u++) if (isFinite(D[v][u])) s += `<rect x="${p + u * sc}" y="${p + v * sc}" width="${sc}" height="${sc}" stroke="none"/>`;
  const g = (u, v) => (u < 0 || v < 0 || u >= W || v >= Hh) ? Infinity : D[v][u];
  let e = '';
  for (let v = 0; v <= Hh; v++) for (let u = 0; u < W; u++) { const a = g(u, v - 1), b = g(u, v); if (a !== b && (isFinite(a) || isFinite(b))) e += `M${p + u * sc} ${p + v * sc}h${sc}`; }
  for (let u = 0; u <= W; u++) for (let v = 0; v < Hh; v++) { const a = g(u - 1, v), b = g(u, v); if (a !== b && (isFinite(a) || isFinite(b))) e += `M${p + u * sc} ${p + v * sc}v${sc}`; }
  return `<svg viewBox="0 0 ${W * sc + 2 * p} ${Hh * sc + 2 * p}" style="width:${(W * sc + 2 * p) * 1.6}px;max-width:100%" role="img" aria-label="Ansicht"><g class="vw">${s}<path class="ol" d="${e}"/></g></svg>`;
}
const VIEW_NAME = {v: 'Vorderansicht', d: 'Draufsicht', s: 'Seitenansicht von links'};
function voxel(root, o = {}) {
  let cubes = o.cubes, proj = o.proj || 'kab';
  const shown = {v: o.show !== false, d: o.show !== false, s: o.show !== false};
  root.innerHTML = `<div class="vox"><div><div class="tk-fig vx-body"></div><div class="tk-row"><span class="vx-seg"></span>${o.bodies ? '<span class="vx-bodies"></span>' : ''}</div></div>
    <div><div class="vox-views"></div><div class="tk-row">${['v', 's', 'd'].map(k => `<button class="btn" data-vw="${k}">${VIEW_NAME[k].split(' ')[0]} ${'zeigen'}</button>`).join('')}</div></div></div>`;
  function draw() {
    $('.vx-body', root).innerHTML = voxDraw(cubes, proj) + `<p class="tk-cap">${proj === 'iso' ? 'Isometrische Projektion' : 'Kabinettprojektion'}</p>`;
    const dims = voxDims(cubes);
    const fig = k => shown[k] ? `<figure>${voxView(cubes, k, 22, dims)}<figcaption>${VIEW_NAME[k]}</figcaption></figure>` : `<figure class="empty"><figcaption>${VIEW_NAME[k]} – ?</figcaption></figure>`;
    $('.vox-views', root).innerHTML = fig('v') + fig('s') + fig('d') + '<figure style="border:0;background:none"></figure>';
    $$('[data-vw]', root).forEach(b => b.textContent = (shown[b.dataset.vw] ? 'verdecken: ' : 'zeigen: ') + VIEW_NAME[b.dataset.vw].split(' ')[0]);
  }
  seg($('.vx-seg', root), [['kab', 'Kabinett'], ['iso', 'Isometrie']], v => { proj = v; if (cubes) draw(); }, proj);
  if (o.bodies) seg($('.vx-bodies', root), o.bodies.map((b, i) => [i, b.name]), v => { cubes = o.bodies[+v].cubes; draw(); }, 0);
  root.addEventListener('click', e => { const b = e.target.closest('[data-vw]'); if (b) { shown[b.dataset.vw] = !shown[b.dataset.vw]; draw(); } });
  if (o.bodies) cubes = o.bodies[0].cubes;
  draw();
}
/* Quiz: Welche Ansicht gehört zum Körper? bodies: [{name, cubes}] */
function voxQuiz(root, bodies, o = {}) {
  let ok = 0, n = 0;
  root.innerHTML = `<div class="vox"><div class="tk-fig vq-body"></div><div><h3 class="vq-q"></h3><div class="vox-opts"></div><p class="status" aria-live="polite"></p><div class="controls"><span class="score"></span><button class="btn primary" data-q="next">Nächster Körper →</button></div></div></div>`;
  function next() {
    const b = pick(bodies), k = pick(o.views || ['v', 'd', 's']);
    const right = voxView(b.cubes, k);
    const cand = new Map([[right, true]]);
    shuffle(bodies.slice()).forEach(x => ['v', 'd', 's'].forEach(kk => { const sv = voxView(x.cubes, kk); if (!cand.has(sv) && cand.size < 4 && Math.random() < .6) cand.set(sv, false); }));
    shuffle(bodies.slice()).forEach(x => ['v', 'd', 's'].forEach(kk => { const sv = voxView(x.cubes, kk); if (!cand.has(sv) && cand.size < 4) cand.set(sv, false); }));
    $('.vq-body', root).innerHTML = voxDraw(b.cubes, 'kab') + `<p class="tk-cap">Körper ${b.name}</p>`;
    $('.vq-q', root).textContent = `Welche Zeichnung ist die ${VIEW_NAME[k]}?`;
    $('.vox-opts', root).innerHTML = shuffle([...cand.entries()]).map(([sv, r]) => `<button data-r="${r ? 1 : 0}">${sv}</button>`).join('');
    $('.status', root).textContent = 'Tippe die passende Ansicht an.';
  }
  root.addEventListener('click', e => {
    if (e.target.closest('[data-q]')) return next();
    const b = e.target.closest('.vox-opts button'); if (!b || b.parentElement.dataset.done) return;
    b.parentElement.dataset.done = '';
    n++; const r = b.dataset.r === '1'; if (r) ok++;
    b.classList.add(r ? 'ok' : 'err'); if (!r) $('.vox-opts [data-r="1"]', root).classList.add('ok');
    $('.status', root).innerHTML = r ? '<b class="good">Richtig!</b>' : '<b class="bad">Nicht ganz.</b> Die grün markierte Zeichnung ist richtig.';
    $('.score', root).innerHTML = `Richtig: <b>${ok}</b> / ${n}`;
    setTimeout(() => delete b.parentElement.dataset.done, 0);
    $$('.vox-opts button', root).forEach(x => x.disabled = true);
  });
  next();
}

/* ---------- Messschieber mit Nonius (1/10 mm) ----------
   caliper(root, {quiz:true}) */
function caliper(root, o = {}) {
  let v = o.value ?? 23.4, ok = 0, n = 0;
  const s = 7.4, x0 = 60;
  root.innerHTML = `<div class="tk-fig"><svg class="ms-svg" viewBox="0 0 720 215" role="img" aria-label="Messschieber"></svg></div>
    ${o.quiz ? `<div class="tk-row"><label>Messwert <input type="text" inputmode="decimal" class="ms-in" style="width:6rem" autocomplete="off"> mm</label><button class="btn primary" data-c="check">Prüfen</button><button class="btn" data-c="solve">Lösung</button><button class="btn" data-c="new">Neues Werkstück</button><span class="score"></span></div>`
      : `<div class="tk-row"><label>Schieber <input type="range" min="0" max="70" step="0.1" value="${v}" class="ms-r"></label><button class="btn" data-c="read">Ablesung zeigen</button></div>`}
    <p class="status" aria-live="polite"></p>`;
  const svg = $('svg', root), st = $('.status', root);
  function draw(hl) {
    const xv = x0 + v * s; let g = '';
    g += `<path class="body" d="M${x0 - 40} 40H700V92H${x0}V200L${x0 - 18} 186L${x0 - 40} 120Z"/>`;
    for (let mm = 0; mm <= 85; mm++) { const x = x0 + mm * s; if (x > 698) break; const L = mm % 10 === 0 ? 20 : mm % 5 === 0 ? 14 : 9; g += `<line class="tick" x1="${x}" x2="${x}" y1="${92 - L}" y2="92"/>`; if (mm % 10 === 0) g += `<text x="${x}" y="${64}" text-anchor="middle">${mm / 10}</text>`; }
    g += `<text x="690" y="56" text-anchor="end" style="font-size:10px">cm</text>`;
    if (v > 0.05) g += `<rect class="work" x="${x0}" y="150" width="${v * s}" height="40"/>`;
    g += `<path class="slide" d="M${xv - 14} 92H${xv + 110}V138H${xv + 22}V200L${xv + 18} 200L${xv} 186V138H${xv - 14}Z"/>`;
    const k = Math.round((v - Math.floor(v + 1e-9)) * 10) % 10;
    for (let i = 0; i <= 10; i++) { const x = xv + i * .9 * s, L = i % 5 === 0 ? 16 : 10; g += `<line class="vtick${hl && i === k ? ' hit' : ''}" x1="${x}" x2="${x}" y1="92" y2="${92 + L}"/>`; if (i % 5 === 0) g += `<text class="vt" x="${x}" y="${92 + 28}" text-anchor="middle">${i}</text>`; }
    if (hl) { const x = xv + k * .9 * s; g += `<line class="hit" x1="${x}" x2="${x}" y1="70" y2="114"/>`; }
    svg.innerHTML = g;
  }
  function explain() { const mm = Math.floor(v + 1e-9), k = Math.round((v - mm) * 10) % 10; return `Hauptskala: Die Null des Nonius steht hinter <b>${mm} mm</b>. Nonius: Strich <b>${k}</b> deckt sich mit einem Strich der Hauptskala → <b>0,${k} mm</b>. Messwert: <b>${numDE(v, 1)} mm</b>.`; }
  function nv() { v = randInt(30, 650) / 10; draw(false); if ($('.ms-in', root)) { $('.ms-in', root).value = ''; $('.ms-in', root).className = 'ms-in'; } st.textContent = 'Lies den Messwert auf 1/10 mm genau ab.'; }
  root.addEventListener('input', e => { if (e.target.matches('.ms-r')) { v = +e.target.value; draw(false); st.innerHTML = ''; } });
  root.addEventListener('click', e => {
    const b = e.target.closest('[data-c]'); if (!b) return;
    if (b.dataset.c === 'read') { draw(true); st.innerHTML = explain(); }
    if (b.dataset.c === 'new') nv();
    if (b.dataset.c === 'solve') { draw(true); $('.ms-in', root).value = numDE(v, 1); st.innerHTML = explain(); }
    if (b.dataset.c === 'check') {
      const x = parseNum($('.ms-in', root).value); if (!isFinite(x)) { st.textContent = 'Trage zuerst einen Wert ein.'; return; }
      const good = Math.abs(x - v) < .05; n++; if (good) ok++;
      $('.ms-in', root).className = 'ms-in ' + (good ? 'ok' : 'err');
      st.innerHTML = good ? '<b class="good">Richtig gemessen!</b> ' + explain() : `<b class="bad">Noch nicht.</b> Lies zuerst die ganzen Millimeter links von der Nonius-Null ab, dann suche den Nonius-Strich, der sich mit einem Strich oben deckt.`;
      $('.score', root).innerHTML = `Richtig: <b>${ok}</b> / ${n}`;
    }
  });
  if (o.quiz) nv(); else draw(false);
  root.addEventListener('keydown', e => { if (e.key === 'Enter' && e.target.matches('.ms-in')) $('[data-c="check"]', root).click(); });
}

/* ---------- Widerstand mit Farbringen ---------- */
const RCOL = [['schwarz', '#111'], ['braun', '#7B3F12'], ['rot', '#D61F1F'], ['orange', '#F28A0F'], ['gelb', '#F5D20A'], ['grün', '#1E9B3A'], ['blau', '#1F5FD1'], ['violett', '#8A3FC6'], ['grau', '#8A8A8A'], ['weiß', '#F4F4F4']];
function resistorSVG(ohm) {
  const e = Math.floor(Math.log10(ohm)) - 1, d = Math.round(ohm / 10 ** e), a = Math.floor(d / 10), b = d % 10;
  const bands = [RCOL[a][1], RCOL[b][1], e < 0 ? '#C9A227' : RCOL[e][1], '#C9A227'];
  return `<svg class="res-svg" viewBox="0 0 300 70" style="max-width:300px" role="img" aria-label="Widerstand"><line class="lead" x1="0" x2="300" y1="35" y2="35"/><rect class="body" x="60" y="12" width="180" height="46" rx="20"/>${bands.map((c, i) => `<rect x="${[88, 116, 144, 206][i]}" y="12" width="14" height="46" fill="${c}" stroke="rgba(0,0,0,.25)"/>`).join('')}</svg>`;
}
function resistorBands(ohm) { const e = Math.floor(Math.log10(ohm)) - 1, d = Math.round(ohm / 10 ** e); return [RCOL[Math.floor(d / 10)][0], RCOL[d % 10][0], e < 0 ? 'gold' : RCOL[e][0]]; }
const E12 = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82];

/* ---------- Sicherheitszeichen (vereinfacht, Form und Farbe nach DIN EN ISO 7010) ---------- */
const PICTO = {
  brille: '<path d="M22 46h22v12a6 6 0 0 1-6 6h-10a6 6 0 0 1-6-6zM56 46h22v12a6 6 0 0 1-6 6h-10a6 6 0 0 1-6-6zM44 50q6-5 12 0M22 50l-8-4M78 50l8-4" fill="none" stroke-width="5" stroke-linejoin="round"/>',
  ohr: '<path d="M28 56q0-32 22-32t22 32" fill="none" stroke-width="6"/><rect x="20" y="48" width="16" height="26" rx="6" stroke="none"/><rect x="64" y="48" width="16" height="26" rx="6" stroke="none"/>',
  hand: '<path d="M38 54V28M46 50V22M54 50V22M62 54V30" stroke-width="7" stroke-linecap="round" fill="none"/><path d="M34 50h32v18q0 10-16 10t-16-10z" stroke="none"/><path d="M35 60l-11-11" stroke-width="7" stroke-linecap="round"/>',
  blitz: '<path d="M55 22 35 58h14l-8 26 26-38H52l9-24z" stroke="none"/>',
  heiss: '<path d="M38 66q6-8 0-16t0-16M50 66q6-8 0-16t0-16M62 66q6-8 0-16t0-16" fill="none" stroke-width="4.5"/><path d="M28 74h44" stroke-width="5"/>',
  kreuz: '<path d="M42 22h16v20h20v16H58v20H42V58H22V42h20z" stroke="none"/>',
  loescher: '<rect x="40" y="36" width="20" height="46" rx="7" stroke="none"/><rect x="44" y="26" width="12" height="10" stroke="none"/><path d="M56 30q18 0 16 18" fill="none" stroke-width="4"/>',
  tuer: '<path d="M58 22h18v58H58z" fill="none" stroke-width="5"/><path d="M18 52h28M36 41l11 11-11 11" fill="none" stroke-width="6"/>',
  schuh: '<path d="M30 28h18v30l24 4q8 2 7 12H30z" stroke="none"/>',
  flamme: '<path d="M50 20q18 22 12 40q-3 16-12 16q-12 0-12-16q0-12 6-16q0 10 6 10q4-14 0-34z" stroke="none"/>',
  becher: '<path d="M34 38h28v32q0 8-8 8H42q-8 0-8-8z" stroke="none"/><path d="M62 46h6q6 0 6 8t-6 8h-6" fill="none" stroke-width="5"/>',
  ausruf: '<path d="M46 34h8l-1 30h-6z" stroke="none"/><circle cx="50" cy="72" r="5" stroke="none"/>',
  haar: '<circle cx="48" cy="36" r="13" stroke="none"/><path d="M36 38q-4 22 10 30M60 38q4 22-10 30" fill="none" stroke-width="5"/><path d="M30 80q18-14 36 0" fill="none" stroke-width="6"/>'
};
function signSVG(kind, picto) {
  const ink = kind === 'gebot' || kind === 'rettung' || kind === 'brand' ? '#fff' : '#111';
  const p = `<g fill="${ink}" stroke="${ink}">${PICTO[picto] || ''}</g>`;
  if (kind === 'gebot') return `<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="var(--gebot)"/>${p}</svg>`;
  if (kind === 'verbot') return `<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="43" fill="#fff" stroke="var(--verbot)" stroke-width="9"/>${p}<path d="M20 20 80 80" stroke="var(--verbot)" stroke-width="9"/></svg>`;
  if (kind === 'warn') return `<svg viewBox="0 0 100 100"><path d="M50 8 95 88H5z" fill="var(--warn)" stroke="#111" stroke-width="6" stroke-linejoin="round"/><g transform="translate(12 18) scale(.76)">${p}</g></svg>`;
  if (kind === 'rettung') return `<svg viewBox="0 0 100 100"><rect x="3" y="3" width="94" height="94" fill="var(--rettung)"/>${p}</svg>`;
  return `<svg viewBox="0 0 100 100"><rect x="3" y="3" width="94" height="94" fill="var(--verbot)"/>${p}</svg>`;
}
/* Zeichenwand: signs(root, [{k:'gebot', p:'brille', n:'Augenschutz benutzen', t:'…'}], {hide:true}) */
function signs(root, list, o = {}) {
  root.classList.add('signs');
  root.innerHTML = list.map((s, i) => `<button class="sign" data-i="${i}" style="cursor:pointer;font:inherit;color:inherit">${signSVG(s.k, s.p)}<b>${o.hide ? '?' : s.n}</b><span class="sn" ${o.hide ? 'hidden' : ''}>${s.t || ''}</span></button>`).join('');
  root.addEventListener('click', e => { const b = e.target.closest('.sign'); if (!b) return; const s = list[+b.dataset.i]; $('b', b).textContent = s.n; $('.sn', b).hidden = false; });
}

/* ---------- Logikgatter ----------
   logic(root, {type:'UND'|'ODER'|'NICHT', switches:true}) */
function logic(root, o = {}) {
  const T = o.type || 'UND', one = T === 'NICHT';
  let A = 0, B = 0;
  const f = (a, b) => T === 'UND' ? a & b : T === 'ODER' ? a | b : 1 - a;
  root.innerHTML = `<div class="cols-2"><div class="tk-fig"><svg class="gate-svg" viewBox="0 0 420 220" role="img" aria-label="Logikgatter ${T}"></svg><p class="tk-cap">Schaltzeichen ${T}</p></div>
    ${o.switches !== false ? '<div class="tk-fig"><svg class="sch" viewBox="0 0 420 220" role="img" aria-label="Schalter-Schaltung"></svg><p class="tk-cap">Gleiche Funktion mit Schaltern</p></div>' : ''}</div>
    <table class="tt" style="margin-top:.8rem"><thead><tr><th>A</th>${one ? '' : '<th>B</th>'}<th>Y</th></tr></thead><tbody>${(one ? [[0], [1]] : [[0, 0], [0, 1], [1, 0], [1, 1]]).map(r => `<tr data-r="${r.join('')}"><td>${r[0]}</td>${one ? '' : `<td>${r[1]}</td>`}<td>${f(r[0], r[1] || 0)}</td></tr>`).join('')}</tbody></table>`;
  const gs = $('.gate-svg', root), ss = $('svg.sch', root);
  function draw() {
    const Y = f(A, B), on = v => v ? ' on' : '';
    const sym = T === 'UND' ? '&amp;' : T === 'ODER' ? '≥1' : '1';
    let g = `<g class="in${on(A)}" data-in="A" tabindex="0" role="button" aria-label="Eingang A umschalten"><rect x="20" y="${one ? 92 : 42}" width="56" height="36"/><text x="48" y="${one ? 118 : 68}" text-anchor="middle">A=${A}</text></g>`;
    g += `<path class="w${on(A)}" d="M76 ${one ? 110 : 60}H170"/>`;
    if (!one) g += `<g class="in${on(B)}" data-in="B" tabindex="0" role="button" aria-label="Eingang B umschalten"><rect x="20" y="142" width="56" height="36"/><text x="48" y="168" text-anchor="middle">B=${B}</text></g><path class="w${on(B)}" d="M76 160H170"/>`;
    g += `<rect class="g" x="170" y="30" width="90" height="160"/><text x="215" y="${one ? 78 : 118}" text-anchor="middle">${sym}</text>`;
    if (one) g += `<circle class="g" cx="268" cy="110" r="8"/>`;
    g += `<path class="w${on(Y)}" d="M${one ? 276 : 260} 110H340"/><circle class="lamp${on(Y)}" cx="365" cy="110" r="24"/><text x="365" y="118" text-anchor="middle">Y=${Y}</text>`;
    gs.innerHTML = g;
    if (ss) {
      let s = SY.wire([[40, 120], [40, 30], [380, 30], [380, 190], [40, 190], [40, 120]]) + SY.bat(40, 120);
      const sw = (x, y, cl, lab, v) => `<rect x="${x - 26}" y="${y - 6}" width="52" height="12" fill="var(--surface)"/><circle class="sym" cx="${x - 17}" cy="${y}" r="3.5"/><circle class="sym" cx="${x + 17}" cy="${y}" r="3.5"/><path class="w" d="M${x - 17} ${y}L${cl ? `${x + 17} ${y}` : `${x + 13} ${y - 17}`}"/><text x="${x}" y="${y + 26}" text-anchor="middle" class="sm">${lab}</text>`;
      if (T === 'UND') s += sw(150, 30, A, 'Schalter A') + sw(260, 30, B, 'Schalter B');
      else if (T === 'ODER') s += SY.wire([[120, 30], [120, 90], [300, 90], [300, 30]]) + `<rect x="160" y="22" width="100" height="16" fill="var(--surface)"/>` + SY.wire([[120, 30], [180, 30]]) + SY.wire([[240, 30], [300, 30]]) + sw(210, 30, A, '') + sw(210, 90, B, 'A oben, B unten') + `<circle cx="120" cy="30" r="4" class="fillw"/><circle cx="300" cy="30" r="4" class="fillw"/>`;
      else s += sw(200, 30, !A, 'Öffner A (geschlossen, solange A=0)');
      s += SY.lamp(380, 120, Y) + `<text x="345" y="125" text-anchor="end">Y</text>`;
      ss.innerHTML = s;
    }
    $$('tr[data-r]', root).forEach(tr => tr.classList.toggle('cur', tr.dataset.r === (one ? `${A}` : `${A}${B}`)));
  }
  const tog = el => { if (el.dataset.in === 'A') A = 1 - A; else B = 1 - B; draw(); };
  root.addEventListener('click', e => { const el = e.target.closest('[data-in]'); if (el) tog(el); });
  root.addEventListener('keydown', e => { const el = e.target.closest('[data-in]'); if (el && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); tog(el); } });
  draw();
}

/* ---------- Regelkreis: Raumtemperatur mit Zweipunktregler ---------- */
function regel(root, o = {}) {
  let mode = o.mode || 'regel', soll = 21, level = 60, win = false, T = 16, heat = 0, t = 0, hist = [], hb = [];
  const OUT = 5;
  root.innerHTML = `<div class="tk-row"><span class="rg-mode"></span><label>Sollwert <input type="range" data-k="soll" min="15" max="25" step="0.5" value="${soll}"> <span class="tk-val" data-o="soll"></span></label>
    <label class="rg-lvl">Heizstufe <input type="range" data-k="lvl" min="0" max="100" step="10" value="${level}"> <span class="tk-val" data-o="lvl"></span></label>
    <button class="btn" data-k="win">Fenster öffnen</button><button class="btn" data-k="reset">Neustart</button></div>
    <div class="cols-2"><div class="rg-plot"></div><div><div class="tk-readout"></div><p class="status" aria-live="polite"></p></div></div>`;
  const pl = plot($('.rg-plot', root), {x: [0, 120], y: [0, 30], xl: 't in min', yl: 'ϑ in °C', ys: 5, xs: 20, series: []});
  const ro = $('.tk-readout', root), st = $('.status', root);
  seg($('.rg-mode', root), [['regel', 'Regelung'], ['steuer', 'Steuerung']], v => { mode = v; $('.rg-lvl', root).hidden = v === 'regel'; }, mode);
  function stepSim() {
    if (mode === 'regel') { if (T < soll - .5) heat = 1; else if (T > soll + .5) heat = 0; }
    else heat = level / 100;
    T += .3 * heat - .013 * (T - OUT) * (win ? 3.2 : 1);
    t++; hist.push([t, T]); hb.push(heat);
    if (hist.length > 120) { hist.shift(); hb.shift(); }
  }
  function draw() {
    const off = Math.max(0, t - 120);
    const bands = []; hb.forEach((h, k) => { if (h > 0) bands.push([k + 1 + 0, k + 2, mode === 'regel' ? 'var(--bad)' : `color-mix(in srgb,var(--bad) ${Math.round(h * 100)}%,transparent)`]); });
    pl.set({x: [0, 120], series: [{pts: hist.map(([a, b]) => [a - off, b]), cls: 's0', name: 'Istwert'}, ...(mode === 'regel' ? [{pts: [[0, soll], [120, soll]], cls: 's1', name: 'Sollwert'}] : [])], bands});
    readout(ro, [['Istwert', numDE(T, 1) + ' °C'], ['Sollwert', mode === 'regel' ? numDE(soll, 1) + ' °C' : '—'], ['Heizung', mode === 'regel' ? (heat ? 'AN' : 'AUS') : level + ' %'], ['Störgröße', win ? 'Fenster offen' : 'keine']]);
    st.innerHTML = mode === 'regel' ? 'Der Temperatursensor misst ständig den <b>Istwert</b>. Der Regler vergleicht ihn mit dem <b>Sollwert</b> und schaltet die Heizung an oder aus. Der rote Balken zeigt, wann geheizt wird.'
      : 'Die Heizung läuft mit fester Stufe. Niemand misst die Temperatur – eine <b>Störung</b> wie ein offenes Fenster wird nicht ausgeglichen.';
    $$('[data-o]', root).forEach(e => e.textContent = e.dataset.o === 'soll' ? numDE(soll, 1) + ' °C' : level + ' %');
  }
  root.addEventListener('input', e => { if (e.target.dataset.k === 'soll') soll = +e.target.value; if (e.target.dataset.k === 'lvl') level = +e.target.value; draw(); });
  root.addEventListener('click', e => { const b = e.target.closest('[data-k]'); if (!b) return; if (b.dataset.k === 'win') { win = !win; b.textContent = win ? 'Fenster schließen' : 'Fenster öffnen'; b.classList.toggle('err', win); } if (b.dataset.k === 'reset') { T = 16; t = 0; hist = []; hb = []; } draw(); });
  let acc = 0;
  animLoop(root, dt => { acc += dt; if (acc > .12) { acc = 0; stepSim(); draw(); } });
  draw();
}

/* ---------- Energieflussbild ----------
   sankey(root, {inName, outs:[{n, v, use:true}], unit:'%'}) → {set(outs)} */
function sankey(root, o = {}) {
  root.classList.add('tk-fig');
  function draw() {
    const outs = o.outs || [], tot = outs.reduce((a, x) => a + x.v, 0), H = 170, k = H / (tot || 1), x0 = 30, xs = 230, y0 = 40;
    if (!tot) { root.innerHTML = ''; return; }
    let s = `<rect class="in" x="${x0}" y="${y0}" width="${xs - x0}" height="${H}"/><text x="${x0 + 8}" y="${y0 - 10}">${o.inName || 'zugeführte Energie'}: ${numDE(tot, 1)} ${o.unit || '%'}</text>`;
    let y = y0, ly = y0 + H + 6;
    const use = outs.filter(x => x.use), loss = outs.filter(x => !x.use);
    use.forEach(u => { const h = u.v * k, big = h >= 24; s += `<path class="use" d="M${xs} ${y}H560l20 ${h / 2}-20 ${h / 2}H${xs}Z"/><text x="${xs + 20}" y="${big ? y + h / 2 + 5 : y - 7}" style="fill:${big ? '#fff' : 'var(--good)'}">${u.n}: ${numDE(u.v, 1)} ${o.unit || '%'}</text>`; y += h; });
    const L = loss.length, R = 18, yb = y0 + H + 46;
    loss.forEach((u, i) => {
      const h = Math.max(u.v * k, 1.5), xc = xs + 30 + (L - 1 - i) * 105;
      s += `<path class="loss" d="M${xs} ${y}H${xc}A${R + h} ${R + h} 0 0 1 ${xc + R + h} ${y + R + h}V${yb}H${xc + R + h + 7}L${xc + R + h / 2} ${yb + 16}L${xc + R - 7} ${yb}H${xc + R}V${y + R + h}A${R} ${R} 0 0 0 ${xc} ${y + h}H${xs}Z"/>`;
      s += `<text x="${xc + R + h / 2}" y="${yb + 34}" text-anchor="middle" style="font-size:13px">${u.n}</text><text x="${xc + R + h / 2}" y="${yb + 50}" text-anchor="middle" style="font-size:13px">${numDE(u.v, 1)} ${o.unit || '%'}</text>`;
      y += h;
    });
    root.innerHTML = `<svg class="sankey" viewBox="0 0 600 ${yb + 60}" role="img" aria-label="Energieflussbild">${s}</svg>`;
  }
  draw();
  return {set(outs) { o.outs = outs; draw(); }};
}

/* ---------- Profile und Biegung ---------- */
const PROFILES = [
  {id: 'flach', n: 'Flachstab liegend', k: 1, d: 'M10 34h60v8H10z'}, {id: 'hoch', n: 'Flachstab hochkant', k: 100, d: 'M36 4h8v60h-8z'},
  {id: 'winkel', n: 'Winkelprofil (L)', k: 40, d: 'M20 6h8v50h40v8H20z'}, {id: 'u', n: 'U-Profil', k: 55, d: 'M16 8h48v8H24v36h40v8H16z'},
  {id: 't', n: 'T-Profil', k: 38, d: 'M10 6h60v8H44v48h-8V14H10z'}, {id: 'rohr', n: 'Vierkantrohr', k: 105, d: 'M14 6h52v52H14zM20 12v40h40V12z'},
  {id: 'i', n: 'I-Profil (Doppel-T)', k: 210, d: 'M12 4h56v8H44v40h24v8H12v-8h24V12H12z'}
];
function beam(root, o = {}) {
  let p = PROFILES[0], F = o.F ?? 50;
  root.innerHTML = `<div class="tk-fig"><svg class="beam-svg" viewBox="0 0 600 240" role="img" aria-label="Biegeversuch"></svg></div>
    <div class="tk-row"><span class="bm-seg"></span></div><div class="tk-row"><label>Last F <input type="range" min="0" max="100" step="5" value="${F}" data-k="F"> <span class="tk-val"></span></label></div><div class="tk-readout"></div>`;
  const svg = $('svg', root), ro = $('.tk-readout', root);
  function draw() {
    const f = Math.min(80, F / p.k * 1.6 * 2);
    let s = `<path class="sup" d="M40 130l-20 30h40zM460 130l-20 30h40z"/>`;
    s += `<path class="beam" d="M30 ${118}Q250 ${118 + 2 * f} 470 118v12Q250 ${130 + 2 * f} 30 130z"/>`;
    s += `<rect class="load" x="230" y="${70 + f}" width="40" height="46"/><text x="250" y="${64 + f}" text-anchor="middle">F</text>`;
    s += `<g transform="translate(505 60)"><rect x="-6" y="-6" width="92" height="82" fill="var(--surface-2)"/><path class="prof" d="${p.d}" fill-rule="evenodd"/></g><text x="550" y="165" text-anchor="middle" style="font-size:12px">Querschnitt</text>`;
    s += `<text x="250" y="215" text-anchor="middle">Durchbiegung: ${numDE(f / 8, 1)} mm (Modell)</text>`;
    svg.innerHTML = s;
    $('.tk-val', root).textContent = F + ' N';
    readout(ro, [['Profil', p.n], ['Steifigkeit', `${p.k}-fach`], ['Material', 'gleich viel']]);
  }
  seg($('.bm-seg', root), PROFILES.map((x, i) => [i, x.n.split(' ')[0] + (x.id === 'hoch' ? ' hochkant' : x.id === 'flach' ? ' liegend' : '')]), v => { p = PROFILES[+v]; draw(); }, 0);
  root.addEventListener('input', e => { if (e.target.dataset.k === 'F') { F = +e.target.value; draw(); } });
}
/* Rahmen gegen Dreieck: truss(root) */
function truss(root) {
  let F = 0, dg = 'none';
  root.innerHTML = `<div class="tk-fig"><svg class="beam-svg" viewBox="0 0 600 260" role="img" aria-label="Rahmen"></svg></div>
    <div class="tk-row"><span class="tr-seg"></span><label>Kraft von links <input type="range" min="0" max="100" step="5" value="0"> <span class="tk-val"></span></label></div><p class="status" aria-live="polite"></p>`;
  const svg = $('svg', root), st = $('.status', root);
  function draw() {
    const d = dg === 'none' ? F * .9 : F * .04;
    const A = [180, 220], B = [420, 220], C = [420 + d, 40], D = [180 + d, 40];
    let s = `<path d="M150 228H450" stroke="var(--ink-2)" stroke-width="4"/>`;
    const bar = (p, q, c = 'bar') => `<line class="${c}" x1="${p[0]}" y1="${p[1]}" x2="${q[0]}" y2="${q[1]}"/>`;
    s += bar(A, B) + bar(B, C) + bar(C, D) + bar(D, A);
    if (dg === 'ab') s += bar(D, B, 'druck') + `<text x="${300 + d / 2}" y="120" fill="var(--bad)" style="fill:var(--bad)">Druck</text>`;
    if (dg === 'ba') s += bar(A, C, 'zug') + `<text x="${300 + d / 2}" y="120" style="fill:var(--e)">Zug</text>`;
    [A, B, C, D].forEach(p => s += `<circle class="node" cx="${p[0]}" cy="${p[1]}" r="8"/>`);
    if (F) s += `<path d="M${D[0] - 90} 40h${70}" stroke="var(--accent)" stroke-width="6"/><path d="M${D[0] - 22} 28l14 12-14 12z" fill="var(--accent)"/><text x="${D[0] - 80}" y="28">F</text>`;
    svg.innerHTML = s;
    $('.tk-val', root).textContent = F + ' %';
    st.innerHTML = dg === 'none' ? (F ? 'Das Viereck verschiebt sich zu einem Parallelogramm – die Gelenke drehen sich, der Rahmen ist <b>nicht stabil</b>.' : 'Ein Rahmen aus vier Stäben mit Gelenken.') : 'Die Diagonale teilt das Viereck in zwei <b>Dreiecke</b>. Ein Dreieck lässt sich nicht verschieben, ohne dass ein Stab länger oder kürzer wird – der Rahmen ist <b>stabil</b>.';
  }
  seg($('.tr-seg', root), [['none', 'ohne Diagonale'], ['ab', 'Diagonale ↘'], ['ba', 'Diagonale ↗']], v => { dg = v; draw(); });
  root.addEventListener('input', e => { F = +e.target.value; draw(); });
}

/* ---------- Transistor-Schaltungen ----------
   transistorSim(root, {mode:'dunkel'|'hell'|'waerme'}) */
function transistorSim(root, o = {}) {
  let mode = o.mode || 'dunkel', lux = 300, temp = 20, Rf = o.Rf || 10000;
  const UB = 9;
  root.innerHTML = `<div class="cols-2"><div class="tk-fig"><svg class="sch" viewBox="0 0 440 330" role="img" aria-label="Transistorschaltung"></svg></div>
    <div>${o.modes !== false ? '<div class="tk-row"><span class="tr-mode"></span></div>' : ''}<div class="tk-row"><label class="tx-l">Helligkeit <input type="range" data-k="lux" min="0" max="3" step="0.05" value="${Math.log10(lux)}"> <span class="tk-val" data-o="lux"></span></label>
    <label class="tx-t">Temperatur <input type="range" data-k="temp" min="0" max="60" step="1" value="${temp}"> <span class="tk-val" data-o="temp"></span></label>
    <label>Poti R₁ <input type="range" data-k="rf" min="1000" max="47000" step="1000" value="${Rf}"> <span class="tk-val" data-o="rf"></span></label></div>
    <div class="tk-readout"></div><p class="status" aria-live="polite"></p></div></div>`;
  const svg = $('svg', root), ro = $('.tk-readout', root), st = $('.status', root);
  function sensorR() { return mode === 'waerme' ? 10000 * Math.exp(3950 * (1 / (temp + 273.15) - 1 / 298.15)) : 400000 * Math.pow(Math.max(lux, 1), -0.85); }
  function draw() {
    const Rs = sensorR(), sensorUp = mode !== 'dunkel';
    const Rup = sensorUp ? Rs : Rf, Rlo = sensorUp ? Rf : Rs;
    const Udiv = UB * Rlo / (Rup + Rlo), on = Udiv >= 0.7, Ube = Math.min(Udiv, 0.75);
    const sens = (x, y) => mode === 'waerme' ? `${SY.res(x, y, true)}<path class="thin" d="M${x - 16} ${y + 18}l8 0 16 -36"/><text x="${x - 48}" y="${y + 5}" class="sm">−ϑ</text>`
      : `${SY.res(x, y, true)}<path class="thin" d="M${x - 40} ${y - 26}l20 14m-8 -1 8 1-3 -8M${x - 40} ${y - 8}l20 14m-8 -1 8 1-3 -8"/>`;
    const poti = (x, y) => `${SY.res(x, y, true)}<path class="thin" d="M${x - 16} ${y + 20}L${x + 16} ${y - 20}m-8 0 8 0 0 8"/>`;
    let s = SY.wire([[40, 30], [400, 30]]) + SY.wire([[40, 300], [400, 300]]) + `<text x="20" y="26">+9 V</text><text x="20" y="296">0 V</text>`;
    s += SY.wire([[100, 30], [100, 300]]) + SY.wire([[100, 165], [250, 165]]) + `<circle cx="100" cy="165" r="4" class="fillw"/>`;
    s += sensorUp ? sens(100, 95) + poti(100, 235) : poti(100, 95) + sens(100, 235);
    s += `<text x="125" y="${sensorUp ? 100 : 240}" class="sm">${mode === 'waerme' ? 'NTC' : 'LDR'}</text><text x="125" y="${sensorUp ? 240 : 100}" class="sm">R₁</text>`;
    s += SY.res(190, 165) + `<text x="190" y="150" text-anchor="middle" class="sm">R_B</text>`;
    // Transistor
    s += `<circle cx="285" cy="165" r="30" fill="var(--surface)" stroke="var(--wire)" stroke-width="2"/><path class="w" d="M270 145V185M250 165H270M270 155L300 135V100M270 175L300 195V300"/><path d="M300 195l-12 -2 6 -8z" class="fillw"/>`;
    s += `<text x="315" y="172" class="sm">T</text><text x="303" y="128" class="sm">C</text><text x="303" y="215" class="sm">E</text><text x="246" y="158" class="sm">B</text>`;
    s += SY.wire([[300, 30], [300, 100]]) + SY.res(300, 60, true) + `<text x="318" y="64" class="sm">R_V</text>`;
    s += `<g transform="translate(0 0)">${SY.led(300, 112, on, true)}</g>`;
    if (on) s += `<path class="flow" d="M300 40V300"/><path class="flow" style="stroke-width:2" d="M110 165H265"/>`;
    svg.innerHTML = s;
    $$('[data-o]', root).forEach(e => { const k = e.dataset.o; e.textContent = k === 'lux' ? numDE(lux, 0) + ' lx' : k === 'temp' ? temp + ' °C' : fmtR(Rf); });
    $('.tx-l', root).hidden = mode === 'waerme'; $('.tx-t', root).hidden = mode !== 'waerme';
    readout(ro, [[mode === 'waerme' ? 'R des NTC' : 'R des LDR', fmtR(Rs)], ['Spannung an B–E', numDE(Ube, 2) + ' V'], ['Transistor', on ? 'leitet' : 'sperrt'], ['LED', on ? 'AN' : 'AUS']]);
    st.innerHTML = on ? `Am Spannungsteiler liegen mindestens <b>0,7 V</b> zwischen Basis und Emitter. Ein kleiner Basisstrom fließt – der Transistor <b>schaltet durch</b>, die LED leuchtet.` : `Zwischen Basis und Emitter liegen weniger als <b>0,7 V</b>. Es fließt kein Basisstrom, der Transistor <b>sperrt</b>.`;
  }
  if (o.modes !== false) seg($('.tr-mode', root), [['dunkel', 'Dunkelschaltung'], ['hell', 'Hellschaltung'], ['waerme', 'Wärmeschaltung']], v => { mode = v; draw(); }, mode);
  root.addEventListener('input', e => { const k = e.target.dataset.k; if (k === 'lux') lux = 10 ** +e.target.value; if (k === 'temp') temp = +e.target.value; if (k === 'rf') Rf = +e.target.value; draw(); });
  draw();
}

/* ---------- Kondensator: Laden und Entladen ---------- */
function rcSim(root, o = {}) {
  let R = o.R || 47, C = o.C || 470, U = 0, mode = 0, t = 0, pts = [];
  const UB = 9, TH = o.th ?? 2;
  root.innerHTML = `<div class="tk-row"><label>Widerstand R <input type="range" data-k="R" min="10" max="100" step="1" value="${R}"> <span class="tk-val" data-o="R"></span></label><label>Kapazität C <input type="range" data-k="C" min="100" max="2200" step="100" value="${C}"> <span class="tk-val" data-o="C"></span></label></div>
    <div class="tk-row"><button class="btn primary" data-k="lad">Taster drücken: laden</button><button class="btn" data-k="ent">Taster loslassen: entladen</button></div>
    <div class="cols-2"><div class="rc-plot"></div><div class="dev"><div class="lampbig">LED</div><div><div class="tk-readout"></div><p class="status" aria-live="polite"></p></div></div></div>`;
  const pl = plot($('.rc-plot', root), {x: [0, 30], y: [0, 10], xl: 't in s', yl: 'U in V', xs: 5, ys: 2, hl: [{y: TH, t: 'Schaltschwelle'}], series: []});
  const ro = $('.tk-readout', root), st = $('.status', root), lamp = $('.lampbig', root);
  const tau = () => R * 1000 * C * 1e-6;
  function draw() {
    pl.set({series: [{pts, cls: 's0', name: 'Spannung am Kondensator'}]});
    lamp.classList.toggle('on', U > TH);
    readout(ro, [['τ = R · C', numDE(tau(), 1) + ' s'], ['U am Kondensator', numDE(U, 2) + ' V'], ['Leuchtdauer ≈', numDE(tau() * Math.log(UB / TH), 1) + ' s']]);
    $$('[data-o]', root).forEach(e => e.textContent = e.dataset.o === 'R' ? R + ' kΩ' : C + ' µF');
    st.innerHTML = mode === 1 ? 'Der Kondensator wird über den Taster schnell <b>geladen</b>.' : mode === -1 ? `Der Kondensator <b>entlädt</b> sich über den Widerstand. Die LED leuchtet, bis die Spannung unter ${TH} V fällt.` : 'Drücke den Taster.';
  }
  root.addEventListener('input', e => { const k = e.target.dataset.k; if (k === 'R') R = +e.target.value; if (k === 'C') C = +e.target.value; draw(); });
  root.addEventListener('click', e => { const b = e.target.closest('[data-k]'); if (!b) return; if (b.dataset.k === 'lad') { mode = 1; t = 0; pts = [[0, U]]; } else if (mode === 1) { mode = -1; } draw(); });
  animLoop(root, dt => {
    if (!mode || t > 30) return;
    t += dt;
    if (mode === 1) U += (UB - U) * (1 - Math.exp(-dt / 0.15));
    else U *= Math.exp(-dt / tau());
    pts.push([t, U]); draw();
  });
  draw();
}

/* ---------- Stückkosten: Einzel- gegen Serienfertigung ---------- */
function costSim(root, o = {}) {
  const a = o.a, b = o.b, nMax = o.nMax || 100;
  let n = o.n || 10;
  root.innerHTML = `<div class="tk-row"><label>Stückzahl <input type="range" min="1" max="${nMax}" step="1" value="${n}"> <span class="tk-val"></span></label></div><div class="cols-2"><div class="cs-plot"></div><div><div class="tk-readout"></div><p class="status" aria-live="polite"></p></div></div>`;
  const cost = (m, k) => m.fix + m.var * k, be = (b.fix - a.fix) / (a.var - b.var);
  const pl = plot($('.cs-plot', root), {x: [0, nMax], y: [0, Math.max(cost(a, nMax), cost(b, nMax)) * 1.05], xl: 'Stück', yl: 'Gesamtkosten in €', series: [{pts: [[0, a.fix], [nMax, cost(a, nMax)]], cls: 's1', name: a.name}, {pts: [[0, b.fix], [nMax, cost(b, nMax)]], cls: 's0', name: b.name}]});
  function draw() {
    pl.set({vl: [{x: n, t: n + ' Stück'}], marks: be > 0 && be < nMax ? [{x: be, y: cost(a, be), t: 'gleich teuer'}] : []});
    $('.tk-val', root).textContent = n;
    readout($('.tk-readout', root), [[a.name + ' je Stück', numDE(cost(a, n) / n, 2) + ' €'], [b.name + ' je Stück', numDE(cost(b, n) / n, 2) + ' €']]);
    $('.status', root).innerHTML = cost(b, n) < cost(a, n) ? `Bei ${n} Stück ist die <b>${b.name}</b> günstiger: Die Kosten für die Vorrichtung verteilen sich auf viele Teile.` : `Bei ${n} Stück ist die <b>${a.name}</b> günstiger – die Vorrichtung lohnt sich erst ab etwa ${Math.ceil(be)} Stück.`;
  }
  root.addEventListener('input', e => { n = +e.target.value; draw(); });
  draw();
}

/* ---------- Stromnetz an einem Tag ---------- */
function gridSim(root) {
  let pv = 50, wind = 30, store = false;
  root.innerHTML = `<div class="tk-row"><label>Solaranlagen <input type="range" data-k="pv" min="0" max="100" step="10" value="${pv}"> <span class="tk-val" data-o="pv"></span></label><label>Windräder <input type="range" data-k="wind" min="0" max="100" step="10" value="${wind}"> <span class="tk-val" data-o="wind"></span></label><button class="btn" data-k="st">Speicher einschalten</button></div>
    <div class="cols-2"><div class="gr-plot"></div><div><div class="tk-readout"></div><p class="status" aria-live="polite"></p></div></div>`;
  const H = [...Array(25).keys()];
  const need = h => 45 + 15 * Math.exp(-((h - 8) ** 2) / 6) + 22 * Math.exp(-((h - 19) ** 2) / 5) - 12 * Math.exp(-((h - 3) ** 2) / 8);
  const sun = h => Math.max(0, Math.sin((h - 6) / 14 * Math.PI));
  const pl = plot($('.gr-plot', root), {x: [0, 24], y: [0, 140], xs: 4, ys: 20, xl: 'Uhrzeit', yl: 'Leistung (Modell)', series: []});
  function draw() {
    const gen = h => pv * 1.2 * sun(h) + wind * (.55 + .25 * Math.sin(h / 3.5));
    let sur = 0, def = 0, soc = 0;
    const net = H.map(h => { let d = gen(h) - need(h); return d; });
    if (store) { // Überschuss tagsüber speichern, abends abgeben
      net.forEach((d, k) => { if (d > 0) { const s = Math.min(d, 40); soc += s; net[k] = d - s; } });
      net.forEach((d, k) => { if (d < 0 && soc > 0) { const s = Math.min(-d, soc); soc -= s; net[k] = d + s; } });
    }
    net.forEach(d => d > 0 ? sur += d : def -= d);
    pl.set({series: [{pts: H.map(h => [h, need(h)]), cls: 's1', name: 'Verbrauch'}, {pts: H.map(h => [h, gen(h)]), cls: 's2', name: 'Wind + Sonne'}], area: [...H.map(h => [h, gen(h)]), [24, 0], [0, 0]]});
    readout($('.tk-readout', root), [['Überschuss', numDE(sur, 0) + ' Einh.'], ['aus Kraftwerken', numDE(def, 0) + ' Einh.'], ['Speicher', store ? 'an' : 'aus']]);
    $$('[data-o]', root).forEach(e => e.textContent = (e.dataset.o === 'pv' ? pv : wind) + ' %');
    $('.status', root).innerHTML = (def > 1 ? `Wenn Wind und Sonne nicht reichen, müssen <b>Kraftwerke oder Speicher</b> einspringen (${numDE(def, 0)} Einheiten).` : 'Wind und Sonne decken den ganzen Tag.') + (sur > 1 ? ` Mittags gibt es <b>Überschuss</b> (${numDE(sur, 0)} Einheiten) – ${store ? 'ein Teil wird gespeichert.' : 'ohne Speicher wird er abgeregelt oder exportiert.'}` : '');
  }
  root.addEventListener('input', e => { const k = e.target.dataset.k; if (k === 'pv') pv = +e.target.value; if (k === 'wind') wind = +e.target.value; draw(); });
  root.addEventListener('click', e => { const b = e.target.closest('[data-k="st"]'); if (b) { store = !store; b.classList.toggle('ok', store); b.textContent = store ? 'Speicher ausschalten' : 'Speicher einschalten'; draw(); } });
  draw();
}

/* ---------- Viertaktmotor ---------- */
function engine4(root) {
  let phi = 0, run = false;
  const TAKT = [['1. Takt: Ansaugen', 'Der Kolben bewegt sich nach unten. Das Einlassventil ist offen, Kraftstoff-Luft-Gemisch strömt in den Zylinder.'],
    ['2. Takt: Verdichten', 'Beide Ventile sind geschlossen. Der Kolben bewegt sich nach oben und presst das Gemisch zusammen.'],
    ['3. Takt: Arbeiten', 'Die Zündkerze zündet das Gemisch. Die heißen Gase dehnen sich aus und drücken den Kolben nach unten – nur in diesem Takt wird Arbeit verrichtet.'],
    ['4. Takt: Ausstoßen', 'Das Auslassventil ist offen. Der Kolben bewegt sich nach oben und schiebt die Abgase hinaus.']];
  root.innerHTML = `<div class="cols-2"><div class="tk-fig"><svg viewBox="0 0 300 380" class="sch" role="img" aria-label="Viertaktmotor"></svg></div><div><div class="tk-row"><span class="en-seg"></span></div><div class="tk-row"><button class="btn primary" data-k="run">▶ Abspielen</button></div><h3 class="en-h"></h3><p class="en-t"></p></div></div>`;
  const svg = $('svg', root);
  function draw() {
    const a = phi * Math.PI / 180, r = 40, l = 110, cx = 150, cy = 300;
    const xp = r * Math.sin(a), yp = cy - (r * Math.cos(a) + Math.sqrt(l * l - xp * xp));
    const top = yp - 30, k = Math.floor((phi % 720) / 180);
    const inl = k === 0 ? 14 * Math.sin((phi % 180) / 180 * Math.PI) : 0, exh = k === 3 ? 14 * Math.sin((phi % 180) / 180 * Math.PI) : 0;
    const gas = ['#7DB8F0', '#3D7FD6', '#F97316', '#9CA3AF'][k];
    const spark = k === 2 && (phi % 180) < 25;
    let s = `<rect x="90" y="40" width="120" height="${top - 40 + 2}" fill="${gas}" opacity=".55"/>`;
    s += `<path class="w" d="M88 40V250M212 40V250M88 40H118M182 40H212"/>`;
    s += `<path class="w" d="M118 40V10M182 40V10"/><text x="100" y="22" class="sm">Einlass</text><text x="186" y="22" class="sm">Auslass</text>`;
    s += `<path class="w" d="M108 ${40 + inl}H128M118 ${40 + inl}V0"/><path class="w" d="M172 ${40 + exh}H192M182 ${40 + exh}V0"/>`;
    s += `<path class="w" d="M150 40V28"/><circle cx="150" cy="44" r="${spark ? 10 : 3}" fill="${spark ? 'var(--lamp)' : 'var(--wire)'}"/><text x="156" y="34" class="sm">Zündkerze</text>`;
    s += `<rect class="sym" x="92" y="${top}" width="116" height="40"/><text x="150" y="${top + 26}" text-anchor="middle" class="sm">Kolben</text>`;
    s += `<path class="w" d="M150 ${top + 40}L${cx + xp} ${cy - r * Math.cos(a)}"/><circle class="thin" cx="${cx}" cy="${cy}" r="${r}"/><circle class="fillw" cx="${cx + xp}" cy="${cy - r * Math.cos(a)}" r="6"/><circle class="fillw" cx="${cx}" cy="${cy}" r="5"/><text x="${cx + 48}" y="${cy + 46}" class="sm">Kurbelwelle</text>`;
    svg.innerHTML = s;
    $('.en-h', root).textContent = TAKT[k][0]; $('.en-t', root).textContent = TAKT[k][1];
    $$('.en-seg button', root).forEach((b, i) => b.setAttribute('aria-pressed', i === k));
  }
  seg($('.en-seg', root), TAKT.map((t, i) => [i, t[0].split(': ')[1]]), v => { phi = +v * 180 + 90; draw(); }, 0);
  root.addEventListener('click', e => { const b = e.target.closest('[data-k="run"]'); if (b) { run = !run; b.textContent = run ? '❚❚ Anhalten' : '▶ Abspielen'; } });
  animLoop(root, dt => { if (run) { phi = (phi + dt * 120) % 720; draw(); } });
  draw();
}

/* Übungskörper aus Würfeln (x rechts, y nach hinten, z oben) */
const VOX_BODIES = [
  {name: 'A Winkel', cubes: [[0, 0, 0], [1, 0, 0], [2, 0, 0], [0, 0, 1], [0, 1, 0], [1, 1, 0], [2, 1, 0], [0, 1, 1]]},
  {name: 'B Treppe', cubes: [[0, 0, 0], [1, 0, 0], [2, 0, 0], [0, 0, 1], [1, 0, 1], [0, 0, 2], [0, 1, 0], [1, 1, 0], [2, 1, 0], [0, 1, 1], [1, 1, 1], [0, 1, 2]]},
  {name: 'C T-Stück', cubes: [[0, 0, 1], [1, 0, 1], [2, 0, 1], [1, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [1, 1, 0]]},
  {name: 'D Säule hinten', cubes: [[0, 0, 0], [1, 0, 0], [2, 0, 0], [0, 1, 0], [1, 1, 0], [2, 1, 0], [2, 1, 1], [2, 1, 2]]},
  {name: 'E Brücke', cubes: [[0, 0, 0], [2, 0, 0], [0, 0, 1], [1, 0, 1], [2, 0, 1], [0, 1, 0], [2, 1, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1]]},
  {name: 'F Podest', cubes: [[0, 0, 0], [1, 0, 0], [2, 0, 0], [0, 1, 0], [1, 1, 0], [2, 1, 0], [0, 2, 0], [1, 2, 0], [2, 2, 0], [1, 1, 1]]},
  {name: 'G U-Form', cubes: [[0, 0, 0], [1, 0, 0], [2, 0, 0], [0, 0, 1], [2, 0, 1], [0, 1, 0], [1, 1, 0], [2, 1, 0], [0, 1, 1], [2, 1, 1]]},
  {name: 'H Stufe hinten', cubes: [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 2, 0], [1, 2, 0], [0, 1, 1], [1, 1, 1], [0, 2, 1], [1, 2, 1], [0, 2, 2], [1, 2, 2]]}
];
