# Investment-Grade Self-Custody: Industry & Opportunity Research for Product Design Strategy (US, September 2026)

> Source: the *Investment-Grade Self-Custody* doc in the "Secret" Claude project. Copied verbatim as the research baseline for everything else in this repo.

An investment-focused self-custody account has a real and widening opening in the US. Demand for a "deliberate slice" of crypto is now normal behavior: allocation guidance has settled at 1–5%, holder counts are rising, and brokerages have made buying crypto cheap and familiar. Meanwhile the leading self-custody wallets are turning into trading super-apps, and exchanges are wrapping DeFi yield inside custodial or semi-custodial experiences. Nobody yet owns the job of "allocate a sized, risk-rated slice of my wealth onchain, keep my keys, and never operate DeFi myself." Winning that job depends less on yield or token breadth than on four things: legible risk, recovery the user can trust, tax-grade records, and interaction models that keep the user as the decision-maker. That last point is a regulatory necessity as well as a UX preference.

## TL;DR

- **The market is ready, but the slot is narrow.** Estimates of US crypto ownership range from 22% (Motley Fool, May 2026) to "1 in 4 adults / 67 million" (NCA/Harris, spring 2026). BlackRock (1–2%) and Morgan Stanley (2–4%) have made "a small, rebalanced slice" the mainstream frame. Brokerages now sell bitcoin and ether at 50–75 bps, and spot ETFs such as IBIT (about $67B AUM) cover passive exposure. A self-custody product therefore cannot win on access or price. It has to win on onchain earning, ownership, and portfolio-grade control.
- **Regulation now permits the model but constrains the design.** The GENIUS Act bans issuer-paid stablecoin yield. The CLARITY Act failed cloture 49–50 on September 15, 2026, so market structure is being set by SEC/CFTC staff statements and proposals rather than statute. SEC staff relief for non-custodial "Covered User Interfaces" and Commissioner Peirce's July 2026 warning on curated vaults both point the same way: the product must not exercise discretion over user funds unless it registers. "Intent and allocation as the only decisions" must therefore be built as user-authored policy with disclosed, non-discretionary execution, not as a black-box robo-manager.
- **The design opportunity is trust infrastructure, not yield.** In 2025, 158,000 personal-wallet compromises hit 80,000 victims (Chainalysis). US crypto fraud complaints exceeded $11B in losses (FBI IC3). Only 43% of surveyed users could even identify a seed phrase (CHI 2025). Curated-vault failures such as Stream Finance's roughly $93M loss show that "curated" does not mean "safe." The highest-value, most defensible bets are: (1) risk-rated, explainable earning; (2) user-authored guardrails and policies; (3) recovery the user can actually rely on; (4) portfolio and tax-grade reporting; (5) human-in-the-loop automation.

---

## 1. Market Landscape and Size

### 1.1 Adoption among US investors

| Metric | Figure | Source / date | Confidence |
|---|---|---|---|
| US adults owning crypto | "1 in 4" / 67M+, up 12M year over year | NCA with The Harris Poll, 10,000 holders surveyed Feb 12–Mar 3, 2026 | Medium (industry-sponsored; extrapolated) |
| US adults owning crypto directly or via ETF | 22% (16% direct, 6% ETF only) | Motley Fool Money, Pollfish survey of 2,000 adults, May 8, 2026 | Medium |
| Holders planning to buy more | 90%; more than half of planned buyers expect to add up to $5,000 | NCA/Harris 2026 | Medium |
| Holders concerned about scams | 72% | NCA/Harris 2026 | Medium |
| Non-owners who "don't know how to buy" | 48%; 35% don't know what they'd do with it | Motley Fool 2026 | Medium |
| Never-owners who think crypto is a scam / cite security | 32% / 30% | Motley Fool 2026 | Medium |
| Primary reason to own | 57% cite investment | Motley Fool 2026 | Medium |

**Interpretation.** The ownership figures conflict: 22% versus about 25%. The gap is methodological (NCA extrapolates from a holders-only sample), and neither figure should be treated as precise. What matters for design is the direction and the mix. New holders skew toward women (42% of 2025–26 entrants versus 34% of earlier adopters, per NCA), toward age 55 and older (28% of recent buyers), and toward mainstream, non-technical backgrounds. This cohort brings brokerage mental models, not crypto-native ones. The main barriers for non-owners are know-how and trust, not access. Nearly half don't know how to buy, and about a third see crypto as a scam. These are design problems as much as marketing problems.

### 1.2 How investors think about a "slice"

The industry has converged on a small, rebalanced satellite allocation:

- **BlackRock Investment Institute** ("Sizing Bitcoin in Portfolios," sent to advisors June 23, 2026) recommends 1–2% bitcoin in a traditional multi-asset portfolio. Its reasoning: in a 60/40 portfolio a 1% position contributes about 2% of total portfolio risk, and beyond about 2% bitcoin's risk contribution "balloons." BlackRock compares a 2% position to the risk of holding one Magnificent Seven stock.
- **Morgan Stanley Global Investment Committee** (October 2025 special report) allows up to 2% for balanced growth, up to 3% for moderate growth and up to 4% for aggressive portfolios, with rebalancing "preferably quarterly or at least annually." The committee guides roughly 16,000 advisors overseeing about $2T.
- **Fidelity Institutional**, in "The case for bitcoin" (August 1, 2025), wrote that "portfolio allocations of 2%–5% (7.5% for young investors) could have an outsized positive impact in an optimistic adoption scenario."

**Design implication (inference).** A "deliberate slice" already has a mental model: a percentage of total net worth, sized by risk budget and kept in check by rebalancing. The product should use that vocabulary natively (target %, drift, rebalance bands, risk contribution) instead of token-first language. The largest institutional guidance frames sizing by risk contribution, not dollar amount. That argues for showing "this slice is X% of your risk" alongside "X% of your money," which would be a genuine differentiator, since no crypto wallet does this today.

### 1.3 ETF and spot-crypto product growth

- **Spot ETFs are the default passive vehicle.** BlackRock's IBIT held about $67.25B AUM on September 24, 2026, after a $166.3M daily inflow. Estimates earlier in 2026 put its share of US spot bitcoin ETF assets at about 49%.
- **Brokerages have entered spot crypto.** Schwab launched Schwab Crypto (BTC and ETH, custody via Paxos per trade press) in a phased rollout from mid-May 2026, priced at 75 bps per trade. Morgan Stanley began piloting spot BTC, ETH and SOL trading on E\*Trade on May 6, 2026, charging "50 basis points on the dollar value of each crypto transaction" with Zerohash as custodian (The Block, citing Bloomberg), and plans access for all 8.6M E\*Trade clients. Schwab says its clients already hold about 20% of spot crypto ETPs. Vanguard reversed course in December 2025 and now allows third-party BTC, ETH, XRP and SOL funds, while stating it has no plans for its own products.
- **Price volatility remains the context.** Bitcoin peaked at about $126,080 in October 2025, traded near $59,700 in late June 2026 (down more than 50%), and recovered to about $84,500 by late September 2026. Any "slice" product must be designed for 50% drawdowns as a normal event, not an edge case.

**Interpretation.** Brokerages and ETFs now cover "buy and hold BTC/ETH in a familiar account." Bloomberg's Eric Balchunas argued that the 75 bps spot fee makes ETFs the better deal for most Schwab clients. A self-custody product entering this space cannot compete on price for plain beta. Its value must lie in what ETFs and brokerage sleeves cannot do: direct ownership, onchain earning, stablecoin and RWA access, portability, and 24/7 programmability.

### 1.4 Tokenized assets / RWAs

- Estimates of tokenized RWA value, excluding stablecoins, **conflict widely.** Figures for May 2026 range from about $22–25B to $31–34B, and CoinGecko put market cap at about $19.3B at the end of Q1 2026. The spread comes from "distributed" versus "represented" value and from which categories are included. All sources agree on roughly 3–4x growth since early 2025.
- Tokenized US Treasuries and money market funds are the largest segment, at roughly $10–15B depending on source and date (about $12.9B in April 2026, per RWA.xyz via MetaMask). BlackRock's BUIDL exceeded $2.8B by July 2026.
- Tokenized equities are small but growing fast: about $1B in distributed value. Ondo Global Markets launched in early 2026 with more than 100 tokenized US stocks and ETFs. MetaMask now markets tokenized stocks, ETFs and commodities inside its wallet.

**Implication.** Tokenized Treasuries give self-custody users a regulated-feeling, lower-volatility "cash earning" sleeve at a moment when stablecoins themselves cannot pay yield. Many of these products carry issuer KYC, whitelisting and qualified-purchaser limits, so eligibility gating becomes a first-class UX pattern.

### 1.5 Stablecoins

- Total stablecoin market cap was about $305.1B on September 21, 2026 (DefiLlama), down from an all-time high of about $321.4B on April 18, 2026. Stablecoin supply is now roughly 3–4x total DeFi TVL. Stablecoins have become a payments and savings rail in their own right, not just DeFi collateral.
- New "wallet-branded" dollars are appearing. MetaMask's mUSD is issued through Bridge, a Stripe company, and backed 1:1 by dollars and short-term T-bills. Fidelity has launched the Fidelity Digital Dollar.

### 1.6 Onchain yield and earning products (September 2026 snapshot)

| Product | Mechanism | Headline rate | Custody |
|---|---|---|---|
| Coinbase USDC Rewards | Loyalty program funded from Coinbase's marketing budget (not lending) | 3.50% for Coinbase One members (as of Sept 15, 2026) | Custodial |
| Coinbase USDC Lending ("DeFi Earn") | Morpho vaults curated by Steakhouse on Base; Coinbase creates a smart-contract wallet for the user | Variable; launched at "up to 10.8%" with a temporary Morpho subsidy; "High Yield" vault added June 11, 2026 with Ethena-linked collateral | Hybrid: onchain vault via Coinbase app |
| MetaMask Money Account | Deposits convert to mUSD and route to a Steakhouse-curated vault on Monad (Veda infrastructure) lending on Morpho and Aave | "Up to ~6% APY" until Sept 30, 2026, then "up to 4%"; strategy targets 4% base | Self-custodial wallet |
| Direct DeFi lending (Fluid, Aave, Morpho vaults) | Overcollateralized lending | Fluid USDC about 5.19% on Ethereum (Sept 15, 2026, per DefiLlama via Eco) | Self-custody |
| Synthetic dollars (sUSDe) | Basis and funding-rate trade | About 5%, down from double digits earlier in 2026 | Self-custody |
| Tokenized Treasuries (BUIDL, OUSG, USDY) | T-bill funds | Tracks short-term rates, minus fees | Issuer-permissioned tokens |
| ETH staking | Protocol staking | Roughly 3% APR (early 2026) | Either |

Total DeFi TVL was about $93.9B on September 21, 2026 (DefiLlama), though one secondary source reported $71.8B in mid-June. This is another conflict driven by methodology and price. The key structural fact is that **curated vaults** (Morpho plus curators such as Steakhouse) have become the default "earn" engine behind both exchange and wallet front ends. Morpho reports $16B in deposits and $5.2B in outstanding loans across its network. Coinbase added fixed-rate BTC-backed loans through Morpho Midnight on September 22, 2026.

**Interpretation.** Retail "earn" has become a curation business sold through a trusted front end. That makes the curator and the front end, not the protocol, the new locus of trust. It also makes them the new locus of regulatory exposure (see §2) and failure risk (see §4).

---

## 2. Regulatory and Policy Environment

### 2.1 Current state (as of September 30, 2026)

| Area | Status | Key dates / facts |
|---|---|---|
| **Market structure (CLARITY Act, H.R. 3633)** | **Stalled.** Passed the House in 2025; Senate Banking advanced it 15–9 on May 14, 2026; a merged 616-page Senate text was released July 22. **Cloture on the motion to proceed failed 49–50 on Sept 15, 2026.** | Failure was driven by ethics provisions on officials' crypto holdings; stablecoin yield remained unresolved. The most plausible remaining window is the lame-duck session, and prediction markets priced 2026 passage in single digits after the vote. *Reporting of the tally differs (49–50 vs. 50–49); either way it fell 10+ votes short of 60.* |
| **Stablecoins (GENIUS Act)** | Enacted July 18, 2025; **implementing rules still pending**. Regulators missed the July 18, 2026 deadline for final rules. | Effective on the earlier of Jan 18, 2027 or 120 days after final regulations. OCC NPRM (Feb 2026) creates a rebuttable presumption that yield routed through affiliates or "related third parties" violates the yield ban. Treasury §3 NPRM (Aug 18, 2026; comments due Oct 19, 2026) exempts transactions via self-custody software/hardware wallets and direct peer-to-peer transfers. From July 18, 2028, US service providers may offer only permitted-issuer stablecoins. |
| **Stablecoin yield** | Issuers are **prohibited** from paying yield "solely for holding." Whether exchanges and platforms may pass reserve income to users (e.g., Coinbase USDC Rewards) remains contested. | More than 40 banking associations led by the ABA have lobbied to extend the ban to affiliates and exchanges. With CLARITY stalled, the answer rests on GENIUS rules and agency interpretation. |
| **SEC posture: staking** | Staff statements say protocol staking (May 29, 2025) and liquid staking (Aug 5, 2025) generally do not involve securities offerings, where the activity is "administrative or ministerial." | Joint SEC–CFTC interpretation (March 17, 2026; Release 33-11412) set out a crypto-asset taxonomy covering staking. Staff statements are non-binding and reversible. |
| **SEC posture: wallets and front ends** | Division of Trading and Markets staff statement (April 13, 2026): staff "will not object" to non-custodial **"Covered User Interfaces"** operating without broker-dealer registration if conditions are met. | Conditions (Latham counts 12; Hunton "over 20") include: no solicitation; user-customizable defaults; educational materials; disclosed default venues and routing; **no discretion**. Transaction-based fees are allowed; payment for order flow is prohibited. No relief for custodial wallets. The statement is deemed withdrawn after five years. |
| **SEC posture: vaults and curated lending** | Commissioner Peirce, "Headstands and Summervaults" (July 22, 2026): moving securities activity onchain "does not take those activities outside the scope" of securities laws. Vaults range "from programmatic allocations determined solely by immutable smart contracts, to allocations at the sole discretion of another person." | Curators and lending managers "setting interest rates, deciding which assets to accommodate, setting loan-to-value limits" should analyze investment-contract, investment-company, note (*Reves*) and investment-adviser exposure. This is a single Commissioner's view, not a rule. |
| **SEC rulemaking** | *Regulation Crypto Assets* **proposed** Aug 18, 2026 (Release 33-11434; comments due Oct 20, 2026): startup exemption up to $5M over four years, an investment-contract safe harbor, and a "qualified purchaser" definition. *Innovation Exemption* order (Sept 17, 2026; Release 34-106402) gives five-year conditional relief for tokenized-securities venues using permissioned AMMs. | The Innovation Exemption covers trading venues, not wallets, and gives no Investment Company Act relief for tokenized funds. |
| **Bank custody (OCC)** | OCC has confirmed national banks may offer crypto custody and ancillary services, including staking. | Enables bank-grade custodial competitors (e.g., Schwab via its bank entity). |
| **Tax (Form 1099-DA)** | Custodial brokers report gross proceeds for 2025 sales; **cost basis becomes mandatory for "covered" assets acquired on or after Jan 1, 2026**, held at the same broker (forms arrive early 2027). | **The DeFi broker rule was repealed via the Congressional Review Act on April 10, 2025.** Self-custody and DeFi activity generate no 1099-DA but remain fully taxable on Form 8949. Transferring assets breaks the basis chain: the receiving broker treats them as noncovered. |
| **KYC/AML, unhosted wallets, Travel Rule** | FinCEN's 2020 unhosted-wallet proposal (>$10K reporting, >$3K recordkeeping) was **withdrawn** (agenda listing April 2024). No re-proposal found. The separate 2020 proposal to lower the Travel Rule threshold to $250 had unconfirmed status as of this writing. | FinCEN/OFAC GENIUS AML NPRM (April 2026) treats permitted issuers as BSA financial institutions, requires sanctions programs and the ability to "block, freeze, and reject" transfers network-wide, but "barely mention[s] self-hosted wallets and impose[s] no additional requirements" (Ledger Insights). No direct obligations on wallet software. |

### 2.2 Design constraints these create (inference, grounded in the above)

1. **Non-discretion is the load-bearing constraint.** The Covered User Interface relief requires that the interface convert *user-chosen* transaction details into commands the user signs, with no discretion, no solicitation, and disclosed, customizable defaults. Peirce's statement suggests that whoever selects and reallocates yield strategies may be an adviser or be offering a security. Together these imply the product's allocation engine must either:
   - (a) execute **user-authored** policies deterministically, with every default disclosed and editable; or
   - (b) have its discretionary pieces (curation, auto-rebalancing into chosen strategies) provided by a **registered adviser** or a disclosed third-party curator the user explicitly selects.

   The positioning line "turns intent and allocation into the only decisions the user has to make" fits (a) well. It becomes legally risky if the product quietly makes those decisions for the user.
2. **Yield language and sourcing.** The product cannot present stablecoin holding as "interest." Earn features must name the source of return (borrower interest, staking rewards, T-bill fund income, incentives, subsidies), because the GENIUS yield ban and the OCC anti-evasion presumption turn on it. MetaMask's own disclaimer is the market benchmark: "not a bank account, savings account, or insured deposit product… could result in partial or total loss of funds."
3. **Promotional and teaser rates.** Both Coinbase (a Morpho subsidy) and MetaMask (6% until Sept 30, then 4%) have used temporary boosts. The design system should separate base yield from incentives and expiry dates in every rate display.
4. **Eligibility gating.** Tokenized funds (qualified-purchaser or KYC whitelists), perps and certain earn products vary by state and region. The product needs eligibility states, explanations of why an asset is unavailable, and state-level gating (e.g., Coinbase only recently resumed operations in Hawaii).
5. **Tax clarity is the user's burden, which makes it the product's opportunity.** Since no 1099-DA is issued for self-custody activity, the product that gives users tax-lot-grade records (basis, holding period, income events for staking and lending, and transfers that preserve basis) solves a problem the law has deliberately left to the user.
6. **Regulatory reversibility.** Almost everything enabling the model is staff guidance, a proposal, or a single-commissioner view, and a future SEC can reverse it. The architecture should let "earn" modules be switched off, re-gated or re-papered without breaking the account.

---

## 3. Competitive Landscape

### 3.1 Comparison table

| Category / examples | Target user | Value proposition | Custody | Earning offer | Onboarding | UX strengths | UX weaknesses | Trust & safety | Pricing (where known) |
|---|---|---|---|---|---|---|---|---|---|
| **(a) Exchange accounts & sleeves** — Coinbase (plus Base app / smart wallet), Robinhood Crypto, Kraken | Retail traders; crypto-curious | Broad assets, fast fiat on-ramp, "DeFi mullet" (CeFi front end, DeFi back end) | Custodial; Coinbase lending creates a user smart wallet routing to Morpho | USDC Rewards 3.5% (Coinbase One); Morpho lending vaults (standard and high-yield); staking; BTC-backed loans (variable, and fixed via Morpho Midnight) | Full KYC; card/bank funding in minutes | Familiar app; no gas, no bridges; consolidated view; 1099-DA provided | Counterparty and custody risk; opaque vault risk; yield mixes loyalty with lending; trading-first nudges | Regulated entity; 24/7 support; account recovery via identity | Retail trade fees often >1% (simple) and up to 0.60% (advanced); Coinbase One subscription |
| **(b) Brokerage crypto & ETFs** — Schwab Crypto, E\*Trade, Fidelity Crypto, Vanguard (third-party ETFs), IBIT and peers | Brokerage-native investors; advisors | Crypto "next to everything else," with education, support and tax reporting | Custodial (Schwab via Paxos); ETFs held by a fund custodian | None or minimal on spot; ETF options (covered calls) as a yield proxy; no DeFi | Existing account; near-zero friction | Portfolio context; trusted brand; advisor guidance; the allocation frame is native | BTC/ETH only at launch; no onchain utility or portability; no stablecoin earn | SIPC does not cover crypto directly, but brand trust is high; phone support | Schwab 75 bps per trade; E\*Trade 50 bps per transaction (Zerohash custody; pilot from May 6, 2026, per The Block citing Bloomberg); ETF expense ratios |
| **(c) Self-custody wallets** — MetaMask, Phantom, Trust, Rainbow, Rabby; smart/passkey wallets (Coinbase Smart Wallet / Base Account, Argent-style guardian wallets); MPC (Zengo, now owned by eToro) | Crypto-native to crypto-curious | Ownership, access to everything onchain | User-held keys (seed phrase, MPC shares, passkeys, guardians) | MetaMask: Money Account (mUSD vault, up to 6% then 4%), staking and lending via Earn, perps up to 50x, prediction markets, tokenized stocks, points/rewards | Download; seed backup or passkey; card/Apple Pay on-ramp | Breadth; composability; passkeys and 7702 upgrades remove gas and approval friction | Feature sprawl (trading, perps, points pull toward speculation); signing opacity; recovery burden; weak portfolio and tax views | Transaction simulation and scanning (MetaMask says its scanner blocked $191M in scams in 2025, per a Zengo marketing page); Transaction Shield; guardian recovery | Swap fee about 0.875% (MetaMask); conversion fees; network fees |
| **(d) DeFi front ends & aggregators** — Aave, Morpho, Fluid, Pendle, Yearn-style vaults, Ethena | Experienced DeFi users | Best rates; composable strategies | Self-custody | Lending, fixed-rate PTs, basis trades, looping | Wallet connect; no KYC (for permissionless use) | Transparency; rate choice; exit anytime (subject to liquidity) | Operator burden: chains, gas, approvals, liquidation math, curator due diligence | Audits; curator risk committees; but failures happen (e.g., Stream/xUSD) | Protocol and curator fees embedded in APY |
| **(e) Emerging hybrids** — curated-earn accounts (MetaMask Money Account, Coinbase DeFi Earn), tokenized funds (BUIDL, Ondo), agentic wallets (Coinbase Agentic Wallets, Feb 2026; MetaMask Agent Wallet, June 2026, "Guard Mode"/"Beast Mode") | Mainstream users wanting "one balance that earns"; developers building agents | Idle balance earns automatically; agents act within limits | Mixed: self-custody wallet plus third-party curated vaults; agent wallets use MPC/TEE with policy engines | Curated stablecoin yield; T-bill funds; automated strategies | One tap from existing wallet or app | "Nothing to claim, nothing to restake"; invisible DeFi | Risk hidden behind simplicity; a single curator is a concentration point; teaser rates; agent policies per wallet, not per portfolio | Curator risk committees; spending caps, allowlists, 2FA outside policy | Spread between vault APY and displayed rate; conversion fees |

### 3.2 What the map shows (inference)

- **Convergence from both sides.** Exchanges (Coinbase lending via Morpho) are moving toward onchain rails, and wallets (MetaMask Money Account, perps, tokenized stocks) are moving toward exchange-like breadth. Both are converging on the same Steakhouse/Morpho-style curated vault engine. The underlying yield is becoming a commodity. The *front-end experience of risk, control and reporting* is where products will differ.
- **MetaMask already uses the word "Account."** MetaMask Money Account shows that "self-custody + account" is a live positioning, but MetaMask frames it as a spending and earning balance inside a trading hub. No one frames it as an *investment* account with allocation targets, risk budgets and rebalancing. That is the white space.
- **Brokerages own the allocation mental model but not onchain utility.** Wallets own onchain utility but not the allocation mental model. The project's positioning sits exactly in that gap.

---

## 4. User Research and Behavioral Insight

### 4.1 What is publicly known

**Key management and recovery**
- In a Carnegie Mellon study at CHI 2025 (643 surveyed, 20 interviewed), only **43%** of crypto users could correctly identify a seed phrase from an image. Many believed a lost seed phrase could be "reset" like a password. *Fact; peer-reviewed.*
- Oobit's own survey page (1,000 US holders via CloudResearch Connect, 2026) reports: "Only 15% have tested their recovery process (restored a wallet or confirmed backups worked)." It also found 35% had lost access to a wallet or account, and 31% of those never recovered their funds. *Medium confidence; vendor survey.*
- A survey of more than 3,000 US crypto users found 66% consider self-custody important and 46% fear an exchange breach, yet 88% still keep assets on centralized exchanges and only 33% use a cold wallet (as reported by Crypto Daily, June 2026). *Low–medium confidence; original publisher unclear.* The **belief–behavior gap** is the core insight: users endorse self-custody but will not take on the responsibility at current UX cost.
- River Financial estimated in January 2025 that about 1.6M BTC has been lost to self-custody mismanagement. *Dated; estimate.*

**Scams, fraud and irreversibility**
- **FBI IC3 2025:** total reported cybercrime losses were $20.877B (+26%). Crypto-related complaints numbered 181,565, with more than $11B in losses (+22%). Crypto investment fraud alone was about $7.2B (complaints +48%). Recovery scams drew about 10,500 complaints and $1.4B in losses, including fraudsters impersonating IC3. Crypto ATM/kiosk complaints totaled 13,460 and $389M. Victims aged 60+ reported about $7.7B in total losses. *Fact; primary.*
- **Chainalysis (2026 Crypto Crime Report):** $3.4B was stolen in 2025. **Personal-wallet compromises reached 158,000 incidents across 80,000 victims**; total value fell to $713M, so attacks are more frequent and smaller. Violent "wrench attacks" exceeded $30M in H1 2026 across 46 incidents, on pace to beat 2025's $58M record, with leaked personal data a key driver. *Fact; primary.*
- Academic work confirms that EIP-7702 delegations are a phishing vector. Qi et al., "EIP-7702 Phishing Attack" (arXiv:2512.12174, December 2025), analyzed more than 150k events across 26k addresses and found authorizations "dominated by a small number of contract families linked to criminal activity." Coverage of the USENIX presentation (August 2026) reported 63% of sampled authorizations tied to malicious contracts and more than $2.3M in confirmed thefts. Wintermute had earlier (May 30, 2025) found more than 97% of delegations pointed to identical sweeper code. Separately, address-poisoning transactions rose 5.5x between November 2025 and January 2026. *The lesson: new account capabilities create new drainer surfaces.*

**Smart-contract and curator risk**
- **Stream Finance / xUSD (November 2025):** Stream disclosed that "an external fund manager… disclosed the loss of approximately $93 million," then suspended withdrawals. xUSD fell about 77%. Analyst YAM estimated that "$284.96 million in outstanding loans are secured by Stream's xUSD, xBTC, and xETH collateral." Curator vaults on Morpho, Euler, Silo and Compound were hit, led by TelosC ($123.64M), Elixir (about $68M) and MEV Capital (about $25M). Elixir wound down deUSD. *Only the $93M figure is company-disclosed; the rest are industry estimates.* **Lesson:** "curated" and "blue-chip protocol" did not protect users from a curator's collateral choices. Risk ratings must look through to the underlying collateral.

**Barriers for newcomers**
- 48% of non-owners don't know how to buy, 35% don't know what they'd do with crypto, 32% think it's a scam, and 30% cite security (Motley Fool 2026). Scam concern is high even among *holders* (72%, NCA).

**Tax**
- Self-custody and DeFi activity produce no 1099-DA, yet every swap, LP deposit and bridge is a reportable disposition, and first-year 1099-DA mismatches are common. *Fact, per multiple tax practitioners.* This is a known, recurring pain point, and support-ticket themes around basis reconstruction are widely reported by tax-software vendors.

### 4.2 Synthesized friction map (inference)

| Friction type | Where it bites | Evidence strength |
|---|---|---|
| **Control anxiety** ("if I lose it, it's gone") | Onboarding, backup, first large deposit | Strong (CHI 2025, belief–behavior gap) |
| **Signing opacity** ("what am I approving?") | Every transaction; approvals; 7702 delegations | Strong (Chainalysis wallet compromises; drainer patterns) |
| **Complexity wall** (chains, gas, bridges, approvals, liquidation) | Funding, earning, exiting | Strong (industry consensus; account-abstraction adoption driven by removing this) |
| **Risk illegibility** ("5% from what?") | Earn selection | Strong (Stream/xUSD; teaser rates; loyalty vs. lending confusion) |
| **Transparency gap** (no portfolio or tax view) | Monitoring, tax season | Medium–strong |
| **Recovery failure** | Device loss, death or incapacity, coercion | Strong on incidence; weak on public post-mortems |
| **Scam susceptibility** (social engineering, "recovery" scams, AI deepfakes) | Every trust moment, especially for 60+ users | Strong (FBI IC3) |

**Research gap.** Public data on *brokerage-native* investors' mental models of self-custody is thin; most surveys sample existing holders. This should be the priority for primary UXR.

---

## 5. Technology Enablers

| Enabler | What it changes for UX | Maturity (Sept 2026) | Key risks |
|---|---|---|---|
| **Smart accounts (ERC-4337) and EIP-7702** | Batching (approve + deposit in one step), sponsored gas, spending policies, programmable recovery; 7702 upgrades existing EOAs without changing address | **Production.** 7702 went live in Pectra on May 7, 2025. Around April 2026, roughly 62M active smart accounts and about 14M EOAs with 7702 authorizations were reported (via BundleBear/Dune aggregations; secondary). Supported by MetaMask, Rabby, Trust, Coinbase Base Account and Safe. | Persistent delegations are a phishing target; cross-chain delegation semantics; implementation bugs |
| **Passkeys** | Biometric sign-in; no seed phrase at creation; P-256 verification onchain | **Production.** Embedded-wallet infrastructure at scale: Privy (75M+ wallets, acquired by Stripe June 2025), Turnkey (50M+) | Passkeys handle authentication, not necessarily key custody. Platform-account (Apple/Google) dependency; recovery if the cloud account is lost |
| **MPC wallets** | Seedless; key shares spread across device, cloud and provider | **Production** (Zengo: about 2M users; acquired by eToro, April 2026) | Recovery depends on the provider; unclear legal characterization; share-holder availability |
| **Social / guardian recovery** | Trusted parties can rotate keys | **Production but niche** (Argent about 500K users) | Guardian collusion or unavailability; UX of choosing guardians |
| **Session keys and permissions (e.g., ERC-7715)** | Scoped, time-boxed, amount-capped authority for apps or agents | **Early production** | Policy misconfiguration; a clear UI for "what have I delegated?" is still immature |
| **Gas abstraction / paymasters** | Users never hold ETH; gasless USDC transfers (Circle) | **Production** | Sponsor economics; censorship or dependency on paymaster |
| **Chain abstraction / intents** | "I want X" → solver network finds the route; unified balances | **Early–mid** | Solver trust; MEV; failure and partial-fill states; weaker auditability |
| **Onchain risk scoring and curation** | Curator risk committees, transaction simulation, threat scanning | **Mid.** Curators are mainstream (Steakhouse behind Coinbase and MetaMask); scanners are widely deployed | Curator failure (Stream); ratings as implied endorsement; adviser-status questions (Peirce) |
| **Stablecoin rails** | Instant, 24/7 dollar settlement; card spend; regulated issuers under GENIUS | **Production; regulation in progress** | Yield ban; issuer freeze/block powers (a feature for AML, a risk for control-seekers); depegs |
| **AI / agentic assistants** | Agents execute within caps, allowlists and approval thresholds | **Early.** Coinbase Agentic Wallets (Feb 11, 2026; MPC/TEE, session caps); MetaMask Agent Wallet (early access June 8, 2026; Guard Mode with daily limits and 2FA outside policy) | Prompt injection is the leading attack class (e.g., the May 2026 Grok wallet incident); per-wallet policies do not add up to portfolio-level governance; regulatory status of agents that "decide" |

**Key takeaway (inference).** The stack needed for "keys without operating DeFi" now exists and is proven in production: smart accounts, passkeys, paymasters, curated vaults and policy engines. The remaining gaps sit mostly in the **human interface to that stack**: explaining delegations and policies, rating risk, reporting, and designing recovery. That favors a design-led entrant.

---

## 6. Opportunity Analysis

### 6.1 Ranked opportunities

Scores run High/Med/Low for user value (V), feasibility (F) and defensibility (D).

| Rank | Opportunity | V | F | D | Why |
|---|---|---|---|---|---|
| **1** | **Allocation-first account model** (set a target % of net worth or a fixed dollar slice; sleeves such as "BTC core," "ETH + staking," "dollar earn," "tokenized T-bills"; drift bands; user-approved rebalances) | H | H | M–H | Matches the dominant institutional mental model (BlackRock, Morgan Stanley). No wallet offers it. Stays non-discretionary if the user authors targets and approves or pre-authorizes rebalances |
| **2** | **Risk-rated, explainable earning** (look-through risk labels covering source of yield, collateral, curator, liquidity/exit time, contract age/audits, and incentive vs. base rate; "what would have happened" stress views) | H | M | H | Directly answers the Stream/xUSD lesson and the teaser-rate problem. A proprietary rating methodology and a data moat compound over time. Must be framed as information, not a recommendation, to avoid adviser drift |
| **3** | **Guardrail and policy authoring** (spend limits, allowlisted protocols, max % per venue, withdrawal delays for large exits, trusted-address books, "never allow unlimited approvals") | H | H | M–H | Smart accounts and session keys make it enforceable onchain. Converts control anxiety into a sense of control. The same primitives later govern agents |
| **4** | **Recovery the user can trust** (layered: passkey + guardian/institutional co-signer + time-locked recovery; *tested* recovery drills; inheritance/beneficiary flows; duress and coercion features such as delayed large withdrawals) | H | M | H | Only about 15% test recovery; wrench attacks are rising; inheritance is unsolved for mainstream users. Hard to copy because trust builds over time |
| **5** | **Portfolio and tax-grade reporting** (cost basis per lot across wallets; income events for staking and lending; realized/unrealized P&L; 8949-ready export; brokerage-style statements; "import your ETF/brokerage slice" to show the whole allocation) | H | M | M | Self-custody gets no 1099-DA. For brokerage-native users this is table stakes and absent in wallets |
| **6** | **Progressive trust / graduated autonomy** (start with small limits and curated defaults; unlock capabilities by demonstrated understanding, time and backups completed) | M–H | H | M | Reduces irreversible early mistakes; creates a relationship arc; can double as an eligibility and suitability record |
| **7** | **Human-in-the-loop automation and agents** (the assistant proposes rebalances, harvests or migrations with a plain-language rationale; executes only inside user-set policy; auto-pauses on anomalies) | M–H | M | M | Differentiates while the market is early. Risks: prompt injection and regulatory "discretion." Sequence after #3 |
| **8** | **Safe exit and off-ramp design** (one-tap "unwind this sleeve to USD," with an up-front exit-time estimate by liquidity) | M | M | L–M | Exit is the least-designed moment across competitors; liquidity-dependent withdrawals are a real risk |
| **9** | **Scam-resistant signing** (simulation in plain English, human-readable intents, cooling-off periods for new payees, "someone told you to do this?" interrupts) | H | H | L–M | High value, but MetaMask and others ship scanners; differentiation comes from framing, not tech |

### 6.2 The "self-custody" vs. "account" tension

- **What "account" implies to a brokerage-native user:** a regulated custodian, SIPC/FDIC-style protection, someone to call who can reverse errors, statements, tax forms and password reset. Most of that is untrue for a self-custody product. MetaMask has to disclaim that its Money Account "is not a bank account… or insured deposit product."
- **What "self-custody" implies:** sole responsibility, irreversibility, no one to call. That is exactly the fear stopping 88% of surveyed users from acting on their stated preference.
- **Resolution (recommendation).** Keep "account" but redefine it in the product through what users can see and do. An account means statements, allocations, a recovery plan, and support that can *guide but not reverse*. Say plainly, early and repeatedly: "You own the keys. We can't move, freeze or recover your funds, and here is how *you* recover them." Test candidate framings in research ("self-custody investment account," "your onchain portfolio account," "owner-controlled account"). There is a legal dimension too: avoid implying custody, insurance or advice. Counsel should review "account" nomenclature against broker-dealer and bank-like marketing rules.
- **Hidden trap.** If the product uses institutional co-signers, guardians or recovery providers, it moves along the custody spectrum. That can be good for trust and bad for the pure self-custody claim. The UI should show the *custody topology* clearly: who holds which key or share, and what each party can and cannot do.

### 6.3 Key risks and open questions

1. **Regulatory reversal.** Staff statements (staking, Covered User Interfaces) and Peirce's views can change under a future Commission. With CLARITY stalled, there is no statutory floor.
2. **Adviser / investment-company characterization** of curated allocation and auto-rebalancing. *Open question:* does the product register as, or partner with, an RIA for managed sleeves?
3. **Stablecoin yield rules.** Final GENIUS rules, and any lame-duck CLARITY revival, could restrict pass-through rewards, forcing earning toward tokenized T-bill funds or protocol lending.
4. **Curator and protocol concentration.** Coinbase and MetaMask both lean on Steakhouse/Morpho-style stacks, so a single failure would be correlated across the market.
5. **Economics.** Brokerages price spot at 50–75 bps, and ETFs are cheaper for passive exposure. *Open question:* can revenue come from earn spread, subscription or reporting without misaligned incentives (e.g., pushing higher-risk vaults)?
6. **Recovery liability.** If a recovery partner fails or is coerced, who bears responsibility?
7. **Chain choice.** Monad (MetaMask), Base (Coinbase) and Ethereum each fragment liquidity. Chain abstraction is still maturing.
8. **Data sensitivity.** Portfolio aggregation creates a honeypot. Wrench attacks were linked to leaked personal data, including a tax-software breach (Waltio, about 50,000 users).
9. **Market cyclicality.** Drawdowns above 50% will test "deliberate slice" discipline and retention.

---

## 7. Design Strategy Implications

### 7.1 Candidate design principles (each resolves a real tension)

1. **"You decide; we execute exactly."** *(Automation vs. control / non-discretion.)* Every automated action traces to a user-authored rule, with the rule visible at the moment of execution.
2. **"Name the source of every dollar of return."** *(Simplicity vs. risk legibility.)* No bare APY: every rate breaks into base, incentives, expiry and source.
3. **"Recovery before funding."** *(Fast onboarding vs. irreversibility.)* No meaningful balance until a recovery path has been set up *and rehearsed*. Small balances can move fast; large ones earn trust first.
4. **"Show the custody map."** *(Self-custody vs. account.)* Always make clear who holds which key, and what we can and cannot do.
5. **"Portfolio first, token second."** *(Crypto-native breadth vs. investor mental model.)* The home screen shows allocation vs. target and risk contribution, not a token list.
6. **"Friction where it is irreversible, speed where it is not."** *(Safety vs. convenience.)* Use cooling-off periods for new payees and large exits; let routine rebalances within policy stay one tap.
7. **"Plain language, precise detail on demand."** *(Novice vs. expert.)* Progressive disclosure: expert users can inspect calldata, curator parameters and liquidation thresholds; novices never have to.
8. **"Designed for the drawdown."** *(Growth marketing vs. investor wellbeing.)* No gamified trading or points loops; rebalancing and "stay the course" framing during volatility.

### 7.2 Highest-trust moments in the journey

| Stage | Trust moment | Design must-haves |
|---|---|---|
| **Discover** | "Is this legit, and is it for me?" | Custody explainer; comparison with ETFs and brokerage (and honesty about when an ETF is better); regulatory status in plain language |
| **Onboard** | Key creation and recovery setup | Passkey-first; layered recovery chosen with explained trade-offs; a recovery drill; scam-education moment (IC3 patterns) |
| **Fund** | First fiat-to-onchain transfer | Exact fees; arrival time; which chain and why (or abstracted, with an audit trail); address-poisoning defense |
| **Allocate** | Setting the slice and the sleeves | Target-% tool linked to net worth; risk-contribution view; a user-signed policy summary ("investment policy statement") |
| **Earn** | Choosing a risk tier | Look-through risk card; base vs. boosted rate; exit-time estimate; curator identity; "what could go wrong" examples |
| **Monitor** | Drawdowns, rate changes, curator events | Drift alerts; incident banners with clear required actions; statements; tax-lot view |
| **Exit / Recover** | Withdrawal, device loss, death, coercion | Unwind preview with liquidity timing; time-locked recovery; beneficiary flow; duress delays |

### 7.3 Design system considerations

- **Transaction states.** Draft → Simulated → Awaiting signature → Submitted → Pending (with chain and solver status) → Confirmed → Final, plus Partially filled, Failed (reason + retry), Reverted and Delayed by policy (with countdown and cancel option). Every state shows fees paid, what changed in the portfolio, and a link to the policy rule that authorized it.
- **Risk indicators.** A multi-dimensional risk badge (smart contract, collateral/credit, liquidity/exit, counterparty/issuer, depeg, regulatory) rather than a single score. Use tier labels plus drill-down, avoid green "safe" semantics, and include a "last reviewed" timestamp and an incident history.
- **Asset display.** Group by sleeve rather than by chain. Show the wrapper chain (e.g., USDC → vault share → underlying loans), nominal vs. real value for staked or receipt tokens, and eligibility badges (KYC required, region-limited). Include cost basis and unrealized P&L per lot.
- **Policy components.** Rule builder (limits, allowlists, max allocation per venue, approval thresholds); a delegation inventory ("what can act on my behalf": session keys, agents, 7702 delegations) with one-tap revoke; policy diff views when a rule changes; human-readable policy summaries the user signs.
- **Disclosure patterns.** Standard "not a bank account / not insured / may lose principal" modules; yield-source disclosures; conflicts disclosures (e.g., who is paid when you choose a vault); default-routing disclosures matching the Covered User Interface conditions.
- **Recovery components.** A recovery health meter; guardian management; drill scheduler; inheritance setup.

### 7.4 Hypotheses to test in follow-up research

1. Brokerage-native investors will fund a self-custody account more readily when the home screen shows allocation vs. target and risk contribution than when it shows a token list.
2. A rehearsed recovery drill during onboarding raises willingness to deposit more than $1,000 more than it lowers onboarding completion.
3. Showing yield broken into source, base, incentive and exit time lowers choice of the highest-APY option and raises trust scores without lowering deposit rates.
4. Users prefer to *author* a simple policy ("keep crypto at 5%, rebalance at ±2%, ask me first above $X") over accepting a managed default. This matters for the non-discretion model.
5. A "custody map" visual reduces the false belief that the company can reverse transactions, without reducing sign-up.
6. The word "account" creates insurance/SIPC expectations that must be actively corrected; alternative framings keep appeal while lowering misbeliefs.
7. Crypto-native users will trade some yield for guardrails (e.g., a max % per curator, withdrawal delays) if the guardrails are user-configurable.
8. Human-in-the-loop agent proposals ("here's why I suggest rebalancing") are trusted more than fully automated execution for amounts above a personal threshold, and that threshold varies predictably by experience level.
9. Cooling-off delays on new payees and large exits are acceptable to most users and are seen as protective, especially by users aged 55+.

**Recruiting criteria (suggested mix, n≈24–36 for qualitative work, followed by a quantitative survey):**

| Segment | Screener definition | Share |
|---|---|---|
| **Brokerage-native, crypto-new** | Self-directed brokerage account with $25K+ investable; no crypto, or ETF-only exposure; considering an allocation | ~35% |
| **Crypto-curious mainstream** | Owns crypto only on an exchange or brokerage (Coinbase, Robinhood, Schwab); has never used a self-custody wallet; holds $1K–$50K | ~30% |
| **Self-custody intermediate** | Has used a self-custody wallet for more than 6 months; has done a swap or staked; limited DeFi | ~20% |
| **Experienced DeFi** | Regularly uses lending/vaults; has managed approvals, bridges or liquidations; ideally has experienced a loss or incident | ~15% |

Quotas: at least 25% aged 55+ (reflecting the recent-buyer mix and scam exposure); at least 40% women (reflecting 2025–26 entrants); spread across incomes. Include people who *tried and abandoned* self-custody, and people who have lost funds to a scam or lost keys (handled with care). Exclude crypto-industry employees.

---

## Caveats

- **Conflicting data flagged:** US ownership (22% vs. 25%); RWA market size ($19B–$34B, methodology-dependent); DeFi TVL ($72B in June vs. $94B in September, plausibly price-driven); CLARITY vote tally reporting (49–50 vs. 50–49).
- **Lower-confidence sources:** figures on the self-custody belief–behavior gap, recovery testing, 7702 phishing share and smart-account counts come from vendor blogs or secondary aggregators and should be verified before external use. NCA is an industry advocacy group.
- **Dated items:** Morgan Stanley guidance is from October 2025. Seed-loss estimates (River) are from January 2025. The SEC staking statements are from 2025 but remain current.
- **Forward-looking items are not facts:** GENIUS effective dates depend on final rules that have not been issued. Regulation Crypto Assets is a proposal (comments due Oct 20, 2026). Lame-duck CLARITY revival is speculative. Promotional APYs (MetaMask's 6% through Sept 30, 2026) expire, and rates change daily.
- **Not legal advice:** the regulatory design constraints above are research-based inferences. Securities, adviser, money-transmission and state-law questions (especially around curated allocation and the "account" label) require counsel.
