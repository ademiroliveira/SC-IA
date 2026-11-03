"""Build the offline web version of the Wallet Time Machine decks: one page per session plus a landing page.

Usage: python3 -I build.py <fonts dir> <out dir> <session 1 deck dir> <session 2 deck dir> <session 3 deck dir>

Each deck dir holds deck.json and slides/<id>.html in the Claude Slides format.
Fonts: the unpacked Fontsource npm packages for Inter Tight (variable) and JetBrains Mono.
"""
import base64
import json
import pathlib
import sys

from bs4 import BeautifulSoup

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from details import MARKS, REPORT, resolved  # noqa: E402

REPO = "https://github.com/ademiroliveira/SC-IA/blob/main/time-machine-workshop/"
SESSIONS = [
    ("1-the-past", "The past", "Where wallets came from, and which next milestone we want to drive or be part of."),
    ("2-the-futures", "The futures", "Two opposing worlds for 2040, 2035 and 2030, with our milestones inside them."),
    ("3-the-way-back", "The way back", "From 2040 back to two or three moves we make now, each with an owner and a first step."),
]

fonts_dir, out_dir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
deck_dirs = [pathlib.Path(p) for p in sys.argv[3:]]
if len(deck_dirs) != len(SESSIONS):
    sys.exit(f"expected {len(SESSIONS)} deck dirs, got {len(deck_dirs)}")
out_dir.mkdir(parents=True, exist_ok=True)


def font(path):
    return "data:font/woff2;base64," + base64.b64encode(path.read_bytes()).decode()


FONTS = [
    ["Inter Tight", font(next(fonts_dir.glob("fontsource-variable-inter-tight-*/files/inter-tight-latin-wght-normal.woff2"))), "100 900"],
    ["JetBrains Mono", font(next(fonts_dir.glob("fontsource-jetbrains-mono-*/files/jetbrains-mono-latin-400-normal.woff2"))), "400"],
    ["JetBrains Mono", font(next(fonts_dir.glob("fontsource-jetbrains-mono-*/files/jetbrains-mono-latin-500-normal.woff2"))), "500"],
]
FONT_JS = """
for (const [family, src, weight] of DATA.fonts) {
  const face = new FontFace(family, 'url(' + src + ')', {weight, style: 'normal', display: 'swap'});
  document.fonts.add(face); face.load().catch(() => {});
}
"""

marks_by_slide = {}
for slide_id, text, key in MARKS:
    marks_by_slide.setdefault(slide_id, []).append((text, key))


def json_script(obj):
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


DECK_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;background:#0f1418}
body{font-family:'Inter Tight',Arial,sans-serif;color:#192026;-webkit-font-smoothing:antialiased}
p{line-height:1.4}h1{font-size:96px;font-weight:600;line-height:1.1}h2{font-size:64px;font-weight:600;line-height:1.15}h3{font-size:44px;font-weight:600;line-height:1.2}
a{color:inherit}
#stage{position:fixed;left:50%;top:50%;width:1920px;height:1080px;transform-origin:center center}
.slide{position:absolute;left:0;top:0;width:1920px;height:1080px;overflow:hidden;visibility:hidden;opacity:0;transition:opacity .25s ease,visibility 0s linear .25s}
.slide.active{visibility:visible;opacity:1;transition:opacity .25s ease}
.more{display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;margin-left:16px;background:#416AEE;color:#EEE5D7;font-family:'JetBrains Mono','Courier New',monospace;font-size:24px;font-weight:500;line-height:1;letter-spacing:0;vertical-align:middle;transition:background .15s ease}
[data-detail]{cursor:pointer}
[data-detail]:hover .more,[data-detail]:focus-visible .more{background:#E74D3D}
[data-detail]:focus-visible{outline:3px solid #416AEE;outline-offset:12px}
#scrim{position:fixed;inset:0;background:rgba(25,32,38,.45);opacity:0;visibility:hidden;transition:opacity .2s ease,visibility 0s linear .2s}
#scrim.open{opacity:1;visibility:visible;transition:opacity .2s ease}
#drawer{position:fixed;top:0;right:0;width:min(560px,100vw);height:100%;overflow:auto;background:#EEE5D7;color:#192026;border-left:2px solid #192026;padding:40px 40px 56px;transform:translateX(105%);transition:transform .25s ease;display:flex;flex-direction:column;gap:24px}
#drawer.open{transform:translateX(0)}
#drawer .top{display:flex;justify-content:space-between;align-items:flex-start;gap:24px;border-top:2px solid #192026;padding-top:12px}
#drawer .eyebrow,#drawer .label,#drawer button,#drawer .report{font-family:'JetBrains Mono','Courier New',monospace;font-size:14px;letter-spacing:1px;text-transform:uppercase}
#drawer button{background:none;border:0;color:#192026;cursor:pointer;padding:4px 0}
#drawer button:hover{color:#E74D3D}
#drawer h2{font-size:36px;font-weight:700;line-height:1.1;letter-spacing:-.5px}
#drawer .body{display:flex;flex-direction:column;gap:14px}
#drawer .body p{font-size:19px;line-height:1.5}
#drawer .sources{display:flex;flex-direction:column;gap:10px;border-top:2px solid #192026;padding-top:12px}
#drawer .sources ul{list-style:none;display:flex;flex-direction:column;gap:10px}
#drawer .sources a,#drawer .report a{font-size:17px;line-height:1.4;text-decoration:underline;text-decoration-color:#416AEE;text-decoration-thickness:2px;text-underline-offset:3px}
#drawer .report{margin-top:auto;color:#4E555B}
#drawer .report a{text-transform:none;letter-spacing:0;font-family:'Inter Tight',Arial,sans-serif;color:#192026}
#chrome{position:fixed;right:16px;bottom:16px;display:flex;gap:8px;opacity:0;transition:opacity .3s ease}
#chrome.show,#chrome:focus-within{opacity:1}
#chrome button,#chrome a{display:inline-flex;align-items:center;justify-content:center;min-width:44px;height:44px;padding:0 12px;border:0;background:rgba(25,32,38,.85);color:#EEE5D7;font-family:'JetBrains Mono','Courier New',monospace;font-size:14px;letter-spacing:1px;text-transform:uppercase;text-decoration:none;cursor:pointer}
#chrome button{font-size:18px;letter-spacing:0}
#chrome button:hover,#chrome a:hover{background:#416AEE}
body.detail-open #chrome{display:none}
#hint{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:rgba(25,32,38,.9);color:#EEE5D7;font-family:'JetBrains Mono','Courier New',monospace;font-size:14px;padding:10px 16px;white-space:nowrap;transition:opacity .6s ease}
#hint.gone{opacity:0;pointer-events:none}
"""

DECK_JS = r"""
const DATA = JSON.parse(document.getElementById('data').textContent);
""" + FONT_JS + r"""
const stage = document.getElementById('stage');
const slides = [...stage.querySelectorAll('.slide')];
const drawer = document.getElementById('drawer');
const scrim = document.getElementById('scrim');
let current = 0;
function fit() {
  const s = Math.min(innerWidth / 1920, innerHeight / 1080);
  stage.style.transform = 'translate(-50%, -50%) scale(' + s + ')';
}
function show(i, push) {
  current = Math.max(0, Math.min(slides.length - 1, i));
  slides.forEach((el, n) => {
    const on = n === current;
    el.classList.toggle('active', on);
    el.setAttribute('aria-hidden', on ? 'false' : 'true');
    el.querySelectorAll('[data-detail]').forEach(d => d.tabIndex = on ? 0 : -1);
  });
  closeDetail();
  const hash = '#slide-' + (current + 1);
  if (location.hash !== hash) history[push ? 'pushState' : 'replaceState'](null, '', hash);
}
function fromHash() {
  const m = location.hash.match(/^#slide-(\d+)$/);
  show(m ? parseInt(m[1], 10) - 1 : 0, false);
}
function esc(s) { const d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
let lastFocus = null;
function openDetail(key, from) {
  const d = DATA.details[key];
  if (!d) return;
  lastFocus = from || null;
  let html = '<div class="top"><p class="eyebrow">' + esc(d.eyebrow) + '</p><button type="button" id="close" aria-label="Close">Close ×</button></div>';
  html += '<h2 id="drawer-title">' + esc(d.title) + '</h2><div class="body">' + d.body.map(p => '<p>' + esc(p) + '</p>').join('') + '</div>';
  if (d.sources.length) {
    html += '<div class="sources"><p class="label">Sources</p><ul>' +
      d.sources.map(([label, url]) => '<li><a href="' + esc(url) + '" target="_blank" rel="noopener">' + esc(label) + '</a></li>').join('') + '</ul></div>';
  }
  html += '<p class="report">From the research · <a href="' + esc(DATA.report) + '" target="_blank" rel="noopener">Wallet evolution report</a></p>';
  drawer.innerHTML = html;
  drawer.classList.add('open'); scrim.classList.add('open'); document.body.classList.add('detail-open');
  drawer.setAttribute('aria-hidden', 'false');
  document.getElementById('close').addEventListener('click', closeDetail);
  document.getElementById('close').focus();
}
function closeDetail() {
  if (!drawer.classList.contains('open')) return;
  drawer.classList.remove('open'); scrim.classList.remove('open'); document.body.classList.remove('detail-open');
  drawer.setAttribute('aria-hidden', 'true');
  if (lastFocus) lastFocus.focus();
}
const isOpen = () => drawer.classList.contains('open');
stage.addEventListener('click', e => {
  const cell = e.target.closest('[data-detail]');
  if (cell) openDetail(cell.dataset.detail, cell);
});
stage.addEventListener('keydown', e => {
  const cell = e.target.closest('[data-detail]');
  if (cell && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); openDetail(cell.dataset.detail, cell); }
});
scrim.addEventListener('click', closeDetail);
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') { closeDetail(); return; }
  if (isOpen() || e.altKey || e.ctrlKey || e.metaKey) return;
  if (e.target.closest && e.target.closest('[data-detail]') && (e.key === 'Enter' || e.key === ' ')) return;
  if (['ArrowRight', 'PageDown', ' '].includes(e.key)) { e.preventDefault(); show(current + 1, true); }
  else if (['ArrowLeft', 'PageUp'].includes(e.key)) { e.preventDefault(); show(current - 1, true); }
  else if (e.key === 'Home') show(0, true);
  else if (e.key === 'End') show(slides.length - 1, true);
  else if (e.key === 'f' || e.key === 'F') toggleFull();
});
function toggleFull() {
  if (document.fullscreenElement) document.exitFullscreen();
  else if (document.documentElement.requestFullscreen) document.documentElement.requestFullscreen();
}
document.getElementById('prev').addEventListener('click', () => show(current - 1, true));
document.getElementById('next').addEventListener('click', () => show(current + 1, true));
document.getElementById('full').addEventListener('click', toggleFull);
let tx = null;
stage.addEventListener('touchstart', e => { tx = e.touches[0].clientX; }, {passive: true});
stage.addEventListener('touchend', e => {
  if (tx === null || isOpen()) return;
  const dx = e.changedTouches[0].clientX - tx; tx = null;
  if (Math.abs(dx) > 50) show(current + (dx < 0 ? 1 : -1), true);
});
const chrome = document.getElementById('chrome');
let idle;
addEventListener('mousemove', () => { chrome.classList.add('show'); clearTimeout(idle); idle = setTimeout(() => chrome.classList.remove('show'), 2000); });
addEventListener('resize', fit);
addEventListener('hashchange', fromHash);
addEventListener('popstate', fromHash);
setTimeout(() => document.getElementById('hint').classList.add('gone'), 4500);
fit(); fromHash();
"""


def build_deck(deck_dir, slug, number, label, total_sessions):
    deck = json.loads((deck_dir / "deck.json").read_text(encoding="utf-8"))
    order = deck["order"]
    parts, marks_used = [], 0
    for index, slide_id in enumerate(order, 1):
        soup = BeautifulSoup((deck_dir / "slides" / f"{slide_id}.html").read_text(encoding="utf-8"), "html.parser")
        section = soup.find("section")
        notes = section.find("aside")
        if notes:
            notes.decompose()
        section["class"] = ["slide"]
        section["data-index"] = str(index)
        section["role"] = "region"
        section["aria-roledescription"] = "slide"
        section["aria-label"] = f"{index} of {len(order)}"
        for text, key in marks_by_slide.get(slide_id, []):
            target = next((t for t in section.find_all(["p", "h3"]) if t.get_text(strip=True) == text), None)
            if target is None:
                sys.exit(f"mark not found: {slug} {slide_id!r} {text!r}")
            cell = target.parent
            cell["data-detail"] = key
            cell["role"] = "button"
            cell["tabindex"] = "0"
            cell["aria-label"] = f"More about {text}"
            marker = soup.new_tag("span", attrs={"class": "more", "aria-hidden": "true"})
            marker.string = "+"
            target.append(marker)
            marks_used += 1
        parts.append(str(section))
    data = json_script({"details": resolved() if marks_used else {}, "report": REPORT, "fonts": FONTS})
    hint = "← → to move · click + for detail · F for full screen" if marks_used else "← → to move · F for full screen"
    title = deck["title"]
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="Session {number} of {total_sessions} of the Wallet Time Machine futures workshop: {label.lower()}.">
<style>{DECK_CSS}</style>
</head>
<body>
<main id="stage" aria-label="{title} slides">
{chr(10).join(parts)}
</main>
<div id="scrim"></div>
<aside id="drawer" role="dialog" aria-modal="true" aria-labelledby="drawer-title" aria-hidden="true"></aside>
<nav id="chrome" aria-label="Slide controls">
<a href="index.html">All sessions</a>
<button type="button" id="prev" aria-label="Previous slide">←</button>
<button type="button" id="next" aria-label="Next slide">→</button>
<button type="button" id="full" aria-label="Full screen">⛶</button>
</nav>
<p id="hint">{hint}</p>
<noscript><p style="position:fixed;inset:auto 0 0 0;padding:16px;background:#E74D3D;color:#EEE5D7;font-family:Arial,sans-serif">This deck needs JavaScript to move between slides.</p></noscript>
<script type="application/json" id="data">{data}</script>
<script>{DECK_JS}</script>
</body>
</html>
"""
    out = out_dir / f"{slug}.html"
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size // 1024} KB, {len(order)} slides, {marks_used} detail links)")
    return len(order)


counts = [build_deck(d, slug, n, label, len(SESSIONS)) for n, (d, (slug, label, _)) in enumerate(zip(deck_dirs, SESSIONS), 1)]

LANDING_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#EEE5D7;color:#192026;font-family:'Inter Tight',Arial,sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:1200px;margin:0 auto;padding:clamp(24px,6vw,80px) clamp(16px,5vw,64px) 56px;display:flex;flex-direction:column;gap:clamp(40px,7vw,80px)}
.mono{font-family:'JetBrains Mono','Courier New',monospace;font-size:14px;letter-spacing:1px;text-transform:uppercase}
header{display:flex;flex-direction:column;gap:20px;border-top:2px solid #192026;padding-top:14px;position:relative}
header .mark{position:absolute;right:0;top:14px;width:clamp(28px,4vw,48px);height:clamp(28px,4vw,48px);background:#E74D3D}
header .mono{padding-right:clamp(44px,6vw,72px)}
h1{font-size:clamp(44px,9vw,104px);font-weight:700;line-height:1;letter-spacing:-.03em;max-width:12ch}
.lede{font-size:clamp(18px,2.2vw,24px);line-height:1.4;color:#4E555B;max-width:40ch}
.line{display:grid;grid-template-columns:5fr 1fr 4fr;align-items:center;gap:6px}
.line i{display:block;height:6px;background:#192026}.line i.today{height:16px;background:#E74D3D}.line i.future{background:#416AEE}
.sessions{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:24px}
.session{display:flex;flex-direction:column;gap:12px;border-top:2px solid #192026;padding-top:18px;text-decoration:none;color:inherit}
.session .num{font-size:clamp(56px,8vw,96px);font-weight:700;line-height:1;letter-spacing:-.03em;color:#416AEE}
.session h2{font-size:clamp(26px,3vw,34px);font-weight:700;line-height:1.1;letter-spacing:-.01em}
.session p{font-size:18px;line-height:1.45;color:#4E555B}
.session .go{margin-top:auto;padding-top:8px;color:#192026}
.session:hover .num,.session:focus-visible .num{color:#E74D3D}
.session:focus-visible{outline:3px solid #416AEE;outline-offset:8px}
.more{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:24px}
.more a{display:flex;flex-direction:column;gap:8px;border-top:2px solid #192026;padding-top:14px;text-decoration:none;color:inherit}
.more a span:last-child{font-size:20px;font-weight:700;text-decoration:underline;text-decoration-color:#416AEE;text-decoration-thickness:2px;text-underline-offset:4px}
footer{color:#4E555B;line-height:1.6}
"""

cards = "\n".join(
    f"""<a class="session" href="{slug}.html"><span class="num">{n}</span><h2>{label}</h2><p>{blurb}</p><span class="mono go">{count} slides · Open →</span></a>"""
    for n, ((slug, label, blurb), count) in enumerate(zip(SESSIONS, counts), 1)
)
landing = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wallet Time Machine</title>
<meta name="description" content="A three-session futures workshop on crypto wallets: the past, two futures for 2030 to 2040, and the way back to moves worth making now.">
<style>{LANDING_CSS}</style>
</head>
<body>
<div class="wrap">
<header>
<span class="mark" aria-hidden="true"></span>
<p class="mono">Futures workshop · Three sessions · 60 minutes each</p>
<h1>Wallet Time Machine</h1>
<p class="lede">How crypto wallets evolved, where they could go by 2030, 2035 and 2040, and the moves worth making now.</p>
</header>
<div class="line" aria-hidden="true"><i></i><i class="today"></i><i class="future"></i></div>
<nav class="sessions" aria-label="Sessions">
{cards}
</nav>
<section class="more" aria-label="Background">
<a href="{REPO}facilitation-guide.md"><span class="mono">For the facilitator</span><span>Facilitation guide</span></a>
<a href="{REPO}wallet-evolution-research.md"><span class="mono">The evidence</span><span>Wallet evolution research</span></a>
</section>
<footer class="mono">Arrow keys move between slides · Each slide has its own link · Works offline once downloaded</footer>
</div>
<script type="application/json" id="data">{json_script({"fonts": FONTS})}</script>
<script>const DATA = JSON.parse(document.getElementById('data').textContent);{FONT_JS}</script>
</body>
</html>
"""
(out_dir / "index.html").write_text(landing, encoding="utf-8")
print(f"wrote {out_dir / 'index.html'} (landing)")
