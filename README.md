# SC-IA — Self-Custody Investment Account

Research, competitive analysis, problem framing and product design strategy for a self-custody investment account for US investors.

**Status:** hypothesis-led draft, based on desk research only (September to October 2026). No primary research with the target user yet.

## Positioning under test

> For self-directed US investors who want a deliberate slice of their wealth in digital assets and onchain earning, [project] is a self-custody investment account that keeps them in control of their keys without making them a DeFi operator. Unlike integrated onchain offerings or raw DeFi front ends, it turns intent and allocation into the only decisions the user has to make.

## Where things stand

- **Earning inside self-custody is no longer white space.** Robinhood, MetaMask, Kraken and Coinbase all ship it, mostly on the same Steakhouse and Morpho curated-vault engine.
- **The investor frame is unclaimed in US self-custody.** No US self-custody product is built around allocation, drift and risk contribution; outside the US, Glider and Bitwise now run target allocations with automatic rebalancing in the user's own wallet. Everyone in the US who has the frame (Schwab, E\*Trade, Wealthfront, Coinbase Advisor) is custodial.
- **Robinhood is the closest threat.** It has a brokerage-native audience, one-tap self-custody earn inside its main app, and its own chain. Robinhood and Coinbase are answering "intent is the only decision" with AI agents rather than plans (round 2).
- **The strategic bet:** allocation is the unit of the product. The user defines a plan and its rules; the product follows those rules, every return names its source and risk, and recovery is rehearsed before meaningful money arrives.
- **The outcome it must move:** deliberate holders, meaning investors who hold a sized slice in their own custody, under rules they wrote, and who could recover it. It counts people, not deposits.
- **What could sink it:** 13 of the 23 assumptions behind the strategy are leaps of faith. Three come first: that brokerage-native investors want their own keys (A1), think of crypto as a share of their portfolio (A2), and would write their own rules (A4). One round of generative interviews tests all three, and opens with pain discovery (A0), because every pain the strategy answers comes from studies of people who already hold crypto.

## Read in this order

| # | Doc | What it covers |
|---|---|---|
| 01 | [Market and opportunity research](research/01-market-and-opportunity-research.md) | US market size, regulation, user behaviour, technology enablers and ranked opportunities |
| 02 | [Competitive analysis](research/02-competitive-analysis.md) | Nine competitors and six adjacent groups scored against the five claims in the positioning; threats; white space |
| 03 | [Problem framing](strategy/03-problem-framing.md) | Problem statement, users and job to be done, evidence levels, constraints, research plan |
| 04 | [Product design strategy (v2)](strategy/04-product-design-strategy.md) | Umbrella outcome and its six components, where we play, five bets with their riskiest assumptions, principles and trust checklist, product model (incomplete), experience, automation stance, research order, open decisions |
| — | [Decision log](decisions/decision-log.md) | What has been decided about the work and what is still open |
| 05 | Design system strategy brief *(not yet written)* | New components: risk card, plan and rules builder, custody map, allocation and drift views, eligibility states, transaction-state vocabulary |
| 06 | [Experience map](strategy/06-experience-map.md) | The seven trust-critical stages mapped for the primary user: questions, pain today, design response, emotional curve, stress cases |
| 07 | [Outcome-led product design deep dive](research/07-outcome-led-design-deep-dive.md) | Where outcome-led design comes from, the main frameworks compared, how it works in practice, its critiques, and four candidate outcomes for this product |
| 08 | [Assumption map](strategy/08-assumption-map.md) | A0 (the pains we expect are real) and the 23 assumptions behind the strategy, a driver tree, a priority 2x2, the cheapest test and pass signal for each, and the research order |
| 09 | [Critical research questions](strategy/09-critical-research-questions.md) | Pain discovery first, then three decision-level questions (first user, defining a plan, trusting recovery) with hypotheses, conditions and what each result means; supporting interview questions |
| 10 | [Competitive analysis, round 2](research/10-competitive-analysis-round-2.md) | What changed since round 1, a rescored C1–C5 scorecard with new entrants, a revised category matrix, the trust layer by lens, candidate new claims (C5′ to C9) and unanswered competitor claims, price benchmarks, naming and eligibility, regulation, demand and user voice |

Numbers are the reading order, and each doc builds on the ones before it, with one exception: strategy v2 (04) was revised after 07, 08 and 09 and draws on them. New docs continue the sequence (05, 06, …) in the folder that fits: `research/` for evidence, `strategy/` for framing and direction. The decision log is unnumbered because it runs alongside all of them.

## Competitive watch

Scheduled agents keep the competitive analysis current between rounds. Every Monday a weekly watch reads that morning's weekly signal report and checks the scored competitors, new entrants, prices and dated events. On the 1st of each month a rescore re-checks the whole market. Both write to `watch/` and only propose score changes, which the owner accepts or rejects by id. Details are in [watch/README.md](watch/README.md), and the rules are in [CLAUDE.md](CLAUDE.md).

## Concept Development Toolkit

A coordinated set of reusable skills for moving from raw material to a considered product direction. The toolkit has one human-guided orchestrator and five specialist skills, each available to Codex and Claude Code.

| Skill | Use it for | Codex | Claude Code |
| --- | --- | --- | --- |
| **Concept Development Orchestrator** | Route work, coordinate handoffs, preserve evidence and decisions, and assemble outputs | [Open](.agents/skills/concept-development-orchestrator/SKILL.md) | [Open](.claude/skills/concept-development-orchestrator/SKILL.md) |
| **Concept Notes Organiser** | Structure raw notes into a source-faithful concept brief | [Open](.agents/skills/concept-notes-organiser/SKILL.md) | [Open](.claude/skills/concept-notes-organiser/SKILL.md) |
| **Opportunity Framer** | Frame a user problem and opportunity from evidence | [Open](.agents/skills/opportunity-framer/SKILL.md) | [Open](.claude/skills/opportunity-framer/SKILL.md) |
| **Concept Challenger** | Red-team a concept's value, assumptions, risks and feasibility | [Open](.agents/skills/concept-challenger/SKILL.md) | [Open](.claude/skills/concept-challenger/SKILL.md) |
| **Milestone Architect** | Translate direction into North Star, experience and enabling outcomes | [Open](.agents/skills/milestone-architect/SKILL.md) | [Open](.claude/skills/milestone-architect/SKILL.md) |
| **Concept Synthesiser** | Compare concepts and form a traceable strategic narrative | [Open](.agents/skills/concept-synthesiser/SKILL.md) | [Open](.claude/skills/concept-synthesiser/SKILL.md) |

### How to use the toolkit

Every skill works **with you** by default: it plays back what it understood, asks a few questions at a time, offers candidates for the choices that are yours (who, outcome, evidence, what to keep) and builds the output in steps. Say “just draft it” for a one-pass draft that lists the choices it made for you. Each skill also works on its own; none requires another to run first.

Start with the **Concept Development Orchestrator** when work spans several stages or the right skill is unclear. It selects the minimum useful set of specialists and coordinates handoffs. For a focused task, invoke the relevant specialist directly.

A common route is:

`Concept Notes Organiser → Opportunity Framer → Concept Challenger → Milestone Architect`

Use **Concept Synthesiser** when comparing multiple concepts or workstreams; it can be used before, after or instead of other stages. This is a flexible route, not a mandatory sequence.

The orchestrator is a Level 1, human-guided instruction skill. It plans and coordinates, but it does not automatically execute sibling skills unless the host platform explicitly supports that. Where automatic invocation is unavailable, it provides the next skill, context and handoff packet for the user to invoke. It does not make decisions, validate concepts or change the scheduled competitive watch's scope or permissions.

**Example prompts**
- “Help me choose the right skill and plan the work.”
- “Organise these workshop notes into a concept brief.”
- “Frame the opportunity from these research findings. Keep observations separate from hypotheses.”
- “Challenge this proposition. What would make it fail?”
- “Extract a North Star and supporting experience and enabling milestones. Do not invent years.”
- “Compare these three concept briefs and show what should stay separate.”

All specialist skills use a common handoff packet covering the intended decision, source references, findings, evidence status, assumptions, decisions and unresolved questions. Their repository-specific rules defer to `CLAUDE.md`.

## Repository layout

```
research/    evidence: market research, competitive analysis (rounds 1 and 2), and the outcome-led design deep dive
strategy/    problem framing, the design strategy that answers it, the experience map, the assumption map and the critical research questions
             (images in strategy/assets/)
decisions/   decision log: decided and open
watch/       weekly watch and monthly rescore files, the watchlist, entry points and the researcher contract
.agents/     repository-level Agent Skills for Codex
.claude/     Claude Code project agents, commands and skills
CLAUDE.md    rules for any session in this repo: vocabulary, claims, scores, source tags, the watch
```

## Next steps

1. Review the assumption map's ratings and pass signals with PM before the first study.
2. In parallel, with no participants: hands-on teardown of Robinhood Wallet and MetaMask Money Account; counsel review of the discretion and execution model, risk ratings and the word "account"; desk checks on how investors use rules today, segment size and price benchmarks.
3. Generative interviews with brokerage-native and exchange-only investors, opening with pain discovery before any concept is shown.
4. Rules and recovery prototypes (the phase 1 gate), then the allocation home prototype (the phase 2 gate).
5. A conceptual-model session to complete the product model in strategy section 6.
6. Write the design system strategy brief once the phase 1 gates pass.

## Caveats

Claims marked "no one ships X" mean no evidence was found on public pages, not a tested absence. Several figures come from vendor or secondary sources and are flagged in each doc. Regulatory points are research-based inferences, not legal advice.

## Live versions

The strategy, framing, competitive analysis (both rounds), experience map, deep dive, assumption map and critical research questions also exist as editable Claude docs, linked from the top of each file, and copies of the framing and strategy sit in the "Secret" Claude project. Those links are private: readers without access should treat this repo as the source.

This repo is the organized record. If a live doc changes, update the matching file here and the sync date below.

**Last synced with live docs:** 2026-10-20
