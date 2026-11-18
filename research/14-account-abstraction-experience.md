# Account Abstraction: Experience Opportunities and Limits — Self-Custody Investment Account

As of November 18, 2026 · Builds on [11, Account abstraction design brief](11-account-abstraction-design-brief.md), [12, Account abstraction deep dive](12-account-abstraction-deep-dive.md), [13, Frameworks and delegates](13-account-abstraction-frameworks.md) and the [experience map](../strategy/06-experience-map.md)

This is desk research from public sources: standards and developer docs, vendor posts, press, preprints and research papers. No product was used hands-on, and no user research was run. Each finding carries a source-type tag. Developer docs are tagged [Help doc]; papers, preprints and data dashboards are tagged [Report]. Undated pages are marked "undated". Sources were read on November 18, 2026. Findings from research 11 to 13 are linked rather than repeated. It started from a broader desk report that was not published. Every claim kept here was re-checked against the page cited, and claims that didn't hold up were dropped.

Vocabulary follows the current terms: the user **defines** a **plan**, made of **rules**; **guardrails** are spending and exit limits.

**Why this doc.** Research 11 sets principles and components for programmable accounts. This doc walks the experience map's seven stages to show where account abstraction changes the experience and where it doesn't. It also collects what is known about people (little) and pairs each limit with a design response.

## Bottom line

1. **The near-term wins are fewer steps, not new powers.** Paying the fee in the asset held and doing approve-and-deposit in one signature remove two of C3's operator tasks on EVM networks ([12](12-account-abstraction-deep-dive.md#not-a-defi-operator-c3)). ethereum.org advises apps to ask the wallet for the outcome through `wallet_sendCalls` and to let the wallet decide whether to use EIP-7702, ERC-4337 or another account system [Help doc].
2. **Authority that lasts is the new way to lose money.** A study of the first ten months after EIP-7702 went live found that roughly 70% of observed delegations pointed to ETH sweeper contracts. It counted 4,668,209 malicious delegations and more than 600,000 accounts that didn't promptly revoke or update one [Report]. The design work is making authority visible and easy to remove, not only easy to grant.
3. **Evidence about people is thin.** The studies found test how people read signing requests and how they rate recovery options, not account abstraction itself. No public conversion or drop-off figures for account abstraction features were found on the pages checked. Treat comprehension as untested.
4. **The mechanisms will keep changing.** Ethereum and Base developers stopped trying to align their native account abstraction proposals and will pursue separate standards [Press]. What the user is promised should stay the same when the mechanism changes ([11](11-account-abstraction-design-brief.md#6-experience-principles-for-programmable-accounts)).

## What changes at each stage

The stages are the [experience map](../strategy/06-experience-map.md)'s. "Inference" marks a reading not stated by a source.

| Stage | What account abstraction makes possible | What it doesn't change |
| --- | --- | --- |
| 1. Discover | Capabilities described as outcomes ("pay this fee in USDC"), with the networks they work on ([11 §3.4](11-account-abstraction-design-brief.md#34-other-networks-avalanche-c-chain-solana-and-bitcoin)) | Who holds the keys still needs explaining |
| 2. Onboard | Passkey signing on EVM networks with a smart account ([12](12-account-abstraction-deep-dive.md#what-account-abstraction-can-do-for-this-product)) | On an upgraded account the original key keeps ultimate control [Help doc]. A synced passkey ties recovery to one Apple or Google account ([12](12-account-abstraction-deep-dive.md#recovery-c8-l4)) |
| 3. Fund | Fees paid in the asset held: a paymaster on EVM networks, a fee payer on Solana ([11 §3.4](11-account-abstraction-design-brief.md#34-other-networks-avalanche-c-chain-solana-and-bitcoin)) | Bitcoin fees are paid in BTC. Someone runs the fee service, and its costs and abuse handling move to that operator ([12](12-account-abstraction-deep-dive.md#what-production-taught)) |
| 4. Allocate | Approve and deposit in one all-or-nothing signature, so no standing approval is left behind ([12](12-account-abstraction-deep-dive.md#what-account-abstraction-can-do-for-this-product)) | A batch can hide a step, so each step still needs decoding. Readable descriptions exist only for contracts that have a descriptor in the public registry [Press] |
| 5. Earn | One-step entry and exit on EVM networks; scheduled actions under periodic, stream or allowance permissions [Help doc] | **Inference:** waiting periods set by the protocol, such as unbonding, stay the same. Account abstraction shortens the path, not the clock |
| 6. Monitor | One list of every standing power: the account's delegation, token approvals, app permissions and automation grants, each with one-tap revoke (strategy principle 4) | Revoking costs a network fee unless the product covers it ([12](12-account-abstraction-deep-dive.md#permissions-and-one-tap-revoke-principle-4-l2)). MetaMask lists token-approval revocation only for its developer kit [Help doc]. More than 600,000 accounts with a malicious delegation didn't promptly revoke it [Report] |
| 7. Exit or recover | Delays and limits that bind, on a full smart account. On Bitcoin, a timelocked recovery or inheritance path. Nunchuk's inheritance path needs both an inheritance key and the wallet's configuration, and owners can postpone the timelock [Vendor] | On an upgraded account, whoever holds the seed can bypass its rules [Help doc]. Bitcoin timelocks need coins refreshed ([11 §3.4](11-account-abstraction-design-brief.md#34-other-networks-avalanche-c-chain-solana-and-bitcoin)) |

## Limits and design responses

| Limit | Evidence | Design response (proposed) |
| --- | --- | --- |
| Authority that lasts, used by sweepers | About 70% of observed delegations pointed to ETH sweeper contracts in the first ten months, and more than 600,000 accounts didn't promptly revoke [Report]. A formal analysis cites 63% of observed delegations pointing to malicious contracts [Report] | Delegate only to the one pinned implementation ([13](13-account-abstraction-frameworks.md)). Alert on any change to the account's delegation. Offer a sponsored one-tap reset. Put the delegation first in the custody map |
| The seed overrides an upgraded account's rules | ethereum.org: the original key keeps ultimate control, and delegated code is a security boundary that can act as the user [Help doc] | Describe those rules as limits on apps and automation, not on the seed holder. Use a full smart account where limits must bind ([12](12-account-abstraction-deep-dive.md#guardrails-and-protected-exits-principle-1-c7-l3)) |
| Open-ended session keys | Base's team found a session key could misuse approvals the user had already granted, because contracts trust whoever calls them. ERC-4337 added a way to drain a paymaster approval [Vendor] | Prefer narrow, typed permissions checked by a contract that accepts only tightly formatted requests, as Base's Spend Permissions do [Vendor]. Give every grant a cap and an end date |
| Modules combined into a large surface | Once an account hosts many modules, its security boundary moves to how they combine ([13](13-account-abstraction-frameworks.md#bottom-line)) | A fixed feature set on upgraded accounts; narrow modules only in the automation account |
| Mechanisms differ and change | Two native formats are coming [Press]. An address holds one delegation at a time, so another wallet can replace the product's ([12](12-account-abstraction-deep-dive.md#what-shipping-products-do)) | Promise outcomes. Show capability per network ([11 §3.4](11-account-abstraction-design-brief.md#34-other-networks-avalanche-c-chain-solana-and-bitcoin)). Detect a replaced delegation and offer a reset |
| Readable signing has gaps | The Ethereum Foundation backs a public registry where anyone can submit contract descriptors, which independent experts attest before wallets show them [Press] | **Inference:** a step with no descriptor needs louder treatment and simulation, never a silent fallback |
| Fee sponsorship is a dependency | Sponsorship moved complexity into billing, limits and abuse handling ([12](12-account-abstraction-deep-dive.md#what-production-taught)) | Always offer paying in the network's own coin. Say who pays. When a sponsor stops, fall back to the user paying, not to a failed action |
| Sponsoring costs little per action | ethereum.org's illustration: an ERC-20 transfer at about 65,000 gas costs roughly $0.076 at 0.5 gwei with ETH near $2,350 [Help doc] | **Inference:** sponsor the moments that matter (revokes, resets, recovery and the first deposit) rather than everything |
| Automation that acts with discretion | The April 13, 2026 SEC staff statement conditions relief on not exercising discretion ([11](11-account-abstraction-design-brief.md#9-applying-it-to-this-product)) | Every automated action traces back to a rule the user defined. Counsel reviews the execution model (research reading, not legal advice) |

## What is known about people

| Finding | Source | Confidence |
| --- | --- | --- |
| People judge signing requests by surface familiarity rather than by what the transaction does, and underestimate high-risk signatures. A decoder that explained signatures improved detection of risky ones, clarity and decision confidence, and lowered workload, in a between-subjects study of 128 | Preprint, January 23, 2026 [Report] | Medium: not specific to account abstraction; only the abstract was checked |
| A survey of 331 asked people to rate recovery options for usability, security and availability. The authors report notable views on sharing keys across devices and on trusting friends or family | ePrint, September 16, 2025 [Report] | Low to medium: the direction of the ratings wasn't checked beyond the abstract |
| Weekly retention of smart accounts fell below 1% five weeks after opening, and paymasters paid the fees for more than 97% of UserOperations in Q4 2023 | Alchemy report with BundleBear data, as reported by Blockworks, undated [Press] | Medium: early data from 2023 |
| Conversion or drop-off figures for account abstraction features from major wallets | Not found on the pages checked | Gap |
| Studies of how people understand EIP-7702 delegation, session keys or permissions | Not found on the pages checked | Gap |

Attacks are measured carefully; people aren't. The permission sheet, the upgrade moment and the batched review are untested in the way that matters, and AA1 to AA14 below are the product's own studies.

## Patterns this suggests (proposed, not decided)

These add to the components in [11 §7](11-account-abstraction-design-brief.md#7-patterns-and-design-system-components).

- **Signing severity levels.** They map to the strategy's three confirmation levels; the last gets the step-by-step confirmation and the delay of principle 1:
  - 0: read-only sign-in;
  - 1: a transfer to a known recipient;
  - 2: approvals and capped permissions;
  - 3: a delegation change, a large exit to a new payee, or loosening a guardrail.
- **Batched review.** Net effect first (you give, you get, you allow, fee), then numbered and decoded steps, then an explicit line saying nothing else happens. A step with no descriptor is shown more loudly.
- **Permission sheet.** Who, what, how much per period and in total, where, until when, and how to stop it. This matches Coinbase's spend-permission prompt (amount, frequency, dates; [12](12-account-abstraction-deep-dive.md#what-shipping-products-do)) and MetaMask's periodic, stream and allowance types [Help doc].
- **Cooling-off states.** Reuse the language of waiting states: "Withdrawal to a new address · available Thursday 14:00 · Cancel".
- **Automation activity log.** Each action cites the plan rule that allowed it and shows its inputs and when they were read, the outcome, the remaining budget and Pause.
- **Bitcoin recovery upkeep.** Show the time left, a refresh with its network fee, and a reminder well before the deadline.

**Anti-patterns.**
- Upgrade prompts that arrive from a website, email or support chat. ethereum.org advises against asking users to delegate to app-controlled code [Help doc].
- "Free" or "gasless" labels in place of who pays and in what.
- Open-ended session keys [Vendor].
- Limits on an upgraded account presented as hard limits [Help doc].
- Unlimited approvals to save a click, which batching makes unnecessary (inference).

## Outlook

- **Native account abstraction.** Ethereum scheduled EIP-8141 for Hegotá (2027), and Base's Base Transactions (EIP-8430) has no date ([11](11-account-abstraction-design-brief.md#3-state-of-play-november-2026)). The two will be separate standards [Press]. **Inference:** a later "move to native" moment will be another signature phishers can imitate. Design it before it is needed.
- **Clear signing.** As of May 12, 2026 the Ethereum Foundation acts as a neutral steward for clear signing, built on ERC-7730, which Ledger proposed in 2024. Contributors named include MetaMask, Trezor, WalletConnect and Fireblocks [Press].

## Research questions

These continue AA1 to AA8 in [11 §11](11-account-abstraction-design-brief.md#11-research-questions).

| # | Question | Method | What it decides |
| --- | --- | --- | --- |
| AA9 | In a batched review, do users notice an injected extra step? Does showing the net effect first or the steps first catch more? | Prototype with seeded steps | The batched-review layout |
| AA10 | Can users answer "who can move my money right now?" from the custody map within 30 seconds? | Timed task | Custody map structure |
| AA11 | Which caps and end dates do investors choose when they define a plan, and do they revisit them? | Plan prototype with defaults | Default caps and expiry |
| AA12 | Do people who left an exchange after a withdrawal pause read a cooling-off delay on their own exits as protection or as a custody red flag? | Concept test with that group | How delays are framed (principle 1, C7) |
| AA13 | Will users rehearse recovery when prompted, and does rehearsal change confidence? | Prompted drill over several weeks (extends A9) | Recovery rehearsal (C8) |
| AA14 | How much explanation does an automation activity log need before users trust an automated rebalance? | Log variants in a diary study | Activity log detail |

## Sources and confidence

Source-type tags: [Vendor], [Help doc], [Terms], [Filing], [Press], [Review], [Video], [User review], [Report], [Regulator]. Developer docs are tagged [Help doc]; papers, preprints and dashboards are tagged [Report]. All read on November 18, 2026. Findings linked to research 11, 12 and 13 carry those docs' sources.

**Standards and platform guidance**

- [ethereum.org: Building on Ethereum in 2026](https://ethereum.org/latest/building-on-ethereum-in-2026/) [Help doc], May 7, 2026: key control, security boundary, `wallet_sendCalls`, advice against app-controlled delegation, the fee illustration.
- [MetaMask: Supported Advanced Permissions](https://docs.metamask.io/smart-accounts-kit/get-started/supported-advanced-permissions/) [Help doc], undated, Smart Accounts Kit 2.0.0: permission types; token-approval revocation listed for the kit only.
- [Base: From session keys to sub accounts](https://www.base.org/blog/subaccounts) [Vendor], February 27, 2025: problems with session keys; Spend Permissions and Sub Accounts.

**Market and ecosystem**

- [The Block: Ethereum Foundation rolls out support for Clear Signing](https://www.theblock.co/news/regulation/2026-05-12-ethereum-foundation-rolls-out-support-for-clear-signing-crypto-security-solution-401001) [Press], May 12, 2026: stewardship, attested registry, contributors.
- [The Block: Ethereum and Base developers abandon effort to align account abstraction proposals](https://www.theblock.co/news/ecosystems/2026-09-15-ethereum-base-account-abstraction-proposals-414775) [Press], September 15, 2026: separate standards.
- [Blockworks: Alchemy report on smart accounts](https://blockworks.com/news/alchemy-report-smart-accounts) [Press], undated, Q4 2023 data: retention and paymaster share.
- [Nunchuk: Autonomous inheritance](https://nunchuk.io/blog/autonomous-inheritance) [Vendor], November 12, 2025: Miniscript timelocks, two secrets for a beneficiary, postponing the timelock.

**Research**

- [What I Sign Is Not What I See: towards explainable and trustworthy wallet signatures (arXiv 2601.16751)](https://arxiv.org/abs/2601.16751) [Report], January 23, 2026: familiarity-based judgment; decoder study with 128 participants.
- [Web3 recovery mechanisms and user preferences (IACR ePrint 2025/1687)](https://eprint.iacr.org/2025/1687) [Report], September 16, 2025: survey of 331.
- [Who Swept My ETH? EIP-7702-based Ether redirection attacks (arXiv 2610.41153)](https://arxiv.org/abs/2610.41153) [Report], October 30, 2026: malicious delegations, sweeper share, accounts that didn't revoke.
- [DelegProof: a machine-checked security analysis of EIP-7702 delegation (IACR ePrint 2026/2060)](https://eprint.iacr.org/2026/2060) [Report], September 2026: the 63% figure cited as motivation.

**Confidence.** High for what platform docs say about their own products. Medium for security measurements, which come from preprints. Low for evidence about people: two studies read at abstract level and one dated retention figure. This pass couldn't load two sources, so their claims are left out: a CHI 2024 study of how people choose and secure wallets, and press reports on the October 2026 Binance breach.
