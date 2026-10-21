# /competitive-watch — weekly

Runs every Monday after AO's weekly signal report. It reports only what changed since the last watch, against the baseline, and proposes score changes without applying them. Read `CLAUDE.md` first. Work from the root of the SC-IA clone.

## Step 0: Set up

- **Today** is the run date in Europe/Dublin.
- **Skip on the 1st.** If today is the 1st of the month, stop: the monthly rescore covers this week. End with `<routine_summary>Weekly watch skipped: the monthly rescore runs today.</routine_summary>`.
- **Window.** From the day after the window end recorded in the Source log of the newest `watch/YYYY-MM-DD.md` or `watch/rescore-YYYY-MM.md`, through today, inclusive, at most 7 days. With no watch files yet, start the day after the baseline's as-of date. If the last file is older than 7 days, use today − 6 through today and note the gap in the Source log.
- **Baseline.** The highest-numbered `research/*competitive-analysis*.md`, plus the newest `watch/rescore-*.md` if it is newer.
- **Seen list.** Every URL in `watch/*.md` and in the baseline's Sources section.
- **Pending proposals.** Every id matching `W-YYYYMMDD-n` or `R-YYYYMM-n` in `watch/*.md` that does not appear in `decisions/decision-log.md`.
- **Due events.** Rows in `watch/watchlist.md` dated inside the window, past their date and still Waiting, or undated and still Waiting.

## Step 1: Read the signal report

Run `git clone --depth 1 https://github.com/ademiroliveira/weekly-signals /tmp/weekly-signals`. It is read-only: never commit or push there. Read the newest `signals/*.md` dated inside the window.

For each of its items that touches a scored player, a claim (C1 to C9), a lens or an open decision, note the title, strength, URL and what it touches. Do not research those items again. If no report falls in the window, say so in the Source log and continue.

## Step 2: Research (3 agents in parallel)

Spawn `direct-threats`, `wallet-challengers` and `pricing-naming` at once, in mode `weekly`. Give each: today, the window, the seen list, the pending proposals, and the signal-report items already covered. Give `pricing-naming` the due events as well.

For each hand-off URL that no agent returned as a finding, fetch it and write it up in the contract's format yourself, or drop it if it fails the self-check.

## Step 3: Verify

Spawn `verifier` in mode `items` on every finding. If there are more than 12, spawn two verifiers, each on half. Drop every FAIL and apply every ADJUST.

## Step 4: Write the watch file

Write `watch/<today>.md` in the format below. Number proposed score changes `W-<today without dashes>-1`, `-2` and so on. Order every section by how much it matters to the positioning, most first. If nothing changed, say so plainly; never pad.

## Step 5: Check the draft

Spawn `verifier` in mode `draft` on the file and apply every REMOVE and FIX. Then run `python3 watch/check.py watch/<today>.md` and fix anything it flags.

## Step 6: Update the watchlist and sources

- In `watch/watchlist.md`, change the Status of events that happened, moved or were cancelled, and add newly announced dated events. Every change cites a source that appears in the watch file.
- In `watch/sources.md`, update the status of any entry point that the Source logs show has changed (now blocked, now working, moved).

## Step 7: Commit and push

Run `git add watch/ && git commit -m "watch: <window>" && git pull --rebase -q && git push`. Retry a failed push once.

If the push is refused for lack of permission and the `add_repo` tool is available, call it for owner `ademiroliveira`, repo `SC-IA`, access `push`, then retry once. If it still fails, paste the whole watch file into your final message so nothing is lost, and name the failure in the summary.

## Step 8: Summary

End with the summary in `<routine_summary>` tags. The first sentence is the banner: either `No score changes this week.` or `<n> proposed score changes: <short list>.` Then include:
- each proposed change id with one line
- anything that contradicts the baseline
- watchlist events that happened
- how many proposals are still pending
- any problem: a failed push, no signal report in the window, a newly blocked source, a gap in the window

---

## Format

```markdown
# Competitive watch — <window, e.g. October 21–26, 2026>

<One sentence: what changed and why it matters, or "No score changes this week.">

## Proposed score changes

| Id | Player | Claim | From → To | Deciding evidence | Source | Date |
| --- | --- | --- | --- | --- | --- | --- |
| W-20261026-1 | Coinbase | C5′ | No → Partial | Trade-size and spending caps now live for agents | [Help doc] [link](url) | 2026-10-24 |

(or "None this week.")

## Other changes

- **<Title>** · <player> · affects <claims or lenses> · <new / contradicts / confirms / new player / new claim>: <summary>. <Why it matters.> [tag] [link](url) · <date>

(or "None this week.")

## From the signal report

- **<Title>** · <strength> · touches <claim or decision>: <one line>. [link](url)

(or "No signal report in the window." or "Nothing in this week's signal report touches the scorecard.")

## New claims and players

(only when there are any)

## Watchlist

- <Event>: happened / moved to <date> / still waiting. <source if changed>

## Pending proposals

- <id>: <one line>, proposed <date>

(or "None.")

## Source log

- Window: <start> to <end> (<gap note if any>)
- <agent>: <n> fetched → <n> in window → <n> verified → <n> included
- Verifier: <n> FAIL, with one-line reasons
- Entry points whose status changed
```
