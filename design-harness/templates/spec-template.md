# Feature Specification: {{FEATURE NAME}}

- **Intent:** `.harness/intents/{{slug}}.md` (accepted {{date}})
- **Status:** draft <!-- draft | accepted -->
- **UX risk:** {{none | review | test}}
- **Approvals:** product {{}} · design, UX section {{}} · risk owners (security, compliance, legal) {{}}

## User Scenarios & Testing *(mandatory)*

### User story 1: {{title}} (P1)
{{The journey in plain language.}}

- **Why this priority:** {{}}
- **Independent test:** {{how this story can be tested on its own}}
- **Evidence:** {{insight IDs from the intent, or none}}

**Acceptance scenarios**
1. **Given** {{state}}, **when** {{action}}, **then** {{outcome}}.
2. **Given** {{}}, **when** {{}}, **then** {{}}.

### User story 2: {{title}} (P2)
{{}}

### Edge cases
- What happens when the user is {{offline / on a slow connection / interrupted / tapping twice}}?
- What happens with {{partial data / an error from a dependency}}?

## User Experience *(mandatory when UX risk is not none)*

### Flow and navigation
Entry points, steps and exits. Does this change navigation or information architecture? If yes, the change is `test` class.

### States
| State | What the user sees | What they can do next |
|---|---|---|
| Loading | | |
| Empty | | |
| Error | | |
| Success | | |

### Content
Key labels, messages and confirmations. Use terms from `{{glossary path}}`. Flag any copy about {{money, consent, irreversible actions}}.

### Components and tokens
| Need | System component | New? |
|---|---|---|
| {{}} | {{}} | {{no}} |

New components need design approval before planning starts.

### Accessibility
- Reading order and labels for key elements: {{}}
- Focus, and announcements for status changes and errors: {{}}
- Large text ({{200%}}) and reflow: {{}}
- Touch targets and contrast are covered by automated checks.

### Design reference
{{Mockup link and version.}} A mockup shows the target look. It is not evidence that the flow works.

## Requirements *(mandatory)*

### Functional requirements
- **FR-001:** System MUST {{capability}}.
- **FR-002:** System MUST {{capability}} [NEEDS CLARIFICATION: {{question}}].

### Key entities *(include if the feature involves data)*
- **{{Entity}}:** {{what it represents, key attributes, relationships}}

## Success Criteria *(mandatory)*
Each criterion names a baseline and how it is measured in production.
- **SC-001:** {{task success, e.g. share completing without an error}}
- **SC-002:** {{abandonment or error rate on the flow}}
- **SC-003:** {{technical or business metric}}

## Flagged concerns
| Concern | Risk owner | Resolution |
|---|---|---|
| {{}} | {{}} | {{}} |

## Assumptions
- {{}}
