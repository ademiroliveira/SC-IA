---
name: opportunity-framer
description: Frame product opportunities from research and observations without jumping to a solution, working step by step with the user by default or drafting in one pass on request. Separate evidence, interpretation, user need, opportunity and assumptions.
---

# Opportunity Framer

## Purpose
Create an evidence-aware opportunity frame: whose situation may be improved, what is difficult today, why it matters and what remains unknown. This skill structures evidence; it does not conduct research, validate demand or choose the opportunity.

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

1. **Who and why.** Who the frame is about, and what decision it should inform.
2. **Evidence.** List what the user has (interviews, desk research, support themes). Show coverage and gaps; ask what they know that is not written down, and label it as reported.
3. **Themes.** Show observation themes with their sources. The user confirms or corrects the reading.
4. **Problem statement.** Offer two or three candidates that differ in user or situation. The user picks and edits.
5. **Opportunity areas.** Propose them solution-neutral. The user ranks them.
6. **Unknowns.** The user ranks unknowns by how much they could change the decision; then draft discovery questions for the top ones.

Useful questions: “What have you seen or heard, as opposed to believe?” · “What do people do today instead?” · “What would change your mind?”

## Use when
- Framing a problem from interviews, research, support themes, analytics or desk research.
- Synthesising observations into needs and opportunity areas.
- Reviewing a problem statement for solution bias.
- Preparing discovery questions.

If the user has no material yet, start by asking what they have seen or heard and from whom. If the source is mostly solution ideas, say so and ask what problem the user believes they solve. Do not reverse-engineer a user problem to justify a preferred solution.

## Source discipline
Label material claims:
- **Observed:** directly present in supplied material.
- **Reported:** stated by a participant or source, not independently verified.
- **External evidence:** supported by a cited source.
- **Interpretation:** reasoned reading of observations.
- **Hypothesis:** plausible but untested.
- **Unknown:** the material cannot answer it.

Preserve source wording, contradictions and minority perspectives. Never invent quotes, participants, sample sizes, prevalence or causal explanations. Cite source IDs, page/line references or URLs when available.

For SC-IA, read `CLAUDE.md` and `README.md`. The strategy is hypothesis-led and has no primary research with the target user yet. Treat brokerage-native investor pains and preferences as hypotheses unless supplied evidence supports them. Use the repository vocabulary: the user defines a plan, its parts are rules, and guardrails are spending and exit limits. Never add employer/internal details or personal identifying information to this public repository.

## Workflow
1. **Establish the evidence base.** Record source, date/context if known, represented users, limitations, missing perspectives and possible bias. Add an evidence-coverage summary: which sources and user perspectives are represented, how direct or indirect the evidence is, what is missing, and whether the material is sufficient for the current framing. Do not use a numeric confidence score without a defensible basis.
2. **Extract observations.** Group by situation, behaviour, workaround, consequence, motivation, concern and context. Do not merge distinct user groups just because comments sound similar.
3. **Frame the problem.** Identify who, situation, current behaviour, friction or unmet need, and evidenced consequence. Keep what happens separate from why you think it happens.
4. **Write a problem statement.** Use: “[User/actor] needs a way to [need] when [situation], because [evidenced consequence].” Mark unsupported parts as hypotheses or leave gaps.
5. **Identify opportunity areas.** Describe user progress without prescribing a feature. Link each opportunity to observations; state beneficiary, context, assumptions, dependencies and unintended consequences.
6. **Create discovery questions.** Prioritise unknowns that could change the framing or decision. For each, state why it matters, evidence that would support/weaken the hypothesis, a suitable learning method and the decision informed.

## Default output
1. **Opportunity frame** — user and context.
2. **Evidence base** — sources, scope and limitations, including source coverage, represented and missing perspectives, evidence directness and sufficiency.
3. **Observation themes** — traceable references.
4. **Problem statement** — with claim status.
5. **Opportunity areas** — outcome-led and solution-neutral.
6. **Assumptions and unknowns** — prioritised by decision impact and uncertainty.
7. **Discovery questions and next learning** — method and decision informed.
8. **What this does not establish** — evidence boundaries.

Use a table when helpful: Claim/theme | Source | Status | Confidence | Unknowns.

## Quality check
- Is the user/context specific without inventing a segment?
- Can observations be traced to sources?
- Are reported statements separate from verified facts?
- Have solution bias, leading questions and unsupported causes been avoided?
- Are contradictions and evidence limitations visible?
- Does each opportunity describe user progress rather than a feature?
- Are learning steps tied to decisions?

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
- **Concept Notes Organiser:** structure a broader body of raw notes.
- **Concept Challenger:** stress-test an existing concept.
- **Milestone Architect:** translate a sufficiently clear outcome into milestones.
- **Concept Synthesiser:** compare or combine multiple opportunity/concept briefs.

An opportunity frame is not a product decision.
