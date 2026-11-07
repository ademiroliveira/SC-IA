---
name: ux-escalate
description: Write a UX escalation file and stop, when the UX risk command prints review, test or blocked. Use only at that moment, in the executor session. Hands the decision to a person; does not continue the plan.
---

# UX escalate

## Steps
1. Copy `.harness/templates/ux-escalation-template.md` to `.harness/ux-escalations/<slug>.md`.
2. Fill "Raised by", "Class", "Triggered by" (the rule the command printed) and the spec and plan paths.
3. Under "What changed", write two to five bullets about your diff, in user terms.
4. Fill "Changed strings" if any user-facing text changed.
5. Under "Evidence attached", list the paths of visual-baseline diffs and accessibility test output. Do not create or update baselines.
6. Under "Questions for a person", write what you could not decide.
7. Leave "Decision" and "Test notes" empty.
8. Stop. Report the file path. Do not continue with the plan.

## Done when
The header fields are filled and "Decision" is empty.
