---
name: spec-writer
description: Turn an accepted intent into spec.md using the repo's spec template, including the User Experience section, Given/When/Then acceptance scenarios and measurable success criteria. Use only after the intent's status is accepted. Marks unknowns for clarification instead of deciding them.
---

# Spec writer

Read `.harness/constitution.md` first. It holds every product rule; this skill holds only the steps.

## Inputs
- `.harness/intents/<slug>.md` (status must be `accepted`)
- `.harness/templates/spec-template.md`
- The insight files the intent cites
- The glossary and design-system component list named in the constitution

## Checklist
Copy this list into your reply and tick each item as you go.

- [ ] 1. Confirm the intent is `accepted` and names both approvers. If not, stop.
- [ ] 2. Write one user story per distinct user goal, in priority order. Give each an independent test, Given/When/Then scenarios and the evidence ids from the intent.
- [ ] 3. List edge cases: offline, slow, interrupted, repeated taps, dependency errors, plus any the product's critical flows add.
- [ ] 4. If UX risk is not `none`, fill the whole User Experience section: flow and navigation, every state, content, components, accessibility and design reference.
- [ ] 5. If the change alters navigation or information architecture, set UX risk to `test`.
- [ ] 6. Use system components first. List any new component as "needs design approval".
- [ ] 7. Write requirements as `FR-###: System MUST …`. Mark anything unknown with `[NEEDS CLARIFICATION: …]`. Do not decide open questions from the intent.
- [ ] 8. Write success criteria with a baseline and a measurement. Include at least one user outcome (task success or abandonment).
- [ ] 9. Route each flagged concern to a named risk owner.

## Done when
- Every mandatory section is filled.
- The spec's UX risk is equal to or higher than the intent's.
- No requirement settles a question the intent left open.

## Output
Write `.harness/specs/<slug>.md` with status `draft`, then stop and report the path. Do not write a plan.
