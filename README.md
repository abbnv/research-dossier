# Research Dossier

Research Dossier turns a topic, idea, transcript, notes, URL, or call recording into a local research dossier for a future video. It is research fuel, not a finished script: the report combines evidence, concepts, cases, quotes, media references, metaphors, and ten bold creative directions while marking what is proven, inferred, stretched, or invented.

The default audience profile is a Russian-speaking business and self-development YouTube audience inspired by the editorial profile of Mikhail Dashkiev. It is editable and stored locally. The project is designed around the ChatGPT/Codex plugin and has a Claude Code adapter plus generic compatibility notes for Antigravity, Google, OpenCode, and similar skill-based environments.

## What it does

1. Creates or resumes a local project under `./research/<slug>/`.
2. Collects a short brief and builds a question map.
3. Pauses for user confirmation before deep research.
4. Searches the web in any relevant language and writes the report in Russian.
5. Separates evidence, interpretation, creative hypotheses, and short illustrative fiction.
6. Saves checkpoints so a long research can resume after context loss.
7. Writes `output/research.md` and can generate `output/research.html` on request.
8. Offers optional factcheck, critic, editorial review, and concept-refinement skills.

## Codex / ChatGPT installation

Install the directory `plugins/research-dossier` using the Codex plugin installation flow or local plugin UI. The plugin manifest is at `plugins/research-dossier/.codex-plugin/plugin.json`, and the bundled skills are under `plugins/research-dossier/skills/`.

After installation, start a new Codex task and ask: `Сделай ресерч по теме: ...`.

## Claude Code installation

Copy the skill directories from `plugins/research-dossier/skills/` into the Claude Code skills directory used by your project or user environment. The detailed adapter is in [adapters/claude-code/README.md](adapters/claude-code/README.md). The main skill is `skills/research/`; companion skills can be installed alongside it.

## Other agents

Use the canonical skill folders and follow [adapters/generic/COMPATIBILITY.md](adapters/generic/COMPATIBILITY.md). If the host has no web search, ask the user for sources or enable external search before starting a full research pass. Do not pretend model memory is verified research.

## First run and audience

On first run, accept or edit the default audience profile. It is one global local profile, not a universal truth. The user is responsible for the confidentiality and privacy of transcripts and other input material; the skill does not promise automatic anonymization.

## Local project layout

```text
./research/<project-slug>/
├── PROJECT.md
├── input/original-material.md
├── working/{brief,question-map,source-ledger,findings,creative-lab,open-questions}.md
├── output/research.md
└── reviews/{factcheck,critic,editorial-review}.md
```

Use `plugins/research-dossier/scripts/new_research_project.py` to scaffold a project and `project_state.py` to inspect resume state. Existing input and output are never overwritten by a second scaffold run.

## HTML and copy buttons

After Markdown is ready, ask for HTML or run:

```bash
python3 plugins/research-dossier/scripts/render_html.py \
  research/<project-slug>/output/research.md \
  research/<project-slug>/output/research.html
```

The HTML report adds navigation, tables, evidence styling, source links, available reviews, and plain-text `Скопировать` buttons. It does not add facts or alter the Markdown.

## Reference example

See [examples/immunity-to-change/](examples/immunity-to-change/) for the complete reference case based on «Иммунитет к изменениям».

## Development and validation

```bash
python3 -m unittest discover -v
python3 /Users/aleksandrbubnov/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  plugins/research-dossier/skills/research
python3 /Users/aleksandrbubnov/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py \
  plugins/research-dossier
```

The bundled validators may need a Python environment with `PyYAML` installed. The repository's own tests use only the Python standard library.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing the workflow or output contract. Keep the core behavior platform-independent and update the changelog for user-visible changes.
