# SC-IA — Self-Custody Investment Account

Research, competitive analysis, problem framing and product design strategy for a self-custody investment account for US investors.

**Status:** hypothesis-led draft, based on desk research only (September to October 2026). No primary research with the target user yet.

## Positioning under test

> For self-directed US investors who want a deliberate slice of their wealth in digital assets and onchain earning, [project] is a self-custody investment account that keeps them in control of their keys without making them a DeFi operator. Unlike integrated onchain offerings or raw DeFi front ends, it turns intent and allocation into the only decisions the user has to make.

## Where things stand

- **Earning inside self-custody is no longer white space.** Robinhood, MetaMask, Kraken and Coinbase all ship it, mostly on the same Steakhouse and Morpho curated-vault engine.
- **The investor frame is unclaimed.** No self-custody product is built around allocation, drift and risk contribution. Everyone who has that frame (Schwab, E\*Trade, Wealthfront) is custodial.
- **Robinhood is the closest threat.** It has a brokerage-native audience, a self-custody wallet, an earn product and its own chain.
- **The strategic bet:** allocation is the unit of the product. The user writes a policy, the product executes it exactly, every return names its source and risk, and recovery is rehearsed before meaningful money arrives.
- **The outcome it must move:** deliberate holders, meaning investors who hold a sized slice in their own custody, under rules they wrote, and who could recover it. It counts people, not deposits.
- **What could sink it:** 13 of the 23 assumptions behind the strategy are leaps of faith. Three come first: that brokerage-native investors want their own keys (A1), think of crypto as a share of their portfolio (A2), and would write their own rules (A4). One round of generative interviews tests all three.

## Read in this order

| # | Doc | What it covers |
|---|---|---|
| 01 | [Market and opportunity research](research/01-market-and-opportunity-research.md) | US market size, regulation, user behaviour, technology enablers and ranked opportunities |
| 02 | [Competitive analysis](research/02-competitive-analysis.md) | Nine competitors and six adjacent groups scored against the five claims in the positioning; threats; white space |
| 03 | [Problem framing](strategy/03-problem-framing.md) | Problem statement, users and job to be done, evidence levels, constraints, research plan |
| 04 | [Product design strategy (v2)](strategy/04-product-design-strategy.md) | Umbrella outcome and its six components, where we play, five bets with their riskiest assumptions, principles and trust checklist, product model (incomplete), experience, automation stance, research order, open decisions |
| — | [Decision log](decisions/decision-log.md) | What has been decided about the work and what is still open |
| 05 | Design system strategy brief *(not yet written)* | New components: risk card, policy builder, custody map, allocation and drift views, eligibility states, transaction-state vocabulary |
| 06 | [Experience map](strategy/06-experience-map.md) | The seven trust-critical stages mapped for the primary user: questions, pain today, design response, emotional curve, stress cases |
| 07 | [Outcome-led product design deep dive](research/07-outcome-led-design-deep-dive.md) | Where outcome-led design comes from, the main frameworks compared, how it works in practice, its critiques, and four candidate outcomes for this product |
| 08 | [Assumption map](strategy/08-assumption-map.md) | The 23 assumptions behind the strategy, a driver tree, a priority 2x2, the cheapest test and pass signal for each, and the research order |

Numbers are the reading order, and each doc builds on the ones before it, with one exception: strategy v2 (04) was revised after 07 and 08 and draws on both. New docs continue the sequence (05, 06, …) in the folder that fits: `research/` for evidence, `strategy/` for framing and direction. The decision log is unnumbered because it runs alongside all of them.

## Repository layout

```
research/    evidence: market research, competitive analysis, and the outcome-led design deep dive
strategy/    problem framing, the design strategy that answers it, the experience map and the assumption map
             (images in strategy/assets/)
decisions/   decision log: decided and open
```

## Next steps

1. Review the assumption map's ratings and pass signals with PM before the first study.
2. In parallel, with no participants: hands-on teardown of Robinhood Wallet and MetaMask Money Account; counsel review of the discretion and execution model, risk ratings and the word "account"; desk checks on how investors use rules today, segment size and price benchmarks.
3. Generative interviews with brokerage-native and exchange-only investors.
4. Rules and recovery prototypes (the phase 1 gate), then the allocation home prototype (the phase 2 gate).
5. A conceptual-model session to complete the product model in strategy section 6.
6. Write the design system strategy brief once the phase 1 gates pass.

## Caveats

Claims marked "no one ships X" mean no evidence was found on public pages, not a tested absence. Several figures come from vendor or secondary sources and are flagged in each doc. Regulatory points are research-based inferences, not legal advice.

## Live versions

The strategy, framing, competitive analysis, experience map, deep dive and assumption map also exist as editable Claude docs, linked from the top of each file, and copies of the framing and strategy sit in the "Secret" Claude project. Those links are private: readers without access should treat this repo as the source.

This repo is the organized record. If a live doc changes, update the matching file here and the sync date below.

**Last synced with live docs:** 2026-10-05
