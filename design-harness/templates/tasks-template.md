# Tasks: {{FEATURE}}

Plan: `.harness/plans/{{slug}}.md`

Rules: do one task at a time. Run its check before ticking it. If the same check fails twice, write a stuck report and stop. `[P]` marks tasks that can run in parallel.

## Setup
- [ ] T001 {{}} · check: `{{command}}`

## Story 1 (P1)
- [ ] T002 {{}} · check: `{{command}}`
- [ ] T003 [P] {{}} · check: `{{command}}`
- [ ] T004 Add accessibility assertions for {{elements}} · check: `{{command}}`

## Story 2 (P2)
- [ ] T005 {{}} · check: `{{command}}`

## Wrap-up
- [ ] T0xx Run every Proof command in the plan
- [ ] T0xx Run `{{ux_risk_command}}`. If it prints anything but `none`, write the escalation file and stop
- [ ] T0xx Write the PR summary: what changed, proof output, UX risk class
