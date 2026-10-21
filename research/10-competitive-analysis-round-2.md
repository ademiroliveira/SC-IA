# Competitive Analysis, Round 2 — Self-Custody Investment Account

As of October 20, 2026 · Author: AO · Live doc: https://claude.ai/code/artifact/271cac5b-ef84-45be-b25a-c0ffa60a24f6 · Builds on [round 1](02-competitive-analysis.md) (September 30, 2026)

Round 2 is desk research from public sources: vendor and help pages, terms, regulator documents, filings, press, industry reports, review sites, app stores and YouTube descriptions. No product was used hands-on, and Reddit and Bogleheads threads could not be read. Each finding carries a source-type tag, such as [Help doc] or [Press], so secondhand evidence does not read like testing. Every finding that changes a score or the bottom line was checked against its source on October 20.

Vocabulary follows the current terms: the user **defines** a **plan**, made of **rules**; **guardrails** are spending and exit limits.

## Bottom line

Five things changed since round 1. The open ground is now US self-custody only, and the window to claim it is shorter.

1. **Allocation inside self-custody now exists, though not yet in the US.** Glider runs a target allocation with scheduled rebalancing from a smart account the user owns [Help doc], and Bitwise's Automated Token Portfolios run on it for eligible non-US users [Press]. In the US I found no self-custody product that does this. Coinbase Advisor brings goal-and-risk portfolios to custodial accounts, in beta [Vendor]. Round 1's "allocation-first is unclaimed" now holds only for US self-custody.
2. **The incumbents are answering "intent is the only decision" with AI agents, not plans.** Robinhood Agents and Loops (coming soon), Coinbase for Agents (live, with trade caps still "coming soon") and MetaMask Agent Wallet all let a model act inside a sandbox, and Robinhood puts all the risk on the user [Vendor]. That makes "your rules, executed exactly" a sharper claim, and makes agents the likeliest substitute.
3. **Headline yields are largely targets and subsidies.** In early September, Robinhood's 7% was 3.86% native yield plus 3.24% in Merkl top-ups, shown as one number [Vendor, partner]. In July, the median consumer earn vault realized 3.4%, below the 3-month T-bill at 3.82% [Report]. No competitor shows cost or realized yield next to the rate, so C4 is more open than round 1 said.
4. **Protection is now a marketed claim, and the positioning says nothing about it.** Coinbase One lists coverage from $1,000 to $250,000 by tier with no stated scope, MetaMask offers up to $10,000 a month for eligible transactions, and Kraken up to $100,000 per depositor on one vault [Vendor] [Help doc].
5. **Nobody rehearses recovery.** Investor-grade products check keys on a schedule, while mainstream wallets fall back on Apple, Google or a seed phrase and cannot help if that fails [Help doc]. Delays on large exits exist only in investor-grade products. Recovery and protected exits are still the hardest gap to copy.

One finding cuts against demand. Gallup found that crypto ownership among US investors with $10,000 or more fell from 17% to 11% between 2025 and June 2026 [Report]. Other surveys disagree, so the primary-user interviews matter more, not less.

## What changed since round 1

Ten round 1 statements are now out of date, corrected or resolved.

| Round 1 said | Round 2 found | Effect |
| --- | --- | --- |
| Allocation-first is unclaimed | Glider and Bitwise ship it outside the US; Coinbase Advisor (custodial, beta) builds goal-based portfolios | Open in US self-custody only; less time to claim it |
| Robinhood Earn sits in Robinhood Wallet | Earn lives in the main Robinhood app on an embedded wallet whose keys sit with Privy; Robinhood cannot restore access | Robinhood's C3 rises; brokerage-native self-custody earn is already one tap away |
| Kraken has the weakest disclosure; US status unknown | DeFi Earn runs in Kraken's main app, in most of the US, with per-vault risks and liquidity, a named curator and optional coverage | Kraken now has the strongest C4 in the set |
| Coinbase USDC rewards: 3.5% or 4.1% (conflict) | 3.75% APY, for Coinbase One members only (from $4.99 a month) | Conflict resolved; the yield is a paid perk |
| MetaMask: 6% promo, Morpho and Aave | Up to 4% variable; Morpho only at launch, Aave later; one curator | Scores unchanged |
| Four competitors rely on Steakhouse | Curators now include Sentora, Gauntlet and Chaos Labs, but the top three hold about 76% of tracked curated TVL; collateral is concentrated too | Threat 4 reframed: shared curator and shared collateral |
| Coinbase "Base account" | Base App was renamed Coinbase Wallet on September 10: a self-custodial trading hub with perps, tokenized stocks and copy trading | The opposite of an investor product |
| E\*Trade launch date conflict | Pilot began May 6, wider rollout later in 2026 | Resolved |
| Unchained Signature costs $6,000 a year | $6,000 in the first year, then $4,500 | Corrected |
| Stream Finance lost about $93M | Later estimates are larger (about $160M frozen to about $285M in related bad debt, by source); claims opened in June 2026, with no recoveries yet | Strengthens the case for the risk card |

## Scorecard, rescored

No competitor fully meets C1, and the only C5 scores above No are Partial. C5 now reads "a user-defined plan executed exactly". A product scores **No** on C5 when a model decides inside a sandbox, and **Partial** when rules the user set (caps, allowlists) are enforced by the system.

| Competitor | C1 Slice | C2 Keys | C3 No DeFi ops | C4 Legible earn | C5 Plan executed exactly | Change and deciding evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Robinhood (Earn in the main app) | No | Yes\* | **Yes** (provisional) | Partial | No | C3 up from Partial: earn is one action in the brokerage app, on an embedded wallet [Help doc]. C4: one blended estimate, no fee shown. Agents are model-driven and still coming soon |
| Coinbase (exchange, lending, Advisor, Agents) | **Partial** | Partial | Yes | Partial | No | C1 up from No: Advisor builds goal-and-risk portfolios that include USDC lending, but it is custodial, advice only and in beta for select users [Vendor]. C4: the Earn page shows only "up to 7.14%" with no tiers, risks or fee. Agent caps are not live |
| Coinbase Wallet (new row) | No | Yes | Partial | No | No | Self-custodial trading hub [Press]; its USDC rewards are a Coinbase-paid perk, not onchain earning |
| Kraken DeFi Earn (main app; replaces "Kraken Wallet") | No | Yes\* | **Yes** (provisional) | Partial, strongest | No | US availability confirmed; per-vault risks and liquidity shown before deposit; Sentora named; optional coverage; fee percentage unstated; key provider for the embedded wallet not disclosed [Help doc] |
| MetaMask Money Account | No | Yes\* | Partial | Partial | Partial | Unchanged. Up to 4% with fees unstated, one curator [Vendor]. The Money Account cannot be exported or funded from a hardware wallet [Help doc]. C5 rests on Agent Wallet caps and allowlists, set per agent |
| Glider and Bitwise ATPs (new row; non-US) | Partial | Partial | Yes (provisional) | No | Partial | Target allocation plus scheduled rebalancing, run by a session key limited to what the user authorized [Help doc]. No net-worth slice, drift bands or guardrails found; US availability unverified |
| Brokerage crypto (Schwab, E\*Trade, Fidelity) | Partial | No | Yes | No | No | Fidelity added: 1% per trade, crypto beside brokerage and IRA accounts [Help doc] |
| Spot and staking ETFs | Partial | No | Yes | No (spot) / Partial (staking) | No | Staking ether ETFs now pay monthly income, with the provider's cut disclosed in filings [Filing] [Press] |
| Phantom | No | Yes | Partial | No | No | Unchanged; no rate published for CASH yield |
| Casa | No | Yes | Partial | No | No | Unchanged; still the recovery benchmark |
| Bitkey (new row) | No | Yes | Partial | No | No | Bitcoin only; the strongest delays and recovery in a consumer product [Help doc] |
| Direct DeFi stack (Aave, Morpho, Ledger, Rabby, Safe) | No | Yes | No | Partial | No | Ledger confidence raised: Ledger Wallet now offers Morpho vaults and borrowing, with every approval clear-signed on the device [Vendor] |

\*Yes, with a caveat: the user holds the keys, but recovery depends on a login or cloud account, and the provider cannot help if that fails.

**The pattern.** Round 1's split still holds in the US: products where users hold the keys lack the investor frame, and products with the frame are custodial. Two things erode it. Glider shows the frame can be built into self-custody. And C2 alone no longer differentiates, because every embedded wallet now makes the same promise. What differs is what the provider can still do for the user when something goes wrong.

**Also checked, lower threat or not in the US.** Trust Wallet Earn (excludes the US), Uniswap Earn (Gauntlet vaults; US not stated), Tether's wallet (no earn), Exodus Pay (spending and rewards), Jupiter Wallet Auto-Earn (a single sweep rule), Zerion (an agent tool for developers), Nunchuk and Ready (limits and guardian recovery), Kubera (a net-worth tracker that covers wallets and brokerages, with no targets), and Parrot (a US adviser app offering Bitwise crypto models).

## Category matrix, revised

Eight core categories and one adjacent now compete for the target user, up from round 1's six, and none reaches Yes on both the slice (C1) and keys (C2). The three new categories all come at that gap from different sides: advice from custody, agents through a model's judgment, and automated portfolios from self-custody outside the US.

Each cell shows the best score any product in the category reaches, so a row is the category's frontier, not its typical product. **By custody** means the provider solves it by holding the assets; **—** means not applicable. C5′ replaces C5, and C6 to C9 are the candidate claims under New claims.

| Category and players | Job they compete for | C1 Slice | C2 Keys | C3 No ops | C4 Legible earn | C5′ Rules, exactly | C6 Cost seen | C7 Protected exits | C8 Proven recovery | C9 Records |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Brokerage crypto and ETFs** · Schwab, E\*Trade, Fidelity, spot and staking ETFs | "Put crypto next to my stocks, and earn on it with a tax form" | Partial | No | Yes | Partial | No | Partial | By custody | By custody | Partial |
| **Advice and model portfolios** (new) · Coinbase Advisor, Wealthfront, Betterment, Parrot, Robinhood Strategies | "Tell me what to hold, and keep it on target" | Yes | No | Yes | No | Partial | Partial | By custody | By custody | Partial |
| **Exchange apps with embedded self-custody earn** (merged) · Robinhood Earn, Coinbase lending, Kraken DeFi Earn | "Earn on my dollars in the app I already use" | No | Yes | Yes | Partial | No | Partial | No | No | No |
| **AI agents acting inside limits** (new) · Robinhood Agents, Coinbase for Agents, MetaMask Agent Wallet | "Act for me, within limits I set" | No | Yes | Partial | No | Partial | No | Partial | No | No |
| **Automated portfolios in self-custody, outside the US** (new) · Glider, Bitwise ATPs | "Keep my onchain portfolio on target automatically" | Partial | Partial | Yes | No | Partial | No | No | No | No |
| **Self-custody wallets** · MetaMask Money Account, Phantom, Coinbase Wallet, Trust Wallet Earn (outside the US), Uniswap | "Own everything onchain, and trade or spend it" | No | Yes | Partial | Partial | No | No | No | No | No |
| **Investor-grade custody** · Casa, Bitkey, Unchained, Nunchuk | "Protect a large holding from loss, theft and death" | No | Yes | Partial | No | Partial | No | Yes | Partial | No |
| **DeFi front ends and stacks** · Aave, Morpho vaults, Ledger Wallet, Rabby, Safe | "Best rate, full control" | No | Yes | No | Partial | No | Partial | Partial | No | No |
| **Tracking and tax tools** (adjacent) · Kubera, CoinTracker, Koinly | "See it all in one place, and file my taxes" | Partial | — | — | — | No | — | — | No | Partial |
| **SC-IA, as positioned** (target, not shipped) | "Hold a sized slice in my own keys, under my rules" | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

**Reading down the columns.** C5′, C6, C8 and C9 never rise above Partial in any category, and C7 reaches Yes only in investor-grade custody, mostly for bitcoin. The custodial categories answer protected exits and recovery by holding the assets, which is the answer self-custody gives up.

**What changed from round 1's six groups.**

- **Merged.** "Integrated onchain offerings" and "wallet-first challengers" become one category, because Robinhood, Coinbase and Kraken all now put self-custody earn inside the main app, on an embedded or smart wallet.
- **New.** Advice and model portfolios, AI agents acting inside limits, and automated portfolios in self-custody. Tracking and tax tools move up from adjacent, because they come closest to C1 and C9 outside custody.
- **Moved.** Coinbase Wallet (formerly Base App) joins self-custody wallets; its direction is trading. MetaMask's Agent Wallet is counted under agents, which is where the scorecard's Partial on C5 for MetaMask comes from.
- **Expanded.** Brokerage adds Fidelity and staking ether ETFs; investor-grade custody adds Bitkey, Unchained and Nunchuk.
- **Rescored.** Unchained drops from Partial to No on C1: an IRA wrapper sits inside a retirement allocation but shows no target, drift or rebalancing.
- **Watch.** Registered advisers self-custodying client crypto, if the SEC's October 1 custody proposal is adopted. Round 1's tokenized treasury and fintech stablecoin yield groups stay adjacent; reward models like PayPal's face the new stablecoin rules.

## The trust layer, by lens

None of the four main competitors meets L1 (cost beside return), offers one-tap revoke (L2), or rehearses recovery (L4); the best answers on friction and recovery come from investor-grade products.

| Lens | Robinhood | Coinbase | MetaMask | Kraken | Best in the market |
| --- | --- | --- | --- | --- | --- |
| **L1** Cost beside return | No: one blended estimate | No: fee share undisclosed; USDC rewards need a subscription | No: rate is net of fees it never states | Partial: APY is net of fees and coverage, but the fee percentage is unstated | Nobody |
| **L2** Permissions and revoke | No in-app revoke | Coinbase Wallet: revoke on the web, paid in gas | Revoke on three chains, paid in gas | Not found | Nobody offers one-tap revoke |
| **L3** Friction where irreversible | Agent approvals on by default; no delays | Coinbase Vault has a 48-hour withdrawal window that can be cancelled | Agent caps, and 2FA when a limit is exceeded; no delays | None found | Bitkey (daily limit, 7-day recovery delay with alerts), Safe, Nunchuk, Casa's emergency lockdown |
| **L4** Recovery | Login-based; Robinhood cannot restore access | Passkey, or a phrase that must be set up in advance | Phrase, or social login plus password | Phrase, cloud backup or social login; a known iOS restore bug | Casa and Unchained check keys every six months; nobody rehearses a restore |
| **L5** Curator choice | Steakhouse only | Steakhouse only | Steakhouse only | Several vaults; one curator named on the help page | Kraken, in part |
| **L6** Drawdown behaviour | Perps, social posts of P&L, 24/7 trading | Coinbase Wallet: perps, copy trading | Trading hub, card cashback | Not assessed | Nobody reminds users of their own plan |

Naming (L7) and eligibility (L8) have their own section below.

## New claims

Five candidate claims could sharpen the positioning, and seven competitor claims need a stance; no competitor fully owns any of the five, though bitcoin-only products hold parts of two and MetaMask part of one.

### Candidate claims for the positioning

| # | Candidate | Evidence | Who owns it today | Recommendation |
| --- | --- | --- | --- | --- |
| C5′ | **Your rules, executed exactly, not a model's judgment** | Robinhood and Coinbase route intent through AI agents and disclaim the result; MetaMask's limits are set per agent; counsel commentary sees rules-based vaults as lower adviser risk [Vendor] [Report] | Nobody; MetaMask in part, for agents | Rewrite C5 this way. Make the plan the contract any agent must obey, so agents become a channel rather than a substitute |
| C6 | **Cost and realized yield you can see** | About half of Robinhood's 7% is subsidy; the median vault realized less than a T-bill; curator fees run from 0% to 25% of interest; no product shows all-in cost or compares itself with an ETF [Report] [Vendor] | Nobody | Fold into C4 and L1: show realized net yield, subsidy and its end date, and all-in yearly cost, beside a T-bill and an ETF |
| C7 | **Protected exits** | Wrench attacks rose 33% in the first half of 2026 [Report]; Americans 60 and over lost $4.4B to crypto fraud in 2025, including through recovery scams [Regulator, via press]; Bitkey, Safe and Nunchuk ship delays and limits | Bitkey, for bitcoin only; no brokerage-native wallet | Add as a claim; it gives guardrails a safety story as well as a discipline story. Ask counsel whether a provider co-signer that can delay a transaction counts as control (see Regulation) |
| C8 | **Proven recovery** | Casa, Unchained and Nunchuk check keys but run no restore drill; mainstream wallets depend on one Apple or Google account; Kraken has a known iOS restore bug; the Coldcard flaw showed a key check cannot prove a seed is strong [Help doc] [Press] | Casa holds the "check" half | Move rehearsed recovery from "where we play" into the positioning, worded as rehearsed and not tied to one account |
| C9 | **Records that survive the move** | Assets moved to self-custody lose their covered status, so the broker stops tracking basis; basis is tracked wallet by wallet; the first 1099-DA forms showed $0 basis for coins moved in from wallets; lending is excluded from 1099-DA [Review] [Press] | Nobody; Robinhood could, as it controls both sides of the move | Re-rate Bet 5 (records) in the assumption map; the pain is better evidenced than round 1 assumed |

**A tension, not a claim: "your plan, or a model you choose".** Bitwise offers manager-designed models through Glider outside the US and through Parrot in the US, and Coinbase Advisor proposes portfolios. Some users may prefer picking a model to defining a plan. That is research question 2, and it bears on the discretion decision, because selecting a third party's model may sit close to advice.

### Competitor claims the positioning does not answer

| Claim | Who makes it | How prominent | Stance to decide |
| --- | --- | --- | --- |
| Protection or coverage | Coinbase One tiers; MetaMask Transaction Protection; Kraken Firelight coverage; Robinhood's Lloyd's policy, which covers Robinhood and gives users no direct claim | A headline tier benefit at Coinbase; on MetaMask's launch page | Partner for coverage, or state exactly what is and is not covered at the moment of deposit |
| AI that acts for you | Robinhood Agents; Coinbase for Agents and Advisor; MetaMask Agent Wallet | The headline of Robinhood's HOOD Summit | Answer with C5′; the phase 3 assistant follows the same rules |
| Registered advice | Coinbase Advisors, LLC; Robinhood Strategies (an adviser charging 0.25%, no crypto yet) | In the product names | State the non-advisory stance plainly: you define the plan, the product executes it |
| Tax forms | Every custodial broker issues a 1099-DA | A default, not marketing | C9 |
| Borrowing against bitcoin | Ledger Wallet (Morpho), Coinbase | Release headlines | Not in the strategy today; decide whether it belongs in a later phase |
| Spending and cards | MetaMask, Phantom, Exodus, Coinbase One card | Prominent | Not doing; consistent with the investor frame |
| Perps, tokenized stocks, copy trading | Robinhood, Coinbase Wallet, Phantom | Prominent | Not doing; contradicts principle 5 |

## Pricing benchmarks

Safety already sells as a subscription at $120 to $480 a year, while spot crypto trades cost 0.5% to 1% at brokerages; these figures feed the open business-model decision. Dates vary, and figures older than September 2026 are marked dated.

| Product | Model | Figure |
| --- | --- | --- |
| E\*Trade / Schwab / Fidelity | Per-trade fee on crypto | 0.50% / 0.75% / 1.00% (May–Aug 2026, dated) |
| Robinhood | Maker and taker fees by volume when routed to its exchange | 0.95% / 0.50% for small traders, falling with volume (June 2026, dated) |
| Coinbase One | Subscription | $49.99, $299.99 or $2,999.99 a year; includes 3.75% on USDC |
| MetaMask / Phantom | Swap fee | 0.875% / 0.85% |
| Spot bitcoin ETFs | Expense ratio | From 0.14% (MSBT) to 0.25% (IBIT, FBTC); GBTC 1.50% |
| Staking ether ETFs | Expense ratio plus a cut of rewards | ETHB 0.25% plus 18% of staking rewards; Grayscale's staking mini fund 0.15% |
| Robo-advisers | Advisory fee, crypto through ETFs | Wealthfront and Betterment 0.25% |
| Casa / Unchained / Nunchuk | Subscription for custody and recovery | $250 a year / $250 per vault a year / $120 to $480 a year |
| Kubera | Subscription for net-worth tracking | $250 a year |
| Curators | Performance fee on interest | 0% (Robinhood's vault) to 25% (Coinbase's USDC vault); about 14.5% across decoded vaults |

Yield as a membership perk (Coinbase One) is one model, but it is also the one most exposed to the new stablecoin rules. Curator fees work out to several times what a T-bill fund charges, which supports showing cost beside return.

## Naming, disclosure and eligibility

Avoid "vault", and explain eligibility in plain words: only Fidelity does that today. These findings feed the open naming and first-scope decisions.

- **Names in use.** "Account" (MetaMask Money Account; Schwab and Fidelity crypto accounts), "Earn" (Robinhood, Kraken), "Vault" (Coinbase and Kraken for strategies, Casa and Unchained for custody) and "Rewards" (Coinbase). "Vault" means two opposite things in this market, so SC-IA should avoid it.
- **Disclaimers.** The standard set is: not a bank or savings account, not FDIC or SIPC insured, and you can lose some or all of the deposit. It sits in a footer, a help article or an inline footnote, never in the headline. Kraken says its coverage is not insurance.
- **Enforcement.** I found no 2026 action aimed at the word "account". The New York Attorney General settled with Uphold for $5M in May 2026 over an earn product marketed as savings, with insurance claims (conduct from 2019 to 2020) [Report].
- **Eligibility.** Robinhood Earn is hidden in New York and Texas with no explanation. Coinbase lending excludes New York. Schwab excludes New York and Louisiana. Fidelity's crypto IRA excludes California and Oregon. Robinhood staking excludes California, Maryland, New Jersey and Wisconsin. MetaMask decides at its discretion, and Trust Wallet Earn excludes the US. Only Fidelity lists its exclusions in plain text, so explaining "not available to you, and why" is an easy place to beat the market.

## Regulation since September 30

No statute is coming soon, stablecoin yield is being narrowed by rule, and the same control test keeps recurring. These are research-based readings, not legal advice.

- **No statute soon.** The CLARITY Act failed cloture 49–50 on September 15 and is shelved; prediction markets put passage in 2026 at about 7% [Report]. Products, including this one, keep running on staff relief that can be reversed.
- **Stablecoin yield is being narrowed by rule.** The Federal Reserve's GENIUS Act proposal (September 29; comments due November 30) presumes an issuer is paying yield when it flows through an affiliate or related third party, including on white-label coins [Regulator]. The OCC expects its final rule by the end of October [Press]. Rewards funded by issuer revenue, such as Coinbase's USDC rewards, are the most exposed; yield from lending is less exposed. Naming the source of a return is becoming a compliance matter as well as a design one.
- **Advisers may self-custody.** The SEC's October 1 custody proposal (comments due December 7) would let registered advisers self-custody client crypto when no qualified custodian will hold it, with two-person authorization, one address per client and quarterly statements reconciled to the chain [Report]. That could create a new class of competitor, and it offers a ready vocabulary for controls and statements.
- **How choices may be shown.** SEC staff guidance for non-custodial interfaces asks that options be sorted by disclosed, objective criteria, not labelled "best" or "preferred", and that fees be fixed rather than tied to outcomes [Report]. This constrains how curator choice is presented.
- **The control test.** California's new licensing regime generally leaves out non-custodial wallets that cannot execute or prevent a transaction on their own [Report], and the Fed's proposal excludes self-custodial software interfaces from its definition of a service provider [Regulator]. My inference, for counsel: a provider co-signer that enforces delays could count as able to prevent a transaction. Rules enforced onchain may avoid that.
- **Curator discretion is the SEC's focus.** Sentora asked SEC staff to distinguish programmatic, limit-bound and actively curated vaults [Regulator], and counsel commentary sees rules-based strategies as lower risk [Report]. No source says a strategy the user selects reduces adviser risk.

## Demand and user voice

Surveys disagree on demand, users complain most about custodial freezes, and portfolio-share thinking (A2) still has no user-voice evidence.

- **Ownership.** Gallup (poll in June, released September 21): ownership among investors fell from 17% to 11%, 63% call crypto very risky, and 66% are not interested; ownership among upper-income investors is 15% [Report]. Security.org finds 30% of adults own, up from 27%, and a CoinShares survey of affluent investors finds about 70% of US respondents own [Report]. The surveys measure different groups and do not agree.
- **Older investors.** People 55 and over were 28% of first-time buyers in the past year, and 76% of 10,000 US holders want to hold crypto alongside their bank accounts [Report]. People 60 and over lost $4.4B to crypto fraud in 2025 [Regulator, via press].
- **What users complain about.** Custodial freezes and withdrawal holds lead the complaints at Kraken and Coinbase; this is the pain that pushes people toward self-custody, and round 1's pains table missed it. MetaMask reviews centre on lost funds, stuck transactions and support. Robinhood Wallet reviews mention having to use separate apps and seeing stale balances [User review]. No reviews yet mention the new earn products.
- **Sizing (A2).** Still no user-voice evidence that brokerage-native investors think in portfolio share; the evidence comes from advisers. The forums where these investors gather restrict crypto talk, which will make recruiting harder [Press].
- **Scams have shifted.** Losses to wallet drainers fell 83% in 2025, while fraud and recovery scams grew [Report]. The scam pain is now about being talked into a transfer, not approving a malicious contract.

Two rows to add to round 1's pains table: **custodial freezes and holds** (relieved by self-custody, but with no help if access is lost) and **scams aimed at older investors** (relieved by nobody).

## Implications for design strategy

Differentiate sooner on allocation, reframe C5 against agents, widen C4 to cost and realized yield, and add protected exits and proven recovery to the positioning.

| Decision | Where | Design implication |
| --- | --- | --- |
| **Differentiate, sooner** | Allocation home (C1) | The US window is open but the technique is proven. Decide build or partner for session-key rebalancing before phase 2 |
| **Differentiate, reframed** | Plan executed exactly (C5′) | The plan is the contract any agent must obey, and the rule is shown at the moment each action runs |
| **Differentiate, widened** | Legible earn (C4 and L1) | Show realized net yield, subsidy and end date, and all-in yearly cost, beside a T-bill and an ETF |
| **New differentiators** | Protected exits (C7), proven recovery (C8) | Add to the positioning; check provider co-signing with counsel |
| **Decide** | Protection | Partner for coverage, or state exactly what is not covered |
| **Parity** | One-tap earn, a named curator, eligibility explained | Robinhood and Kraken made one-tap earn table stakes inside a main app |
| **Concede, more widely** | Passive exposure, now including ether staking yield | Staking ETFs pay income with a tax form; say when the ETF is the better tool |

### What round 2 adds to the open decisions

| Open decision | What round 2 adds |
| --- | --- |
| Discretion and execution model | Glider's session key is a working precedent for "a limited, revocable permission"; the interface guidance and California's control test; the Sentora memo; no source on user-selected strategies |
| Naming | "Vault" is ambiguous; disclaimers sit in footers; competitors now set protection expectations |
| First scope | State exclusions cluster in New York and Texas; Kraken shows embedded-wallet earn can reach most of the US |
| Business model | The price benchmarks above; safety subscriptions at $120 to $480 a year; yield as a perk is exposed to the new rules |
| Recovery partner and liability | Bitkey's delay-and-notify model, Casa's co-signer and key checks; nobody runs restore drills |
| Primary user | Falling ownership among investors (Gallup); the share of buyers aged 55 and over; forums that suppress crypto |

### What to test next (additions to round 1)

- **Protection.** Do brokerage-native investors expect protection from an "account", and does an exact coverage statement correct that without lowering sign-up?
- **Rules versus agents.** Given an AI agent and a fixed plan, which would they trust with a sleeve, and why?
- **Headline versus realized.** Does showing realized net yield and the subsidy's end date change what people choose? This extends Bet 2's choice experiment.

Competitor screens stay out of the pain-discovery interviews, per the October 5 decision.

### Evidence still needed

- Hands-on teardowns: Robinhood Earn in the main app, Kraken DeFi Earn, Coinbase Advisor, MetaMask Money Account, and Glider if accessible.
- Glider's US availability, fees and revoke flow.
- Coinbase One's protection terms, Kraken's fee percentage, MetaMask's US eligibility and fee split, and Coinbase's current share of lending fees (the source is from October 2025).
- The OCC's final GENIUS rule, expected by October 31.
- Reddit and Bogleheads threads, which could not be read; a16z's State of Crypto 2026, not yet published as of October 20; allocation guidance updated after September.

## Sources and confidence

Source-type tags: [Vendor], [Help doc], [Terms], [Filing], [Press], [Review], [Video], [User review], [Report], [Regulator]. Checked on October 20 means I reopened the source myself.

**Competitors and new entrants**

- [Robinhood Earn support page](https://robinhood.com/us/en/support/articles/crypto-earn/) [Help doc]: USDG, Privy keys, no restore, NY and TX, insurance scope. Checked October 20.
- [HOOD Summit 2026](https://robinhood.com/newsroom/hood-summit-2026/) [Vendor], September 29: Agents, Loops, agentic accounts, risk disclosure. Checked October 20.
- [Merkl case study: Robinhood](https://merkl.xyz/case-studies/robinhood) [Vendor, partner], September 2026: native yield and subsidy split. Checked October 20.
- [Robinhood Strategies](https://robinhood.com/us/en/support/articles/about-strategies) [Help doc]: 0.25% managed portfolios, no crypto.
- [Coinbase USDC rewards](https://www.coinbase.com/usdc) and [Coinbase One](https://www.coinbase.com/one) [Vendor]: 3.75%, tiers and coverage amounts. Checked October 20.
- [Coinbase Advisor](https://www.coinbase.com/advisor) [Vendor]: SEC-registered, non-discretionary, beta. Checked October 20. [Form CRS](https://reports.adviserinfo.sec.gov/crs/crs_342338.pdf) [Regulator], April 24, 2026.
- [Coinbase for Agents](https://www.coinbase.com/nl/blog/coinbase-for-agents) [Vendor], June 11, 2026: permissions, caps "coming soon". Checked October 20.
- [Coinbase Wallet rebrand](https://theblock.co/news/defi/2026-09-10-coinbase-rebrands-base-app-back-to-coinbase-wallet-after-just-over-a-year-as-social-experiment-falls-short-414115) [Press], September 10. Checked October 20.
- [Coinbase smart wallet recovery](https://help.coinbase.com/en/wallet/getting-started/smart-wallet-recovery) and [permissions](https://help.coinbase.com/en-gb/wallet/getting-started/smart-wallet-permissions) [Help doc].
- [Kraken DeFi Earn FAQ](https://support.kraken.com/articles/defi-earn-faq) and [what is DeFi Earn](https://support.kraken.com/articles/what-is-defi-earn) [Help doc], October 15: vaults, curator, US, fees, Firelight. Checked October 20.
- [Kraken iCloud restore](https://support.kraken.com/gb/articles/recovering-your-wallet-with-icloud-backup) [Help doc]: known iOS issue.
- [Veda on MetaMask Money Account](https://www.veda.tech/blog/veda-metamask-money-account-defi-yield-wallet) [Vendor], October 14: up to 4%, Morpho only, Steakhouse. Checked October 20.
- [MetaMask Agent Wallet](https://metamask.io/news/introducing-metamask-agent-wallet) [Vendor], August 6: Guard Mode, 2FA, protection. Checked October 20. [Money Account help](https://support.metamask.io/trade/money-account/) and [Transaction Shield](https://support.metamask.io/manage-crypto/transactions/transaction-shield/) [Help doc].
- [Glider docs](https://docs.glider.fi/) [Help doc]: smart accounts, session keys, strategies. Checked October 20. [Bitwise Automated Token Portfolios](https://crypto-economy.com/bitwise-rolls-out-automated-token-portfolios/) [Press], August 25: non-US only, 0.15% fee. Checked October 20. [Parrot and Bitwise models](https://cryptoslate.com/crypto-model-portfolios-bitwise-parrot/) [Press], June 22.
- [Trust Wallet Stablecoin Earn](https://trustwallet.com/stablecoin-earn) [Vendor]: excludes the US and UK. Checked October 20.
- [Ledger Wallet, October 2026](https://www.ledger.com/blog-ledger-wallet-october-2026) [Vendor], October 7.
- [Phantom Cash](https://phantom.com/cash) [Vendor]; [Fidelity Crypto help](https://www.fidelity.com/crypto/help/account-basics/getting-started) [Help doc].

**Recovery and protected exits**

- [Casa health check](https://support.casa.io/knowledge/what-is-a-health-check) [Help doc], May 21: key checks, not restores. Checked October 20. [Casa pricing](https://casa.io/pricing) [Vendor].
- [Bitkey Delay and Notify](https://support.bitkey.world/hc/en-us/articles/18802027341460-Why-is-there-a-security-delay-during-the-Delay-Notify-recovery-process) [Help doc], October 15: 7-day default. Checked October 20. [How Bitkey works](https://bitkey.world/how-it-works) [Vendor].
- [Unchained key checks](https://help.unchained.com/what-is-a-key-check-and-why-do-i-need-to-do-it) [Help doc]; [Unchained pricing](https://unchained.com/pricing) and [Nunchuk pricing](https://www.nunchuk.io/pricing) [Vendor].
- [Safe RecoveryHub](https://help.safe.global/articles/9622260218-account-recovery-with-saferecoveryhub) [Help doc]; [Coinbase Vault](https://www.coinbase.com/vault) [Vendor].
- [CertiK on wrench attacks](https://decrypt.co/374136/crypto-wrench-attacks-cost-victims-124m-in-six-months-up-12x-certik) [Press], July 23; [Coldcard flaw](https://www.thehackernews.com/2026/08/coldcard-hardware-wallet-flaw-linked-to.html) [Press], August.

**Yield, pricing and naming**

- [Crystal Foresight: the yield you're sold and the yield you get](https://crystalintelligence.com/stablecoin/the-yield-youre-sold-and-the-yield-you-get/) [Report], July 23: realized vs advertised, collateral, curator take, depositor split. Checked October 20.
- [Curated vault concentration](https://en.coin-turk.com/morpho-leads-11-3-billion-curated-defi-vaults-as-top-5-managers-control-69yuzde/) [Report], August 25.
- [Bitcoin ETF expense ratios](https://www.spark.money/tools/bitcoin-etf-expense-ratio-comparison) [Report], August; [ETHB overview](https://info.arkm.com/research/ethb-everything-we-know-about-blackrocks-new-ethereum-staking-etf) [Press]; [Grayscale ETH fact sheet](https://www.sec.gov/Archives/edgar/data/0002020455/000202045526000003/eth_fact_sheet_4.23.26.htm) [Filing].
- [Uphold settlement with the NY Attorney General](https://www.regulatoryoversight.com/2026/05/crypto-company-settles-with-new-york-ag-over-allegedly-misleading-crypto-yield-promotions/) [Report], May 2026.

**Regulation**

- [Federal Reserve GENIUS Act proposal, Docket R-1899](https://govinfo.gov/content/pkg/FR-2026-09-29/html/2026-19860.htm) [Regulator], September 29. Checked October 20.
- [SEC custody proposal (Ropes & Gray)](https://www.ropesgray.com/en/insights/alerts/2026/10/sec-proposes-new-crypto-asset-custody-rules-and-overhaul-of-adviser-registered-fund-and-bdc-custody) [Report], October 16. Checked October 20.
- [CLARITY Act stalls (Orrick)](https://www.orrick.com/en/Insights/2026/10/The-CLARITY-Act-Stalls-in-the-Senate-Whats-Next-for-Digital-Asset-Regulation) [Report], October 2; [CLARITY odds](https://defirate.com/clarity-act-fact-sheet/) [Report]; [OCC final rule timing](https://www.kucoin.com/news/flash/occ-aims-to-finalize-genius-act-stablecoin-rules-by-october-31) [Press], October 15.
- [Non-custodial interface guidance (Fenwick)](https://www.fenwick.com/insights/publications/wallet-to-wall-street-cftc-and-sec-staff-chart-parallel-paths-for-noncustodial-crypto-access) [Report], April 29; [Sentora memo to SEC staff](https://www.sec.gov/files/ctf-memo-sentora-081026.pdf) [Regulator], August 10; [vault registration status (Croke Fairchild)](https://crokefairchild.com/2026/08/client-alert-the-vault-vacuum-the-registration-status-of-defi-vault-protocols-under-u-s-federal-securities-and-commodities-laws/) [Report]; [California DFAL](https://www.elliptic.co/blog/california-dfal-july-2026-licensing-deadline) [Report].
- [1099-DA and cost basis (Harness)](https://www.harness.co/articles/reconciling-crypto-cost-basis-before-new-1099-da-rules) [Review], October 1; [Coinbase executives on 1099-DA confusion](https://finance.yahoo.com/news/coinbase-executives-warn-irs-tax-233607082.html) [Press], March 9.

**Demand and user voice**

- [Gallup ownership poll (Bitcoin.com)](https://news.bitcoin.com/crypto-news/us-crypto-ownership-falls-to-11-as-63-of-investors-see-high-risk/) [Report], September 22. Checked October 20.
- [Security.org survey](https://www.security.org/?p=57009) [Report]; [CoinShares affluent investor survey](https://cointelegraph.com/news/majority-of-affluent-investors-across-7-countries-own-crypto-survey) [Press]; [Americans over 55 holding crypto](https://finance.yahoo.com/markets/crypto/articles/more-americans-over-55-hold-203000149.html) [Report], May 15.
- [FBI crypto fraud figures for 2025](https://www.theblock.co/amp/post/397134/fbi-says-crypto-related-fraud-losses-hit-record-11-4-billion-in-2025-with-seniors-bearing-the-brunt) [Regulator, via press], April 12.
- [Trustpilot: MetaMask](https://www.trustpilot.com/review/metamask.io), [Kraken](https://www.trustpilot.com/review/kraken.com), [Coinbase](https://www.trustpilot.com/review/coinbase.com); [Robinhood Wallet on Google Play](https://play.google.com/store/apps/details?id=com.robinhood.gateway&hl=en_US) [User review].
- [Wallet drainer statistics](https://deepstrike.io/blog/crypto-wallet-drainer-statistics) [Report], August 2; [crypto bans in personal-finance forums](https://startupfortune.com/a-reddit-permaban-for-recommending-bitcoin-exposes-the-generational-fault-line-running-through-personal-finance-orthodoxy/) [Press].

**Confidence.** High for what vendors, help pages and regulators state about their own products and rules, and for the items checked on October 20. Medium for secondary reports, review sites and survey figures. "No evidence found" still means not found on public pages, not tested in the product. Review and forum voices skew toward crypto-native and dissatisfied users. The research ran up against a shared search limit near the end, so some follow-ups (Rabby, Glider's terms, Robinhood's 10-Q) were not done.
