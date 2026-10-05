# Outcome-Led Product Design — Deep Dive

As of October 4, 2026 · Author: AO · Live doc: https://claude.ai/code/artifact/a7c549fb-7729-4c81-907b-d7560d1d4cc1

## In brief

Outcome-led product design is not one method. It is a shared stance across several schools: define success as a change in what people do or how their lives improve, then treat everything you build as a bet on causing that change.

- **The core definition** most people use is Josh Seiden's: an outcome is "a change in human behaviour that drives business results." A feature is an output; it counts only if behaviour changes.
- **Designers have their own version.** Jared Spool frames a UX outcome as the answer to "If we do a great job, whose life do we improve, and how do we improve it?"
- **It is hard for organisational reasons, not conceptual ones.** Practitioners consistently report that it needs leadership support, trust and a different way of funding teams, and that most teams claiming it still measure shipping.
- **The evidence base is thin.** I found practitioner books, essays and case anecdotes, and no controlled study showing outcome-led teams outperform others. The most quantified school, Outcome-Driven Innovation, has a credible critique of its maths.
- **Verdict for this project:** use it, mainly as a discipline for naming what would prove the strategy wrong. For a financial product, pair every business outcome with a customer outcome, which is also how the UK regulator already frames the duty of firms.

A note on the name: the sources use "outcome-led", "outcome-driven" and "outcomes over output" interchangeably, and so does this doc.

## Core ideas

Five ideas carry almost all of the approach.

1. **Output, outcome, impact.** An output is something built and shipped. An outcome is the change in behaviour that the output causes. Impact is the business or social result that follows. The chain comes from programme-evaluation logic models; that origin is from my general knowledge and I did not check it against a source.
2. **An outcome is a behaviour, and it is observable.** Seiden's three "magic questions" make it practical: what user and customer behaviours drive business results, how can we get people to do more of them, and how do we know we are right?
3. **Not all outcomes are the same size.** [Teresa Torres](https://www.producttalk.org/outcomes-vs-outputs/) separates business outcomes (financial health, such as revenue), product outcomes (customer behaviour or sentiment inside the product) and traction metrics (use of one feature). Teams should be given product outcomes: business outcomes are too broad to act on and lag too far behind, and traction metrics only prove adoption, not value.
4. **Leading beats lagging.** A good outcome moves soon enough to learn from. Retention after a year is a lagging result; funding an account in the first week is a leading signal for it.
5. **A customer outcome is not a business outcome.** [Spool](https://articles.centercentre.com/what-are-outcome-driven-ux-metrics/) defines a UX outcome as an improvement in someone's life and measures it three ways: a success metric (a yes-or-no test that the outcome was reached), progress metrics (partial movement toward it) and problem-value metrics (what the current poor experience costs, in money).

A practical test of whether a statement is an outcome, adapted from Torres's test for opportunities: could more than one solution achieve it? If only one could, it is an output written in outcome language.

## Where it came from

The idea reached product design from three directions over about 25 years: innovation research, UX measurement, and the product-management reaction against "feature factories".

| When | Who | Contribution |
| --- | --- | --- |
| 1999 to 2005 | Anthony Ulwick, [Outcome-Driven Innovation](https://en.wikipedia.org/wiki/Outcome-Driven_Innovation) | First patent 1999, Harvard Business Review article 2002, book 2005. Customers want outcomes from a job, not products; rank outcomes by importance and satisfaction |
| 2010 | Rodden, Hutchinson and Fu at Google, [HEART](https://ixdf.org/literature/topics/heart-framework) | UX measured at scale through Happiness, Engagement, Adoption, Retention and Task success, with a goals, signals, metrics process |
| 2017 | John Cutler, [feature factory](https://www.mindtheproduct.com/break-free-feature-factory-john-cutler/) | Named the gap between saying "outcomes over output" and measuring shipping; traced it to low organisational trust |
| 2019 | Josh Seiden, *Outcomes Over Output* | The behaviour-change definition now used almost everywhere |
| 2019 | Marty Cagan, [product vs feature teams](https://www.svpg.com/product-vs-feature-teams/) | Empowered teams are given problems and judged on outcomes; feature teams are given roadmaps and judged on output |
| 2023 | Teresa Torres, [opportunity solution trees](https://www.producttalk.org/opportunity-solution-trees/) | One outcome at the root, then opportunities, solutions and assumption tests (article dated 2023; the method predates it) |
| 2023 | UK Financial Conduct Authority, [Consumer Duty](https://www.fca.org.uk/publications/multi-firm-reviews/consumer-duty-implementation-plans) | In force July 31, 2023. Firms must deliver and evidence good customer outcomes, an outcome-led frame written into regulation |
| 2025 | Jared Spool, [outcome-driven UX metrics](https://articles.centercentre.com/what-are-outcome-driven-ux-metrics/) | Outcomes defined as improvements in people's lives, with success, progress and problem-value metrics |

Two strands matter for designers in particular. Spool's keeps the outcome anchored to the person, and Cagan's explains why the role changes: in a feature team the designer tends to be reduced to visual work, while in an outcome-led team the designer shares responsibility for whether the problem was solved.

## The main frameworks compared

The frameworks answer different questions, so the useful move is to combine two or three, not to pick one.

| Framework | Question it answers | Unit of outcome | Main artefact | Main weakness |
| --- | --- | --- | --- | --- |
| **Outcomes over output** (Seiden) | What are we really trying to change? | A behaviour change that drives a business result | Outcome-based roadmap; hypotheses | Says little about how to find the right outcome |
| **Opportunity solution tree** (Torres) | How do we get from an outcome to something worth building? | One product outcome per team | Tree: outcome, opportunities, solutions, assumption tests | Needs a steady flow of customer interviews; the root is a business-value outcome |
| **Outcome-Driven Innovation** (Ulwick) | Which needs are underserved in this market? | Desired-outcome statements for a job | Opportunity score: importance + (importance − satisfaction) | Long surveys; importance dominates the score (see critiques) |
| **Outcome-driven UX metrics** (Spool) | How do we show design's value? | An improvement in someone's life | Success, progress and problem-value metrics | Depends on stakeholders accepting a customer-defined finish line |
| **HEART** (Google) | Which metrics should we watch? | Goals across five experience categories | Goals, signals, metrics table | Too many metrics; engagement can be a vanity measure |
| **Empowered teams** (Cagan) | How must the organisation work? | A problem to solve | Team objectives | Requires leadership and funding change |
| **Consumer Duty** (UK FCA) | What does a financial firm owe customers? | Four customer outcomes: products and services, price and value, understanding, support | Outcome monitoring and evidence | A UK rule, not a US one; a frame to borrow, not an obligation here |

A workable combination for a new product is Seiden's definition to state the outcome, Spool's question to keep it tied to the customer, and Torres's tree to connect the outcome to bets and tests. HEART helps later, once there is traffic to measure. The weakness listed for Spool's approach is my inference, not a published critique.

## How it works in practice

In practice it is a loop of seven steps, and the work is finished when behaviour changes, not when something ships.

1. **Name the impact** the business needs, such as revenue, retention or cost.
2. **Find the behaviours that drive it** and choose one as the team's product outcome. It should be a leading signal the team can influence.
3. **Write the customer outcome beside it:** whose life improves, and how.
4. **Map the opportunities** from research: the needs, pains and desires that stand between people and that behaviour.
5. **Place several bets per opportunity** and name the riskiest assumption in each.
6. **Test the assumption cheaply** and measure what people do, not what they say.
7. **Review progress against the outcome.** Roadmaps list outcomes and problems, not features and dates.

Steps 1 to 3 come from Seiden and Spool, 4 to 6 from Torres, and 7 from Seiden and Cagan. The ordering into one loop is my synthesis.

**The working rhythm the sources describe.** [Torres](https://www.producttalk.org/opportunity-solution-trees/) has a product manager, designer and engineer build the tree together, start after three or four story-based customer interviews, and revisit the opportunities every three to four weeks. [Dave Martin](https://www.mindtheproduct.com/why-is-outcome-led-so-tricky/) adds weekly customer contact, hypothesis-driven development, and weekly check-ins on the outcome in place of delivery reviews.

**What changes for designers.**

| Before | After |
| --- | --- |
| Brief names a feature | Brief names a behaviour to change and for whom |
| Critique asks "is it good?" | Critique asks "which outcome does this serve, and what is the evidence?" |
| Done means handed off | Done means the behaviour moved, or the bet was dropped |
| Research is a phase | Research is continuous and feeds the opportunity map |
| Metrics belong to product or analytics | The designer helps choose the signal and reads it |

This table is my summary of the shift the sources describe, not a quotation from any one of them.

## Evidence and critiques

The case for outcome-led work rests on practitioner experience, not on controlled evidence, and its best-known failure modes are organisational.

**What the evidence is.** The sources are books, essays and named success stories. Dave Martin cites Datadog, Xero, Slack and Dropbox as outcome-led companies and a figure that 88% of features are rarely or never used; the article does not give a method for either claim, so treat both as illustration. I found no controlled study comparing outcome-led teams with others. That is an absence in what I searched, not proof that none exists.

**Where it goes wrong.**

| Failure mode | What happens | Source |
| --- | --- | --- |
| **Organisation not ready** | Needs leadership backing, trust and a different funding model; without them teams keep being judged on shipping | [Martin](https://www.mindtheproduct.com/why-is-outcome-led-so-tricky/), [Cutler](https://www.mindtheproduct.com/break-free-feature-factory-john-cutler/) |
| **Outcome theatre** | Adoption of a feature is reported as an outcome; teams pick what is easy to measure, or rely on sentiment alone | [Torres](https://www.producttalk.org/outcomes-vs-outputs/) |
| **The slogan oversimplifies** | Results depend on the quality and speed of data, insight and action together; fast delivery with poor decisions fails, and so does good insight with slow delivery | [Cutler](https://cutlefish.substack.com/p/tbm-4353-the-product-outcomes-formula) |
| **Hard to measure** | Many valuable outcomes happen outside the product, lag by months, or have several causes | [Torres](https://www.producttalk.org/outcomes-vs-outputs/) |
| **Scoring that looks rigorous and is not** | In Outcome-Driven Innovation, importance alone explained about 84% of the opportunity score in three reports reviewed; surveys of 50 to 150 statements strain respondents | [Buchanan](https://bradenbuchanan.substack.com/p/outcome-driven-innovation-a-critique) |
| **Too many metrics** | HEART's five categories interact, and engagement means little where use is not optional | [HEART overview](https://ixdf.org/literature/topics/heart-framework) |
| **Gaming the target** | Once a measure becomes a target, people optimise the measure. In finance, chasing deposits or engagement can work against the customer | Goodhart's law; general knowledge, not checked against a source here |
| **No baseline** | A product that does not exist yet has nothing to compare against, so early outcomes are proxies from prototypes | My inference |

**The tension to keep in view.** Torres roots the tree in an outcome that creates business value, on the argument that business value earns the right to keep serving customers. Spool and the UK Consumer Duty start from the customer. For a product holding people's money, the two should be written side by side, so a business outcome can never be met by harming the customer one.

## Applying it to the self-custody investment account

The current strategy has bets and principles but no stated outcome, so the first move is to choose one primary outcome and pair it with a customer outcome. Everything in this section is my proposal, built on the existing strategy doc; none of it is tested.

**Four candidate outcomes.**

| Candidate | Behaviour (product outcome) | Whose life improves, and how (customer outcome) | Earliest signal | Bets it justifies | How it could be gamed |
| --- | --- | --- | --- | --- | --- |
| **A. Funded and understood** | Brokerage-native investors fund beyond a starter balance and can say correctly what the product cannot do | An investor holds a sized slice they understand and control | Funding after the recovery drill; a comprehension check | 1 (allocation home), 4 (rehearsed recovery) | Pushing deposits; the comprehension half blocks that |
| **B. Stays the course** | Holders keep their policy through a fall of 30% or more | An investor avoids panic selling and unplanned risk | A policy written and signed; rebalances run inside it | 3 (policy as core object), 5 (native records) | Making exit hard; must be paired with a fast, clear exit |
| **C. Knows what they earn** | Users can name the source and main risk of their earn sleeve | An investor is not surprised by a loss | Choice experiment; in-product check | 2 (risk shown) | Teaching to the test; check with fresh wording |
| **D. Can get back in** | Users complete a rehearsed recovery, and real recoveries succeed | An investor and their family do not lose access | Drill completion before larger balances | 4 (rehearsed recovery) | Counting drills started, not finished |

**Recommendation.** Make A the primary outcome. It is the earliest behaviour that can be observed in a prototype, it ties to the business, and its second half protects the customer. Treat B as the long-run outcome, since it needs a real drawdown to measure, and C and D as customer outcomes that must hold whenever A improves.

**How this changes the existing docs.**

- The strategy's success-criteria table becomes an outcome tree: A at the root, opportunities from the interviews beneath it, then the five bets, then their tests.
- The three research learning goals each gain a job: sizing and triggers inform A, rules and delegation inform B, custody beliefs inform D.
- The open decision on business model becomes urgent, because the business impact above A (assets held, subscription revenue) is still undefined.
- The four UK Consumer Duty outcomes make a useful check even though the product is US-based: products and services maps to A, understanding to C, support to D, and price and value has no outcome yet.

**What not to do.** Do not set numeric targets before the prototype rounds, and do not let funding volume stand alone as the measure of success.

## Sources and confidence

Pages opened for this doc, as of October 4, 2026.

- [Outcomes vs. outputs](https://www.producttalk.org/outcomes-vs-outputs/), Teresa Torres: definitions, outcome types, common pitfalls; quotes Seiden's definition.
- [Opportunity solution trees](https://www.producttalk.org/opportunity-solution-trees/), Teresa Torres: the tree, its rules and team rhythm (dated December 2023, updated September 2026).
- [Book review: Outcomes Over Output](https://marcabraham.com/2019/06/27/book-review-outcomes-over-output-by-joshua-seiden/), Marc Abraham, 2019: Seiden's definition, magic questions and outcome-based roadmaps. A review, not the book itself.
- [What are outcome-driven UX metrics?](https://articles.centercentre.com/what-are-outcome-driven-ux-metrics/), Jared Spool, May 2025.
- [Why is outcome-led so tricky?](https://www.mindtheproduct.com/why-is-outcome-led-so-tricky/), Dave Martin, April 2023.
- [How to break free of the feature factory](https://www.mindtheproduct.com/break-free-feature-factory-john-cutler/), on John Cutler, August 2017.
- [The product outcomes formula](https://cutlefish.substack.com/p/tbm-4353-the-product-outcomes-formula), John Cutler, 2020.
- [Product vs feature teams](https://www.svpg.com/product-vs-feature-teams/), Marty Cagan, August 2019.
- [Outcome-Driven Innovation](https://en.wikipedia.org/wiki/Outcome-Driven_Innovation), Wikipedia: history and the opportunity formula.
- [Outcome-Driven Innovation: a critique on the quantification process](https://bradenbuchanan.substack.com/p/outcome-driven-innovation-a-critique), Braden Buchanan.
- [HEART framework](https://ixdf.org/literature/topics/heart-framework), Interaction Design Foundation: origin and limits. A secondary summary of the 2010 paper.
- [Consumer Duty implementation plans](https://www.fca.org.uk/publications/multi-firm-reviews/consumer-duty-implementation-plans), UK Financial Conduct Authority.

**Confidence.** High on what each author says, since those come from their own pages or close summaries. Medium on Seiden, which rests on a review and on Torres quoting him, not on the book. Low on effectiveness claims: nothing I found measures results rigorously.

**Not checked.** The origin of the output, outcome, impact chain in logic models; Goodhart's law; the publication year of Torres's book; Jeff Gothelf's Lean UX and OKR work, which belongs in this lineage but which I did not open. The original HEART paper and Seiden's book were not read directly.

**Gaps worth filling next.** Published case studies with numbers, any academic work on outcome-based product management, and US regulatory guidance comparable to the UK Consumer Duty.
