# SC-IA — Self-Custody Investment Account

Research, competitive analysis, problem framing and product design strategy for a self-custody investment account for US investors.

**Status:** hypothesis-led draft, based on desk research only (September 2026). No primary research with the target user yet.

## Positioning under test

> For self-directed US investors who want a deliberate slice of their wealth in digital assets and onchain earning, [project] is a self-custody investment account that keeps them in control of their keys without making them a DeFi operator. Unlike exchange sleeves or raw DeFi front ends, it turns intent and allocation into the only decisions the user has to make.

## Where things stand

- **Earning inside self-custody is no longer white space.** Robinhood, MetaMask, Kraken and Coinbase all ship it, mostly on the same Steakhouse and Morpho curated-vault engine.
- **The investor frame is unclaimed.** No self-custody product is built around allocation, drift and risk contribution. Everyone who has that frame (Schwab, E\*Trade, Wealthfront) is custodial.
- **Robinhood is the closest threat.** It has a brokerage-native audience, a self-custody wallet, an earn product and its own chain.
- **The strategic bet:** allocation is the unit of the product. The user writes a policy, the product executes it exactly, every return names its source and risk, and recovery is rehearsed before meaningful money arrives.

## Read in this order

| # | Doc | What it covers |
|---|---|---|
| 01 | [Market and opportunity research](research/01-market-and-opportunity-research.md) | US market size, regulation, user behaviour, technology enablers and ranked opportunities |
| 02 | [Competitive analysis](research/02-competitive-analysis.md) | Nine competitors and six adjacent groups scored against the five claims in the positioning; threats; white space |
| 03 | [Problem framing](strategy/03-problem-framing.md) | Problem statement, users and job to be done, evidence levels, constraints, research plan |
| 04 | [Product design strategy](strategy/04-product-design-strategy.md) | Vision, five principles, strategic bets and sequencing, success criteria, trust-critical moments, handoff |
| — | [Decision log](decisions/decision-log.md) | What has been decided about the work and what is still open |
| 05 | Design system strategy brief *(not yet written)* | New components: risk card, policy builder, custody map, allocation and drift views, eligibility states, transaction-state vocabulary |
| 06 | [Experience map](strategy/06-experience-map.md) | The seven trust-critical stages mapped for the primary user: questions, pain today, design response, emotional curve, stress cases |

Numbers are the reading order, and each doc builds on the ones before it. New docs continue the sequence (05, 06, …) in the folder that fits: `research/` for evidence, `strategy/` for framing and direction. The decision log is unnumbered because it runs alongside all of them.

## Repository layout

```
research/    evidence: market research and competitive analysis
strategy/    problem framing, the design strategy that answers it, and the experience map
             (images in strategy/assets/)
decisions/   decision log: decided and open
```

## Next steps

1. Hands-on teardown of Robinhood Wallet and MetaMask Money Account.
2. Counsel review of the discretion model and the word "account".
3. Generative interviews with brokerage-native investors.
4. Prototype tests of the allocation home, policy authoring and the recovery drill.
5. Write the design system strategy brief.

## Caveats

Claims marked "no one ships X" mean no evidence was found on public pages, not a tested absence. Several figures come from vendor or secondary sources and are flagged in each doc. Regulatory points are research-based inferences, not legal advice.

## Live versions

The strategy, framing, competitive analysis and experience map also exist as editable Claude docs, linked from the top of each file, and copies of the framing and strategy sit in the "Secret" Claude project. Those links are private: readers without access should treat this repo as the source.

This repo is the organized record. If a live doc changes, update the matching file here and the sync date below.

**Last synced with live docs:** 2026-09-30
