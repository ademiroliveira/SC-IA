# The Design Harness Playbook: Building a Stack-Agnostic System That Keeps Designers and AI Agents On-Brand, Accessible and Production-Ready

> Written 7 November 2026 as a general playbook. It assumes a team that can use Claude Code and MCP. For teams that can't, see `02-research-without-mcp.md` and `03-implementation-spec-pack.md`.

**Bottom line:** Build the design harness as a *generated, layered system*, not a single file. Keep one structured design-system source in DTCG tokens plus machine-readable component contracts and rules. Generate every agent-facing surface from it: AGENTS.md/CLAUDE.md pointers, skills, an MCP server or CLI, Guidelines.md for Figma Make, an optional DESIGN.md, and per-stack theme code such as Flutter ThemeData. Then close the loop with deterministic sensors (lint, golden/visual tests, accessibility checks) and a small eval suite. The companies furthest along (Atlassian, Vercel, BILL, Uber) all point the same way. Prose context helps a lot. Only structured sources plus automated verification make the output reliable. Even then, a human gate is still required.

## TL;DR

- **What it is:** A design harness is everything around the model that shapes UI output. It has *guides* (intent, tokens, component contracts, content/a11y rules, skills) that steer before generation, and *sensors* (linters, golden tests, a11y scans, critic agents, evals) that catch failures after. The term comes from 2026 "harness engineering" (OpenAI, HashiCorp's co-founder, Thoughtworks). Design-system teams at Atlassian, Vercel, BILL, Uber, Spotify and Miro have applied it to design.
- **How to build it:** Keep an agnostic core: principles, content/disclosure rules, WCAG 2.2 AA rules, DTCG semantic tokens, component contracts and workflow skills. It lives in one versioned repo and ships as a Claude Code plugin marketplace plus a design-system MCP server or CLI. Thin per-stack adapters (Flutter/M3, React) map semantic tokens to platform theme APIs and add stack-specific lint and visual tests. For Flutter, generate `ColorScheme`/`TextTheme`/component themes and `ThemeExtension`s from tokens. Disable dynamic color for brand surfaces, and ban raw `Color(...)`/`EdgeInsets` literals via a Dart 3.10 analyzer plugin.
- **What's mature vs. not:** Stable: DTCG 2025.10 tokens, Style Dictionary, Figma Code Connect template files (which accept `dart`), the official Dart & Flutter MCP server, Storybook MCP for React, and Claude Code plugin marketplaces. Alpha or experimental: Google's DESIGN.md (spec "alpha," CLI v0.1.x, no Dart export), Widgetbook MCP (community, self-described experimental), Figma's write-to-canvas `use_figma` (beta), and Material 3 Expressive in Flutter (in progress in the newly decoupled `material_ui` package). Treat DESIGN.md as a portable export, not the source of truth.

## Key Findings

1. **"Harness" is now the accepted frame, and it maps directly onto design systems.** An OpenAI engineering post of February 11, 2026 described building a product with zero hand-written code. The key lesson was that early progress was slow "because the environment was underspecified." The team's fix was a short AGENTS.md that, in OpenAI's words, "(roughly 100 lines) is injected into context and serves primarily as a map," pointing to deeper sources of truth, including a `DESIGN.md` and `FRONTEND.md`. A Thoughtworks article on martinfowler.com splits the harness into *guides* (feedforward) and *sensors* (feedback), each either computational (deterministic) or inferential (LLM-judged). HashiCorp's co-founder described the core habit: every time an agent makes a mistake, engineer a permanent fix into its environment.

2. **Structured, on-demand context beats one big file in production; a portable file wins for greenfield prototypes.** Atlassian generated its own DESIGN.md from its structured content pipeline and tested it. It worked "fairly well" for one-shot Figma Make dashboards. In production codebases, though, Atlassian's MCP server and skills consumed fewer tokens. Atlassian concluded that DESIGN.md is useful as a portable snapshot of a design system, not a replacement for richer design-system tooling. Compared with agents working without MCP, Atlassian's ADS MCP produced 4.9% more accurate code, 11% fewer errors, 34% faster completion, 16% fewer tokens and 26% fewer tool calls.

3. **Evals are what make guidance trustworthy.** Vercel's public `design.md` was rewritten against seven frozen scenarios over 200+ runs. In a six-page comparison it produced 39 known failures with the file versus 91 without, 57% fewer. Vercel is candid that every page still had at least one ship-blocking failure, and that checks only catch failures already named. Vercel's three-layer pattern is prose judgment, plus a fixed stylesheet of primitives the agent cannot reinvent, plus deterministic checks. That pattern is the best template available today.

4. **The winning pattern is "one source, many surfaces."** Atlassian generates its MCP server content, agent skill and DESIGN.md files from one structured source, so "none of them drift." It later added a CLI (Atlassian's `ads-cli` package) that reported sessions 8% faster and 8% fewer tokens than its MCP baseline. BILL kept Storybook as the source of truth and layered a JSON CLI, a hosted MCP server and compliance skills on top, reporting 31–63% token reduction per task. Uber's Base MCP exposes 280 doc pages, 700+ tokens and 3,200+ icons, and reports 500+ users and 50,000+ tool calls.

5. **Adoption is still early, so investing now is a differentiator, not catch-up.** zeroheight's Design Systems Report 2026 (n=147) found that one in ten teams has AI in the process and just under half are experimenting. Spotify's Encore team (speaking at an Into Design Systems meetup in February 2026) found developers going to Cursor first and shipping non-Encore UI because the system was too complex for AI; as the team put it, the AI won't work it out on its own; it will send users down a different path. If the harness is not the easiest path, agents route around it.

6. **For Flutter specifically, the ecosystem shifted in 2026 in your favor.** Flutter decoupled Material into `pkg:material_ui` 1.0.0, released in August 2026 on its own weekly schedule, with Material 3 Expressive work "already underway." Dart 3.10 introduced a first-party analyzer plugin system, so custom rules such as "no hardcoded colors" now run inside `dart analyze` and the IDE. The official Dart & Flutter MCP server and a `dart-flutter` Claude Code plugin give agents analyzer diagnostics, tests and runtime introspection. Figma Code Connect's framework-agnostic template files list `dart` as a supported language.

## Details

### 1. Definitions and mental model

**Agent harness / harness engineering.** HumanLayer condensed the idea as "coding agent = AI model(s) + harness." The harness is the configuration surface: instruction files, skills, tools/MCP, hooks, sub-agents and feedback loops. OpenAI's post popularized the term. Its components were context engineering, architectural constraints enforced by linters and LLM agents, and "garbage collection" agents that scan for drift. The Thoughtworks taxonomy is the most useful vocabulary:

| | Computational (deterministic, cheap) | Inferential (LLM-judged, costly) |
|---|---|---|
| **Guides (before)** | Tokens, typed component APIs, generated theme code, templates, Code Connect mappings | AGENTS.md/CLAUDE.md, Guidelines.md, DESIGN.md prose, skills, voice/disclosure rules |
| **Sensors (after)** | Lint for hardcoded values, contrast/tap-target tests, golden/visual diffs, DESIGN.md `lint` | Design-critic agent, content/compliance reviewer agent, screenshot-vs-Figma comparison |

**Design harness (working definition).** A design harness is the versioned set of guides and sensors that makes the design system the *default context* for every human and agent producing UI. It also makes deviation detectable automatically. It differs from a design system the way a CI pipeline differs from a codebase. The design system is the content. The harness is the delivery, enforcement and feedback machinery around it.

**How the pieces relate:**
- **AGENTS.md / CLAUDE.md** is the always-loaded *map*. Keep it short and point to sources. OpenAI's lesson was that a monolithic file "rots instantly" and "too much guidance becomes non-guidance." HumanLayer found codebase overviews "didn't help at all."
- **Skills** are progressive-disclosure *procedures*: "build a screen," "audit a11y," "write disclosure copy." They load only when relevant.
- **MCP servers / CLIs** give *on-demand retrieval* of tokens, component APIs and docs. MCP suits remote, auth-scoped access. A CLI suits shells and is often cheaper, as Atlassian found.
- **DESIGN.md / Guidelines.md** are *portable snapshots* for tools that can't reach your repo or MCP, such as Figma Make, Stitch or one-off pages.
- **Tokens + component contracts** are the *normative source* the others are generated from.

**Leading practitioners and sources to follow:** OpenAI's harness-engineering write-up, Thoughtworks on martinfowler.com, HashiCorp's co-founder on agent harnesses, the Atlassian Design System team, Vercel's design engineering team, the BILL and Uber design-system teams, the DTCG co-chair's "State of AI in Design Systems" field study, Southleft, zeroheight, and design-systems educators publishing on evals and AI. The DTCG co-chair's build report on agent teams is a useful caution: full autonomy hit a ceiling, and the fix was a human gate rather than a better prompt.

### 2. Reference architecture (described as a diagram)

Picture four horizontal layers with a feedback arrow running from the bottom back to the top:

```
┌────────────────────────── LAYER 1: SOURCES OF TRUTH (design-system team owns) ─────────────────────────┐
│  Figma library + Variables  ⇄  DTCG tokens (*.tokens.json)  ⇄  Component contracts (YAML/JSON schema) │
│  Principles/intent · Content & disclosure rules · A11y rules (WCAG 2.2 AA) · Pattern docs              │
└───────────────────────────────────────────────┬────────────────────────────────────────────────────────┘
                                                │  build pipeline (CI): validate → transform → publish
┌───────────────────────────────── LAYER 2: GENERATED CONTEXT SURFACES ──────────────────────────────────┐
│ AGENTS.md block · CLAUDE.md import · Skills (SKILL.md) · DS MCP server / CLI · DESIGN.md (export)       │
│ Figma Make Guidelines.md · llms.txt · Code Connect templates                                           │
└───────────────────────────────────────────────┬────────────────────────────────────────────────────────┘
                                                │  per-stack adapters (transform + wrap)
┌──────────────────────────────── LAYER 3: STACK ADAPTERS (platform teams own) ──────────────────────────┐
│ Flutter/M3: ThemeData, ColorScheme, TextTheme, component themes, ThemeExtensions, lint plugin, goldens │
│ React/web: CSS vars/Tailwind theme, component lib, ESLint/Stylelint rules, Storybook + MCP, a11y tests │
└───────────────────────────────────────────────┬────────────────────────────────────────────────────────┘
                                                │  agents + humans build product UI
┌──────────────────────────────── LAYER 4: SENSORS & GATES (shared, per-repo CI) ────────────────────────┐
│ Token-compliance lint · Visual regression/goldens · Automated a11y · Critic agents · Evals · Human gate │
└───────────────────────────────────────────────┴── failures → triage → new rule/primitive/eval ──↑───────┘
```

**Separation rule:** the core speaks only *semantic* language, such as `color.action.primary.background`, `space.inset.md` or "use the RiskDisclosure component before any projected return." Adapters translate that into platform vocabulary: `colorScheme.primary`, `EdgeInsets.all(AppSpacing.md)`, a Tailwind class. Never let platform names leak into the core. Never let agents in product repos edit generated adapter output by hand.

**Token naming conventions:**
- Use three tiers. *Primitive* (`color.blue.600`) holds values. *Semantic* (`color.text.subtle`, `color.surface.raised`, `color.feedback.loss`) holds roles. *Component* (`button.primary.background.pressed`) holds states. Southleft's argument applies: `color.text.subtle` "carries a decision where `gray-2` carries a shade." Agents can't infer intent from shade names.
- Put usage constraints in `$description`: the backgrounds a token may sit on and the fills it may not. This is guidance an agent cannot derive from the value.
- Finance-specific semantics deserve first-class tokens: `color.feedback.gain`/`loss` (never color alone, per WCAG 1.4.1), `color.risk.high`, and `surface.disclosure`. Keep them separate from generic success/error, because gain/loss conventions differ by market and must not be confused with system errors.

**Recommended structure for the agnostic core** (one repo, e.g., `design-harness-core`):

```
design-harness-core/
├── AGENTS.md                      # ~60–100 lines: map + non-negotiables + where to look
├── CLAUDE.md                      # imports AGENTS.md + Claude-specific notes
├── principles/
│   ├── intent.md                  # brand personality, what "on-brand" means, anti-patterns ("stock Material look")
│   ├── content-voice.md           # tone, plain language, reading level
│   ├── disclosures.md             # FINRA 2210-aligned rules, required disclosure components, banned phrases
│   ├── trust-patterns.md          # confirmations, irreversible actions, fees, self-custody warnings
│   └── accessibility.md           # WCAG 2.2 AA rules in testable form
├── tokens/                        # DTCG 2025.10 — the normative values
│   ├── primitive/*.tokens.json
│   ├── semantic/{light,dark,high-contrast}.tokens.json
│   ├── component/*.tokens.json
│   └── resolver.json              # theme/brand permutations (DTCG Resolver module)
├── brands/                        # one token override set per brand or product line
├── components/                    # stack-neutral contracts
│   └── button.contract.yaml       # anatomy, variants, states, props, a11y (role, label, min target), do/don't
├── patterns/                      # e.g., trade-confirmation.md, risk-disclosure.md, agent-response.md
├── skills/                        # Agent Skills (SKILL.md + references)
│   ├── build-screen/  audit-a11y/  write-disclosure-copy/  review-design/  figma-to-code/
├── evals/
│   ├── scenarios/*.yaml           # frozen prompts + inputs + expected properties
│   └── checks/                    # deterministic checks shared across stacks
├── exports/                       # GENERATED — never hand-edit
│   ├── DESIGN.md                  # per brand, via generator; lint with the design.md CLI
│   ├── figma-make/Guidelines.md
│   └── llms.txt
├── mcp/  cli/                     # thin servers over the same content (Atlassian pattern)
└── .claude-plugin/marketplace.json  # distributes skills, hooks, MCP config
```

**Pointing agents at it.** Each product repo's AGENTS.md carries a short, *generated, marked block*. Atlassian's `ads-cli init` does exactly this: it creates or updates a marked block in the root AGENTS.md and leaves the content people wrote untouched. The block names the plugin/skills to use, the MCP server or CLI to query before using any component, the adapter package, and the verification commands that prove a change works. Put build/test/lint commands at the top.

### 3. Formats and standards: what to use as the source of truth

| | **DTCG 2025.10** | **Figma Variables** | **Google DESIGN.md** |
|---|---|---|---|
| Status | **Stable** (first stable version, Oct 28, 2025; Format, Color, Resolver modules). A Community Group report, *not* W3C Standards Track | Production; proprietary model | **Alpha** (`version: "alpha"`; CLI (Google's `design.md` npm package) v0.1.x; Apache-2.0; open-sourced April 2026) |
| Strength | Interchange standard; theming/modes via Resolver; supported by Style Dictionary, Tokens Studio, Terrazzo | Where designers actually work; feeds Figma MCP and Make | Tokens + *rationale* in one portable file; lint checks broken refs and WCAG contrast; `diff` detects regressions |
| Limits | No intent/rationale; Style Dictionary support for 2025.10 is "a work in progress in v5" | Not a code artifact; mode/alias semantics differ from DTCG | Small token schema (colors, typography, rounded, spacing, components); exports only Tailwind v3/v4 and DTCG (no Dart); Atlassian notes it "reveals the internals" of your system and is less token-efficient at scale |
| Role in harness | **Normative source in code** | **Authoring surface**, synced both ways with DTCG | **Generated export** for Stitch/Make/one-off tools |

**Recommendation:** make DTCG JSON in git the source of truth for *values*. Treat Figma Variables as the authoring mirror, synced via Tokens Studio or Figma's native variable import/export into DTCG, with a CI diff that fails on unsynced changes. Make DESIGN.md and Guidelines.md *build outputs*. Generate DESIGN.md from tokens plus `principles/` and validate it with the design.md CLI's `lint` command in CI. Use `diff` against the previous release to flag regressions. Don't hand-author DESIGN.md per project. You'll get N drifting copies.

**Token pipeline to Flutter/Dart.** Style Dictionary (v4+ has first-class DTCG support) is the pragmatic default because one pipeline serves web, iOS, Android and Flutter. Its built-in Flutter output is constants-oriented. Real projects write custom formats that emit `ColorScheme`, `TextTheme` and `ThemeExtension` classes. In torana-labs/catch-dating-app PR #1432, a 1,226-line hand-rolled Dart generator was replaced with pinned Style Dictionary 5.7.1 and "two custom formats" producing byte-identical CSS and Dart. Run `dart format` on output and add a `--check` mode in CI to catch stale generated files. Alternatives: `figma2flutter` (Dart package, Tokens Studio-native) for Flutter-only shops, or a custom Dart script if your JSON is bespoke. Note the DTCG 2025.10 change that a dimension is an object (`{"value": 16, "unit": "px"}`), not a string. Update transforms accordingly.

### 4. Flutter + Material 3 adapter

**Recommended adapter structure** (a versioned package, e.g., `ds_flutter`, consumed by every Flutter app):

```
ds_flutter/
├── AGENTS.md                         # adapter-specific rules; imports core rules by reference
├── tool/tokens/                      # Style Dictionary config + custom Dart formats
├── lib/
│   ├── ds_flutter.dart               # public API: AppTheme.light/dark/highContrast(brand)
│   ├── src/generated/                # GENERATED from DTCG — header: "do not edit"
│   │   ├── color_schemes.g.dart      # ColorScheme per brand × mode
│   │   ├── text_theme.g.dart
│   │   └── extensions.g.dart         # AppSpacing, AppRadii, AppMotion, AppElevation, AppFinanceColors
│   ├── src/theme/
│   │   ├── app_theme.dart            # assembles ThemeData + component themes + extensions
│   │   └── component_themes.dart     # FilledButtonThemeData, CardThemeData, InputDecorationTheme, ...
│   └── src/components/               # branded wrappers: DsButton, DsRiskDisclosure, DsAmountField ...
├── analyzer_plugin/                  # Dart 3.10 plugin: no_raw_colors, no_magic_spacing, use_ds_components
├── widgetbook/                       # catalog of every component × state × theme
├── test/goldens/                     # golden tests per component × brand × mode × text scale
└── code_connect/*.figma.ts           # Code Connect templates, language: "dart"
```

**Mapping semantic tokens to M3:**
- **ColorScheme:** map semantic roles to M3 roles explicitly. Examples: `primary`/`onPrimary`, `primaryContainer`, `secondary*`, `tertiary*`, `error*`, `surface`, the `surfaceContainerLowest…Highest` ladder, `outline`/`outlineVariant`, `inverseSurface`. Generate the *full* scheme from tokens rather than relying on `ColorScheme.fromSeed`. Seed-generated tonal palettes are the main reason agent output "looks like stock Material." If you use `fromSeed` for exploration, override every role your brand defines.
- **TextTheme:** map your type scale to the 15 M3 slots (`displayLarge` … `labelSmall`) with your brand fonts, weights, line heights and letter spacing. Agents will otherwise reach for `TextStyle(fontSize: …)`.
- **Component themes:** ship `FilledButtonThemeData`, `OutlinedButtonThemeData`, `CardThemeData`, `InputDecorationTheme`, `NavigationBarThemeData`, `DialogThemeData`, `ChipThemeData` and similar, with shapes, padding and state layers from component tokens. This is where the brand lives. Defaults are where "stock M3" lives.
- **ThemeExtension for everything M3 doesn't model.** ThemeExtension is the official, type-safe way to add custom tokens, and implementing `copyWith` and `lerp` lets theme changes animate. Use it for spacing, radii, motion (durations/curves), elevation/shadows, and finance semantics (gain/loss/risk). Access it via `Theme.of(context).extension<AppSpacing>()!`, and wrap that in a `context.space` getter so agents have one obvious idiom.
- **Dynamic color:** for regulated, trust-critical surfaces such as wallet balances, trade confirmations and disclosures, *disable* Android 12+ dynamic color. Brand recognition and consistent risk/gain semantics matter more than wallpaper harmony, and dynamic palettes can break validated contrast pairs. If a product wants it, allow harmonizing only non-semantic accents, and re-run contrast checks across generated schemes.
- **Material decoupling:** migrate imports to `package:material_ui` (Flutter's `dart fix` does this). Pin the version in the adapter, because Material now releases weekly and M3 Expressive will land there. Treat each `material_ui` bump as a design-system release with golden-test review.

**Avoiding the "stock Material look":** (1) generate full schemes and component themes; (2) export *branded wrapper widgets* (`DsButton`) and tell agents in AGENTS.md to prefer them over raw `FilledButton`; (3) lint against raw Material widgets in feature code where a wrapper exists; (4) include a "what our UI is not" section in `intent.md` with screenshots of stock-M3 anti-patterns; (5) add an eval scenario that a critic agent scores for "generic M3."

**Figma → Flutter workflows:**
- **Figma MCP + Claude Code** is the primary path: the agent reads frames, variables and Code Connect mappings. Figma's remote server is recommended. The desktop server "doesn't support writing to the canvas." The `use_figma` write tool executes Plugin API JavaScript in a file. It needs a Full seat, and is free during the beta but slated to become usage-based.
- **Code Connect for Flutter:** framework-specific parsers stopped being maintained after August 17, 2026. Template files (`.figma.ts`) are "framework-agnostic," and the config's `language` list includes `dart`. You can publish Dart snippets for your `Ds*` widgets, and even a React and a Flutter snippet for the same Figma component, using separate configs with unique labels. Code Connect requires Organization/Enterprise plans. This is the single highest-leverage Figma step for agent accuracy.
- **Figma-to-Flutter plugins and community MCP servers** (Figma to Code, FigmaToFlutter, HuTouch, open-source Figma-Flutter MCP servers) generate widget trees. Treat them as prototyping aids. They don't know your theme or wrappers unless the harness tells them, so they tend to reintroduce hardcoded values.

**Flutter-relevant MCP servers and plugins:**
- **Official Dart & Flutter MCP server** (`dart mcp-server`, ships with the SDK, Dart 3.9+/Flutter 3.35+). It exposes analyzer diagnostics, symbol resolution, test runners and runtime introspection. Install via the official plugin (`claude plugin install dart-flutter@dart-flutter`), which bundles official Flutter/Dart skills. Add the **Developer Knowledge MCP server** for live docs search. Status: official, production-ready.
- **Widgetbook MCP server** (community project). It lists widgets, generates use cases, runs use-case tests and captures screenshots. The repo itself says it is "experimental and shouldn't be used in your production apps/design system." Pilot it in a sandbox only.
- **mcp_toolkit / flutter-mcp-toolkit** (community). It lets agents take semantic snapshots, tap widgets, hot-reload and read logs from a running app, which is useful for closed-loop behavioral checks. Status: community.
- I found no official "Material 3 MCP" server. Use the Developer Knowledge MCP and your own design-system MCP instead.

**Flutter guardrails:**
- **Lint:** Dart 3.10's analyzer plugins run custom rules inside `dart analyze`/`flutter analyze` and the IDE, and are expected to replace the third-party `custom_lint`, which needed a separate `dart run custom_lint`. Write rules such as: no `Color(0x…)`/`Colors.*` outside `generated/`; no numeric literals in `EdgeInsets`/`SizedBox`/`BorderRadius` (require `context.space.*`); no `TextStyle(fontSize:)` in features; prefer `Ds*` wrappers. Ship quick-fixes so agents can self-correct from the message. DCM (commercial) is an alternative with configurable banned-usage rules.
- **Visual verification:** golden tests (`matchesGoldenFile`) per component × brand × light/dark/high-contrast × text scale 1.0/2.0. Use Widgetbook as the browsable catalog for human review. Use the Dart MCP server so agents run tests and read failures themselves.
- **Accessibility tests:** Flutter's `meetsGuideline(textContrastGuideline)`, `androidTapTargetGuideline`, `iOSTapTargetGuideline` and `labeledTapTargetGuideline` in widget tests turn WCAG checks into computational sensors. The Flutter AI docs also list a "Flutter Accessibility agent" among official tools; evaluate it as an inferential reviewer.

### 5. Guardrails and verification loops (any stack)

**Sensors, ordered by ROI:**
1. **Token-compliance lint** (computational, every edit). ESLint/Stylelint for web and the analyzer plugin for Flutter. Wire it as a Claude Code `PostToolUse` hook so violations come back inside the agent's loop, not at PR time. Write messages as fix instructions ("Use `color.text.subtle` via `context.colors.textSubtle`").
2. **Contract checks.** Validate component usage against `*.contract.yaml`: required props such as accessible labels, and allowed variants.
3. **Automated accessibility.** axe-based checks for web (Storybook MCP can run "component and accessibility tests"), Flutter guideline matchers, and DESIGN.md contrast lint on token pairs. Deque's 2021 study of 2,000+ audits found automated testing catches about 57 percent of issues by volume, but only a minority of WCAG success criteria, so keep manual audits for flows.
4. **Visual regression.** Storybook/Chromatic-style snapshots for web and goldens for Flutter. Have agents attach screenshots to PRs; Vercel's design agent posts full-page screenshots back to the thread.
5. **Critic agents (inferential).** A separate reviewer agent with its own context and no stake in the output. It compares screenshots against Figma frames and principles, and runs a content/disclosure reviewer. Separating generator from evaluator counters self-evaluation bias.
6. **Human gate.** Design review on PRs touching patterns, and compliance review on customer-facing copy. At the AI Design Systems Conference 2026, a member of GitHub's Primer team described how agents in the Primer design system "can only create an issue, never merge code."

**Turning failures into rules (the harness flywheel).** For every recurring failure, decide where the fix belongs: a *rule* (prose in a skill or principle), a *primitive* (a new token, component or wrapper the agent can't misuse), a *check* (a lint rule or test), or an *eval scenario*. Vercel's practice is the model: weekly production feedback from Slack, GitHub and Figma becomes "new rules, primitives, or evals," and a correction often lands in two places, "a new rule in design.md, plus a code check." Prefer primitives and checks over prose. As the design-systems consultancy Southleft puts it, "A model can be talked around. A schema can't."

**Measuring harness quality:**
- **Eval suite:** 5–10 frozen scenarios per product line, such as a fund-detail page, a wallet send flow, or an agent response with a risk disclosure. Run them on each harness release and on each model change. Record prompt, inputs, model, harness version, screenshots and human ratings, as Vercel does.
- **Metrics:** token-compliance rate (share of style values resolved through tokens vs. literals, measured by lint across repos); DS component adoption rate (DS vs. ad-hoc widgets); known-failure count per scenario (Vercel's metric); a11y violations per screen; golden diff churn; token usage and tool calls per task (Atlassian's and BILL's metrics); time to merge; and the human-rejection rate at the design gate.
- **Drift metrics:** Figma-vs-DTCG variable diff count; generated-file staleness (`--check` failures); DESIGN.md `diff` regressions; versions behind latest core per repo.
- **Read transcripts, not just dashboards.** Atlassian found that a benchmark shows whether the agent succeeded, while the transcript shows whether it succeeded the way you intended.

### 6. Multi-project distribution and governance

**Distribution channels (use several, all generated from the core):**
- **Claude Code plugin marketplace.** A git repo with `.claude-plugin/marketplace.json`. Plugins can bundle skills, agents, hooks, MCP server configs and LSP servers. Repos auto-enable it via `extraKnownMarketplaces`/`enabledPlugins` in a committed `.claude/settings.json`. On Team/Enterprise plans, owners can distribute plugins org-wide via **Organization settings > Plugins & skills**, mark them "Required," and restrict user uploads. This is the cleanest channel for your skills and hooks.
- **Design-system MCP server and/or CLI.** One hosted, auth-scoped server serving tokens, component contracts and docs to every repo and tool (Uber, Atlassian, BILL). Offer a CLI too: it works where MCP doesn't, and Atlassian found it cheaper. Commercial options include Supernova Relay (official remote MCP, read-only, 14 tools) with per-team scoped "AI Context Management" endpoints (shipped June 22, 2026), and Knapsack's MCP.
- **Packages.** npm for web tokens/components; pub (private registry or git dependency) for `ds_flutter`. Prefer packages over git submodules. Submodules are workable for a docs-only core but give poor version visibility and are easy to leave stale.
- **Generated exports** (Guidelines.md for Figma Make, DESIGN.md for Stitch and one-off tools), published as release assets with a stable URL, as Vercel did with `vercel.com/design.md`.

**Versioning and change management:** SemVer the core. Token renames or removals are major. Use DTCG `$deprecated` with a migration window and codemods or `dart fix`-style fixes. Release notes go to humans *and* into a `CHANGELOG.md` the agent reads. Bots open bump PRs in consuming repos. Run the eval suite in the core's CI before every release, so harness changes are tested the way code is.

**Ownership model (recommended):**
- **Design-system team owns** tokens, contracts, principles, a11y rules, core skills, the MCP server/CLI, the eval suite and DESIGN.md generation.
- **Platform/adapter owners** (one per stack) own theme generation, lint plugins, goldens and wrappers.
- **Product teams own** local AGENTS.md additions, product-specific skills, and proposing rules through a contribution path (issues/PRs against the core with a failing eval scenario attached).
- **Compliance/legal co-own** `disclosures.md` and the disclosure components. Changes require their approval via CODEOWNERS.
- Southleft's accountability test applies: "what rejects the agent's output, and who decided the rule it's being rejected against?" Each rule should have a named owner.

**Separate brands without separate harnesses.** Several products or brands should share the core (principles, a11y, disclosure rules, token *structure*, skills) and differ by brand token sets and pattern libraries. Use the DTCG Resolver module or Style Dictionary themes for brand × mode permutations.

**Avoiding Figma ↔ tokens ↔ code drift:** one direction of authority per artifact (values: DTCG in git; component anatomy: Figma plus contract; code: adapter); CI sync checks; Code Connect on every published component; and scheduled "garbage collection" agent runs that scan repos for literals and deprecated tokens and open PRs, per OpenAI's entropy-management practice.

### 7. Financial-services considerations

**Accessibility compliance:**
- The **European Accessibility Act** has applied since June 28, 2025 to consumer banking services (including certain investment services) and e-commerce. The Dutch regulator AFM expects information to be accessible "via more than one sensory channel." Transitional periods run to 2030 for pre-existing contracts and products. EAA conformance is presumed via EN 301 549, which currently tracks WCAG 2.1.
- In the US, the DOJ's Title II rule (WCAG 2.1 AA) binds state and local governments, not private firms. Its deadlines moved to April 26, 2027 (large entities). Practitioners read it as signaling the standard DOJ could eventually apply under Title III.
- **WCAG 2.2** became ISO/IEC 40500:2025 in October 2025.
- **Recommendation:** target WCAG 2.2 AA in the harness. It's a superset of 2.1, adding focus-not-obscured, target size minimum and accessible authentication, all highly relevant to trading and wallet flows. Encode each criterion as a testable rule.

**Regulatory and disclosure content rules:**
- FINRA Rule 2210 requires communications to be "fair and balanced" and "provide balanced treatment of risks and potential benefits." FINRA guidance says "Material information in a communication may not be buried in footnotes," and communications generally "may not predict or project performance."
- FINRA Regulatory Notice 24-09 (June 2024) states the Rule 2210 content standards apply "whether member firms' communications are generated by a human or technology tool."
- Regulatory Notice 26-14 (July 2026, a *proposal* out for comment) reiterates that firms remain responsible for their communications whether a person or an AI tool produced them.
- For crypto, FINRA's sweep reviewed over 500 crypto-related retail communications. It asks whether risks are fairly presented and whether crypto-futures funds "falsely imply… direct exposure." The 2025 oversight report calls for "clearly and prominently identifying" non-broker-dealer affiliates responsible for crypto businesses. That matters directly for a self-custody wallet alongside brokerage products.
- **Harness implications:**
  - Make disclosures *components with required slots*, not free text. A `DsRiskDisclosure` must render at a minimum prominence adjacent to the claim, never in a collapsed footer.
  - Maintain a banned/flagged phrase list ("guaranteed," "risk-free," "safe as cash," performance projections) enforced by a content lint plus a compliance-critic agent.
  - Route all customer-facing copy changes through compliance CODEOWNERS.
  - For conversational/agentic UI, add patterns for AI-generated-content labeling, citation of sources, and escalation to human advisors. Treat agent responses as communications.

**Trust and safety patterns** (encode as patterns with contracts): explicit review-and-confirm steps for trades and transfers; irreversible-action friction for self-custody sends (address verification, network and fee clarity, no dark-pattern urgency); fee transparency on investment pages; clear separation of brokerage vs. affiliate/crypto products; and accessible authentication (WCAG 2.2 3.3.8).

**Security of agent access to design and code sources:**
- **MCP risks.** The MCP specification's security best practices require that servers "MUST NOT accept any tokens that were not explicitly issued for the MCP server," and they address confused-deputy and SSRF risks. Invariant Labs documented *tool poisoning*: malicious instructions hidden in tool descriptions "invisible to users but visible to AI models," plus "rug pulls" where descriptions change after approval. OWASP's Top 10 for Agentic Applications (December 2025) lists Agentic Supply Chain (explicitly including MCP servers), Tool Misuse and Identity & Privilege Abuse, under a principle of "Least Agency."
- **Figma write access.** `use_figma` runs Plugin-API JavaScript in a file. A prompt-injected agent with a Full seat could modify library files.
- **Controls:**
  - Read-only by default: design-system MCP servers should be read-only, as Supernova Relay explicitly is.
  - Allowlist MCP servers via managed settings and the org plugin marketplace. Use the "Required" and restricted-upload policies.
  - Pin plugin and MCP versions, and review description changes.
  - Grant write-to-canvas only on branch/sandbox files, never on the published library.
  - Keep production credentials and customer data out of prototype environments. Use synthetic data in React and Claude Code prototypes.
  - Agents propose and humans merge on protected branches.
  - Log agent tool calls for audit. Supervisory obligations under FINRA 24-09 make this prudent.

### 8. Tooling landscape (with maturity notes)

| Tool | What it gives the harness | Maturity (Nov 2026) |
|---|---|---|
| **Figma MCP server** | Frames, variables, components and Code Connect into agents; remote server can write to canvas (`use_figma`) | Read: production. Write: **beta**, Full seat, future usage-based pricing |
| **Figma Code Connect** | Maps Figma components to real code snippets, any language incl. `dart`, via template files | **Stable**; v2.0.0 made templates the only maintained path (parsers frozen Aug 17, 2026); Org/Enterprise plans |
| **Figma Make + Guidelines.md** | Generative prototyping steered by a guidelines file | Production; generate Guidelines.md from the core rather than hand-maintaining it |
| **Storybook MCP** (Storybook's `addon-mcp` package) | Component docs/props, story previews, component and a11y tests; remote publishing; composition across Storybooks | Production for **React** (Storybook 10.3+); docs toolset needs a components manifest (React, Angular-Vite, Vue3-Vite only); **no Flutter** |
| **Google Stitch + DESIGN.md** | AI design tool; DESIGN.md import/export; CLI lint/diff/export; Stitch skills | Stitch: Google Labs product. DESIGN.md: **alpha** |
| **Style Dictionary** | DTCG → multi-platform code incl. custom Dart formats | **Stable** (v4 DTCG first-class; full 2025.10 support WIP in v5) |
| **Tokens Studio** | Figma plugin for DTCG tokens, git sync; reference implementation of DTCG | Stable; widely used |
| **Supernova** | Relay remote MCP (read-only, OAuth, 14 tools) + per-team scoped AI Context Management | Commercial; context management shipped June 2026 |
| **Knapsack** | Docs MCP endpoint; DS platform | Commercial; not deeply evaluated here |
| **zeroheight** | Docs platform; Design Systems Report 2026; maturity model with an AI-readiness axis | Commercial; useful for benchmarking |
| **Dart & Flutter MCP + `dart-flutter` plugin** | Analyzer, tests, runtime introspection, official skills | **Official, production** |
| **Widgetbook MCP** | Widget catalog ops, use-case tests, screenshots | **Experimental community project** |
| **Atlassian ADS MCP/CLI** | Reference implementation of the "one source, many surfaces" pattern (public MCP endpoint) | Production; study it even though it serves ADS |
| **Kilo** and other agent IDEs | Alternative agent harnesses | Not evaluated in this research; apply the same AGENTS.md/skills/MCP pattern, since AGENTS.md is the cross-tool convention |

## Recommendations: Adoption Path

**First (weeks 0–6): make the system legible and measurable.**
1. Pick one pilot flow per product line, such as a wallet send flow or an agent answer with a disclosure. Write 5–10 frozen eval scenarios, and run them *before* changing anything to get a baseline.
2. Stand up `design-harness-core` with a short AGENTS.md, `principles/` (intent, a11y, disclosures, trust patterns), and semantic DTCG tokens exported from Figma Variables.
3. Generate Guidelines.md for Figma Make and CLAUDE.md imports from the core. Stop hand-editing per project.
4. Turn on Figma MCP (read) and the official Dart & Flutter MCP server, plus the `dart-flutter` plugin in the Flutter project.

**Next (months 2–4): add computational guides and sensors.**
5. Build the Style Dictionary pipeline that emits the `ds_flutter` theme (full ColorScheme, TextTheme, component themes, ThemeExtensions) and the web theme. Add a CI staleness check.
6. Ship the Dart 3.10 analyzer plugin (no raw colors/spacing/text styles; prefer `Ds*` wrappers) and the equivalent ESLint/Stylelint rules. Wire both as Claude Code hooks.
7. Golden tests and Flutter a11y guideline tests for every `Ds*` component; Widgetbook catalog; Storybook + MCP for React prototypes.
8. Publish Code Connect templates (Dart and React) for top components.
9. Package skills and hooks as a private Claude Code plugin marketplace. Distribute via org settings and mark core skills Required.

**Later (months 4–9): scale and govern.**
10. Stand up a read-only design-system MCP server and CLI generated from the core, or adopt Supernova/Knapsack if buying.
11. Add critic agents (design and compliance) and a scheduled drift-cleanup agent.
12. Generate DESIGN.md per brand as an export, linted in CI, for Stitch and external tools.
13. Formalize governance: CODEOWNERS (DS team, platform owners, compliance), SemVer, deprecation windows, monthly harness review of eval trends and top failures.
14. Re-run evals on every model upgrade and every `material_ui` bump.

## Stack-Agnostic Checklist

- [ ] AGENTS.md ≤ ~100 lines: map, non-negotiables, verification commands; CLAUDE.md imports it
- [ ] Generated, marked AGENTS.md block in every consuming repo pointing to plugin, MCP/CLI and adapter
- [ ] Semantic three-tier DTCG tokens with usage constraints in `$description`; brand × mode via resolver/themes
- [ ] Component contracts (anatomy, variants, states, a11y requirements, do/don't) in machine-readable form
- [ ] Principles: intent and anti-patterns, voice, WCAG 2.2 AA rules, disclosures, trust patterns, with owners
- [ ] Skills for build-screen, audit-a11y, write-disclosure-copy, review-design, figma-to-code
- [ ] Single source → generated surfaces (MCP, CLI, skills, Guidelines.md, DESIGN.md, llms.txt); no hand-edited copies
- [ ] Lint banning hardcoded colors, spacing and type, with fix-instruction messages, run as agent hooks and in CI
- [ ] Visual regression/goldens per component × theme × text scale; screenshots attached to PRs
- [ ] Automated a11y checks plus scheduled manual audits of critical flows
- [ ] Critic agents separated from generators; human design and compliance gates on protected branches
- [ ] Frozen eval scenarios with baseline; metrics: token-compliance rate, DS adoption, known failures, a11y violations, tokens/tool calls per task
- [ ] Figma ↔ DTCG sync check; Code Connect on published components; drift-cleanup agent
- [ ] Read-only MCP by default; allowlisted servers/plugins; pinned versions; no prod data in prototypes; audit logs
- [ ] Failure triage loop: each recurring failure becomes a rule, primitive, check or eval

## Caveats, Open Questions and Immature Areas

- **Evidence is thin and mostly self-reported.** Most quantitative results come from the companies' own blogs: Atlassian's 4.9%/34%/16%, Vercel's 57%, BILL's 31–63%, Uber's usage counts. Vercel itself notes its six-page comparison is "too few to claim quality." Secondary reports such as Miro's 70–80% drop in design-system Slack support questions (per an Into Design Systems recap of May 2026) and GitHub Primer's issue-only policy (AI Design Systems Conference 2026) come from conference recaps, not primary write-ups. Run your own baseline evals before committing budget.
- **DESIGN.md may change under you.** It is alpha, with spec, schema and CLI "under active development," and it has no Dart/Flutter export. Its long-term relationship to DTCG is unresolved. Generating it, rather than authoring it, insulates you.
- **The "harness" vocabulary is new and contested.** Definitions vary between Thoughtworks (guides/sensors), OpenAI (environment + constraints + garbage collection) and HumanLayer (a subset of context engineering). Use the guides/sensors frame internally for clarity, not as an industry standard.
- **Flutter is in transition.** `material_ui` 1.0.0 matches the old in-framework state. M3 Expressive is still forthcoming, and old imports face deprecation. Expect golden churn when Expressive lands, and pin versions.
- **Flutter tooling gaps vs. React.** There is no official Storybook-MCP equivalent for Flutter. Widgetbook MCP is experimental, and analyzer plugins are new (Dart 3.10). Expect to build more of the Flutter sensors yourself.
- **Figma write-to-canvas pricing and security.** `use_figma` is beta, will become usage-based, and executes arbitrary Plugin-API code. Govern it tightly.
- **Regulatory flux.** FINRA's Rule 2210 modernization (Notice 26-14) is a proposal, and the final treatment of AI-generated and interactive communications is pending. I found no 2024–2026 SEC primary guidance specific to AI-generated UI marketing. Confirm with your compliance team.
- **Automated a11y has a ceiling.** Contrast, tap-target and label checks catch only part of WCAG 2.2 (Deque's study puts automated coverage at about 57 percent of issues by volume, not of success criteria). Cognitive load, focus order in complex flows and screen-reader narrative for charts still need humans.
- **Prose rules degrade at scale.** Every line added to an always-loaded file competes for attention. Push rules down into primitives and checks wherever possible, and keep evals as the arbiter of what earns a place in the prose.

## Sources

- [Harness Engineering for Coding Agents: What It Is (2026)](https://www.agentastic.dev/harness-engineering) · agentastic.dev
- [(Complete Guide) Harness Engineering Thoroughly Explained! An Era Where AI Agent Design Skills Make the Dif…](https://note.com/masa_wunder/n/n1858477a1136?hl=en) · note.com
- [What Is Harness Engineering for AI Agents?](https://milvus.io/blog/harness-engineering-ai-agents.md) · milvus.io
- [Atlassian's DESIGN.md is here: what we learned testing portable design context in practice - Inside Atlassian](https://www.atlassian.com/blog/how-we-build/atlassians-design-md-is-here-what-we-learned-testing-portable-design-context-in-practice) · atlassian.com
- [Teaching AI to speak our design language - Inside Atlassian](https://www.atlassian.com/blog/ai-at-work/teaching-ai-to-speak-our-design-language) · atlassian.com
- [Further reading · State of AI in Design Systems](https://state-of-ai-in-design-systems.netlify.app/reading) · state-of-ai-in-design-systems.netlify.app
- [How our agents build on-brand pages with design.md - Plushcap](https://www.plushcap.com/content/vercel/blog/vercel-how-our-agents-build-on-brand-pages-with-designmd) · plushcap.com
- [Material and Cupertino decoupling are here](https://flutter.dev/blog/decoupling-material-cupertino) · flutter.dev
- [Announcing Dart 3.10](https://dart.dev/blog/announcing-dart-3-10) · dart.dev
- [Get started developing with AI](https://docs.flutter.dev/ai/get-started) · docs.flutter.dev
- [How Flutter AI tools work](https://docs.flutter.dev/ai/tools) · docs.flutter.dev
- [Writing template files](https://developers.figma.com/docs/code-connect/template-files/) · developers.figma.com
- [Configuring your project](https://developers.figma.com/docs/code-connect/api/config-file/) · developers.figma.com
- [Skill Issue: Harness Engineering for Coding Agents](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents) · humanlayer.dev
- [Harness Engineering Guide: Build Systems That Make AI…](https://www.nxcode.io/resources/news/harness-engineering-complete-guide-ai-agent-codex-2026) · nxcode.io
- [openai harness engineering codex](https://www.infoq.com/news/2026/02/openai-harness-engineering-codex) · infoq.com
- [Giving AI agents design system context from the terminal: what we learned building a CLI - Inside Atlassian](https://www.atlassian.com/blog/ai-at-work/giving-ai-agents-design-system-context-from-the-terminal-what-we-learned-building-a-cli) · atlassian.com
- [Ads cli package - Atlassian Frontend Development - Atlaskit](https://atlaskit.atlassian.com/packages/design-system/ads-cli) · atlaskit.atlassian.com
- [Design Tokens Community Group](https://styledictionary.com/info/dtcg/) · styledictionary.com
- [export-design-tokens-dtcg: Export design tokens from YAML to W3C DTCG JSON with validation and platform bun…](https://skills.rest/skill/export-design-tokens-dtcg-gabrielnsmnto) · skills.rest
- [Design Tokens: as a design system in Flutter projects](https://insights.overapp.com/design-tokens-ed33db06fa43?gi=3dbda6f2dc24) · insights.overapp.com
- [Design Tokens JSON: The DTCG Format Explained · Livery](https://www.livery.site/guides/design-tokens-json-format) · livery.site
- [Theming and Customization in Flutter: A Handbook for Developers](https://www.freecodecamp.org/news/theming-and-customization-in-flutter-a-handbook-for-developers/) · freecodecamp.org
- [Flutter 3.47+: Material UI Is Now a Package](https://itzpkyadav.medium.com/flutter-3-47-material-ui-is-now-a-package-what-developers-need-to-know-78488a072909) · itzpkyadav.medium.com
- [How to Work with Material and Cupertino Decoupling in Flutter (Full Handbook)](https://daily.dev/posts/how-to-work-with-material-and-cupertino-decoupling-in-flutter-full-handbook--r3kt6va11) · daily.dev
- [Get started with the Figma MCP server](https://help.figma.com/hc/en-us/articles/39216419318551-Get-started-with-the-Figma-MCP-server) · help.figma.com
- [figma/mcp-server-guide: A guide on how to use the Figma MCP server](https://github.com/figma/mcp-server-guide) · github.com
- [write to canvas](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas) · developers.figma.com
- [Releases · figma/code-connect](https://github.com/figma/code-connect/releases) · github.com
- [Figma to Flutter Guide 2026: Tools & Workflow](https://hedrick.io/post/figma-to-flutter-guide) · hedrick.io
- [Transferring your Figma design into Flutter code - LogRocket Blog](https://blog.logrocket.com/ux-design/transferring-figma-design-flutter-code/) · blog.logrocket.com
- [HuTouch](https://www.figma.com/community/plugin/1576201417321638566/hutouch) · figma.com
- [The Dart and Flutter MCP Server: What It Gives Your AI Assistant](https://www.bidev.dev/blog/dart-flutter-mcp-server-explained) · bidev.dev
- [Dart and Flutter MCP Server - Official AI Assistant Integration for Flutter & Dart](https://a2a-mcp.org/entry/flutter-mcp) · a2a-mcp.org
- [mcp_toolkit - Dart API docs](https://pub.dev/documentation/mcp_toolkit/latest/) · pub.dev
- [Lint Smarter, Not Harder: Migrate to the New Dart Analyzer Plugin System](https://leancode.co/blog/migrating-to-dart-analyzer-plugin-system) · leancode.co
- [Design Systems for AI Agents: 2026 Guide](https://www.designme.agency/insights/design-systems-ai-agents-can-build-with-tokens-components-and-rules) · designme.agency
- [Storybook MCP for React](https://storybook.js.org/blog/storybook-mcp-for-react/) · storybook.js.org
- [Vercel DESIGN.md: Markdown Design System for AI (2026)](https://explainx.ai/blog/vercel-design-md-spec-driven-ai-ui-rauchg-2026) · explainx.ai
- [Harness Engineering: How OpenAI Used Codex to Ship 1 Million Lines Without Writing a Single One](https://saascity.io/blog/harness-engineering-codex-agent-first-openai-2026) · saascity.io
- [After 200+ Runs, Vercel Figured Out How to Teach Agents What Good Design Looks Like](https://www.frxiaobei.com/en/posts/2026/09/vercel-design-md-agent-engineering/) · frxiaobei.com
- [Vercel Launches design.md for On-Brand Pages](https://aicrier.com/post/dw5biryp4qrpz7tdhugd) · aicrier.com
- [Claude Code Plugins Complete Guide - Bundling Skills, Hooks, Agents, and MCP Servers for Team Distribution](https://hidekazu-konishi.com/entry/claude_code_plugins_complete_guide.html) · hidekazu-konishi.com
- [How to Build an Internal Skills Marketplace for Claude Code with GitHub · BetterFutureLabs](https://betterfuturelabs.com/insights/internal-skills-marketplace-claude-code-github) · betterfuturelabs.com
- [Claude Marketplace: How to Add a Plugin Marketplace](https://felloai.com/claude-marketplace/) · felloai.com
- [Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization) · support.claude.com
- [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) · support.claude.com
- [Platforms - State of AI in Design Systems - Netlify](https://state-of-ai-in-design-systems.netlify.app/platforms) · state-of-ai-in-design-systems.netlify.app
- [Accessibility of (digital) financial services](https://www.afm.nl/en/sector/themas/dienstverlening-aan-consumenten/toegankelijkheid) · afm.nl
- [The European Accessibility Act: What should financial services firms be focusing on as the June 2025 compli…](https://www.hlc.com/en/publications/the-european-accessibility-act-what-should-financial-services-firms-be-focusing-on-as-the-june-2025) · hlc.com
- [European Accessibility Act (EAA) 2025](https://www.tuwebaccesible.es/en/regulations/european-accessibility-act-of-2025/) · tuwebaccesible.es
- [WCAG 2.2 - Web Content Accessibility Guidelines](https://quality.arc42.org/standards/wcag-2-2) · quality.arc42.org
- [DOJ Extends Title II ADA Web Accessibility Rule Compliance Deadlines for State and Local Governments](https://www.consumerfinancialserviceslawmonitor.com/2026/04/doj-extends-title-ii-ada-web-accessibility-rule-compliance-deadlines-for-state-and-local-governments/) · consumerfinancialserviceslawmonitor.com
- [ADA Web Accessibility Rule: WCAG 2.1 AA Deadlines for State and Local Governments](https://titleii.org/web-accessibility-rule) · titleii.org
- [WCAG 2.2 Is Now an ISO Standard: What This Means for ...](https://www.clym.io/blog/wcag-22-is-now-an-iso-standard-what-this-means-for-your-websites-accessibility-strategy) · clym.io
- [Current Work](https://www.w3.org/WAI/) · w3.org
- [FINRA RULES RULE 2210 COMMUNICATIONS WITH THE PUBLIC 1](https://www.finra.org/sites/default/files/2019-10/2019_AR_Rules_Reference_Guide.pdf) · finra.org
- [Social Media](https://www.finra.org/rules-guidance/key-topics/social-media) · finra.org
- [Regulatory Notice 24-09](https://www.finra.org/rules-guidance/notices/24-09) · finra.org
- [Regulatory Notice 24-09: FINRA Generative AI Obligations](https://www.bankingnewsai.com/ai-regulation/documents/finra-regulatory-notice-24-09) · bankingnewsai.com
- [FINRA Seeks to Modernize Rule 2210](https://www.hklaw.com/en/insights/publications/2026/07/finra-seeks-to-modernize-rule-2210-communications-with-the-public) · hklaw.com
- [Regulatory Notice 26-14](https://www.finra.org/rules-guidance/notices/26-14) · finra.org
- [FINRA Provides Update on Targeted Exam: Crypto Asset Communications](https://www.finra.org/rules-guidance/guidance/sweep-letters-and-updates/update-crypto-asset-communications) · finra.org
- [Member Firms’ Nexus to Crypto](https://www.finra.org/rules-guidance/guidance/reports/2025-finra-annual-regulatory-oversight-report/crypto) · finra.org
- [modelcontextprotocol](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) · modelcontextprotocol.io
- [MCP Tool Poisoning: Adversarial Hijacking of AI Agent Workflows](https://labs.cloudsecurityalliance.org/research/csa-research-note-mcp-tool-poisoning-ai-agent-exfiltration-2/) · labs.cloudsecurityalliance.org
- [MCP Security Notification: Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) · invariantlabs.ai
- [OWASP Top 10 for Agentic Applications 2026](https://cycode.com/blog/owasp-top-10-agentic-applications/) · cycode.com
- [Lessons from OWASP Top 10 for Agentic Applications](https://auth0.com/blog/owasp-top-10-agentic-applications-lessons/) · auth0.com
- [OWASP Top 10 for Agentic Applications: Securing Agentic AI with F5](https://www.f5.com/glossary/owasp-top-10-for-agentic-ai-applications) · f5.com
- [Storybook MCP: Setup, Prompts & Alternatives (2026)](https://www.paralect.com/mcp/storybook) · paralect.com
- [Storybook MCP Server](https://apis.io/apis/storybook/storybook-mcp/) · apis.io
- [Overview - With AI - Atlassian Design](https://atlassian.design/get-started/develop/with-ai) · atlassian.design
- [What Is DESIGN.md? Google Stitch's Open-Source Format for AI Design Systems Explained](https://mindwiredai.com/2026/04/23/design-md-is-now-open-source-googles-new-file-format-that-makes-ai-build-your-brand-correctly/) · mindwiredai.com
- [google-labs-code/design.md: A format specification for describing a visual identity to coding agents. DESIG…](https://github.com/google-labs-code/design.md) · github.com
