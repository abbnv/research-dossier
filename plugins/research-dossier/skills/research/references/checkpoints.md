# Checkpoints and project state

Each research is a separate project under `./research/<project-slug>/`:

```text
PROJECT.md
input/original-material.md
working/brief.md
working/question-map.md
working/source-ledger.md
working/findings.md
working/creative-lab.md
working/open-questions.md
output/research.md
reviews/
```

Update `PROJECT.md` after each major branch with `status`, `last_completed`, and `current_task`. Preserve original input and do not overwrite a finished output during reviews.

Use these stage names when possible: `intake`, `map-draft`, `map-confirmed`, `open-research`, `synthesis`, `report-ready`, and `review`. The broad research pass writes to `working/findings.md`, `working/source-ledger.md`, `working/creative-lab.md`, and `working/open-questions.md`; the synthesis pass then assembles `output/research.md`.

When resuming, read the project state and the artifacts relevant to the last completed stage. Ask the user whether to continue, return to an earlier stage, or start a new project. An incomplete file is a work-in-progress, not evidence of completion. Do not discard a completed broad research pass merely because the scenario synthesis has not been written.
