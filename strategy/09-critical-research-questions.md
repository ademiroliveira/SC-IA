# Critical Research Questions — Self-Custody Investment Account

As of October 5, 2026 · Author: AO · Live doc: https://claude.ai/code/artifact/f61da3b8-39cd-4b78-980f-fa8eaf440b64

## Why these three

These questions decide the product's first user, how far it can automate, and whether recovery gates funding. Each is framed as a research question with a hypothesis that can be supported or refuted. All three rest on desk research; none has been tested with brokerage-native investors yet.

A pain-discovery question now comes before the three. The three mostly test our solutions, and with no primary research yet, the first thing to learn is which pains these investors have at all.

| Working term | Meaning | Example |
| --- | --- | --- |
| Plan | The whole object a user defines | Allocation plan for a 3% slice |
| Rules | The parts of a plan | Target, drift band, ask-first threshold |
| Guardrails | The limits inside a plan | Spend caps, delay on large exits |

The strategy docs still say "policy" and "write". Both change if "plan" and "define" hold up in the wording survey.

## Start here: what is hard today, and for whom?

Every pain the strategy relies on comes from studies of people who already hold crypto, so the first round asks what is hard for these investors before testing any of our solutions. Questions 2 and 3 run as designed only if the pain behind them shows up here.

- **Research question:** What are the pains and unmet needs around holding or considering a deliberate slice of crypto, by segment, and which are severe enough that people act on them?
- **Hypothesis:** The pains that matter most are fear of losing access, the burden of operating it, not understanding where returns come from or what could go wrong, and missing records.
- **Supported if:** Participants raise these unprompted, with a workaround or a past attempt behind them.
- **Refuted if:** Other pains dominate, or these appear only when we prompt for them.
- **Method:** Generative interviews (research plan step 3), in the same sessions as question 1 and across both segments. The pain questions come first in each session, before any concept or product idea is shown.
- **Decision it informs:** Which bets have a real pain behind them, and whether questions 2 and 3 are worth running as designed.

**Discovery questions.** These are open and anchored in real past events. Nothing in them names a pain from our list.

1. Tell me about the last time you bought crypto, or seriously thought about it and held back. What happened?
2. What was the hardest or most worrying part?
3. What have you tried and given up on, and why?
4. What do you do today to keep track of it or keep it safe?
5. Has anything gone wrong, or nearly gone wrong? What did you do next?
6. Is there anything you avoid doing because it feels too risky?
7. Who else is involved or affected, such as a partner, family member or accountant? What do they say about it?
8. If one part of this could be taken off your hands, what would it be?

**How to weigh what people say.**

| What the participant does | Evidence that the pain is real |
| --- | --- |
| Raises it unprompted, and has a workaround or a failed attempt behind it | Strong |
| Raises it unprompted, but has done nothing about it | Medium |
| Agrees only when we name it | Weak |
| Does not recognise it when named | None |

**Pains we expect (hypotheses to compare against).** Keep this list out of the session until the end. Use it to prompt for anything not raised, and in analysis to compare what we expected with what came up unprompted.

| Pain we expect | Where the belief comes from | What it justifies |
| --- | --- | --- |
| Fear of losing access for good | Studies of existing holders | Rehearsed recovery; question 3 |
| The burden of operating it: chains, fees, approvals | Industry consensus among holders | The "not a DeFi operator" claim; question 2 |
| Not knowing where a return comes from or what could go wrong | Curated-vault failures and teaser rates; inferred | The risk card |
| Not knowing what they are approving; fear of scams | Fraud and wallet-compromise reports | Delays and warnings on risky actions |
| No way to size the amount or keep it sized | Advisor guidance; assumed for individuals | The allocation home screen |
| No records for tax or tracking | Tax rules; inferred | Native records |
| Not knowing how to start | Survey of non-owners in the general population | Onboarding |

**If the result is:**

- Our expected pains come up unprompted, with workarounds: run questions 2 and 3 as designed.
- Some come up and others do not: drop or defer the bets whose pain did not appear.
- Different pains dominate: revisit the framing before building any prototype.

## 1. Who is the first user, and what would move them?

The first user may be the exchange-only holder, not the brokerage-native investor the docs assume, and interviews across both segments can settle it.

- **Research question:** Which segment has the strongest intent for a deliberate slice, and what would move them from an ETF or exchange to self-custody?
- **Hypothesis:** Exchange-only holders are the earlier adopter, because they already value self-custody but haven't acted. Brokerage-native investors are the larger but later market, gated by recovery and records.
- **Supported if:** Exchange-only holders describe an unmet need and a past attempt, while brokerage-native participants say an ETF already does the job.
- **Refuted if:** Brokerage-native participants name a need an ETF can't meet (ownership, onchain earning) as often as exchange-only holders do.
- **Method:** Generative interviews (research plan step 3) anchored in past behavior, run across both segments.
- **Decision it informs:** Primary segment, recruiting and messaging.

**If the result is:**

- Brokerage-native participants say an ETF already does the job: the exchange-only holder becomes primary.
- Neither segment has a reason beyond the ETF: revisit the framing.
- Both have reasons, but different ones: there are two entry points, which affects scope.

## 2. Will they define and keep their own plan?

*Depends on the pain round: run this as designed only if participants raise the burden of operating it, or wanting control over what happens to their money.*

The non-discretion model assumes users will define their own plan; a prototype test shows whether they do it, understand it, and keep it.

- **Research question:** Will a brokerage-native novice define, understand and keep an allocation plan, or accept a managed default?
- **Hypothesis:** Novices will define a plan from a starter plan with three or four adjustable values, and will understand it better and trust it more than a managed default. A blank builder will cause errors and abandonment.
- **Supported if:** Most participants in the starter-plan condition change at least one default and can explain what the plan will do in a drawdown.
- **Refuted if:** Most accept defaults unchanged and can't explain them, or still prefer the managed default after seeing both.
- **Decision it informs:** How far the product can automate while staying non-discretionary.

**Conditions (between-subjects):**

- **A:** Blank plan; the user defines every value.
- **B:** Starter plan; the user adjusts disclosed defaults.
- **C:** Managed default; confirm only.

**Method:** Prototype test (research plan step 4). Participants set up a funded slice, handle a drawdown that triggers an ask-first prompt, then answer "what will the product do if...?" after a delay. Measure completion, edits made, intent-match errors, comprehension, and trust and control ratings.

**If the result is:**

- B wins on comprehension and trust: ship starter plans, and ask counsel whether a confirmed default counts as user-authored.
- Only C gets used: managed parts need a registered adviser or a named curator.
- A fails on ability: authoring is a power-user feature, which weakens the case for the brokerage-native user as primary.

## 3. How do users come to trust they can recover, and when?

*Depends on the pain round: run this as designed only if participants raise fear of losing access.*

The goal is justified confidence, meaning recovery works for the user and they know it does, so the key measure is the gap between how confident people feel and how well they recover.

- **Research question:** What gives users justified confidence that they can recover their funds, early enough that it doesn't cost the deposit?
- **Hypothesis:** Users deposit more and recover more successfully when they have seen recovery work for themselves. The drop-off cost is lowest when that proof comes after a small starter balance and before larger deposits.
- **Supported if:** The proof condition gives the most funded users who later complete a simulated lost-device recovery, and their confidence matches their ability.
- **Refuted if:** Proof lowers completion without improving recovery success, or raises confidence without raising ability.
- **Decision it informs:** Whether recovery gates funding, in what form, and at what balance.

**Conditions:**

- **A:** No recovery step.
- **B:** Recovery setup only.
- **C:** Setup plus a light check (confirm the backup or guardian responds).
- **D:** Setup plus a full test restore, placed either before the first deposit or after a starter balance. This is the "recovery drill".

**Method:** Prototype test (research plan step 5), followed by a delayed task where participants "lose" their device and try to recover. That task is the real measure, because it checks whether recovery works, not whether people liked the step.

**Wording note:** "Drill" is internal shorthand. Test "recovery test" and "practice run" with participants.

## Supporting questions for the interview round

The interviews for question 1 can answer six narrower questions in the same sessions. Two are not covered above; four feed the three questions. Each is a point where a wrong answer would change the strategy.

| Question the interviews must answer | Why it is critical | What it decides | Where it sits |
| --- | --- | --- | --- |
| How do they decide how much to put into crypto, and in what terms: a share of their portfolio, a dollar amount, or "what I can afford to lose"? | The allocation home screen assumes a share (A2) | Whether the slice is shown as a percentage or in dollars | **New** |
| What do they believe happens to their money in each place it can sit, and who do they think could move, reverse or protect it? | False beliefs here create risk for them and for the firm (A11) | Whether to use the word "account", and what the custody map must correct | **New** |
| Do they want to hold crypto themselves, and what are their own reasons for or against? | If they do not, the positioning fails (A1) | Whether self-custody leads the pitch | Feeds question 1 |
| When they compare this with a crypto ETF, what would make it worth the extra effort? | We assume onchain earning is the reason (A3) | Whether to lead with earning or with ownership and control | Feeds question 1 |
| Do they set rules for their investments today, or hand decisions to someone else? | Defining a plan is the core of the product and of the regulatory stance (A4) | Whether to lead with a user-defined plan or a managed option | Feeds question 2 |
| What would have to be true for them to trust they could get back in after losing a device? | Fear of losing access is assumed to be the main barrier (A6) | How much recovery work comes before funding | Feeds question 3 |

These are strategic questions, not interview questions. Asked directly they draw polite or hypothetical answers, so the interview guide should reach them through real past events, such as the last time someone bought or decided against crypto. The codes in brackets refer to the [Assumption Map](08-assumption-map.md).

**Questions that wait for a later round.** Two more matter, but each needs something concrete to react to.

- Does showing where a return comes from change which option they pick? (A10, choice experiment)
- Would they pay, and how much? (A13, pricing study once there is a prototype)

## Before testing

Agree on thresholds and recruiting first, since all three studies depend on who participates and what counts as a pass.

- [ ] Set pass/fail thresholds for each "supported if" and "refuted if" with PM.
- [ ] Recruit both segments (brokerage-native and exchange-only) for questions 2 and 3 until question 1 resolves.
- [ ] Cut all results by age, especially 55 and over.
- [ ] Treat prototype deposit amounts as directional, and confirm with real small balances in a beta.
- [ ] Test the wording in the wording survey (research plan step 8): "plan" against "standing instructions", "define" against "set", "recovery test" against "practice run".
- [ ] If the terms hold, update the strategy docs: "policy" becomes "plan" and "write" becomes "define" (Bet 3 and the investment policy statement).

A researcher will also need these settled before starting.

- [ ] **Decision and date:** what decision does each round inform, and by when?
- [ ] **Recruiting source:** can participants come from the company's own brokerage customers, or must they come from outside? Compliance may have a say.
- [ ] **Who and how:** who runs the sessions, and what are the budget and incentives?
- [ ] **Use of findings:** who needs to see them, and in what form?
