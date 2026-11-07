---
name: ux-review
description: Run the UX pass from REVIEW.md on a change whose UX risk is review or test. Compares the diff and before/after screenshots with the spec's User Experience section and the constitution, and writes findings to the escalation file. Use in a fresh session, never in the session that wrote the code. It raises flags; it never approves.
---

# UX review

Read `.harness/constitution.md` and `REVIEW.md` first.

## Inputs
- The diff
- `.harness/specs/<slug>.md`
- `.harness/ux-escalations/<slug>.md`
- Before/after screenshots or visual-baseline diffs, if attached

## Checklist
Copy this list into your reply and tick each item as you go.

- [ ] 1. Read the UX risk class from the escalation file or the PR label. If it is `none`, stop: there is no UX pass.
- [ ] 2. Flow and navigation: compare with the spec.
- [ ] 3. States: check that each state in the spec's table is handled in the code.
- [ ] 4. Copy: compare changed strings with the glossary. List every change to critical copy.
- [ ] 5. Components: flag raw values and any new component that wasn't approved.
- [ ] 6. Accessibility: each item in the spec has a test, or is listed for the manual pass.
- [ ] 7. Screenshots: look for layout, hierarchy, truncation and contrast problems. Treat your sense of whether the flow is usable as unknown, because models overrate usability from static screens.
- [ ] 8. Rate each finding Important or Nit, using REVIEW.md. At most five nits.

## Output
Append a section `## AI UX-review findings` to the escalation file. One row per finding: what, where, which spec line or principle, severity.

If you found nothing, write: "No problems found against the spec. A person must still review."

## Never
- Write "approved", "looks good" or "no issues".
- Edit code, the spec or visual baselines.
