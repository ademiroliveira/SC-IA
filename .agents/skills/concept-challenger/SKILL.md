---
name: concept-challenger
description: Stress-test a product concept before commitment, working through the hardest questions with the user by default or giving a quick verdict on request. Examine user value, evidence, differentiation, feasibility, trust, risks and strategic coherence.
---

# Concept Challenger

## Purpose
Provide a rigorous, constructive challenge to a proposed concept. Surface what must be true, where it is weak, what could invalidate it and what should be tested next. This is not generic SWOT analysis and does not decide on behalf of the team.

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

1. **What and why.** Agree what is being challenged and the decision it informs. Ask what worries the user most.
2. **Their assumptions first.** Ask the user what they think must be true for the concept to work, before adding your own.
3. **Fair restatement.** Restate the concept; the user confirms or corrects it.
4. **Lenses.** Propose the three or four most material lenses; the user can add or drop any.
5. **Hard questions.** For each lens, ask the hardest question and let the user answer before giving your assessment.
6. **Critical assumptions.** Rank them together by consequence if false and uncertainty.
7. **Test and recommendation.** Offer two or three small tests; the user picks. Give the recommendation as advice.

“Give me the quick verdict” switches to draft mode.

Useful questions: “What would make this fail?” · “What does the user do instead today?” · “What evidence would make you drop it?”

## Use when
- A concept, proposition or product thesis is drafted.
- A team wants critique before prototyping or stakeholder review.
- Critical assumptions need stress-testing.

If current competitor, market, technical, legal or regulatory evidence is required, identify that as a separate research task. Do not invent external facts.

## Project context

This skill carries no project-specific rules. Each project supplies its own.

1. **Read the project's rules first.** Before producing or saving anything, read the project's instruction files (`CLAUDE.md`, `AGENTS.md` or equivalent) and its README, plus any strategy, research or decision documents relevant to the task. Their rules take precedence over this skill.
2. **Use its language and evidence rules.** Follow the project's vocabulary (including terms it marks as retired), source and citation rules, claim labels and privacy rules.
3. **Respect its write boundaries.** Follow where drafts may be saved, which folders or records must not be changed, and which checks to run on changed files. If a check cannot be run, say so. If the project states no boundaries, do not overwrite sources, save new drafts only when asked, and say where you saved them.
4. **Keep its decisions as they are.** Treat accepted decisions as accepted and open ones as open. Record a decision only when asked.
5. **No project rules?** If the project has no instruction files, ask the user which vocabulary, privacy constraints and save location matter, or proceed with the generic method and say so.
6. **Claim changes only when confirmed.** Report a file change only after the tool confirms it.

Do not present a project's hypotheses as validated or silently change its accepted decisions.

## Challenge lenses
Assess each as **Strong**, **Partial**, **Weak** or **Unknown**, with evidence and rationale. These are qualitative judgements against the material reviewed, not measured performance, user validation or proof of feasibility. Do not invent numeric scores.

1. **User and problem:** Is the user/context clear? Is the problem consequential? Observed, reported, inferred or assumed? What workaround exists? Who may not benefit?
2. **Value and outcome:** What changes for the user? Is this more than feature novelty? Can the outcome be observed? Why switch, adopt or stay?
3. **Differentiation and alternatives:** What does the user do instead? Is the difference meaningful or repackaging? What is defensible? What evidence is missing?
4. **Concept coherence:** Do user, problem, value, model and experience fit? Are key objects distinct? What assumptions about knowledge, trust or behaviour are hidden?
5. **Feasibility and dependencies:** What must exist technically, operationally or through partners? What fails in degraded/adversarial conditions? Is there a thin test of the riskiest assumption?
6. **Trust, safety and control:** Are system actions and user control clear? Are permissions understandable, bounded, inspectable and revocable where relevant? Are costs, risks and failure states visible? Can users recover, pause or exit?
7. **Viability and constraints:** Who benefits and who bears cost? Are incentives aligned? Are distribution, support, compliance and operating costs acknowledged?
8. **Strategic fit:** Does it support the stated direction? Does it create focus or expand scope? What is out of scope? Which decisions does it depend on or conflict with?

For financial/self-custody concepts, explicitly examine custody, authorisation, execution, asset loss, recovery, liquidity, protocol and counterparty risks. Flag counsel questions; do not give legal conclusions.

## Workflow
1. **Restate fairly** the intended user, problem, proposition and outcome, and ask the user to confirm it before challenging.
2. **Separate evidence from assertion** in a compact claim register.
3. **Apply the lenses** and explain Strong/Partial/Weak/Unknown.
4. **Prioritise critical assumptions** by consequence if false and uncertainty.
5. **Construct counter-cases:** why users may not care, may choose an alternative, misunderstand the model or be harmed.
6. **Define disconfirming evidence** for each critical assumption.
7. **Recommend the smallest useful test** that could change a decision. Identify its type: discovery/research, technical feasibility, prototype/usability, commercial, operational, or legal/regulatory counsel review. State the question, method, evidence that would support or weaken the assumption, and decision informed. Do not default to prototyping.
8. **Make a recommendation** once the user has answered the hard questions: Proceed to next learning step / Narrow and revise / Hold pending evidence / Stop. This is advice, not a team decision.

## Default output
1. Concept as understood.
2. Executive challenge — strongest argument for and against.
3. Lens assessment with evidence gaps.
4. Critical assumptions.
5. Failure modes and unintended consequences.
6. What would change my mind.
7. Smallest useful next test — type, question, method, input/participants where relevant, task, disconfirming evidence and decision informed.
8. Recommendation and rationale.
9. Open decisions.

## Quality check
Represent the concept fairly; ground critique or label inference; avoid generic filler; prioritise consequential assumptions; include trust/safety/recovery/exit where relevant; propose a test that distinguishes explanations; keep recommendation proportionate to evidence.

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
- **Opportunity Framer:** problem or user is unclear.
- **Concept Notes Organiser:** raw notes need structure.
- **Milestone Architect:** concept outcome is sufficiently clear.
- **Concept Synthesiser:** multiple concepts need comparison.

Preserve the original concept. Present proposed changes separately; do not imply the team accepted the critique.
