# Researcher contract

Every research agent in the competitive watch follows this file. Each agent's own file in `.claude/agents/` says what it covers. Repo rules, claims, lenses and source tags are in `CLAUDE.md`.

## What you receive

- Today's date, the **mode** (`weekly` or `monthly`) and the **window** (start and end, inclusive).
- The **seen list**: URLs already used in earlier watch files and in the baseline's Sources section.
- **Pending proposals**: ids not yet accepted or rejected. Do not propose them again; report only new evidence on them.
- **Already covered**: items from the weekly signal report (and, in monthly mode, from this month's weekly watch files) in your lane. Extend them; do not repeat them.

## How to work

1. **Know the baseline.** Read the scorecard, the category matrix and the trust-layer table in the baseline (`CLAUDE.md` says where) for the players you cover.
2. **Start with your entry points** in `watch/sources.md`. Fetch them and look for anything that changed inside the window. Then search wider with WebSearch, adding the month and year to your terms.
3. **Check each candidate.** Fetch it. Confirm a publication or "last updated" date is visible and inside the window. Check it against the seen list. Pick the tag from `CLAUDE.md`. Write the summary from the page only.
4. **Report changes, not restatements.** A finding counts when it would move a score, contradicts the baseline, confirms something the baseline marked unverified, or adds a player, claim, risk or dated event.
5. **Stay open to new claims.** Report competitor promises the positioning does not answer, and dimensions users clearly care about that C1 to C9 miss.
6. **Stay in your lane.** List anything for another agent under Hand-offs with its URL.
7. **Prefer first-party sources.** For a product change, find the company's own page before any coverage of it.
8. **Budget.** Weekly: about 12 searches and fetches. Monthly: about 25. Stop early when your area is covered. `No changes this week.` is a complete answer. The session shares one search limit across all agents, so do not overspend.

## Self-check before you return

Drop any item that fails one of these; the verifier will drop it anyway.

- [ ] A date is visible on the page and inside the window
- [ ] The URL is not in the seen list, or a new primary document moves a known story forward
- [ ] The tag is copied from `CLAUDE.md` and fits the source
- [ ] Every figure, name and date in the summary appears on the page
- [ ] No universal claims ("nobody ships X", "first ever") unless the source makes them
- [ ] A proposed score change names the deciding evidence and the score it moves from and to

## Return format

```
- title:
  status: new | contradicts | confirms | new-player | new-claim | event
  player:
  affects: [C1–C9, L1–L8, or an open decision]
  proposed_change: "<player>: C4 Partial → Yes" | none
  source_type: [tag]
  url:
  published: YYYY-MM-DD (as shown on the page)
  summary: 1–2 sentences, only what the source says
  why_it_matters: one sentence; interpretation allowed, no new facts
  confidence: high | med | low
```

Then:

- **Hand-offs:** URLs for other agents, one line each with the lane they belong to.
- **Source log:** one line per entry point or search tried: `source — ok / blocked (reason) / nothing new`. Flag any entry point whose status differs from `watch/sources.md`.
- **Could not verify:** what you looked for and did not find.
