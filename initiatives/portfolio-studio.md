# Portfolio Studio
<text color="secondary" size="md">Product strategy exploration · Self-custody × Programmable finance × AI</text>

I think we should explore **Portfolio Studio as a new product category**, rather than start by designing another DeFi interface.

The opportunity is to rethink what a financial product can be when the user controls their assets, financial capabilities are available through programmable infrastructure, and a system can coordinate those capabilities around an outcome.

Your product would have two complementary surfaces:

- **The self-custody wallet:** where ownership, recovery, authentication, permissions and transaction authorization are managed.
- **Portfolio Studio:** where users understand their financial position, explore opportunities, compose strategies, define intents and decide how their assets should behave.

The key hypothesis is that the wallet protects the user's agency, while the Studio makes that agency useful.

## 1. The product thesis

<box border radius="xl" padding={4} gap={3}>
  <text color="secondary" weight="medium" size="sm">THE SHIFT</text>
  <title size="xl">From managing assets to programming financial outcomes.</title>
  Traditional financial interfaces primarily help users select products, manage positions and initiate transactions. Most crypto wallets help users manage keys, accounts, assets and on-chain actions.

  **Portfolio Studio would let users define an outcome, establish the boundaries within which it may be pursued, and compose the financial capabilities required to achieve it.**
  <divider />
  <grid columns={2} gap={3}>
    <grid-item>
      <text color="secondary" size="sm">What the user defines</text>
      **Intent, constraints and control**
    </grid-item>
    <grid-item>
      <text color="secondary" size="sm">What the system coordinates</text>
      **Assets, protocols and execution**
    </grid-item>
  </grid>
</box>

Consider the difference between these requests:

<box gap={2}>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} align="center" justify="center" size="44px">
      <icon name="arrow-left-right" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **Transaction**
      “Swap 500 USDC for ETH.”
      <text color="secondary" size="sm">One action with specified inputs and outputs.</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} align="center" justify="center" size="44px">
      <icon name="target" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **Intent**
      “I want to maintain a 30% allocation to ETH.”
      <text color="secondary" size="sm">A desired state that may require one or more actions.</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} align="center" justify="center" size="44px">
      <icon name="workflow" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **Programmable portfolio**
      “Maintain 30% ETH, keep 20% in liquid stablecoins, and use only approved protocols. Ask me before moving funds.”
      <text color="secondary" size="sm">A persistent objective, with conditions, policies and an authorization model.</text>
    </box>
  </row>
</box>

The third example is where the Studio gets interesting. The portfolio is not merely a collection of balances. It becomes a system of **desired states, rules, capabilities and permitted actions**.

## 2. What actually makes this different from existing financial products?

We should be rigorous here. Traditional finance already has discretionary mandates, model portfolios, automated rebalancing and rules-based investment products. Crypto also already has DeFi aggregators, automated position management, intent-based execution and smart accounts.

For example, ERC-7683 defines a common interface for cross-chain intent orders; DeFi Saver provides automated DeFi position management; and smart-account standards enable modular execution and authorization. These are important building blocks, but none of them alone defines the complete Portfolio Studio experience. 【turn605677search1】【turn448439search2】【turn448439search3】

The product opportunity is to **bring these capabilities together around the user's portfolio, intent and control model**.

<box border radius="xl" padding={3} gap={3}>
  <title size="lg">The differentiation stack</title>
  <row gap={3} align="start">
    <box background="surface-secondary" radius="md" size="42px" align="center" justify="center">
      <icon name="wallet" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **1. Self-custody — ownership and agency**

      The user controls the assets and retains explicit authority over the actions that may be performed.
    </box>
  </row>
  <row gap={3} align="start">
    <box background="surface-secondary" radius="md" size="42px" align="center" justify="center">
      <icon name="layers" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **2. Blockchain — programmable financial infrastructure**

      Assets, accounts and smart contracts can support programmable transfers, permissions and execution.
    </box>
  </row>
  <row gap={3} align="start">
    <box background="surface-secondary" radius="md" size="42px" align="center" justify="center">
      <icon name="puzzle" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **3. DeFi — composable capabilities**

      The product can combine supported primitives such as swaps, lending and staking into larger workflows.
    </box>
  </row>
  <row gap={3} align="start">
    <box background="surface-secondary" radius="md" size="42px" align="center" justify="center">
      <icon name="brain-circuit" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **4. Intelligence — context and coordination**

      AI and deterministic systems help interpret intent, find relevant capabilities, construct plans and monitor outcomes.
    </box>
  </row>
  <row gap={3} align="start">
    <box background="surface" border radius="md" size="42px" align="center" justify="center">
      <icon name="target" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **5. Intent — the user-facing abstraction**

      Users describe desired outcomes and boundaries, rather than needing to understand every protocol and transaction.
    </box>
  </row>
</box>

The differentiation is the combination, not any single layer.

### What blockchain enables, and what it doesn't

| Blockchain-native capability | Potential Studio opportunity | Important limitation |
|---|---|---|
| Programmable accounts | Scoped delegation, spending limits and execution policies | Permissions must be enforceable by the underlying account and protocol |
| Composable protocols | Combine supported financial actions into strategies | Composability can introduce dependencies and interconnected risks |
| On-chain settlement | Verify transaction results against an execution plan | Cross-chain workflows can involve separate transactions and failure states |
| Tokenized assets | Incorporate eligible tokenized funds, securities or other RWAs | Eligibility, transfer restrictions, redemption and legal rights vary |
| Publicly verifiable state | Explain asset positions and transaction outcomes | Transparency does not automatically establish safety or accurate valuations |
| Continuous markets | Monitor conditions and react outside traditional market hours | Availability is not equivalent to liquidity or reliable execution |

These distinctions matter. The World Economic Forum identifies programmability and composability as important tokenization opportunities, while also noting interoperability, regulatory and liquidity challenges. Research published by the Federal Reserve Bank of New York in January 2026 further examines how composability can create dependencies and liquidity risks across interconnected protocols. 【turn605677search7】【turn605677search5】

**The Studio should expose the advantages of programmable finance without pretending those advantages eliminate financial or operational risk.**

---

## 3. The core architecture: five layers

I would define Portfolio Studio around five distinct concepts. This is more important than deciding how many navigation items it needs.

<box border radius="xl" padding={3} gap={2} align="center">
  <box background="surface-secondary" radius="lg" padding={3} width="100%" align="center" gap={1}>
    <title size="lg">01 · Portfolio state</title>
    <text textAlign="center" size="sm">What I own, where it lives and what it is doing.</text>
    <text color="secondary" size="xs" textAlign="center">Assets · Accounts · Positions · Liquidity · Exposure</text>
  </box>
  <icon name="arrow-down" color="secondary" size="lg" />
  <box background="surface" border radius="lg" padding={3} width="100%" align="center" gap={1}>
    <title size="lg">02 · Intent</title>
    <text textAlign="center" size="sm">What I want my portfolio to achieve.</text>
    <text color="secondary" size="xs" textAlign="center">Goals · Desired state · Conditions · Priorities</text>
  </box>
  <icon name="arrow-down" color="secondary" size="lg" />
  <box background="surface" border radius="lg" padding={3} width="100%" align="center" gap={1}>
    <title size="lg">03 · Strategy composition</title>
    <text textAlign="center" size="sm">Which capabilities could achieve the outcome?</text>
    <text color="secondary" size="xs" textAlign="center">Protocols · Primitives · Alternatives · Execution plan</text>
  </box>
  <icon name="arrow-down" color="secondary" size="lg" />
  <box background="surface" border radius="lg" padding={3} width="100%" align="center" gap={1}>
    <title size="lg">04 · Authorization and policy</title>
    <text textAlign="center" size="sm">What is the system allowed to do?</text>
    <text color="secondary" size="xs" textAlign="center">Limits · Allowlisted actions · Approval rules · Expiry</text>
  </box>
  <icon name="arrow-down" color="secondary" size="lg" />
  <box background="surface-secondary" radius="lg" padding={3} width="100%" align="center" gap={1}>
    <title size="lg">05 · Execution and observation</title>
    <text textAlign="center" size="sm">What happened, and did we achieve the intended outcome?</text>
    <text color="secondary" size="xs" textAlign="center">Sign · Execute · Verify · Monitor · Explain</text>
  </box>
</box>

AI may help across several layers, but the authorization rules and execution verification should not depend on an AI model simply behaving correctly.

### A distinction worth preserving

An **intent** is not a strategy.

- **Intent:** Keep a defined amount liquid while seeking yield on eligible assets.
- **Strategy:** Allocate a specified amount to a selected lending market, subject to defined conditions.
- **Policy:** Do not exceed a spending limit; use approved contracts; require approval for withdrawals or other sensitive actions.
- **Execution plan:** The exact sequence of transactions, amounts, contracts and expected results.

Separating these objects makes the experience easier to explain, test, audit and extend.

---

## 4. What would users actually do in Portfolio Studio?

I would build the desktop app around four major experiences.

<box gap={3}>
  <row gap={3} align="start">
    <AsyncImage query="modern dark fintech portfolio analytics desktop dashboard multi asset allocation interface" aspectRatio="4:5" width="112px" radius="lg" />
    <box flex="1" gap={1}>
      **A. Portfolio Intelligence**

      A unified view across supported wallets, chains, assets and positions.

      The important shift is from displaying token balances to explaining the portfolio: liquidity, asset exposure, deployed capital, obligations and how positions relate to active intents.

      <text color="secondary" size="sm">Primary question: “What is happening with my assets?”</text>
    </box>
  </row>
  <divider color="subtle" />
  <row gap={3} align="start">
    <AsyncImage query="modern financial planning goal configuration interface desktop app target allocation risk constraints" aspectRatio="4:5" width="112px" radius="lg" />
    <box flex="1" gap={1}>
      **B. Intent Builder**

      A guided way to define what the user wants to achieve. Users can start with templates, configure structured controls, or describe an objective conversationally.

      The Studio translates the input into an explicit intent specification that the user can inspect and edit.

      <text color="secondary" size="sm">Primary question: “What do I want my assets to do?”</text>
    </box>
  </row>
  <divider color="subtle" />
  <row gap={3} align="start">
    <AsyncImage query="DeFi strategy builder visual workflow canvas smart contract financial operations nodes desktop interface" aspectRatio="4:5" width="112px" radius="lg" />
    <box flex="1" gap={1}>
      **C. Strategy Composer**

      The Studio presents compatible capabilities and strategies, explains trade-offs, and shows how an intent might be implemented.

      Advanced users can inspect protocol choices and execution steps; less experienced users can work at the outcome level.

      <text color="secondary" size="sm">Primary question: “How could I achieve this?”</text>
    </box>
  </row>
  <divider color="subtle" />
  <row gap={3} align="start">
    <AsyncImage query="crypto wallet transaction simulation review security permissions approval summary interface desktop fintech" aspectRatio="4:5" width="112px" radius="lg" />
    <box flex="1" gap={1}>
      **D. Control Center**

      Users inspect active intents, pending proposals, granted permissions, execution history and conditions requiring attention. They can pause or revoke permissions where the underlying system supports it.

      <text color="secondary" size="sm">Primary question: “What is allowed to happen, and what has happened?”</text>
    </box>
  </row>
</box>

These experiences should be connected rather than isolated sections. A change in portfolio state might prompt an intent review; an intent might produce a proposed strategy; an execution might change the portfolio state.

---

## 5. A concrete example: “Put my idle assets to work”

Imagine a user has ETH and USDC across supported accounts.

They open Portfolio Studio and say:

> “I want my idle USDC to earn yield, but I need to keep enough liquid for unexpected expenses. I don't want any borrowing or leveraged positions.”

### The experience

<list connector="solid" marker="number" gap={3}>
  <list-item>
    **Understand the intent**

    The Studio identifies the objective as yield generation, alongside liquidity and no-borrowing constraints. It asks how much must remain liquid rather than guessing.
  </list-item>
  <list-item>
    **Evaluate the portfolio**

    It identifies eligible assets and balances, relevant account and network constraints, and existing positions. It distinguishes confirmed facts from estimates.
  </list-item>
  <list-item>
    **Present alternatives**

    It compares eligible strategies using evidence such as yield methodology, liquidity conditions, contract risk, fees and exit requirements. It explains trade-offs rather than returning a single opaque recommendation.
  </list-item>
  <list-item>
    **Simulate the plan**

    The user sees what would move, where it would go, what permissions are required, the expected costs and the conditions that could prevent execution.
  </list-item>
  <list-item>
    **Authorize the action**

    The desktop prepares the plan. The wallet independently presents the critical transaction details through the user's chosen authorization mechanism.
  </list-item>
  <list-item>
    **Monitor the result**

    The Studio tracks the resulting position, reports meaningful changes and tells the user whether the original intent remains satisfied. Any subsequent action follows the configured authorization policy.
  </list-item>
</list>

The powerful part is that the user shouldn't have to learn a protocol first. They should be able to explore the protocol as part of understanding the proposed solution.

---

## 6. The most important product decision: how autonomous should it be?

Intent-based UX and autonomous execution are two different decisions. I would make the first work before introducing the second.

<box border radius="xl" padding={3} gap={3}>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align="center" justify="center">
      <icon name="eye" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **Level 1 · Observe**

      Understand the portfolio and identify when an intent is no longer satisfied. No transaction authority is granted.
      <badge color="secondary">Best starting point</badge>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align="center" justify="center">
      <icon name="file-check" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **Level 2 · Propose**

      Construct and simulate an execution plan. The user reviews and explicitly authorizes each action.
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align="center" justify="center">
      <icon name="shield-check" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **Level 3 · Delegate within limits**

      Permit specific operations within enforceable spending caps, approved destinations, time windows and other policies.
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" size="44px" align="center" justify="center">
      <icon name="refresh-cw" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **Level 4 · Maintain an outcome**

      Allow eligible actions to occur in response to persistent conditions, with monitoring, revocation and clear exception handling.
    </box>
  </row>
</box>

Programmable accounts and delegated permissions make parts of this model technically possible today. For example, Ethereum's account-abstraction work describes more flexible account management, while Solana's spend permissions support bounded token delegation. The availability and enforcement of each policy will nevertheless depend on the chain, account implementation and operation involved. 【turn605677search8】【turn605677search12】

For your product, I would begin with **Observe → Propose → User approves**. That proves the portfolio-intent model without requiring the first release to solve unrestricted agentic execution.

---

## 7. How this fits your existing self-custody architecture

I would not replace the wallet, asset or account model. I would introduce a higher-level portfolio abstraction that uses it.

<box border radius="xl" padding={3} gap={2} align="center">
  <box background="surface-secondary" radius="lg" padding={3} width="100%" align="center" gap={1}>
    <title>Portfolio Studio · Desktop</title>
    <text color="secondary" size="sm" textAlign="center">Understand · Define intents · Compose · Simulate · Monitor</text>
  </box>
  <icon name="arrow-down-up" color="secondary" size="lg" />
  <box border radius="lg" padding={3} width="100%" align="center" gap={1}>
    <title>Portfolio and intent model</title>
    <text color="secondary" size="sm" textAlign="center">Desired state · Strategies · Constraints · Proposals · Policies</text>
  </box>
  <icon name="arrow-down-up" color="secondary" size="lg" />
  <grid columns={2} gap={2}>
    <grid-item>
      <box background="surface" border radius="lg" padding={3} gap={1} align="center">
        <icon name="smartphone" size="xl" />
        **Mobile wallet**
        <text textAlign="center" color="secondary" size="sm">Verify · Authorize · Sign · Recover</text>
      </box>
    </grid-item>
    <grid-item>
      <box background="surface" border radius="lg" padding={3} gap={1} align="center">
        <icon name="cpu" size="xl" />
        **Execution services**
        <text textAlign="center" color="secondary" size="sm">Resolve · Simulate · Execute · Verify</text>
      </box>
    </grid-item>
  </grid>
  <icon name="arrow-down" color="secondary" size="lg" />
  <box background="surface-secondary" radius="lg" padding={3} width="100%" align="center" gap={1}>
    <title>Existing ownership and account foundation</title>
    <text color="secondary" size="sm" textAlign="center">Recovery and authorization · Wallets · Chain accounts · Assets</text>
  </box>
  <text color="secondary" size="xs" textAlign="center">Conceptual architecture, not a prescribed technical implementation.</text>
</box>

This preserves an important separation: the Studio can create a plan, but it does not get to redefine what the owner has authorized. Signing, recovery and any delegated capabilities remain governed by the actual wallet and account mechanisms.

It also supports a gradual evolution from your current **App → Wallets → Assets → Accounts** structure. The portfolio layer can aggregate those entities without pretending that an ERC-20 token on Ethereum is necessarily a separate blockchain account or that every asset supports the same operations.

---

## 8. What should the first MVP prove?

I would resist starting with “all DeFi options.” The breadth is attractive as a long-term vision, but it risks producing a large catalogue of protocols rather than a coherent product experience.

The first version should prove that a user can move from an understandable intent to a transparent, trustworthy execution proposal.

<box gap={2}>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" padding={2} align="center" justify="center" size="40px">
      <icon name="layout-dashboard" size="lg" />
    </box>
    <box flex="1" gap={1}>
      **Portfolio context**

      Read the supported asset/account state and explain what is available, deployed or reserved.
    </box>
  </row>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" padding={2} align="center" justify="center" size="40px">
      <icon name="list-check" size="lg" />
    </box>
    <box flex="1" gap={1}>
      **Two or three intent templates**

      For example, “maintain a target allocation,” “keep a liquidity reserve” and “explore eligible yield opportunities.” Templates should initially generate explicit proposals, not silently trigger transactions.
    </box>
  </row>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" padding={2} align="center" justify="center" size="40px">
      <icon name="git-compare" size="lg" />
    </box>
    <box flex="1" gap={1}>
      **One real capability integration**

      Select a single well-supported operation to demonstrate the full cycle: eligibility check, proposal, simulation, approval, execution and outcome verification. Keep unsupported chains and protocols out of the execution path.
    </box>
  </row>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" padding={2} align="center" justify="center" size="40px">
      <icon name="history" size="lg" />
    </box>
    <box flex="1" gap={1}>
      **Intent history and control**

      Show active, completed, failed and paused intents; what was authorized; what happened; and why the system did or did not proceed.
    </box>
  </row>
</box>

For the first PoC, even the execution stage could be simulated. Then the next iteration could add one real operation on a supported network, subject to the wallet's actual signing and safety capabilities.

### How I would judge success

Not just by swaps executed or protocols integrated. I would measure whether users can:

- Express an objective without knowing the underlying blockchain mechanics.
- Understand and correct the intent the system has inferred.
- Explain the risks, constraints and permissions associated with the proposed plan.
- Predict what will happen before authorization.
- Verify what happened afterward and retain confidence in control of their assets.

---

## 9. The strategic questions worth researching next

The concept now raises a set of fundamental product questions.

| Question | Why it matters |
|---|---|
| **What is a portfolio?** | A visual aggregation of balances, a set of accounts, or a programmable collection of positions and intentions? |
| **What is an intent?** | A one-off request, a persistent desired state, a rule, or a combination of these? |
| **What does the user delegate?** | Viewing, planning, transaction construction, signing, or restricted execution authority? |
| **How are strategies composed?** | From curated capabilities, a permissioned marketplace, protocol integrations or an open solver ecosystem? |
| **How does the Studio handle risk?** | Can users understand liquidity, smart-contract, bridge, oracle, counterparty and tokenization risks before acting? |
| **How does it incorporate RWAs?** | Which tokenized assets are actually accessible, transferable and redeemable through the user's wallet and jurisdiction? |

My strongest recommendation is to investigate the first three together: **portfolio, intent and authorization**. They determine the mental model of the entire product. Protocol discovery and the strategy catalogue can evolve on top of that foundation.

The central hypothesis I would carry forward is:

> **Portfolio Studio is a user-controlled environment for defining financial outcomes, composing programmable digital-asset capabilities and governing how those capabilities may be executed.**

That positions it beyond a wallet dashboard or a DeFi aggregator. It also gives your mobile wallet a clear role: preserving the user's ownership and authority as the desktop environment becomes more capable.

The real design challenge is not making complex finance look simpler. It is making **complex financial behavior understandable, inspectable and controllable**.