# Competitive Analysis — Self-Custody Investment Account

As of September 30, 2026 · Live doc: https://claude.ai/code/artifact/e227448a-bbfb-459f-af30-10f78d7991f5

## Bottom line

The slot is open, but narrower than the market research suggests: the "self-custody wallet plus curated earn" half of the positioning shipped in 2026, and only the "allocation as the decision" half is still unclaimed.

1. **Earn inside self-custody is no longer white space.** [Robinhood Earn](https://robinhood.com/us/en/support/articles/crypto-earn/) (USDG via Morpho, curated by Steakhouse, held in a self-custody wallet), [MetaMask Money Account](https://metamask.io/news/introducing-metamask-money-account) and [Kraken Wallet DeFi Earn](https://blog.kraken.com/product/kraken-wallet/self-custody-with-defi-earn) (Sept 16, 2026) all ship it. Coinbase does the hybrid version. The underlying engine is the same everywhere, so it cannot be the differentiator.
2. **Allocation-first is unclaimed.** None of the nine competitors scored below puts target percentage, drift and risk contribution at the centre of a self-custody product. Schwab and E\*Trade own that mental model, but they are custodial and sell only a handful of spot coins.
3. **Robinhood is the closest threat, not MetaMask.** It has the brokerage-native audience, a self-custody wallet, an earn product, its own chain and AI-agent accounts. It could add an allocation view faster than a new entrant can build distribution.

This is based on public product pages and press releases, not hands-on testing. "No one ships X" means I found no evidence of X, and each such claim should be checked in the product before it is used externally.

## Positioning under test

The statement makes five separable claims, and each competitor is scored on each one rather than on overall similarity.

> For self-directed US investors who want a deliberate slice of their wealth in digital assets and onchain earning, [project] is a self-custody investment account that keeps them in control of their keys without making them a DeFi operator. Unlike exchange sleeves or raw DeFi front ends, it turns intent and allocation into the only decisions the user has to make.

| # | Claim | What a competitor must ship to match it |
|---|---|---|
| C1 | **Deliberate slice** | Home screen built around a target share of net worth, drift and rebalancing, not a token list |
| C2 | **Keys stay with the user** | User-held keys (seed, passkey, MPC or multisig) and no provider that can move funds |
| C3 | **Not a DeFi operator** | No chains, gas, bridges or approvals to manage; earn is one action |
| C4 | **Onchain earning, legibly** | Yield with named source, base vs incentive, and risk shown beyond a bare APY |
| C5 | **Intent and allocation are the only decisions** | User-authored policy executed deterministically, including automated rebalancing inside limits |

The target user is a US, self-directed investor who already holds a brokerage account, so US availability and brokerage-style records count as part of C1 and C4.

## Competitive set

The set has six groups, ordered roughly by how close each sits to the target user's current alternatives, with the competing job named for each.

| Group | Players scored | The job they compete for | Why included |
|---|---|---|---|
| **Brokerage crypto and ETFs** | Schwab Crypto, E\*Trade, spot ETFs (IBIT) | "Put crypto next to my stocks and bonds" | Where the target user already is; owns the allocation mental model |
| **Exchange sleeves and hybrids** | Coinbase (Earn, Base account) | "Buy, hold and earn on crypto in one familiar app" | Largest US crypto brand; moving onchain via Morpho |
| **Wallet-first challengers** | Robinhood Wallet and Earn, Kraken Wallet | "Self-custody from a brand I already trust" | Brokerage or exchange audiences with self-custody plus earn |
| **Self-custody wallets** | MetaMask, Phantom | "Own everything onchain, and spend it" | Largest wallet user bases; now adding earn and accounts |
| **Investor-grade custody** | Casa | "Protect a large holding from loss, theft and death" | Only product built around recovery and inheritance for serious holders |
| **DeFi front ends and stacks** | Aave, Morpho vaults, Rabby, Safe, Ledger | "Best rate, full control" | The raw alternative the positioning defines itself against |

Bitcoin ETFs are included as an indirect competitor, because for passive exposure they beat any self-custody product on price and simplicity. Ledger, Safe and Rabby are scored from the earlier market research and general product knowledge, not fresh page reads, so they carry lower confidence.

## Claim-by-claim scorecard

No competitor fully meets more than one of the five claims, and none fully meets C1, C4 or C5. Scores: Yes = shipped and verified on a public page; Partial = shipped in part or in a different form; No = no evidence found.

| Competitor | C1 Slice | C2 Keys | C3 No DeFi ops | C4 Legible earn | C5 Intent only | Deciding evidence |
|---|---|---|---|---|---|---|
| [Robinhood Wallet + Earn](https://robinhood.com/us/en/support/articles/crypto-earn/) | No | Yes | Partial | Partial | No | Keys held by user; USDG-only lending via Morpho, curated by Steakhouse; blocked in New York and Texas |
| [Coinbase](https://www.coinbase.com/blog/earn-competitive-yields-by-lending-your-usdc) | No | Partial | Yes | Partial | No | Per-user smart wallet on Base; Core and High Yield vaults; "not savings accounts" disclosure |
| [Schwab Crypto / E\*Trade](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Charles-Schwab-Announces-Plans-to-Expand-Digital-Assets-Available-in-Schwab-Crypto-Accounts/default.aspx) | Partial | No | Yes | No | No | Crypto beside stocks in one view; custodial (Paxos sub-custody); no staking or stablecoins at launch |
| [MetaMask Money Account](https://metamask.io/news/introducing-metamask-money-account) | No | Yes | Partial | Partial | Partial | Names yield sources and curator; teaser 6% ends Sept 30; agent wallet has spending limits per wallet |
| [Kraken Wallet](https://blog.kraken.com/product/kraken-wallet/self-custody-with-defi-earn) | No | Yes | Partial | Partial | No | Vaults inside the wallet; generic risk warning; rates and US availability not stated |
| [Phantom](https://www.bankless.com/read/news/phantom-wallet-rolls-out-cash-stablecoin-platform) | No | Yes | Partial | No | No | CASH stablecoin, cards and accounts; yield on CASH only announced as planned (Oct 2025 source) |
| [Casa](https://casa.io/standard) | No | Yes | Partial | No | No | $250/year, 3-key vault, Casa holds one key, inheritance; no earn found on its page |
| Direct DeFi stack (Aave, Morpho, Rabby, Safe) | No | Yes | No | Partial | No | Transparent rates but user carries chains, approvals and curator diligence |
| Spot bitcoin ETFs (IBIT) | Partial | No | Yes | No | No | Sits inside the brokerage allocation frame; no onchain use |

The pattern is a split: everyone with custody control (C2) lacks the investor frame (C1), and everyone with the investor frame lacks control. The positioning sits on the one combination that nobody has assembled. The MetaMask C5 score reflects agent limits reported in the earlier research, not a user-authored allocation policy.

## Competitor teardowns

Ordered by threat to the positioning, highest first. Each entry ends with the gap that would have to close for the competitor to reach the same ground.

### Robinhood Wallet and Earn: highest threat

Robinhood already sells the combination of a brokerage-native audience and a self-custody earn product. [Robinhood Earn](https://robinhood.com/us/en/support/articles/crypto-earn/) lends USDG through a Morpho vault curated by Steakhouse, and states that Robinhood "does not hold your assets, does not control your private keys." It discloses variable rates that can drop to zero, depeg and smart-contract risk, and limited insurance that excludes lending losses. [CoinDesk](https://www.coindesk.com/business/2026/07/01/robinhood-rolls-out-public-blockchain-as-it-expands-deeper-into-crypto) reports an estimated 7% APY, Robinhood Chain (Arbitrum L2) live since July 2026, and Agentic Accounts for eligible US users.

*Gap to close:* an allocation-first home screen, more than one earn product (USDG only, blocked in New York and Texas), and policy-based automation. All are product decisions Robinhood can make quickly.

### Coinbase: strongest distribution, hybrid custody

Coinbase [creates a per-user smart contract wallet on Base](https://www.coinbase.com/blog/earn-competitive-yields-by-lending-your-usdc) that connects to Morpho vaults curated by Steakhouse, in a Core USDC vault (BTC and ETH collateral) and a High Yield vault (dynamic collateral including Ethena assets). It adds that these are "not savings accounts" and not FDIC or SIPC insured. [Forbes](https://www.forbes.com/sites/digital-assets/2026/08/13/schwab-switched-on-crypto-for-40-million-accounts-and-priced-it-like-an-index-fund/) puts Coinbase's take rate at 175 bps, against 75 bps at Schwab.

*Gap to close:* the account is only partly self-custodial, so it cannot make the "you hold the keys" claim cleanly, and its rewards and lending products blur two different sources of yield.

### Schwab Crypto and E\*Trade: own the mental model, lack the rails

Schwab [switched on spot bitcoin and ether on May 13, 2026](https://www.forbes.com/sites/digital-assets/2026/08/13/schwab-switched-on-crypto-for-40-million-accounts-and-priced-it-like-an-index-fund/) for about 39.8M accounts at 75 bps, with its own bank and Paxos as sub-custodian. Its clients already held roughly $25B in crypto ETPs. It [plans to add SOL, AVAX and LINK](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Charles-Schwab-Announces-Plans-to-Expand-Digital-Assets-Available-in-Schwab-Crypto-Accounts/default.aspx). Forbes reports E\*Trade followed in July at 50 bps. The launch left out staking, stablecoins and coin withdrawals.

*Gap to close:* custody model and onchain utility. Both are close to the opposite of what a brokerage wants to operate, so this threat is about demand capture, not feature parity.

### MetaMask Money Account: same engine, wrong frame

Deposits convert to mUSD and route to a Monad vault "curated by Steakhouse and built using Veda's infrastructure," lending on Morpho and Aave, with no lockups, no opening fee and no minimum. [MetaMask names three yield sources](https://metamask.io/news/introducing-metamask-money-account) (borrower interest, partner rewards, MetaMask Rewards). The promotional "up to 6% APY" ends September 30, 2026, and drops to "up to 4%" after. Availability varies by region.

*Gap to close:* MetaMask frames the account as a spending and earning balance inside a trading hub. An investor frame would mean rebuilding the home screen around allocation, against its own trading-first design.

### Kraken Wallet: fast follower

The [September 16, 2026 update](https://blog.kraken.com/product/kraken-wallet/self-custody-with-defi-earn) adds curated vaults inside the self-custody wallet, including those offered on Kraken Exchange. The post gives no rates and no US statement, and carries only a generic list of technology, market and operational risks.

*Gap to close:* everything beyond the earn list, and its risk disclosure is the weakest of the group.

### Phantom: payments-first

Phantom launched a [CASH stablecoin with cards and virtual accounts](https://www.bankless.com/read/news/phantom-wallet-rolls-out-cash-stablecoin-platform) built on Solana and Stripe, and said yield on idle CASH was planned. The source is from October 2025, so current status is unverified. Its direction is spending, not investing.

*Gap to close:* a different product direction, so low near-term threat to this positioning.

### Casa: the recovery benchmark

[Casa Standard](https://casa.io/standard) costs $250 a year for a 3-key vault, where Casa holds one key as an emergency backup and provides guided key replacement and inheritance. It supports BTC, ETH, USDT and USDC. Its page mentions no earning or portfolio reporting.

*Gap to close:* earning and allocation. Casa is the reference point for what "recovery the user can trust" means, and it shows that serious holders will pay a subscription for it.

### Direct DeFi stack (Aave, Morpho vaults, Rabby, Safe)

This is the alternative the positioning defines itself against. It offers the most transparent rates and full control, but leaves chains, approvals, liquidation maths and curator diligence with the user. The Stream Finance failure (about $93M) showed that curated vaults are not safe by default.

*Gap to close:* it does not try to close the gap; it is the audience's fallback for users who outgrow simplicity.

## Adjacent solutions

None of the six adjacent groups meets the full positioning, but each holds one piece of it and shows what users already pay for or accept. Scores use the same C1 to C5 claims and the same Yes, Partial, No scale.

| Group | Examples opened | C1 Slice | C2 Keys | C3 No DeFi ops | C4 Legible earn | C5 Intent only | What it teaches |
|---|---|---|---|---|---|---|---|
| **Wealth platforms and robo-advisors** | [Wealthfront](https://www.wealthfront.com/blog/cryptocurrency-exposure-at-wealthfront/) | Yes | No | Yes | No | Partial | Crypto is capped at 10% of a portfolio (IBIT and ETHA only) with tax-aware rebalancing; the adviser runs the discretion |
| **Tokenized treasury platforms** | [BUIDL, OUSG, USDY, BENJI](https://eco.com/support/en/articles/15254019-how-to-buy-tokenized-t-bills-2026-routes-for-institutions-and-retail) | No | Partial | Partial | Yes | No | Clearest yield source (T-bills), but gated: BUIDL $5M minimum, OUSG $5K qualified purchasers, USDY non-US only, BENJI US retail from $20 |
| **Fintech stablecoin yield** | [PayPal PYUSD Rewards](https://eco.com/support/en/articles/15276699-pyusd-rewards-2026-how-the-yield-actually-works) | No | No | Yes | Partial | No | About 4%, paid by PayPal as a "loyalty offering"; custody stays with PayPal; OCC March 2026 proposal questions this structure |
| **Portfolio and tax tools** | [CoinTracking, Koinly, CoinLedger, CoinTracker, Awaken](https://coinbureau.com/services/crypto-tax-software) | No | n/a | n/a | Partial | No | Reporting exists but is bolted on: basis breaks on transfers and DeFi needs manual review; $49 entry, $259 to $1,999 a year at 10,000 transactions |
| **Onchain asset managers (curated vaults)** | [Curators such as Gauntlet and Steakhouse](https://defiprime.com/defi-vaults-guide) | No | Yes | Partial | Partial | No | Curators set market limits within timelocks (1 to 7 days), guardians and hard caps, and charge 5% to 15% of yield; they cannot move funds outside those limits |
| **Bitcoin-only investor products** | [Unchained](https://www.unchained.com/compare/unchained-vs-strike) | Partial | Yes | Partial | No | No | 2-of-3 multisig (client holds two keys), Traditional, Roth and SEP IRAs with a bank custodian, $250 a year per vault, up to $6,000 a year for white-glove |

Five lessons follow from the table.

1. **The slice has proven demand, but only in wrappers.** Wealthfront's 10% cap and automated rebalancing show that investors accept a bounded crypto sleeve, and only in ETF form. No adjacent player offers it with keys or onchain earning.
2. **Serious holders pay for safety.** Unchained charges $250 to $6,000 a year and Casa $250, for recovery, multisig and retirement wrappers. This supports a subscription model over one priced on spreads or pushed yield.
3. **Curated vaults already contain the guardrail patterns.** Timelocks, guardians and hard-coded limits are the onchain precedent for user-authored policy and for delay windows on large changes. Reuse them and move the authorship from the curator to the user.
4. **Reporting is a partner or build decision.** Third-party tools cover tax, but all break on transfers and DeFi. A native, basis-aware record is a gap, and an integration with one of these tools is a cheaper first step.
5. **Eligibility gating is a design problem.** Treasury funds range from $20 to $5M minimums and exclude whole groups of users, and PayPal's rewards exclude New York. The product needs clear states for "not available to you, and why."

Partly unverified: Wealthfront's page describes changes from 2024, and Betterment, Altruist, Cash App, Revolut, Zerion, Yearn, Sommelier, Enzyme, River and Strike turned up in searches but were not opened.

## White space and defensibility

The defensible ground is the trust layer around earning, not earning itself: the parts that need data, licences or time cannot be copied by shipping a screen. Ease of copying is my inference from what each capability requires.

| Capability | Closest today | Ease for incumbents to copy | Why |
|---|---|---|---|
| Allocation-first home (target %, drift, risk contribution) | Schwab shows crypto beside stocks, but custodial | **Easy** as a screen; **hard** with real net-worth data | The screen is a redesign; the value needs holdings from outside the wallet |
| Look-through risk rating (yield source, collateral, curator, exit time) | Steakhouse risk committee behind MetaMask, Coinbase and Robinhood vaults | **Hard** | Needs a methodology, ongoing data and a stance on adviser status; rating a curator's own vaults is a conflict |
| User-authored policy and guardrails | MetaMask agent wallet limits, per wallet | **Medium** | Smart-account primitives exist; portfolio-level policy is the missing layer |
| Recovery that is rehearsed and inheritable | Casa (3-key, inheritance, $250/year) | **Hard** | Trust accrues over time; seed-phrase wallets would have to change their core model |
| Tax-grade records across wallets and brokerage | Not found in the products reviewed | **Medium** | Solved by third-party tools; the gap is having it native and basis-aware |

Three observations follow.

1. **Yield is a commodity.** Coinbase, MetaMask, Robinhood and Kraken all lean on Steakhouse and Morpho, so rates converge and a single curator failure would hit all of them at once. Legible risk is worth more than a higher number.
2. **The two frames are complementary, not exclusive.** Casa proves people pay for recovery; Schwab proves people want allocation in one view. No one combines them with onchain earning.
3. **Speed is the real moat.** Every capability above is copyable by a well-funded incumbent within a year or two. The advantage lasts only as long as the design gets trust-critical moments right first.

## Threats and ways to lose

The positioning fails mainly by being out-distributed or out-priced, not out-featured.

1. **Robinhood adds the investor frame.** It already has earn, self-custody and an audience of brokerage users. If it adds allocation targets, the product's main difference narrows to recovery and risk depth.
2. **The ETF is simply better for most people.** Schwab charges 75 bps and E\*Trade 50 bps for spot coins, and ETFs cost less again, so a plain slice of bitcoin does not justify self-custody. The product must say so, and win only where onchain earning, ownership or portability matter.
3. **Rate compression makes yield unimpressive.** MetaMask's headline falls from 6% to 4% on October 1, 2026, and Robinhood cites about 7% on one stablecoin. A product that competes on APY loses to whichever incumbent subsidises hardest that quarter.
4. **Shared curator failure.** Four competitors rely on the same Steakhouse and Morpho stack. A single failure would damage trust in the whole category, including a product that rates risk well.
5. **Regulatory reversal.** The non-discretion model rests on staff relief and proposals that a future SEC can withdraw, and final stablecoin rules are still pending. Each competitor carries this risk too, but a new entrant has less room to absorb it.
6. **Distribution.** Schwab has about 39.8M accounts and Coinbase a large installed base. A new product starts at zero and must rely on trust and word of mouth in a narrow segment.
7. **The word "account" sets insurance expectations.** Competitors use hedged names ("Money Account" with a not-a-bank disclaimer), and a stronger investment framing raises the risk of implying protection the product cannot offer.

## Implications for design strategy

Differentiate on the parts of the positioning nobody ships (C1, C4, C5 and recovery) and reach parity, quickly, on everything competitors already do well.

| Decision | Where | Design implication |
|---|---|---|
| **Differentiate** | Allocation-first home (C1) | Home shows share of net worth against target, drift and risk contribution; token list is secondary. Include an import of the brokerage or ETF slice so the whole allocation is visible |
| **Differentiate** | Legible earn (C4) | Every rate splits into base, incentive, expiry and source, with the curator named and a look-through risk card. Competitors show a bare "up to X%" |
| **Differentiate** | Policy as the decision (C5) | User writes a plain-language policy (target, bands, ask-first threshold) that is signed and shown at the moment each action runs |
| **Differentiate** | Rehearsed recovery | Recovery drill before a meaningful balance; use Casa as the benchmark for guided key replacement and inheritance |
| **Parity** | Earn in one action | Users compare against Robinhood, Coinbase and MetaMask; setup must be no harder than theirs |
| **Parity** | Eligibility and disclosure | Explain state and product limits (Robinhood blocks New York and Texas; Coinbase excludes New York) and use standard not-a-bank wording |
| **Concede** | Passive spot exposure | Say when an ETF is the better tool; do not compete on price for plain bitcoin |

### What to test next

- **Framing.** Does "account" raise insurance expectations, and does a custody map correct them without lowering sign-up?
- **Home screen.** Do brokerage-native users fund more when they see allocation against target than when they see tokens?
- **Rate display.** Does showing base, incentive and exit time lower the pull of the highest headline rate?
- **Policy authoring.** Do users prefer to write their own policy over accepting a managed default?

### Evidence still needed before this is decision-grade

- Hands-on teardowns of Robinhood Wallet and MetaMask Money Account, including their home screens and recovery flows.
- Confirmation of Coinbase's current rewards rate (sources conflict; see Sources).
- Fresh reads of Ledger, Safe and Rabby, scored here from earlier research.
- Current status of Phantom's CASH yield and whether Kraken's DeFi Earn is available in the US.

## Sources, confidence and gaps

Pages opened for this analysis, as of September 30, 2026. Market, regulatory and user-research figures come from [the market research](01-market-and-opportunity-research.md).

- [Robinhood Earn support page](https://robinhood.com/us/en/support/articles/crypto-earn/): USDG lending, Morpho and Steakhouse, custody statement, risks, state exclusions.
- [CoinDesk on Robinhood Chain](https://www.coindesk.com/business/2026/07/01/robinhood-rolls-out-public-blockchain-as-it-expands-deeper-into-crypto): chain launch, Stock Tokens, Agentic Accounts, estimated 7% APY.
- [Coinbase USDC lending post](https://www.coinbase.com/blog/earn-competitive-yields-by-lending-your-usdc): smart wallet on Base, vaults, disclosures.
- [MetaMask Money Account](https://metamask.io/news/introducing-metamask-money-account): vault design, yield sources, promotional rate, fees.
- [Kraken Wallet DeFi Earn](https://blog.kraken.com/product/kraken-wallet/self-custody-with-defi-earn): September 16, 2026 update.
- [Schwab press release](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Charles-Schwab-Announces-Plans-to-Expand-Digital-Assets-Available-in-Schwab-Crypto-Accounts/default.aspx) and [Forbes on the Schwab launch](https://www.forbes.com/sites/digital-assets/2026/08/13/schwab-switched-on-crypto-for-40-million-accounts-and-priced-it-like-an-index-fund/): fees, custody, reach, omissions, E\*Trade.
- [Casa Standard](https://casa.io/standard): price, keys, recovery, inheritance.
- [Bankless on Phantom CASH](https://www.bankless.com/read/news/phantom-wallet-rolls-out-cash-stablecoin-platform): stablecoin and accounts (October 2025).

Adjacent solutions, pages opened:

- [Wealthfront on crypto exposure](https://www.wealthfront.com/blog/cryptocurrency-exposure-at-wealthfront/): IBIT and ETHA, 10% cap, rebalancing.
- [How to buy tokenized T-bills in 2026](https://eco.com/support/en/articles/15254019-how-to-buy-tokenized-t-bills-2026-routes-for-institutions-and-retail): eligibility tiers and minimums (secondary source).
- [PYUSD rewards, how the yield works](https://eco.com/support/en/articles/15276699-pyusd-rewards-2026-how-the-yield-actually-works): rate, funding, custody, OCC proposal (secondary source).
- [Best crypto tax software 2026](https://coinbureau.com/services/crypto-tax-software): tool comparison and limits.
- [Complete guide to DeFi vaults](https://defiprime.com/defi-vaults-guide): curator roles, timelocks, fees.
- [Unchained vs Strike](https://www.unchained.com/compare/unchained-vs-strike): multisig, IRAs, pricing (vendor page).

**Confidence.** High for what each page states about its own product. Medium for the "No" scores, which mean no evidence found on public pages, not a tested absence. Lower for Ledger, Safe and Rabby, whose search results were not opened, and for ease-of-copying estimates, which are judgement.

**Conflicts to resolve.** The Coinbase post cites USDC rewards of 4.1% APY (4.5% with Coinbase One), while the market research records 3.5% as of September 15, 2026, so the post may be dated. The market research dates the E\*Trade pilot to May 6, while Forbes says it followed Schwab in July. The Robinhood Chain article's own US availability for Stock Tokens is unclear.
