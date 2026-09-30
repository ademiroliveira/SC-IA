# Product Design Strategy — Self-Custody Investment Account

As of September 30, 2026 · Author: AO · Live doc: https://claude.ai/code/artifact/2d69e259-fb98-4e49-973c-6e4e7b83e414

## Summary

The design problem is not making DeFi easier; it is letting a brokerage-minded US investor hold a sized slice of onchain assets with real control, without becoming an operator and without trusting a black box.

**The bet.** Make allocation, not tokens, the unit of the product. The user writes a policy (target share, drift bands, limits, ask-first thresholds), the product executes it exactly, every return names its source and risk, and recovery is proven before meaningful money arrives.

**Why it is worth pursuing.** Earning inside self-custody is now table stakes (Robinhood, MetaMask, Kraken and Coinbase all ship a version on the same Steakhouse and Morpho engine). No one ships the investor frame with keys held by the user, and everyone who has the investor frame (Schwab, E\*Trade, Wealthfront) is custodial. See the [competitive analysis](../research/02-competitive-analysis.md).

**How much to trust this draft.** It rests on desk research only. The market, regulatory and competitor claims are well sourced; the claims about what this user wants and will pay for are hypotheses, because no primary research with brokerage-native investors exists yet. The evidence level of each claim is set out in the [Problem Framing](03-problem-framing.md).

**Three decisions the strategy cannot avoid.**

1. **Discretion model.** Either users author every rule and the product executes without discretion, or a registered adviser or named curator provides the discretionary parts. This sets how far automation can go.
2. **How to use the word "account".** It signals an investor product but invites insurance and reversal expectations that self-custody cannot meet.
3. **First scope.** Which sleeves launch first (dollar earn, BTC and ETH, tokenized treasuries) and in which states.

## The problem, in brief

The problem, users, evidence, constraints and research plan live in the [Problem Framing](03-problem-framing.md); this strategy is the answer to it.

In one line: a brokerage-minded investor who wants a deliberate slice of digital assets has no product that lets them size it, earn on it and keep their keys without becoming a DeFi operator. The core tension is that the more the product decides, the less it is self-custody; the less it decides, the more the user operates. This strategy resolves it by giving authorship to the user and execution to the product, within the regulatory constraints listed in the framing doc.

## Design vision and principles

> [Project] helps self-directed investors hold a deliberate slice of digital assets by making allocation and policy the only decisions they make, and by showing the source, risk and custody of everything underneath, so that they feel in control of an asset class they cannot afford to misunderstand.

Five principles follow, each resolving a named tension and each usable to settle a real design argument.

| # | Principle | Tension it resolves | In practice |
| --- | --- | --- | --- |
| 1 | **You decide; we execute exactly** | Automation vs control | Every automated action traces to a rule the user wrote, and the rule is shown when the action runs |
| 2 | **Name the source of every return** | Simplicity vs risk legibility | No bare APY: each rate splits into base, incentive, expiry, source and named curator, in plain words first, with full detail (curator parameters, calldata) one tap away |
| 3 | **Friction where it is irreversible** | Speed vs safety | Recovery is set up and rehearsed before larger balances; new payees and large exits wait out a cooling-off delay; routine rebalances inside policy stay one tap |
| 4 | **Say what we cannot do** | Self-custody vs "account" | Always show who holds which key and what the product can and cannot do: it cannot move, freeze or reverse funds |
| 5 | **Portfolio first, built for the drawdown** | Crypto-native breadth vs investor wellbeing | Home shows allocation against target and risk contribution, not a token list; no points, streaks or trading nudges; "stay the course" framing when prices fall 50%, as bitcoin did between October 2025 and June 2026 |

Principles 1 and 2 will be tested most in design reviews, because each makes a feature slower or less exciting than a competitor's. They are also the hardest for an incumbent with a trading-first business to copy.

## Strategic bets

The strategy commits to five design bets that competitors do not make, matches them on the basics they already do well, and deliberately skips the rest.

| Bet | What it means | Why it is defensible | Evidence level |
| --- | --- | --- | --- |
| **1. Allocation is the home screen** | Target share of net worth, drift and risk contribution lead; the token list is secondary | No self-custody competitor does it; brokerages own the frame but are custodial | Inference |
| **2. Risk is shown, not hidden** | A multi-dimensional risk card (contract, collateral, liquidity, issuer, depeg, regulatory) with curator named; no single green score | Needs a methodology and ongoing data; curated vaults failed in the Stream case | Inference |
| **3. The policy is the core object** | User signs a plain-language investment policy that every automated action cites | Fits the non-discretion constraint and moves trust from the brand to the user's own rules | Hypothesis |
| **4. Recovery is rehearsed** | Drill before larger balances; guardian or co-signer options; inheritance | Trust accrues over time; seed-phrase wallets would have to change their model | Inference |
| **5. Records are native** | Tax-lot records, brokerage slice import, statements | Self-custody gets no 1099-DA; third-party tools break on transfers | Inference |

**Where we match, not lead.** Earn in one action, transaction simulation, fiat on-ramp, and clear eligibility and disclosure states. Users will compare these against Robinhood, Coinbase and MetaMask.

**What we are explicitly not doing.**

- Competing on headline APY or on price for plain bitcoin exposure, where ETFs and brokerages win.
- Gamified trading, points or streaks.
- Curating vaults on the user's behalf without a disclosed, selectable curator.
- Implying insurance, reversal or advice the product cannot provide.

**Suggested sequencing.** Each phase is gated by evidence, not by date.

1. **Foundation.** Custody map, rehearsed recovery, policy authoring, and one dollar-earn sleeve with the risk card. Gate: the policy and recovery hypotheses hold in testing.
2. **Investor layer.** Allocation home, drift and rebalancing inside policy, native records and brokerage slice import. Gate: brokerage-native users fund more with the allocation home than with a token list.
3. **Extension.** Human-in-the-loop proposals from an assistant, tokenized treasuries with eligibility states, more sleeves. Gate: counsel confirms the discretion model.

## Design success criteria

Success means users fund the account, understand what they own, and stay in control through a drawdown. Targets are left blank on purpose: this is a new product with no baseline, so they should be set with PM after the prototype rounds in the framing doc's research plan.

| Signal | Why it matters | How measured | Target |
| --- | --- | --- | --- |
| Share of onboarded users who fund beyond a small starter balance | Tests whether trust is earned, not just sign-up | Product analytics | Set after prototype baseline |
| Share who rehearse recovery before a larger deposit | Principle 3 working as intended | Product analytics | Set after prototype baseline |
| Share who write their own policy rather than abandoning setup | Tests bet 3 and the non-discretion model | Product analytics and usability tests | Set after prototype baseline |
| Share who correctly say the product cannot reverse or insure funds | Principle 4; guards against "account" misreadings | Comprehension survey at onboarding and 30 days | Set after wording test |
| Share who can name the source and main risk of their earn sleeve | Principle 2 | In-product check and survey | Set after choice experiment |
| Users who hold their policy through a fall of 30% or more, rather than exiting | Principle 5 | Cohort analysis during drawdowns | Set after first drawdown |
| Funds lost through actions outside the user's policy | Principle 1; the one number that should be zero | Incident log | Zero |

**What failure looks like.** Users believe their funds are insured or reversible. Users pick the highest rate without knowing its source. Most users abandon at the recovery step. Support contacts are dominated by "undo this transaction" requests.

## Trust-critical moments

Trust is won or lost at seven moments in the journey; onboarding and funding are the likely make-or-break points, which is a hypothesis to test.

| Stage | The user's question | What design must get right | Principle |
| --- | --- | --- | --- |
| **Discover** | "Is this legitimate, and is it for me?" | Custody explainer; honest comparison with an ETF, including when the ETF is better; regulatory status in plain words | 4 |
| **Onboard** | "What if I lose access?" | Passkey-first setup; layered recovery with explained trade-offs; a rehearsed recovery drill; a scam-awareness moment | 3, 4 |
| **Fund** | "What will this cost and where does my money go?" | Exact fees and arrival time; which chain and why, or abstracted with an audit trail; address-poisoning defence | 3 |
| **Allocate** | "How much should this be?" | Target tied to net worth; risk-contribution view; a signed policy summary | 1, 5 |
| **Earn** | "Where does this return come from, and what could go wrong?" | Look-through risk card; base versus boosted rate; exit-time estimate; curator named | 2 |
| **Monitor** | "Do I need to do anything?" | Drift alerts; incident banners that say what action is needed; statements and tax-lot view; stay-the-course framing in a drawdown | 5 |
| **Exit or recover** | "Can I get out, and can my family?" | Unwind preview with liquidity timing; time-locked recovery; beneficiary flow; delay on large exits under duress | 3 |

The transaction-state vocabulary needs to be shared across every stage: Draft, Simulated, Awaiting signature, Submitted, Pending, Confirmed, Final, plus Partially filled, Failed, Reverted and Delayed by policy. Every state should show fees paid, what changed in the portfolio, and the policy rule that authorized it.

## Handoff to execution

Once the phase 1 gates pass, detailed design moves to four streams, each with its own guide.

| Stream | What it covers | Guide |
| --- | --- | --- |
| **Web3 execution** | Transaction states, fee display, chain abstraction, passkey and recovery flows, signing and simulation | web3-design-ux skill |
| **Agent and automation UX** | Phase 3 assistant proposals: human-in-the-loop confirmation, action history, what the agent may do inside policy | agent-ux-design skill |
| **Design system** | New components: risk card, policy builder, custody map, allocation and drift views, eligibility states, the shared transaction-state vocabulary | Design system strategy brief (next artifact to write) |
| **Experience map** | The seven trust-critical stages above, mapped in detail for the primary user | Experience map (next artifact to write) |

## Open decisions and sources

Five decisions remain open and should be owned before detailed design starts. They are tracked in the [decision log](../decisions/decision-log.md).

- [ ] Discretion model: user-authored policy only, or a registered adviser or named curator for managed parts.
- [ ] Naming: whether "account" stays, and which alternatives go into the wording test.
- [ ] First scope: which sleeves and which states launch first.
- [ ] Business model: subscription, spread or another source, and how to avoid incentives that push higher-risk vaults.
- [ ] Recovery partner: who co-signs or guards, and who bears liability if that partner fails.

**Sources.** This strategy answers the [Problem Framing](03-problem-framing.md), which holds the evidence base, constraints and research plan. It also draws on the [market research](../research/01-market-and-opportunity-research.md) and the [competitive analysis](../research/02-competitive-analysis.md), which lists every public page used. Regulatory points are not legal advice.
