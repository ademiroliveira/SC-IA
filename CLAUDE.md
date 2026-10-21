# SC-IA — Self-Custody Investment Account

Research and product design strategy for a self-custody investment account for self-directed US investors. `README.md` is the map for people. This file holds the rules for any session working in the repo, including the scheduled competitive watch.

> **This repo is public.** Everything in it comes from public sources. Never write employer names, internal product names or internal plans from any other work into any file. `python3 watch/check.py <file>` rejects known internal names.

## Vocabulary

- The user **defines** a **plan**. Its parts are **rules**. **Guardrails** are spending and exit limits. Older docs say "policy" and "write"; do not spread those terms.
- **Deliberate holders** is the umbrella outcome: people who hold a sized slice of digital assets in their own custody, under rules they defined, and who could recover it.

## Claims, scores and lenses

Competitors are scored claim by claim, never on overall similarity.

- **Yes** = shipped and verified on a public page.
- **Partial** = shipped in part or in a different form.
- **No** = no evidence found on public pages. It is not a tested absence; say "not found on the pages checked", never "nobody ships X".
- **By custody** = the provider solves it by holding the assets. **—** = not applicable.

| # | Claim | To match it, a competitor must ship |
| --- | --- | --- |
| C1 | Deliberate slice | A home built around a target share of net worth, drift and rebalancing, not a token list |
| C2 | Keys stay with the user | User-held keys (seed, passkey, MPC or multisig); no provider can move funds |
| C3 | Not a DeFi operator | No chains, gas, bridges or approvals to manage; earn is one action |
| C4 | Onchain earning, legibly | Yield with a named source, base vs incentive, and risk beyond a bare APY |
| C5′ | Your rules, executed exactly | A user-defined plan executed deterministically, including rebalancing inside limits. A model deciding inside a sandbox scores No; user rules enforced by the system (caps, allowlists) score Partial |
| C6 | Cost and realized yield you can see *(candidate)* | Realized net yield, the subsidy and its end date, and all-in yearly cost, beside a T-bill and an ETF |
| C7 | Protected exits *(candidate)* | User-defined delays on large exits, new payees, loosened limits and recovery, with alerts and one-tap cancel |
| C8 | Proven recovery *(candidate)* | Recovery rehearsed before funding and re-checked, not tied to one Apple or Google account |
| C9 | Records that survive the move *(candidate)* | Cost basis carried between wallet and brokerage; income events from lending |

Lenses: **L1** cost beside return · **L2** permissions and one-tap revoke · **L3** friction where irreversible · **L4** recovery · **L5** curator choice · **L6** drawdown behaviour · **L7** naming and disclosure · **L8** eligibility.

**Baseline.** The current scores are in the highest-numbered competitive analysis in `research/` (now `10-competitive-analysis-round-2.md`): the scorecard, the category matrix and the trust-layer table. Proposals accepted after that doc are logged in `decisions/decision-log.md` with their ids.

## Sources

Tag every finding with one of: `[Vendor]` `[Help doc]` `[Terms]` `[Filing]` `[Press]` `[Review]` `[Video]` `[User review]` `[Report]` `[Regulator]`.

- **Fetched URLs only.** Never guess a URL. The publication or "last updated" date must be visible on the page.
- **The source must say it.** Every figure, name and date in a summary appears on the page. Interpretation goes only in the "why it matters" line.
- **Paraphrase.** At most one quote per source, under 15 words, only where exact wording matters (a disclosure line, a rate).
- **Video** means title, description, chapters or transcript only. Never imply a video was watched.
- **No personal names or personal data.** Refer to people by role only ("Coinbase's CEO", "an SEC commissioner"), never by name, including the repo owner. Never write anyone's email address, phone number, social handle or other identifying details, and never name or quote individual forum users or reviewers. `python3 watch/check.py` flags emails, handles and titled names.
- **Regulation.** Regulatory points are research-based readings, not legal advice.

## Competitive watch (scheduled)

| Run | When (Europe/Dublin) | Command | Writes |
| --- | --- | --- | --- |
| Weekly watch | Mondays 07:39, after the weekly signal report | `.claude/commands/competitive-watch.md` | `watch/YYYY-MM-DD.md` |
| Monthly rescore | The 1st of each month, 08:41 | `.claude/commands/monthly-rescore.md` | `watch/rescore-YYYY-MM.md` |

- Scheduled runs write **only under `watch/`**. They never edit `research/`, `strategy/`, `decisions/`, the README or the live Claude docs.
- Score changes are **proposals** with ids: `W-YYYYMMDD-n` from the weekly watch, `R-YYYYMM-n` from the monthly rescore. The repo owner accepts or rejects them. Accepted proposals are applied to the baseline in a normal session and logged in the decision log with their id.
- Agents are in `.claude/agents/`: six research streams and a verifier. All researchers follow `watch/researcher-contract.md`. Entry points are in `watch/sources.md`; dated events are in `watch/watchlist.md`.
- Regulation, recovery and agentic-wallet news come first from the public weekly signal report in the `weekly-signals` repo, under the same GitHub owner as this one. Read it; never write to that repo.
