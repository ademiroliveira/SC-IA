# Account Abstraction: A Product Experience Design Brief

As of November 6, 2026 · Builds on [market research](01-market-and-opportunity-research.md) (section 5, technology enablers), [competitive analysis round 2](10-competitive-analysis-round-2.md) and the [wallet evolution research](../time-machine-workshop/wallet-evolution-research.md)

> **Provenance.** Desk research run on November 6, 2026, combining web sources with earlier docs in this repo. It is not a competitive-watch file and was not checked claim by claim under the source rules in `CLAUDE.md`. Sources were found by web search; ethereum.org's builder guidance was read in full, and the rest were read from search excerpts. Every figure, date and name in the text appears in the cited source as found. Adoption figures conflict across sources and are flagged where used. Individuals are referred to by role.

**Scope:** Ethereum and EVM layer 2s. Solana and Bitcoin use different account models and are out of scope.
**For:** product experience design on self-custody wallets, this product, and agentic or conversational interfaces.

Vocabulary follows the current terms: the user **defines** a **plan**, made of **rules**; **guardrails** are spending and exit limits. Lines marked **Design implication** or **Inference** are interpretation, offered for discussion.

---

## Contents

1. The short version
2. What account abstraction changes for people
3. State of play, November 2026
4. What changed in the last 90 days
5. Risk moves; it does not disappear
6. Experience principles for programmable accounts
7. Patterns and design-system components
8. Language
9. Applying it to this product
10. Agents and conversational interfaces
11. Research questions
12. Watchlist
13. Glossary
14. Sources

---

## 1. The short version

- **Account abstraction (AA) turns an account from one key into a set of rules.** Who may act, how they prove it, who pays the fee, and what one approval can do all become programmable. For design, this means an account now has settings, permissions and states that users must be able to see and change.
- **The practical path today is EIP-7702 plus ERC-4337, reached through wallet capabilities.** ethereum.org advises apps to ask the wallet for an outcome, such as a batch of calls or a sponsored fee, through ERC-5792, and to let the wallet decide how to deliver it. Native AA on Ethereum (EIP-8141, "Frame Transactions") is scheduled for the Hegotá upgrade, which ethereum.org lists for Q2 2027 with no confirmed date. Its final design may still change.
- **Ethereum and Base have split on native AA.** Base's own proposal, EIP-8130, was taken out of its September upgrade and has no scheduled date. Expect different account models on different chains for some time.
- **The largest theft on record used EIP-7702.** On October 29, 2026 attackers took about $6.3B from Binance hot wallets. On Ethereum, a batch of signed 7702 authorizations pointed one hot wallet at the attacker's sweeper contract. The reported root cause so far is a compromised signing pipeline, not a flaw in 7702. The lesson for design: a delegation is a standing power of attorney, and its damage is not limited to a single transfer.
- **7702 phishing against individuals is large and measured.** A USENIX Security 2026 study found that 63% of the delegations it observed pointed to malicious contracts. Wallets don't support revoking a delegation consistently, and some hardware wallets can't sign 7702 authorizations at all.
- **The design gap is the human interface to standing authority.** The building blocks for limited, revocable permissions (ERC-7715 and ERC-7710, session keys) and for readable signing (ERC-7730) now exist. Most products still lack one clear place that shows what can act on the user's behalf, with its limits, its expiry and a one-tap way to remove it.
- **Published research on how ordinary people understand AA was not found in this search.** Most of the evidence is incident data, which makes comprehension research a priority (section 11).

---

## 2. What account abstraction changes for people

A plain account (an "externally owned account", or EOA) is one private key. Whoever holds the key can do anything, every action needs its own signature, and fees must be paid in the chain's own token. AA lets an account run code that decides what counts as a valid action.

| Capability | What the user experiences | Design question it raises |
| --- | --- | --- |
| **Batching** | "Approve and deposit" in one confirmation instead of two or three | How do you show several effects in one review, and what happens if one step fails? |
| **Gas sponsorship, or paying fees in tokens** | No need to buy ETH first; fees are paid in USDC or by the app | Who pays, how much, and what happens when the sponsorship stops? |
| **Passkeys** | Sign in and approve with Face ID or a fingerprint; no seed phrase at setup | What happens if the person loses access to their Apple or Google account? |
| **Session keys and permissions** | An app or agent can act within limits, such as "up to 10 USDC a day for 30 days", without asking each time | Can the user see what they granted, understand it, and remove it? |
| **Spending limits and time delays** | Daily limits, approved-address lists, waiting periods on large withdrawals | Which guardrails are defaults and which are the user's own, and how are they changed safely? |
| **Programmable recovery and key rotation** | Replace a lost device or key without moving funds | Who can start recovery, how long does it take, and what can the old key still do? |

**Inference.** Each capability removes a step but adds a relationship: a permission, a sponsor, a rule, a recovery party. The experience problem shifts from "too many steps" to "too many relationships the user can't see". Good AA design makes those relationships visible.

---

## 3. State of play, November 2026

### 3.1 The standards stack

| Layer | Standard | Status | What it means for design |
| --- | --- | --- | --- |
| Smart accounts without a protocol change | **ERC-4337** | Live since March 2023; bundlers and paymasters in production | Mature rails for sponsorship, batching and session keys, but they add infrastructure the account depends on |
| Upgrading existing accounts | **EIP-7702** | Live since the Pectra upgrade (May 7, 2025) | Users keep their address. The original key keeps full control and can change or clear the delegation at any time |
| How apps ask wallets for features | **ERC-5792** (`wallet_getCapabilities`, `wallet_sendCalls`); **ERC-7677** (sponsorship requests) | Rolling out; support differs by wallet and by chain | Apps should check what the wallet supports and fall back gracefully; the wallet decides how to execute |
| Permissions | **ERC-7715** (requesting a permission); **ERC-7710** (delegating and using it onchain) | Shipping in MetaMask as "Advanced Permissions"; used by agent products | Permission requests a person can read, and adjust before granting |
| Modular accounts | **ERC-7579**, **ERC-6900** | In production through account toolkits | Features such as session keys and limits are installable modules, so each module is a trust decision |
| Passkeys on Ethereum mainnet | **EIP-7951** (P-256 signature check) | Live since the Fusaka upgrade (December 3, 2025); major L2s such as Base, Optimism, Arbitrum and Polygon already had the earlier RIP-7212 | Accounts secured by passkeys are now cheap to verify on mainnet as well as on L2s |
| Readable signing | **ERC-7730** ("clear signing") | Launched by the Ethereum Foundation on May 12, 2026; backed by Ledger, Trezor, MetaMask, WalletConnect and others | Works only where a contract has a published description and the wallet displays it |
| Native AA on Ethereum | **EIP-8141** (Frame Transactions) | Draft; scheduled for Hegotá; named a "must ship" by the Foundation's protocol team | Sponsorship, batching and new signature schemes become part of ordinary transactions. The spec may still change |
| Native AA on Base | **EIP-8130** | Draft; runs only on a Base test network; removed from Base's Cobalt upgrade; no scheduled date | Built-in session keys (called "actors") and fee payers. Not the same model as EIP-8141 |

### 3.2 Timeline

| Date | Event |
| --- | --- |
| March 2023 | ERC-4337 goes live |
| May 7, 2025 | EIP-7702 activates in Pectra |
| December 3, 2025 | Fusaka adds EIP-7951 (passkey verification) |
| January 29, 2026 | EIP-8141 drafted by Ethereum's co-founder and other authors |
| March 26, 2026 | EIP-8141 "considered for inclusion" in Hegotá |
| April 13, 2026 | SEC staff statement on non-custodial "Covered User Interfaces" |
| May 12, 2026 | Ethereum Foundation launches clear signing (ERC-7730) |
| July 2026 | Base announces EIP-8130 for its September Cobalt upgrade |
| August 27, 2026 | EIP-8141 moves to "scheduled for inclusion" in Hegotá |
| September 7, 2026 | The Foundation's protocol team names EIP-8141 a "must ship" for Hegotá |
| September 2026 | Ethereum and Base end talks on a shared native-AA standard; EIP-8130 leaves Cobalt |
| September 30, 2026 | Base Cobalt goes live without EIP-8130's transaction type |
| October 6 and 26, 2026 | Glamsterdam goes live on the Sepolia and Hoodi test networks; no mainnet date yet |
| October 29, 2026 | Binance hot-wallet drain uses EIP-7702 delegation on Ethereum |
| Q2 2027 (not confirmed) | Hegotá, per ethereum.org |

### 3.3 Adoption, with caveats

- **Figures conflict; treat all of them as directional.** Totals of ERC-4337 operations cited for early to mid 2026 run from about 380 million to over 2 billion, depending on the source and which chains it counts. Counts of smart accounts run from about 40 million to about 65 million. For EIP-7702, one research blog reports that more than 27 million Ethereum accounts had used it by September 2026, and an academic study observed 2 to 3 million delegations a day across major EVM chains, many of them malicious. The [wallet evolution research](../time-machine-workshop/wallet-evolution-research.md) cites 45–60 million live delegations from secondary BundleBear write-ups. Check BundleBear and Dune directly before quoting any figure outside the team.
- **The largest wallet now makes smart features the default.** MetaMask turns smart-account features on automatically for new users, lets them switch back per network for a small fee, and supports only its own delegation contract. Its help centre tells users that it will only ever offer the upgrade inside the wallet.

**Design implication.** Programmable accounts are becoming the default for new users of major wallets, often without the user choosing. A product should assume that a user's account may already be delegated, possibly to code the user doesn't recognize.

---

## 4. What changed in the last 90 days

1. **Native AA got a target, and a rival.** EIP-8141 moved from "considered" to "scheduled" on August 27 and was named a must-ship on September 7. Reporting on the decision notes the spec is still a draft whose details can change before it ships. Base's competing EIP-8130 claimed USDC transfers about 63% cheaper than under ERC-4337, but it was taken out of Cobalt and now has no scheduled date. CoinDesk reported that Ethereum and Base gave up on a shared standard, which could force wallets that span both networks to support two transaction systems.
2. **Clear signing became a real standard.** The Ethereum Foundation now stewards ERC-7730 (since May). Trezor rolled it out on September 8, and the number of published contract descriptions grew about 28% between May and the end of July. Coverage still depends on each protocol publishing a description for its contracts.
3. **The Binance drain (October 29).** Binance puts the loss at about $6.3B, and Chainalysis at about $6.4B. On Ethereum, one transaction carried 50 valid EIP-7702 authorizations signed by a Binance hot wallet, delegating it to an attacker's sweeper contract. Binance's initial account points to a compromised engineer's laptop that gave access to a service able to submit withdrawals. Binance says it found no evidence that a private key leaked, and a full root-cause report is still pending. Analysts agree that 7702 was not the root cause. It did let the attacker take over the wallet outside Binance's normal approval steps, and keep sweeping it while Binance's own systems refilled it. The [November 2 watch](../watch/2026-11-02.md) logged the same event.
4. **Glamsterdam slipped.** It went live on both test networks in October, but mainnet is not scheduled. Hegotá, and native AA with it, comes after Glamsterdam.

**Design implication of item 3.** A 7702 authorization should be treated as the most dangerous thing a person can sign, for retail and institutional users alike: it hands standing control of the whole account to code. Any product that holds signing authority, such as an executor that carries out a user's plan, becomes a target for the same class of attack. Its authority must be scoped so that a compromise cannot turn into a full drain.

---

## 5. Risk moves; it does not disappear

| New capability | Where the risk goes | Evidence | Design response |
| --- | --- | --- | --- |
| 7702 delegation | To the contract being delegated to, and to anyone who can obtain a signature | 63% of observed delegations were malicious (USENIX 2026); the Binance drain | Only wallet-vetted contracts; never triggered by an app; highest signing severity; delegation status always visible |
| Standing permissions (session keys, ERC-7715 grants, token allowances) | To mistakes in scope, and to the security of whoever holds the permission | An audit found session-key spending limits that could be bypassed to drain the account | One list of everything granted, with limits, expiry, last use and removal; short default expiry |
| Gas sponsorship | To the sponsor's availability and terms | Sponsor economics and dependency ([market research](01-market-and-opportunity-research.md), section 5) | Show who pays; fall back gracefully when sponsorship ends |
| Passkeys | To the person's Apple or Google account | Platform-account dependency ([market research](01-market-and-opportunity-research.md), section 5) | A second recovery path, and an explanation of the dependency |
| Programmable recovery | To guardians, co-signers and timing | Under 7702 the original key can still change the delegation | Recovery that replaces the lost credential, and says what the old key can still do |
| Batching | To understanding: one signature, many effects | The gap between what the screen shows and what gets signed is the main surface for drainers ([wallet evolution research](../time-machine-workshop/wallet-evolution-research.md)) | Review that describes effects; results per step; clear signing |
| Native AA split across chains | To consistency | The Ethereum and Base split | Show what works on each network; don't promise features across all chains |

**Further known gaps.**

- Wallets don't consistently support revoking an arbitrary 7702 delegation (Curvegrid, February 2026).
- As of March 2026 some hardware wallets couldn't sign 7702 authorizations, so fee sponsorship and smart features may not be available to their users (Linea documentation).
- Early analyses found that most of the first 7702 delegations, reported as anywhere from 80% to over 97%, pointed to copies of the same sweeper code.

---

## 6. Experience principles for programmable accounts

Each principle resolves a tension. They are written to sit alongside the principles in [strategy 04](../strategy/04-product-design-strategy.md), section 5.

1. **Sell outcomes, not account types.** *(Capability versus understanding.)* Users see "approve and deposit in one step" or "fees paid in USDC", never "smart account" or "7702". ethereum.org's guidance for builders makes the same point: ask the wallet for an outcome and let it choose the mechanism.
2. **Upgrades belong to the wallet, never to an app.** *(Convenience versus phishing.)* An account upgrade is offered only inside the wallet, only to vetted contracts, and never because a website asked. ethereum.org tells builders to treat delegation targets "like wallet infrastructure", and MetaMask tells its users the same thing.
3. **Every standing power is a visible object.** *(Automation versus control.)* Anything that can act without a fresh signature appears in one list, with its scope, limit, expiry, last use and a one-tap way to remove it. That covers delegations, session keys, permission grants, token allowances, agents and guardians. This maps to strategy principle 4.
4. **Describe effects, not code, and match friction to how reversible an action is.** *(Speed versus safety.)* Simulate each transaction and show the balance changes. Use ERC-7730 descriptions where they exist, and say so where they don't. 7702 authorizations, account upgrades and new permissions sit at the highest severity. This maps to strategy principle 3.
5. **Recovery replaces authority, and says what is left.** *(Seedless setup versus leftover risk.)* Recovery should replace the lost credential, not add another one. Where an original key keeps power, as it does under 7702, say so and offer a way to retire it.
6. **Be honest about who pays.** *(Free versus dependent.)* If fees are sponsored, say by whom, within what limits, and what happens if the sponsorship stops. "Gasless" must never read as "free forever".
7. **Promise per network, not per account.** *(One account versus many chains.)* Show which features work on which network. Native AA will differ between Ethereum and Base for some time.
8. **Automate only inside rules the user defined.** *(Operator burden versus discretion.)* Session keys and permissions should encode the user's plan, so that every automated action can cite the rule that allowed it. This maps to strategy principle 1.

---

## 7. Patterns and design-system components

These are candidates for the design system strategy brief (05, not yet written).

| Component | Purpose | Key states and fields |
| --- | --- | --- |
| **Account capability panel** | Shows what this account can do on each network | Standard or smart, per network; which contract and whether it is vetted; features available (batching, sponsorship, permissions) |
| **Upgrade sheet** | Explains gains and risks, per network; offered only inside the wallet | Gains in plain words; what changes and what stays the same (address, key); cost; how to switch back |
| **"Who can act for me" list** | One place for every standing authority | Type (delegation, session key, permission, allowance, agent, guardian); who holds it; scope; limit used and remaining; expiry; last used; remove; whether removal succeeded |
| **Permission request sheet** | Grants a scoped permission, in the ERC-7715 style | Who is asking; what they can do; amount per period; start and end dates; fields the user can adjust; what they can never do |
| **Batched review** | One signature, several effects | Steps in order; net balance change; fee and who pays it; result per step after execution; explanation of a partial failure |
| **Signing severity levels** | Friction in proportion to risk | Level 1: routine and inside the plan. Level 2: above an ask-first threshold. Level 3: irreversible or grants authority (7702, new permission, upgrade, loosening a guardrail), confirmed step by step and subject to a delay |
| **Fee and sponsor line** | Says who pays | "Sponsored by X", "Paid in USDC" or "You pay in ETH"; what happens if the sponsor declines |
| **Recovery setup and rotation** | Layered recovery | Methods; parties involved; time lock; whether it has been rehearsed; what the old credential can still do |
| **Cooling-off state** | Shows a delay in progress | Countdown; the rule that triggered it; cancel |
| **Additional transaction states** | Extend the strategy's state vocabulary (section 7) | "Sponsored"; "Batch, step n of N"; "Done under permission [name]"; "Blocked by guardrail"; alert for "Delegation changed" |

**Inference.** The "who can act for me" list is the single most valuable component. It answers the question that matters most after an incident ("what could act on my account?"), it makes removal fast, and it is the object the custody map in strategy principle 4 already promises.

---

## 8. Language

| Avoid in the interface | Prefer | Why |
| --- | --- | --- |
| Smart account, EIP-7702, delegation, EntryPoint | "Account features", "one-step actions", "fees in USDC" | People decide on outcomes, not mechanisms |
| "Upgrade your account" (from any app) | Only inside the wallet: "Turn on one-step actions for Ethereum" | "Upgrade" prompts are a known phishing lure |
| Session key | "Permission for [app]: up to $X a day until [date]" | Names who holds it, what it covers, the limit and the expiry |
| Gasless | "Network fee paid by [sponsor]" | Honest about the dependency |
| Approve | Say what is approved, and for how long | An approval is a standing power |
| Revoke | "Remove access", followed by confirmation that it worked | A plain verb, with the result checked |

These are proposals for the language and disclosures stream in [strategy 04](../strategy/04-product-design-strategy.md), section 10. They need testing and counsel review.

---

## 9. Applying it to this product

### 9.1 The open execution-model decision is an AA decision

[Strategy 04](../strategy/04-product-design-strategy.md), section 8, leaves one choice open. Inside the user's plan, does the user sign every action, or grant the product a limited, revocable onchain permission to act? AA defines what each option looks like in practice.

| | **A. User signs every action** | **B. Scoped permission to a product executor** | **C. Native AA actors (future)** |
| --- | --- | --- | --- |
| Mechanism | Plain or smart account. Batching and sponsorship cut steps, but every action is still signed | An ERC-7715/7710 grant or a session key on a smart account, encoding the user's plan: sleeves, bands, venues, caps, expiry | Account-level actors with scoped permissions (EIP-8130 style) or frame-based validation (EIP-8141) |
| Operator burden | Medium: every rebalance needs the user | Low: rebalances inside the plan run without the user | Low |
| "We cannot move your funds" | True | True only outside the granted scope, and must be stated exactly | Same as B |
| Damage if our systems are compromised | Nothing from our side | Bounded by the grant: amounts, venues, period | Bounded, if the scopes are tight |
| Regulatory reading (for counsel) | Closest to user-directed | Depends on whether a pre-granted plan the user defined counts as user-directed | Same question as B |
| Maturity | Production | Early production (MetaMask Advanced Permissions; Glider's session key is the precedent in [round 2](10-competitive-analysis-round-2.md)) | Not before Hegotá on Ethereum; no date on Base |
| Chain coverage | Broad | Varies by wallet and chain | Fragmented |

**Inference.** Of the three, B alone removes operator burden today, and the Binance drain shows why its scope matters more than its convenience. A version of B worth testing:

- The executor can only move funds between the user's own sleeves and named venues, within the user's drift bands and caps.
- It can never send to a new address, change the plan, or change the account's delegation.
- It expires on a short cycle that the user renews.
- Loosening the grant waits out the same cooling-off delay as loosening a rule (strategy principle 1).

### 9.2 Where AA supports each bet

| Bet ([strategy 04](../strategy/04-product-design-strategy.md), section 4) | How AA helps | Watch out for |
| --- | --- | --- |
| 1. Allocation home | Batched rebalances; sponsored fees make small rebalances worth doing | Fees and sponsorship must still be shown for each action |
| 2. Risk shown, not hidden | Clear-signing descriptions for vault deposits | Gaps where a vault has no published description |
| 3. The plan as the core object | The plan can be enforced onchain, not only in our app | The plan the user sees must match what the contract enforces |
| 4. Recovery rehearsed | Passkeys, guardians, time-locked key replacement | The old key's remaining power under 7702; dependence on Apple or Google |
| 5. Records native | A receipt for each step, tied to the rule that allowed it | Batched actions complicate tax-lot records |

### 9.3 Questions for counsel

These extend the counsel review already in the research order ([strategy 04](../strategy/04-product-design-strategy.md), section 9).

- Does a user-defined plan, enforced through a scoped onchain permission, stay within the conditions of the SEC staff statement of April 13, 2026: user-directed, non-discretionary, with defaults disclosed and editable? The statement is staff-level, non-binding and lapses after five years.
- Does holding a session key or executor role change how the product's custody is characterized?
- What disclosures does a sponsored-fee model need?

---

## 10. Agents and conversational interfaces

- **Session keys and ERC-7715/7710 permissions are the limit layer for agents.** The limits are enforced by code, not by the agent's judgement. Coinbase launched Agentic Wallets on February 11, 2026 with per-session and per-transaction limits, and MetaMask has an Agent Wallet.
- **Prompt injection is the leading attack.** The Grok wallet incident of May 4, 2026 is the usual reference case.
- **Design implications:**
  - An agent never holds root authority, never asks for a 7702 upgrade, and never edits its own permissions.
  - Every agent action cites the permission and the rule that allowed it, as the trust checklist in strategy section 5 requires.
  - Grants are made per purpose and are short-lived; renewing one is an explicit step.
  - Limits set per wallet don't add up to governance across a portfolio ([market research](01-market-and-opportunity-research.md), section 5). The user's plan is a candidate to be that portfolio layer.
  - A confirmation in conversation is not enough for level 3 actions; they need the structured review.

---

## 11. Research questions

The search found little published research on how ordinary users understand AA features. These questions address that gap, and each says what its answer would change.

| # | Question | Method | What the answer changes |
| --- | --- | --- | --- |
| AA1 | Can users tell a genuine in-wallet upgrade from a phishing "upgrade" prompt? | Recognition test with real prompts and lures | The upgrade sheet; whether to turn smart features on automatically |
| AA2 | After granting a permission, can users say what it lets someone do, until when, and how to remove it? | Grant, then recall | Fields on the permission sheet and the "who can act for me" list |
| AA3 | Do brokerage-native investors prefer to sign each rebalance or to grant a scoped permission, and at what amount does their preference flip? | Concept test of both execution models across a ladder of amounts | The execution-model decision (9.1) |
| AA4 | Does "network fee paid by [sponsor]" change trust or perceived cost compared with "no fees"? | A/B wording test | Fee-line copy and disclosure |
| AA5 | Do users accept a cooling-off delay on loosening a permission or guardrail? | Prototype with the delay | How strategy principle 1 is implemented |
| AA6 | What do users believe happens if they lose their phone with a passkey-only setup? | Mental-model interviews | Recovery setup and rehearsal |
| AA7 | Does showing capability per network confuse or reassure? | Usability test | The account capability panel |

These extend the [critical research questions](../strategy/09-critical-research-questions.md) rather than replace them. AA3 sharpens the "rules versus agents" test proposed in [round 2](10-competitive-analysis-round-2.md).

---

## 12. Watchlist

| Item | Why it matters | Signal to watch |
| --- | --- | --- |
| Glamsterdam mainnet date | Hegotá and native AA follow it | Ethereum Foundation mainnet announcement |
| Final shape of EIP-8141 | Defines native AA patterns on Ethereum | Core developer calls; the Hegotá meta EIP |
| EIP-8130 on Base | A second native model | A Base upgrade that schedules it |
| Binance root-cause report | Lessons for any executor or signing service | Binance's post-mortem |
| 7702 revocation and hardware-wallet support | Whether "remove access" can be promised | Wallet release notes |
| ERC-7730 coverage of target vaults | Whether readable signing covers this product's flows | Registry entries for the chosen venues |
| Regulatory reading of pre-granted permissions | Decides option B | Counsel; SEC statements |

The first four are candidates for [watch/watchlist.md](../watch/watchlist.md); adding them is the owner's call.

---

## 13. Glossary

| Term | Plain meaning |
| --- | --- |
| **Account abstraction (AA)** | Letting an account's own code decide what counts as a valid action, instead of a single fixed key |
| **EOA** | A plain account controlled by one private key |
| **Smart account** | An account whose rules are set by code: limits, permissions, recovery, batching |
| **EIP-7702 delegation** | A signed instruction that makes a plain account run a contract's code. It stays in place until it is changed or cleared |
| **Bundler** | A service that collects ERC-4337 operations and submits them onchain |
| **Paymaster / payer** | Whoever covers the network fee on the user's behalf |
| **Session key** | A temporary key with limited power, such as an amount, an expiry or specific contracts |
| **ERC-7715 / ERC-7710** | Standards for requesting a scoped permission (7715) and for granting and using it onchain (7710) |
| **Clear signing (ERC-7730)** | Showing a transaction in plain words, from a published description of the contract |
| **Passkey** | A device-held credential unlocked with biometrics. On Ethereum, verification became cheap with EIP-7951 |
| **Native AA** | Account abstraction built into the protocol itself, so no extra infrastructure is needed |
| **Frame transaction (EIP-8141)** | Ethereum's proposed native AA: a transaction split into steps for validation, payment and execution |
| **Glamsterdam / Hegotá** | Ethereum's next two network upgrades; native AA is planned for Hegotá |

---

## 14. Sources

Found by web search on November 6, 2026. Tags follow `CLAUDE.md`. Protocol documentation, specifications and Ethereum Foundation announcements are tagged [Help doc]; academic papers and law-firm analyses are tagged [Report].

**Protocol, standards and product documentation**

- [Building on Ethereum in 2026: what has changed](https://ethereum.org/latest/building-on-ethereum-in-2026/) [Help doc], ethereum.org, published May 7, 2026, updated May 28, 2026. Read in full.
- [Hegotá](https://ethereum.org/roadmap/hegota/) [Help doc], ethereum.org roadmap page: expected Q2 2027, date not confirmed.
- [Glamsterdam Hoodi testnet announcement](https://blog.ethereum.org/2026/10/16/glamsterdam-hoodi-announcement) [Help doc], Ethereum Foundation, October 16, 2026: mainnet date not decided.
- [EIP-7951: precompile for secp256r1](https://eips.ethereum.org/EIPS/eip-7951) [Help doc]: passkey signature verification.
- [Native account abstraction on Base](https://docs.base.org/base-chain/network-information/native-account-abstraction.md) [Help doc]: EIP-8130 is experimental and devnet-only.
- [Base Cobalt upgrade overview](https://docs.base.org/base-chain/specs/upgrades/cobalt/overview.md) [Help doc].
- [MetaMask Advanced Permissions (ERC-7715)](https://docs.metamask.io/smart-accounts-kit/concepts/advanced-permissions/) [Help doc].
- [MetaMask: switch to or revert from a smart account](https://support.metamask.io/configure/accounts/switch-to-or-revert-from-a-smart-account) [Help doc]: auto-enabled for new users; offered only inside the wallet.
- [Linea: EIP-7702 support](https://docs.linea.build/protocol/eip-7702) [Help doc]: hardware-wallet limitation as of March 2026.
- [Candide: batch and sponsor transactions via ERC-5792](https://docs.candide.dev/instagas/batch-sponsor-transactions/) [Help doc]: ERC-5792 and ERC-7677 support by wallet.

**Research and analysis**

- [EIP-7702 Phishing Attack](https://arxiv.org/html/2512.12174) [Report], arXiv 2512.12174: 2 to 3 million delegations a day observed.
- [IACR ePrint 2026/2060](https://eprint.iacr.org/2026/2060.pdf) [Report]: summarizes the USENIX Security 2026 measurement (63% malicious; $2.36M confirmed losses).
- [Toward Web 4.0: bidirectional trust between AI agents and blockchain](https://arxiv.org/pdf/2605.08922) [Report], arXiv 2605.08922: agent delegation standards; session-key audit findings.
- [SEC staff statement on crypto trading interfaces](https://www.pillsburylaw.com/en/news-and-insights/sec-staff-statement-crypto-trading-interfaces.html) [Report], Pillsbury, April 2026.
- [SEC staff provides clarity on broker-dealer registration for certain crypto asset securities user interfaces](https://www.chapman.com/publication-sec-staff-provides-clarity-on-broker-dealer-registration-for-certain-crypto-asset-securities-user-interfaces) [Report], Chapman.
- [Base Cobalt live without EIP-8130's transaction type](https://github.com/shemnon/evm-directory/pull/35) [Report], community EVM directory: activation September 30, 2026.

**Press**

- [Ethereum, Base give up on common wallet standard after months of talks](https://www.coindesk.com/tech/2026/09/16/ethereum-base-give-up-on-common-wallet-standard-after-months-of-talks) [Press], CoinDesk, September 16, 2026.
- [Ethereum core developers schedule EIP-8141 for Hegotá upgrade](https://cryptobriefing.com/ethereum-eip-8141-hegota-upgrade/) [Press], Crypto Briefing: August 27 decision; Hegotá planned for 2027.
- [Frame Transactions join Ethereum's 2027 upgrade roadmap](https://cryptonews.com/news/ethereum-news-eip-8141-frame-transactions/) [Press], Cryptonews: spec still a draft; details can change.
- [Frame Transactions: setting Ethereum transaction free](https://research.4pillars.io/en/research/frame-transactions-setting-ethereum-transaction-free) [Press], Four Pillars: drafting and "considered for inclusion" dates.
- [Ethereum Foundation sets 2029 quantum target and narrows Hegotá scope](https://thedefiant.io/news/blockchains/ethereum-foundation-sets-2029-quantum-target-and-narrows-hegot-scope) [Press], The Defiant.
- [Ethereum Foundation rolls out support for Clear Signing](https://www.theblock.co/post/401001/ethereum-foundation-rolls-out-support-for-clear-signing-crypto-security-solution) [Press], The Block, May 12, 2026.
- [Trezor supports clear signing via ERC-7730](https://cryptobriefing.com/trezor-clear-signing-erc-7730/) [Press], Crypto Briefing: September 8 rollout; registry growth.
- [What is EIP-7702? The Ethereum upgrade behind the $6.4B Binance hack](https://decrypt.co/resources/what-is-eip-7702-the-ethereum-upgrade-behind-the-6-4b-binance-hack) [Press], Decrypt.
- [Binance hack explained](https://www.cryptotimes.io/insights/binance-hack-explained/) [Press], Crypto Times.
- [Base Cobalt upgrade explained](https://www.bitrue.com/blog/base-cobalt-upgrade-explained) [Press], Bitrue: EIP-8130 not in Cobalt.
- [Base to implement native account abstraction (EIP-8130)](https://www.kucoin.com/news/flash/base-to-implement-native-account-abstraction-eip-8130-in-september-cobalt-upgrade) [Press], KuCoin News: gas comparison with ERC-4337.

**Vendor and security firms (lower confidence for figures)**

- [Inside the $6.3B Binance hot-wallet drain](https://www.hypernative.io/insights/blog/inside-the-largest-crypto-theft-of-all-time-the-6-3b-binance-hot-wallet-drain) [Vendor], Hypernative.
- [Binance hack: inside the $6.3B hot wallet theft](https://socradar.io/blog/binance-hack-6-3b-hot-wallet-theft/) [Vendor], SOCRadar.
- [How a compromised DevOps laptop reached the hot-wallet signer](https://phoenix.security/binance-hack-devops-laptop-hot-wallet-signer-eip-7702/) [Vendor], Phoenix Security.
- [A practical look at EIP-7702 and wallet delegation](https://www.curvegrid.com/blog/2026-02-13-a-practical-look-at-eip-7702-and-wallet-delegation) [Vendor], Curvegrid, February 13, 2026: revocation gaps.
- [EIP-7702: how code delegation turns every Ethereum EOA into a smart wallet](https://www.spark.money/research/ethereum-eip-7702-code-delegation-wallets) [Vendor], Spark: adoption; the original key keeps control.
- [Agentic wallet security](https://www.quillaudits.com/blog/web3-security/Agentic-Wallet-Security) [Vendor], QuillAudits, August 30, 2026.
- [How programmable wallets can limit autonomous spending](https://coincub.com/wallets/guides/how-programmable-wallets-can-limit-autonomous-spending/) [Vendor], Coincub: Grok incident; Coinbase Agentic Wallets date.
- ERC-4337 adoption figures, which conflict: [Zelcore](https://zelcore.io/newsroom/erc-4337-architecture-explained) [Vendor], [Eco](https://eco.com/support/en/articles/14797813) [Vendor], [Cobo](https://www.cobo.com/post/what-is-erc-4337) [Vendor].

**This repo**

- [Market and opportunity research](01-market-and-opportunity-research.md), section 5
- [Competitive analysis, round 2](10-competitive-analysis-round-2.md)
- [Product design strategy v2](../strategy/04-product-design-strategy.md)
- [Critical research questions](../strategy/09-critical-research-questions.md)
- [Wallet evolution research](../time-machine-workshop/wallet-evolution-research.md)
- [Weekly watch, November 2](../watch/2026-11-02.md)

*Regulatory points are research-based readings, not legal advice.*
