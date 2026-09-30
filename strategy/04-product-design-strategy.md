# Product Design Strategy — Self-Custody Investment Account

As of September 30, 2026 · Author: AO · Live doc: https://claude.ai/code/artifact/2d69e259-fb98-4e49-973c-6e4e7b83e414

## Summary

The design problem is not making DeFi easier; it is letting a brokerage-minded US investor hold a sized slice of onchain assets with real control, without becoming an operator and without trusting a black box.

**The bet.** Make allocation, not tokens, the unit of the product. The user writes a policy (target share, drift bands, limits, ask-first thresholds), the product executes it exactly, every return names its source and risk, and recovery is proven before meaningful money arrives.

**Why it is worth pursuing.** Earning inside self-custody is now table stakes (Robinhood, MetaMask, Kraken and Coinbase all ship a version on the same Steakhouse and Morpho engine). No one ships the investor frame with keys held by the user, and everyone who has the investor frame (Schwab, E\*Trade, Wealthfront) is custodial. See the [competitive analysis](../research/02-competitive-analysis.md).

**How much to trust this draft.** It rests on desk research only. The market, regulatory and competitor claims are well sourced; the claims about what this user wants and will pay for are hypotheses, because no primary research with brokerage-native investors exists yet. The evidence level of each claim is set out in the [Problem Framing](03-problem-framing.md).

**Four decisions the strategy cannot avoid.** All four block phase 1; the full list of six, each tagged with the phase it blocks, is under [Open decisions](#open-decisions-and-sources).

1. **Discretion and execution model.** Who acts when the policy fires: the user signs every action, the user grants the product a limited, revocable permission to act inside the policy, or a registered adviser or named curator provides the discretionary parts. This sets how far automation can go, and whether "we cannot move your funds" stays true.
2. **How to use the word "account".** It signals an investor product but invites insurance and reversal expectations that self-custody cannot meet.
3. **First scope.** Which states launch first, and when BTC and ETH sleeves arrive; the sequencing below starts with a dollar-earn sleeve.
4. **Recovery partner.** Who guards or co-signs recovery, and who is liable if they fail; rehearsed recovery cannot ship without one.

## The problem, in brief

The problem, users, evidence, constraints and research plan live in the [Problem Framing](03-problem-framing.md); this strategy is the answer to it.

In one line: a brokerage-minded investor who wants a deliberate slice of digital assets has no product that lets them size it, earn on it and keep their keys without becoming a DeFi operator. The core tension is that the more the product decides, the less it is self-custody; the less it decides, the more the user operates. This strategy resolves it by giving authorship to the user and execution to the product, within the regulatory constraints listed in the framing doc.

## Design vision and principles

> [Project] helps self-directed investors hold a deliberate slice of digital assets by making allocation, policy and the choice of curator their decisions, and by showing the source, risk, cost and custody of everything underneath, so that they feel in control of an asset class they cannot afford to misunderstand.

Five principles follow, each resolving a named tension and each usable to settle a real design argument.

| # | Principle | Tension it resolves | In practice |
| --- | --- | --- | --- |
| 1 | **You decide; we execute exactly** | Automation vs control | Every automated action traces to a rule the user wrote, and the rule is shown when the action runs. Loosening a rule waits out the same cooling-off delay as a large exit; tightening takes effect at once, so a phished or coerced user cannot raise the limits and drain the account in one step |
| 2 | **Name the source and cost of every return** | Simplicity vs risk legibility | No bare APY: each rate splits into base, incentive, expiry, source, named curator and what each party, including us, is paid, in plain words first, with full detail (curator parameters, calldata) one tap away. An all-in yearly cost sits beside it, comparable with an ETF's fee |
| 3 | **Friction where it is irreversible** | Speed vs safety | Three confirmation levels: actions inside policy run or take one tap; actions above an ask-first threshold need an explicit confirm with a preview; irreversible actions (new payees, large exits, loosening the policy) are confirmed step by step and wait out a cooling-off delay. Recovery is set up and rehearsed before larger balances |
| 4 | **Say what we cannot do** | Self-custody vs "account" | Always show who holds which key and every permission the user has granted, with one-tap revoke. The product cannot reverse, freeze or insure funds, and cannot move them outside the permissions the user granted; support can guide but not undo |
| 5 | **Portfolio first, built for the drawdown** | Crypto-native breadth vs investor wellbeing | Home shows allocation against target and risk contribution, not a token list; no points, streaks or trading nudges. When prices fall sharply (bitcoin fell more than 50% between October 2025 and June 2026), remind users of the target and rules they chose, without telling them to hold or sell |

Principles 1 and 2 will be tested most in design reviews, because each makes a feature slower or less exciting than a competitor's. They are also the hardest for an incumbent with a trading-first business to copy.

## Strategic bets

The strategy commits to five design bets that competitors do not make, matches them on the basics they already do well, and deliberately skips the rest. Each bet carries two evidence levels: whether the gap is open, and whether users want it. Per the framing doc, every claim about what users will choose is a hypothesis until tested.

| Bet | What it means | Why it is hard to copy | Is the gap open? | Do users want it? |
| --- | --- | --- | --- | --- |
| **1. Allocation is the home screen** | Target share of net worth, drift and risk contribution lead; the token list is secondary | On its own it is not: Robinhood has the audience, a self-custody wallet and earn, and could add an allocation view quickly. It becomes hard to copy combined with bets 2 and 3 | Inference; needs hands-on teardown | Hypothesis (research step 4) |
| **2. Risk is shown, not hidden** | A multi-dimensional risk card (contract, collateral, liquidity, issuer, depeg, regulatory) with curator named; no single green score | Needs a methodology and ongoing data; curated vaults failed in the Stream case | Inference | Hypothesis (research step 7) |
| **3. The policy is the core object** | User signs a plain-language investment policy that every automated action cites; any change is shown as a before-and-after diff | Fits the non-discretion constraint and moves trust from the brand to the user's own rules | Inference | Hypothesis (research step 5) |
| **4. Recovery is rehearsed** | Drill before larger balances; guardian or co-signer options; inheritance | Trust accrues over time; seed-phrase wallets would have to change their model | Inference | Hypothesis (research step 6) |
| **5. Records are native** | Tax-lot records, brokerage slice import, statements | Self-custody gets no 1099-DA; third-party tools break on transfers | Inference | Hypothesis; not yet in the research plan |

The moat is the combination, not any single bet: user-written rules, named return sources and no trading nudges all cut against a business that earns from trading, which is why an incumbent is slow to copy them.

**Where we match, not lead.** Earn in one action, transaction simulation, fiat on-ramp, clear eligibility and disclosure states, and limited token approvals with one-tap revoke. Users will compare these against Robinhood, Coinbase and MetaMask. Accessibility is a baseline too: WCAG 2.1 AA, addresses and transaction states that work with screen readers, and no meaning carried by colour alone, including on the risk card. Users aged 55 and over are 28% of recent buyers.

**What we are explicitly not doing.**

- Competing on headline APY or on price for plain bitcoin exposure, where ETFs and brokerages win.
- Gamified trading, points or streaks.
- Curating vaults on the user's behalf without a disclosed, selectable curator.
- Implying insurance, reversal or advice the product cannot provide.
- Unprompted investment suggestions from the assistant, which would be solicitation.

**Suggested sequencing.** Each phase is gated by evidence, not by date. The gates for phases 1 and 2 can be tested with prototypes (research plan steps 4 to 6) before anything is built, so the phases set build order, not the order of learning.

1. **Foundation.** Custody map, rehearsed recovery, policy authoring, and one dollar-earn sleeve with the risk card. Gate: the policy and recovery hypotheses hold in testing, and the execution model is settled with counsel. On its own, phase 1 sits in the half of the positioning competitors already ship; if it is released before phase 2, it should include a minimal allocation view so the first release carries the differentiator.
2. **Investor layer.** Allocation home across dollar, BTC and ETH sleeves, drift and rebalancing inside policy, native records and brokerage slice import. Gate: brokerage-native users fund more with the allocation home than with a token list.
3. **Extension.** An assistant that explains, and prepares actions that carry out rules the user already wrote; it proposes new allocations only when asked, says it is an AI, uses principle 3's confirmation levels and hands off to a person when asked. Also tokenized treasuries with eligibility states, and more sleeves. Gate: counsel confirms the discretion model.

## Design success criteria

Success means users fund the account, understand what they own, and stay in control through a drawdown. Targets are left blank on purpose: this is a new product with no baseline, so they should be set with PM after the prototype rounds in the framing doc's research plan. Business rows tie design to results; counter-metrics catch a principle that costs more than it earns.

| Signal | Why it matters | How measured | Target |
| --- | --- | --- | --- |
| Share of onboarded users who fund beyond a small starter balance | Tests whether trust is earned, not just sign-up | Product analytics | Set after prototype baseline |
| Share who rehearse recovery before a larger deposit | Principle 3 working as intended | Product analytics | Set after prototype baseline |
| Share who write their own policy rather than abandoning setup | Tests bet 3 and the non-discretion model | Product analytics and usability tests | Set after prototype baseline |
| Share who correctly say the product cannot reverse or insure funds | Principle 4; guards against "account" misreadings | Comprehension survey at onboarding and 30 days | Set after wording test |
| Share who can name the source and main risk of their earn sleeve | Principle 2 | In-product check and survey | Set after choice experiment |
| Exits during a fall of 30% or more that are deliberate: made after viewing the user's own target and rules, not straight from a price alert | Principle 5, measured without rewarding the product for keeping money in | Cohort analysis and exit survey | Set after first drawdown |
| Funds lost through actions outside the user's policy | Principle 1; the one number that should be zero | Incident log | Zero |
| **Business:** funded balance per active user | Ties design to revenue under any business model | Product analytics | Set with PM |
| **Business:** funded users still active at 90 days | Trust that lasts beyond the first deposit | Cohort analysis | Set with PM |
| **Counter-metric:** onboarding completion by stage | The recovery drill must not cost more completion than it earns in deposits (research step 6) | Funnel analytics | Set after recovery prototype |
| **Counter-metric:** drop-off at signing | Fee or trust surprise at the moment of commitment | Product analytics | Set after prototype baseline |
| **Counter-metric:** support contacts by type, especially "undo" requests | Principle 4; makes the failure below measurable | Support tagging | Set after launch baseline |

**What failure looks like.** Users believe their funds are insured or reversible. Users cannot say what they have allowed the product to do. Users pick the highest rate without knowing its source. Most users abandon at the recovery step. Support contacts are dominated by "undo this transaction" requests.

## Trust-critical moments

Trust is won or lost at seven moments in the journey; onboarding and funding are the likely make-or-break points, which is a hypothesis to test. The [experience map](06-experience-map.md) sets out each stage in detail.

| Stage | The user's question | What design must get right | Principle |
| --- | --- | --- | --- |
| **Discover** | "Is this legitimate, and is it for me?" | Custody explainer; honest comparison with an ETF, including all-in yearly cost and when the ETF is better; regulatory status in plain words | 2, 4 |
| **Onboard** | "What if I lose access?" | Passkey-first setup; layered recovery with explained trade-offs; a rehearsed recovery drill; a scam-awareness moment | 3, 4 |
| **Fund** | "What will this cost and where does my money go?" | Exact fees in dollars and arrival time; which chain and why, or abstracted with an audit trail; address-poisoning defence | 3 |
| **Allocate** | "How much should this be?" | Target tied to net worth; risk-contribution view; a signed policy summary; any permission granted shown in the custody map | 1, 4, 5 |
| **Earn** | "Where does this return come from, and what could go wrong?" | Look-through risk card; base versus boosted rate; who is paid; exit-time estimate; curator named | 2 |
| **Monitor** | "Do I need to do anything?" | Drift alerts; incident banners that say what action is needed; statements and tax-lot view; a reminder of the user's own target and rules in a drawdown | 5 |
| **Exit or recover** | "Can I get out, and can my family?" | Unwind preview with liquidity timing; time-locked recovery; beneficiary flow; delay on large exits under duress | 3 |

The transaction-state vocabulary needs to be shared across every stage: Draft, Simulated, Awaiting signature, Submitted, Pending, Confirmed, Final, plus Partially filled, Failed, Reverted and Delayed by policy. Every state should show fees paid, what changed in the portfolio, and the policy rule that authorized it.

## Handoff to execution

Once the phase 1 gates pass, detailed design moves to five streams. Each names the deliverable it produces; owners are still to be named with PM.

| Stream | What it covers | Deliverable | Method |
| --- | --- | --- | --- |
| **Web3 execution** | Transaction states, fees in dollars, chain abstraction, passkey and recovery flows, signing and simulation, limited approvals | Web3 flow specs and a design audit | web3-design-ux skill: user-flow template, dApp design checklist |
| **Agent and automation UX** | Phase 3 assistant: what it may propose, confirmation levels, action history, handoff to a person | Agent flow and handoff specs | agent-ux-design skill: flow and handoff templates |
| **Language and disclosures** | "Account" wording, yield language that never says "interest", risk and conflicts disclosures, what support can and cannot do | Copy and disclosure library, reviewed by counsel | web3-design-ux skill: regulatory compliance template; wording survey (research step 8) |
| **Design system** | Risk card, policy builder with before-and-after diff, custody map with granted permissions and one-tap revoke, approvals view, recovery health meter, allocation and drift views, eligibility states, disclosure modules, the shared transaction-state vocabulary; accessible by default | Design system strategy brief (next artifact to write) | product-design-strategy skill: design system brief template |
| **Experience map** | The seven trust-critical stages above, mapped in detail for the primary user | [Experience map](06-experience-map.md) | product-design-strategy skill |

## Open decisions and sources

Six decisions remain open and should be owned before detailed design starts. Each is tagged with the phase it blocks; owners are still to be named in the [decision log](../decisions/decision-log.md).

- [ ] **Discretion and execution model** (blocks phase 1): every action signed by the user; a limited, revocable onchain permission for actions inside the policy; or a registered adviser or named curator for managed parts. It also decides whether "we cannot move your funds" stays true, and needs counsel to confirm the chosen model stays within the non-custodial interface relief.
- [ ] **Naming** (blocks phase 1 copy): whether "account" stays, and which alternatives go into the wording test.
- [ ] **First scope** (blocks phase 1 release): which states launch first, and whether BTC and ETH arrive in phase 1 or phase 2.
- [ ] **Business model** (blocks phase 1 if earn carries a spread): subscription, spread or another source, how any cut is shown under principle 2, and how to avoid incentives that push higher-risk vaults.
- [ ] **Recovery partner** (blocks phase 1): who co-signs or guards, and who bears liability if that partner fails.
- [ ] **Primary user** (blocks phase 1 research recruiting): the brokerage-native investor, or the exchange-only holder as the early adopter. Generative interviews decide it; see the [Problem Framing](03-problem-framing.md#open-questions-and-sources).

**Sources.** This strategy answers the [Problem Framing](03-problem-framing.md), which holds the evidence base, constraints and research plan. It also draws on the [market research](../research/01-market-and-opportunity-research.md) and the [competitive analysis](../research/02-competitive-analysis.md), which lists every public page used. Regulatory points are not legal advice.
