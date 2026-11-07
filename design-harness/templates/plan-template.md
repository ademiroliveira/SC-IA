# Plan: {{FEATURE}} (from `.harness/specs/{{slug}}.md`, {{date}})

Approved by: {{engineer}} · {{tech lead, if high risk}}

<!-- The executor reads this file. Keep it short: with AGENTS.md and the loaded skill, stay under about 30 instructions. -->

## Summary
{{One paragraph: what changes and the approach.}}

## Technical context
- Language / framework: {{}}
- Design system package: {{name, version}}
- Test tools: {{unit, visual, accessibility}}
- Constraints: {{}}

## Constitution check
- [ ] Uses system components only, or new components are approved (II)
- [ ] UX risk class is {{none | review | test}}; an escalation file exists if not `none` (IV)
- [ ] The agent does not update visual baselines (VI)
- [ ] Accessibility checks are listed under Proof (III)

## Files that change
- `{{path}}`: {{why}}

## Do not touch
- `{{protected path}}`

## Order of work
1. {{}}
2. {{}}

## Risks
- {{risk}} → {{mitigation}}

## Proof
Done when all of these pass:

```
{{lint or analyze command}}
{{design-system audit command}}
{{unit and accessibility test command}}
{{visual test command}}
{{ux_risk_command}}   # must print the class stated above
```

People check: {{design approves new visual baselines}} · {{manual a11y pass, if test class}}

## Complexity tracking
Fill in only if a constitution check fails: what is violated, why it is needed, and which simpler option was rejected.
