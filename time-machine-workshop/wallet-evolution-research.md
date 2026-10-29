# The Evolution of Crypto Wallets, 2009 to October 2026: From wallet.dat to Programmable, Agent-Ready Accounts

> **Provenance.** This is the output of a research task run on 2026-10-29 as the pre-read for the Time Machine workshop. It is not a competitive-watch file, so it was not checked claim by claim under the source rules in `CLAUDE.md`, and the sources at the end are the task's citations, not URLs re-fetched for this repo. Figures from 2025 and 2026 are cited to named sources in the text and flagged where sources conflict. Treat adoption numbers as directional. Individuals named in the original report are referred to by role.

The wallet has turned from a key file into a programmable account with rules. Each major shift moved the main design problem: first "don't lose the file," then "write down 12 words," then "understand what you're signing." Today the problems are "decide what this account, app or AI agent is allowed to do" and "recover without a seed phrase." Losses data from 2025–2026 shows two things. Mass-market drainer theft fell sharply, though Scam Sniffer, the main tracker, ties the drop mainly to lower market activity rather than proving that wallet-side protections caused it. The largest losses now come from the signing interface and the software supply chain, not from broken cryptography.

## TL;DR
- **The architecture is converging on smart accounts.** EIP-7702 (live since Pectra, May 7, 2025) lets existing addresses gain batching, gas sponsorship, passkeys and scoped permissions without changing address. Trackers counted roughly 45–60 million live delegations by August–September 2026, but much of that is inflated by attacker "sweeper" bots. Embedded and wallet-as-a-service (WaaS) providers now sit inside payments and custody companies: Stripe owns Privy and Fireblocks owns Dynamic.
- **Security has moved from keys to comprehension and supply chain.** Drainer phishing losses fell 83% in 2025 ($494M to $83.85M, Scam Sniffer). Scam Sniffer's report ties the drop mainly to market activity, describing phishing as "a probability function of user activity," and warns that the decline "may partly reflect a shift toward harder-to-track attack vectors." Over the same period, Bybit lost about $1.46B through a tampered Safe{Wallet} interface plus blind signing on hardware wallets, and Trust Wallet's Chrome extension was trojanized through a leaked publishing key. In response, clear signing (ERC-7730) became an Ethereum Foundation–stewarded standard in 2026.
- **The next frontier is delegated authority, for apps, subscriptions and AI agents.** Coinbase, Phantom, Trust Wallet and MetaMask all shipped agent wallets or agent tooling in 2026. x402 agent micropayments passed 138M transactions on Base by Q3 2026 (Chainalysis). The first documented prompt-injection theft from an agent wallet (Grok/Bankrbot, May 2026) shows that spending policies have to be enforced on-chain, not by the model. For product teams, the core design task is now a permissions UX that people can understand, review and revoke.

*Scope and assumptions:* "Wallet" here means the software and hardware that holds or controls signing authority, plus the UX layer around it. Most of the depth is on Bitcoin and EVM chains, with Solana covered where it shaped UX. History before 2024 is well established and drawn from widely documented record. Figures from 2025–2026 are cited to named sources, and conflicts between sources are flagged. Many 2026 adoption numbers come from dashboards or secondary aggregators and should be treated as directional.

---

## Key Findings

1. **Every key-management innovation traded one failure mode for another.** wallet.dat files were lost. Seed phrases were phished and photographed. Multisig was misconfigured or blind-signed. MPC adds dependence on a provider. Passkeys are tied to platform cloud accounts. Smart accounts bring delegation and upgrade risk. No architecture removes risk; each moves it somewhere else. Design quality depends on whether the moved risk is visible and recoverable.
2. **The signing moment is the most important surface in crypto UX.** Drainers, Permit phishing, the Bybit UI swap and EIP-7702 phishing kits all exploit the gap between what the screen shows and what gets signed. Simulation and clear signing are the strongest-evidenced interventions.
3. **The industry is choosing smart-account upgrades over migrations.** EIP-7702 succeeded where ERC-4337-only smart wallets stalled because users keep their address. Native account abstraction (EIP-8141 "Frame Transactions") is targeted for the Hegotá fork after Glamsterdam, but it is still a Draft.
4. **Wallets are becoming financial front ends.** MetaMask, Phantom and Coinbase Wallet now bundle swaps, perpetuals (via Hyperliquid), rewards and cards. Coinbase's Base App social experiment (July 2025 to September 2026) failed and was reverted to a trading-first Coinbase Wallet.
5. **Regulation largely protects self-custody software while formalizing custodial and issuer layers.** The OCC's GENIUS Act rules state that the Act does not prohibit self-custody, and they exempt firms that only provide self-custody hardware or software from custody rules. The Act takes effect January 18, 2027.
6. **Agentic wallets are real but early.** Production volume consists mostly of micropayments; 87% of x402 payments are under $0.10. The security model, meaning on-chain caps, allowlists, TEEs and human-in-the-loop modes, is still settling.

---

## Timeline of Key Milestones

| Year | Milestone | UX/design significance |
|---|---|---|
| 2009 | Bitcoin v0.1 (original client, later Bitcoin-Qt/Core) stores keys in wallet.dat | Full node and wallet in one; backup means copying a file |
| 2011 | Wallet encryption added to the client; Electrum, Blockchain.info web wallet and Bitcoin Wallet for Android launch | Light clients and mobile; first custodial/hosted-key trade-offs |
| 2012 | BIP32 (HD wallets); BIP16 P2SH enables practical multisig | One seed backs up unlimited addresses |
| 2013 | BIP39 mnemonic seed phrases | The "write down 12/24 words" ritual is born |
| 2014 | BIP44 multi-account paths; Trezor ships; Ledger founded; Mt. Gox collapse | Hardware isolation; "not your keys, not your coins" |
| 2015–16 | Ethereum launches; MetaMask browser extension (2016) | Wallet becomes the identity and dApp connector |
| 2017 | SegWit activates; ERC-20 boom; Trust Wallet launches (acquired by Binance 2018) | Token lists, gas, approvals enter UX |
| 2018 | WalletConnect protocol; Gnosis Safe multisig; Argent (social recovery) | Mobile-to-dApp via QR; contract wallets |
| 2020–21 | DeFi/NFT summer; Rainbow, Phantom (2021); Taproot (Nov 2021) | Approvals and NFT `setApprovalForAll` become attack surface |
| 2022 | FTX collapse (Nov) | Self-custody narrative surges |
| 2023 | ERC-4337 EntryPoint live (Mar); Ordinals; Ledger Recover controversy (May); Ledger Connect Kit supply-chain exploit (Dec) | Smart accounts, inscriptions, recovery-as-a-service debates |
| 2024 | US spot Bitcoin ETFs (Jan); Runes (Apr); Coinbase Smart Wallet (passkeys); ERC-7730 clear signing initiative; drainer losses peak at ~$494M | Institutional rails; seedless onboarding; signing-comprehension push |
| 2025 | Bybit ~$1.46B (Feb 21); Pectra/EIP-7702 (May 7); Stripe buys Privy (Jun 11); GENIUS Act enacted; Base App rebrand (Jul); Fireblocks buys Dynamic (Oct 23); Fusaka/EIP-7951 passkey precompile (Dec 3); Trust Wallet extension compromise (Dec 24) | Upgrade-in-place smart accounts; WaaS consolidation; supply-chain risk |
| 2026 | Coinbase Agentic Wallets (Feb 11); Phantom MCP server (Feb 18); Trust Wallet Agent Kit (Mar 26); ERC-7730 v2 (Apr); EF Clear Signing launch (May 12); Grok/Bankrbot prompt-injection theft (May 4); Ledger pauses IPO (May); x402 Foundation under Linux Foundation (Jul 14); MetaMask Agent Wallet GA (Aug 6); Base App reverts to Coinbase Wallet (Sep 10); OCC GENIUS final rule (Oct) | Agent permissions, clear-signing standardization, regulatory clarity for self-custody |

---

## Details

### 1. Origins (2009–2013): the key file era
**Technical:** The original Bitcoin client (later Bitcoin-Qt, then Bitcoin Core) was a full node with a built-in wallet. Private keys sat in a Berkeley DB file, `wallet.dat`, with a pre-generated "keypool" of keys. Encryption did not arrive until 2011. Backups went stale, because change outputs went to new keys from the pool that an old backup did not contain. Light clients followed: Electrum (2011) introduced a deterministic seed before BIP39, and Blockchain.info offered a browser-based wallet where keys were encrypted client-side. Android wallets (the Bitcoin Wallet app) used SPV.

**UX implications:** Onboarding meant downloading the whole blockchain. Recovery meant finding the right file. Security depended on the host PC. Chainalysis (June 2020, reported by Decrypt) estimated that about 3.7M BTC, roughly 20% of minted supply, had not moved in at least five years and were probably lost. Its earlier November 2017 estimate was 2.78M–3.79M BTC (17–23%). That established the first design problem of crypto UX: *the user is the backup system*. Exchanges like Mt. Gox were the convenient alternative, and their failure in 2014 created the "not your keys" ethos that drove the next decade.

### 2. Key management milestones: HD wallets, mnemonics, multisig
- **BIP32 (2012)** created hierarchical deterministic wallets: one master seed derives a tree of keys. **BIP39 (2013)** encoded that seed as 12–24 words. **BIP44 (2014)** standardized derivation paths for multiple coins and accounts.
- **What it solved:** a single, one-time, human-transcribable backup that works across wallets. That made wallet portability, and therefore a competitive wallet market, possible.
- **What it created:** the seed phrase became a bearer instrument that users are asked to protect perfectly and never type anywhere. It is the main phishing target ("validate your wallet") and the cause of the "paper in a drawer" anxiety. Derivation-path mismatches between wallets made restores appear to show missing funds, a long-running support problem.
- **Multisig (P2SH, 2012; Gnosis Safe on Ethereum, 2018):** removes single points of failure and is now the default treasury model. The UX costs are coordinating several devices, setup complexity and, as Bybit showed, a dangerous dependence on whichever interface presents the transaction to signers.

### 3. Hardware wallets (2014 onward) and their incidents
**Evolution:** Trezor (first commercial device, shipped 2014) used a general-purpose MCU and open-source firmware. Ledger used secure-element chips and a proprietary OS. Later entrants such as Coldcard, Keystone, Foundation, BitBox and Trezor Safe models pushed air-gapped signing via QR codes, microSD and PSBT (partially signed Bitcoin transactions), and secure elements became nearly universal. Market data is commercial and approximate. Ledger's CEO, in the company's Atom launch post on ledger.com, cites "more than eight million devices sold in 165 countries," and secondary aggregators put Trezor at more than 2 million. Ledger hired banks for a reported $4B+ US IPO in January 2026 but put it on hold in May 2026 because of market conditions, according to CoinDesk.

**Key incidents and lessons:**
- *Ledger customer database leak (2020):* physical-world phishing and "wrench" risk. Privacy of the purchase is part of wallet security.
- *Ledger Recover (May 2023):* an optional, ID-verified seed-sharding backup caused an outcry because it showed firmware *could* export key material. Lesson: trust models must be communicated explicitly. Users judged it a betrayal of the "keys never leave" promise even though the feature was opt-in.
- *Ledger Connect Kit (December 2023):* a compromised npm package injected a drainer into dApps that used Ledger's connector library. Ledger's December 20, 2023 statement said "approximately $600,000 in assets were impacted or stolen... through blind signing on EVM dApps"; CoinDesk separately reported about $484K. Lesson: the JavaScript supply chain around the device is part of the attack surface.
- *Bybit (February 21, 2025, ~$1.46B):* The Safe Ecosystem Foundation attributed the attack to "a compromised Safe{Wallet} developer machine resulting in the proposal of a disguised malicious transaction." Its forensic review "did NOT indicate any vulnerabilities in the Safe smart contracts or source code." Signers saw what looked like a routine transfer; the actual payload replaced the multisig's implementation contract. The Ledger devices could not decode the payload, so the signers were **blind signing**. Lesson: hardware wallets only protect you if the device can display what it is signing. Three days later Safe removed its legacy `eth_sign` fallback.

**Design takeaway:** The hardware wallet's value has moved from "keys are offline" to "the trusted display is the source of truth." That is why clear signing (section 4) is now the core hardware-wallet roadmap.

### 4. Ethereum and the smart-contract era
**What changed:** With MetaMask (2016), a wallet stopped being only a payment tool and became the user's identity, login and transaction-approval layer for every dApp. Injected providers (`window.ethereum`) and later EIP-6963 multi-wallet discovery shaped desktop. WalletConnect (2018) did the same for mobile through QR-code sessions. WalletConnect now reports 700+ wallets and 80,000+ apps, and its H1 2026 review cited $207.82B in total network volume across about 19.08M on-chain transactions.

**New design problems:**
- **Token approvals.** ERC-20 `approve` (often unlimited), NFT `setApprovalForAll`, and off-chain signatures (EIP-2612 Permit, Permit2) let a single signature authorize future transfers. Scam Sniffer's 2025 report (via Cointelegraph) records the year's largest single drainer theft as a "$6.5 million Permit-based theft," down from a $55.4M largest case in 2024.
- **Signing comprehension.** Raw hex calldata and EIP-712 typed data are unreadable to most users. Blind signing on hardware devices became normal for DeFi.
- **Phishing and drainer-as-a-service.** Drainer kits (Inferno, Angel, Pink and others) industrialized theft. Scam Sniffer counted ~$494M stolen from ~332,000 victims in 2024. In 2025 that fell to **$83.85M across 106,106 victims**, an 83% drop. Only 11 thefts exceeded $1M, versus 30 in 2024.
- **Responses that worked:** transaction simulation (asset-change previews), domain and contract risk scoring (Blockaid, Wallet Guard and in-wallet equivalents), approval revocation tools, and clear signing. Ledger's ERC-7730 standard (2024) uses JSON metadata to render calldata in plain language. Ledger shipped a Generic Parser in 2025 and ERC-7730 v2 in April 2026, and moved governance to the Ethereum Foundation. The EF launched "Clear Signing" on May 12, 2026, with a working group spanning MetaMask, Ledger, Trezor, Fireblocks and WalletConnect.
- **Caveat:** Scam Sniffer warns the decline "may partly reflect a shift toward harder-to-track attack vectors" such as key compromise and targeted social engineering. Simulation itself can be spoofed (Scam Sniffer documented "transaction simulation spoofing" in January 2025). Address poisoning needs no signature. On December 19–20, 2025, one victim sent 49,999,950 USDT to a look-alike address (0xBaFF…f8b5) after a $50 test transfer. Web3 Antivirus flagged the theft, CoinDesk and SlowMist reported it, and the funds were swapped to ETH and moved through Tornado Cash.

### 5. Multi-chain and mobile-first wallets
Trust Wallet (2017), Coinbase Wallet (2018), Rainbow (2020) and Phantom (2021, Solana-first) showed that mobile-native, consumer-grade design could match exchange apps. The defining patterns were in-app dApp browsers (a workaround for mobile's lack of extensions), token discovery and spam filtering, NFT galleries, built-in swaps (MetaMask charges 0.875%; Phantom ~0.85%) and, later, perps.

**Adoption snapshot (self-reported; treat as directional):**

| Wallet | Reported scale | Notes |
|---|---|---|
| MetaMask | 30M+ MAU (figure repeated since 2022; reaffirmed at Dec 2025 Bitcoin launch), 143M downloads | Native Bitcoin (Dec 2025), Solana, perps via Hyperliquid, Rewards program; MASK token confirmed but not launched as of reporting |
| Trust Wallet | ~220M users (company figure) | Binance-owned; Agent Kit (Mar 2026) |
| Phantom | 15M MAU (Jan 2025 Series C), ~17M peak | $3B valuation; multichain; perps |
| Coinbase Wallet | Not disclosed | Rebranded "Base App" Jul 2025; reverted Sep 10, 2026 to a trading-first, 11-chain self-custodial app |

The **MAU figures are not comparable.** The MetaMask "30M" figure is old and unaudited, and "100M+ users" claims refer to lifetime installs.

**Design lesson from the Base App reversal:** Coinbase's 14-month "everything app" with social features "never quite clicked." In January 2026 Base's lead pivoted it to "trading-first," and the Coinbase Wallet name returned because it "tells users exactly what the product is." Users want a wallet to be a clear financial tool, not a social network.

**The multi-chain cost:** every new chain adds address formats, gas tokens, bridges and network-switch prompts. This "cross-chain complexity" is now the largest source of friction that is not about security.

### 6. Custodial vs non-custodial dynamics
- Exchange collapses (Mt. Gox 2014, QuadrigaCX 2019, Celsius/FTX 2022) each strengthened the self-custody story. FTX's November 2022 failure in particular drove hardware wallet sales and withdrawals.
- **But custody risk did not disappear; it moved.** Chainalysis counted $3.4B stolen in 2025, dominated by the Bybit service compromise. Personal-wallet compromises reached **158,000 incidents and ~80,000 unique victims** in 2025, a record count. Their *value* ($713M) fell from $1.5B in 2024, and they made up 20% of total stolen value, down from 44%. Chainalysis's mid-year figure (23.35%) differs because it covers a different period. Physical "wrench attacks" rose with the bitcoin price.
- **Regulatory influence:** EU MiCA pushed some custodial Lightning services out of the EU. The April 2024 Samourai Wallet arrests caused Phoenix to leave the US market temporarily (it returned in April 2025). In the US, the GENIUS Act (2025) explicitly does not regulate peer-to-peer transfers or self-custody of payment stablecoins. In its October 2026 final rule, the OCC wrote that "the Act does not specifically prohibit self-custody or non-hosted wallets," while noting that issuers' lawful-order, AML and sanctions duties still apply. Firms that only provide self-custody hardware or software are excluded from the custody requirements. Effective date: January 18, 2027. Expect pressure on *issuers* (freeze and blacklist capability) rather than on wallet software.

### 7. Smart accounts and abstraction
- **Contract wallets first:** Gnosis Safe (2018) for multisig and treasuries; Argent (2018–19) for guardian-based social recovery. Both proved the model, but they needed a new address, deployment gas and relayers, and many dApps did not support contract signatures (ERC-1271).
- **ERC-4337 (EntryPoint live March 2023)** standardized smart accounts without a hard fork, using UserOperations, bundlers and **paymasters** for gas sponsorship. A late-August 2026 BundleBear-sourced summary cited 1.26B+ UserOperations, ~65M active accounts and ~$13.6M of paymaster-covered gas. Modular standards (ERC-7579) and **session keys** enabled scoped, expiring permissions.
- **EIP-7702 (Pectra, May 7, 2025)** was the turning point. Any EOA can sign an authorization that points its code to a smart-account implementation, keeping the same address and key. MetaMask Smart Accounts, Ambire, Trust Wallet, OKX, Safe and Coinbase all integrated it. Most delegate to 4337-compatible implementations, and eth-infinitism's EntryPoint v0.8 added native 7702 support.
  - **Adoption is contested.** Secondary reports citing BundleBear give 45.1M (August 2026), ~51–53M (late August) and ~60M (September) live delegations against 214–250M cumulative authorizations. Much of the gap comes from sweeper bots. Wintermute found more than 97% of early delegations used one reused sweeper contract ("CrimeEnjoyor"). A USENIX Security 2026 paper analyzed this "dark side," and Scam Sniffer recorded two EIP-7702 batch-phishing cases totaling $2.54M in August 2025.
  - **UX implication:** "upgrade your account" is now a high-trust prompt that phishers imitate. Wallets should only allow delegation to allowlisted implementations, and should never let a dApp trigger it.
- **Native AA is next but not yet decided.** EIP-8141 (Frame Transactions) split validation, payment and execution into frames, making gas sponsorship, passkeys and post-quantum signatures native. It is Draft, and as of September 2026 it was graded "Must ship" by the EF for **Hegotá**, which comes after Glamsterdam (itself estimated for Q4 2026). A competing Base-proposed design, EIP-8130, has prominent supporters, including a WalletConnect leader. Do not assume a mainnet date. ethereum.org's own guidance is that "the practical 2026 build path for account UX is still EIP-7702 plus ERC-4337."
- **Chain abstraction and intents:** solver networks and cross-chain execution layers (e.g., Relay, ERC-7683-style intents) let users state outcomes ("pay 10 USDC on Base") instead of routes. This removes gas tokens and bridge steps but shifts trust to solvers and makes "what am I signing" harder to show.

### 8. Beyond the seed phrase: MPC, passkeys, embedded wallets
- **MPC/TSS** splits signing between device and server (e.g., Fireblocks for institutions; ZenGo and Dynamic for consumers). There is no single seed, but recovery and liveness depend on the provider. Whether a given MPC wallet is truly self-custodial depends on its export and exit path, and that varies by vendor.
- **Passkeys/WebAuthn** use P-256 keys in Secure Enclave or Android Keystore. Coinbase Smart Wallet (2024) made passkey-native smart accounts mainstream. **Fusaka (December 3, 2025) added EIP-7951**, a secp256r1 precompile (~6,900 gas per verification), so passkey signatures are cheap to verify on Ethereum L1 as well as L2s. Trade-off: the account's security now rests on Apple and Google cloud-account recovery and sync policies.
- **Embedded wallets / WaaS** create a wallet at email or social login, usually with key shares in TEEs or MPC. This category consolidated quickly. **Stripe acquired Privy (announced June 11, 2025; 75M+ accounts)**. **Fireblocks acquired Dynamic (October 23, 2025; 50M+ on-chain accounts)**. Consensys acquired Web3Auth (being renamed MetaMask Embedded Wallets). Paxos bought Fordefi, and Kraken parent Payward bought Magic's wallet business. Turnkey (TEE-based key infrastructure), Crossmint (smart-contract wallets) and Coinbase CDP Embedded Wallets remain major independents and platforms.
- **What this means for product:** "seedless" onboarding is now commodity infrastructure. The differentiators are (a) exit and portability (can users take their keys or account elsewhere?), (b) recovery UX, and (c) how wallet permissions are shown when the user never chose "a wallet." Vendor concentration is now a strategic risk: your wallet layer may belong to a payments competitor.

### 9. Bitcoin-specific evolution
- **SegWit (2017)** fixed transaction malleability (needed for Lightning) and cut fees; bech32 addresses (bc1q...) followed. **Taproot (November 2021)** brought Schnorr signatures, more private multisig and script spends, and bc1p addresses. Wallet UX had to handle several address types and fee estimation.
- **Lightning UX** went from manual channel management, to custodial shortcuts (e.g., Wallet of Satoshi), to *automated self-custody*. Phoenix (ACINQ) runs a mobile node with a single spliced channel. Breez's SDK now offers Liquid, Spark and Ark backends. Wallet of Satoshi moved to self-custody via Spark. Trade-off: "self-custodial" Lightning still trusts an LSP, a federation or protocol operators to varying degrees, and wallets rarely explain this well. Fees are explicit (e.g., Phoenix 0.4% send).
- **Ordinals (2023) and Runes (April 2024)** turned individual satoshis into collectibles and tokens. Wallets had to avoid accidentally spending inscribed sats (UTXO "coin control" became a consumer feature), which favored specialized wallets (Xverse, Unisat, Magic Eden) and MetaMask/Phantom Bitcoin support.
- **How Bitcoin wallets differ from EVM wallets:** UTXO selection versus account balances; PSBT-based multisig and air-gapped flows are mature; there is little arbitrary contract approval, so far less drainer surface. The main threats are seed theft, address poisoning and malware. Chainalysis noted bitcoin accounted for ~$900M of personal-wallet theft in H1 2025. Bitcoin's design challenge is fee and UTXO comprehension and Lightning liquidity, not signing comprehension.

### 10. Institutional and fintech convergence
- **ETFs moved much retail exposure back to custodial wrappers.** US spot Bitcoin ETFs (January 2024) held **$103.94B in total net assets on October 27, 2026, of which BlackRock's IBIT was $65.52B** (SoSoValue via TokenPost). Yahoo Finance shows IBIT at $67.06B, so figures differ slightly by source and timing.
- **Payments companies own the wallet stack:** Stripe (Bridge + Privy), Fireblocks (Dynamic), Paxos (Fordefi) and Coinbase (CDP, Base). The OCC allowed national trust banks to offer stablecoin custody and issuance (February 2026 final rule) and published its GENIUS Act framework. Banks preparing for stablecoins are being told to build wallet functions such as "key management, address whitelisting, and transaction-level controls" (Wolters Kluwer).
- **Policy-based permissions** are the institutional pattern now moving down to consumers: allowlists, velocity limits, multi-approver quorums, transaction-type rules and co-signing services (Fireblocks/Cobo-style policy engines; Safe modules and guards).
- **Compliance in self-custody:** Travel Rule handling for unhosted wallets, sanctions screening (OFAC/KYT) in wallet infrastructure, and issuer freeze functions mean "self-custody" of stablecoins is custody of a token whose issuer can still freeze it.

### 11. Agentic and AI-assisted wallets
**What shipped (2026):**

| Product | Date | Control model |
|---|---|---|
| Coinbase Agentic Wallets (CDP) | Feb 11, 2026 | TEE-isolated keys "never exposed to the agent's prompt or LLM"; session caps; per-transaction limits; KYT/OFAC screening; native x402 |
| Phantom MCP Server | Feb 18, 2026 | Agents (Claude etc.) sign/swap/transfer via MCP; preview status |
| Trust Wallet Agent Kit (TWAK) | Mar 26, 2026 | 25+ chains; dedicated agent wallet with pre-set rules, or WalletConnect "agent proposes, user approves" |
| MetaMask Agent Wallet | Early access Jun 2026; GA Aug 6, 2026 | Daily limits, protocol allowlists, "Guard Mode" (human approval outside rules) vs "Beast Mode"; mandatory simulation, Blockaid scanning, MEV protection |
| MetaMask Advanced Permissions (ERC-7715/7710) | 2025–26 | Standardized scoped grants, e.g., "10 USDC/day for 30 days," periodic/stream allowances, enforced on-chain by delegation caveats |

**Volume:** x402 (HTTP 402-based stablecoin micropayments) grew from about 1,500 cumulative transactions in mid-2025 to **more than 138M on Base by Q3 2026**, and 87% of payments fall between $0.0001 and $0.10 (Chainalysis, October 14, 2026). The x402 Foundation launched under the Linux Foundation on July 14, 2026 with 40 members, and AWS Bedrock AgentCore Payments added x402 in May 2026. *Caveat:* other trackers report different totals, and coverage notes that wash trading and self-dealing could distort volume.

**Incidents and research:**
- *Freysa (November 2024):* an adversarial game in which a human talked an agent into releasing 13.19 ETH (~$47K) after 482 attempts. This shows that LLM "judgment" is not a security boundary.
- *AIXBT (March 18, 2025):* 55.5 ETH taken after an attacker accessed the agent's dashboard. This was an operator-interface compromise, not model manipulation.
- *ElizaOS memory injection (Princeton/Sentient, arXiv:2503.16248):* fake "memories" planted via Discord carried across plugins and triggered transfers. The authors found "prompt-based defenses are not effective against this attack vector."
- *Grok/Bankrbot (May 4, 2026):* a Morse-code message relayed by Grok made Bankrbot send 3B DRB tokens (estimates range from $150K to $204K). MetaMask's security report called it "the first documented prompt injection attack against an AI agent with real financial capabilities." Accounts of how the permissions were enabled and whether funds were recovered disagree.

**Design implication:** The agent must never be the policy enforcer. Limits belong in on-chain caveats, TEE policy engines or smart-account modules, and the human should approve the *policy*, not each transaction. The new UX objects are permission grants (scope, amount, period, expiry, counterparties), a live dashboard of active delegations, and one-tap revoke.

### 12. Current state (2025–2026) and what comes next

**Comparison of wallet architectures**

| Architecture | Onboarding | Recovery | Signing / comprehension | Main security risk | Permissions model | Where it's winning |
|---|---|---|---|---|---|---|
| EOA + seed phrase (software) | Medium; seed ritual | Seed only; loss = total loss | Raw approvals; relies on simulation | Seed phishing, malware, extension supply chain | Per-tx approvals + token allowances | Power users, DeFi long tail |
| Hardware wallet | High friction, cost | Seed (+ optional services like Ledger Recover) | Strong *if* clear signing; blind-signing gap | Interface tampering, blind signing, supply chain, physical | Same as EOA | Long-term holders, signers in multisig |
| Multisig (Safe, PSBT) | High; coordination | Remaining signers rotate keys | Depends on UI integrity | UI compromise (Bybit), signer collusion | Thresholds, modules, guards | Treasuries, DAOs, funds |
| MPC/TSS | Low (consumer) to medium | Provider-assisted share refresh | Provider UI + policy engine | Provider dependence, liveness, opaque trust | Policy engines (institutional) | Institutions, exchanges, some consumer apps |
| Smart account (4337 / 7702) | Low with passkeys/paymasters | Guardians, key rotation, recovery modules | Batching can help or obscure | Malicious delegation/upgrade, module bugs | Session keys, ERC-7715 grants, spending limits | New consumer apps, upgraded EOAs |
| Embedded / WaaS | Lowest (email/social/passkey) | Email/OAuth + provider infra | Often app-controlled UI | Vendor concentration, export limits | App-defined policies | Fintech, games, payments, agents |

**Unresolved problems:**
1. **Recovery.** There is still no universally trusted, portable, non-custodial recovery. Options are seeds (fragile), guardians (social burden), cloud passkeys (platform dependence) and provider MPC (custody-adjacent).
2. **Signing comprehension.** ERC-7730 only works when *both* the wallet and the dApp support it. Typed data, batched calls, 7702 delegations and intents are each harder to explain than a transfer.
3. **Supply chain.** Bybit (developer machine to S3-hosted front end), Trust Wallet extension v2.68 ($8.5M, 2,520 wallets, after the Shai-Hulud npm worm exposed GitHub secrets and a Chrome Web Store API key) and Ledger Connect Kit show that auto-updating front ends and extensions are the new single points of failure.
4. **Cross-chain complexity.** Gas tokens, bridges and fragmented balances remain. Chain abstraction moves trust to solvers.
5. **Delegation sprawl.** Allowances, 7702 delegations, session keys and agent grants are piling up. Few wallets give a single, understandable "what can act on my behalf" view.

**Likely directions (forecasts, not facts):** EIP-7702 upgrade prompts become default in major EVM wallets. Native AA (EIP-8141 or similar) lands in Hegotá at the earliest, so not before 2027. Clear signing gets wider adoption as a requirement for wallet certification. Passkey-first smart accounts become the default for new users, while seeds remain an "advanced" export. Agent wallets become standard features with on-chain policy enforcement. Regulated stablecoin flows (from January 2027) push wallets toward payments UX and issuer-compliance awareness. Post-quantum signature migration is an emerging long-horizon driver for programmable validation.

---

## Recommendations (for a self-custody wallet product leader)

1. **Make "permissions" a first-class object, not a buried settings page.** Build one "Who can act for me" surface that unifies token allowances, NFT operator approvals, 7702 delegation status, session keys, ERC-7715 grants and agent policies, each with scope, limit, expiry and one-tap revoke.
2. **Treat the signing screen as your core product.** Default to simulation with balance-change previews. Support ERC-7730 clear signing end to end, including on hardware. Hard-block `eth_sign`-style blind payloads. Escalate friction for approvals, Permits, `setApprovalForAll`, implementation upgrades and 7702 authorizations, with interstitials whose severity scales with risk rather than a uniform warning that users click through.
3. **Own your 7702 upgrade path.** Offer smart-account upgrades only to audited, allowlisted implementations from inside the wallet, never at a dApp's request. Explain gains (batching, gasless, recovery) and risks plainly.
4. **Design recovery as a menu, not a ritual.** Offer passkey plus guardian or recovery module plus optional encrypted backup, with seed export available. Show the user which parties their recovery depends on.
5. **Harden the delivery pipeline as part of UX.** Use reproducible builds, staged extension rollouts, multi-party publishing keys and an "update verified" indicator. The Trust Wallet and Ledger Connect Kit incidents hit users who did everything right.
6. **Ship agent support with human approval of the policy.** Use per-agent sub-accounts or session keys, on-chain caps and allowlists, a Guard-Mode-style default, mandatory simulation that the agent cannot bypass, and visible audit trails. Never let model output be the only control.
7. **If you embed WaaS, plan for exit.** Make sure users can export keys or migrate the account, and evaluate vendor-concentration risk now that the major vendors belong to Stripe, Fireblocks and Consensys.
8. **For Bitcoin, design around UTXOs and liquidity.** Make coin control friendly for inscriptions, explain Lightning trust assumptions (LSP, Spark, Liquid) honestly, and show fees transparently.

---

## Caveats
- **Adoption metrics are soft.** MetaMask's 30M MAU dates from 2022 and is repeated in later coverage. Phantom's 15M is from January 2025. Trust Wallet's ~220M is cumulative and company-reported. No independent cross-wallet MAU dataset exists.
- **EIP-7702 counts conflict** (45M to 60M live; 214M to 250M cumulative) depending on date and tracker, and they are heavily padded by sweeper bots. Most figures reach this report through secondary write-ups of BundleBear rather than the dashboard itself.
- **Loss statistics measure different things.** Scam Sniffer tracks EVM drainer phishing only. Chainalysis's personal-wallet figure is a lower bound and its share changes by period (23.35% mid-2025 vs 20% full year). Scam totals ($17B estimated for 2025) are a separate category.
- **Agent-wallet incidents are poorly documented.** The Grok/Bankrbot loss ranges from $150K to $204K, its mechanism is disputed, and fund recovery is unconfirmed. Some 2026 agent incidents (e.g., a reported ~$500K "LLM router" drain) lack primary sources.
- **x402 volume** may include wash or self-dealing activity, and trackers differ (138M per Chainalysis; other trackers report more than 200M).
- **Timing of the OCC final rule:** sources date it to October 21 or October 23, 2026. Both agree on the January 18, 2027 effective date.
- **Native AA timing (EIP-8141 / Hegotá) and Glamsterdam (est. Q4 2026)** are roadmap targets, not commitments. EIP-8130 remains a live alternative.

---

## Synthesis: Major Inflection Points and Open Challenges

**Inflection points:**
1. **2012–2014, HD wallets and BIP39:** keys became a portable, human-recordable seed, creating the wallet market and the seed-phishing problem.
2. **2014, hardware isolation:** keys left the PC, and the trusted display became the real security boundary.
3. **2016–2018, MetaMask and WalletConnect:** the wallet became identity plus approval layer, and signing comprehension became the main UX problem.
4. **2022, FTX:** self-custody went from niche preference to mainstream argument.
5. **2023–2025, smart accounts (ERC-4337, then EIP-7702):** accounts became programmable without abandoning addresses, enabling gasless, batched, recoverable, permissioned UX.
6. **2024–2025, passkeys and WaaS consolidation:** seedless onboarding became commodity infrastructure owned by payments firms.
7. **2025, Bybit and supply-chain compromises:** the industry accepted that the interface, not the key, is the weakest link, which led to clear-signing standardization.
8. **2026, agentic wallets and x402:** wallets began serving non-human principals, making policy-based permissions the central design object.

**Open design and product challenges:** portable non-custodial recovery that ordinary users trust; readable signing for batched, delegated and intent-based transactions; a unified, revocable view of every delegation; supply-chain integrity for auto-updating wallet front ends; cross-chain UX without hidden solver trust; and agent permission models that humans can set once, understand later and revoke instantly. Teams that solve permission legibility, the step after signing comprehension, will define the next generation of self-custody.

---

## Sources

Citations from the research task. Three of the task's sources were left out because their addresses contain a personal name or social handle.

- [github](https://github.com/iotexproject/iotex-core/issues/5057)
- [moneycheck](https://moneycheck.com/coinbase-abandons-base-app-rebrand-returns-to-coinbase-wallet-name-after-failed-social-experiment)
- [coti](https://coti.io/blog/genius-act-final-rule/)
- [bravenewcoin](https://bravenewcoin.com/insights/coinbases-x402-records-138-5m-transactions-chainalysis-shows-ai-agents-reshaping-crypto-payments)
- [CoinDesk](https://www.coindesk.com/business/2026/05/13/crypto-wallet-provider-ledger-puts-u-s-ipo-plans-on-hold-due-to-market-conditions)
- [marketscreener](https://ca.marketscreener.com/news/ledger-targets-ipo-of-over-4bn-in-2026-ce7e5bdbd889f321)
- [maxavery](https://www.maxavery.org/blog/bybit-the-largest-theft-in-the-asset-class-and-the-signing-interface-behind-it/)
- [fireblocks](https://www.fireblocks.com/blog/bybit-attack-security-flaws-fireblocks-nation-state-resilient-solutions)
- [zerotracelabs](https://zerotracelabs.xyz/bybit-multisig-blind-signing-hack-a-1-5-billion-supply-chain-compromise-via-safe-wallet-frontend-manipulation/)
- [coinbureau](https://coinbureau.com/technology/what-is-walletconnect)
- [deepstrike](https://deepstrike.io/blog/crypto-wallet-drainer-statistics)
- [coincentral](https://coincentral.com/scam-sniffer-crypto-phishing-losses-fall-to-83m-in-2025/)
- [ledger](https://www.ledger.com/academy/topics/ledgersolutions/what-is-clear-signing)
- [ledger](https://www.ledger.com/academy/cryptos-greatest-weakness-blind-signing-explained)
- [cryptonomist](https://en.cryptonomist.ch/2026/05/13/ethereum-clear-signing-erc-7730/)
- [beincrypto](https://beincrypto.com/ethereum-foundation-launches-clear-signing-standard/)
- [scamsniffer](https://drops.scamsniffer.io/scam-sniffer-2025-crypto-phishing-losses-fall-83-to-84-million/)
- [scamsniffer](https://drops.scamsniffer.io/category/reports/)
- [Wikipedia](https://en.wikipedia.org/wiki/MetaMask)
- [coinlaw](https://coinlaw.io/metamask-vs-phantom-wallet-statistics/)
- [coinlaw](https://coinlaw.io/metamask-wallet-statistics/)
- [coinlaw](https://coinlaw.io/phantom-wallet-statistics/)
- [theblock](https://www.theblock.co/news/defi/2026-09-10-coinbase-rebrands-base-app-back-to-coinbase-wallet-after-just-over-a-year-as-social-experiment-falls-short-414115)
- [cryptobriefing](https://cryptobriefing.com/coinbase-rebrands-base-app-wallet/)
- [bitcoinfoundation](https://bitcoinfoundation.org/news/companies/coinbase-abandoned-wallet-rebrand-base-app/)
- [infosecurity-magazine](https://www.infosecurity-magazine.com/news/north-korea-steals-over-2bn-crypto/)
- [chainalysis](https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/)
- [chainalysis](https://www.chainalysis.com/blog/2025-crypto-crime-mid-year-update/)
- [crowdfundinsider](https://www.crowdfundinsider.com/2025/07/246173-chainalysis-examines-impact-of-crypto-crime-and-compliance-following-major-us-digital-assets-legislation-announcements/)
- [blofin](https://blofin.com/en/academy/education/bitcoin/best-lightning-wallet-types)
- [spark](https://www.spark.money/tools/lightning-wallet-comparison)
- [debevoise](https://www.debevoise.com/-/media/document/2026/10/payment-stablecoins-under-the-genius-act.pdf)
- [davispolk](https://www.davispolk.com/insights/client-update/occ-proposes-regulatory-framework-implement-genius-act)
- [hoge](https://hoge.gg/account-abstraction-goes-native-2026/)
- [turnkey](https://www.turnkey.com/blog/account-abstraction-erc-4337-eip-7702)
- [watswallet](https://watswallet.com/blog/eip-7702-native-account-abstraction)
- [spark](https://www.spark.money/research/ethereum-eip-7702-code-delegation-wallets)
- [hoge](https://hoge.gg/eip-7702-2026-how-wallet-delegation-works/)
- [hoge](https://hoge.gg/eip-7702-2026-complete-guide-smart-account-wallets/)
- [hoge](https://hoge.gg/eip-7702-wallets-exchanges-smart-accounts-2026/)
- [hoge](https://hoge.gg/eip-7702-smart-account-dark-side-2026/)
- [cybersecuritynews](https://cybersecuritynews.com/crypto-wallet-drainer-malicious-approvals/)
- [kucoin](https://www.kucoin.com/news/flash/2025-crypto-phishing-losses-drop-83-to-83-85m-drainer-ecosystem-remains-active)
- [ethereum](https://ethereum.org/latest/building-on-ethereum-in-2026/)
- [niteagent](https://niteagent.com/blog/eip-8141-frame-transactions-agent-guide-2026/)
- [ethdaily](https://ethdaily.io/glamsterdam-gas-repricings-breaking-changes)
- [relay](https://relay.link/blog/erc-7715-agentic-payments-crosschain)
- [tradingview](https://www.tradingview.com/news/cointelegraph:3f90403a9094b:0-how-the-fusaka-upgrade-fits-into-ethereum-s-long-term-roadmap/)
- [rango](https://rango.exchange/learn/market-trends/ethereum-fusaka-upgrade)
- [bloclabs](https://bloclabs.com/blog/privy-alternatives-2026)
- [markaicode](https://markaicode.com/web3/developer-tools/wallets-and-account-abstraction/)
- [upshift](https://www.upshift.finance/blog/wallet-as-a-service-providers)
- [atlas21](https://atlas21.com/guide-to-using-a-lightning-network-wallet/)
- [spark](https://www.spark.money/tools/bitcoin-white-label-wallet-comparison)
- [spark](https://www.spark.money/tools/which-bitcoin-lightning-wallet-should-i-use)
- [tokenpost](https://www.tokenpost.com/news/investing/42457)
- [Yahoo Finance](https://finance.yahoo.com/quote/IBIT/)
- [nixonpeabody](https://www.nixonpeabody.com/insights/alerts/2026/04/02/proposed-occ-regulations-for-payment-stablecoins-under-the-genius-act)
- [wolterskluwer](https://www.wolterskluwer.com/en/expert-insights/the-genius-act-in-2026-a-strategic-inflection-point-for-us-banks)
- [coinbase](https://www.coinbase.com/developer-platform/discover/launches/agentic-wallets)
- [coinbase](https://docs.cdp.coinbase.com/agentic-wallet/cli/welcome)
- [autheo](https://www.autheo.com/signals/coinbase-ai-agents-future-crypto-april-2026)
- [kucoin](https://www.kucoin.com/news/flash/phantom-launches-mcp-server-to-support-ai-autonomous-transaction-signing-and-token-transfers)
- [messari](https://messari.io/compare/trust-wallet-token-vs-phantom-wallet)
- [trustwallet](https://trustwallet.com/blog/company/introducing-the-trust-wallet-agent-kit-twak-your-ai-agent-can-now-act-on-crypto)
- [cryptobriefing](https://cryptobriefing.com/metamask-launches-ai-agent-wallet-for-automated-onchain-trading/)
- [bankless](https://www.bankless.com/read/news/metamask-launches-agent-wallets)
- [metamask](https://docs.metamask.io/smart-accounts-kit/guides/advanced-permissions/use-permissions/erc20-token/)
- [metamask](https://metamask.io/news/clawnch-ai-agent-launchpad-delegation)
- [metamask](https://metamask.io/news/introducing-advanced-permissions)
- [newscord](https://newscord.org/article/chainalysis-finds-ai-agents-made-138-million-x402-payments-on-coinbase-base--Story_20261014_AIagentsmake138milli81ca11e7)
- [coincentral](https://coincentral.com/ai-agents-gain-ground-as-x402-passes-138-million-transactions214628-2)
- [openfort](https://www.openfort.io/blog/x402-agentic-payments)
- [kucoin](https://www.kucoin.com/news/flash/138-million-on-chain-transactions-ai-agents-use-forgotten-402-code-for-autonomous-payments)
- [the-decoder](https://the-decoder.com/hacker-wins-47000-by-tricking-ai-chatbot-with-smart-prompting/)
- [makerchecker](https://www.makerchecker.ai/incidents/aid-2024-0003/)
- [makerchecker](https://www.makerchecker.ai/incidents/aid-2025-0007/)
- [blockonomi](https://blockonomi.com/ai-crypto-bot-aixbt-loses-106200-in-eth-through-dashboard-breach/)
- [gigazine](https://gigazine.net/gsc_news/en/20250514-web3-ai-agents-with-fake-memories/)
- [arxiv](https://arxiv.org/pdf/2503.16248)
- [metamask](https://metamask.io/news/crypto-security-report-may-2026)
- [mexc](https://www.mexc.com/news/1070204)
- [giskard](https://www.giskard.ai/knowledge/how-grok-got-prompt-injected-an-x-user-drained-150-000-from-an-ai-wallet)
- [phemex](https://phemex.com/news/article/ai-agent-prompt-injection-leads-to-cryptocurrency-theft-78776)
- [bestcadpapers](https://bestcadpapers.com/art-and-society/ai-agents-are-taking-on-more-keep-their-access-focused)
- [quillaudits](https://www.quillaudits.com/blog/web3-security/Agentic-Wallet-Security)
- [ledger](https://shop.ledger.com/pages/clear-signing)
- [thehackernews](https://thehackernews.com/2025/12/trust-wallet-chrome-extension-hack.html)
- [sqmagazine](https://sqmagazine.co.uk/phantom-wallet-statistics/)
- [libertify](https://www.libertify.com/interactive-library/chainalysis-crypto-crime-report/)
- [cornfordandcross](https://cornfordandcross.com/financial-technology/how-to-keep-ai-agent-delegation-from-becoming-a-security-problem)
- [ledger](https://www.ledger.com/academy/topics/agentic-ai/ai-agents-best-practices)
