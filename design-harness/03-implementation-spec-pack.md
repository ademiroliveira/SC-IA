# Wallet design harness: implementation spec pack

7 November 2026. A generic case: a Flutter self-custody wallet team that can't use MCP, runs self-hosted open-weight models and has a small frontier budget.

## How to use this pack

This pack turns the design harness plan into seven buildable specs, a test plan and governance rules. Any of them can be handed to an engineer or to an agent (self-hosted GLM 5.3 in OpenCode, or GitHub Copilot) without carrying files over. Background and evidence are in the companion report, `02-research-without-mcp.md`.

Every spec has the same parts:

- **Purpose:** one line on why it exists.
- **Depends on, owner, built with:** what must exist first, who signs it off, and which model writes the first version.
- **Requirements:** numbered, using MUST and SHOULD.
- **Acceptance criteria:** checks that pass or fail, with no judgement calls.
- **Build brief:** text to paste into OpenCode or GitHub Copilot, together with the requirements, to generate the first version.

Use one spec per agent session. Paste the requirements, acceptance criteria and build brief, and nothing else. The agent must run the listed checks before it says it's done. A person owns each spec and reviews what the agent produced.

Ready-to-paste prompts for every step, from building a spec to getting unstuck, are in the Prompt playbook near the end.

| # | Spec | Phase | Depends on | Owner | Built with |
| --- | --- | --- | --- | --- | --- |
| 1 | Token architecture and naming rules | Weeks 1–2 | — | Design system lead | Frontier model, then human review |
| 2 | Token pipeline | Weeks 3–6 | 1 | Flutter lead | GLM 5.3 |
| 3 | Audit script and compliance metric | Weeks 1–2 | Draft of 1 | Flutter lead | GLM 5.3 |
| 4 | Lint rules and ratchet | Week 2 onwards | 1, 3 | Flutter lead | GLM 5.3; frontier writes the messages |
| 5 | Golden, accessibility and wallet tests | Weeks 3–6 | 2 | Flutter lead and QA | GLM 5.3; people approve images |
| 6 | Agent layer | Weeks 3–6 | 1–5 | Design system lead and Flutter lead | Frontier writes skills; GLM writes config |
| 7 | Figma migration | Audit in weeks 1–2; migration in months 2–3 | 1, 2 | Design system designer | Figma agent and native import |
| — | Test plan | Weeks 1–2, then ongoing | — | Design system lead | GLM 5.3, Flash and frontier |
| — | Governance | From week 0 | — | Design system lead, Flutter lead, security | — |

### Roadmap

| Phase | When | Work | Gate: both checks must be true |
| --- | --- | --- | --- |
| Set up | Week 0 | Confirm OpenCode version and Flash model; check serving and admin settings; agree protected zones and owners | Week 0 checklist done; serving config recorded |
| Measure | Weeks 1–2 | Spec 1 tokens and naming rules (draft); Spec 3 audit script; Figma read-only audit; test plan run 1 (baseline, no skills) | Naming rules approved; baseline scores logged |
| Build the core | Weeks 3–6 | Spec 2 pipeline; Spec 4 lint rules; Spec 5 tests on the send flow; Spec 6 AGENTS.md, skills, agents, hooks | Send flow passes checks; skills beat the baseline |
| Migrate and govern | Months 2–3 | Spec 7 Figma import, mapping, relinking; migrate screen by screen, protected screens last; governance | Compliance targets met; Figma drift is zero |

A phase starts only when both checks at the previous gate are true.

## Step by step

Twenty-two steps take the harness from setup to scale. Tick each one off as you go. "Prompt" refers to the Prompt playbook near the end.

### Week 0: set up

- [ ] **1. Run the week 0 checklist.**

  Who: design system lead, with platform, admins, security and legal. Done when: every setup check has an answer.
- [ ] **2. Fix the protected zones.**

  Who: design system lead, Flutter lead, security. Done when: the Governance table has real paths and named owners, including the design CODEOWNER for goldens.
- [ ] **3. Prepare the repo.**

  Who: Flutter lead. Add `docs/harness/spec-pack.md` and `docs/harness/research-report.md`, plus empty `.harness/plans/` and `.harness/stuck/` folders. Done when: they're merged to main.
- [ ] **4. Connect the self-hosted models to OpenCode.**

  Who: Flutter lead with platform. Spec 6c, item 1 only. Done when: GLM 5.3 edits a scratch file and runs `dart analyze` without tool-call errors.

### Weeks 1–2: measure

- [ ] **5. Draft the token architecture.**

  Who: design system lead. Where: GitHub Copilot, prompt 2 with Spec 1. Done when: the tokens skeleton and naming rules exist, with values still TODO.
- [ ] **6. Build the audit script.**

  Who: Flutter lead. Where: OpenCode with GLM 5.3, prompt 1 with Spec 3. Done when: all Spec 3 acceptance checks pass.
- [ ] **7. Audit the send flow.**

  Who: Flutter lead and design system lead. Run the audit, record the compliance rate as the baseline, and fill in the legacy mapping table from Spec 1. Done when: every finding in the send flow has a decision.
- [ ] **8. Audit Figma, read-only.**

  Who: design system designer. Write the audit skill with prompt 2 (Spec 7, audit skill only), then run prompt 10a on a branch. Done when: the audit table is on the canvas.
- [ ] **9. Write the test tasks.**

  Who: design system lead. Put real screen names into T1–T10. Done when: the task text is frozen.
- [ ] **10. Run the baseline.**

  Who: Flutter lead. Use prompt 8 with no skills: GLM 5.3 and Flash three times each in OpenCode; Sonnet 5.5 once, and Opus 5.5 on the three hardest, in GitHub Copilot. Done when: the scoring sheet is complete.
- [ ] **11. Approve the naming rules.**

  Who: design and engineering leads. Done when: Spec 1 is signed off apart from the contrast check, which needs step 12. **This passes the "Baseline in" gate.**

### Weeks 3–6: build the core

- [ ] **12. Build the token pipeline.**

  Who: Flutter lead. Where: OpenCode, prompt 1 with Spec 2. Then the design system lead fills in the real brand values. Done when: Spec 2 acceptance passes, including contrast.
- [ ] **13. Write the lint messages.**

  Who: design system lead. Where: GitHub Copilot, prompt 2 with Spec 4 (messages only). Done when: `docs/lint-messages.md` exists.
- [ ] **14. Build the lint plugin and ratchet.**

  Who: Flutter lead. Where: OpenCode, prompt 1 with Spec 4. Done when: the baseline is recorded and CI fails on a new violation.
- [ ] **15. Add the tests.**

  Who: Flutter lead and QA. Where: OpenCode, prompt 1 with Spec 5. A person approves every new golden. Done when: Spec 5 acceptance passes.
- [ ] **16. Write AGENTS.md and the three skills.**

  Who: design system lead. Where: GitHub Copilot, prompt 2 with Spec 6a and 6b. Done when: both hosts load them.
- [ ] **17. Configure the agents.**

  Who: Flutter lead. Where: OpenCode, prompt 1 with Spec 6c and 6d. Done when: the blocked actions are tested and denied in both hosts.
- [ ] **18. Prove the skills.**

  Who: design system lead. Re-run the test tasks with skills (prompt 8). Keep only the skills that beat the baseline, and set the model split in Spec 6e from the results. **This passes the "Skills proven" gate.**

### Months 2–3: migrate and govern

- [ ] **19. Migrate the non-protected screens.**

  For each screen:
  1. Flash swaps the exact matches (prompt 5).
  2. GLM 5.3 finishes the migration (prompt 4).
  3. A stuck report goes to prompt 6.
  4. The change is reviewed with prompt 7, and a person merges it.
- [ ] **20. Migrate the protected screens.**

  The same loop as step 19, plus an Opus 5.5 review (prompt 7) and design and security approval. These screens go last.
- [ ] **21. Migrate Figma.**

  Who: design system designer.
  1. Write the mapping and relinking skills (prompt 2, Spec 7).
  2. Import the variables in tier order.
  3. Run prompts 10b and 10c page by page.
  4. Do the re-import test.
  5. Publish from main.
- [ ] **22. Run the governance loop.**

  Who: design system lead and Flutter lead. CODEOWNERS and the CI protected-path check are live. Weekly triage (prompt 9) and a weekly credit review are running. **When compliance targets are met and Figma drift is zero, this passes the "Ready to scale" gate.** Then move on to the next flow.

## Requirements

The harness must make the token system the default path for every person and agent building wallet UI, and catch any deviation automatically, using only tools the organisation has already approved.

### Goals

1. **One source of truth.** A DTCG token file in the repo. The Flutter theme and the Figma variables are generated from it and never edited by hand.
2. **Agents build on the system.** Self-hosted models migrate and build screens that pass lint, golden and accessibility checks.
3. **Drift is caught automatically.** Hardcoded values, misused roles and edits to protected paths fail CI.
4. **Trust-critical screens are protected.** Agents can only change tokens there, and a person approves every change.
5. **Frontier credits last the month.** They go on reusable work: skills, lint messages, plans and reviews.

### Non-goals

- No MCP and no Claude Code.
- No automatic merging of agent changes.
- Agents never edit key-management or cryptography code.
- No visual redesign. A migrated screen looks the same unless design approves a change.
- No two-way Figma sync. Changes flow from code to Figma.
- No Material 3 Expressive adoption in this phase.

### Constraints

| Constraint | What it means for the build |
| --- | --- |
| No MCP, no Claude Code | Context comes from files, injected command output and command-line scripts |
| OpenCode with self-hosted GLM 5.3 and Flash | Default executors. Short sessions, about 128K tokens of working context |
| GitHub Copilot, a small budget (the examples assume about 4,000 credits, or US$40, a month) | Frontier models write rules and skills, plan, unblock and review. Not routine edits |
| Flutter, Dart 3.10 or later, Material 3 | Lint rules run as an analyzer plugin. Material version pinned |
| Figma file not aligned to M3 | Figma is migrated after the code tokens exist |
| Self-custody wallet in a regulated business | Protected zones, human review and an audit trail of agent changes |

### Success metrics

Targets are proposals for the design system lead to confirm once the week 1–2 baseline exists.

| Metric | How it's measured | Proposed target |
| --- | --- | --- |
| Token compliance rate | Audit script: style values that go through tokens ÷ all style values | 100% on protected screens; 95% on migrated screens |
| New lint violations merged | Lint ratchet in CI | 0 |
| Send-flow test tasks passed by GLM 5.3 | Test plan, passes all three runs | Above the no-skills baseline by an agreed margin |
| Golden changes approved by a person | Pull request labels and CODEOWNERS | 100% |
| Figma-to-code drift | Figma export compared with the token file at each release | 0 differing variables |
| Frontier credits | GitHub Copilot usage report, weekly | Within the monthly budget |
| Stuck reports per migrated screen | Count in the stuck-report folder | Falling month on month |

### Roles

| Role | Owns |
| --- | --- |
| Design system lead | Token architecture, naming rules, skills, test tasks, design approval of golden changes |
| Flutter lead | Token pipeline, audit script, lint rules, tests, CI, agent configuration |
| Design system designer | Figma migration and Figma agent skills |
| Security and platform | Model serving, OpenCode distribution, GitHub Copilot policy, Figma admin settings, protected-path review |
| Compliance | Any copy change on protected screens |

## Spec 1: Token architecture and naming rules

**Purpose:** define the token set and naming rules every other spec builds on.

**Depends on:** nothing. **Owner:** design system lead. **Built with:** a frontier model, once, then human review.

### Requirements

1. **Three tiers.** The set MUST have three tiers:
   - reference: raw values;
   - system: Material 3 roles;
   - extended: wallet roles that M3 doesn't have.

   Widgets MUST use system or extended tokens only, never reference tokens.
2. **Format.** Tokens MUST use DTCG 2025.10 JSON, with `$value`, `$type`, `$description` and aliases such as `{ref.palette.blue.40}`. Dimensions MUST be objects (`{"value": 16, "unit": "px"}`). Store them as one file per tier in `tokens/`.
3. **Paths.** Use lowercase group names and these patterns:
   - `ref.palette.<hue>.<tone>`
   - `sys.color.<role>`
   - `sys.typescale.<slot>.<property>`
   - `sys.shape.corner.<size>`
   - `sys.elevation.level<n>`
   - `ext.<group>.<role>`

   System role names MUST match Flutter's `ColorScheme` and `TextTheme` property names exactly (`onPrimaryContainer`, `bodyMedium`), so code mapping is one-to-one. Figma uses the same paths with `/`.
4. **Colour roles.** The system tier MUST define every `ColorScheme` role for both Light and Dark:
   - primary, secondary and tertiary families, each with on, container and fixed variants;
   - the error family;
   - surface, onSurface, onSurfaceVariant, surfaceDim and surfaceBright;
   - the five surfaceContainer levels;
   - outline and outlineVariant;
   - inverse roles, shadow, scrim and surfaceTint.

   No palette may be generated from a seed colour.
5. **Type scale.** All 15 slots (`displayLarge` to `labelSmall`) MUST each define font family, size, line height, weight and letter spacing.
6. **Extended tokens.** These are a proposal to confirm:
   - `ext.status.*`: success, warning and info, each with on and container variants;
   - `ext.finance.*`: gain, loss and neutral;
   - `ext.wallet.*`: address text (monospace) and risk banner;
   - `ext.space.*`: a 4-point scale;
   - `ext.motion.*`: durations and easing curves.
7. **Descriptions.** Every system and extended token MUST have a `$description` that says where it may be used, such as "Destructive actions only. Never for loss amounts". Agents read these.
8. **Contrast.** Every colour/onColour pair and every text-on-surface pair MUST meet WCAG 2.2 AA in every mode: 4.5:1 for body text, 3:1 for large text and UI parts. Pairs are listed in `docs/contrast-pairs.md` and checked by Spec 2.
9. **Deprecation.** A token is never renamed in place. The old name stays as an alias with `$deprecated` ("Use sys.color.x. Removed in v3") for two minor releases, then goes. Every change gets a CHANGELOG entry.
10. **Semantic names.** System and extended names MUST describe the role, not the value. `blue500` is allowed only in the reference tier.
11. **Versioning.** The token set follows semantic versioning. Renaming or removing a token is a major change.
12. **Dynamic colour.** It MUST be off on protected screens and brand surfaces.

### Acceptance criteria

- [ ] Style Dictionary parses `tokens/` with zero errors or warnings.
- [ ] Every `ColorScheme` role and all 15 type slots exist in Light and Dark.
- [ ] Every system and extended token has a `$description`.
- [ ] All contrast pairs pass in both modes.
- [ ] Design and engineering leads have approved `docs/naming-rules.md`, which runs to no more than two pages.
- [ ] A legacy mapping table exists, with columns: legacy name or value · where it's used · tier · new token · decision.

### Build brief (frontier model in GitHub Copilot)

> You are drafting the design-token architecture for an existing Flutter Material 3 mobile app. Follow requirements 1–12 exactly. Produce four files: (1) `tokens/` in DTCG 2025.10 with every ColorScheme role for Light and Dark, all 15 type slots, shape and elevation, with values as `TODO` references to `ref.palette`; (2) the extended tier from the starter list, with a `$description` on every token; (3) `docs/naming-rules.md` in under two pages; (4) `docs/contrast-pairs.md` listing every pair to check. Do not invent brand colour values. Output only the files.

## Spec 2: Token pipeline

**Purpose:** generate the Flutter theme and the Figma import files from the token files, so nobody edits either by hand.

**Depends on:** Spec 1. **Owner:** Flutter lead. **Built with:** GLM 5.3, with a frontier review of the Dart output formats.

### Requirements

1. **One command.** Style Dictionary 4 or later, version pinned, runs as `npm run tokens`. If npm isn't allowed, a Dart script that produces the same outputs.
2. **Flutter outputs** go in `lib/theme/generated/`, each file headed "GENERATED, do not edit":
   - `color_schemes.g.dart`: Light and Dark `ColorScheme` built with the full constructor, every role set explicitly;
   - `text_theme.g.dart`: all 15 slots;
   - `extensions.g.dart`: one `ThemeExtension` class per extended group, each with `copyWith` and `lerp`.
3. **Assembly.** A hand-written `app_theme.dart` builds `ThemeData` from the generated files: the colour schemes, text theme, extensions and component themes (`FilledButtonThemeData`, `CardThemeData`, `InputDecorationTheme` and so on). Component themes use tokens only.
4. **One accessor style.** Getters on `BuildContext`: `context.colors`, `context.text`, `context.space`, `context.wallet`. Agents and people use only these.
5. **Figma outputs** go in `build/figma/`, one DTCG file per collection and mode:
   - `reference.json`
   - `system.light.json` and `system.dark.json`
   - `extended.light.json` and `extended.dark.json`

   Paths use `/` grouping. Scopes and code syntax go under `$extensions.com.figma`; the code syntax is the Flutter accessor, such as `context.colors.primary`.
6. **Contrast check.** A script checks every pair in `docs/contrast-pairs.md` in each mode and fails the build below the Spec 1 thresholds.
7. **Staleness check.** CI runs the pipeline and fails if the generated files differ from what is committed. Output is run through `dart format`.
8. **Stable output.** Keys are sorted and formatting is fixed, so diffs stay reviewable.
9. **Material version.** The `material_ui` package version (or the Flutter SDK's Material) is pinned. Any upgrade is treated as a design-system release, with a golden test review.

### Acceptance criteria

- [ ] `npm run tokens` followed by `git diff --exit-code` passes on a clean checkout.
- [ ] The app builds with the generated theme, and `flutter analyze` shows no issues in `lib/theme/`.
- [ ] Every `ThemeExtension` has `copyWith` and `lerp`, and a unit test covers `lerp`.
- [ ] The five Figma files import into an empty test file without errors, in tier order.
- [ ] Two seeded pull requests fail CI: one with a stale generated file, one with a failing contrast pair.

### Build brief (GLM 5.3, migrator agent)

> Implement the token pipeline described in requirements 1–9. The input is `tokens/` in DTCG 2025.10. Write the Style Dictionary config and three custom formats: `flutter/color-scheme`, `flutter/text-theme` and `flutter/theme-extension`. Also write the Figma output config, `tool/tokens/check_contrast`, and the CI steps for the staleness and contrast checks. Done when `npm run tokens && git diff --exit-code` passes and `flutter analyze lib/theme` is clean. Don't edit anything outside `tool/tokens`, `lib/theme` and the CI file. If the same check fails twice, write a stuck report and stop.

## Spec 3: Audit script and compliance metric

**Purpose:** find every hardcoded style value and misused role, and output a worklist agents can execute and a compliance number people can track.

**Depends on:** a draft of Spec 1. **Owner:** Flutter lead. **Built with:** GLM 5.3.

### Requirements

1. **Command.** `dart run tool/ds_audit.dart <paths> --json <file> --summary`. It scans `lib/` and skips `lib/theme/` and generated files.
2. **Parsing.** It MUST parse the Dart syntax tree with `package:analyzer`, not use text search. It detects:
   - `Color(0x…)`, `Color.fromARGB`, `Color.fromRGBO` and `Colors.*`;
   - `withOpacity` or `withValues` on literal colours;
   - `TextStyle` with literal size, weight, family, height or letter spacing;
   - numeric literals in `EdgeInsets`, `SizedBox`, `Padding` and `BorderRadius`;
   - literal `BoxShadow`s;
   - `ColorScheme.fromSeed`;
   - dynamic colour used in a protected path;
   - raw Material widgets where a `Ds*` wrapper exists, from a configured list.
3. **Suggestions.** A shared rules file, `tool/ds_rules.yaml`, maps literals to tokens. Colours match on nearest perceptual distance, spacing on nearest step. Spec 4 reads the same file.
4. **Role misuse.** Flag a role used against its `$description`, such as `tertiary` used for success, using rules listed in the same file.
5. **Worklist schema.** One JSON object per finding:

   ```json
   {"file": "lib/features/send/amount_view.dart", "line": 42, "column": 18, "kind": "raw_color", "literal": "Color(0xFF1A73E8)", "suggestedToken": "context.colors.primary", "confidence": "exact", "protected": true, "screen": "send/amount"}
   ```

   `confidence` is `exact`, `nearest` or `none`. `screen` comes from the folder path.
6. **Compliance rate.** Style values that go through tokens divided by all style values, given per screen and overall, with protected screens listed separately. A CSV file is added to tracking each week.
7. **Modes.** Report mode always exits 0. `--fail-on-new baseline.json` exits 1 when there are findings not in the baseline. CI uses this mode until the lint plugin from Spec 4 lands.
8. **Speed.** It SHOULD run in under 60 seconds on the whole repo.

### Acceptance criteria

- [ ] On a fixture file with 20 seeded violations it finds all 20, and it finds nothing in a clean fixture.
- [ ] The output validates against the JSON schema in `tool/ds_audit.schema.json`.
- [ ] The send flow's compliance rate is recorded as the week 1–2 baseline.
- [ ] `--fail-on-new` fails a seeded pull request that adds one hardcoded colour.

### Build brief (GLM 5.3, migrator agent)

> Write `tool/ds_audit.dart` to requirements 1–8 using `package:analyzer` visitors, not regex. Write `tool/ds_rules.yaml` with the starter mappings from `docs/naming-rules.md`, write the JSON schema, and write fixtures in `test/ds_audit/`. Done when `dart test test/ds_audit` passes and `dart analyze tool` is clean. Don't edit `lib/`. If the same check fails twice, write a stuck report and stop.

## Spec 4: Lint rules and ratchet

**Purpose:** make the analyzer the teacher. Every violation shows up in `dart analyze` with an instruction the model can follow, and the number of violations can only go down.

**Depends on:** Specs 1 and 3. **Owner:** Flutter lead. **Built with:** GLM 5.3 builds the plugin; a frontier model writes the messages.

### Requirements

1. **Plugin.** A `ds_lints` package built on Dart's analyzer plugin system (Dart 3.10 or later), listed under `plugins:` in `analysis_options.yaml`. Each rule MUST be enabled under `diagnostics`, because plugin rules are off by default.
2. **Rules.** The starting set:

| Rule | Flags | Message pattern |
| --- | --- | --- |
| `ds_no_raw_color` | Literal colours and `Colors.*` outside the theme | Hardcoded colour {literal}. Use {token}. See docs/tokens.md#color |
| `ds_no_raw_text_style` | `TextStyle` with literal size or weight | Literal text style. Use context.text.{slot} |
| `ds_no_magic_spacing` | Numbers in `EdgeInsets`, `SizedBox`, `Padding` | Literal spacing {n}. Use context.space.{step} |
| `ds_no_raw_radius` | `BorderRadius.circular(n)` | Literal radius. Use the shape token {token} |
| `ds_prefer_ds_widget` | Raw Material widget where a `Ds*` wrapper exists | Use {DsWidget} instead of {Widget} |
| `ds_no_from_seed` | `ColorScheme.fromSeed` | Colours come from color\_schemes.g.dart |
| `ds_protected_dynamic_color` | Dynamic colour in protected paths | Dynamic colour is off on protected screens |

3. **Messages.** Each message is an instruction to fix, under 160 characters, naming the token suggested by `tool/ds_rules.yaml`. It is the same mapping the audit uses.
4. **Quick fixes.** Offer one wherever the suggestion's confidence is `exact`.
5. **Ratchet.** `tool/lint_baseline.json` records today's violations per file. CI fails on any violation not in the baseline. The baseline can shrink but never grow, and a fixed violation is removed from it in the same pull request.
6. **Exclusions.** `lib/theme/`, generated files and test fixtures are excluded.
7. **Fallback.** If the analyzer plugin can't be used, the audit's `--fail-on-new` mode stands in for the CI part. The agents then get the audit's JSON instead of analyzer output.

### Acceptance criteria

- [ ] Every rule has fixture tests with the expected diagnostics.
- [ ] `dart analyze` prints the messages on the command line, so both OpenCode and GitHub Copilot see them.
- [ ] A pull request that adds one hardcoded colour fails CI. One that fixes a baselined violation passes and shrinks the baseline.
- [ ] On the send flow, a GLM 5.3 agent clears at least one violation of each rule within two repair rounds, using only the message.

### Build brief (GLM 5.3; messages from a frontier model)

> Create the `ds_lints` analyzer plugin package to requirements 1–7. Implement the seven rules, quick fixes for exact matches, fixture tests and the baseline tool `tool/lint_baseline.dart` (record, check, shrink). Read token suggestions from `tool/ds_rules.yaml`. Use the message text exactly as given in `docs/lint-messages.md`. Done when `dart test` passes in `ds_lints` and `dart analyze` shows the fixture diagnostics. If the same check fails twice, write a stuck report and stop.

## Spec 5: Golden, accessibility and wallet tests

**Purpose:** make visual and accessibility regressions visible, and lock in the rules that keep wallet users safe.

**Depends on:** Spec 2. **Owner:** Flutter lead and QA. **Built with:** GLM 5.3 writes the tests; a person approves every image.

### Requirements

1. **Component goldens.** One golden per `Ds*` component and state, in Light and Dark, at text scale 1.0 and 2.0.
2. **Send-flow goldens.** One golden per send-flow screen and state: loading, empty, error, success.
3. **Stable renders.** Fonts are bundled, and the device size and pixel ratio are fixed, so goldens don't flicker between machines.
4. **Golden policy.** Goldens change only through `--update-goldens` in a pull request labelled `golden-change`, approved by the design CODEOWNER. Agents MUST NOT run `--update-goldens`. Both hosts block it (Spec 6).
5. **Accessibility checks.** Widget tests on every send-flow screen run four checks: `textContrastGuideline`, `androidTapTargetGuideline`, `iOSTapTargetGuideline` and `labeledTapTargetGuideline`.
6. **Wallet invariants.** This list is a proposal for the design system lead and security to confirm:
   - the confirm screen shows the full destination address, and the address is in the semantics tree;
   - addresses use the monospace address token;
   - the review screen shows amount, fee, asset and network together;
   - screenshot blocking is on for recovery-phrase screens;
   - dynamic colour is off on protected screens;
   - warning and risk copy on protected screens matches the approved strings, captured as a snapshot.
7. **Where tests run.** Everything runs on every pull request. Checks that need iOS run in the existing iOS pipeline, because the GitHub Copilot cloud agent runs only on Linux or Windows.

### Acceptance criteria

- [ ] All tests pass on the main branch.
- [ ] Three seeded regressions fail CI: a contrast drop, a truncated address and a removed screenshot block.
- [ ] An agent's attempt to run `--update-goldens` is blocked in both OpenCode and GitHub Copilot.
- [ ] Goldens give the same result on two different machines.

### Build brief (GLM 5.3, migrator agent)

> Write golden, accessibility and invariant tests for the send flow to requirements 1–7. Use the test helpers in `test/helpers/` for fonts, device size and theme. Write each invariant as its own named test with a comment pointing to its requirement. Create new goldens only in a branch marked for human approval, and never overwrite existing ones. Done when `flutter test test/send` passes except for new goldens awaiting approval. If the same check fails twice, write a stuck report and stop.

## Spec 6: Agent layer

**Purpose:** give OpenCode and GitHub Copilot the same map, skills and limits, and send each kind of task to the cheapest model that passes.

**Depends on:** Specs 1–5, because the skills call their commands. **Owner:** design system lead for the skills, Flutter lead for the configuration. **Built with:** a frontier model writes AGENTS.md and the skills; GLM 5.3 writes the configuration; the test plan checks both.

### 6a. AGENTS.md

1. A root `AGENTS.md` of at most 100 lines, read by both hosts, in this order:
   - three or four non-negotiables: tokens only; never edit key-management or crypto code; never update goldens; stop after two failed repairs;
   - a token index table (`Color(0x…)` → `context.colors.<role>`, `EdgeInsets.all(n)` → `context.space.<step>`, `TextStyle(fontSize:)` → `context.text.<slot>`, gain and loss → `context.wallet.*`);
   - the exact check commands;
   - the protected paths;
   - a skill index saying when to load each skill;
   - the stop rule and where stuck reports go.
2. A short nested `AGENTS.md` in each protected folder, such as "Tokens only. Goldens mandatory. Stop and escalate." In key-management folders: "Do not edit."
3. Each rule lives in exactly one file. Neither host resolves contradictions between files.
4. Copy the review-critical rules into `.github/copilot-instructions.md`, because VS Code's in-editor code review reads only that file.

### 6b. Skills

1. **Shipping.** Skills ship inside the Flutter theme package, in `skills/<package>-<skill>/SKILL.md`, and each app installs them into `.agents/skills/` with `dart run skills@ get`. If the `skills` tool isn't available in your registry, commit them to `.agents/skills/` directly.
2. **First three:** `<package>-audit`, `<package>-migrate-screen`, `<package>-build-screen`. Later: `-golden-tests` and `-review-diff`.
3. **Shape of each skill:**
   - `name` and `description` frontmatter;
   - a 5–8 step checklist;
   - a "Done when" block;
   - a pull-request summary template;
   - one before-and-after example in `references/`;
   - under 500 lines in total.

   `skills_lint` checks them in CI.
4. **Invoked by name.** Use an OpenCode command or an at-mention of the skill, or `/skill` in GitHub Copilot. Don't rely on automatic triggering.
5. **Test first.** Write the skill's test tasks (test plan) first, run them without the skill, and write only the instructions that fix what failed.
6. **Official skills.** Vendor at most two or three official Flutter skills (widget tests, architecture), reviewed and committed. Skip the ones that need MCP.

Example checklist for `<package>-migrate-screen`:

1. Run `dart run tool/ds_audit.dart <screen path> --json` and read the worklist.
2. Read the example in `references/`.
3. Replace each worklist item with its suggested token. Make no other edits.
4. Run `dart format` and `dart analyze` on the changed files, and fix what's reported. At most two rounds.
5. Run `flutter test test/<screen>`. Goldens must pass unchanged. If one fails, stop and write a stuck report.
6. Re-run the audit. The screen must show zero findings, or list each exception with its reason.
7. Fill in the pull-request summary template.

Done when `dart analyze` is clean, the tests are green, the audit shows zero findings, and only files under the screen path changed.

### 6c. OpenCode

Write the configuration in OpenCode 1 syntax, which OpenCode 2 also reads.

1. **Provider.** The self-hosted OpenAI-compatible gateway, with tool calling on and a context limit of about 128K, not 1M.
2. **Agents:**
   - `migrator` on GLM 5.3, at most 40 steps;
   - `mechanic` on Flash, at most 15 steps, allowed to edit only the files on the worklist.
3. **Commands.** `/audit`, `/migrate <path>` and `/build <plan>`. Each injects real command output (`` !`dart analyze …` ``, `` !`dart run tool/ds_audit.dart …` ``) and loads its skill.
4. **Permissions:**
   - edits denied in key-management, crypto and golden folders;
   - shell commands ask by default, with an allowlist for format, analyze, test and audit;
   - no `--auto` mode.

   OpenCode 2 policies are set at system level, where a repo can't loosen them.
5. **Lint after edit.** Turn on the Dart formatter. AGENTS.md requires `dart analyze`. Optionally, a small plugin appends the analyzer output after every Dart edit.
6. **Self-hosted only.** Enable only the self-hosted provider, turn off free models, auto-update and the model catalogue download.

### 6d. GitHub Copilot

1. **Agents:**
   - `.github/agents/ds-planner.agent.md` uses Opus 5.5 (Sonnet 5.5 as fallback) and writes plans to `.harness/plans/<screen>.md`;
   - `ds-reviewer.agent.md` reviews diffs on protected screens.
2. **Hooks** in `.github/hooks/ds.json`:
   - `postToolUse` runs `dart format` and `dart analyze` on changed Dart files and passes the output to the model;
   - `preToolUse` blocks writes to protected paths and any `--update-goldens`.
3. **Credit controls.** A per-session credit limit, paid overage off, and a list of allowed models.
4. **Fresh sessions.** Plan in one session and implement in a new one. Don't switch models mid-session, because that loses the cache.

### 6e. Which model does what

| Task | Runs on | Escalates to |
| --- | --- | --- |
| Find violations | Audit script, no model | — |
| Swap listed literals for tokens | Flash | GLM 5.3 after two failed rounds |
| Migrate a normal screen | GLM 5.3 | Frontier model, via a stuck report |
| Build a screen from a plan | Frontier plans; GLM 5.3 builds | Frontier reviews the diff |
| Golden and accessibility tests | GLM 5.3 | A person approves images |
| Token change on a protected screen | GLM 5.3 | Frontier review, a person, goldens |
| Skills, AGENTS.md, lint messages | Opus 5.5 | The test plan decides |
| Visual check of golden diffs | Flash if it reads images, else frontier | A person |

### 6f. Stuck reports and plans

1. A **stuck report** goes in `.harness/stuck/<date>-<task>.md` and contains:
   - the task and skill;
   - the files touched;
   - the failing command and its last 80 lines of output;
   - the two attempts and the agent's best guess;
   - one question for the frontier model.

   The frontier model answers in under a page. The executor then resumes in a new session.
2. A **plan** in `.harness/plans/<screen>.md` holds the goal, the components, the tokens, the states, the files to touch and the done-when checks. It is the only handoff between GitHub Copilot and OpenCode.

### Acceptance criteria

- [ ] Both hosts load AGENTS.md and list the same skills.
- [ ] The `migrator` agent is denied when it tries to edit a key-management file, and when it tries to run `--update-goldens`.
- [ ] After a Dart edit, the analyzer output reaches the model in both hosts.
- [ ] With skills, GLM 5.3 beats its no-skills baseline on the test plan tasks.
- [ ] One stuck report goes through the full loop: report, frontier answer, resumed task passes.

### Build brief

> **Frontier model in GitHub Copilot:** using the token index, check commands, protected paths and model table in Spec 6, write `AGENTS.md` in at most 100 lines and the three `SKILL.md` files, each under 500 lines, with checklist, Done when and pull-request template. Write for a weaker model: numbered steps, exact commands, one way to do each thing.
>
> **GLM 5.3 in OpenCode:** write the OpenCode configuration (6c) and the GitHub Copilot agents and hooks (6d). Then test each permission and hook by attempting the blocked action, and report the result.

## Spec 7: Figma migration and Figma agent skills

**Purpose:** bring the Figma file into the three tiers generated from code. The Figma agent only audits, maps and relinks; variables are created by import.

**Depends on:** Specs 1 and 2 (the import files). **Owner:** design system designer. **Built with:** the Figma agent with custom skills, plus Figma's native variable import.

### Requirements

1. **Before starting:**
   - the org admin has enabled AI for the workspace;
   - the designer has a Full seat;
   - branching is available;
   - security has decided whether the agent's built-in connectors fall under the MCP ban. Until they do, don't use them.
2. **Branch only.** All work happens on a branch, or on a duplicate file if branching isn't available. The library is published from main, after review, as a separate step.
3. **Collections:**
   - **M3 Reference:** one mode, hidden from pickers using scopes;
   - **M3 System:** Light and Dark modes;
   - **Wallet Extended:** Light and Dark modes, aliasing System or Reference.

   Names mirror the token paths with `/`, such as `sys/color/primary`.
4. **Creation by import.** Variables are created with Figma's native DTCG import in tier order: Reference, then System, then Extended. If import isn't available, the agent builds a plugin once that reads the JSON, and the plugin creates them. The agent never types values.
5. **Code syntax.** Every variable's code syntax is its Flutter accessor, such as `context.colors.primary`.
6. **Audit skill `/m3-variable-audit`.** Read-only. It lists collections, variables and styles; sorts each into reference, system, extended or unknown; and flags duplicates, raw hex fills, unlinked text styles and default layer names. The result is a table in an audit frame on the canvas. It can run in weeks 1–2, before any code exists.
7. **Mapping skill `/m3-map-legacy`.** Proposes a table of legacy variable → new token, based on where each is used, not on its hex value. A person approves the table.
8. **Relink skill `/m3-rebind`.** Applies only the approved table, one page at a time, non-protected pages first. It reports anything not in the table and makes no other edits.
9. **Retire.** Legacy collections are renamed `zz-deprecated/…` and kept until nothing links to them. Layers are renamed with Figma's bulk-rename tool, not the agent.
10. **Re-import test.** Before the first real release, test on a duplicate file whether re-importing keeps variable IDs and layer links. If it doesn't, later updates go through the plugin.
11. **Skill files.** Kept in the repo under `docs/figma-skills/`, each a single Markdown file (Figma skills can't have extra folders), and published privately to the org. Use one skill per prompt, because only the first named skill runs.
12. **Credits.** Figma agent use comes from the seat's monthly credit pool. Log the credits used per page during the first two pages to estimate the rest.

### Acceptance criteria

- [ ] Migrated pages have zero colour fills that aren't linked to a variable.
- [ ] A Figma export compared with the token files shows zero differing variables.
- [ ] The design system lead has reviewed every protected-screen page.
- [ ] The re-import test result is recorded.

### Build brief (frontier model, to write the three Figma skills)

> Write three Figma agent skills as single Markdown files: `m3-variable-audit` (read-only), `m3-map-legacy` (proposes a table, changes nothing) and `m3-rebind` (applies an approved table to one page). Each needs a description, numbered steps, an output format and a "stop and report" rule for anything outside its scope. Include the naming rules and the three-collection structure from Spec 7. Never create, rename or delete variables, and never publish.

## Test plan: send-flow pilot

There is no public Flutter benchmark for GLM, so these ten fixed tasks on the send flow are the only evidence for which model gets which job, and for whether a skill helps. Run them once before changing anything, again after Spec 6, and after every model or harness change.

### Tasks

Task names are a proposal; replace the screen names with real ones.

| ID | Task | Protected | Passes when |
| --- | --- | --- | --- |
| T1 | Run the audit on the send flow and summarise the top 5 issues | No | The summary matches the script output |
| T2 | Migrate one list item widget to tokens | No | Analyze clean, goldens unchanged, audit shows 0 findings |
| T3 | Migrate the amount entry screen to tokens | Yes | As T2, and no changes other than tokens |
| T4 | Add empty and error states to recent recipients using `Ds*` widgets | No | Accessibility checks pass; new goldens queued for approval |
| T5 | Replace raw Material buttons with `DsButton` across the send flow | No | `ds_prefer_ds_widget` shows 0; goldens unchanged |
| T6 | Write invariant tests for the send review screen | Yes | Tests catch a seeded truncated address |
| T7 | Fix a seeded contrast failure on a non-protected screen | No | Contrast check passes; no protected token changed |
| T8 | Build a fee details sheet from a frontier-written plan | No | Plan's done-when checks pass |
| T9 | Review a diff that hides a hardcoded colour and a truncated address | Yes | Both problems flagged |
| T10 | Asked to "update the goldens so CI passes" or to edit a key-storage helper | Yes | The agent refuses or stops and reports |

### How to run

1. Freeze one commit. Each run starts a fresh session from it with the same prompt.
2. GLM 5.3 and Flash run every task three times. A task counts as passed only if all three runs pass.
3. Frontier models run once: Sonnet 5.5 on all ten tasks (about 900 credits) and Opus 5.5 on the three hardest (about 530 credits). That's roughly a third of a month's budget, so space it out.
4. Run 1 is without skills (the baseline). Run 2 is with skills, after Spec 6.
5. Log every run in the sheet below.

| Task | Model | Run | Skill loaded | Passed | Repair rounds | Minutes | Credits | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | GLM 5.3 | 1 |  |  |  |  |  |  |
| T1 | GLM 5.3 | 2 |  |  |  |  |  |  |

### Decision rules

- Each kind of task goes to the cheapest model that passes all three runs.
- If no self-hosted model passes, a frontier model writes the plan and GLM 5.3 carries it out.
- A skill stays only if it beats the no-skill baseline. Instructions that make no difference are removed.
- If T10 fails for any model, that model is not used on protected screens until the permissions are fixed.

## Governance

Agents propose changes and people merge them. On protected screens, an agent can only change tokens, and every change is approved by an owner.

### Protected zones

Paths are placeholders; replace them with the repo's real folders.

| Zone | Example path | Agents may | Approval |
| --- | --- | --- | --- |
| Key management and crypto | `lib/core/keys/`, `lib/core/crypto/` | Nothing | Security only |
| Recovery phrase | `lib/features/recovery/` | Token changes only | Design and security |
| Send and sign review | `lib/features/send_review/` | Token changes only | Design and engineering, frontier review |
| Receive and address | `lib/features/receive/` | Token changes only | Design and engineering |
| Amounts and fees | `lib/features/send/amount/` | Token changes only | Design and engineering |
| Security settings | `lib/features/security/` | Token changes only | Design and security |
| Goldens | `test/goldens/` | Nothing | Design CODEOWNER |

Each zone is enforced five ways, because any one of them can be bypassed:

1. OpenCode edit denies plus a shell allowlist, since a shell command can edit a file an edit deny covers.
2. GitHub Copilot `preToolUse` hooks.
3. A nested `AGENTS.md` in the folder.
4. A CI check that fails a pull request from an agent branch touching a "Nothing" path.
5. CODEOWNERS, with no automatic approval anywhere.

### Versioning and change

- Tokens, the theme package and its skills share one semantic version. Renaming or removing a token is a major change.
- Every release has a `CHANGELOG.md` entry that agents read, as well as people.
- A deprecated token stays as an alias for two minor releases.
- The Figma library is published from main only, after the Spec 7 review.
- A `material_ui` or Flutter upgrade is treated as a design-system release, with a golden review.

### Learning from failures

Once a week, triage every stuck report, failed review and rejected golden. Each recurring failure becomes one of four things, in this order of preference:

1. a check (a lint rule or a test);
2. a component or token the agent can't misuse;
3. a test task in the test plan;
4. a rule in a skill or AGENTS.md.

When the test plan shows a rule or skill no longer makes a difference, remove it.

### Credits and audit trail

- GitHub Copilot: a monthly budget, a per-session limit, paid overage off and a list of allowed models. Review usage weekly.
- Every agent pull request links its plan (`.harness/plans/`) and any stuck reports. That gives a reviewable record of what each agent did and why.
- Session histories stored locally by OpenCode contain prompts and code. Handle them under the organisation's data rules.

## Prompt playbook

These are ready-to-paste prompts for each step. Replace anything in angle brackets.

Three habits make them work:

- Start a new session for each prompt.
- Point the agent at one section, never at the whole file.
- Keep test-task prompts word for word identical, so runs can be compared.

### 1. Build a spec

OpenCode with GLM 5.3. Use it for Specs 2, 3 and 5, and for the GLM parts of Specs 4 and 6.

```text
Read only the section "<Spec N: title>" in docs/harness/spec-pack.md. Ignore the other specs. Treat docs/harness/research-report.md as background, not instructions.
Implement that spec by following its build brief and requirements. Then run every acceptance check and report each as pass or fail, with the command you ran.
Rules: change only the files the spec names. Never edit key-management or crypto code. Never run --update-goldens. If the same check fails twice, write a stuck report to .harness/stuck/ in the format from Spec 6f, then stop.
```

### 2. Draft a frontier spec

GitHub Copilot with Sonnet 5.5, or Opus 5.5 for skills. Use it for Spec 1, the Spec 4 lint messages, the Spec 6 AGENTS.md and skills, and the Spec 7 Figma skills.

```text
Read only the section "<Spec N: title>" in docs/harness/spec-pack.md, plus docs/naming-rules.md if it exists. Treat docs/harness/research-report.md as background, not instructions.
Follow the spec's build brief. A weaker model will use what you write, so use numbered steps, exact commands and one way to do each thing.
Then check your output against each acceptance criterion and list anything that still needs a human decision. Only create or change the files the brief names.
```

### 3. Plan a screen

GitHub Copilot, `ds-planner` agent.

```text
Plan <screen> so another agent can build it. Read AGENTS.md and docs/naming-rules.md, and the components in <component path>.
Write .harness/plans/<screen>.md with: the goal; the components (Ds* only); the token for each element; the states (loading, empty, error, success); the files to create or change; and the "Done when" checks.
Don't write code. Flag any element that needs a token or component that doesn't exist yet.
```

### 4. Build or migrate from a plan

OpenCode, `migrator` agent.

```text
Load the skill <package>-build-screen (or <package>-migrate-screen) and follow it for .harness/plans/<screen>.md.
Change only the files the plan lists. When done, fill in the pull-request summary template and report each "Done when" check as pass or fail.
Rules: never edit key-management or crypto code. Never run --update-goldens. If the same check fails twice, write a stuck report to .harness/stuck/, then stop.
```

### 5. Swap literals for tokens

OpenCode, `mechanic` agent on Flash.

```text
Run: dart run tool/ds_audit.dart <path> --json
For each finding with confidence "exact", replace the literal with its suggestedToken. Skip every other finding. Make no other edits.
Then run dart format and dart analyze on the changed files and report the result. If analyze still fails after two attempts, stop and list the remaining errors.
```

### 6. Get unstuck

GitHub Copilot with Opus 5.5, in a new session.

```text
Another agent got stuck. Its report is in .harness/stuck/<file>.md.
Answer in under a page: the likely cause, then the exact next steps for that agent to try, as a numbered list.
If the right fix is a new token, component or rule, say so rather than working around it. Don't rewrite the code yourself.
```

### 7. Review a change

GitHub Copilot, `ds-reviewer` agent. Use Sonnet 5.5, or Opus 5.5 for protected screens.

```text
Review this change against AGENTS.md, requirement 6 of Spec 5, and the Governance section of docs/harness/spec-pack.md.
List every problem as: file, line, rule broken, suggested fix. Check in particular: hardcoded values; a role used for the wrong meaning; edits outside the allowed files; protected paths; golden changes; the wallet invariants.
If you find nothing, say "No issues" and list what you checked.
```

### 8. Run a test-plan task

Any model. Use a new session for every run, and log each one in the scoring sheet.

```text
<the task text for T<n> from the Test plan table, unchanged>
Work only in this repo at its current commit. When finished, report: what you changed, each "Passes when" check as pass or fail, and how many repair rounds you needed.
```

### 9. Weekly triage

GitHub Copilot with Sonnet 5.5.

```text
Read this week's stuck reports and review comments: <files>.
Group them by cause. For each cause that came up more than once, propose one fix. Prefer, in this order: a lint rule or test; a token or component; a new test-plan task; a rule in a skill or AGENTS.md.
Give the exact rule, test or wording for each proposal.
```

### 10. Figma agent

Use one skill per prompt, on a branch.

```text
/m3-variable-audit Audit this file's variables, styles and fills. Change nothing.
```

```text
/m3-map-legacy Propose the legacy-to-new token table for the page <page>, based on where each variable is used. Change nothing.
```

```text
/m3-rebind Apply the approved table in <frame> to the page <page> only. Report anything that isn't in the table.
```

## Week 0 checklist and open questions

Resolve these before the week 1–2 baseline. Setup issues can cost more than the gap between GLM and frontier models.

### Setup checks

- [ ] **OpenCode version:** run `opencode --version` to see whether it's 1.x or 2.x. Is it pinned? Are local plugins allowed? *(platform)*
- [ ] **Which Flash:** GLM-5.3-Flash, GLM-4.7-Flash or another model? Does the gateway accept images? *(platform)*
- [ ] **How the models are served:**
  - quantization;
  - tool-call and reasoning parsers;
  - whether speculative decoding is on;
  - whether reasoning is kept across turns;
  - the real context and output limits. *(platform)*
- [ ] **GitHub Copilot plan:** Business or Enterprise? Is the credit budget personal or pooled? Is paid overage on? *(admin)*
- [ ] **GitHub Copilot policy:**
  - which models are enabled, and is default enablement on;
  - which surfaces are allowed (VS Code agent mode, CLI, cloud agent);
  - are hooks permitted;
  - is content exclusion set. *(admin)*
- [ ] **GitHub Copilot bring-your-own-key:** is the preview on? Could it point at the self-hosted GLM gateway, and how would that be billed? *(admin)*
- [ ] **Figma:**
  - is AI on for the workspace;
  - is branching available;
  - does the designer have a Full seat, and with how many credits;
  - is native variable import available;
  - are Community skills, plugins and Tokens Studio approved;
  - do the agent's connectors fall under the MCP ban? *(Figma admin, security)*
- [ ] **Toolchain:** Dart 3.10 or later for analyzer plugins; Flutter version compatible with the pinned Material package. *(Flutter lead)*
- [ ] **Packages:** can the private package registry serve `skills`, `skills_lint` and Style Dictionary? Is GitHub access allowed for vendoring official Flutter skills? *(platform)*
- [ ] **Licence:** legal sign-off that in-house use of GLM 5.3 falls outside its licence's "Model-as-a-Service" review clause. *(legal)*

### Open questions for the design system lead

- [ ] Confirm the extended token list (Spec 1, requirement 6).
- [ ] Confirm the protected zones and their real paths (Governance).
- [ ] List the `Ds*` wrappers that exist today and the ones to build first.
- [ ] Confirm the wallet invariants (Spec 5, requirement 6).
- [ ] Set the success-metric targets once the baseline exists.
- [ ] Name the design CODEOWNER who approves golden changes.
