# Problem Framing — Self-Custody Investment Account

As of September 30, 2026 · Author: AO · Live doc: https://claude.ai/code/artifact/1cc4f4a2-8416-4231-a838-426e9321b2d2

## Problem statement

A self-directed investor who decides to hold a deliberate slice of digital assets has no product that lets them size it, earn on it, keep their own keys and stay out of DeFi operations, all in one place.

Investors who already think in allocations, drift and rebalancing must choose between custodial brokerage sleeves (familiar, but no ownership or onchain earning) and self-custody wallets (ownership, but token-first screens, opaque signing, unrehearsed recovery and no records). The gap between them is where people stall: they say they value self-custody, and most still keep assets on exchanges.

This doc frames the problem for agreement before solutions are argued. The answer to it lives in the [Product Design Strategy](04-product-design-strategy.md).

**Why now.**

1. Brokerages opened spot crypto in 2026 (Schwab alone to about 40M accounts), so the allocation frame is now mainstream.
2. Earn is commoditizing on one shared curated-vault engine, so the differentiator has moved to risk, control and records.
3. Staff guidance permits non-custodial front ends only with disclosed, non-discretionary execution, which makes user-authored decisions a requirement.
4. Robinhood already combines an audience, self-custody and earn, so the window for an investor-framed entrant is finite.

**How we know it is real.** The risk and market facts are published and checked: 158,000 personal-wallet compromises in 2025, over $11B in crypto fraud losses, and only 43% of surveyed crypto users able to identify a seed phrase. The demand side, whether this investor wants this product, is not yet tested; see the evidence base.

## Who it is for

The primary user is the brokerage-native investor, and almost everything we know about them is inferred, not observed.

| User | Who they are | Their goal | Their pain today | Crypto experience |
| --- | --- | --- | --- | --- |
| **Primary: brokerage-native investor** | Self-directed, $25K or more investable, no crypto or ETF-only exposure | A 1% to 5% slice that earns and stays sized | Must choose between custodial sleeves and operator-grade wallets | Novice |
| **Secondary: exchange-only holder** | Holds $1K to $50K on an exchange or brokerage | Ownership without new risk | Believes in self-custody, has never practised it | Novice to intermediate |
| **Stress case: users aged 55 and over** | 28% of recent buyers | Safety and inheritance | Most exposed to fraud | Mixed |
| **Stress case: self-custody regulars** | Six months or more in a wallet | Guardrails that do not slow them down | Operator burden, no records | Intermediate to expert |

**Job to be done.** When I decide part of my wealth belongs onchain, help me put it there, keep it sized and earning, and know I can recover it, so I can stop thinking about it without giving anyone my keys or learning DeFi.

**The core tension.** The more the product decides for the user, the less it is self-custody and the closer it is to a regulated manager. The less it decides, the more the user becomes an operator. Any solution has to say where it sits on that line.

## How might we

Six questions define the problem space; any strategy should answer all six.

1. How might we show a crypto slice as a share of net worth and of risk, not as a token list?
2. How might we make every return name its source, its risk and its expiry?
3. How might we let users set rules simple enough to write and strict enough to trust?
4. How might we prove recovery works before a large balance arrives?
5. How might we keep any automation inside the user's rules and visible when it runs?
6. How might we state plainly what the product can and cannot do, so "account" does not imply protection it cannot give?

## Evidence base

The market, risk and competitor claims are facts from public sources; every claim about what this user will choose, trust or pay for is a hypothesis. Levels: **Fact** = published and checked, **Inference** = reasoned from facts, **Hypothesis** = untested.

| Claim | Evidence | Level |
| --- | --- | --- |
| Investors accept a small, rebalanced crypto slice | BlackRock 1% to 2%, Morgan Stanley 2% to 4%, Fidelity 2% to 5%; Wealthfront caps crypto at 10% | Fact that guidance exists; whether the target user adopts it is a Hypothesis |
| People want self-custody but do not practise it | 66% call it important, 88% still use exchanges (single secondary report) | Inference, low confidence |
| Key management is a real barrier | 43% could identify a seed phrase (CHI 2025); 15% had tested recovery (vendor survey) | Fact for the first, medium confidence for the second |
| Mistakes and scams are costly and common | 158,000 personal-wallet compromises in 2025 (Chainalysis); over $11B crypto fraud losses (FBI IC3); Stream Finance vault loss of about $93M | Fact |
| Earning inside self-custody is now standard | Robinhood, MetaMask, Kraken and Coinbase pages, all on Steakhouse and Morpho | Fact |
| No one ships an allocation-first self-custody account | No evidence found across nine competitors and six adjacent groups | Inference; needs hands-on teardown |
| Serious holders pay for safety | Casa $250 a year, Unchained $250 to $6,000 a year | Inference; not tested for this segment |
| Users prefer to write their own rules over a managed default | None | Hypothesis |
| A rehearsed recovery drill raises willingness to deposit | None | Hypothesis |
| Showing rate source and risk changes which option people choose | None | Hypothesis |

The thinnest evidence is also the most important: how brokerage-native investors with no crypto think about self-custody. Existing surveys sample people who already hold crypto. Sources are listed in the [competitive analysis](../research/02-competitive-analysis.md) and the [market research](../research/01-market-and-opportunity-research.md).

## Constraints

Eight boundaries, most of them regulatory and most of them open to reversal, limit what any solution may say and do. These are research-based inferences and not legal advice; counsel must review them.

| Constraint | Basis | What it rules out or requires |
| --- | --- | --- |
| **Non-discretion** | SEC staff statement of April 13, 2026 on non-custodial interfaces: no solicitation, user-customizable defaults, disclosed routing | Decisions authored by the user; every default disclosed and editable; deterministic execution |
| **Curator and adviser exposure** | Commissioner Peirce, July 22, 2026, on curated vaults | Curator named; risk ratings presented as information, not a recommendation |
| **Yield language and source** | GENIUS Act ban on issuer-paid yield; OCC presumption on affiliate-routed yield | Held stablecoins never called "interest"; the source of each return stated |
| **Teaser rates** | MetaMask's 6% falling to 4% on October 1, 2026; Coinbase's earlier "up to 10.8%" | Base, incentive and expiry shown separately |
| **Eligibility** | New York and Texas exclusions at Robinhood and Coinbase; qualified-purchaser limits on treasury funds | "Not available to you, and why" as a first-class state |
| **Tax records** | No 1099-DA for self-custody; basis breaks when assets transfer | Records kept natively or through an integration |
| **Custody topology** | Guardians or co-signers move the product along the custody spectrum | Who holds which key, and what each party can do, made visible |
| **Reversibility of rules** | Most enabling guidance is staff-level and can be withdrawn | Earn modules switchable and re-gatable without breaking the account |

Data aggregation is a related risk: a product that holds portfolio and personal data becomes a target, and leaked personal data has driven physical attacks on holders.

## Research plan

The must-answer question is: **what would need to be true for a brokerage-native investor to put a deliberate slice of their wealth into self-custody?** The plan runs two cheap desk steps first, then generative interviews, then prototype tests on the riskiest hypotheses, then a survey to size what the earlier rounds find.

Questions come from the Web3 and AI research question bank; wording in quotes is taken from the bank, lightly shortened or adapted to this product.

| Order | Study | Primary question | Secondary questions | Decision it informs |
| --- | --- | --- | --- | --- |
| 1 | Hands-on teardown of Robinhood Wallet and MetaMask Money Account | What do they show on home, earn and recovery? | Where do they already meet the positioning? | Whether the gap is real |
| 2 | Counsel review | Is user-authored configuration enough to stay non-discretionary? | Is "account" safe to use? | Discretion model and naming |
| 3 | Generative interviews | "What would need to be true for a mainstream user to feel comfortable with self-custody?" | "What mental model do users have of where their crypto lives?"; "What prior mental models (banking, investing, gaming) do users bring?" | Whether this framing holds for the primary user |
| 4 | Allocation home prototype | Do investors fund more when home shows allocation against target than when it shows tokens? | "How do users monitor positions over time, and what would make them feel more in control?"; the trust-threshold question: what moves the point at which they proceed? | The home screen |
| 5 | Rules and automation prototype | Do users prefer writing their own rules over accepting a managed default, and can they write them? | "How much control do users want, and does that vary by context?"; "What would make delegation feel safe and trustworthy?" | How much the product automates |
| 6 | Recovery prototype | Does a rehearsed recovery drill raise willingness to deposit more than it lowers completion? | "How do users currently recover from wallet mistakes?"; "What does losing funds mean emotionally, and how does it affect future behaviour?" | The funding gate |
| 7 | Rate and risk choice experiment | Does showing source, incentive and exit time change which option people pick? | "What is users' mental model of yield: where does it come from, and does that affect trust?"; "What risk disclosures do users actually read vs scroll past?" | The risk card |
| 8 | Wording survey | What does "account" lead people to believe about protection and reversal? | The language question: "Does the product's language match the user's vocabulary?"; "this app has my money" versus "this contract has my money" | Naming and disclosure copy |

**Participants.** Twenty-four to thirty-six people in the qualitative rounds, then a quantitative survey. Suggested mix: about 35% brokerage-native and crypto-new ($25K or more investable), 30% exchange-only holders, 20% self-custody intermediates, 15% experienced DeFi users. Set quotas of at least 25% aged 55 or over and at least 40% women, include people who tried and abandoned self-custody, and exclude crypto-industry employees. State each participant's crypto experience explicitly when recruiting, because "has used DeFi" and "crypto-curious" recruit very different people.

## Open questions and sources

Five questions about the problem itself remain open. The research plan covers the first two; the next two need a sizing and pricing study that is not yet planned.

- [ ] Is the brokerage-native investor the right primary user, or is the exchange-only holder the real early adopter?
- [ ] Do these users think of the slice as a share of net worth, or as a dollar amount?
- [ ] Would they pay for this, how much, and in what form?
- [ ] How large is the segment in the US?
- [ ] Should users aged 55 and over be a first audience, given their fraud exposure, or served later with more protection?

**Sources.** Market, regulatory and user-research facts come from the [market research](../research/01-market-and-opportunity-research.md) (September 2026). Competitor and adjacent-solution facts come from the [competitive analysis](../research/02-competitive-analysis.md), which lists every public page used. Figures on the self-custody belief gap and recovery testing come from vendor or secondary sources and should be verified before external use. Regulatory points are not legal advice.
