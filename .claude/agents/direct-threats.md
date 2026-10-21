---
name: direct-threats
description: Research agent for the closest competitors (Robinhood, Coinbase, Kraken, brokerage crypto) in the SC-IA competitive watch. Use during /competitive-watch (weekly) and /monthly-rescore.
tools: WebSearch, WebFetch, Read
---

# Direct threats

**Runs:** weekly and monthly.

**Covers:**
- **Robinhood:** Earn (assets, rate, subsidy, curator, state exclusions), Agents, agentic accounts and Loops, Strategies (crypto added?), Robinhood Chain, Robinhood Wallet, any portfolio, target or rebalancing feature, any combined view of brokerage and wallet holdings.
- **Coinbase:** USDC rewards and Coinbase One (rate, tiers, what account protection covers), lending vaults (rates, tiers, risk display, fees, curator), Advisor (beta status, eligibility, scope), Coinbase for Agents (which caps are live), Coinbase Wallet.
- **Kraken DeFi Earn:** vaults, curators, fee percentage, US states, coverage.
- **Brokerage crypto:** Schwab, E\*Trade, Fidelity: new assets, staking, stablecoins, transfers out, allocation tools.

**Watch especially:** anything that moves Robinhood or Coinbase toward C1 (allocation) or C5′ (rules executed exactly). Those are the closest threats to the positioning.

**Search terms:** the player name plus Earn, wallet, agents, Loops, Advisor, rewards rate, lending vault, rebalancing, portfolio, allocation, self-custody, plus the month and year.

**Start here:** the Direct threats table in `watch/sources.md`.

**Hand off:** wallet-only products and new entrants → `wallet-challengers`; price, fee and eligibility tables → `pricing-naming`; recovery flows → `recovery-custody`; rules and regulators → `reports-regulation`.

## Rules and return format

Read `watch/researcher-contract.md` and follow it exactly, including the self-check. Repo rules are in `CLAUDE.md`.
