---
name: concept-challenger
description: Stress-test a product concept before commitment. Examine user value, evidence, differentiation, feasibility, trust, risks and strategic coherence.
---

# Concept Challenger

## Purpose
Provide a rigorous, constructive challenge to a proposed concept. Surface what must be true, where it is weak, what could invalidate it and what should be tested next. This is not generic SWOT analysis and does not decide on behalf of the team.

## Use when
- A concept, proposition or product thesis is drafted.
- A team wants critique before prototyping or stakeholder review.
- Critical assumptions need stress-testing.

If current competitor, market, technical, legal or regulatory evidence is required, identify that as a separate research task. Do not invent external facts.

## Repository context
For SC-IA, read `CLAUDE.md`, `README.md` and relevant strategy, problem framing, assumption map and decision-log materials. Respect public-repository privacy and vocabulary: the user defines a plan, its parts are rules, and guardrails are spending and exit limits. The strategy is hypothesis-led and has no primary target-user research yet. Do not present assumptions as validated or silently change accepted decisions.

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
1. **Restate fairly** the intended user, problem, proposition and outcome.
2. **Separate evidence from assertion** in a compact claim register.
3. **Apply the lenses** and explain Strong/Partial/Weak/Unknown.
4. **Prioritise critical assumptions** by consequence if false and uncertainty.
5. **Construct counter-cases:** why users may not care, may choose an alternative, misunderstand the model or be harmed.
6. **Define disconfirming evidence** for each critical assumption.
7. **Recommend the smallest useful test** that could change a decision. Identify its type: discovery/research, technical feasibility, prototype/usability, commercial, operational, or legal/regulatory counsel review. State the question, method, evidence that would support or weaken the assumption, and decision informed. Do not default to prototyping.
8. **Make a recommendation:** Proceed to next learning step / Narrow and revise / Hold pending evidence / Stop. This is advice, not a team decision.

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
