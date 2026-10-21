# /monthly-rescore — monthly

Runs on the 1st of each month. Six agents re-check the whole market against the baseline and the month's weekly watch files, and propose a rescored scorecard and category matrix. Nothing is applied: AO accepts or rejects each proposal. Read `CLAUDE.md` first. Work from the root of the SC-IA clone.

## Step 0: Set up

- **Today** is the run date in Europe/Dublin. The file is named for the month just ended: a run on November 1, 2026 writes `watch/rescore-2026-10.md`.
- **Window.** From the day after the window end recorded in the Source log of the newest `watch/rescore-*.md`, through today. With no rescore yet, start the day after the baseline's as-of date. At most 35 days; note any gap.
- **Baseline, seen list, pending proposals and due events:** as in Step 0 of `.claude/commands/competitive-watch.md`.
- **This month's weekly files.** Read every `watch/YYYY-MM-DD.md` inside the window. Their verified findings count as already covered.

## Step 1: Read the signal reports

Clone `https://github.com/ademiroliveira/weekly-signals` read-only, as in the weekly command, and read every `signals/*.md` dated inside the window. Note the items that touch a scored player, a claim, a lens or an open decision.

## Step 2: Research (6 agents in parallel)

Spawn `direct-threats`, `wallet-challengers`, `pricing-naming`, `recovery-custody`, `voice-of-user` and `reports-regulation` at once, in mode `monthly`. Give each: today, the window, the seen list, the pending proposals, and what is already covered in its lane (weekly findings and signal-report items). Give `pricing-naming` the due events.

All agents share one search limit for the session, so hold each to the monthly budget in the contract. Handle hand-offs as in the weekly command.

## Step 3: Verify

Spawn two `verifier` agents in mode `items`, each on half the findings. Drop every FAIL and apply every ADJUST.

## Step 4: Write the rescore

Write `watch/rescore-<YYYY-MM>.md` in the format below. Number new proposals `R-<YYYYMM>-1`, `-2` and so on. Carry every pending weekly proposal into the Pending section with a recommendation, rather than proposing it again.

## Step 5: Check the draft

Spawn `verifier` in mode `draft` on the file and apply every REMOVE and FIX. Then run `python3 watch/check.py watch/rescore-<YYYY-MM>.md` and fix anything it flags.

## Step 6: Update the watchlist and sources

As in Step 6 of the weekly command.

## Step 7: Commit and push

As in Step 7 of the weekly command, with the message `rescore: <YYYY-MM>`.

## Step 8: Summary

End with the summary in `<routine_summary>` tags. The first sentence is the banner: `<n> proposed changes for <month>: <short list>.` Then include the pending proposals with their recommendations, the biggest new claim or player if any, and any problem (a failed push, a blocked source, a gap in the window).

---

## Format

```markdown
# Monthly rescore — <Month YYYY>

<One or two sentences: what moved this month and what it means for the positioning.>

## Bottom line

1. <3 to 5 points, most important first>

## Proposed score changes

| Id | Player or category | Claim | From → To | Deciding evidence | Source | Date |
| --- | --- | --- | --- | --- | --- | --- |

## Proposed scorecard

<The full scorecard from the baseline, every row and cell, with changed cells written "Partial → Yes (R-202611-1)">

## Proposed category matrix

<The full category matrix from the baseline, with changed cells marked the same way>

## Trust layer

<Changes to L1 to L8 by competitor, or "No changes.">

## New claims and players

<Candidate claims, competitor claims the positioning does not answer, new players to score>

## Pending proposals

| Id | Proposal | Proposed | Recommendation | Why |
| --- | --- | --- | --- | --- |
| W-20261026-1 | Coinbase C5′ No → Partial | 2026-10-26 | Accept / Reject / Check by hand | <one line> |

## What to check by hand next

- <Hands-on teardowns or checks that agents cannot do>

## Watchlist

- <Event>: happened / moved / still waiting

## Sources

- [Title](url) [tag], <date>: <what it supports>

## Source log

- Window: <start> to <end>
- <agent>: <n> fetched → <n> in window → <n> verified → <n> included
- Verifier: <n> FAIL, with one-line reasons
- Entry points whose status changed
```
