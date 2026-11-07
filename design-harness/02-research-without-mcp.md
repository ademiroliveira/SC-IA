# Steer the wallet harness with checks, not prose

A team can run a credible design harness for a Flutter wallet without MCP or Claude Code. This report takes a generic case: a self-custody wallet built in Flutter and Material 3, a team that can't use MCP or Claude Code, open-weight models (GLM 5.3 and a Flash model) hosted in-house and run in OpenCode, and a small GitHub Copilot budget for frontier models. It has to be built around deterministic checks rather than instructions, because the models doing most of the work follow prose less reliably than the frontier models the earlier playbook assumed. **GLM 5.3 now matches or beats Claude Opus 4.8 on classic agentic-coding benchmarks, but trails it by 12 points on SkillsBench**, the closest proxy for "follows skills and AGENTS.md". There is also **no published evidence of any GLM model writing Flutter**. "Flash" is most likely GLM-5.3-Flash, a strong 320B model that can also read images, but it could be a far weaker 30B model, and that changes what it can be trusted with. So the harness should keep the active rule set to roughly 10–30 instructions per task and invoke skills by name. The Dart analyzer plugin, an audit script and golden tests should do the teaching, with two repair rounds before escalation. **An example budget of 4,000 GitHub Copilot credits is about US$40 of tokens, roughly 20 full Opus 5.5 agent sessions or several hundred short "stuck-report" consultations.** Spend them on writing skills and lint messages, planning new screens, unblocking stuck runs and reviewing protected screens, not on routine edits. OpenCode and GitHub Copilot can share one AGENTS.md and one `.agents/skills/` folder, but agents, hooks and permissions must be written per host, and whether the team runs OpenCode V1 or V2 changes how lint feedback reaches the model. In Figma, use the agent to audit, name and rebind. Create the M3 reference/system/extended variables with Figma's native DTCG import, or with a plugin the agent builds once, on a branch. Neither route needs the Enterprise-only REST API. The agreed plan holds; the main changes are a "week 0" serving check, a cheaper baseline design, pulling the analyzer plugin forward, and moving Figma token creation from the agent to deterministic import.

## GLM 5.3 is near-frontier on benchmarks and unproven on Flutter

GLM 5.3 is a real, current model. Z.ai opened API access in August 2026 and released open weights on 29 August. It is a text-only mixture-of-experts model of about **744–753B total and 40B active parameters with a 1M-token context** ([Gigazine](https://gigazine.net/gsc_news/en/20260829-glm-5-3-open/); [Hugging Face](https://huggingface.co/zai-org/GLM-5.3)). On Vals AI's independent harness it beats Claude Opus 4.8 on SWE-bench (**95.4% vs 88.6%**) and Terminal-Bench 4.0 (38.9% vs 23.2%). It trails on LiveCodeBench (80.5% vs 87.8%), on Vibe Code Bench app-building (78.1% vs 82.7%) and, most importantly for a skills-driven harness, on **SkillsBench (47.5% vs 59.2%)** ([Vals AI](https://www.vals.ai/comparisons/anthropic_claude-opus-4-8-vs-zai_glm-5.3)). Z.ai's own table puts it 5–6 points behind GPT-5.6 Sol on the hardest long-horizon tests, for example Terminal-Bench 3.0 at 28.3 vs 34.6 ([Hugging Face](https://huggingface.co/zai-org/GLM-5.3)). No source compares GLM 5.3 with the models a GitHub Copilot budget actually buys (Opus 5.5, Sonnet 5.5, GPT-6 Sol). The gap to those is therefore unmeasured, and it is probably wider than the Opus 4.8 comparison suggests.

"Flash" needs identifying before anything is assigned to it. The likeliest candidate is **GLM-5.3-Flash: 320B total / 18B active, natively multimodal (image and text in), MIT-licensed** ([Hugging Face](https://huggingface.co/zai-org/GLM-5.3-Flash)). On bounded tasks it keeps 90–100% of GLM 5.3's score (SWE-bench 92.0 vs 95.4). On the long-horizon FrontierSWE v2 it drops to **18.1 vs 30.2** ([BenchLM](https://benchlm.ai/md/compare/glm-5-3-vs-glm-5-3-flash.md); aggregator, provenance not stated). That makes it fine for scoped edits and risky for multi-step refactors. If the in-house "Flash" is instead the older GLM-4.7-Flash (30B total, about 3B active), it sits in a much weaker tier ([Hugging Face](https://huggingface.co/zai-org/GLM-4.7-Flash)). The modality difference has a direct design consequence. GLM 5.3 "cannot inspect screenshots or design files directly" ([SiliconFlow](https://www.siliconflow.com/ja/blog/glm-5-3-coding-use-cases)), so **only a multimodal Flash or a frontier model can look at a rendered golden**.

There is no Flutter-specific evidence for any GLM model. The Flutter team's FlutterBench page still says "Coming soon" ([Flutter docs](https://docs.flutter.dev/ai/flutter-bench)), and Z.ai has not published a knowledge cutoff ([SiliconFlow](https://www.siliconflow.com/ja/blog/glm-5-3-coding-use-cases)). The model-agnostic evidence on AI-written Flutter shows a consistent pattern. A hands-on test found tools defaulting to older Riverpod providers, writing a `ThemeExtension` without `copyWith` and `lerp` until the analyzer flagged it, and repeatedly missing `dispose` ([vibecodemeta](https://vibecodemeta.pages.dev/blog/best-ai-coding-tools-for-flutter-2026)). Flutter developers single out the `withOpacity`-instead-of-`ColorScheme` habit as "the biggest problem" ([r/FlutterDev](https://reddit.sentinel-team.org/posts/1qhxc64/snapshots/2026-01-21T00%3A21%3A10.577712Z)). Expect GLM to write pre-`material_ui`, pre-M3 idioms unless the analyzer stops it.

Operational failure modes matter as much as raw capability. GLM 5.3 is slow and verbose. Artificial Analysis measured **31.7 minutes per index task against a 13.6-minute median, with about 100 seconds to the first answer token** ([Artificial Analysis](https://artificialanalysis.ai/models/glm-5-3)), and its reasoning cannot be switched off ([SiliconFlow](https://www.siliconflow.com/ja/blog/glm-5-3-coding-use-cases)). Users of the predecessor GLM-5.1 reported output breaking down at **100–120K tokens**, far below the advertised window, and quantized serving produced flipped logic and stray Chinese characters ([HN](https://hn.markojs.workers.dev/story/47677853)). GLM-5 thinking variants emitted malformed tool-call JSON in OpenCode, causing loops ([OpenCode #13982](https://github.com/anomalyco/opencode/issues/13982)). vLLM crashes or hangs when `tool_choice: "required"` meets its MTP speculative decoding ([Hugging Face](https://huggingface.co/nvidia/GLM-5.2-NVFP4/discussions/7)). The harness itself also moves results. One vendor ran the same GLM-5.2 on Terminal-Bench 2.1 at **72.6% in its own harness and 59.8% in OpenCode**, a directional, uncontrolled comparison ([Kimchi](https://kimchi.dev/blog/same-model-different-harness-terminal-bench)). The practical stance follows. Treat GLM 5.3 as the default executor for scoped, machine-verified work. Configure an effective context of about 128K rather than 1M, keep sessions short, and fix the serving setup before running any baseline.

## Write for omission: few rules, named skills, red-green gates

### Keep the active rule set under thirty

The strongest evidence on instruction design is about counting. In IFScale, frontier models stayed near perfect at 50 simultaneous instructions (claude-sonnet-4 98%). Smaller models collapsed: claude-3.5-haiku fell to 78% and llama-4-scout to **54%**. They failed mainly by **silently omitting** instructions rather than misapplying them ([arXiv 2507.11538](https://arxiv.org/html/2507.11538v1)). AGENTS.md, the loaded skill and the task prompt all count against that budget, so aim for about **10–30 active instructions per task**. Put the three or four non-negotiables first, because early instructions are followed better.

The planned ~100-line AGENTS.md matches what OpenAI's harness team uses: a file that "serves as a map", pointing to deeper docs (OpenAI's harness-engineering post, read through a secondary summary). Vercel's evals add the key twist on what goes inside it. A **compressed docs index in AGENTS.md scored 100%**. A skill left to auto-trigger scored 53%, because it was never invoked in 56% of runs. Explicit instructions to use the skill raised that to 79% ([Vercel](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)). For the wallet, AGENTS.md should therefore hold five things:

- a pipe-delimited **token index** mapping each literal pattern to its replacement (`Color(0x…)` → `colorScheme.<role>`, `EdgeInsets.all(n)` → `context.space.<step>`, `TextStyle(fontSize:)` → `textTheme.<slot>`, gain/loss colours → the wallet `ThemeExtension`);
- the exact verify commands;
- the protected paths;
- a skill index stating when to load each skill;
- a stop rule.

Everything else goes into skills and reference files.

### Invoke skills by name and write them at "Haiku level"

The Agent Skills spec is small:

- `name` up to 64 lowercase-hyphen characters, matching the folder name;
- `description` up to 1,024 characters, saying what the skill does and when to use it;
- body ideally under 500 lines;
- `scripts/` and `references/` one level deep, loaded on demand ([agentskills.io](https://agentskills.io/specification)).

Anthropic's authoring guidance says weaker models need more detail ("What works perfectly for Opus might need more detail for Haiku"). It recommends a copyable checklist, low-freedom exact commands for fragile steps, one default approach instead of options, and the gate "**Only proceed when validation passes**" ([Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)).

Each wallet skill (audit, migrate screen, build screen first; golden tests and diff review later) should hold four things:

- a 5–8 step checklist the model copies and ticks;
- a "Done when" block listing the commands that must pass;
- a PR-summary template;
- a pointer to one canonical before/after migrated screen in `references/`.

Do not rely on auto-triggering. Load skills explicitly with an at-mention of the skill id in OpenCode or a command bound to an agent, and with `/skill-name` in GitHub Copilot ([OpenCode Skills](https://opencode.ai/docs/skills/); [GitHub Docs](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-skills)). Anthropic also says to **write the evals before the skill**: run the model without it, record the failures, and write the minimum instructions that fix them ([Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)).

### Make the analyzer the teacher

Deterministic feedback is where weaker models gain the most. With a compiler-error loop, a 4B model's compile success rose from **18% to 97.4%**, beating a 70B model's unaided 92% ([arXiv 2601.12146](https://arxiv.org/html/2601.12146v1)). Across models, **two repair rounds captured 76–95% of the achievable gain**. Logic and assertion failures were repaired only about 45% of the time, and an 8B model fixed only about 30% of its own failures ([alphaXiv 2604.10508](https://www.alphaxiv.org/abs/2604.10508.md)).

That evidence maps directly onto the plan. Dart 3.10 analyzer plugins surface custom rules in `dart analyze` and `flutter analyze`, which means both hosts can run them without LSP or MCP. Plugin rules are **off by default** and must be enabled under the plugin's `diagnostics` key ([dart.dev](https://dart.dev/tools/analyzer-plugins)). Write every message as a fix instruction ("Hardcoded `Color(0xFF1A73E8)`. Use `Theme.of(context).colorScheme.primary`. See docs/tokens.md#color"), as OpenAI's team did with its linters (OpenAI's harness-engineering post, read through a secondary summary).

Make the audit script emit a JSON worklist (file, line, literal, suggested token), so migrations follow plan → validate → edit → verify. Golden failures behave like logic errors, so **a cheap model must never regenerate goldens**; it would "fix" the test instead of the UI. Allow two repair rounds. If the same check then fails twice, the agent writes a short stuck report (task, diff, failing output, what it tried) and stops.

## Spend frontier credits on words that get reused

GitHub Copilot no longer counts "premium requests" for Business and Enterprise. Since 1 June 2026, usage is billed in **AI credits worth US$0.01 each, metered by input, output and cached tokens**. Business includes 1,900 credits per user per month and Enterprise 3,900, pooled. "Paid usage" is on by default, and there is **no automatic fallback to a cheaper model** ([GitHub Docs](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises)). Per million tokens, Opus 5.5 costs $4 in and $20 out, Sonnet 5.5 and GPT-6 Sol $2/$10, and Haiku 5.5 and GPT-6 Luna $0.10/$0.50. Opus 5.5 is cheaper than Opus 4.8 ($5/$25) ([GitHub Docs](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)).

For a mid-sized agent session (25 model calls, 60K-token prompts, 90% cache hits), the published rates work out to about **177 credits on Opus 5.5, 89 on Sonnet 5.5, 102 on GPT-6 Sol and 5 on Haiku 5.5 or GPT-6 Luna**. These are estimates from the prices above. A 4,000-credit month is therefore about 22 Opus sessions. A short advisor-style consultation (a 20K-token stuck report in, a 700-token plan out) costs about **10 credits on Opus 5.5**, so the same month buys roughly 400 of them.

The evidence favours exactly that shape. In Anthropic's advisor pattern a cheap executor does the work and consults a stronger model only at hard decisions, receiving a 400–700-token plan. **Haiku with an Opus advisor scored 41.2% vs 19.7% solo** on BrowseComp, at 85% lower cost per task than Sonnet alone ([Claude blog](https://claude.com/blog/the-advisor-strategy)). Predictive routers, by contrast, fail under task shift: on RouterBench no routing algorithm significantly beat a no-router baseline (an academic review of routing and cascade research). So route by task type, and escalate only when a check fails. Use a separate model or fresh context as reviewer, because agents "reliably skew positive when grading their own work" ([Anthropic Engineering](https://anthropic.com/engineering/harness-design-long-running-apps)).

| Task | Runs on | Escalate or judge |
|---|---|---|
| Find violations | `ds_audit` script, no model | — |
| Swap listed literals for tokens | Flash | GLM 5.3 after 2 failed rounds |
| Migrate a normal screen | GLM 5.3 | Frontier advisor via stuck report |
| Build screen from contract | Frontier writes short spec; GLM 5.3 builds | Frontier reviews diff |
| Golden and a11y tests | GLM 5.3 | Human approves new images |
| Protected-screen token change | GLM 5.3 | Frontier review + human + goldens |
| Skills, AGENTS.md, lint messages | Opus 5.5 | Eval suite decides |
| Visual triage of golden diffs | Flash if multimodal, else frontier | Human |

GitHub's own guidance matches this: plan with a strong model, then implement with a cheaper one **in a new session**. Don't switch models mid-session, because that invalidates the cache. Set a CLI session credit limit so a runaway loop stops cleanly ([GitHub Docs](https://docs.github.com/copilot/tutorials/optimize-ai-usage)). The handoff between hosts has to be a written file. A GitHub Copilot planner writes `.harness/plans/<screen>.md`, and an OpenCode agent executes it.

Haiku 5.5 and GPT-6 Luna, at about 5 credits per session, are worth adding to the baseline as a fallback executor if in-house serving proves slow. No capability data on them was found here.

## One AGENTS.md and one skills folder serve both hosts

| Artifact | OpenCode | GitHub Copilot |
|---|---|---|
| Rules | `AGENTS.md`, nested files | `AGENTS.md` on most surfaces |
| Skills | `.agents/skills/` | `.agents/skills/` |
| Agents | `.opencode/agents/*.md` | `.github/agents/*.agent.md` |
| Lint after edit | LSP (V1), plugin, commands | `postToolUse` hook |
| Hard blocks | `permission` denies, V2 policies | `preToolUse` deny, policy hooks |

Both hosts read `AGENTS.md` and `.agents/skills/` natively, so those should be the single shared source. In V1, OpenCode enforces that a skill's `name` matches its folder name, so follow that rule everywhere ([OpenCode V1 skills](https://github.com/anomalyco/opencode/blob/dev/packages/web/src/content/docs/skills.mdx); [GitHub Docs](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-skills)). Neither host resolves contradictions between instruction files. OpenCode "combines the files and does not resolve conflicts" ([OpenCode](https://opencode.ai/docs/instructions/)), and the GitHub Copilot CLI docs state there is no general priority order between files ([GitHub Docs](https://docs.github.com/de/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions)). Each rule must therefore live in exactly one file. Short nested files work well for protected areas: `lib/features/send_review/AGENTS.md` says "tokens only, goldens mandatory", and `lib/core/keys/AGENTS.md` says "do not edit; stop and escalate". Agent definitions do not share a format across hosts, so keep their bodies thin and put the knowledge in skills.

### OpenCode: check the version, then agents, commands and denies

OpenCode now ships two major versions, and they behave differently.

- **V2** (npm 2.0.0 published 11 September 2026) runs no language servers, so it produces no Dart diagnostics on its own. It ignores `CLAUDE.md`. It uses a new plugin API and an ordered `permissions` array, renames `bash` to `shell`, and does not send per-agent temperature; temperature has to be set on a model variant.
- **V1** (latest 1.19.5) still feeds LSP diagnostics back to the agent when `"lsp": true` is set.
- V2 reads V1 config and agent files, so **writing everything in V1 syntax** survives either version ([OpenCode migration guide](https://opencode.ai/docs/migrate-v1/); [Capital and Compute](https://capitalandcompute.net/blog/opencode-2-0-what-changed/)).

Connect the self-hosted models as an OpenAI-compatible provider with `tool_call: true`. Set `limit.context` to the effective ~128K, not 1M, so compaction starts early. The gateway must actually have tool calling enabled; V2's vLLM auto-discovery assumes it is off ([OpenCode Models](https://opencode.ai/docs/models/)).

Define two agents: a **migrator** on GLM 5.3 and a **mechanic** on Flash with few tools and a low step limit. Bind each skill to a command. Commands are the most reliable way to give a weak tool-caller real context without MCP, because `` !`dart analyze $1 | tail -n 80` `` and `` !`./tool/ds_audit.sh $1` `` are executed by OpenCode, not chosen by the model ([OpenCode Commands](https://opencode.ai/docs/commands/)). In V2, these shell blocks run outside the permission system, so limit them to read-only scripts. A sketch of the migrator agent (paths and model IDs are placeholders):

```markdown
---
description: Migrates one screen to tokens
mode: subagent
model: inhouse/glm-5.3
steps: 40
permission:
  edit:
    "*": allow
    "lib/core/keys/*": deny
    "lib/core/crypto/*": deny
  bash:
    "*": ask
    "dart analyze *": allow
    "dart format *": allow
    "flutter test *": allow
    "./tool/ds_audit.sh *": allow
  webfetch: deny
---
Load skill ds-migrate-screen first. Run
dart analyze on each edited file. Same
failure twice: write a stuck report, stop.
```

For lint after edits, combine three layers:

1. Turn on the built-in `dart` formatter (`"formatter": true`).
2. Require `dart analyze` in AGENTS.md. The V1 docs themselves recommend this over LSP.
3. If plugins are allowed, add a small plugin that appends `dart analyze` output to every `.dart` edit result. V2 documents an `execute.after` hook that can rewrite what the model sees ([OpenCode plugins](https://opencode.ai/docs/build/plugins/server/)). Keep it dependency-free, because npm plugins trigger `bun install` at startup.

Permissions block edits to key-management paths and allowlist shell commands. **Edit denies do not stop `sed -i` through the shell**, and the docs advise a narrow shell allowlist ([OpenCode Permissions](https://opencode.ai/docs/permissions/)). So also keep `bash "*": "ask"`, never use `--auto`, and add a CI check plus CODEOWNERS that reject diffs to protected paths. In V2, put the denies in system-level policies, which a repository cannot loosen.

For a fully self-hosted setup:

- enable only the self-hosted provider;
- set `OPENCODE_DISABLE_FREE_MODELS=1`;
- disable auto-update and the models.dev fetch ([OpenCode V1 CLI](https://github.com/anomalyco/opencode/blob/dev/packages/web/src/content/docs/cli.mdx));
- treat `~/.local/share/opencode/` as sensitive, because it stores prompts and file contents ([OpenCode Troubleshooting](https://opencode.ai/docs/troubleshooting/)).

### GitHub Copilot: pinned planner agents, hooks and hard budgets

`AGENTS.md` reaches the GitHub Copilot CLI, the cloud agent, VS Code Chat and GitHub.com code review. **VS Code's in-IDE code review and Visual Studio read only `.github/copilot-instructions.md`** ([GitHub Docs](https://docs.github.com/en/copilot/reference/custom-instructions-support)), so copy the few review-critical rules there.

Custom agents in `.github/agents/` accept a `model` preference list. That lets a `ds-planner` and a `ds-reviewer` be pinned to Opus 5.5 with Sonnet 5.5 as fallback ([VS Code docs](https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference)). Prompt files do not reach the CLI or the cloud agent ([GitHub Docs](https://docs.github.com/en/copilot/reference/customization-cheat-sheet)), so package reusable workflows as skills.

Hooks in `.github/hooks/*.json` can run `dart format` and `dart analyze` after each edit. A `postToolUse` hook can inject the output as context for the model, though it cannot undo the edit. A `preToolUse` hook can deny actions, and machine-wide policy hooks load before repository hooks ([GitHub CLI hooks](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-hooks-reference)). VS Code hooks are still in preview, and their payload fields were not confirmed, so test them before relying on them.

The cloud agent prepares its environment from `copilot-setup-steps.yml`. That runs only on the default branch, and only on Ubuntu or Windows ([GitHub Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment)). That covers `flutter test` but not iOS builds.

Two governance facts matter for a regulated product:

- Since 26 August 2026, **new GA models are auto-enabled** unless an admin opts out ([GitHub changelog](https://github.blog/changelog/2026-07-29-default-model-enablement-for-copilot-business-and-enterprise/)).
- Content exclusion is **not honoured in VS Code Edit and Agent modes**, though it is GA in the CLI ([tproger](https://tproger.ru/news/copilot-v-prilozhenii-i-cli-perestal-chitat-isklyuchyonnye-fajly)).

The protected key-management code therefore needs hooks, CODEOWNERS and CI checks, not exclusion alone. One option to check is enterprise BYOK, in public preview for "any OpenAI-compatible provider" ([GitHub changelog](https://github.blog/changelog/2026-01-15-github-copilot-bring-your-own-key-byok-enhancements/)). It could let GitHub Copilot run the self-hosted GLM endpoint, but how that usage is billed against credits is undocumented.

## Figma's agent should audit and name, not import

The in-app Figma agent left beta on **6 October 2026** and now draws from the per-seat AI-credit pool: 3,000 per month on Professional, 3,500 on Organization and 4,250 on Enterprise. Requests cost **30+ credits for a font change and 300+ for a five-screen flow**, and Figma "can't predict" costs in advance ([FourWeekMBA](https://fourweekmba.com/ai-figma-design-agent-leaves-beta-now-draws-ai-credits/)). Only Full-seat users with edit access can have it edit shared files.

Figma documents these agent capabilities: applying variables, switching modes, updating variable-bound properties, applying styles, renaming layers and running plugins ([Figma Help](https://help.figma.com/hc/en-us/articles/37998629035799-Work-with-the-Figma-agent-in-design-files)). It also documents batch-naming variables to a convention you prompt ([Figma](https://www.figma.com/solutions/ai-variable-namer/)). There are two important limits. "Rename layers" only touches layers that still have default names, and Figma itself points to the deterministic bulk-rename tool for enforced conventions ([Figma Help](https://help.figma.com/hc/en-us/articles/38978644498199-AI-workflows-collection-Refine-your-components-and-variables-for-the-Figma-agent)). Undo also reverts only the most recent change. **Moving variables between collections, creating alias chains, setting scopes and deleting variables are not documented as native agent actions.**

Skills follow the Agent Skills spec, but only as a **single `.md` file**, with no `scripts/` or `references/`. They can be published privately to a team or the organisation and invoked with `/skill-name`. If a prompt names several skills, only the first runs, and deleting a published skill removes it for everyone ([Figma Help](https://help.figma.com/hc/en-us/articles/40283639496599-Custom-skills-for-the-Figma-agent-and-Figma-Make)). Keep the canonical file in git, flatten the M3 naming rules into it, and re-upload it on each release.

### A seven-step route from messy file to M3 tiers

1. **Confirm governance and branch.** The org admin, the only role that controls AI on Organization and Enterprise, confirms the agent is enabled ([Figma Help](https://help.figma.com/hc/en-us/articles/17725942479127)). Decide whether the MCP ban also covers the agent's built-in connectors, such as GitHub; the safe default is not to use them. Work on a branch: you can only publish a library from main ([Figma Help](https://help.figma.com/hc/en-us/articles/360063144053-Guide-to-branching)).
2. **Audit read-only.** Run a flattened `m3-variable-audit` skill. It inventories collections, classifies each variable as reference, system, extended or unknown, and flags duplicates, raw hex fills and default-named layers in an audit frame on the canvas. This can start in weeks 1–2.
3. **Generate the target variables from code.** The same Style Dictionary run that builds the Flutter theme emits one JSON file per collection and mode. Figma's native import takes DTCG-shaped files with `$value`/`$type`, `{alias}` references, and scopes and code syntax under `$extensions.com.figma` ([Atomize](https://atomize.tools/blog/figma-variables-export-json/)). Import in tier order (Reference, then System, then Extended), because aliases need their target collection to exist first ([Figma forum](https://forum.figma.com/ask-the-community-7/how-to-import-your-existing-variables-css-json-into-figma-via-new-import-feature-48528)).
4. **Map legacy variables to new ones.** The agent proposes a table of legacy variable → new system role, and a human approves it.
5. **Rebind, one non-protected page first.** Use the agent's "apply variables", or a plugin calling `setBoundVariableForPaint` ([Figma Plugin API](https://developers.figma.com/docs/plugins/api/figma-variables/)).
6. **Retire the old structure.** Bulk-rename layers deterministically. Park legacy collections under a deprecated name until nothing binds to them.
7. **Review, merge and publish from main**, as a separate, deliberate step.

If native import is not available or proves awkward, have the agent build a **generative plugin** once: paste the tokens JSON, and it creates or updates collections, aliases, scopes and code syntax. Building it costs credits; **running plugins is free** ([Figma blog](https://www.figma.com/blog/agent-custom-tools-context-skills/)). A practitioner test shows why the deterministic route wins. An agent-driven token run took 6 minutes 46 seconds and choked on 77KB of inline JSON, while the scripted pipeline finished in 36 seconds ([GitButler](https://blog.gitbutler.com/design-tokens-ai-agent-vs-button)). Tokens Studio is the mature git-sync alternative. Its default format is Legacy rather than DTCG, and multi-file sync and branches are paid features ([Tokens Studio](https://docs.tokens.studio/token-storage/remote/)).

For the target structure, M3 separates reference tokens, which hold concrete values (`--md-ref-*` on the web), from system tokens, which name roles and map to them (`--md-sys-*`) ([Material Web](https://material-web.dev/theming/material-theming/)). Use three collections:

- **M3 Reference**: one mode. Set its scopes so palette values stay out of pickers.
- **M3 System**: Light and Dark modes, plus contrast modes if needed.
- **Wallet Extended**: aliases to System, mirroring the Flutter `ThemeExtension`.

Mirror DTCG paths exactly with `/` grouping (`sys/color/primary`), so the import needs no translation layer. Put the Flutter accessor in each variable's code syntax. Use semantic names in System and Extended; as Figma notes, "a variable called `blue-500` tells agents nothing" ([Figma Help](https://help.figma.com/hc/en-us/articles/38978644498199-AI-workflows-collection-Refine-your-components-and-variables-for-the-Figma-agent)).

One sync risk is open. Native import **"overwrites rather than merges, so it is not a sync strategy"** ([Atomize](https://atomize.tools/blog/figma-variables-export-json/)). Whether re-importing preserves variable IDs, and therefore layer bindings, is unverified. Test it on a duplicate file before the first real release, and route token renames through a deprecation window rather than in-place renames.

## The plan holds; four parts move

| Plan item | Verdict | Change or addition |
|---|---|---|
| Send-flow pilot, 5–10 frozen tasks, GLM vs frontier baseline | Confirmed, widened | Add Flash. Run self-hosted models 3× per task and report "passes all three". Run frontier once on Sonnet 5.5 (~900 credits for 10 tasks), plus Opus 5.5 on the 3 hardest (~530). Log whether the skill loaded, repair rounds and wall time. |
| Code audit script and compliance metric | Confirmed, upgraded | Emit a JSON worklist; it becomes Flash's input and the migration plan. |
| Naming rules (tiers, deprecation, WCAG 2.2 AA) | Confirmed | Add Figma path form, code syntax per variable, reference tier hidden from pickers. |
| Style Dictionary → Flutter theme, CI staleness, `material_ui` pin, dynamic colour off | Confirmed | Same run emits Figma-import JSON per collection × mode. |
| Analyzer plugin with fix messages and ratchet | Confirmed, now central | Start in week 2. Enable rules under `diagnostics`. Wire into both hosts' after-edit loops. |
| `Ds*` wrappers | Confirmed | "Prefer `DsButton`" lint naming the wrapper. |
| AGENTS.md, three skills, model split | Changed | AGENTS.md holds token index, skill index and stop rule. Skills in `.agents/skills/`, invoked by name. Evals written first. One agent file per host. |
| Goldens, a11y matchers, wallet invariants | Confirmed | Cheap models never update goldens; humans approve images. |
| Port variables via Figma agent on a branch | Changed | Native DTCG import or agent-built plugin creates tiers; agent audits, names, rebinds. Read-only audit moves to weeks 1–2. |
| Screen-by-screen, protected last; CODEOWNERS, versions, CHANGELOG | Confirmed | Skills canonical in git; GitHub Copilot hooks and setup steps only work from the default branch. |
| Failure flywheel | Confirmed | Stuck reports feed it. Remove scaffolding when evals show it no longer matters. |
| Protected zones | Confirmed, hardened | Shell can bypass OpenCode edit denies, so add a CI protected-path check. VS Code agent mode ignores content exclusion. No auto-approve anywhere. |
| *New:* week 0 | Added | Confirm OpenCode version and serving config before the baseline. |
| *New:* credit governance | Added | User budget, CLI session limit, paid overage off, explicit model allowlist. |
| *New:* skill distribution | Added (see addendum) | Ship the harness skills inside the Flutter theme package and install them with `dart run skills@ get`. Vendor two or three reviewed official Flutter skills. |

## Addendum: Flutter's official skills and package skills

*Added 7 November 2026, after reviewing [flutter.dev/ai](https://flutter.dev/ai).* The landing page is mostly about adding AI features to apps (Firebase AI Logic, Genkit, GenUI). The page it links to, on [MCP, skills and AI plugins](https://docs.flutter.dev/ai/get-started), has three things that work without MCP.

**Official skills install into the shared folder.** For GitHub Copilot, Flutter's docs install skills with `npx skills add flutter/agent-plugins …` and `npx skills add dart-lang/skills …` using `--agent universal`, which targets `.agents/skills/`. That is the folder both hosts already read. The [flutter/agent-plugins](https://github.com/flutter/agent-plugins) repo (BSD-3-Clause) has ten skills, covering widget tests, app architecture, responsive layout, routing and localisation among others. Two of them, `flutter-fix-layout-issues` and `flutter-add-integration-test`, rely on MCP tools, so skip them. None covers theming, Material 3, design systems, `ThemeExtension`, golden tests or accessibility, so the harness skills fill a real gap rather than duplicate anything.

Don't install with `--skill '*'` straight from GitHub. Pick two or three (widget tests, architecture), review them, commit them to the repo and add them to the skill index in AGENTS.md. Every installed skill's description competes for a weaker model's attention.

**Package skills replace the plugin marketplace.** A Dart package can ship skills in a top-level `skills/` folder next to `lib/` ([dart.dev](https://dart.dev/tools/pub/package-skills)):

- one subfolder per skill, each with a `SKILL.md` and optional `scripts/`, `references/` and `assets/`;
- each folder name starts with the package name, for example `ds_flutter-migrate-screen`;
- `dart pub publish` bundles `skills/` automatically;
- each consuming app runs `dart run skills@ get` to install the chosen skills into its `.agents/skills/` folder;
- `skills_lint` validates the skills in CI;
- maintainer-only skills stay in the package repo's own `.agents/skills/` and are not distributed.

Putting the harness skills inside the Flutter theme package means every app gets skills that match that exact version of the tokens and `Ds*` wrappers. They travel through a private pub registry, which gives the multi-project channel the earlier playbook expected from a Claude Code plugin marketplace.

**Official rules.** A [rules folder](https://github.com/flutter/agent-plugins/tree/main/rules) holds `.md` and `.mdc` rule files. Copy only rules that don't assume MCP (the documented example, proactively triggering hot reload, does) and keep the total within the 10–30 rule budget.

**Not usable here:** the Dart and Flutter MCP server, the Developer Knowledge MCP server and the bundled plugins. The Flutter accessibility agent ships through the plugin route; check whether its instructions can be adapted into a skill. **For later:** GenUI, shown as a sample on the landing page, is Flutter's approach to agents building UI at runtime from your own widget catalog. It is relevant to conversational and agentic interface work and rewards clean, well-defined components.

## Conclusion

Removing MCP and Claude Code changes where the harness's intelligence lives more than it changes the plan. The earlier playbook could lean on a strong model reading rich context through tools. Here, the context has to be computed for the model by analyzer rules, audit worklists, injected command output and goldens. That turns out to be cheaper, more portable across OpenCode, GitHub Copilot and Figma, and more auditable for a regulated product. The scarce resource is no longer tokens but frontier judgement. It pays off most when spent on artifacts that are reused thousands of times (lint messages, skills, contracts) and on the moments a cheap model is stuck or a trust-critical screen changes.

Two things will decide whether this works, and neither is a model choice. The first is plumbing: serving quantization, tool-call parsers and the OpenCode version can each cost more points than the GLM-versus-frontier gap. The second is the frozen send-flow suite. With no Flutter benchmark for GLM anywhere, that suite will be the only evidence the team has, and it will also be what lets each scaffold be removed as models improve.

## Verify these before week 1

1. **OpenCode build:** run `opencode --version` to see whether it is V1 (1.19.x) or V2 (2.x). Is it pinned? Are local plugins and a private npm registry allowed?
2. **Which "Flash":** GLM-5.3-Flash, GLM-4.7-Flash or something else? Does the gateway accept image input?
3. **Serving for both models:** quantization (FP8 vs INT4 or lower), tool-call and reasoning parsers, MTP speculative decoding on or off, reasoning preserved across turns, real context and output limits, and whether reasoning effort is exposed.
4. **GitHub Copilot billing:** Business or Enterprise? Is the credit budget personal or a share of a pool? Is paid overage on? What do code reviews cost in credits plus Actions minutes?
5. **GitHub Copilot policy:** are Opus 5.5, Sonnet 5.5, GPT-6 Sol and Haiku 5.5 enabled, and is default model enablement on? Which surfaces are allowed (VS Code agent mode, CLI, cloud agent)? Are hooks permitted? Is content exclusion configured?
6. **GitHub Copilot BYOK:** is the preview enabled? Could it target the self-hosted GLM gateway, and how would that usage count against credits?
7. **Figma admin:** is AI on for the design workspace? Does the plan tier allow branching? Does the designer have a Full seat, and how many credits does it carry? Does the MCP ban cover the agent's connectors? Is native variable import available? Are Community skills, plugins and Tokens Studio approved?
8. **Wallet toolchain:** the Dart SDK is at least 3.10, which analyzer plugins need, and the Flutter version supports the pinned `material_ui`.
9. **Legal:** sign-off that in-house use falls outside the GLM 5.3 licence's "Model-as-a-Service" review clause ([licence](https://huggingface.co/zai-org/GLM-5.3/blob/main/LICENSE)).
10. **Skills tooling:** can the private pub registry serve the `skills` and `skills_lint` packages, and is GitHub access allowed for vendoring the official Flutter skills?
