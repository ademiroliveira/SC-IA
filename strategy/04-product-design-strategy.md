# Product Design Strategy v2 — Self-Custody Investment Account

As of October 5, 2026 · Author: AO · Live doc: https://claude.ai/code/artifact/d02bb77f-8e65-4056-b17e-6d4cfe01a856

## Summary

The strategy is to turn brokerage-minded US investors into deliberate holders: people who hold a sized slice of digital assets in their own custody, under rules they wrote, and who could recover it. It does this by making allocation the unit of the product: the user writes a policy, the product executes it exactly, every return names its source and risk, and recovery is rehearsed before meaningful money arrives.

This version is organised as one chain: outcome, need, bets, product model, experience, learning. It is still a hypothesis-led draft built on desk research. No primary research with the target user exists yet.

**What changed from [v1](https://github.com/ademiroliveira/sc-ia/blob/c3610a4/strategy/04-product-design-strategy.md).**

| Change | Why |
| --- | --- |
| An umbrella outcome with six components now leads the doc (section 1) | v1 had bets and principles but nothing they were meant to move |
| New section on the product model (section 6) | v1 relied on objects such as policy and slice without defining them |
| New section on automation stance (section 8) | It was scattered across constraints and phasing, and both the regulatory limit and the agent work depend on it |
| A trust checklist added to the principles (section 5) | Gives a concrete test for every automated action |
| Bets are tied to the outcome; each will carry an assumption and a test (section 4) | Makes clear what would prove a bet wrong |
| Success criteria folded into the outcome section | They were behaviours with blank targets; they now sit under the outcome they measure |
| v1's September 30 revisions carried forward: execution model, granted permissions with one-tap revoke, the cost beside every return, confirmation levels, business and counter-metrics, accessibility, a language and disclosures stream | v2 was first drafted from a copy of v1 that predated them; restored on October 5 |

One section is still marked incomplete: the product model (6), which needs a conceptual-model session. Bets (4) and how we learn (9) now draw on the Assumption Map.

The umbrella outcome, deliberate holders, was confirmed on October 4, 2026. Its six components and the focus for each phase are still proposals.

## 1. Outcome

The umbrella outcome is **deliberate holders**: investors who hold a sized slice in their own custody, under rules they wrote, and who could recover it. It counts people, not deposits, and a person counts only once several things are true of them, so it cannot be met by pushing money in. This framing was chosen on October 4, 2026 over four alternatives.

**Components.** Six component outcomes sit under the umbrella, in journey order. The early ones are leading signals for the later ones.

| Component | The behaviour | What the customer gets | When it can be observed | How it could be gamed |
| --- | --- | --- | --- | --- |
| **Can get back in** | Has completed a rehearsed recovery | They and their family do not lose access | In onboarding | Counting drills started, not finished |
| **Policy in force** | Has written and signed a policy | Their own rules, not ours, govern their money | In setup | Pre-filled policies signed without reading |
| **Funded and understood** | Has funded beyond a starter balance and can say what the product cannot do | A slice they understand and control | In the first weeks | Pushing deposits; the comprehension half blocks that |
| **Knows what they earn** | Can name the source and main risk of their earn sleeve | No surprise losses | When they first use earn | Teaching to the test; check with fresh wording |
| **Sized deliberately** | Holdings stay within the band they chose | The slice stays the size they intended | Over months | Wide default bands that are never breached |
| **Stays the course** | Keeps their policy through a fall of 30% or more | Avoids panic selling and unplanned risk | Only in a drawdown | Making exit hard; see the guardrails |

**Focus.** One component is in focus per phase, while the umbrella stays fixed. Phase 1 focuses on funded and understood, with can get back in and policy in force as its leading signals. Phase 2 moves the focus to sized deliberately. Stays the course cannot guide early work because it needs a real drawdown.

**Guardrails.** Two outcomes sit outside the umbrella and must not get worse while the others improve.

- **Leaves cleanly.** When someone exits, it takes the time and cost they were told.
- **Avoids an irreversible mistake.** Risky actions are caught by a delay or a warning, and funds lost through actions outside the user's policy stay at zero.

**How it connects upward and sideways.**

- **Business impact above it:** assets held under the user's own rules is the candidate. It depends on the open business-model decision.
- **Customer check beside it:** confident owners, meaning investors who can explain what they hold, where returns come from and how they would get back in.

**Reporting.** Always report the six components beside the umbrella, never the umbrella alone, because a composite hides which part moved.

**Targets.** None are set. A new product has no baseline, so targets should be agreed with PM after the prototype rounds.

**Business and counter-metrics.** Two business signals tie the outcome to results: funded balance per active user, and funded users still active at 90 days. Three counter-metrics catch a principle that costs more than it earns: onboarding completion by stage, since the drill must not cost more completion than it earns in deposits; drop-off at signing; and support contacts by type, especially "undo" requests. Their targets are set with PM, like the rest.

**What failure looks like.** Users believe their funds are insured or reversible. Users cannot say what they have allowed the product to do. Users pick the highest rate without knowing its source. Most users abandon at the recovery step. Support contacts are dominated by "undo this transaction" requests.

The components, the focus for each phase, the guardrails and the gaming risks are proposals and have not been tested.

## 2. Problem and evidence

A self-directed investor who wants a deliberate slice of digital assets has no product that lets them size it, earn on it and keep their own keys without becoming a DeFi operator. The full framing, users, constraints and research plan are in the [Problem Framing](03-problem-framing.md) doc.

**Primary user.** The brokerage-native investor: self-directed, $25K or more investable, no crypto or ETF-only exposure, considering a 1% to 5% slice. The secondary user is the exchange-only holder.

**The core tension.** The more the product decides, the less it is self-custody and the closer it is to a regulated manager. The less it decides, the more the user operates. Section 8 states where this strategy sits on that line.

**How solid the foundations are.** A layer-by-layer audit of the v1 docs rated them as follows.

| Layer | State | What that means here |
| --- | --- | --- |
| Observed behaviour | Weak | No primary research; every source studies people who already hold crypto |
| The domain | Partial | Market and regulation well understood; how investors talk about this space is not mapped |
| User needs | Assumed | One job to be done and a user table, both inferred |
| Strategy | Assumed | This doc; its bets rest on the assumed needs |
| Product model | Not started | See section 6 |
| Interaction flows | Not started | Stages listed in section 7, no flows |

The market, risk and competitor facts are well sourced. Every claim about what this user wants, will choose or will pay for is a hypothesis.

**The pains are hypotheses too.** The frictions this strategy answers (fear of losing access, the burden of operating it, not understanding returns and risk, missing records) come from studies of existing crypto holders. No brokerage-native investor has yet named them to us. The first study therefore opens with pain discovery before testing any solution; see the [Critical Research Questions](09-critical-research-questions.md) doc and assumption A0 in the [Assumption Map](08-assumption-map.md).

## 3. Where we play

We differentiate on the investor frame and the trust layer around earning, match competitors on the basics, and concede passive exposure to ETFs.

| Stance | Area | Why |
| --- | --- | --- |
| **Differentiate** | Allocation as the home screen | No self-custody product is built around target share, drift and risk contribution; those who have that frame (Schwab, E\*Trade, Wealthfront) are custodial |
| **Differentiate** | Risk and source of every return shown | Competitors show a bare "up to X%" on the same Steakhouse and Morpho engine |
| **Differentiate** | User-written policy as the core object | Fits the non-discretion constraint; nobody offers portfolio-level policy |
| **Differentiate** | Rehearsed recovery and inheritance | Casa is the benchmark; seed-phrase wallets would have to change their model |
| **Match** | Earn in one action, transaction simulation, fiat on-ramp, eligibility and disclosure states, limited token approvals with one-tap revoke | Users will compare these with Robinhood, Coinbase and MetaMask |
| **Concede** | Plain spot exposure on price | Brokerages charge 50 to 75 bps and ETFs less; say when an ETF is the better tool |

**Accessibility is a baseline too.** WCAG 2.1 AA, addresses and transaction states that work with screen readers, and no meaning carried by colour alone, including on the risk card. Users aged 55 and over are 28% of recent buyers.

**What we are explicitly not doing.**

- Competing on headline APY.
- Gamified trading, points or streaks.
- Curating vaults on the user's behalf without a disclosed, selectable curator.
- Implying insurance, reversal or advice the product cannot provide.
- Unprompted investment suggestions from the assistant, which would be solicitation.

**Closest threat.** Robinhood already combines a brokerage-native audience, a self-custody wallet and an earn product. If it adds an allocation view, the difference narrows to recovery and risk depth. Details are in the [competitive analysis](../research/02-competitive-analysis.md).

## 4. Bets

Five bets are expected to move the umbrella outcome through its components. Each names the component it serves, its riskiest assumption, the cheapest test and the signal that counts as a pass. These come from the [Assumption Map](08-assumption-map.md), which lists all 23 assumptions; the pass signals are proposed and need agreeing before each study.

| Bet | Component it serves | Riskiest assumption | Cheapest test | Pass signal (proposed) |
| --- | --- | --- | --- | --- |
| **1. Allocation is the home screen** | Funded and understood; sized deliberately | A2: they think of crypto as a share of their portfolio | Interviews, then a home-screen prototype | At least 5 of 8 describe their crypto decision as a share or a limit of their total |
| **2. Risk is shown, not hidden** | Knows what they earn | A10: showing the source of a return changes what people choose | Choice experiment | Fewer pick the highest rate when the source is shown, and they can state its main risk |
| **3. The policy is the core object** | Policy in force; stays the course | A4 and A8: they prefer their own rules, and can write them | Interviews, then a rules prototype | Most choose to write or edit rules over a default; 8 of 10 finish a policy and predict what it does |
| **4. Recovery is rehearsed** | Can get back in; funded and understood | A9: a drill builds confidence more than it causes drop-off | Recovery prototype, with and without the drill | Stated deposit is higher with the drill; drop-off stays under an agreed limit |
| **5. Records are native** | Sized deliberately; stays the course | A5: they miss brokerage-style records enough to value them here | Interviews; later a records prototype | Not yet set; lower priority |

**The pain behind each bet.** A bet is only worth testing if the pain it answers is real for this user. None of these pains has been heard from the primary user yet; the pain round at the start of the interviews decides which bets go forward.

| Bet | Pain it answers (expected) | Where the belief comes from | If the pain does not appear |
| --- | --- | --- | --- |
| **1. Allocation is the home screen** | No way to size the amount or keep it sized | Advisor guidance; assumed for individuals | Size in dollars or drop the allocation frame; the main differentiator weakens |
| **2. Risk is shown, not hidden** | Not knowing where a return comes from or what could go wrong | Vault failures and teaser rates; inferred | Keep disclosure as a duty, stop treating it as a selling point |
| **3. The policy is the core object** | The burden of operating it; wanting control over what happens to their money | Industry consensus among holders | Lead with a managed option; the discretion model changes |
| **4. Recovery is rehearsed** | Fear of losing access for good | Studies of existing holders | Keep recovery for safety, stop gating funding on it |
| **5. Records are native** | No records for tax or tracking | Tax rules; inferred | Defer; integrate a third-party tool instead |

Two assumptions sit underneath all five and come first: that brokerage-native investors want to hold their own keys at all, and that they would pay for this. The first is tested by the generative interviews. The second waits for a pricing study.

**Sequencing.** Each phase is gated by evidence, not by date.

1. **Foundation.** Custody map, rehearsed recovery, policy authoring, and one dollar-earn sleeve with the risk card. Gate: the policy and recovery assumptions hold in testing, and the execution model is settled with counsel (section 8). If phase 1 is released before phase 2, it includes a minimal allocation view so the first release carries the differentiator.
2. **Investor layer.** Allocation home, drift and rebalancing inside policy, native records and brokerage slice import. Gate: brokerage-native users fund more with the allocation home than with a token list.
3. **Extension.** An assistant that explains, and prepares actions that carry out rules the user already wrote; it proposes new allocations only when asked, says it is an AI, uses principle 3's confirmation levels and hands off to a person when asked. Also tokenized treasuries with eligibility states, and more sleeves. Gate: counsel confirms the discretion model.

## 5. Principles and trust

> [Project] helps self-directed investors hold a deliberate slice of digital assets by making allocation, policy and the choice of curator their decisions, and by showing the source, risk, cost and custody of everything underneath, so that they feel in control of an asset class they cannot afford to misunderstand.

Five principles settle design arguments. They are v1's principles as revised on September 30: a delay on loosening the policy, the cost beside every return, three confirmation levels, and granted permissions with one-tap revoke.

| # | Principle | Tension it resolves | In practice |
| --- | --- | --- | --- |
| 1 | **You decide; we execute exactly** | Automation vs control | Every automated action traces to a rule the user wrote, and the rule is shown when the action runs. Loosening a rule waits out the same cooling-off delay as a large exit; tightening takes effect at once, so a phished or coerced user cannot raise the limits and drain the account in one step |
| 2 | **Name the source and cost of every return** | Simplicity vs risk legibility | No bare APY: each rate splits into base, incentive, expiry, source, named curator and what each party, including us, is paid, in plain words first, with full detail (curator parameters, calldata) one tap away. An all-in yearly cost sits beside it, comparable with an ETF's fee |
| 3 | **Friction where it is irreversible** | Speed vs safety | Three confirmation levels: actions inside policy run or take one tap; actions above an ask-first threshold need an explicit confirm with a preview; irreversible actions (new payees, large exits, loosening the policy) are confirmed step by step and wait out a cooling-off delay. Recovery is set up and rehearsed before larger balances |
| 4 | **Say what we cannot do** | Self-custody vs "account" | Always show who holds which key and every permission the user has granted, with one-tap revoke. The product cannot reverse, freeze or insure funds, and cannot move them outside the permissions the user granted; support can guide but not undo |
| 5 | **Portfolio first, built for the drawdown** | Crypto-native breadth vs investor wellbeing | Home shows allocation against target and risk contribution, not a token list; no points, streaks or trading nudges. When prices fall sharply (bitcoin fell more than 50% between October 2025 and June 2026), remind users of the target and rules they chose, without telling them to hold or sell |

**Trust checklist (new).** Every automated or assisted action must pass four tests before it ships.

| Test | The user can... | Principle it enforces |
| --- | --- | --- |
| **Legibility** | see what the product understood, what it intends to do and which rule allows it | 1, 2 |
| **Control** | approve, change or stop it, and set the limits it runs inside | 1 |
| **Verification** | check afterwards what was done, what it cost and what changed | 1, 4 |
| **Recoverability** | undo it where that is possible, and is told plainly where it is not | 3, 4 |

The four tests are adapted from a 2026 design-strategy piece shared during this work, which defines trust as legibility, control, verification and recoverability. That piece credits Nielsen Norman Group for the underlying themes; I have not checked that attribution.

## 6. Product model

**This section is incomplete.** The strategy depends on a handful of objects that have never been defined. The list below is a harvest of the terms the docs already use, so the gap is visible; a conceptual-model session decides which are real objects, what states they have and what each is called.

| Candidate | What the docs mean by it | Open question |
| --- | --- | --- |
| **Slice** | The share of a person's wealth they choose to hold in digital assets | Is it a percentage of net worth, a dollar amount, or either? Does the product know net worth at all? |
| **Sleeve** | A part of the slice with one purpose, such as bitcoin core, dollar earn or tokenized treasuries | Fixed set or user-defined? One earn position per sleeve or several? |
| **Policy** | The user's written rules: target, drift bands, limits, ask-first thresholds | One policy per account or per sleeve? What are its states (draft, signed, amended)? What happens to past actions when it changes? |
| **Earn position** | Money placed in one earning product, with a source, rate and risk | How does it relate to the vault, curator and underlying loans? |
| **Recovery plan** | The set-up that lets the user regain access: passkey, guardians, co-signer, time lock | Is "rehearsed" a state? Who are the other parties, and are they objects too? |
| **Custody map** | Who holds which key and what each party can do | Probably a view of the recovery plan and account, not an object of its own |
| **Risk card** | The breakdown of an earn position's risks | Probably a view of the earn position, not an object |
| **Action** | Anything the product does: a deposit, rebalance, exit | Transaction states are listed in section 7; the link from each action to the policy rule that allowed it is not modelled |

**Vocabulary is not settled.** The v1 docs use "slice", "sleeve" and "allocation" loosely, and "policy", "rules" and "investment policy" for the same thing. This doc uses slice, sleeve and policy as working terms until the session decides. The word "account" is itself an open decision (section 10).

All of these objects are provisional. Several exist only because of an untested bet, so they should not be locked until that bet is tested.

## 7. Experience

Trust is won or lost at seven moments in the journey; onboarding and funding are the likely make-or-break points, which is a hypothesis to test. The stages are v1's as revised on September 30, with one column added to show which outcome each stage serves. The [experience map](06-experience-map.md) sets out each stage in detail.

| Stage | The user's question | What design must get right | Principle | Outcome |
| --- | --- | --- | --- | --- |
| **Discover** | "Is this legitimate, and is it for me?" | Custody explainer; honest comparison with an ETF, including all-in yearly cost and when the ETF is better; regulatory status in plain words | 2, 4 | Funded and understood |
| **Onboard** | "What if I lose access?" | Passkey-first setup; layered recovery with explained trade-offs; a rehearsed recovery drill; a scam-awareness moment | 3, 4 | Can get back in |
| **Fund** | "What will this cost and where does my money go?" | Exact fees in dollars and arrival time; which chain and why, or abstracted with an audit trail; address-poisoning defence | 3 | Funded and understood |
| **Allocate** | "How much should this be?" | Target tied to net worth; risk-contribution view; a signed policy summary; any permission granted shown in the custody map | 1, 4, 5 | Policy in force; sized deliberately |
| **Earn** | "Where does this return come from, and what could go wrong?" | Look-through risk card; base versus boosted rate; who is paid; exit-time estimate; curator named | 2 | Knows what they earn |
| **Monitor** | "Do I need to do anything?" | Drift alerts; incident banners that say what action is needed; statements and tax-lot view; a reminder of the user's own target and rules in a drawdown | 5 | Stays the course |
| **Exit or recover** | "Can I get out, and can my family?" | Unwind preview with liquidity timing; time-locked recovery; beneficiary flow; delay on large exits under duress | 3 | Can get back in |

The transaction-state vocabulary is shared across every stage: Draft, Simulated, Awaiting signature, Submitted, Pending, Confirmed, Final, plus Partially filled, Failed, Reverted and Delayed by policy. Every state shows fees paid, what changed in the portfolio, and the policy rule that authorized it.

No flows exist yet. Each stage needs one once the product model in section 6 is stable.

## 8. Automation stance

The product automates execution, never judgement: the user decides what should happen and writes it down as policy, and the product carries it out exactly. This is where the strategy sits on the line between operator and managed service.

| Level | Who decides | Who acts | Our stance | Why |
| --- | --- | --- | --- | --- |
| **Manual** | User, each time | User, each time | Always available | The user can always act directly |
| **Policy execution** | User, once, in a written policy | Product, inside the policy | **The core model, phases 1 and 2** | Removes operator burden while the user stays the decision-maker |
| **Assisted** | Assistant proposes with reasons; user approves | Product, after approval | Phase 3, after counsel confirms the model | Useful, but a proposal can shade into advice |
| **Discretionary** | The product or a manager | The product | Not offered by us; only through a registered adviser or a named curator the user selects | Choosing on the user's behalf is the line the regulatory guidance draws |

**How the product acts is still open.** Inside the policy, either the user signs every action, or the user grants the product a limited, revocable onchain permission to act within it. The second removes operator burden, but "we cannot move your funds" then holds only outside the permissions granted. Counsel must confirm that the chosen model stays within the non-custodial interface relief (section 10).

**Why the line sits here.** The SEC staff statement of April 13, 2026 on non-custodial interfaces requires that the user chooses the transaction details and that defaults are disclosed and editable. Commissioner Peirce's statement of July 22, 2026 suggests that whoever selects and reallocates strategies may be acting as an adviser. Both are non-binding and reversible, and neither is legal advice; counsel must confirm the model.

**A test for any feature.** If a request such as "move $20,000 into a diversified crypto portfolio" is answered by the product choosing the portfolio, that is discretion. If it is answered by applying a mix the user already wrote into their policy, or by a proposal the user approves, it is not. This is my reading of the guidance, for counsel to confirm.

**Rules for anything automated or assisted.**

- It passes the trust checklist in section 5.
- It cites the policy rule that allows it at the moment it runs.
- It acts only through permissions the user granted, shown in the custody map and revocable in one tap.
- It stops and asks when a request falls outside the policy.
- It can be switched off without breaking the account, because the rules that permit it may change.

## 9. How we learn

**Updated from the Assumption Map.** Research is ordered by how much the strategy depends on each assumption and how little evidence exists for it. The order below follows the Assumption Map, which also sets a proposed pass signal for each study.

| Order | Work | Assumptions it tests | Unlocks |
| --- | --- | --- | --- |
| Now, in parallel | Hands-on teardown of Robinhood Wallet and MetaMask Money Account | Nobody ships an allocation-first self-custody account | Confidence in section 3 |
| Now, in parallel | Counsel review | User-written policy keeps the product non-discretionary; a pre-granted permission still counts as the user signing; risk ratings are information, not advice; "account" is safe to use | Section 8; risk card; naming |
| Now, at a desk | Three narrow checks: how investors use rules today, segment size, price benchmarks | Background for bets 1 and 3 and the business model | Sharper interview questions |
| 1 | Generative interviews with brokerage-native and exchange-only investors | They want to hold their own keys; they think in portfolio share; fear of losing access is the main barrier | Whether the positioning stands |
| 2 | Rules prototype and recovery prototype | They will write their own rules; a drill builds confidence | Phase 1 gate |
| 3 | Allocation home prototype | They fund more with allocation than with a token list | Phase 2 gate |
| 4 | Choice experiment and wording survey | Rate source changes choice; what "account" implies | Risk card and naming |
| Later | Pricing and sizing study | They will pay, and the segment is large enough | Business model |

An interview plan was drafted in conversation and is not yet saved to a doc: three learning goals (sizing and triggers, custody beliefs, rules and delegation today), interviews about real past events, and observation of how people use their brokerage app. The full research plan and participant mix are in the [Problem Framing](03-problem-framing.md) doc, which now follows this order.

The interviews open with pain discovery, before any concept is shown: open questions about real past events, with our expected pains kept out of the session until the end. This tests assumption A0, and its result decides which of the later studies still run as designed.

**How a decision gets made.** A bet moves forward when its test shows the behaviour, is reworked when the result is mixed, and is dropped when the assumption fails. Progress is reviewed against the outcomes in section 1, not against what was delivered.

## 10. Open decisions and sources

Seven decisions are open. The first two block the most.

- [ ] **Outcome components.** The umbrella, deliberate holders, was decided on October 4, 2026. Still open: confirm the six components and the focus for each phase.
- [ ] **Business model.** Subscription, spread or another source. It defines the business impact above the primary outcome and must not reward pushing higher-risk vaults.
- [ ] **Discretion and execution model.** User-written policy only, or a registered adviser or named curator for managed parts; and whether the user signs every action or grants a limited, revocable permission to act inside the policy. It decides whether "we cannot move your funds" stays true. Waits on counsel.
- [ ] **Naming.** Whether "account" stays, and which alternatives go into the wording test.
- [ ] **First scope.** Which sleeves and which states launch first.
- [ ] **Recovery partner.** Who co-signs or guards, and who bears liability if that partner fails.
- [ ] **Primary user.** Brokerage-native investor, or the exchange-only holder as the early adopter. Waits on the interviews.

**What comes next.**

1. Assumption map: drafted. Its ratings and pass signals need review with PM before the first study.
2. Conceptual-model session: decides the objects, states and names. It completes section 6.
3. Handoff to execution, once phase 1 gates pass: Web3 execution specs, agent and automation UX, a language and disclosures library reviewed by counsel (yield language never says "interest"), and the design system brief, accessible by default. The experience map already exists as a hypothesis map and is updated after the interviews.

**Sources.** This version reorganises [v1](https://github.com/ademiroliveira/sc-ia/blob/c3610a4/strategy/04-product-design-strategy.md) and adds decisions from four places: the [Problem Framing](03-problem-framing.md), the [competitive analysis](../research/02-competitive-analysis.md), the [outcome-led deep dive](../research/07-outcome-led-design-deep-dive.md), and the layer audit and research planning done in conversation. Market and regulatory facts come from the project doc *Investment-Grade Self-Custody* (September 2026). Regulatory points are not legal advice.

