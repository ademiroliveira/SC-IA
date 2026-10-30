# Time Machine workshop

A two-session futures workshop on the evolution of crypto wallets. Eight people in two teams walk from wallet history to today, build opposing wallet worlds for 2040, 2035 and 2030, then backcast to opportunities worth starting now.

This folder is separate from the SC-IA research and strategy docs. It holds workshop material only, and nothing here changes a score, a claim or a decision.

| File | What it is |
| --- | --- |
| [web/index.html](web/index.html) | The deck as one web page: 28 slides, a link per slide, and research detail with sources behind each milestone, number and open problem. Works offline |
| [wallet-evolution-research.md](wallet-evolution-research.md) | Research on how wallets evolved from 2009 to October 2026. The pre-read, the source of the seed signals in the world briefs, and the source of the web deck's detail panels |
| [facilitation-guide.md](facilitation-guide.md) | Run of show for both sessions: world briefs, timings, prompts, lens cards, board layouts, dot voting, scoring template and facilitator notes |
| [deck/](deck/) | Source of the 28-slide "Wallet Time Machine" deck: history, the exercise, and four printable lens cards |

## The web version

- **Online:** https://ademiroliveira.github.io/SC-IA/time-machine-workshop/web/ once GitHub Pages is turned on for this repo.
- **Offline:** download `web/index.html` and open it in any browser. The fonts are built into the file; only the source links in the detail panels need a connection.
- **Controls:** ← and → move between slides, a blue **+** opens the detail behind an item, Esc closes it, and F toggles full screen. Each slide has its own link, such as `#slide-19` for the four worlds. On a phone, swipe.
- **Rebuilding after the deck changes:** the detail text and its sources are in `web/details.py`. Run `python3 web/build.py deck <fonts> web/index.html`, where `<fonts>` holds the unpacked Fontsource npm packages for Inter Tight (variable) and JetBrains Mono (it needs `beautifulsoup4`).
- **Fonts:** Inter Tight and JetBrains Mono, both under the SIL Open Font License.

## Using the deck source

`deck/deck.json` sets the slide order and three sections (history, exercise and lens cards). Each file in `deck/slides/` is one slide, written for a 1920 by 1080 canvas with inline styles only. It was built for the Claude Slides artifact type, where `deck.json` and `slides/` sit under a `project/` folder, and it is not a PowerPoint file. To change a slide, edit its HTML file and keep its id in `deck.json`, then rebuild the web version.

The look: a cream, ink, blue and red palette (`#EEE5D7`, `#192026`, `#416AEE`, `#E74D3D`), Swiss-style grid and rules, Inter Tight for text and JetBrains Mono for labels.

## Worlds in one line each

- **Team A, agents under my rules.** Personal agents act under rules the user writes and owns.
- **Team B, institution wallet.** The wallet dissolves into institutional apps and custody is invisible.
- **Default drift (baseline).** Today's wallet, improved step by step. The facilitator holds it.
- **Wildcard, institutional agents.** Agents act inside bank and brokerage rails. Revealed in session 2.
