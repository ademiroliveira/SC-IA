# Time Machine workshop

A three-session futures workshop on the evolution of crypto wallets. Eight people walk through wallet history and name the next milestones they want to drive, build two opposing wallet worlds for 2040, 2035 and 2030, then walk back to two or three moves worth starting now.

This folder is separate from the SC-IA research and strategy docs. It holds workshop material only, and nothing here changes a score, a claim or a decision.

| Session | Deck | What happens |
| --- | --- | --- |
| 1. The past | 28 slides | Wallet history as problems that moved, with a guess before each big number. Then each person names milestones to Lead, Join or Watch, and the room votes three or four themes |
| 2. The futures | 15 slides | Two teams each build the world least friendly to their favourite milestone, 2040 first, and say where the milestone sits in every column |
| 3. The way back | 15 slides | Backcast to today, a wildcard world, a pre-mortem, then a vote that sorts moves into no-regret, bet, blind spot or hedge. Ends with owners and a sealed time capsule |

All three sessions share one wall: the milestone band from session 1 in the middle, the worlds above it, the way back below it.

| File | What it is |
| --- | --- |
| [web/index.html](web/index.html) | Landing page for the web version, linking the three session pages. Session 1 has research detail with sources behind each milestone, number and open problem. Works offline |
| [facilitation-guide.md](facilitation-guide.md) | Run of show for all three sessions and the time between them: the wall, world briefs, timings, prompts, lens cards, board layouts, dot voting, the four kinds of move, scoring template, facilitator notes and what happens after |
| [wallet-evolution-research.md](wallet-evolution-research.md) | Research on how wallets evolved from 2009 to October 2026. The pre-read, the source of the seed signals in the world briefs, and the source of the web deck's detail panels |
| [decks/](decks/) | Source of the three "Wallet Time Machine" decks, one folder per session. Decks 2 and 3 end with four printable lens cards |

## Before you run it

Fill in these placeholders in the decks, then rebuild the web version:

- **Session 2, recap slide:** the three or four themes from the session 1 vote, each with its tag and year
- **Session 2, teams slide:** the four names in each team
- **Session 3, capsule slide:** the date to reopen the time capsule, and the date of the 30-day check-in or the team ritual it joins

## The web version

- **Online:** https://ademiroliveira.github.io/SC-IA/time-machine-workshop/web/ once GitHub Pages is turned on for this repo.
- **Offline:** download the four HTML files in `web/` into one folder and open `index.html`, or open a single session page on its own. The fonts are built into each file; only the source links in the detail panels need a connection.
- **Controls:** ← and → move between slides, a blue **+** opens the detail behind an item, Esc closes it, and F toggles full screen. Each slide has its own link, such as `1-the-past.html#slide-23` for the question. On a phone, swipe.
- **Rebuilding after a deck changes:** the detail text and its sources are in `web/details.py`. From this folder, run `python3 web/build.py <fonts> web decks/1-the-past decks/2-the-futures decks/3-the-way-back`, where `<fonts>` holds the unpacked Fontsource npm packages for Inter Tight (variable) and JetBrains Mono (it needs `beautifulsoup4`).
- **Fonts:** Inter Tight and JetBrains Mono, both under the SIL Open Font License.

## Using the deck source

Each folder in `decks/` holds one deck. `deck.json` sets the slide order and sections, and each file in `slides/` is one slide, written for a 1920 by 1080 canvas with inline styles only. The decks were built for the Claude Slides artifact type, where `deck.json` and `slides/` sit under a `project/` folder, and they are not PowerPoint files. To change a slide, edit its HTML file and keep its id in `deck.json`, then rebuild the web version.

The look: a cream, ink, blue and red palette (`#EEE5D7`, `#192026`, `#416AEE`, `#E74D3D`), Swiss-style grid and rules, Inter Tight for text and JetBrains Mono for labels.

## Worlds in one line each

- **Team A, agents under my rules.** Personal agents act under rules the user writes and owns.
- **Team B, institution wallet.** The wallet dissolves into institutional apps and custody is invisible.
- **Default drift (baseline).** Today's wallet, improved step by step. The facilitator holds it.
- **Wildcard, institutional agents.** Agents act inside bank and brokerage rails. Revealed in session 3.
