# Intent: {{short title in user terms}}

- **Status:** draft <!-- draft | accepted | rejected -->
- **Originator:** {{name, role}}
- **Source:** {{idea | ticket | alert | research}}
- **Problem only:** {{no}} <!-- yes = research filing, no solution proposed yet -->
- **Accepted by:** {{product owner, date}} · {{design, date}}

## User goal
What is the user trying to do? One or two sentences, in their terms.

## Problem
What gets in their way, and why? Keep what was observed separate from what is assumed.

## Evidence
| Insight or source | What it shows | Strength |
|---|---|---|
| {{INS-012}} | {{}} | {{observed / reported / assumed}} |

Write `none` if there is no evidence. The intent is then a bet, and "How we'll know it worked" must include a validation step.

## Proposed outcome
What changes for the user. Describe the outcome, not the screen. Leave blank if this is problem only.

## Affected users and systems
{{segments, platforms, services}}

## Constraints
{{regulatory, security, brand, technical, deadline}}

## Expected UX risk
{{none | review | test}}, because {{reason}}. The classifier confirms this on the diff.

## Out of scope
- {{}}

## How we'll know it worked
| Metric | Baseline | Target | Measured by |
|---|---|---|---|
| {{}} | {{}} | {{}} | {{}} |

## Open questions
- {{}}

<!-- Keep this to one screen. If it grows into a PRD, split it into several intents. -->
