# Design harness

A design harness is the context, rules and checks that keep people and AI coding agents producing on-system, accessible UI. These three docs cover how to build one, using a generic case: a self-custody wallet built in Flutter and Material 3.

They sit apart from the SC-IA research. Nothing here feeds the claims, the scores or the decision log.

| # | Doc | What it covers |
| --- | --- | --- |
| 01 | [Design harness playbook](01-playbook-with-mcp.md) | Definitions, reference architecture, a Flutter and Material 3 adapter, guardrails, governance, financial-services considerations and tooling maturity. Assumes the team can use Claude Code and MCP |
| 02 | [Design harness without MCP](02-research-without-mcp.md) | The same goal when MCP and Claude Code aren't available: open-weight models (GLM 5.3) in OpenCode, GitHub Copilot credits and the Figma agent. Includes an addendum on Flutter's official and package skills |
| 03 | [Implementation spec pack](03-implementation-spec-pack.md) | Seven buildable specs, a 22-step runbook, a send-flow test plan, governance rules and ready-to-paste prompts for OpenCode, GitHub Copilot and the Figma agent |

Read 01 for the model, 02 for the evidence when MCP is off the table, and 03 to build.

The AI SDLC kit that used to sit here as `04-ai-sdlc-kit/` (templates, agents and skills for an agent-built delivery loop with UX gates) now lives in its own repository, `AI-SDLC`, under the same GitHub owner as this one.

## Notes

- Written on 7 November 2026. Models, prices and product features change fast, so check them before relying on any figure.
- Citations are inline links rather than SC-IA's source tags, because these docs are outside the competitive research. People appear by role only, as everywhere in this repo.
- Paths such as `docs/harness/` and `lib/features/` in 03 refer to the app repo the specs are written for, not to this repo.
