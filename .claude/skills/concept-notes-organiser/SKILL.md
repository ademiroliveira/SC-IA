---
name: concept-notes-organiser
description: Organise raw product, workshop, research and strategy notes into a source-faithful concept brief. Extract a North Star, experience and enabling milestones in the team's exact “By [year], [who] can [do what] without [today's friction]” format. Use for note synthesis and concept development; do not use to claim validation or make decisions.
---

# Concept Notes Organiser

## Purpose

Turn fragmented notes, workshop outputs, research observations, hypotheses and early ideas into a coherent concept brief that a team can discuss, challenge and develop.

This skill organises thinking. It does not validate a market, decide strategy, settle disagreements or make commitments on behalf of the team.

## When to use

Use when asked to:
- Organise workshop notes, brainstorms, sticky-note exports or meeting notes.
- Bring related observations, opportunities and ideas into one concept.
- Clarify an emerging product thesis or conceptual model.
- Extract a North Star and supporting milestones.
- Restructure an existing concept document without losing its intent.

Do not use as a substitute for primary user research, market validation, competitive/technical/legal/regulatory research, a PRD or a delivery plan unless explicitly requested. Do not combine unrelated concepts; separate them first and explain the proposed grouping.

## Operating principles

1. **Preserve before improving.** Keep the source's terminology, intent, distinctions, contradictions and level of certainty.
2. **Do not invent evidence.** A brainstorm, opinion or team interpretation is not a validated user need or market fact.
3. **Label claim status.** Distinguish source observations, external evidence, team hypotheses, synthesis, recommendations, decisions and open questions.
4. **Keep outcomes central.** Organise around what a person is trying to achieve, not a feature list.
5. **Make the logic traceable.** Connect source material to needs, opportunities, concepts, capabilities and outcomes.
6. **Preserve useful disagreement.** Do not force consensus or silently choose between competing ideas.
7. **Be proportionate.** Use only sections supported by the source; mark gaps rather than filling them with generic content.
8. **Use clear language.** Retain specialist vocabulary where it carries meaning and explain unfamiliar terms.
9. **Do not over-prescribe.** Recommendations remain recommendations until accepted by the team.
10. **Keep the original intact.** Do not overwrite source notes or existing strategy documents unless explicitly asked.

## Repository-specific rules for SC-IA

When used inside the SC-IA repository:

1. Read `CLAUDE.md` and `README.md` before producing or saving repository content. Their rules take precedence over this skill.
2. Follow the repository vocabulary: the user **defines** a **plan**; its parts are **rules**; **guardrails** are spending and exit limits. Do not introduce the older terms “policy” or “write” as current product language. Preserve an old term only when quoting or documenting historical wording.
3. Use **deliberate holders** as the umbrella outcome when the concept concerns the SC-IA product. Do not assume every new idea contributes to it; explain the connection or leave it open.
4. Treat the strategy as hypothesis-led. The repository has no primary research with its target users yet. Do not describe inferred needs, pains or preferences as validated findings.
5. Follow the source, citation and claim rules in `CLAUDE.md` when external research is part of the input. A claim copied from notes is not independently verified by being organised.
6. The repository is public. Never add employer names, internal product names or plans from other work, personal names, contact details or identifying information. Use role descriptions. Run `python3 watch/check.py <file>` on each changed file when working in a local clone.
7. Do not write synthesis into `watch/`, competitive research, the strategy baseline or `decisions/decision-log.md` by default. A new initiative brief may be proposed under `initiatives/` when the user asks to save it. Do not update the decision log unless explicitly asked to record an accepted decision.
8. This is a user-invoked synthesis skill, not part of the scheduled competitive watch. It does not change watch agents' scope or write permissions.

Outside SC-IA, use the vocabulary and constraints of the relevant project and source material; do not import SC-IA assumptions.

## Workflow

### 1. Understand and classify the input

Identify:
- Whether the input is raw notes, workshop output, research evidence, an existing document or a mixture.
- The apparent concept or concepts.
- The intended user or actor, if stated.
- The problem, need, opportunity or desired outcome, if stated.
- Constraints, dependencies, assumptions and decisions.
- What is explicit versus inferred or still being explored.

If the material is ambiguous but usable, proceed with a labelled working interpretation and list the ambiguity. Ask at most one clarification, and only when the missing information prevents useful progress.

### 2. Capture the source signals

Identify main observations, repeated themes, distinct viewpoints, important original phrases, explicit decisions, unresolved questions and gaps.

Preserve note references, headings, timestamps or speaker roles when available. Do not invent attribution. For long sources, provide a concise digest rather than reproducing every note.

### 3. Organise the concept

Use the structure below only where supported by the material.

**Concept snapshot:** Working name and concise description. State intended user, problem and desired outcome only when supported.

**Opportunity:** Separate current situation, user need or tension, opportunity and “why now”. Include the last only when the source supports it. A team belief about a user problem is a hypothesis, not proof that users experience it.

**Product thesis:** Explain the proposed shift. A useful pattern is “From [current way of working] to [desired way of working].” Describe what the user defines or controls and what the product or system enables or coordinates. Keep the thesis provisional unless the source records an accepted decision or validation.

**Concept boundaries:** Make clear what is included, excluded, assumed or undecided. Distinguish the intended outcome from features that might enable it.

**Concept model:** Describe key objects, layers, actors or steps and how they relate. Use the source's model where one exists. Keep concepts separate when the source gives them different jobs; for example, do not collapse a user's goal, a strategy, a set of permissions and an execution plan into one object.

**Experience areas or capability groups:** Group related ideas into a small number of meaningful areas. For each, state its name and purpose, the user question or job it addresses, candidate capabilities or interactions, and known dependencies, constraints or risks. Do not imply brainstormed features are approved.

**Example scenario:** When the notes support it, describe user context or trigger, desired outcome, information or choices, user decision and authorisation, system action or support, and result/feedback. Label illustrative scenarios as examples; do not describe hypothetical behaviour as implemented.

### 4. Extract outcome-led milestones

Use the exact canonical sentence format:

> By [year], [who] can [do what] without [what they do today].

A milestone describes a meaningful change in a person's ability or experience, not a feature delivery statement.

**Rules**
- **By [year]:** Use a date only when the source or team provides it. Otherwise keep the literal placeholder **[year]** and mark timing “To be sequenced”. Never invent a year or quietly turn a suggested horizon into a commitment.
- **[Who]:** Name the user or actor specifically enough to be meaningful. Do not invent a target segment.
- **[Can do what]:** Describe one observable outcome or new ability from that person's perspective.
- **[Without today's friction]:** Describe current manual, fragmented, confusing or burdensome behaviour the milestone aims to reduce. It must be supported by the source or explicitly marked as a hypothesis to validate.
- Keep one primary outcome per milestone. Prefer concrete, testable language over “seamlessly”, “effortlessly” or “intelligently”.
- “Build a dashboard”, “launch an AI agent” and “integrate protocol X” are deliverables or enablers, not user milestones.
- If today's friction is not identified, do not invent it to complete the sentence. Keep the milestone as a candidate and flag the evidence gap.

**Milestone hierarchy**

A. **North Star milestone** — the larger change the concept aims to enable. Normally one statement. If the source contains competing North Stars, show alternatives rather than choosing silently.

B. **Experience milestones** — user-facing abilities that progressively contribute to the North Star.

C. **Enabling milestones** — user, operator or service-provider outcomes needed to enable the experience, such as trusted data, intelligible risk, reliable recovery, safe permissions or dependable execution. Keep internal engineering deliverables in a separate dependency list rather than disguising them as user milestones.

For each milestone include:
- **Statement:** the canonical sentence.
- **Type:** North Star / Experience / Enabling.
- **Why it matters:** one sentence linking it to the concept outcome.
- **Timing:** source-provided year, or “To be sequenced”.
- **Dependencies:** known dependencies; label inferred ones as likely.
- **Confidence:** Source-backed / Team hypothesis / Suggested framing.
- **Evidence gap:** include when the user, friction or outcome needs validation.

**Sequencing:** Group milestones into stages only when the source supports a genuine maturity progression. A possible progression is “Understand and define”, “Compose and control”, “Delegate and maintain”. This is optional, not a default roadmap. Do not force dates, stage names or linear progression onto the material; state when ordering is only a recommendation.

### 5. Quality-check the synthesis

Before presenting, check:
- Can each important synthesis point be traced to source notes or evidence?
- Are observations, reported opinions, hypotheses, synthesis and recommendations distinct?
- Have disagreements and meaningful distinctions been preserved?
- Is the concept framed around a user outcome rather than a feature inventory?
- Are boundaries and unresolved decisions visible?
- Does every milestone follow the exact sentence format?
- Are milestone users and today's friction supported or labelled as hypotheses?
- Are years and maturity stages sourced or left open?
- Are milestones distinct and sequenced by dependency or maturity?
- Have unsupported claims, invented capabilities and premature commitments been removed?
- Has the original source been left intact?
- If saving to the public SC-IA repository, have privacy and validation checks been followed?

## Default output structure

Produce a concise but useful Markdown brief. Use only sections that add value:

1. **Concept snapshot**
2. **Source signals and synthesis**
3. **Opportunity**
4. **Product thesis**
5. **Concept boundaries and model**
6. **Experience areas / capability groups**
7. **Example scenario** (if supported)
8. **Concept milestones**
   - North Star
   - Experience milestones
   - Enabling milestones
   - Optional maturity stages
9. **Assumptions, risks and open questions**
10. **Decisions and next steps**

Add a **Source trace** when input references, IDs, headings or evidence can be mapped. When notes are fragmented, finish with **What I clarified / what I did not assume**: what was grouped or renamed, original terms retained, uncertainty remaining, and recommendations needing agreement.

## Interaction behaviour

- “Organise these notes” → produce the structured synthesis directly.
- “Extract milestones” → focus on the North Star, experience and enabling hierarchy; do not generate an unnecessary full brief.
- “Challenge this concept” → identify gaps, contradictions, unsupported assumptions and competing interpretations before recommending changes.
- “Make it shorter” → preserve the thesis, milestone hierarchy and critical uncertainties.
- “Turn this into a roadmap” → separate outcome milestones from delivery activities, owners, sequencing and dates; do not invent commitments.
- “Save this” → create a new draft file in the appropriate project location. Do not overwrite the source unless explicitly asked.
- When external validation is requested, treat it as a separate research task and distinguish source-derived content, new research and model inference.

## Milestone examples (templates only)

**North Star**

> By [year], [defined user group] can [achieve the larger outcome] without [the current fragmented or manual approach].

**Experience**

> By [year], [user group] can [understand, define, compare, control or verify a meaningful outcome] without [specific current friction].

**Enabling**

> By [year], [user or operator] can [rely on, inspect, recover or govern a required capability] without [specific current limitation].

These are templates, not product claims. Replace every bracketed phrase with source-supported content, or leave it open and label the gap.
