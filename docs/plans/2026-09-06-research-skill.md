# Research Skill Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a public, cross-platform research-skill repository whose main Codex/ChatGPT plugin turns a topic or source material into a sourced, creative research dossier with resumable local project files.

**Architecture:** Keep the research contract in the plugin's skill resources so the installed Codex plugin is self-contained. Provide thin Claude Code and generic compatibility adapters that point to the same skill folders. Use small Python standard-library helpers for deterministic project scaffolding, checkpoint state, and Markdown-to-HTML publication; keep editorial judgment in the skill instructions rather than code.

**Tech Stack:** Markdown skill files, Codex plugin JSON, Claude Code-compatible skill folders, Python 3 standard library, HTML/CSS/vanilla JavaScript, `unittest`, bundled plugin and skill validators.

---

### Task 1: Create the plugin and repository skeleton

**Files:**
- Create: `plugins/research-dossier/.codex-plugin/plugin.json`
- Create: `plugins/research-dossier/skills/`
- Create: `adapters/claude-code/`
- Create: `adapters/generic/`
- Create: `.gitignore`

**Step 1: Write the failing repository-contract test**

Create `tests/test_repository_contract.py` with assertions for the required plugin manifest path, manifest name/version/description, and the presence of the main skill directory.

**Step 2: Run the test to verify it fails**

Run: `python3 -m unittest tests.test_repository_contract -v`

Expected: FAIL because the plugin scaffold and skill directories do not exist.

**Step 3: Scaffold the Codex plugin**

Run the bundled plugin creator from its skill root:

```bash
python3 /Users/aleksandrbubnov/.codex/skills/.system/plugin-creator/scripts/create_basic_plugin.py \
  research-dossier \
  --path /Users/aleksandrbubnov/Documents/DEV/research_skill/plugins \
  --with-skills \
  --with-scripts
```

Edit the generated manifest with real metadata and point `skills` to `./skills/`. Do not add unused apps, MCP, or hooks fields.

**Step 4: Run the test to verify it passes**

Run: `python3 -m unittest tests.test_repository_contract -v`

Expected: PASS.

### Task 2: Add deterministic research-project scaffolding

**Files:**
- Create: `plugins/research-dossier/scripts/new_research_project.py`
- Create: `plugins/research-dossier/scripts/project_state.py`
- Create: `tests/test_project_scaffolding.py`
- Create: `plugins/research-dossier/templates/`

**Step 1: Write failing tests**

Test that creating a slug produces `./research/<slug>/` with `PROJECT.md`, `input/`, `working/`, `output/`, and `reviews/`, plus the agreed checkpoint files. Test that a second invocation detects the existing project without overwriting its input or output.

**Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_project_scaffolding -v`

Expected: FAIL because the scripts and templates do not exist.

**Step 3: Implement the minimal scaffolder**

Use only the Python standard library. Accept a working directory and project slug, create missing directories/files, write a status-bearing `PROJECT.md`, and refuse destructive overwrite by default. Add a state reader that returns the last completed stage and lists missing/incomplete artifacts.

**Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_project_scaffolding -v`

Expected: PASS.

### Task 3: Add the core Research skill instructions

**Files:**
- Create: `plugins/research-dossier/skills/research/SKILL.md`
- Create: `plugins/research-dossier/skills/research/references/output-format.md`
- Create: `plugins/research-dossier/skills/research/references/evidence-policy.md`
- Create: `plugins/research-dossier/skills/research/references/checkpoints.md`
- Create: `plugins/research-dossier/skills/research/references/audience-profile.md`
- Create: `plugins/research-dossier/skills/research/references/research-example.md`

**Step 1: Add a static contract test**

Extend `tests/test_repository_contract.py` to verify valid frontmatter, a discriminating description, required workflow terms, the mandatory confirmation pause after the question map, evidence labels, ten wild concepts, source links, checkpoints, and the reference case.

**Step 2: Run the contract test to verify the new assertions fail**

Run: `python3 -m unittest tests.test_repository_contract -v`

Expected: FAIL because the skill files do not exist.

**Step 3: Write the skill and focused references**

Keep `SKILL.md` concise and route detailed schemas/policies to references. Encode the approved workflow, local storage, adaptive depth, multilingual search with Russian output, citation rules, quote rules, status labels, creative separation, the ten-concept block, HTML/post-review handoff, and the no-web-search stopping behavior. Include the Dashkiev-style default audience as an editable example, not a universal requirement.

**Step 4: Run the contract test and the bundled skill validator**

Run:

```bash
python3 -m unittest tests.test_repository_contract -v
python3 /Users/aleksandrbubnov/.codex/skills/.system/skill-creator/scripts/quick_validate.py plugins/research-dossier/skills/research
```

Expected: PASS with no scaffold placeholders.

### Task 4: Add optional post-research skills

**Files:**
- Create: `plugins/research-dossier/skills/research-critic/SKILL.md`
- Create: `plugins/research-dossier/skills/research-factcheck/SKILL.md`
- Create: `plugins/research-dossier/skills/research-editorial-review/SKILL.md`
- Create: `plugins/research-dossier/skills/research-concept-refiner/SKILL.md`

**Step 1: Write the failing companion-skill contract test**

Add assertions that each companion skill has valid frontmatter, reads saved project artifacts, writes a new review artifact, and does not overwrite `output/research.md`.

**Step 2: Run it to verify failure**

Run: `python3 -m unittest tests.test_repository_contract -v`

Expected: FAIL because companion skills are absent.

**Step 3: Implement the four focused skills**

Each skill should be independently invokable and should state its inputs, output path, evidence boundaries, and limitations. The main skill offers them only after the base dossier is complete.

**Step 4: Re-run contract and skill validation**

Run the repository tests and `quick_validate.py` for every new skill directory. Expected: PASS.

### Task 5: Implement Markdown-to-HTML publication

**Files:**
- Create: `plugins/research-dossier/scripts/render_html.py`
- Create: `plugins/research-dossier/assets/report.css`
- Create: `plugins/research-dossier/templates/report.html`
- Create: `tests/test_html_renderer.py`
- Create: `plugins/research-dossier/skills/research-html/SKILL.md`

**Step 1: Write failing renderer tests**

Test that a Markdown dossier renders headings, tables, source links, evidence labels, review sections when present, and a plain-text `Copy` button for useful blocks. Test that HTML generation does not modify the Markdown source.

**Step 2: Run tests to verify failure**

Run: `python3 -m unittest tests.test_html_renderer -v`

Expected: FAIL because the renderer does not exist.

**Step 3: Implement the minimal renderer**

Use standard-library HTML escaping and a constrained Markdown parser or a documented optional dependency. Render navigation, cards, tables, status colors, expandable details, clickable links, review status, and copy-to-clipboard controls. Copy controls must export clean text only and preserve relevant source URLs.

**Step 4: Run renderer tests**

Run: `python3 -m unittest tests.test_html_renderer -v`

Expected: PASS.

### Task 6: Add the cross-platform adapters and installation documentation

**Files:**
- Create: `adapters/claude-code/README.md`
- Create: `adapters/generic/COMPATIBILITY.md`
- Create: `README.md`
- Create: `CONTRIBUTING.md`
- Create: `CHANGELOG.md`
- Create: `LICENSE`

**Step 1: Write documentation checks**

Add `tests/test_documentation.py` to verify that README contains Codex/ChatGPT installation, Claude Code installation, local storage, first-run audience setup, resume behavior, web-search limitation, HTML, optional reviews, privacy responsibility, example usage, and validation commands.

**Step 2: Run the checks to verify failure**

Run: `python3 -m unittest tests.test_documentation -v`

Expected: FAIL because public documentation is absent.

**Step 3: Write platform-neutral documentation**

Document the canonical skill folders, how to install/copy them for Claude Code, how to adapt the same contract to Antigravity/Google/OpenCode, and which capabilities may be unavailable. Do not claim unsupported platform behavior. Include a concise quick start and example project layout.

**Step 4: Run documentation checks**

Run: `python3 -m unittest tests.test_documentation -v`

Expected: PASS.

### Task 7: Create the reference example for «Иммунитет к изменениям»

**Files:**
- Create: `examples/immunity-to-change/input.md`
- Create: `examples/immunity-to-change/question-map.md`
- Create: `examples/immunity-to-change/research.md`
- Create: `examples/immunity-to-change/source-ledger.md`
- Create: `examples/immunity-to-change/creative-lab.md`
- Create: `examples/immunity-to-change/README.md`

**Step 1: Add failing example-contract checks**

Test that the example contains the agreed report modules, source links beside factual claims, evidence labels, verified/paraphrased quote handling, and exactly ten wild concepts.

**Step 2: Run checks to verify failure**

Run: `python3 -m unittest tests.test_reference_example -v`

Expected: FAIL because the example artifacts are absent.

**Step 3: Produce the sourced reference dossier**

Use authoritative web sources and clearly separate verified facts, interpretations, creative hypotheses, and short invented illustrations. Include related concepts, research limits, real stories, quotes, books/videos/films, and scenario-use notes without turning the example into a script.

**Step 4: Run the example-contract checks**

Run: `python3 -m unittest tests.test_reference_example -v`

Expected: PASS.

### Task 8: Run complete verification and package validation

**Files:**
- Modify: any files required by validation failures only.

**Step 1: Run the complete test suite**

Run: `python3 -m unittest discover -v`

Expected: all tests pass.

**Step 2: Validate every skill**

Run `quick_validate.py` for the main skill and every companion skill.

Expected: no invalid frontmatter, missing names, or unfinished placeholders.

**Step 3: Validate the Codex plugin**

Run:

```bash
python3 /Users/aleksandrbubnov/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py \
  plugins/research-dossier
```

Expected: plugin manifest and packaged paths are valid.

**Step 4: Exercise the scaffold and renderer manually**

Create a temporary project under a temporary directory, render a small dossier, inspect the output for navigation, tables, source links, and copy buttons, and confirm source Markdown remains unchanged.

**Step 5: Review the requirements checklist**

Compare the implementation against `DESIGN.md`, record any deviations, and do not claim completion until every required behavior has fresh verification evidence.
