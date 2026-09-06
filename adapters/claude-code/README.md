# Claude Code adapter

The canonical source is `../../plugins/research-dossier/skills/`. Install the `research` directory and any companion directories into the Claude Code skills location used by your project or user environment.

The skill is intentionally self-contained: it can use the host's web-search capability when available and otherwise asks the user to provide sources or enable external search. It stores projects in the current working directory under `./research/`.

Start with:

```text
Сделай ресерч по теме: Иммунитет к изменениям
```

The skill asks for or loads the global audience profile, checks for unfinished projects, collects a brief, creates a question map, and waits for confirmation before deep research. Do not skip this confirmation when adapting the skill.

Claude Code users can use the companion directories as separate skills: `research-factcheck`, `research-critic`, `research-editorial-review`, `research-concept-refiner`, and `research-html`.

If the host's skill loader requires a different directory convention, copy the contents of the canonical skill folder without changing the behavior contract. Do not duplicate the methodology into a second hand-maintained implementation.
