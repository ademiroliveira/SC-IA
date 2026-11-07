# REVIEW.md

How AI review runs on every PR. Findings inform people. They never approve or block a PR on their own.

## Passes
1. **Bugs**
2. **Security**
3. **Compliance** with the spec, the plan and the constitution
4. **UX.** Runs only when the PR's UX risk is `review` or `test`. Check the change against the spec's User Experience section:
   - flow and navigation match the spec;
   - every state (loading, empty, error, success) is handled;
   - copy uses glossary terms;
   - only system components are used;
   - the accessibility items are covered.

   Report problems. Never state that the UX is fine. A person decides that.

## What Important means
- **Bugs and security:** {{}}
- **UX:** could stop a user finishing the task, mislead them about {{money, data or consequences}}, or exclude people who use assistive technology.

## Nits
At most {{5}} per review.

## Do not report
- Generated code: `{{paths}}`
- Anything CI already enforces (lint, design-system audit, automated accessibility checks)
- Visual-style opinions not tied to the spec or the design system
