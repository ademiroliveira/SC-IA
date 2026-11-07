---
name: intent-author
description: Draft an intent.md from an originator's notes, a ticket, an alert or a research finding, using the repo's intent template. Use before any spec or plan exists for a change. Records evidence honestly, lists contradicting research, and never invents evidence.
---

# Intent author

Read `.harness/constitution.md` first. It holds every product rule; this skill holds only the steps.

## Inputs
- The originator's notes, ticket, alert or research trigger
- `.harness/templates/intent-template.md`
- Front matter of the files in `research/insights/`

## Checklist
Copy this list into your reply and tick each item as you go.

- [ ] 1. Read the template and constitution principle I (Evidence before solutions).
- [ ] 2. Write the user goal in the user's terms. If the notes describe a solution, restate the problem it solves and move the solution to "Proposed outcome".
- [ ] 3. Search the insight front matter for the same flow or segment. List insights that support the problem **and** insights that contradict it, by id.
- [ ] 4. Fill "Evidence" only with sources you can point to. If there are none, write `none`. Never write evidence the inputs don't contain.
- [ ] 5. Set "Expected UX risk" from the critical flows in the constitution and the paths in `.harness/ux-risk.yaml`.
- [ ] 6. Fill "How we'll know it worked". Write "baseline unknown" rather than guessing a number.
- [ ] 7. Put anything you are unsure about under "Open questions" instead of deciding it.
- [ ] 8. Set status to `draft` and leave "Accepted by" empty.

## Done when
- Every template heading is present and the intent fits on one screen.
- No evidence row is empty, and nothing in it is invented.
- Status is `draft`.

## Output
Write `.harness/intents/<slug>.md`, then stop and report the path. Do not write a spec or plan.

## Stop and ask
If the inputs don't say who the user is or what they are trying to do, ask the originator before drafting.
