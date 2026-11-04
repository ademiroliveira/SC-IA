---
name: concept-development-orchestrator
description: Coordinate concept-development work with the user by agreeing which specialist skills to use and in what order, preserving evidence and decisions, and assembling human-reviewable outputs.
---

# Concept Development Orchestrator

## Purpose

Coordinate the Concept Development Toolkit so a person or team can move from source material to a considered product direction without losing context, evidence status, disagreements or decision ownership.

This is a **Level 1, human-guided orchestrator**. It plans, routes, checks handoffs and consolidates outputs. It does not replace specialist skills, conduct research, validate concepts, make product decisions or autonomously execute other skills unless the host platform explicitly supports that capability.

## Responsibility boundaries

- **Orchestrator:** intake, classification, minimum-skill routing, sequence, handoffs, continuity, quality checks and final assembly.
- **Concept Notes Organiser:** structure fragmented notes and extract source-grounded candidate concepts/outcomes.
- **Opportunity Framer:** frame user, problem, evidence and opportunity.
- **Concept Challenger:** red-team value, coherence, feasibility, assumptions and risks.
- **Milestone Architect:** develop North Star, experience and enabling outcomes.
- **Concept Synthesiser:** compare multiple concepts and create traceable synthesis options.
- **Designer/team:** interpret, prioritise, approve and decide.

## Capability and invocation honesty

These repository files are instruction skills, not a guaranteed multi-agent runtime.

- Do not claim to have invoked or received output from another skill unless the host actually executed it and the output is available.
- If the host cannot invoke sibling skills, recommend the skill and provide a ready-to-use handoff packet or prompt. The user may need to invoke it separately.
- Referencing a skill name does not itself execute it.
- Do not claim background monitoring, autonomous collaboration, shared memory or repository writes unless the host actually performed them.
- Keep a useful static plan when orchestration features are unavailable.

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

1. **Intake.** Play back the request, ask what it should help decide and what material exists.
2. **Route.** Propose the minimum route, with why each skill is in or out. The user confirms or changes it before any specialist runs.
3. **Each specialist.** Run it in guided mode, so the user makes that skill's choices.
4. **Each handoff.** Show the handoff packet; the user decides what carries forward.
5. **Assembly.** Assemble only what the user asked for.

If the user wants one skill only, route straight to it. Every specialist works on its own.

## When to use

Use for multi-step concept development, routing decisions, coordination of multiple specialist outputs, or review of a previous concept-development run.

For a focused request that clearly maps to one specialist, use that specialist directly. Do not add process without value.

## Intake

Identify:
1. **Request:** what the person wants produced or decided.
2. **Inputs:** raw notes, research, one concept, multiple concepts, thesis, milestones or existing briefs.
3. **Audience/user:** only where stated.
4. **Decision context:** what the work may inform; otherwise “Not stated”.
5. **Constraints:** scope, timing, format and repository context.
6. **Evidence condition:** source-backed, reported, hypothesis-led, mixed or unknown.
7. **Requested output:** analysis, opportunity frame, challenge, milestones, comparison or another artifact.

Run intake as a short conversation: play back what you understood, ask what the work should help decide and what the user already has, and agree the route before starting. Do not ask users to repeat information already in the sources. In draft mode, state a working interpretation, label the gaps and proceed.

## Routing decision tree

Choose the **minimum useful set**. Skills may be skipped, repeated or revisited. Do not force every request through all five.

| Input or need | Route to | When |
|---|---|---|
| Fragmented notes, workshop output, mixed material | Concept Notes Organiser | Source material first needs structure and source-faithful synthesis |
| Unclear user, situation, need or evidence | Opportunity Framer | The central question is whether a meaningful user opportunity exists |
| Draft concept needs red-team review | Concept Challenger | The proposition is clear enough to test value, coherence, risks or feasibility |
| North Star or outcome hierarchy needed | Milestone Architect | Direction is clear enough to describe meaningful outcomes |
| Multiple concepts/frames/workstreams | Concept Synthesiser | Need to expose overlap, divergence, combinations or strategic choices |

### Routing rules

- **Raw notes plus unclear problem:** Organiser first; then Opportunity Framer only if material supports a useful evidence-aware frame.
- **Solution-heavy notes:** organise ideas without inventing a user problem. Frame what is known and what must be learned only when useful.
- **Clear concept, unclear value or risk:** Challenger directly; do not force the organiser/framer sequence.
- **Clear direction, milestone request:** Milestone Architect directly.
- **Multiple concepts:** Synthesiser can start from existing briefs. Organise only inputs that need it. Challenge an integrated option only when that informs a real choice.
- **Changed assumptions:** revisit the relevant specialist and show what changed.
- **External evidence required:** identify a separate research task. Skills do not establish current market, technical, legal or regulatory facts by themselves.

## Guided workflow

### 1. State the plan

Summarise the request, sources, selected skills, order and expected outputs. Explain why each skill is needed and what is skipped. For a clear single-skill request, keep this brief. Ask the user to confirm or change the route before running any specialist.

### 2. Preserve the source record

For multiple inputs, maintain a source register:

| Source ID | Title/reference | Version/date | Type | Scope/limitations |
|---|---|---|---|---|
| S1 | Source name or link | Known version/date or “Not stated” | Notes/research/brief | Known limits |

Do not invent authors, dates, sample sizes, participant attributes or versions. Preserve originals.

### 3. Run specialist work

Use the selected skill's method and output structure, in guided mode unless the user asked for a draft, so the user makes that skill's choices. Preserve findings, claim labels, contradictions and minority views.

If the platform cannot execute the skill, provide its path and a ready-to-use prompt with the request, relevant sources and handoff packet.

### 4. Validate the handoff

Each output passed to another skill carries this packet:

- **Task and intended decision**
- **Inputs and source references**
- **Key findings**
- **Evidence status** — observed, reported, external evidence, interpretation, hypothesis or unknown
- **Assumptions and limitations**
- **Decisions** — accepted, proposed and open, kept separate
- **Unresolved questions**
- **Suggested next step** — only when useful, with rationale

Use “Not stated” rather than inference. Do not promote recommendations into decisions. Do not treat repeated mentions of a common source or hypothesis as independent corroboration.

### 5. Maintain a lightweight assumption and decision ledger

| Item | Status | Source/owner | Implication |
|---|---|---|---|
| Assumption | Untested / partly supported / supported by supplied evidence | Reference if available | What changes if false |
| Recommendation | Proposed / accepted / rejected | Who accepted it, if stated | Resulting direction |
| Decision | Open / accepted / superseded | Source or decision record | Scope or next step |

Do not infer approval from silence. Do not create formal repository decision records unless explicitly asked.

### 6. Human review gates

Pause when:
- A material ambiguity changes how sources are grouped or interpreted.
- Distinct concepts are about to be combined.
- A recommendation materially changes scope, target user, positioning or direction.
- Proposed milestones or dates could be mistaken for commitments.
- A repository write, overwrite or decision-log update is requested.

In guided mode, show each handoff and let the user decide what carries forward. In draft mode, do not require approval for every routine handoff; continue reversible analysis while labelling recommendations.

### 7. Assemble the requested output

Use only relevant sections. A full brief may include:
1. Concept snapshot and intended user.
2. Source signals and evidence coverage.
3. Opportunity and problem framing.
4. Product thesis and desired outcome.
5. Boundaries, model and experience areas.
6. Scenario/journey, if supported.
7. North Star, experience and enabling milestones, if requested and grounded.
8. Assumptions, risks and dependencies.
9. Alternatives, tensions and open decisions.
10. Recommended next learning/action.
11. Source trace and handoff history.

Do not produce a full brief for a focused request.

## Quality gates

Check:
- Was the minimum useful skill set selected?
- Does each output answer the task it was selected for?
- Are material claims traceable or labelled as interpretation/hypothesis?
- Are common-source repetitions distinguished from independent evidence?
- Are observations, assumptions, model inferences and recommendations distinct?
- Are contradictions preserved?
- Are accepted decisions separate from recommendations?
- Are milestone users, dates and current frictions grounded or left open?
- Are delivery activities separate from outcomes?
- Are originals preserved?
- Has the orchestrator avoided claims about capabilities the host did not perform?

If a gate fails, identify the gap and recommend the smallest corrective step. Do not silently fill it.

## Project context

This skill carries no project-specific rules. Each project supplies its own.

1. **Read the project's rules first.** Before producing or saving anything, read the project's instruction files (`CLAUDE.md`, `AGENTS.md` or equivalent) and its README, plus any strategy, research or decision documents relevant to the task. Their rules take precedence over this skill.
2. **Use its language and evidence rules.** Follow the project's vocabulary (including terms it marks as retired), source and citation rules, claim labels and privacy rules.
3. **Respect its write boundaries.** Follow where drafts may be saved, which folders or records must not be changed, and which checks to run on changed files. If a check cannot be run, say so. If the project states no boundaries, do not overwrite sources, save new drafts only when asked, and say where you saved them.
4. **Keep its decisions as they are.** Treat accepted decisions as accepted and open ones as open. Record a decision only when asked.
5. **No project rules?** If the project has no instruction files, ask the user which vocabulary, privacy constraints and save location matter, or proceed with the generic method and say so.
6. **Claim changes only when confirmed.** Report a file change only after the tool confirms it.

Do not alter any scheduled or automated workflow in the project, or its scope or permissions, during concept orchestration.

## Test scenarios

### A — Messy workshop notes

**Input:** sticky notes, possible user problems, proposed features, contradictions and no explicit decisions.

**Expected:** Organiser first; preserve wording and contradictions; label hypotheses and solution ideas; do not invent pains; use Opportunity Framer only if a useful evidence-aware frame is possible; return source trace, unresolved questions and what was not assumed.

### B — Developed concept needs challenge

**Input:** concise brief with target user, proposition, experience outline and constraints.

**Expected:** Challenger directly; no unnecessary organiser/framer steps; qualitative assessment; critical assumptions; suitable research, technical, commercial, operational or counsel test; recommendation kept separate from team decision.

### C — Competing concept synthesis

**Input:** three briefs with shared capabilities, different users and overlapping claims.

**Expected:** Synthesiser; inventory and version sources; distinguish real convergence from common terminology or common-source repetition; present keep-separate, shared-foundation and integrated options when useful; preserve differences and new assumptions; human approval before treating an integrated option as chosen.

## Interaction behaviour

- “Which skill should I use?” → recommend the minimum useful route.
- “Develop this concept” → propose a short plan, agree it with the user, then work through each skill in guided mode.
- “I only want one skill” → route straight to it; every specialist works on its own.
- “Challenge this” → Challenger directly unless the concept is too fragmented to understand.
- “Compare these concepts” → Synthesiser; organise inputs only if needed.
- “Extract milestones” → Milestone Architect if direction is clear; otherwise state what's missing.
- “Save this” → follow repository write boundaries and confirm only after success.
- “Run the whole toolkit” → explain the useful sequence; do not force irrelevant skills.

The orchestrator is a coordinator, not an autonomous product team. Its success is continuity, traceability, useful routing and better human decisions—not the number of skills invoked.
