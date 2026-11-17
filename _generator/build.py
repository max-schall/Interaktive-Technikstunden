#!/usr/bin/env python3
"""Baut die Technik-Reihen aus src/<reihe>/*.html in den Zielordner.
Aufbau wie bei den Chemie- und IT-Präsentationen, eigenes Design „Werkstattzeichnung“:
base.css (Bausteine aus IT) + style.css (Technik-Gestaltung), lib.js (Bausteine aus IT) + tech.js (Technik-Bausteine).
Aufruf: build.py [<reihe> ...]   (ohne Argument: alle Reihen und die Startseite)"""
import html, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from series import SERIES  # noqa: E402

SUBJ = 'Technik'
FONTS = '<link rel="stylesheet" href="../fonts/fonts.css">'
# Hell: Zeichenpapier (ohne Raster) · Dunkel: Blaupause
LIGHT = ("--bg:#F3F0E8; --surface:#FFFEFA; --surface-2:#EAE5D8; --ink:#17212B; --ink-2:#55606B; --line:#C9C1AE; --grid:rgba(38,92,140,.07); --grid-2:rgba(38,92,140,.14);\n"
         "  --edge:#17212B; --edge-shadow:transparent; --accent:#1D4ED8; --accent-ink:#FFFFFF; --good:#15803D; --bad:#B91C1C;\n"
         "  --e:#1D6FB8; --v:#B45309; --a:#BE185D; --k1:#6D28D9; --k2:#C2410C; --k3:#0369A1; --k4:#047857; --zl-a:#F7E9A8; --zl-b:#F1B35A;\n"
         "  --bar:#FFFEFA; --bar-2:#F3F0E8; --bar-line:#17212B; --bar-ink:#17212B; --bar-ink-2:#55606B; --led:#1D4ED8;\n"
         "  --phone:#2B3438; --phone-scr:#CFE6EE; --phone-part:#55636A; --heft-line:rgba(38,92,140,.10);\n"
         "  --wire:#17212B; --cu:#B87333; --wood:#C8955A; --wood-2:#A8743E; --steel:#8A9AA8; --steel-2:#5F7181; --plastic:#5BB5D6; --warn:#F5C400; --gebot:#1E5AA8; --verbot:#C1121C; --rettung:#16794C; --lamp:#FFD23F;")
DARK = ("--bg:#0E2A47; --surface:#123456; --surface-2:#18406A; --ink:#EAF2FA; --ink-2:#A9C1D9; --line:#3B6489; --grid:rgba(214,234,255,.06); --grid-2:rgba(214,234,255,.13);\n"
        "    --edge:#D6EAFF; --edge-shadow:transparent; --accent:#93C5FD; --accent-ink:#0E2A47; --good:#86EFAC; --bad:#FCA5A5;\n"
        "    --e:#7DB8F0; --v:#FBBF24; --a:#F472B6; --k1:#C4B5FD; --k2:#FDBA74; --k3:#7DD3FC; --k4:#6EE7B7; --zl-a:#E9D98F; --zl-b:#E3A04A;\n"
        "    --bar:#0B2340; --bar-2:#0E2A47; --bar-line:#D6EAFF; --bar-ink:#EAF2FA; --bar-ink-2:#A9C1D9; --led:#93C5FD;\n"
        "    --phone:#3A464B; --phone-scr:#1E3A44; --phone-part:#6B7B82; --heft-line:rgba(214,234,255,.08);\n"
        "    --wire:#D6EAFF; --cu:#E0A36B; --wood:#C8955A; --wood-2:#A8743E; --steel:#9FB2C4; --steel-2:#6F8597; --plastic:#7CCBE6; --warn:#F5C400; --gebot:#2F6FC2; --verbot:#D9343E; --rettung:#1F9D63; --lamp:#FFD23F;\n"
        "    color-scheme:dark;")


def palette_css(series=None):
    fonts = ('  --f-body:"Atkinson Hyperlegible","Segoe UI",system-ui,sans-serif;\n'
             '  --f-mono:"Barlow Semi Condensed","Arial Narrow","Roboto Condensed",system-ui,sans-serif;\n'
             '  --f-code:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Consolas,monospace;\n  font-size:clamp(16px, 0.75vw + 9px, 22px);\n')
    light, dark = LIGHT, DARK
    if series and 'accent' in series:
        la, da = series['accent']
        light += f" --accent:{la}; --led:{la};"
        dark = dark.replace('color-scheme:dark;', f'--accent:{da}; --led:{da}; color-scheme:dark;')
    return (":root{\n  " + light + "\n" + fonts + "}\n"
            "@media (prefers-color-scheme: dark){\n  :root:not([data-theme=\"light\"]){\n    " + dark + "\n  }\n}\n"
            ":root[data-theme=\"dark\"]{\n    " + dark + "\n}\n")


META_RE = re.compile(r'^\s*<!--(.*?)-->', re.S)


def parse_lesson(path):
    txt = path.read_text(encoding='utf-8')
    m = META_RE.match(txt)
    meta = {}
    for line in m.group(1).strip().splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            meta[k.strip()] = v.strip()
    body = txt[m.end():]
    js = ''
    if '<script>' in body:
        i = body.index('<script>')
        js = body[i + 8:body.rindex('</script>')]
        body = body[:i]
    return meta, body.strip(), js


SEC_RE = re.compile(r'<section class="station" id="([^"]+)"([^>]*)>')
ATTR_RE = re.compile(r'data-([a-z]+)="([^"]*)"')


def neighbours(series):
    """Vorige/nächste Reihe derselben Klassenstufe als Links für die Übersicht."""
    same = [s for s in SERIES if s['grade'] == series['grade']]
    k = same.index(series)
    out = []
    if k > 0:
        out.append((f'../{same[k - 1]["folder"]}/00_Uebersicht.html', f'← Kapitel {same[k - 1]["chapter"]}'))
    if k + 1 < len(same):
        out.append((f'../{same[k + 1]["folder"]}/00_Uebersicht.html', f'Kapitel {same[k + 1]["chapter"]} →'))
    return out


def build_lesson(series, idx, lessons, outdir, css, js):
    path, meta, body, ljs = lessons[idx]
    grade = series['grade']
    num = idx + 1
    secs = [(mm.group(1), dict(ATTR_RE.findall(mm.group(2)))) for mm in SEC_RE.finditer(body)]
    first = True

    def hide(mm):
        nonlocal first
        tag = mm.group(0)
        if first:
            first = False
            return tag
        return tag[:-1] + ' hidden>'
    body = SEC_RE.sub(hide, body)
    stations = [(i, a) for i, a in secs if 'yr' in a]
    tl = ['      <li><button class="tl-pill" data-go="start">Start</button></li>', '      <li class="sep" aria-hidden="true"></li>']
    for k, (sid, a) in enumerate(stations):
        cls = 'm' + (' first' if k == 0 else '') + (' last' if k == len(stations) - 1 else '')
        tl.append(f'      <li class="{cls}"><button class="tl-stop" data-go="{sid}"><span class="dot"><span class="num">{k + 1}</span></span><span class="yr">{a["yr"]}</span><span class="nm">{a.get("label", sid)}</span></button></li>')
    tl.append('      <li class="sep" aria-hidden="true"></li>')
    for sid, a in secs:
        if sid != 'start' and 'yr' not in a:
            tl.append(f'      <li><button class="tl-pill" data-go="{sid}">{a.get("label", sid)}</button></li>')
    prev = ['    <ol class="preview" aria-label="Stationen dieser Stunde">']
    for k, (sid, a) in enumerate(stations):
        prev.append(f'      <li><button data-go="{sid}"><span class="num">{k + 1}</span><span class="y">{a["yr"]}</span><span class="n"><b>{a.get("title", a.get("label"))}</b><span>{a.get("sub", "")}</span></span></button></li>')
    prev.append('    </ol>')
    body = body.replace('<!--PREVIEW-->', '\n'.join(prev)).replace('{{N}}', str(num)).replace('{{K}}', str(grade))
    if idx + 1 < len(lessons):
        npath, nmeta = lessons[idx + 1][0], lessons[idx + 1][1]
        nxt = {'href': npath.name, 'label': f'Stunde {num + 1}: {nmeta["short"]}'}
        box = (f'<div class="next-lesson"><p><b>Nächste Stunde – {nmeta["title"]}:</b> {nmeta["q"]}</p>'
               f'<a class="btn primary" href="{npath.name}">Zu Stunde {num + 1} →</a></div>')
    else:
        nxt = {'href': '00_Uebersicht.html', 'label': 'Zur Übersicht'}
        box = '<div class="next-lesson"><p><b>Geschafft!</b> Das war die letzte Stunde dieser Reihe.</p><a class="btn primary" href="00_Uebersicht.html">Zur Übersicht der Reihe</a></div>'
    if 'id="uebungen"' in body:
        i = body.index('id="uebungen"')
        j = body.index('</section>', i)
        body = body[:j] + '  ' + box + '\n' + body[j:]
    page = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{meta["title"]}</title>
{FONTS}
<style>
/* Layout „Werkstattzeichnung“: Schriftfeld mit Arbeitsschritten oben, eine Station pro Bildschirm, Blätter-Leiste unten – gebaut für Beamer & Presenter */
{palette_css(series)}{css}
</style>
</head>
<body data-next="{html.escape(json.dumps(nxt, ensure_ascii=False))}">
<div class="app">
<header class="top">
  <div class="brand"><small>Benennung</small><b>{meta["short"]}</b><span>Stunde {num} · {SUBJ} · Klasse {grade}</span></div>
  <nav class="tl-scroll" aria-label="Stationen der Stunde">
    <ol class="tl" id="tl">
{chr(10).join(tl)}
    </ol>
  </nav>
  <a class="icon-btn" href="../index.html#klasse-{grade}" title="Startseite: alle Reihen der Klassenstufe">⌂ Start</a>
  <a class="icon-btn" href="{path.stem}.pdf" target="_blank" rel="noopener" title="Arbeitsblatt zur Stunde (PDF)">Arbeitsblatt</a>
  <a class="icon-btn" href="00_Uebersicht.html" title="Zur Übersicht der Reihe">Übersicht</a>
  <button class="icon-btn" id="fs" title="Vollbild (F)">Vollbild</button>
</header>

<main id="stage">
{body}
</main>

<footer class="pager">
  <button class="btn" id="prev">←</button>
  <div class="mid"><span id="pos"></span><span class="keys"> · Pfeiltasten ← → oder Presenter</span></div>
  <button class="btn primary" id="next">→</button>
</footer>
</div>

<script>
(() => {{
{js}
/* ================================================================ */
/* ================= Inhalte dieser Stunde ================= */
{ljs}
startApp();
}})();
</script>
</body>
</html>
'''
    (outdir / path.name).write_text(page, encoding='utf-8')


def build_overview(series, lessons, outdir, css):
    grade = series['grade']
    items = []
    for k, (path, meta, body, _) in enumerate(lessons):
        facts = ''.join(f'<li>{f.strip()}</li>' for f in meta.get('facts', '').split('|') if f.strip())
        items.append(f'''    <li class="lesson">
      <div class="l-num">{k + 1}</div>
      <div class="l-body">
        <p class="eyebrow">Stunde {k + 1} · {meta.get("time", "1 Unterrichtsstunde")}</p>
        <h2>{meta["title"]}</h2>
        <p class="l-q"><b>Leitfrage:</b> {meta["q"]}</p>
        <ul class="facts">{facts}</ul>
        <p class="l-int"><span class="tag info">Interaktiv</span> {meta.get("inter", "")}</p>
      </div>
      <div class="l-go"><a class="btn" href="{path.stem}.pdf" target="_blank" rel="noopener">Arbeitsblatt</a><a class="btn primary" href="{path.name}">Öffnen →</a></div>
    </li>''')
    links = ''.join(f'\n  <a class="icon-btn" href="{h}">{t}</a>' for h, t in neighbours(series))
    notes = '\n'.join(f'    <div class="box"><span class="tag {c}">{t}</span>\n      <p>{p}</p></div>' for t, c, p in series['notes'])
    page = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{series["name"]} – Übersicht</title>
{FONTS}
<style>
{palette_css(series)}{css}
</style>
</head>
<body>
<div class="app">
<header class="top">
  <div class="brand"><small>Reihe</small><b>{series["name"]}</b><span>{SUBJ} · Klasse {grade}</span></div>
  <span style="flex:1"></span>
  <a class="icon-btn" href="../index.html#klasse-{grade}">⌂ Start</a>{links}
  <a class="icon-btn" href="#hinweise">Hinweise für Lehrkräfte</a>
</header>
<main>
<section class="ov">
  <div class="ov-hero">
    <div>
      <p class="eyebrow">Klasse {grade} · Kapitel {series["chapter"]} · {len(lessons)} Stunde{"n" if len(lessons) != 1 else ""}</p>
      <h1>{series["h1"]}</h1>
      <p class="lead">{series["lead"]}</p>
    </div>
    <div class="ov-facts">
      <div class="meter"><span>Stunden</span><b>{len(lessons)}</b><small>Präsentation{"en" if len(lessons) != 1 else ""}</small></div>
      <div class="meter"><span>Umfang</span><b>≈ {series["ue"]}</b><small>Unterrichtsstunden</small></div>
      <div class="meter"><span>Thema</span><b>{series["bp"]}</b><small>{series.get("ral", "")}</small></div>
    </div>
  </div>
  <ol class="lessons">
{chr(10).join(items)}
  </ol>
  <div class="section-head mt" id="hinweise"><p class="eyebrow">Für Lehrkräfte</p><h2>Hinweise zum Einsatz</h2></div>
  <div class="takeaway">
    <div class="box"><span class="tag info">Bedienung</span>
      <p>Blättern mit den Pfeiltasten, Bild↑/Bild↓ oder einem Presenter. <b>F</b> schaltet den Vollbildmodus. Über das Schriftfeld oben springt man direkt zu jeder Station. Stationen lassen sich direkt verlinken, z. B. <code>{lessons[0][0].name}#merke</code>.</p></div>
    <div class="box"><span class="tag info">Aufbau jeder Stunde</span>
      <p>Start mit Einstieg und Leitfrage → nummerierte Stationen (Einstieg, Erarbeitung, Werkstatt/Material) → <b>Hefteintrag</b>, der Punkt für Punkt aufgedeckt wird → <b>Übungen</b> mit Prüfen-Knopf und Lösung. Zu jeder Stunde gibt es ein Arbeitsblatt (PDF) mit QR-Code zur Präsentation, Platz für den Hefteintrag und ein Lösungsblatt.</p></div>
{notes}
    <div class="box"><span class="tag info">Technik</span>
      <p>Jede Datei ist eigenständig und funktioniert offline, auch vom USB-Stick. Die Schriften liegen im Ordner <code>fonts</code> neben den Reihen. Hell (Papier) und Dunkel (Blaupause) folgen der Systemeinstellung.</p></div>
  </div>
</section>
</main>
</div>
</body>
</html>
'''
    (outdir / '00_Uebersicht.html').write_text(page, encoding='utf-8')


GRADE_INFO = {'7': 'Technikraum und Sicherheit, der Werkstoff Holz mit Werkzeugen und Bohrmaschine, Skizzen und technische Zeichnungen.',
              '8': 'Metall und Kunststoff, Fertigungsverfahren und Werkstoffprüfung, der elektrische Stromkreis mit dem ohmschen Gesetz.',
              '9': 'Elektronik mit Sensoren und Transistor, CAD, Lasercutter und Serienfertigung, Maschinen, Getriebe und Mobilität.',
              '10': 'Bautechnik und Haustechnik, Energieversorgung mit erneuerbaren Energien, Steuerung, Regelung und Mikrocontroller.'}

INDEX_CSS = '''.hero{position:relative;padding:1.4rem 1.6rem 1.2rem;border:1.5px solid var(--edge);background:var(--surface);margin-bottom:1.6rem}
.hero::before{content:"";position:absolute;inset:6px;border:.5px solid var(--line);pointer-events:none}
.hero h1{font-size:clamp(2.6rem,7vw,5rem);letter-spacing:.02em;margin:.1rem 0 .2rem}
.hero h1 small{font-size:.38em;letter-spacing:.08em;color:var(--accent);margin-left:.4rem;vertical-align:.5em;text-transform:uppercase}
.kitap-sub{font-family:var(--f-mono);font-size:clamp(1rem,1.6vw,1.25rem);color:var(--ink-2);margin:0 0 1rem;letter-spacing:.02em}
.hero .lead{max-width:70ch}
.crumbs{display:flex;flex-wrap:wrap;align-items:center;gap:.2rem;margin:0 0 1.2rem;padding:.45rem .8rem;background:var(--surface);border:1.5px solid var(--edge);font-family:var(--f-mono);font-size:.95rem;scroll-margin-top:5rem;text-transform:uppercase;letter-spacing:.05em}
.crumbs::before{content:"Pos.";color:var(--ink-2);margin-right:.5rem;font-size:.75rem}
.crumbs a{color:var(--ink);text-decoration:none;padding:.05rem .3rem}
.crumbs a:hover{color:var(--accent)}
.crumbs [aria-current]{color:var(--accent);font-weight:600;padding:.05rem .3rem}
.crumbs .sep{opacity:.5}
.vh{font-size:1.4rem;margin:0 0 1rem}
.grades{display:grid;grid-template-columns:repeat(auto-fit,minmax(14rem,1fr));gap:1.2rem}
.grade{position:relative;display:grid;grid-template-columns:1fr auto;grid-template-rows:auto auto 1fr auto;column-gap:.6rem;text-decoration:none;color:inherit;background:var(--surface);border:1.5px solid var(--edge);transition:transform .12s}
.grade:hover,.grade:focus-visible{transform:translateY(-3px)}
.grade:hover .g-num,.grade:focus-visible .g-num{background:var(--accent);color:var(--accent-ink)}
.g-lbl{grid-column:1;padding:.5rem .8rem 0;font-family:var(--f-mono);font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;color:var(--ink-2)}
.g-num{grid-column:2;grid-row:1/3;display:grid;place-items:center;min-width:5.2rem;padding:.4rem .8rem;border-left:1.5px solid var(--edge);border-bottom:1.5px solid var(--edge);font-family:var(--f-mono);font-weight:700;font-size:clamp(2.6rem,6vw,3.6rem);line-height:1;color:var(--accent);transition:background .12s,color .12s}
.g-meta{grid-column:1;padding:0 .8rem;font-family:var(--f-mono);font-size:1.05rem;font-weight:600}
.g-txt{grid-column:1/-1;padding:.7rem .8rem .2rem;font-size:.9rem;color:var(--ink-2)}
.g-leds{grid-column:1/-1;display:flex;gap:0;border-top:1.5px solid var(--edge);margin-top:.6rem}
.g-leds i{flex:1;height:.6rem;background:var(--accent)}
.g-leds i+i{border-left:1.5px solid var(--edge)}
.lesson .l-num{color:var(--accent)}
.lesson{border-left:8px solid var(--accent)}
.topic-head{display:flex;flex-wrap:wrap;gap:1rem 2rem;align-items:flex-end;justify-content:space-between;margin-bottom:1.2rem}
.topic-head h2{margin:0 0 .3rem}
.topic-head p{margin:0;color:var(--ink-2);max-width:64ch}
.topic-head .eyebrow{margin-bottom:.4rem}
.rows{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.55rem}
.rows li{display:flex;gap:.55rem}
.row{flex:1;display:flex;align-items:center;gap:1rem;text-decoration:none;color:inherit;background:var(--surface);border:1.5px solid var(--edge);padding:.6rem .9rem;min-width:0}
.row:hover,.ws:hover{background:var(--surface-2)}
.row .no{flex:none;display:grid;place-items:center;width:2.1rem;height:2.1rem;border:1.5px solid var(--edge);border-radius:50%;font-family:var(--f-mono);font-weight:700;font-size:1.05rem;color:var(--accent);background:var(--surface)}
.row .rt{flex:1;min-width:0;display:flex;flex-direction:column}
.row .rt small{color:var(--ink-2);font-size:.85rem}
.row .go{font-family:var(--f-mono);font-size:.9rem;color:var(--accent);font-weight:600;flex:none;text-transform:uppercase;letter-spacing:.05em}
.ws{flex:none;display:grid;place-items:center;width:3.2rem;font-family:var(--f-mono);font-weight:700;font-size:.9rem;text-decoration:none;color:var(--ink);background:var(--surface);border:1.5px solid var(--edge)}
.site-foot{margin-top:3rem;color:var(--ink-2);font-size:.82rem}
.site-foot a{color:inherit}
.site-foot a:hover{color:var(--accent)}
@media (max-width:600px){.row .go{display:none}}
'''

INDEX_JS = '''(() => {
  const views = [...document.querySelectorAll('.view')], crumbs = document.getElementById('crumbs'), home = document.getElementById('home');
  function show() {
    let h = decodeURIComponent(location.hash.slice(1));
    if (!views.some(v => v.dataset.view === h)) h = '';
    views.forEach(v => v.hidden = v.dataset.view !== h);
    home.hidden = !h;
    const parts = h ? h.split('/') : [];
    let out = parts.length ? '<a href="#">Klassen</a>' : '<span aria-current="page">Klassen</span>';
    parts.forEach((p, i) => {
      const key = parts.slice(0, i + 1).join('/'), name = T[key] || p;
      out += '<span class="sep">/</span>' + (i === parts.length - 1 ? `<span aria-current="page">${name}</span>` : `<a href="#${key}">${name}</a>`);
    });
    crumbs.innerHTML = out;
    document.title = (h ? T[h] + ' – ' : '') + 'KITAP – Technik';
  }
  addEventListener('hashchange', () => { show(); if (location.hash) crumbs.scrollIntoView({block: 'start', behavior: 'smooth'}); });
  show();
})();'''


def build_index(css):
    """Startseite: Klassenstufe wählen → Reihe wählen → Stunde wählen (Ansichten über #Anker)."""
    grades = {}
    for k, s in enumerate(SERIES):
        files = sorted((HERE / 'src' / s['folder']).glob('[0-9][0-9]_*.html'))
        if not files:
            continue
        s = dict(s, idx=k, lessons=[(f, parse_lesson(f)[0]) for f in files])
        grades.setdefault(s['grade'], []).append(s)
    tiles, views, scss_l, scss_d, titles = [], [], [], [], {}
    for g, ss in grades.items():
        gk = f'klasse-{g}'
        titles[gk] = f'Klasse {g}'
        n = sum(len(s['lessons']) for s in ss)
        leds = ''.join(f'<i class="ser{s["idx"]}" title="{html.escape(s["name"])}"></i>' for s in ss)
        tiles.append(f'''    <a class="grade ser{ss[0]["idx"]}" href="#{gk}">
      <span class="g-lbl">Klasse</span><span class="g-num">{g}</span>
      <span class="g-meta">{len(ss)} Reihen · {n} Stunden</span>
      <span class="g-txt">{GRADE_INFO.get(g, '')}</span>
      <span class="g-leds" aria-hidden="true">{leds}</span>
    </a>''')
        cards, sviews = [], []
        for s in ss:
            titles[f'{gk}/{s["folder"]}'] = s['name']
            scss_l.append(f'.ser{s["idx"]}{{--accent:{s["accent"][0]}}}')
            scss_d.append(f'.ser{s["idx"]}{{--accent:{s["accent"][1]}}}')
            ln = len(s['lessons'])
            cards.append(f'''      <li class="lesson ser{s["idx"]}">
        <div class="l-num">{s["chapter"]}</div>
        <div class="l-body"><p class="eyebrow">Kapitel {s["chapter"]} · {ln} Stunde{"n" if ln != 1 else ""} · ≈ {s["ue"]} Unterrichtsstunden</p><h2>{s["name"]}</h2><p class="l-q">{s["lead"]}</p></div>
        <div class="l-go"><a class="btn primary" href="#{gk}/{s["folder"]}">Stunden →</a><a class="btn" href="{s["folder"]}/00_Uebersicht.html">Übersicht</a></div>
      </li>''')
            rows = []
            for k2, (f, m) in enumerate(s['lessons']):
                rows.append(f'''        <li><a class="row" href="{s["folder"]}/{f.name}"><span class="no">{k2 + 1}</span><span class="rt"><b>{m["title"]}</b><small>{m.get("q", "")}</small></span><span class="go">öffnen →</span></a><a class="ws" href="{s["folder"]}/{f.stem}.pdf" target="_blank" rel="noopener" title="Arbeitsblatt (PDF)">AB</a></li>''')
            sviews.append(f'''  <section class="view ser{s["idx"]}" data-view="{gk}/{s["folder"]}" hidden>
    <div class="topic-head">
      <div><p class="eyebrow">Klasse {s["grade"]} · Kapitel {s["chapter"]}</p><h2>{s["name"]}</h2><p>{s["lead"]}</p></div>
      <a class="btn primary" href="{s["folder"]}/00_Uebersicht.html">Übersicht der Reihe →</a>
    </div>
    <ol class="rows">
{chr(10).join(rows)}
    </ol>
  </section>''')
        views.append(f'''  <section class="view" data-view="{gk}" hidden>
    <h2 class="vh">Klasse {g}: Reihe wählen</h2>
    <ol class="lessons">
{chr(10).join(cards)}
    </ol>
  </section>''')
        views += sviews
    kcss = (''.join(scss_l) + '\n@media (prefers-color-scheme: dark){' + ''.join(':root:not([data-theme="light"]) ' + x for x in scss_d) + '}\n'
            + ''.join(':root[data-theme="dark"] ' + x for x in scss_d) + '\n')
    page = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>KITAP – Technik</title>
<meta name="description" content="Interaktive Präsentationen mit Arbeitsblättern für den Technikunterricht der Klassen 7 bis 10.">
<link rel="stylesheet" href="fonts/fonts.css">
<style>
{palette_css()}{css}
{kcss}{INDEX_CSS}</style>
</head>
<body>
<div class="app">
<header class="top"><div class="brand"><small>Fach</small><b>KITAP Technik</b><span>Klassen 7–10 · interaktiv</span></div><span style="flex:1"></span><a class="icon-btn" href="#" id="home" hidden>⌂ Klassen</a></header>
<main>
<section class="ov">
  <div class="hero">
    <p class="eyebrow">Interaktive Präsentationen · Klassen 7–10</p>
    <h1>KITAP<small>Technik</small></h1>
    <p class="kitap-sub">Klassenfertige Inhalte – Thematisch Aufbereitet und Präsentationsbereit</p>
    <p class="lead">Präsentationen für den Technikunterricht: Werkstoffe und Werkzeuge, Zeichnen und Fertigen, Elektrotechnik und Elektronik, Maschinen, Bauen, Energie, Steuerung und Regelung. Jede Stunde mit Stationen, Simulationen, Hefteintrag, Übungen und Arbeitsblatt mit QR-Code. Wähle zuerst die Klassenstufe, dann die Reihe.</p>
  </div>
  <nav class="crumbs" aria-label="Navigation" id="crumbs"><span aria-current="page">Klassen</span></nav>
  <section class="view" data-view="">
    <h2 class="vh">Klassenstufe wählen</h2>
    <div class="grades">
{chr(10).join(tiles)}
    </div>
  </section>
{chr(10).join(views)}
  <footer class="site-foot">KITAP · freie Unterrichtsmaterialien · <a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a></footer>
</section>
</main>
</div>
<script>
const T = {json.dumps(titles, ensure_ascii=False)};
{INDEX_JS}
</script>
</body>
</html>
'''
    (ROOT / 'index.html').write_text(page, encoding='utf-8')


def load_assets():
    css = (HERE / 'base.css').read_text(encoding='utf-8') + '\n' + (HERE / 'style.css').read_text(encoding='utf-8')
    js = (HERE / 'lib.js').read_text(encoding='utf-8') + '\n' + (HERE / 'tech.js').read_text(encoding='utf-8')
    return css, js


def main(only=None):
    css, js = load_assets()
    for s in SERIES:
        if only and s['folder'] not in only:
            continue
        files = sorted((HERE / 'src' / s['folder']).glob('[0-9][0-9]_*.html'))
        if not files:
            continue
        lessons = [(p, *parse_lesson(p)) for p in files]
        out = ROOT / s['folder']
        out.mkdir(exist_ok=True)
        for i in range(len(lessons)):
            build_lesson(s, i, lessons, out, css, js)
        build_overview(s, lessons, out, css)
        print('gebaut:', s['folder'], len(lessons), 'Stunde(n)')
    build_index(css)


if __name__ == '__main__':
    main(sys.argv[1:] or None)
