# Time Machine workshop

A two-session futures workshop on the evolution of crypto wallets. Eight people in two teams walk from wallet history to today, build opposing wallet worlds for 2040, 2035 and 2030, then backcast to opportunities worth starting now.

This folder is separate from the SC-IA research and strategy docs. It holds workshop material only, and nothing here changes a score, a claim or a decision.

| File | What it is |
| --- | --- |
| [wallet-evolution-research.md](wallet-evolution-research.md) | Research on how wallets evolved from 2009 to October 2026. The pre-read and the source of the seed signals in the world briefs |
| [facilitation-guide.md](facilitation-guide.md) | Run of show for both sessions: world briefs, timings, prompts, lens cards, board layouts, dot voting, scoring template and facilitator notes |
| [deck/](deck/) | Source of the 14-slide "Wallet Time Machine" deck: the wallet story, the exercise, the four worlds, the board layout and the lens cards |

## Using the deck source

`deck/deck.json` sets the slide order and the two sections (history and exercise). Each file in `deck/slides/` is one slide, written for a 1920 by 1080 canvas with inline styles only. It was built for the Claude Slides artifact type, where `deck.json` and `slides/` sit under a `project/` folder, and it is not a PowerPoint file. To change a slide, edit its HTML file and keep its id in `deck.json`.

## Worlds in one line each

- **Team A, agents under my rules.** Personal agents act under rules the user writes and owns.
- **Team B, institution wallet.** The wallet dissolves into institutional apps and custody is invisible.
- **Default drift (baseline).** Today's wallet, improved step by step. The facilitator holds it.
- **Wildcard, institutional agents.** Agents act inside bank and brokerage rails. Revealed in session 2.
