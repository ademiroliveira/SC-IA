# {{Product}} Constitution

Version {{1.0.0}} · Ratified {{YYYY-MM-DD}} · Owners: {{design lead}}, {{engineering lead}}

Every intent, spec, plan and review is checked against these rules. Planners and reviewers read this file; executors do not. Each principle gives the rule, then how it is checked.

## Core principles

### I. Evidence before solutions
Every intent names the user goal and cites evidence (insight IDs, data, support tickets), or says `none`. An intent without evidence ships only as a labelled bet, with a validation step in its success criteria.
**Check:** intent gate, where design co-approves.

### II. The design system is the default
UI uses system components and tokens. No raw colour, size, spacing or type values. A new component or variant needs design approval before it is built.
**Check:** `{{lint or analyzer command}}`, `{{design-system audit command}}`.

### III. Accessibility is a release criterion
Target {{WCAG 2.2 AA}}. Automated checks are required, but they cover only about a third of success criteria. `test`-class changes also need a manual screen-reader and large-text pass.
**Check:** `{{a11y test command}}`; manual pass recorded in the escalation file.

### IV. Machines classify UX risk; people judge it
Every diff gets a class from `ux-risk.yaml`: `none`, `review` or `test`. Agents stop on anything above `none`.
**Check:** `{{ux_risk_command}}` in CI, which also sets the PR label.

### V. AI review raises UX flags; only people clear them
Model reviewers can report UX problems. They cannot approve a `review` or `test` change, because models tend to overrate usability from static screens.
**Check:** branch protection.

### VI. People approve visual baselines
Agents never create or update snapshot or golden baselines. A failing visual test means fix the UI or escalate.
**Check:** CODEOWNERS on `{{visual-baseline-path}}`.

### VII. User failure triggers research, not fixes
Production UX signals (abandonment, error spikes, support tags) open a research trigger. A researcher decides whether it becomes an intent.
**Check:** monitoring routes alerts to `.harness/research-triggers/`.

### VIII. Rules live in code, not prose
Prefer components, lints and tests to instructions. Executor context stays under {{30}} active rules. UX knowledge that can't be coded goes in planner and reviewer context.
**Check:** AGENTS.md and skill review at each amendment.

## Critical flows
Any change to these flows is `test` class. List them by path or route.
- {{e.g. checkout, payment confirmation, account recovery, consent, deletion}}

## Quality gates

| Gate | Blocks | Approver | Required evidence |
|---|---|---|---|
| Intent | Spec | Product + design | User goal; evidence or `none` |
| Spec | Plan | Product; design (UX section); risk owners (flags) | Stories, UX section, success criteria |
| Plan | Build | Engineer; tech lead if high risk | Proof commands |
| UX risk `review` | Merge | Designer | Escalation file, before/after screenshots |
| UX risk `test` | Release | Design lead | 3–5 user test or signed waiver; manual a11y pass |
| Release | Deploy | Tech lead | Green CI; all approvals above |

## Governance
- Amend by PR. The owners above approve.
- Versioning: MAJOR removes or redefines a principle, MINOR adds one, PATCH clarifies wording.
- Every {{quarter}}, review stuck reports, escalations and research triggers. Remove rules that evals show no longer make a difference.
