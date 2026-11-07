---
name: plan-writer
description: Write plan.md and tasks.md for the executor from an accepted spec, using the repo's templates. Use after the spec is accepted and before any code changes. Keeps the executor's instruction load under the budget and gives every task a command that checks it.
---

# Plan writer

Read `.harness/constitution.md` first. It holds every product rule; this skill holds only the steps.

## Inputs
- `.harness/specs/<slug>.md` (status must be `accepted`)
- `.harness/templates/plan-template.md` and `tasks-template.md`
- `AGENTS.md` and the build skill the executor will load
- The source files the change touches

## Checklist
Copy this list into your reply and tick each item as you go.

- [ ] 1. Confirm the spec is `accepted`. If not, stop.
- [ ] 2. Run the constitution check in the template. If a check fails, fill "Complexity tracking" and stop for approval.
- [ ] 3. List "Files that change". List "Do not touch": protected paths from the constitution and AGENTS.md, and the visual-baseline folder.
- [ ] 4. Break the work into the smallest steps that can each be verified.
- [ ] 5. Fill "Proof" with exact commands, including the UX risk command and the class it must print.
- [ ] 6. Write one task per step, each with a check command. Add an accessibility-assertion task for every element in the spec's Accessibility section.
- [ ] 7. Count the executor's rules: AGENTS.md + build skill + plan + tasks. If the total is over 30, cut prose and move rationale out of the plan.

## Done when
- Every task has a check command.
- Proof states the expected UX risk class.
- No task asks the executor to judge UX quality or update visual baselines.

## Output
Write `.harness/plans/<slug>.md` and `.harness/tasks/<slug>.md`, then stop and report both paths.
