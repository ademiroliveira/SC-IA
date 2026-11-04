---
name: concept-synthesiser
description: Compare and synthesise multiple opportunity or concept briefs into a coherent strategic narrative while preserving differences, contradictions and evidence status.
---

# Concept Synthesiser

## Purpose
Bring several related opportunity frames, concept briefs or strategy explorations into a coherent view. Identify shared themes, distinct propositions, tensions, overlaps and possible combinations without flattening meaningful differences.

Synthesis is not consensus by default. It does not decide which concept wins or claim a combination is stronger without evidence.

## Use when
- Several teams/workstreams have overlapping concepts.
- Opportunity or concept briefs need a common narrative.
- Leadership needs to understand convergence, divergence and strategic choices.
- A concept portfolio needs clearer boundaries and relationships.
- Multiple milestone sets need comparison.

Do not merge unrelated ideas because they share a technology, audience label or business area. Different users or jobs may require separate propositions.

## Repository context
For SC-IA, read `CLAUDE.md`, `README.md` and relevant strategy/decision documents. Respect public-source discipline, privacy and vocabulary: the user defines a plan, its parts are rules, and guardrails are spending and exit limits. Use “deliberate holders” only where the connection is justified. Do not merge a new concept into the existing strategy or record a decision without explicit instruction.

## Principles
1. Compare before combining.
2. Preserve provenance: connect every shared theme or proposed combination to its source.
3. Keep evidence status visible: repeated hypotheses are not validated user evidence. Repetition across documents is not independent corroboration when documents derive from the same original source, workshop or assumption; record source lineage and distinguish repeated mention from independent support.
4. Respect differences in users, jobs, risk profiles, operating models and value propositions.
5. Expose trade-offs rather than hiding them in a smooth narrative.
6. Do not mistake frequency in documents for stakeholder agreement.
7. Separate synthesis from recommendation.
8. Preserve source documents.

## Workflow
1. **Inventory inputs:** assign a stable reference to each input and record title, author/team if supplied, date/version, user, problem, proposition, outcome, capabilities, assumptions, constraints, dependencies and decisions. Mark missing fields “Not stated”. Where documents share an underlying source, record that relationship so repeated claims are not counted as independent evidence.
2. **Compare:** user/actor; situation/job; problem/evidence; outcome; proposition; model/capabilities; trust/control/risk; dependencies/operating model; differentiation/alternatives; assumptions/open decisions. For material claims, preserve source references and note whether supporting sources are independent or share a common origin.
3. **Identify patterns:** shared, overlapping, complementary, conflicting and unique elements; gaps; duplicates versus shared components.
4. **Develop options** where appropriate:
   - **Keep separate:** distinct propositions remain distinct.
   - **Shared foundation:** common capabilities/principles, separate experiences.
   - **Integrated proposition:** combine elements with rationale, trade-offs and new assumptions.
5. **Evaluate options:** strategic coherence, user value, complexity, dependencies, risks and evidence needed to choose.
6. **Write the narrative:** common context, connected user outcomes, what is shared/distinct, organising principle and choices ahead.
7. **Reconcile milestones only when justified:** identify duplicate outcomes, dependencies, incompatible timing and missing enablers. Do not combine different users or outcomes.

## Default output
1. Executive synthesis — what connects and what does not.
2. Source inventory — stable source references, document versions and known source relationships.
3. Comparison matrix.
4. Convergence and divergence.
5. Synthesis options, where useful.
6. Recommended organising principle (labelled as recommendation).
7. Strategic narrative.
8. Milestone implications, if supported.
9. Open decisions and evidence gaps.
10. Source trace — each synthesis claim mapped to source documents.

## Quality check
Represent each source fairly; preserve contradictions; trace synthesis claims; distinguish hypotheses from evidence; ensure combinations make sense for users, not only technically; identify new assumptions; show alternatives and trade-offs; preserve source files.

## Handoff packet

When passing this output to another skill or orchestration step, include:
- **Task and intended decision**
- **Inputs and source references**
- **Key findings**
- **Evidence status** — observed, reported, external evidence, interpretation, hypothesis or unknown
- **Assumptions and limitations**
- **Decisions** — accepted, proposed and open, kept separate
- **Unresolved questions**
- **Suggested next step** — only when useful, with rationale

Do not upgrade a recommendation to an accepted decision during handoff. Preserve source references and disagreements. Use “Not stated” rather than filling gaps.

## Hand-offs
- **Opportunity Framer:** problem frames unclear or inconsistent.
- **Concept Notes Organiser:** raw material needs structuring.
- **Concept Challenger:** stress-test an integrated proposition.
- **Milestone Architect:** translate an accepted direction into outcome milestones.

A synthesis is interpretation and recommendation, not stakeholder agreement, validation or an accepted product decision.
