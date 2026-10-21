# Competitive watch

Scheduled agents keep the competitive analysis current between rounds. They report what changed against the baseline (the latest competitive analysis in `research/`) and propose score changes. They never apply them.

| Run | When (Europe/Dublin) | What it does | Output |
| --- | --- | --- | --- |
| Weekly watch | Mondays 07:39 | Reads that morning's weekly signal report, then three agents check the scored competitors, new entrants, pricing, eligibility and dated events | `YYYY-MM-DD.md` |
| Monthly rescore | The 1st of each month, 08:41 | Six agents re-check the whole market against the baseline and the month's weekly files, and propose a rescored scorecard and category matrix | `rescore-YYYY-MM.md` |
| Quarterly round | By hand | Hands-on teardowns with real accounts, then a new numbered competitive analysis | `research/NN-competitive-analysis-round-N.md` |

**Accepting a change.** Each proposal has an id (`W-20261026-1`, `R-202611-2`). Tell Claude in a session which ids to accept or reject. Accepted changes are applied to the baseline and its live doc, and logged in `decisions/decision-log.md`. Until then the runs list them as pending and do not propose them again.

**Files here**

- `researcher-contract.md`: how every research agent works and what it returns
- `sources.md`: tested entry points per player and topic, and known blocked sources
- `watchlist.md`: dated events the runs check for
- `check.py`: format and internal-name check run before each commit
