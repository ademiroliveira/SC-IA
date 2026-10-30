# Time Machine Workshop: Facilitation Guide

## Overview

Three 60-minute sessions take eight people from wallet history to two or three committed moves. Session 1 looks back and names the milestones the team wants to drive; session 2 builds two opposing futures; session 3 walks back from them to today.

|  | Session 1: The past | Session 2: The futures | Session 3: The way back |
| --- | --- | --- | --- |
| Mode | Look back, then aim | Diverge | Converge |
| Work | History with guess-first numbers, then milestones tagged Lead, Join or Watch | Two world strips for 2040, 2035 and 2030 | Backcast, wildcard, pre-mortem, vote |
| Output | Three or four milestone themes on the wall | Two world strips with our milestones in them | Two or three committed moves with owners |
| Deck | Wallet Time Machine 1: The past, 28 slides | Wallet Time Machine 2: The futures, 15 slides | Wallet Time Machine 3: The way back, 15 slides |

**Method.** Session 1 asks which milestone we want to drive before any futures work, so the team starts from its own ambition. Session 2 starts far out, at 2040, which stops people extrapolating today. Session 3 asks what had to be true at each step back, then tests the ambition against every world.

**Roles.** Eight participants. In sessions 2 and 3 they work in two teams of four, each person with one lens. You facilitate, keep time and hold the default-drift baseline. You do not build a world.

**Spacing.** A week apart at most, with the next date set before each session ends.

**Materials.**

- One wall that stays up for all three sessions (see The wall)
- Sticky notes: one neutral color for session 1, then four colors, one per lens
- Dot stickers for two votes, 3 per person each time, or votes on a digital board
- Printed lens cards and world briefs, one set per team
- A timer everyone can see

## The wall

One wall carries the whole workshop, so each session starts where the last one stopped and the recap takes two minutes.

| Band | Filled in | What goes there |
| --- | --- | --- |
| Above the line | Session 2 | The two team world strips: 2040, 2035, 2030 |
| The line | Session 1 | A 2027 to 2040 timeline with three lanes, Lead, Join and Watch, holding the milestone stickies |
| Below the line | Session 3 | The backcast band under each world, then the sorted moves |

Photograph the wall at the end of every session. At the end of session 3, seal the 2030 strips for the time capsule (see After the workshop).

## The worlds

Two axes: who acts (a person directly, or an agent they delegate to) and where trust lives (with the user, or with an institution).

| | User-held trust | Institution-held trust |
| --- | --- | --- |
| **Agent-delegated** | **Team A: agents under my rules.** Personal agents act under rules the user writes and owns. | **Wildcard: institutional agents.** Agents act for you inside bank and brokerage rails. Revealed in session 3. |
| **Human-direct** | **Default drift (baseline).** Today's wallet, improved step by step. | **Team B: institution wallet.** The wallet dissolves into institutional apps. Custody is invisible. |

Teams A and B are built by the teams in session 2. The default-drift box is your baseline, and the wildcard is revealed in session 3. Print the table below as the world brief for each team.

| World | Core assumption | Push on this | Seed signals today |
| --- | --- | --- | --- |
| Team A: agents under my rules | Users keep their keys and delegate to agents through policies they write | Who audits what agents do, and who is liable? | ERC-7715 permission grants; MetaMask Agent Wallet limits and Guard Mode; Coinbase agent wallets with session caps |
| Team B: institution wallet | Institutions hold custody and users rarely sign | What does self-custody still mean, and who wants it? | Stripe owns Privy and Fireblocks owns Dynamic; US spot Bitcoin ETFs hold about $104B; OCC GENIUS Act rules exempt self-custody software from custody rules |
| Default drift (baseline) | Wallets improve step by step | Which problems are still unsolved in 2040? | EIP-7702 upgrades; passkeys; clear signing (ERC-7730) |
| Wildcard (session 3) | Agents act inside institutional rails | Which of our opportunities survive here? | x402 agent payments passed 138M transactions on Base by Q3 2026; GENIUS Act takes effect January 18, 2027 |

Seed signals come from the wallet evolution research report in this folder. Confirm dated figures before the session.

**Placing teams.** Place people so each team builds the world least friendly to its favourite milestone from session 1. If the top milestone needs user-held keys, its strongest backers build the institution wallet. A milestone that survives a hostile world is worth more than one that only works in the world its fans would draw.

## Preparation

Set all three dates and send the pre-read two days before session 1, and put up the wall before people arrive. Teams and lenses are set between sessions 1 and 2, once you know the favourite milestones.

**Pre-read (send 2 days before session 1).**

- The timeline of wallet milestones, one page
- The five unsolved problems today: recovery, signing comprehension, supply chain, delegation sprawl and cross-chain complexity
- Two questions to think about: which wallet change of the last 15 years did nobody see coming, and which next milestone would you want us to drive?

**Before session 1.**

- Put up the wall: a 2027 to 2040 timeline with Lead, Join and Watch lanes in the middle, and space above and below it
- Prepare your default-drift baseline: today's wallet extended to 2030, 2035 and 2040
- Check the figures behind the three guess slides: lost bitcoin, drainer losses and agent payments
- Neutral stickies, markers and dots for the vote

**Teams and lenses.** Assign these between sessions 1 and 2, so you can give each team the world least friendly to its favourite milestone. Mix functions across the two teams where you can. Inside each team of four, give each person one lens: the person, the attacker or regulator, the builder, the business. People keep their lens in sessions 2 and 3.

**Room and boards.**

- The wall, as in The wall
- One board per team for session 2, laid out as in Board layouts and pinned above the milestone band
- Your own board for the default-drift baseline

## Session 1: The past (60 min)

Session 1 walks the room through wallet history as a series of design problems, with a guess before each big number. It then asks which next milestone the team wants to drive or be part of, and ends with three or four milestone themes on the wall.

| Minutes | Block | What happens | Output |
| --- | --- | --- | --- |
| 0-5 | Frame | Goal, the three sessions, ground rules | Shared starting point |
| 5-30 | The past and the question | Four eras, three guesses, five open problems, then the question and the tags | A calibrated sense of how often we are wrong |
| 30-38 | Write | Silent writing: a milestone, a year, why us and a tag on each sticky | Two or three stickies each |
| 38-52 | Place and cluster | Read, place by year and tag, cluster | Named clusters on the milestone band |
| 52-60 | Vote and close | Silent dot vote, name the themes, set homework | Three or four milestone themes |

### Block 1: Frame (0-5)

- Say: "We are not predicting the future. Today we look back and name the milestones we want to drive. Next time we build two futures, and in the last session we walk back to the moves we make now."
- Show the three sessions and the wall that stays up between them.
- Ground rules: be specific, not clever; write before you talk; no milestone is wrong today.

### Block 2: The past and the question (5-30)

- Present the history as problems that moved, not technology that shipped: "don't lose the file," then "write down 12 words," then "understand what you are signing," then "decide what this account, app or agent may do."
- Walk the milestones from 2009 to 2026 in about two minutes, then the four eras: keys became portable (2012-14), the wallet became the approval layer (2016-24), accounts became programmable (2023-25), and interfaces and agents became the risk (2025-26).
- Guess before each big number. Give 30 seconds to write a guess on a sticky, hear two or three, then reveal: lost bitcoin, drainer losses in 2025, agent payments on Base. The gap between the guesses and the answer is the point.
- Read the caveats aloud: the lost-bitcoin share is an estimate, drainer losses fell mainly on lower market activity, and agent payment totals differ across trackers.
- Name the five open problems today: recovery, signing comprehension, supply chain, delegation sprawl, cross-chain complexity. Ask which one each person feels most in their own product.
- Ask: "In 2012, which of these shifts would this room have predicted?" Expect almost none. Say: "Ours will be wrong too. The value is in the reasoning."
- Close the block with the question: "Which next milestone do we want to drive or be part of? Which problem do we want to own?" A milestone is a shift in what wallets are or do, anywhere from 2027 to 2040, not a feature.
- Explain the tags. Lead: we make it happen. Join: we ride a shift others drive, such as a new standard. Watch: it matters, but it isn't ours to move. Ask people not to tag everything Lead.

### Block 3: Write (30-38)

- Eight minutes of silent writing, alone, before anyone speaks, so the loudest idea does not set the agenda.
- Two or three stickies each, one milestone per sticky, with the year it would be real, one line on why us, and a Lead, Join or Watch tag.

### Block 4: Place and cluster (38-52)

- Each person reads each sticky in one sentence and places it on the milestone band by year and lane. No debate yet.
- Cluster stickies that describe the same shift and give each cluster a short name.
- If one lane is crowded and another is empty, say so. That is a finding too.

### Block 5: Vote and close (52-60)

- Silent dot vote, then name the top three or four clusters as themes, each with its tag and year: 6 minutes. Rules are in Scoring and voting.
- Say: "These themes are hypotheses. Sessions 2 and 3 will test them."
- Close in 2 minutes: each person brings two real signals for or against the themes. Set the session 2 date before people leave.

### Outputs

- Every milestone on the band, by year and by Lead, Join or Watch
- Named clusters
- Three or four themes, each with a tag and a year

## Between sessions 1 and 2

Allow up to a week. Participants look for evidence for and against the themes, and you prepare the recap, the teams and a short signal pack.

| Who | Task | Time |
| --- | --- | --- |
| Each participant | Find two real signals for or against the themes: a launch, a rule or a paper | 15 min |
| Facilitator | Photograph the wall and fill the recap slide in deck 2 with the themes, tags and years | 15 min |
| Facilitator | Build a short signal pack from the latest weekly signal report: regulation, recovery and agent-wallet news that bears on the themes | 20 min |
| Facilitator | Place teams in the world least friendly to their favourite milestone, assign lenses and fill in the teams slide | 15 min |
| Facilitator | Print the world briefs, lens cards and two team boards | 20 min |
| Facilitator | Send the themes and the signal pack one day before session 2 | 10 min |

## Session 2: The futures (60 min)

Session 2 builds two opposing worlds for 2040, 2035 and 2030, starting far out, and asks in every column where our session 1 milestones sit. It ends with each team pitching its world and trying to break the other.

| Minutes | Block | What happens | Output |
| --- | --- | --- | --- |
| 0-5 | Recap | Read the themes, tags and years from the wall | Shared starting point |
| 5-10 | Worlds, teams and lenses | Show the 2x2, the teams and the lenses; hand out briefs and cards | Teams at their boards |
| 10-45 | Build the worlds | 2040 (15 min), 2035 (10), 2030 (10), with our milestone in every column | One world strip per team |
| 45-55 | Swap pitch | 3-minute pitch each, then 2 minutes on the other team's board | Signals and "what would break this" notes |
| 55-60 | Close | Homework and the session 3 date | Evidence to add before session 3 |

### Block 1: Recap (0-5)

- Read the three or four themes from the recap slide and point to them on the wall. Keep it to two minutes.
- Share one or two signals from the pack that cut against a theme, so the room does not start from agreement.
- Say: "Today we build two futures. In each one, we look for our milestones: do they exist, who drives them, and are they bigger, smaller or gone?"

### Block 2: Worlds, teams and lenses (5-10)

- Show the 2x2: who acts, agent-delegated or human-direct, by where trust lives, user-held or institution-held. Team A builds agents under my rules; Team B builds the institution wallet. Show your default-drift baseline first so teams have something to contrast against. The third world stays hidden until session 3.
- Show the teams and say why each got its world: it is the one least friendly to its favourite milestone.
- Hand out world briefs and lens cards. Each person keeps one lens for sessions 2 and 3. Ask the attacker and business lenses to speak first so optimism does not dominate.

### Block 3: Build the worlds (10-45)

Teams pin their board above the milestone band and fill one column at a time, using the rows on the board.

| Column | Time | Prompts |
| --- | --- | --- |
| 2040 | 15 min | Write the headline. Finish "In 2040 a wallet is ___." Name two things that no longer exist. Where is our milestone? Which UX pillar breaks first? |
| 2035 | 10 min | Same rows, shorter. Which shift between 2035 and 2040 made 2040 possible? Note it on a sticky marked T. |
| 2030 | 10 min | Same rows, shorter. What is already visible today that leads here? Name one thing that goes wrong. |

**Facilitator moves:**

- Call time at minute 25 and minute 35, hard. Say: "2030 will feel easy. That is the point: the near term is where concrete moves live."
- Around minute 20, ask each attacker lens: "How does this world get robbed?" Ask each business lens: "Who pays?"
- Keep the milestone question on screen. In every column, the "Our milestone here" row answers: does it exist, who drives it, is it bigger, smaller or gone? A milestone that is gone is as useful a finding as one that grows.
- If a team drifts toward today, ask: "What is gone?"

### Block 4: Swap pitch (45-55)

- Each team pitches its world in 3 minutes: the headline, "the wallet is...", what is gone, and where our milestone sits.
- Each team then spends 2 minutes on the other team's board, adding signals seen today to the signals row and notes on what would break the world.

### Block 5: Close (55-60)

- Before session 3, each person adds three signals and one "what would break it" note to their own team's board.
- Set the session 3 date before people leave.

### Outputs

- Two world strips, 2040 to 2030, above the milestone band
- An "Our milestone here" answer in every column
- A signals row on each board
- Tipping-point notes between columns

## Between sessions 2 and 3

Allow up to a week. Teams add real-world evidence to their worlds, and you build the cross-world map that opens session 3.

| Who | Task | Time |
| --- | --- | --- |
| Each participant | Add three signals to the team board: something seen today that points toward the world (a launch, a rule, a paper) | 20 min |
| Each participant | Add one note on what would break the world | 5 min |
| Facilitator | Photograph or export both boards after session 2 | 10 min |
| Facilitator | Build the cross-world map from both boards | 45 min |
| Facilitator | Prepare the wildcard card, pick the milestone for the pre-mortem and print the scoring template | 15 min |
| Facilitator | Send the recap and the map one day before session 3 | 10 min |

Look for four things when you build the map:

- Needs that appear in both worlds (for example, a signing or recovery need)
- Contradictions, where one world needs what the other forbids
- Gaps that neither team touched
- Where each session 1 theme grew, shrank or disappeared

## Session 3: The way back (60 min)

Session 3 swaps the worlds, walks backward from 2040 to today, tests the results against a wildcard world and a pre-mortem, compares them with what we wanted in session 1, and ends with two or three committed moves.

| Minutes | Block | What happens | Output |
| --- | --- | --- | --- |
| 0-5 | Recap | Walk the wall: milestones, two worlds, the cross-world map | Shared starting point |
| 5-27 | Backcast | Teams swap worlds and walk back from 2040 to today | Enablers, dependencies, tipping points, opportunities |
| 27-35 | Wildcard | Both teams test their opportunities against a merged world | Survivors and casualties |
| 35-40 | Pre-mortem | "It's 2030 and our milestone failed. Why?" | Causes and early signs to watch |
| 40-52 | Harvest | Silent dot vote, cluster, compare with session 1, sort | Clusters labeled no-regret, bet, blind spot or hedge |
| 52-60 | Commit and seal | Choose two or three moves with owners; seal the time capsule | Committed moves and a sealed capsule |

### Block 1: Recap (0-5)

- Walk the room along the wall: the milestone band from session 1, the two worlds above it, and the cross-world map. Name the needs both worlds share and the contradictions.
- Say: "Today we walk backward. For each world, what had to be true to get there, and what would we do first?"
- Teams swap boards. Each person keeps their lens.

### Block 2: Backcast (5-27)

Teams walk their new world in three steps, in the band below the strip. Capture each answer on a sticky marked E (enabler), D (dependency), T (tipping point) or O (opportunity). Aim the walk back at the session 1 milestones where they appear in the world.

| Step | Time | Question | Note type |
| --- | --- | --- | --- |
| 2040 to 2035 | 7 min | For 2040 to exist, what had to be true by 2035? | E, D, T |
| 2035 to 2030 | 7 min | For 2035 to exist, what had to be true by 2030? | E, D, T |
| 2030 to now | 8 min | What would we ship, test or decide in the next 12 months? | O |

**Lens moves:**

- The attacker lens challenges every enabler: "What would stop this?"
- The business lens asks of every opportunity: "Who pays, and why us?"
- The builder lens marks each opportunity as ready, hard or unknown.
- The person lens asks of each step: "Would I trust this?"

### Block 3: Wildcard (27-35)

Bring both teams to the wall and reveal the wildcard world: agents act inside institutional rails. Ask: "What if the two worlds merge?" Then go through the O notes one by one and ask: "Does this survive in the merged world?" Mark survivors with a star.

### Block 4: Pre-mortem (35-40)

- Pick the top milestone from session 1. Say: "It's 2030 and our milestone failed. Why?"
- Each person writes causes for two minutes. The attacker lens reads first.
- The room names the early signs we could watch for. Keep them: they become the watch items for hedges.

### Block 5: Harvest (40-52)

- Silent dot vote on the O notes: 3 minutes. Rules are in Scoring and voting.
- Cluster the top-voted notes: 4 minutes.
- Compare each cluster with the session 1 wall: did we name it then? 2 minutes.
- Sort each cluster as no-regret, bet, blind spot or hedge: 3 minutes. The four kinds are in Scoring and voting.

### Block 6: Commit and seal (52-60)

- Score the top clusters with the template, then choose two or three moves: 6 minutes. Prefer no-regret moves, and add one bet if the team has capacity.
- Each move gets an owner, a first step within 30 days, and one thing we will stop or skip to make room.
- Keep each move's Lead, Join or Watch tag. A Join move needs a named partner or standard. A Watch move becomes a hedge with a signal to track.
- Seal the time capsule in the last 2 minutes: photograph the wall, seal the 2030 strips, and name the dates for the 30-day check-in and the reopening.

### Outputs

- Two backcast boards
- Pre-mortem causes and the early signs to watch
- A ranked list of opportunity clusters, each labeled no-regret, bet, blind spot or hedge
- Two or three committed moves, each with an owner, a first step, a no and a tag
- A sealed time capsule

## After the workshop

Futures work fades when nobody looks at it again. Three habits keep it alive.

- **The 30-day check-in.** Put it inside a ritual the team already has, such as a monthly ideation session, rather than a new meeting. For each committed move, ask: did the first step happen, and what did it teach us?
- **The time capsule.** Reopen the sealed 2030 strips a year later. Compare what we predicted with what happened, and note which signals we read well and which we missed.
- **The watch items.** Keep the pre-mortem's early signs next to each hedge. When one shows up in the weekly signal report, open the ready plan.

Send the recap within 48 hours of session 3: photos of the wall, the committed moves with owners and first steps, and the check-in date.

## Lens cards

Print one set per team, one card per person, for sessions 2 and 3. Each lens has its own sticky-note color, so the boards show whose view an idea comes from. The cards are also at the end of decks 2 and 3.

### The person (yellow stickies)

Your job: speak for someone living in this world.

- What do I do on a normal Tuesday?
- What do I no longer have to know or decide?
- What would make me stop trusting this wallet?
- Which UX pillar am I relying on most?

### The attacker or regulator (pink stickies)

Your job: find what breaks and what gets blocked.

- How would I steal from this world?
- What would a regulator require or ban?
- Which signing, recovery or permission step is weakest?
- What does the news story about a failure say?

### The builder (blue stickies)

Your job: say what we would have to build, and in what order.

- What would we have to ship by 2030?
- What is hard or still unknown technically?
- What could we prototype this quarter?
- What would this change in how we design today?

### The business (green stickies)

Your job: say who makes money and who loses.

- Who pays for this, and why?
- Who loses revenue or control?
- What would the company need to believe?
- What is our right to play here?

### Pillar reference

Use these five pillars for the "first pillar to break" row on the board: Trust Through Transparency, Continuous Feedback and Clarity, Risk Prevention and Recovery, Efficiency and Cost Respect, Adaptive Guidance.

## Board layouts

**Session 2 strip**

| | 2040 | 2035 | 2030 |
| --- | --- | --- | --- |
| Headline | | | |
| The wallet is… | | | |
| What is gone | | | |
| **Our milestone here** | | | |
| First pillar to break | | | |
| Signals today | | | |

**Session 3 backcast band** (under the same columns)

| | Under 2040 | Under 2035 | Under 2030 |
| --- | --- | --- | --- |
| Box | True by 2035, so that 2040 exists | True by 2030, so that 2035 exists | Next 12 months: ship, test or decide |
| Notes | E, D, T | E, D, T | O |

Note key: E enabler · D dependency · T tipping point · O opportunity. The last box is the one that matters most; it holds the opportunities.

Each team gets one copy, pinned above the milestone band from session 1. Session 2 fills the top strip, including the "Our milestone here" row, and session 3 adds the backcast band under the same columns. Sticky colors follow the lens cards: yellow for the person, pink for the attacker or regulator, blue for the builder, green for the business.

## Scoring and voting

Both votes use three dots each, 24 in all: session 1 votes on milestone clusters, session 3 on O notes. In session 3 the four kinds of move then compare what holds across the worlds with what we named in session 1.

**Dot voting rules.**

- Each person gets 3 dots: on milestone clusters in session 1, only on O notes in session 3
- Stacking dots on one note is allowed
- Vote in silence, before any discussion
- In session 3, starred notes, the ones that survived the wildcard, stay visible while people vote

**Four kinds of move.** Sort each cluster of top-voted notes on two questions: did we name it in session 1, and does it hold in every world, including the wildcard?

|  | Holds in every world | Holds in one world |
| --- | --- | --- |
| We named it in session 1 | **No-regret:** start now | **Bet:** run a small, cheap test |
| We didn't name it | **Blind spot:** it holds everywhere and we missed it, so add it | **Hedge:** keep a watch item and a ready plan |

The gap between what we wanted and what holds is often the most useful finding of the workshop.

**Scoring template.** Fill it in for the top five clusters during the commit block. Time to start is now, within 6 months, or later. Type is no-regret, bet, blind spot or hedge. Choose two or three: prefer no-regret moves and blind spots, add one bet if the team has capacity, and name one hedge to watch.

| Cluster | Votes | Worlds (A, B, wildcard) | Impact (1-5) | Right to play (1-5) | Time to start | Type | Owner | First step within 30 days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cluster 1 |  |  |  |  |  |  |  |  |
| Cluster 2 |  |  |  |  |  |  |  |  |
| Cluster 3 |  |  |  |  |  |  |  |  |
| Cluster 4 |  |  |  |  |  |  |  |  |
| Cluster 5 |  |  |  |  |  |  |  |  |

## Facilitator notes

Futures workshops usually go wrong in a handful of ways. Each has a sign to watch for and a fix.

| Risk | Sign | Fix |
| --- | --- | --- |
| Session 1 anchors on the near term | Milestones read like next year's features | Ask which problem we want to own, and treat the themes as hypotheses |
| Teams build the world they like | Every milestone grows in both worlds | Place each team in the world least friendly to its favourite milestone |
| Teams extrapolate today | The 2040 column looks like a nicer version of the current wallet | Ask "What is gone?" and compare with the default-drift baseline |
| One lens dominates | The builder talks most while the attacker stays quiet | Rotate who speaks first in each column; the attacker speaks first on enablers |
| Optimism bias | Nothing goes wrong in any column | Each team writes one failure per column, and the session 3 pre-mortem does the same for our top milestone |
| 2040 overruns | 2035 and 2030 get rushed | Call time hard at minutes 25 and 35 of session 2; 2035 and 2030 are shorter by design |
| The loudest idea wins | Dots cluster right after someone's pitch | Write and vote in silence, before discussion |

**If attendance changes.**

- 6 or 7 people: keep two teams (3+3 or 4+3). In the smaller team, one person holds both the builder and business lenses.
- Fewer than 6: run one team in one world, use the default-drift baseline as the contrast, and skip the swap.

**If the board is digital.** Make each cell a frame, set one sticky color per lens, and lock the column headers.

**Closing checklist.**

- [ ] Pre-read sent 2 days before session 1
- [ ] All three session dates set before session 1
- [ ] The wall up, with the milestone band, before session 1
- [ ] Teams and lenses set before session 2, each team in its least friendly world
- [ ] Recap slide and team names filled in deck 2
- [ ] Boards, stickies, dots and printed cards ready
- [ ] Wall photographed after each session
- [ ] Recap and committed moves sent within 48 hours of session 3
- [ ] 30-day check-in booked inside an existing ritual
- [ ] Time capsule sealed, with a reopening date
