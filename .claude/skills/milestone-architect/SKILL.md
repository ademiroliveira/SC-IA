---
name: milestone-architect
description: Translate a product direction into North Star, experience and enabling outcomes using the exact “By [year], [who] can [do what] without [today's friction]” format.
---

# Milestone Architect

## Purpose
Translate a sufficiently clear product direction into an outcome hierarchy. Make progression understandable without turning milestones into feature backlogs or invented delivery roadmaps. This skill does not set dates, commit teams or replace product planning.

## Use when
- A product thesis or concept direction is clear enough to express outcomes.
- A team needs a North Star and supporting milestones.
- Milestones need grouping, de-duplication or sequencing.
- A roadmap mixes user outcomes with features and engineering tasks.

If user, problem or desired outcome is unclear, use Opportunity Framer or Concept Notes Organiser first.

## Repository context
For SC-IA, read `CLAUDE.md`, `README.md` and relevant strategy/decision documents. Use the repository vocabulary: the user defines a plan, its parts are rules, and guardrails are spending and exit limits. Use “deliberate holders” only where appropriate. Distinguish proposed outcomes from validated behaviour. Never invent segments, dates or commitments.

## Canonical format
Every milestone statement must use:

> By [year], [who] can [do what] without [what they do today].

- **Year:** only use a year supplied or accepted by the team. Otherwise retain **[year]** and mark timing “To be sequenced”.
- **Who:** use the intended user or actor in the source; do not invent a persona.
- **Can do what:** one meaningful, observable ability or outcome.
- **Without:** specific current friction or workaround. If unknown, label it a hypothesis or leave it open.
- Avoid feature-delivery statements, vague adjectives and compound outcomes.
- Never quietly promote proposed timing into a commitment.

## Milestone types
- **North Star:** overarching user/customer outcome. Normally one; show alternatives if source contains competing outcomes.
- **Experience:** user-facing abilities that contribute to the North Star.
- **Enabling:** outcomes required from an operator, provider or system-facing actor to make the experience dependable (e.g. reliable data, intelligible risk, recovery readiness, enforceable permissions, execution verification). Keep internal technical deliverables in a dependency list, not as user milestones.

## Workflow
1. **Confirm source direction:** user, problem, thesis, outcome, constraints and accepted decisions. Flag conflicts.
2. **Draft North Star:** ensure it is a user outcome, not a product capability.
3. **Decompose experience outcomes:** work backwards from the North Star and forwards through the user's journey. Keep each milestone distinct.
4. **Identify enabling outcomes:** include only what is necessary to support the experience.
5. **Check completeness:** remove duplicates, split compound statements and expose unsupported assumptions.
6. **Map dependencies:** distinguish hard dependencies from likely sequencing.
7. **Sequence maturity:** use stages only where source supports progression; label recommendations as recommendations.
8. **Define evidence:** propose observable signals without inventing numeric targets or baselines.
9. **Check coherence:** all milestones should support the North Star without claiming more than evidence allows.

## For each milestone include
- **Statement** — canonical sentence.
- **Type** — North Star / Experience / Enabling.
- **User change** — what becomes possible.
- **Evidence status** — Source-backed / Team hypothesis / Suggested framing.
- **Timing** — source-provided year or “To be sequenced”.
- **Dependencies** — hard / likely / none identified.
- **Observable signal** — behaviour or evidence that could show progress.
- **Open question** — material uncertainty, if any.

## Separate outcomes from delivery
Use a companion map: Outcome milestone | Enabling capability/dependency | Delivery activity | Evidence of progress. Keep delivery activities uncommitted unless the source includes an accepted plan, owner and timing.

## Default output
1. North Star.
2. Experience milestones.
3. Enabling milestones.
4. Suggested maturity stages (only if justified).
5. Dependency map.
6. Evidence/measurement signals.
7. Open assumptions and decisions.
8. What is not yet a commitment.

## Quality check
Every statement follows the canonical format; user, outcome and friction are supported or labelled; milestones are distinct; enablers are separate from internal deliverables; dates and sequence are grounded; progress is observable without invented targets.

## Hand-offs
- **Opportunity Framer:** user/problem unclear.
- **Concept Challenger:** test whether outcomes are valuable and credible.
- **Concept Notes Organiser:** direction remains scattered in raw notes.
- **Concept Synthesiser:** multiple milestone sets or concept directions must be reconciled.

A milestone set is a framing aid, not a delivery commitment or evidence of product-market fit.
