# AI SDLC templates with UX gates (stack-agnostic)

Templates for a delivery loop where agents write most of the code and people approve at gates. They work with any stack and any agent host (OpenCode, GitHub Copilot, Claude Code, Spec Kit).

- **Structure:** Anthropic's AI-native SDLC playbook (intent → spec → plan → review) and GitHub Spec Kit's templates (constitution, spec, plan, tasks). Spec Kit's mandatory section names are kept, so these can replace its templates.
- **What's added:** neither source has UX gates, user evidence or accessibility. This pack adds them, following NN/g's "The Role of UX in Agentic Software Factories" (October 2026).
- **Agents and skills:** three agent roles (planner, builder, reviewer) for OpenCode, GitHub Copilot and Claude Code, and the five skills they load.

Fill the `{{placeholders}}` in `constitution.md`, `ux-risk.yaml` and the agent files once per product. The other templates are filled once per change.

## Files

| File | Copy to | Written by | Approved by | Executor reads it? |
|---|---|---|---|---|
| constitution.md | `.harness/constitution.md` (Spec Kit: `.specify/memory/constitution.md`) | Design + eng leads | Leads, by PR | No |
| ux-risk.yaml | `.harness/ux-risk.yaml` | Design lead | Design + platform eng | Classifier only |
| intent-template.md | `.harness/templates/` | Originator, with AI | Product + design | No |
| spec-template.md | `.harness/templates/` (Spec Kit: `.specify/templates/`) | AI, from the intent | Product; design for the UX section | No |
| plan-template.md | same | Frontier planner | Engineer | **Yes** |
| tasks-template.md | same | Planner | Engineer | **Yes** |
| review-template.md | repo root as `REVIEW.md` | Tech lead + design | Code owners | Reviewer only |
| ux-escalation-template.md | `.harness/templates/` | Agent, when it stops | Design | No |
| research-trigger-template.md | `.harness/templates/` | Monitoring / analytics | Research triages | No |
| insight-template.md | `research/insights/_template.md` | Research | Research | Planner only |

Only the plan and tasks reach the executor. Keep them short: together with AGENTS.md and the loaded skill, stay under about 30 active rules. Everything else is for people, planners and reviewers.

## The loop

1. **Intent** (`.harness/intents/<slug>.md`). A user problem with evidence. Product and design co-approve. Researchers can file problem-only intents.
2. **Spec** (`.harness/specs/<slug>.md`). Stories, UX, requirements and success criteria. Design approves the UX section.
3. **Plan and tasks** (`.harness/plans/<slug>.md`, `.harness/tasks/<slug>.md`). What the executor reads.
4. **Build and verify.** The executor runs the proof commands. Two repair rounds, then a stuck report.
5. **UX risk check.** The classifier labels the diff `none`, `review` or `test`. Anything above `none` stops the agent, which writes an escalation file.
6. **Review.** AI review runs the passes in `REVIEW.md`. It can raise UX flags but never clear them. People approve.
7. **Maintain.** Technical alerts become intents. User-failure signals become research triggers, not intents.

## Agents and skills

Three agents run the loop. Each one loads a skill for the step it is on, so the agent files stay short and the know-how lives in skills every host can read.

| Agent | Model | Can edit | Loads | Never |
|---|---|---|---|---|
| planner | Frontier | `.harness/intents/`, `specs/`, `plans/`, `tasks/` | `intent-author`, `spec-writer`, `plan-writer` | Writes code, marks a document accepted, invents evidence |
| builder | Cheaper or open-weight | Source code, except protected paths | The build skill the plan names, `ux-escalate` | Updates visual baselines, edits protected paths, judges UX |
| reviewer | Frontier, fresh session | `.harness/ux-escalations/` only | `ux-review` | Approves, edits code, says the UX is fine |

No agent decides UX risk. A script classifies the diff and a person decides. Write the build skill yourself, because it depends on the stack, for example "migrate a screen to tokens".

| Folder in this pack | Copy to |
|---|---|
| `skills/` | `.agents/skills/` (OpenCode, GitHub Copilot, Codex) and `.claude/skills/` (Claude Code). Keep the two copies identical |
| `agents/opencode/` | `.opencode/agents/` |
| `agents/github-copilot/` | `.github/agents/` |
| `agents/claude-code/` | `.claude/agents/` |

The skills are project-agnostic. They read `.harness/constitution.md` and the templates for every rule, so the same five skills work for any product.

**Enforcement differs by host.**
- OpenCode agent files limit edit paths and shell commands directly. They use the V1 `permission:` and `steps:` fields, which OpenCode 2 still reads but marks as deprecated.
- GitHub Copilot agent files limit only tool types (read, search, edit, execute). Path limits need a `preToolUse` hook, CODEOWNERS and a CI protected-path check.
- Claude Code agent files limit tools. Path limits need hooks in `.claude/settings.json`.
- On every host, CODEOWNERS and CI are the backstop, because a shell command can get around an edit deny.

**Check before use.** Tool names and model names in `agents/github-copilot/` vary between VS Code, the Copilot CLI and the cloud agent. Match them to what your surface shows.

## Wire-up

AGENTS.md needs one stop rule, not a section of UX rules:

```
## Stop rule
- Same check fails twice: write .harness/stuck/<slug>.md and stop.
- `{{ux_risk_command}}` prints anything but `none`: write
  .harness/ux-escalations/<slug>.md from the template and stop.
```

CODEOWNERS:

```
/.harness/constitution.md   {{design-lead}} {{eng-lead}}
/.harness/ux-risk.yaml      {{design-lead}}
/.harness/intents/          {{product-owner}} {{design-lead}}
/.harness/templates/        {{design-lead}}
/.agents/skills/            {{design-lead}} {{eng-lead}}
/REVIEW.md                  {{tech-lead}} {{design-lead}}
/research/insights/         {{research-lead}}
{{visual-baseline-path}}    {{design-lead}}
```

In branch protection or CI, require design approval when a PR carries the `ux-risk:review` or `ux-risk:test` label.

The classifier is a small script you write once. It reads `ux-risk.yaml`, inspects the diff and prints one class. Start with path rules, which are reliable, then add change detectors.

## Why the defaults are set this way

- Automated accessibility checks catch most issues by volume but only about a third of WCAG A/AA success criteria (Deque, vendor study). Hence a manual pass for `test` changes.
- Multimodal models judge visual quality well but overrate usability from static screens (Springer benchmark, 1,000 screens). Hence "AI raises flags, people clear them."
- Pre-built components gave higher design-system compliance than style guides in context or as instructions (CHI EA '26). Hence "rules live in code."
- Instruction-following drops as instruction count rises, mostly through omission (IFScale preprint). Hence the 30-rule executor budget.
- Small tests with 3–5 users are cited as acceptable good practice for checking customer understanding (FCA consumer understanding review, March 2026).
