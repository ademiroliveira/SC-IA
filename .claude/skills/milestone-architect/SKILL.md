---
name: milestone-architect
description: Work with the user to translate a product direction into North Star, experience and enabling outcomes using the exact “By [year], [who] can [do what] without [today's friction]” format.
---

# Milestone Architect

## Purpose
Translate a sufficiently clear product direction into an outcome hierarchy. Make progression understandable without turning milestones into feature backlogs or invented delivery roadmaps. This skill does not set dates, commit teams or replace product planning.

## How to work with the user

This skill helps the user define the work. It does not hand over a finished answer on the first turn. The user owns the choices: who it is for, the outcome, what counts as evidence, what to keep or drop. The skill brings structure, options and challenge.

**Guided mode (default).**
1. **Start from where the user is.** If invoked with no request, ask what they are working on and offer two or three ways to start. If invoked with material, play back in two or three lines what you understood, name the gaps, and ask.
2. **Ask a few good questions at a time.** At most three per turn, each with one line on why it matters. Where it helps, offer options with a recommended default so the user can answer quickly. Never ask for what the sources already say. Use the host's structured question tool when it has one.
3. **Offer candidates, not conclusions.** For each choice that belongs to the user, propose two or three candidates with the trade-off between them, recommend one when useful, and let the user pick, edit or reject.
4. **Build in steps.** Work through the checkpoints below one at a time. Confirm before moving on, and carry forward what the user decided in their own words.
5. **Assemble at the end.** Produce the full output only once the key choices are made. Mark anything you filled in yourself.

**Draft mode.** When the user asks for a straight answer (“just draft it”, “first pass”, “no questions”) or the task is fully specified, produce the output in one go. List the choices you made on the user's behalf at the top, ask them to confirm or change them, and offer to switch to guided mode.

**Works on its own.** This skill can be used without any other skill in the toolkit. If an input that another skill would normally provide is missing, gather the minimum here through questions instead of sending the user elsewhere. Suggest another skill only as an optional next step.

### Checkpoints for this skill

1. **Who and what changes.** Confirm the user, the change they should experience, and what they do today. If the sources do not settle these, ask.
2. **North Star.** Offer two or three candidates with the trade-off between them. The user picks or rewrites one. Years come only from the user.
3. **Experience milestones.** Walk the user's journey stage by stage. Ask which abilities matter, draft a few at a time, and ask the user to confirm each “without” friction from what they know.
4. **Enabling milestones.** Propose the actors and outcomes the experience depends on; the user keeps or drops each.
5. **Sequence and signals.** Ask whether stages are wanted at all, then agree how progress would be observed. No invented targets.
6. **Milestone set.** Assemble the agreed set.

Useful questions: “Who exactly, in your words?” · “What does this person do today instead?” · “How would you know it happened?”

## Use when
- A product thesis or concept direction is clear enough to express outcomes.
- A team needs a North Star and supporting milestones.
- Milestones need grouping, de-duplication or sequencing.
- A roadmap mixes user outcomes with features and engineering tasks.

If the user, problem or desired outcome is unclear, establish them here with a few questions: who, what changes for them, and what they do today. Suggest Opportunity Framer or Concept Notes Organiser only if the user wants deeper framing first.

## Project context

This skill carries no project-specific rules. Each project supplies its own.

1. **Read the project's rules first.** Before producing or saving anything, read the project's instruction files (`CLAUDE.md`, `AGENTS.md` or equivalent) and its README, plus any strategy, research or decision documents relevant to the task. Their rules take precedence over this skill.
2. **Use its language and evidence rules.** Follow the project's vocabulary (including terms it marks as retired), source and citation rules, claim labels and privacy rules.
3. **Respect its write boundaries.** Follow where drafts may be saved, which folders or records must not be changed, and which checks to run on changed files. If a check cannot be run, say so. If the project states no boundaries, do not overwrite sources, save new drafts only when asked, and say where you saved them.
4. **Keep its decisions as they are.** Treat accepted decisions as accepted and open ones as open. Record a decision only when asked.
5. **No project rules?** If the project has no instruction files, ask the user which vocabulary, privacy constraints and save location matter, or proceed with the generic method and say so.
6. **Claim changes only when confirmed.** Report a file change only after the tool confirms it.

Distinguish proposed outcomes from validated behaviour. Never invent segments, dates or commitments. If the project names an umbrella outcome, connect milestones to it only where the connection is justified.

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
- **Enabling:** outcomes required from an identifiable user, operator, provider or system-facing actor to make the experience dependable (e.g. reliable data, intelligible risk, recovery readiness, enforceable permissions, execution verification). The statement must describe a meaningful change that actor can achieve and the friction it removes. If the only wording is an engineering activity (for example, “integrate transaction simulation”), keep it in the dependency/delivery list, not as a milestone.

## Workflow
1. **Confirm source direction:** user, problem, thesis, outcome, constraints and accepted decisions. Flag conflicts, and ask the user to settle or supply what the sources do not.
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
Every statement follows the canonical format; user, outcome and friction are supported or labelled; milestones are distinct; enablers identify an actor and meaningful outcome, and remain separate from internal deliverables; dates and sequence are grounded; progress is observable without invented targets.

## Handoff packet

When passing this output to another skill or orchestration step, include:
- **Task and intended decision** — why this work was done and what decision it may inform.
- **Inputs and source references** — files, links, note IDs, versions or sections reviewed; use “Not stated” where unavailable.
- **Key findings** — main source-grounded results.
- **Evidence status** — observed, reported, external evidence, interpretation, hypothesis or unknown.
- **Assumptions and limitations** — what remains unproven or outside the input.
- **Decisions** — accepted decisions, proposed recommendations and open decisions kept separate.
- **Unresolved questions** — gaps that could change the next step.
- **Suggested next step** — a skill or activity only when useful, with rationale.

Do not upgrade a recommendation to an accepted decision during handoff. Preserve source references and meaningful disagreements. Use “Not stated” rather than filling gaps.

## Hand-offs
- **Opportunity Framer:** user/problem unclear.
- **Concept Challenger:** test whether outcomes are valuable and credible.
- **Concept Notes Organiser:** direction remains scattered in raw notes.
- **Concept Synthesiser:** multiple milestone sets or concept directions must be reconciled.

A milestone set is a framing aid, not a delivery commitment or evidence of product-market fit.
