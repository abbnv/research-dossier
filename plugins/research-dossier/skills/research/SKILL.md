---
name: research
description: Turn a topic, idea, transcript, or source material into a sourced, creative, scenario-ready research dossier for a future video. Use when the user wants research fuel, not a finished script.
---

# Research

Create a local, resumable research dossier that gives a writer maximum useful material for a future video: findings, studies, cases, quotations, books, films, metaphors, visual possibilities, and bold concepts. The dossier is not a finished script. It is a clear bridge from evidence to possible scenario structures.

## User-facing behavior

Keep internal routing, instruction loading, path resolution, cache paths, tool calls, and progress narration invisible. Do not announce that you are reading or locating a skill, do not mention an environment-specific skill path, and do not expose implementation details. Start with a useful acknowledgement, a concise question when user input is genuinely missing, or the next visible research action.

Keep internal routing and instruction loading invisible.

## Start and resume

1. On the first run, offer the editable default audience profile for a Russian-language business and self-development YouTube channel inspired by Mikhail Dashkiev's audience. Save one global local profile; do not present it as universal.
2. Inspect `./research/` for incomplete projects. Ask whether to continue an existing project or start a new one.
3. For a new project, accept a topic, idea, URL, notes, transcript, or call recording. First infer what is already clear. Ask only high-value questions whose answers could materially change the map; each question should offer five options generated for this topic. Do not make the user complete a long generic intake form.
4. An editorial line is optional at intake. If the user has one, use it as a priority; otherwise begin with open research and discover possible lines from the material.
5. Create a project folder with `scripts/new_research_project.py`, preserve the original input, and complete `working/brief.md`.
6. Read [research-map.md](references/research-map.md) and build `working/question-map.md`. The map is a set of research tasks, desired evidence, human material, practical implications, criticism, quotations, references, and visual/creative opportunities. It is not a premature script outline.
7. Stop and ask the user to confirm or edit the map. Do not start the deep research pass before confirmation. If the user explicitly asks you to proceed without waiting, record that choice and continue.

Read [checkpoints.md](references/checkpoints.md) before resuming or changing project state.

## Pass 1: open research and material collection

Read [evidence-policy.md](references/evidence-policy.md) and [research-card.md](references/research-card.md) before collecting claims. Search the web in any relevant language and use model knowledge for orientation, discovery, and synthesis. Do not present unsupported memory as verified evidence.

Cover every approved branch where relevant:

- how the phenomenon works;
- studies, data, methods, and limitations;
- adjacent concepts and competing explanations;
- real people, cases, and human conflicts;
- practical implications and possible experiments;
- criticism, counterarguments, and what the model cannot explain;
- short verified quotations from research and books;
- books, films, videos, lectures, interviews, and essays;
- metaphors, visual devices, and short invented illustrations;
- unusual conceptual directions.

Turn every important source into an editorial card in `working/findings.md`. The card must answer: what was studied, what was found, what it means in ordinary language, what it does not prove, why it belongs in this dossier, and how it could serve a video. Save provenance in `working/source-ledger.md`, creative material in `working/creative-lab.md`, and unresolved issues in `working/open-questions.md`.

Do not use repetitive status tags in the reader-facing report. Не используйте повторяющиеся статусные теги: разницу между фактом, выводом и гипотезой показывайте формулировками, ссылками, методом и ограничениями. Technical source evaluation belongs only in the source ledger and later reviews.

Research until each branch has useful coverage and new searches stop adding material, not until a fixed number of links or minutes is reached. Record remaining gaps instead of filling them with guesses. If web search is unavailable, say so and ask for sources or permission to continue with an explicitly limited evidence base.

Save a checkpoint after every major branch and update `PROJECT.md` with `status`, `last_completed`, and `current_task`.

## Pass 2: editorial synthesis

When the first pass has adequate coverage, read [scenario-synthesis.md](references/scenario-synthesis.md) and [output-format.md](references/output-format.md). Then:

1. Write 7–10 short findings for fast reading, followed by expanded explanations.
2. Propose one recommended structure for the future video and 2–4 alternatives. Map facts, cases, quotations, visuals, and gaps to each structure.
3. Build a list of possible lines of presentation. These are outputs of the research, not a gate that restricted the search.
4. Curate the strongest concepts, quotes, references, metaphors, and ten unusual ideas.
5. Make contradictions, unsupported links, and missing evidence visible.

The synthesis must explain how the material can become a scenario without pretending to be the final script.

## Output and follow-up

Read [output-format.md](references/output-format.md) before assembling `output/research.md`. Write in natural Russian. Translate technical terms on first use and retain the original in parentheses only when useful. Put source links next to factual claims and include a complete source list at the end.

The final report contains no repetitive evidence tags. Keep creative material in dedicated sections so it is visibly different from sourced findings. Direct quotations require a checked original, Russian translation, author, context, and locator; otherwise use a clearly marked paraphrase.

Finish by telling the user where `output/research.md` is and offer `research-html`, `research-factcheck`, `research-critic`, `research-editorial-review`, and `research-concept-refiner`. Run HTML only on request. Optional reviews read saved artifacts and write new files without overwriting the dossier.

The reference example is «Иммунитет к изменениям». Use it to understand the expected breadth, evidence discipline, and creative ambition. When working on that topic, explain what each useful finding adds to a possible video.
