# Account Abstraction Deep Dive — Self-Custody Investment Account

As of November 6, 2026 · Builds on [01 §5, Technology enablers](01-market-and-opportunity-research.md#5-technology-enablers) (September 2026) and [10, Competitive analysis round 2](10-competitive-analysis-round-2.md) (October 20, 2026)

This is desk research from public sources: standards pages, wallet help pages and developer docs, vendor posts, press, and security research. No product was used hands-on. Each finding carries a source-type tag. Standards and developer docs are tagged [Help doc]. Undated help pages are marked "undated" with the day they were read. All sources were read on November 6, 2026.

Vocabulary follows the current terms: the user **defines** a **plan**, made of **rules**; **guardrails** are spending and exit limits.

**Why this doc.** Section 8 of the [strategy](../strategy/04-product-design-strategy.md#8-automation-stance) leaves open how the product acts inside the plan. Either the user signs every action, or the user grants a limited, revocable onchain permission. That choice and three candidate claims all depend on what an account can enforce: C5′ (your rules, executed exactly), C7 (protected exits) and C8 (proven recovery). Account abstraction is the technology that decides it. This doc updates 01 §5 and asks what the current state means for those decisions.

## Bottom line

1. **Smart-account features are now on by default in mainstream wallets, upgraded in place.** MetaMask's smart account capability is enabled by default [Help doc]. Trust Wallet lets people pay network fees in USDT or USDC on five networks [Vendor]. Both delegate only to their own code. Existing accounts get upgraded at the same address rather than moved to new smart-account addresses.
2. **An upgraded account still answers to its seed.** With EIP-7702, the account's original private key can override the smart account's security rules [Vendor]. A delay on loosening a rule, or a limit on large exits, set in a 7702 account can therefore be bypassed by whoever holds the seed, including a phished or coerced user. Guardrails that hold under pressure (principle 1, C7) need an account whose root key can be replaced. Today that means a full smart account at a new address, or protocol changes that are not yet live.
3. **Native account abstraction is scheduled, not close.** Ethereum's core developers moved EIP-8141 (Frame Transactions) to Scheduled for Inclusion in the Hegotá upgrade on August 27, 2026. Hegotá follows Glamsterdam and is due in 2027, and the spec is still a draft [Press]. On Base, the Cobalt upgrade went live on mainnet on September 30, 2026, and account abstraction is not in its feature list [Help doc]. Base's docs describe Base Transactions (EIP-8430, split out from EIP-8130) for a later upgrade, Everest, with activation dates "TBD" [Help doc]. The product should commit to capabilities, not to one mechanism.
4. **The limited, revocable permission now has standard shapes, but revoking still costs a fee.** ERC-7715 (an app asks the wallet for execution permissions) is still a Draft that requires wallets to display the permissions clearly [Help doc]. MetaMask ships it as Advanced Permissions [Help doc]. Coinbase's spend permissions show amount, frequency and start and end dates [Help doc]. Revoking one needs funds for the network fee [Help doc], which matches round 2's L2 finding. One-tap revoke is only one tap if the product covers that fee.
5. **The attack surface moved with the features.** One signed EIP-7702 authorization can hand an account's future execution to someone else's code [Report]. In the first weeks after launch, most delegations pointed to copy-pasted sweeper contracts [Press]. Single phishing losses reached about $1.54 million [Report]. Separately, a phishing kit now targets iCloud Keychain recovery to pull every synced passkey [Vendor]. C8's wording, "not tied to one Apple or Google account", is better evidenced than in round 2.

## What changed since 01

| 01 said (September 2026) | Now (November 6, 2026) | Effect |
| --- | --- | --- |
| 7702 is supported by MetaMask, Rabby, Trust, Coinbase Base Account and Safe | MetaMask's smart account capability is on by default and is switched per network for a fee; Trust Wallet's FlexGas pays fees in USDT, USDC, USDC.e or TWT on BNB Chain, Ethereum, Arbitrum, OP Mainnet and Base; both delegate only to their own code [Help doc] [Vendor] | Upgrading in place is the mass-market path; wallets restrict delegation to code they control |
| About 62M active smart accounts and about 14M 7702 accounts, from secondary aggregations | By mid-2026, about 1.22 billion UserOperations and 62.9 million addresses that sent at least one, which are not distinct or retained users; sponsored fees made up most of the volume [Vendor]. Base recorded 795.9K 7702 transactions in the last 30 days and 4.44M since Pectra [Report] | Count usage, not deployments. Smart accounts grew inside app flows; main-wallet migration did not happen [Vendor] |
| Session keys and permissions (ERC-7715): early production; a clear "what have I delegated?" UI is immature | ERC-7715 is still a Draft; MetaMask's Advanced Permissions can be revoked any time or left to expire, under Permissions [Help doc]; Coinbase's spend permissions show amount, frequency and dates, and revoking needs a network fee [Help doc] | Packaging exists; the cost of revoking remains (L2) |
| Passkeys depend on the platform account; recovery fails if the cloud account is lost | A phishing kit active since early 2026 abuses iCloud Keychain recovery so the attacker's device joins the victim's keychain and receives every synced passkey (Palo Alto Networks research, reported October 29) [Vendor]. On Solana, transactions still need Ed25519 signatures that passkeys cannot produce [Vendor] | Strengthens C8 as worded; a passkey alone is not proven recovery |
| Persistent delegations are a phishing target | More dated evidence: see the security record below [Report] [Press] | Same direction; the upgrade signature itself is the highest-stakes moment |
| Not covered | Native account abstraction: EIP-8141 scheduled for Hegotá (2027); Base's design moved from EIP-8130 to EIP-8430 [Press] [Help doc] | Real key replacement and native fee sponsorship are a 2027 question at the earliest on Ethereum |

## What account abstraction can do for this product

| Capability | What the user gets | Claims and lenses | Available today | Caveat |
| --- | --- | --- | --- | --- |
| Pay fees in the asset held | No ETH to keep for fees; a dollar sleeve stays in dollars | C3, L1 | Yes, on EVM networks (FlexGas pattern) [Vendor] | Someone runs the fee service; sponsorship moves cost and abuse handling to that operator [Vendor] |
| Several steps in one signature | Approve and deposit happen together or not at all, so no standing approval is left behind | C3, L2 | Yes; apps request it with EIP-5792 `wallet_sendCalls`, which is Final [Help doc] | The app and the wallet both have to support it |
| A limited, revocable permission to act inside the plan | The product (or an agent) executes the plan's rules without asking each time | C5′, L2, strategy §8 | Yes, in wallet-specific forms (MetaMask Advanced Permissions, Coinbase spend permissions, Glider's session key) [Help doc] | ERC-7715 is still a Draft; packaging differs by wallet |
| Guardrails the account enforces: caps, allowlists, delays | A phished or coerced user cannot loosen rules or drain the account in one step | C5′, C7, L3, principle 1 | Partly: an upgraded account can run the rules, but its seed can override them [Vendor] | Real enforcement needs a replaceable root key |
| Passkey signing | Sign with Face ID or a fingerprint instead of a seed | C2, L4 | Yes on EVM networks with a smart account; on Solana only through a program or a session that unlocks another key [Vendor] | A synced passkey ties recovery to one Apple or Google account |
| Replace a lost or exposed key without moving funds | Recovery that can be rehearsed without a migration | C8, L4 | Only with a full smart account; not with an upgraded (7702) account; native at protocol level from 2027 at the earliest [Press] | Upgraded accounts keep the seed as the root |

## Standards and their status

| Standard | What it does | Status | Source |
| --- | --- | --- | --- |
| ERC-4337 | Smart accounts at new addresses, with bundlers and paymasters outside the protocol | Final; about 1.22 billion UserOperations by mid-2026; a few operators carry most traffic | ZeroDev retrospective, August 12, 2026 [Vendor] |
| EIP-7702 | An existing account points at smart-account code, keeping its address | Final. The delegation persists until changed; an authorization with chain ID 0 is valid on every chain; pointing it at the zero address clears it; the spec advises wallets not to offer apps a way to request it | EIP page, created May 2024 [Help doc] |
| EIP-5792 | `wallet_sendCalls`: an app asks the wallet to submit a batch, all-or-nothing when flagged | Final | EIP page [Help doc] |
| ERC-7715 | An app asks the wallet for permission to execute on the user's behalf | Draft; wallets must show the permissions clearly and warn about dangerous ones | EIP page [Help doc] |
| ERC-7730 | Readable descriptions of what a signature does (clear signing) | Ledger introduced v2 and is transferring governance to the Ethereum Foundation | Ledger, May 15, 2026 [Vendor] |
| EIP-8141 | Native account abstraction on Ethereum: checking the signature, paying the fee and running the calls are separate steps | Scheduled for Inclusion in Hegotá on August 27, 2026; Hegotá due in 2027 after Glamsterdam; spec still a draft | 24/7 Wall St, September 7, 2026 [Press] |
| Base native account abstraction | Base Transactions (EIP-8430, split out from EIP-8130) | Activation dates "TBD" with the Everest upgrade; the EIP-8130 page says it runs only on a devnet | Base docs, undated, read November 6 [Help doc] |

## What shipping products do

| Product | What the user sees | What matters for this product |
| --- | --- | --- |
| MetaMask | A smart account at the same address, set up per network from Account details for a small fee, and reverted the same way; the seed still controls the account; only MetaMask's own contract is supported [Help doc] | Smart account capability is enabled by default [Help doc], so many users already have an upgraded account. Advanced Permissions are revoked under Permissions or expire on their own [Help doc] |
| Trust Wallet FlexGas | Choose the token that pays the network fee when sending or swapping [Vendor] | Delegation can point only at Trust Wallet's own infrastructure [Vendor]. The fee token must be held at the same address |
| Coinbase spend permissions | The prompt shows amount, frequency and start and end dates; approved with a passkey [Help doc] | Revoking needs funds for the network fee [Help doc] |
| Glider (from round 2) | Target allocation with scheduled rebalancing, run by a session key limited to what the user authorized [Help doc] | A working precedent for the execution model's second option, outside the US |
| Hardware wallets | As of March 2026, some hardware wallets cannot sign 7702 authorizations (Linea docs, undated) [Help doc] | A cold account may not get smart-account features |
| Several wallets on one address | The most recent 7702 delegation replaces earlier ones, because an address delegates to one contract at a time [Help doc] | A user who also uses another wallet can switch the product's account features off without knowing |

## What production taught

ZeroDev's ERC-4337 retrospective (August 12, 2026) [Vendor] reads production data against the standard:

- Smart accounts grew most where account creation disappeared inside an application flow. The data shows no broad move of main wallets to new smart-account addresses.
- Paying users' fees removed the fee from view but moved the complexity into billing, eligibility, limits and abuse handling.
- Session keys were narrow but durable wins, where an app could name the sequence or repeated signing was the bottleneck. Fine-grained permissions are still looking for a package.
- In its words: "Programmability became a product only when it addressed a pain someone already felt."

For this product that argues for leading with the felt pains: fees, approvals and rules the user defined. Account features shouldn't be sold as an upgrade in themselves.

## Security record

- **June 1, 2025.** Wintermute found more than 80% of EIP-7702 delegations pointed to copy-pasted sweeper contracts that drain wallets with leaked keys. SlowMist advised wallets to show the target contract prominently when users sign a delegation. A security expert said the root problem is leaked private keys, which 7702 makes cheaper to sweep [Press]. A later account of Wintermute's first-month data puts the share above 97% [Report].
- **May 24, 2025.** A user lost about $146,551 to a malicious 7702 batched transaction tied to Inferno Drainer [Report].
- **August 24, 2025.** One person lost about $1.54 million in wstETH, cbBTC and NFTs to a 7702 batch-transaction phish [Report].
- **December 13, 2025.** An academic paper showed that one signed authorization can give an attacker persistent control through three trigger pathways. Authorizations not tied to one chain allow replay-like compromises across networks, and the ERC-4337 entry point can reactivate delegated code without the victim. It measured more than 150k events and found authorizations concentrated in a few contract families linked to criminal activity (arXiv:2512.12174) [Report]. 01 §4 covers the same paper.
- **Early 2026 onward.** A phishing kit abuses iCloud Keychain recovery to receive every synced passkey (Palo Alto Networks research, reported October 29, 2026) [Vendor].

## Beyond Ethereum

- **Solana** pays fees through a fee payer that can be someone other than the sender. Kora, on solana.com, is a fee abstraction layer: its operators co-sign as fee payer and accept fees in SPL tokens such as USDC (undated) [Help doc]. Solana has verified P-256 signatures onchain since June 2025, but transactions still need Ed25519 signatures. Passkeys therefore authorize a session or a smart-wallet program rather than signing directly [Vendor].
- **Bitcoin** has no account code. Round 2's investor-grade bitcoin products (Bitkey, Casa) get delays and limits from multisig with a provider key, not from the account. That is why round 2 asks counsel whether a provider co-signer that can delay a transaction counts as control.

## Implications for the strategy

### The execution model (strategy §8, open)

- The second option, a limited, revocable onchain permission to act inside the plan, now has standard shapes. A session account holds a permission the user granted and redeems it within the account's rules, as MetaMask's Advanced Permissions and Glider's session key show [Help doc]. The rules travel with the account, not with the product's servers. That fits C5′ better than a model acting in a sandbox.
- **What "we cannot move your funds" means changes.** If the user's account runs code the product wrote, as MetaMask and Trust Wallet users' accounts do, then the product's ability to change that code is a power in its own right. It sits next to the permissions the user granted. The 7702 spec treats changing a delegation as security-critical [Help doc]. *Question for counsel: does product-authored, upgradeable account code affect the non-custodial interface relief?*

### Guardrails and protected exits (principle 1, C7, L3)

- Principle 1 says loosening a rule waits out a cooling-off delay. In an upgraded (7702) account, the seed can override the account's rules [Vendor]. So the delay protects against an app or agent acting outside its permission, but not against someone holding the seed. Three ways to close the gap:
  1. **Upgraded account, said plainly.** Use the account's rules for permissions granted to apps and agents, and tell the user the seed bypasses them. Fastest, but C7 holds only in part.
  2. **Full smart account at a new address**, whose root key can be replaced and whose rules bind every signer. C7 holds, at the cost of a funding move and an address the user has to learn. ZeroDev's data shows users rarely make that move unless it is hidden inside a flow [Vendor].
  3. **Wait for native account abstraction** (Hegotá, 2027 at the earliest, spec still changing) [Press].
- The bitcoin precedent, a provider co-signer that enforces delays, reaches the same result by another route. It carries round 2's open counsel question.

### Recovery (C8, L4)

- A synced passkey makes one Apple or Google account the real key, and that recovery path is now attacked directly [Vendor]. A passkey can be a factor, but alone it doesn't meet C8 as worded.
- Rehearsing recovery without moving funds needs a replaceable key, so option 2 or 3 above. With an upgraded account, a rehearsal can prove the seed restores access, but a real recovery after exposure still means moving everything.

### Permissions and one-tap revoke (principle 4, L2)

- The highest-stakes permission is the account's own delegation. It belongs at the top of "every permission the user has granted", with the code it points to named, as SlowMist advised [Press].
- Revoking costs a network fee at Coinbase [Help doc], and round 2 found the same at MetaMask. For revoke to be one tap, the product covers that fee or takes it in the asset the user holds.
- Another wallet on the same address can replace the product's delegation [Help doc]. The product should watch for it and say so.

### Not a DeFi operator (C3)

- Paying fees in the asset held and batching approve-plus-deposit remove two of C3's four operator tasks (gas and approvals) on EVM networks today [Vendor] [Help doc]. Chains and bridges are not touched by account abstraction.

### Naming (L7)

- Users see capabilities: "pay this fee in USDC", "both steps in one signature", "this app can spend up to 100 USDC a week until December 31". Standard numbers, "paymaster", "UserOperation" and "smart wallet" stay out of the interface. Whether "smart account" helps or hurts is a naming test, alongside the word "account" itself (strategy §10).

## Design principles this suggests (proposed, not decided)

1. **Capabilities, not standards.** People see what they can now do, never the mechanism.
2. **The product's own code or none.** The account delegates only to code the product publishes and has audited, with the version and changes shown. Apps and agents get permissions, never delegations.
3. **The upgrade is an irreversible-class action.** Turning on account features gets principle 3's step-by-step confirmation: what changes, what doesn't (address, seed), on which networks, and how to undo it.
4. **Every standing power in one list.** The delegation, approvals, permissions and agent mandates all sit in the custody map, each with one-tap revoke.
5. **Safety never waits on a fee coin.** Revoking, pausing or clearing a bad delegation works even when the user holds no ETH.
6. **Say what the seed can still do.** Until the root key can be replaced, guardrails are described as limits on apps and agents, not on the seed holder.

## Open questions

**For counsel**
- Does product-authored, upgradeable account code change the non-custodial analysis (strategy §8 and §10)?
- Does covering users' fees, or converting a held token to pay them, raise any US regulatory question?

**For engineering**
- Upgraded account, full smart account or both: which networks, and how a restore finds the account's delegation and permissions.
- Whose account code: the product's own, or an audited open implementation the product takes over; how upgrades are governed.
- One authorization for every chain (chain ID 0) or one per network, given the replay finding [Report].
- Which fee and bundler services, and the fallback when they are down.
- Hardware wallet support for 7702 authorizations [Help doc].

**For research** (the phase 1 gate)
- A8, defining a plan: do people understand that a rule binds apps and agents but not the seed holder? Test both wordings in the rules prototype.
- A9, the recovery drill: does a drill that proves the seed restores access build as much confidence as one that replaces a key?
- A4, own rules over management: does a visible, revocable permission list make granting the product a permission feel like control rather than handing over?

## Sources and confidence

Source-type tags: [Vendor], [Help doc], [Terms], [Filing], [Press], [Review], [Video], [User review], [Report], [Regulator]. Standards and developer docs are tagged [Help doc]. All read on November 6, 2026.

**Standards**

- [EIP-7702: Set EOA account code](https://eips.ethereum.org/EIPS/eip-7702) [Help doc], created May 2024, Final: persistence, chain ID 0, clearing, wallet guidance.
- [EIP-5792: Wallet call API](https://eips.ethereum.org/EIPS/eip-5792) [Help doc], Final: batching with an all-or-nothing flag.
- [ERC-7715: Request execution permissions](https://eips.ethereum.org/EIPS/eip-7715) [Help doc], Draft: wallets must display permissions.
- [The evolution of Clear Signing](https://www.ledger.com/blog-the-evolution-of-clear-signing) [Vendor], May 15, 2026: ERC-7730 v2 and governance transfer.
- [EIP-8141 scheduled for Hegotá](https://247wallst.com/investing/cryptocurrency/2026/09/07/ethereums-eip-8141-would-let-you-pay-gas-fees-in-stablecoins-instead-of-eth-will-it-actually-launch-with-hegota-in-2027/) [Press], September 7, 2026: August 27 decision, 2027 timing, draft spec.
- [Base: native account abstraction](https://docs.base.org/base-chain/network-information/native-account-abstraction.md) [Help doc], undated: Base Transactions (EIP-8430), Everest, dates TBD. [Base: EIP-8130](https://docs.base.org/upgrades/denim/eip-8130.md) [Help doc], undated: devnet only. [Base: Cobalt overview](https://docs.base.org/base-chain/specs/upgrades/cobalt/overview.md) [Help doc]: Sepolia live September 23, mainnet September 30, 2026; no account abstraction in its feature list.

**Wallets and infrastructure**

- [MetaMask: switch to or revert from a smart account](https://support.metamask.io/configure/accounts/switch-to-or-revert-from-a-smart-account/) [Help doc], undated: per-network set-up and revert for a fee, seed still in control, MetaMask's contract only.
- [MetaMask: Advanced Permissions](https://support.metamask.io/more-web3/dapps/advanced-permissions/) [Help doc], undated: enabled by default, revoke under Permissions or let expire.
- [Trust Wallet: FlexGas](https://trustwallet.com/blog/company/flexgas-pague-o-gas-com-twt-usdt-e-usdc) [Vendor], published May 26, 2025, updated August 19, 2026: networks, tokens, delegation to own infrastructure only.
- [Coinbase: Base account spend permissions](https://help.coinbase.com/en-gb/wallet/getting-started/smart-wallet-permissions) [Help doc], undated: prompt contents; revoking needs a network fee.
- [Alchemy: EIP-7702 overview](https://www.alchemy.com/overviews/eip-7702-ethereum-pectra-hardfork) [Vendor], May 19, 2025: the original key can override smart-account rules.
- [Etherscan: what you need to know about EIP-7702](https://info.etherscan.com/what-you-need-to-know-about-eip-7702-smart-account) [Help doc], June 13, 2025: one delegation per address; the latest replaces earlier ones.
- [Linea: EIP-7702 support](https://docs.linea.build/protocol/eip-7702.md) [Help doc], undated: some hardware wallets cannot sign authorizations as of March 2026.
- [Solana: Kora](https://solana.com/docs/tools/kora/getting-started) [Help doc], undated: fee payer co-signing, fees in SPL tokens.
- [Helius: Solana passkeys](https://www.helius.dev/blog/solana-passkeys) [Vendor], June 24, 2025: P-256 verification from June 2025; transactions still need Ed25519.

**Adoption and lessons**

- [ZeroDev: ERC-4337, Final, Not Finished](https://www.zerodev.app/blogs/erc-4337-final-not-finished) [Vendor], August 12, 2026: usage figures, sponsorship, session keys, no main-wallet migration.
- [growthepie: EIP-7702 activity by L2](https://www.growthepie.com/answers/most-smart-account-activity-ethereum-l2) [Report], data as of November 6, 2026: Base 795.9K in 30 days, 4.44M since Pectra.

**Security**

- [The Block: Wintermute on EIP-7702 sweepers](https://www.theblock.co/post/356481) [Press], June 1, 2025.
- [Zealynx: EIP-7702 wallet security](https://www.zealynx.io/research/smart-contracts/eip-7702-wallet-security) [Report], May 18, 2026, revised October and November 2026: the 97% figure, the May 24 and August 24, 2025 losses.
- [EIP-7702 Phishing Attack (arXiv:2512.12174)](https://arxiv.org/abs/2512.12174v1) [Report], December 13, 2025.
- [Corbado: synced passkey attacks](https://www.corbado.com/blog/synced-passkey-attacks-threat-models.md) [Vendor], October 29, 2026: iCloud Keychain recovery phishing.

**Confidence.** High for what standards pages and wallet help pages say about their own rules and products. Medium for adoption figures, which come from one infrastructure vendor's reading of a public dashboard and one tracker, and for loss figures reported by security firms. Native account abstraction dates are plans, not commitments, and Base's docs already show its design split across upgrades.
