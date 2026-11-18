# Account Abstraction Frameworks and Delegates — Self-Custody Investment Account

As of November 18, 2026 · Builds on [11, Account abstraction design brief](11-account-abstraction-design-brief.md) and [12, Account abstraction deep dive](12-account-abstraction-deep-dive.md)

This is desk research from public sources: developer docs, code repositories, block-explorer pages, audit reports, vendor posts and press. No product was used hands-on and no code was reviewed. It is not a security assessment. Each finding carries a source-type tag. Developer docs and repositories are tagged [Help doc], and explorer records and audits are tagged [Report]. Undated pages are marked "undated". Sources were read on November 18, 2026 unless marked otherwise. It started from a broader desk report that was not published. Every claim kept here was re-checked against the page cited, and claims that didn't hold up were corrected or dropped.

Vocabulary follows the current terms: the user **defines** a **plan**, made of **rules**; **guardrails** are spending and exit limits.

**Why this doc.** Research 12 leaves an engineering question open: whose account code the product runs, its own or an audited open implementation. Research 11 sets out the execution-model options for strategy §8. Both depend on which implementations exist, how they handle set-up and upgrades, and what they have been audited for. This doc compares them.

## Bottom line

1. **For upgrading an existing account in place, the safest shape is a delegate with no set-up step, no owner of its own and no upgrade path.** If a delegate needs an initialization call that anyone can make, an attacker can front-run it. If that call reverts, the delegation stays in place and the account is left for anyone to claim [Help doc]. MetaMask's stateless delegator stores no signer data and needs no initialization [Help doc]. Uniswap's Calibur has no upgrade path and no owner [Help doc].
2. **Most modular accounts are not meant to sit behind an existing account.**
   - Safe says its existing contracts cannot be used with EIP-7702, and that all its 7702 approaches are experimental and unaudited [Help doc].
   - Alchemy allows only one variant of its modular account as a 7702 target [Help doc].
   - ZeroDev, which makes Kernel, says that once an account hosts many modules its security boundary moves to how they combine [Vendor].
3. **Narrow permissions exist, but most teams haven't used them.** Kernel v3 could limit authority by target, function, value, token and time, but most integrations used the blanket "sudo" path. ZeroDev blames the shortest SDK path and immature permission UX [Vendor].
4. **Home-built delegates are where losses have come from.** In April 2026 an administrator account delegated to a home-built batch executor. Its batch function had no permission checks, and 1,988.5 QNT was drained [Press].
5. **Hardware wallets limit which delegates they will sign for.** Ledger initially allows only the Ethereum Foundation's simple 7702 contract [Vendor]. Trezor's 7702 support works only behind experimental features and keeps a list of allowed delegates [Vendor].

## Two jobs, two kinds of account

Research 11 and 12 point to two separate jobs. This doc treats them separately, as options rather than decisions.

| Job | What it needs | Kind of account |
| --- | --- | --- |
| Upgrade the user's existing account in place for fees paid in the asset held, batching and simple permissions | No set-up step, no upgrade path, a fixed feature set, the same address on every network | A minimal EIP-7702 delegate |
| Carry out the plan's rules under a limited, revocable permission (strategy §8, option B) | Caps, allowlists, time windows and expiry, enforced by the account, with a root key that can be replaced | A full smart account at its own address |

The second job needs a full smart account because, under EIP-7702, the original key keeps ultimate control of the account [Help doc]. Rules set in an upgraded account can therefore be bypassed by whoever holds the seed. Research 12 covers this.

## Delegates for in-place upgrades

| Delegate | Set-up | Upgrade path | What it adds | Audit seen |
| --- | --- | --- | --- | --- |
| MetaMask EIP7702StatelessDeleGator | Stores no signer data; needs no initialization; the account that shares its address controls it [Help doc] | The repository says 7702 contracts use a different upgrade mechanism from its earlier proxy design and doesn't describe it [Help doc] | Works through the ERC-4337 EntryPoint or directly; its constructor names a DelegationManager and EntryPoint v0.7 [Report] | Cyfrin, April 1, 2025, shown on Etherscan [Report] |
| Uniswap Calibur | Built for EIP-7702; the same address on supported networks [Help doc] | None: no upgrade path and no owner [Help doc] | Batching (including ERC-7821), fees paid through ERC-4337 with EntryPoint v0.8 by default, extra keys with their own limits [Help doc]; secp256k1, P-256 and WebAuthn key types; a hook per key [Report] | OpenZeppelin, published December 12, 2025: 0 critical, 0 high, 4 medium, 14 low [Report] |
| Simple7702Account (ERC-4337 reference team) | Minimal | — | Added to the core distribution in EntryPoint v0.8, which brought native 7702 support. EntryPoint v0.9 is ABI-compatible with v0.8 and v0.7 [Help doc] | Not checked in this pass |
| Coinbase EIP7702Proxy | Requires the account's own signature over the implementation, set-up data and expiry, then checks the account is secure, to stop set-up front-running [Vendor] | Yes: the account can point the proxy at another implementation with a signed call [Vendor] | Built so Coinbase Smart Wallet can run behind an existing account [Vendor] | Not checked in this pass |
| Trust Wallet delegate ("EIP-7702 Delegator 1") | Its interface has no initialize or owner function [Report] | — | Deployed April 25, 2025 [Report] | Quantstamp, final April 16, 2025: 0 high, 0 medium, 2 low (both fixed). The report says it reads guard storage, which breaks an ERC-4337 bundler rule (ERC-7562 STO-033), and that its 4337 off switch can be bypassed by undelegating, changing storage and re-delegating [Report] |
| OKX smart wallet | Not described [Help doc] | UUPS-upgradeable, with access control [Help doc] | Built-in ECDSA and passkey (WebAuthn/P-256) validators; ERC-4337, EIP-7702 and a relayer mode [Help doc] | An audits folder is linked; no auditor is named on the page [Help doc] |

**What the audits flag.**
- **Calibur:** OpenZeppelin resolved a finding that the signing domain left out the delegate address, which could let two delegations from the same account share a domain. It acknowledged, without fixing, two further findings: the WebAuthn user-verification flag is hard-coded off, and WebAuthn signing carries a blind-signing risk [Report].
- **Trust Wallet's delegate:** Quantstamp found it refers to an owner account and a nonce, so it is not stateless [Report].

## Full smart accounts for automated execution

| Account | Permissions and limits | Notes |
| --- | --- | --- |
| Alchemy Modular Account (ERC-6900) | Modules for address and function allowlists with ERC-20 spend limits, native-token spend limits, time ranges per signer, a required paymaster, and WebAuthn (passkey) signers [Help doc] | Only `SemiModularAccount7702` may be an EIP-7702 target; delegating to another variant with an unprotected initializer lets an attacker take over the account. Tagged releases are the audited versions [Help doc] |
| ZeroDev Kernel | v3 can limit authority by target, function, value, token and time [Vendor] | v3.3 added EIP-7702 support. ZeroDev says v4 isn't yet a long-running production result [Vendor]. Offchain Labs, the company behind Arbitrum, acquired ZeroDev on August 13, 2025 and says it will keep expanding to more chains [Vendor] |
| Biconomy Nexus with MEE | Not checked in this pass | The version recommended for new accounts, MEE 2.2.3 on Nexus 1.3.3, was reviewed by Pashov Audit Group in July 2026. MEE 2.3.0 is labelled an unaudited release candidate, not for production [Help doc] |
| Safe | Not checked in this pass | All three of Safe's 7702 approaches are experimental and unaudited. SafeLite, the version with no set-up step, isn't compatible with Safe{Wallet} and has no modules or guards [Help doc] |

**Inference.** None of the pages checked describes an "ask first above this amount" rule as a built-in feature. It would be built as a rule that requires the user's approval above a set amount.

## What shipping wallets delegate to

| Wallet | Delegate | What it means |
| --- | --- | --- |
| MetaMask | Its own stateless delegator, labelled "MetaMask: EIP-7702 Delegator" on Etherscan [Report]; only MetaMask's own contract is supported ([12](12-account-abstraction-deep-dive.md)) | A user who switches to a MetaMask smart account replaces any other wallet's delegation |
| Trust Wallet | Its own delegate, labelled "Trust Wallet: EIP-7702 Delegator 1" [Report] | Vendor-written and not stateless [Report] |
| Coinbase | EIP7702Proxy for Coinbase Smart Wallet [Vendor] | A proxy whose implementation the account can change with a signed call [Vendor] |
| Uniswap | Calibur, which underpins Uniswap's smart wallet features [Help doc] | No upgrade path and no owner [Help doc] |
| OKX | An upgradeable (UUPS) smart wallet [Help doc] | The opposite of pinning one fixed version |
| Ledger | Initially only the Ethereum Foundation's simple 7702 contract; all others blocked on the device. Ethereum app 1.17 is required, so the Nano S can't use EIP-7702 [Vendor] | Any other delegate isn't available to Ledger users until Ledger allows it |
| Trezor | Phase 1 works only behind experimental features. The phase 2 plan, opened October 29, 2026, adds a dedicated flag that is off by default and keeps a list of allowed delegates and a block on chain ID 0 [Vendor] | Allowed delegates may differ from the software wallets' |

**Usage counts are hard to read.**
- BundleBear's table of authorized contracts lists Simple7702Account at about 2.78 million live smart accounts and "Coinbase Wallet" at about 2.21 million.
- It also lists a contract group labelled "Crime" at about 2.34 million.
- Most of its top entries are unlabelled.
- The page shows no as-of date [Report].

## Incidents and formal analysis

- **April 29, 2026: QNT reserve pool.**
  - An administrator account for the pool delegated through EIP-7702 to a batch executor that trusted a batch-call contract.
  - The batch-call contract's batch function had no permission checks, so anyone could make arbitrary calls.
  - An attacker drained 1,988.5 QNT, about 54.93 ETH. SlowMist detected it [Press].
- **September 2026: DelegProof.** A formal analysis of EIP-7702 delegation combined with ERC-4337 found ten machine-checked attack patterns. These include storage confusion across re-delegation and a signature-substitution attack on contracts that rely on the account's signature check. It proposes three mitigations:
  - banning chain-ID-0 authorizations removes cross-chain replay;
  - an initialization gate bound to the account restores control of set-up, while an unbound gate can still be bypassed;
  - namespaced storage removes the storage-confusion class.

  The paper motivates the work with 63% of observed delegations pointing to malicious contracts [Report].
- **November 10, 2026: OpenZeppelin documentation.** OpenZeppelin documented that an initializer anyone can call is unsafe on a 7702 delegate [Help doc].
- **May 7, 2026: ethereum.org.** It calls delegated code a security boundary that can act as the user, including approving and moving tokens. It advises builders to rely on implementations the wallet has vetted, not to ask users to delegate to app-controlled code [Help doc].

## Implications for the strategy (proposed, not decided)

- **Pick, don't write.** The QNT loss came from a home-built delegate [Press], and ethereum.org advises against app-controlled delegates [Help doc]. The candidates that best fit "no set-up step, no upgrade path, audited" are MetaMask's stateless delegator and Calibur, with Simple7702Account if only batching and fee payment are needed. Each has an open check, listed below.
- **Pin one version, per network.**
  - Moving to a new version means every user signs a new authorization. That's a moment to design, and one phishers will copy.
  - Sign one authorization per network: DelegProof shows that banning chain ID 0 removes cross-chain replay [Report].
- **Keep automation in its own account.** A separate full smart account can enforce the plan's caps, allowlists and expiry, and its root key can be replaced. Prefer narrow, typed permissions over blanket ones. Kernel's history shows teams default to blanket access when the narrow path is harder [Vendor].
- **Check hardware support before choosing.** A delegate that Ledger or Trezor won't sign for leaves hardware users without account features [Vendor].
- **Watch for replacement.** Another wallet's delegation replaces the product's ([12](12-account-abstraction-deep-dive.md)). Detecting that and offering a reset should be part of the design.

## Open questions

**For engineering and security**
- Is MetaMask's DelegationManager upgradeable or pausable, and by whom? Its answer decides whether pinning the delegator pins the behaviour.
- In Calibur, does every path that registers keys or sets hooks require the account's own authorization? Is the hard-coded WebAuthn user-verification flag acceptable [Report]?
- Which EntryPoint versions (v0.7, v0.8, v0.9) do the chosen bundler and paymaster services support on each network?
- Which delegates do Ledger and Trezor allow, and when?
- Does the chosen delegate use namespaced storage, given the re-delegation finding [Report]?

**For research**
- Do users understand that pinning means a rare, product-initiated "new version" signature? Can they tell it apart from a phishing prompt? This extends AA1 in [11](11-account-abstraction-design-brief.md#11-research-questions).

## Sources and confidence

Source-type tags: [Vendor], [Help doc], [Terms], [Filing], [Press], [Review], [Video], [User review], [Report], [Regulator]. Developer docs and repositories are tagged [Help doc], and explorer records and audits are tagged [Report]. All read on November 18, 2026.

**Delegates and accounts**

- [MetaMask: EIP7702DeleGator](https://github.com/MetaMask/delegation-framework/blob/main/documents/EIP7702DeleGator.md) [Help doc], undated: no signer data, no initialization, control by the account at the same address.
- [Etherscan: MetaMask: EIP-7702 Delegator](https://etherscan.io/address/0x63c0c19a282a1b52b07dd5a65b58948a07dae32b) [Report], created March 31, 2025: label, Cyfrin audit dated April 1, 2025, constructor arguments.
- [Uniswap: Smart wallet overview](https://developers.uniswap.org/docs/protocols/smart-wallet/overview) [Help doc], undated: Calibur has no upgrade path and no owner; the same address across networks; batching; EntryPoint v0.8.
- [OpenZeppelin: Uniswap Calibur audit](https://www.openzeppelin.com/news/uniswap-calibur-audit) [Report], December 12, 2025: scope, severity counts, key types, hooks, findings.
- [ERC-4337 reference team: releases](https://github.com/eth-infinitism/account-abstraction/releases) [Help doc], v0.9 dated November 16 (year not shown): ABI compatibility; native 7702 support and Simple7702Account arrived in v0.8.
- [Base: Securing EIP-7702 upgrades](https://www.base.org/blog/securing-eip-7702-upgrades) [Vendor], June 10, 2025: EIP7702Proxy, signed set-up, changeable implementation.
- [Etherscan: Trust Wallet: EIP-7702 Delegator 1](https://etherscan.io/address/0xD2e28229F6f2c235e57De2EbC727025A1D0530FB) [Report], deployed April 25, 2025: label; no initialize or owner function in the interface.
- [Quantstamp: Trust Wallet smart account audit](https://strapi-cdn.trustwallet.com/Quantstamp_TW_Smart_Account_Short_version_no_findings_f57d9e0837.pdf) [Report], final April 16, 2025: severity counts, bundler-rule and off-switch notes.
- [OKX smart wallet repository](https://github.com/okxlabs/okx-smart-wallet-evm) [Help doc], undated: UUPS upgrades, validators, modes.
- [Safe and EIP-7702](https://docs.safe.global/advanced/eip-7702/7702-safe) [Help doc], undated: existing contracts unsafe as delegates; all approaches experimental and unaudited.
- [Alchemy modular account repository](https://github.com/alchemyplatform/modular-account) [Help doc], undated: the one variant allowed as a 7702 target; modules; tagged releases audited.
- [ZeroDev: Kernel v1 to v4](https://www.zerodev.app/blogs/kernel-v1-v4-what-production-kept-and-what-it-left-behind) [Vendor], August 13, 2026: sudo usage, composition, v4 status, v3.3 7702 support.
- [ZeroDev: acquired by Offchain Labs](https://www.zerodev.app/blogs/blog-zerodev-acquired) [Vendor], August 13, 2025: acquirer; multi-chain plans.
- [Biconomy: MEE versions](https://docs.biconomy.io/new/versions-and-migrations/mee-versioning) [Help doc], undated, review dates shown: recommended and unaudited versions.

**Wallets, hardware and usage**

- [Ledger: Pectra and EIP-7702](https://www.ledger.com/blog-pectra-upgrade-announcement) [Vendor], May 7, 2025, modified November 10, 2025: app 1.17, simple contract only, Nano S excluded.
- [Trezor: EIP-7702 phase 2](https://github.com/trezor/trezor-firmware/issues/8183) [Vendor], opened October 29, 2026: experimental features today; planned flag; list of allowed delegates and chain-ID-0 block kept.
- [BundleBear: EIP-7702 authorized contracts](https://www.bundlebear.com/eip7702-authorized-contracts/all) [Report], undated: top contracts by live smart accounts.

**Incidents and analysis**

- [PANews: QNT reserve pool drained through an EIP-7702 account](https://panews.io/articles/019dd769-5b5c-766d-beb4-9bb2e860e44d) [Press], April 29, 2026: the delegate, the flaw, the loss, detection by SlowMist.
- [DelegProof: a machine-checked security analysis of EIP-7702 delegation](https://eprint.iacr.org/2026/2060) [Report], September 2026: attack patterns and mitigations.
- [OpenZeppelin: safe set-up of accounts used as EIP-7702 delegates](https://github.com/OpenZeppelin/openzeppelin-contracts/issues/6868) [Help doc], November 10, 2026: initializer front-running.
- [ethereum.org: Building on Ethereum in 2026](https://ethereum.org/latest/building-on-ethereum-in-2026/) [Help doc], May 7, 2026: key control; security boundary; wallet-vetted implementations.

**Confidence.** High for what each repository, doc page and audit says about its own code. Medium for usage counts, which come from one dashboard with no as-of date and many unlabelled entries. Low for anything marked "not checked in this pass". This pass didn't verify Rabby, Phantom, Rainbow, Zerion, Ambire or thirdweb from primary sources, so they are left out.
