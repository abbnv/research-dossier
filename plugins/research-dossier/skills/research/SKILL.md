---
name: research
description: Turn a topic, idea, transcript, or source material into a sourced and creative research dossier for a future video. Use when the user wants research, not a finished script.
---

# Research

Create a local, resumable research dossier. The dossier is research fuel for a writer, not a screenplay. It should maximize interesting, visual, deep directions while keeping evidence, interpretation, speculation, and fiction visibly separate.

## User-facing behavior

Keep internal routing and instruction loading invisible. Do not announce that you are using, reading, or locating a skill; do not mention the skill file path, environment-specific paths, cache paths, or a path mismatch. Do not narrate tool calls or internal progress. Start with a useful acknowledgement, a concise question if user input is genuinely missing, or the next visible research action.

## Start and resume

1. If this is the first run, offer the editable default audience profile for a Russian-language business/self-development YouTube channel modeled on Mikhail Dashkiev's audience. Save one global profile locally; do not treat it as universal.
2. Inspect `./research/` for incomplete projects. Ask whether to continue an existing project or start a new one.
3. For a new project, collect the topic or input material, objective, intended video format, and constraints. Use the scaffolder in `scripts/new_research_project.py` when available.
4. Save the original input and write `working/brief.md`.
5. Build `working/question-map.md` (the question map), showing the research branches and why they matter.
6. Stop and ask the user to confirm or edit the map. Do not begin deep research until confirmation.

Read [checkpoints.md](references/checkpoints.md) before resuming or changing project state.

## Research pass

Use web search plus model knowledge. Search in any relevant language; write the report in Russian and translate or explain non-Russian sources. Do not leave unexplained English phrases in Russian prose: translate technical terms on first use and keep the original only in parentheses, source titles, or verified quotations. Read [evidence-policy.md](references/evidence-policy.md) before collecting claims or quotations.

Research until the topic has adequate coverage, not until a fixed number of links is reached. Look for:

- related theories and concepts;
- studies, data, and methodological limits;
- real cases and human stories;
- short, verified quotations from books or research, always with a Russian translation and the original wording retained;
- books, videos, lectures, films, interviews, and essays;
- metaphors and short invented illustrations;
- ten (10) unusual concepts that are not limited to opening hooks.

Every useful item must explain why it may help the scenario: hook, scene, conflict, visual, transition, reveal, or ending. Keep creative proposals in a separate layer.

If web search is unavailable, ask the user to provide sources or enable external search before starting a full research pass. Do not silently substitute unsupported model memory for evidence.

## Output

Read [output-format.md](references/output-format.md) before assembling `output/research.md`. Use short theses, bullets, comparisons, and tables. Put source links immediately beside factual claims and include a complete source list at the end. Include the complete ten wild concepts block directly in `output/research.md`, even when some ideas are weak; rank them and describe the risk.

Use these status labels exactly:

- `[ДОКАЗАНО]`
- `[ПОДТВЕРЖДАЕТСЯ]`
- `[ИНТЕРПРЕТАЦИЯ]`
- `[НАТЯНУТО]`
- `[КРЕАТИВНАЯ ГИПОТЕЗА]`
- `[ВЫМЫСЕЛ / ИЛЛЮСТРАЦИЯ]`

When sources conflict, choose the most convincing position using relevance, methodology, transparency, independence, and fit for the claim. State meaningful alternatives. Never invent a study, quotation, case, or event. Full invented stories are not allowed; only metaphors and short illustrative examples may be invented and must be labeled.

Save checkpoints after major branches. Update `PROJECT.md` with status and last completed stage. Finish by telling the user where `output/research.md` is and offer `research-html`, `research-factcheck`, `research-critic`, or `research-editorial-review`.

The reference example is the topic «Иммунитет к изменениям»; use the example to understand the expected level of breadth, evidence, and creative ambition. When working on the example, explain what the research adds to «Иммунитету к изменениям» as a video topic.
