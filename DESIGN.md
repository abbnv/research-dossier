# Research Skill — Design Specification

## 1. Goal

Create a universal research skill that turns a topic, idea, notes, meeting transcript, or other source material into a deep but bounded research dossier for a future video. The dossier is not a script and does not need to be used in full. Its two purposes are:

1. start and expand the writer's creative process;
2. provide a sourced investigation for a new video.

The reference editorial profile is a Russian-language YouTube channel about business, thinking, and self-development, initially modeled on Mikhail Dashkiev's audience. The profile is editable and serves as the default for a public, reusable GitHub project.

## 2. Product shape

- Primary distribution: ChatGPT/Codex plugin.
- Compatibility targets: Claude Code, Antigravity, Google, OpenCode, and other environments that support compatible skill specifications.
- One front-door skill: `Research`.
- Optional post-research skills: critic, fact-checker, editorial review, concept refinement, and HTML publisher.
- Each user keeps research projects locally in the current working directory. There is no shared or centralized project storage.

## 3. Interaction flow

### First run

1. Explain what the skill does.
2. Offer the default audience profile or collect a custom global profile.
3. Save the profile locally for later runs.
4. Ask for a topic, idea, URL, notes, transcript, or other input.

### Every run

1. Inspect `./research/` for incomplete projects.
2. Ask whether to continue an existing project or start a new one.
3. For a new project, inspect the input and ask only high-value clarifying questions. Each question offers five topic-specific options; ask another question only when the answer can materially improve the research map. The user may optionally provide an early editorial focus, but a focus is never required before research.
4. Create a project folder and `brief.md`.
5. Build `question-map.md` as a map of research tasks, not a premature script outline. Anchor it in the desired viewer effect, practical usefulness, and evidence needs; include mechanisms, evidence, human dimension, practice, criticism, intellectual context, and visual/creative material.
6. Stop and wait for the user's confirmation or edits.
7. Run a broad first pass across the approved branches using web sources plus model knowledge. Save editorial source cards, quotations, media references, creative material, and open questions as they are found.
8. Save checkpoints after each major branch and update the source ledger for internal verification.
9. Run a synthesis pass: extract key findings, propose possible video structures, assemble scenario material, and identify the strongest and weakest directions.
10. Assemble `output/research.md` and offer HTML generation and optional post-research skills.

The user can narrow the topic, add a branch, return to the question map, save and continue later, or start over at any stage.

## 4. Research policy

- Search in any relevant language; write the report in Russian with translated descriptions where needed.
- Use model knowledge to generate and orient the question map, but label unverified claims until supported.
- Place a source link immediately beside every factual claim.
- Include a complete source list at the end.
- Evaluate sources by relevance, methodology, transparency, independence, and fit for the claim rather than by a rigid category hierarchy.
- When sources conflict, select the most convincing position while explicitly noting meaningful alternatives.
- If web search is unavailable, ask the user to provide sources or enable external search before starting a full research pass.
- Never invent facts, studies, quotations, cases, or events to fill gaps.
- Treat «maximum information» as broad coverage with diminishing returns, not an endless source dump. Stop a branch when new sources repeat the same finding, add no meaningful scenario material, or fail to resolve a relevant contradiction; record remaining gaps.
- Every important source becomes an editorial card with a plain-language takeaway, method, finding, meaning, limitations, source, and scenario application. A source is not finished when it has merely been paraphrased.

## 5. Evidence and creativity language

The final `research.md` does not use repetitive inline status tags or loud confidence markers. Evidence is communicated through precise wording, source links, method details, and limitations. For example: «В метаанализе 94 независимых тестов обнаружили…», «Это может означать…», «Авторы не проверяли…».

Technical source evaluation remains in `source-ledger.md` and review files for fact-checking. It is not repeated in the reader-facing report.

The final report keeps factual material and creative material distinct through section structure and natural language:

- research findings describe what was studied and found;
- interpretations are introduced as possible readings or syntheses;
- creative concepts are grouped in a dedicated section;
- metaphors and short illustrations are explicitly presented as authorial devices, not real events.

Creative ideas may be bold and original, but factual inspiration never turns them into facts.

## 6. Report voice and output contract

The report is a practical editorial dossier, not an academic essay. It should be scan-friendly, concrete, and useful to a writer.

Style rules:

- Prefer short theses, bullets, tables, comparisons, and compact paragraphs.
- One meaningful idea per block.
- Put the thesis before its explanation.
- Explain why each strong item could help the future scenario: hook, scene, turn, conflict, visual, transition, or ending.
- Keep factual material and creative proposals visibly separate.
- Preserve weak or controversial links in a marked section instead of silently deleting them.

Recommended top-level structure:

1. Research passport.
2. Short summary: what we learned, first as 7–10 scan-friendly bullets and then as expanded explanations.
3. How to build the video: one recommended structure and 2–4 alternatives.
4. Research question coverage.
5. Key concepts and related frameworks.
6. Studies and evidence base.
7. Real cases and stories.
8. Quotations.
9. Books, videos, films, and other references.
10. Metaphors and short illustrative examples.
11. Ten wild concepts.
12. Gaps, risks, contradictions, and claims requiring more verification.
13. Complete sources.

Each important item should include a clear thesis, what it means, why it belongs in the dossier, source or origin, limitations where relevant, and 2–3 sentences on how it could serve the scenario. The report is research fuel and scenario assembly material, not a finished script.

The former «Opportunity map» is replaced by «How to build the video». It appears after the short summary, when there is enough material to propose structures without pretending that one has already been chosen.

Required comparison tables include:

- concept comparison;
- claim/evidence/objection/source/scenario use;
- case/story/conflict/visual potential/source;
- creative idea/factual basis/effect/risk/priority.

## 7. Quotations and media references

Quotations are a dedicated module. Each entry includes a Russian translation first, the exact original quote, author and source, context, scenario use, and a verification locator such as page, chapter, timestamp, or URL.

Only verified wording may be presented as a direct quotation. Otherwise use a clearly marked paraphrase. Translations should be labeled, with the original retained where useful. Quotes should be short and functional.

The references module includes books, research papers, lectures, videos, films, interviews, essays, and documentaries. Each item explains what to take from it and how it might serve the video.

Quotes and references are editorial assets, not a bibliography dump. Each one needs a short explanation of why it is strong, what idea it adds, and where it could appear in the future video. An unverified wording is a paraphrase, never a direct quote.

## 8. Ten wild concepts

Every dossier includes ten unusual concepts directly in the final `research.md`, not necessarily opening hooks. They may be a new explanatory frame, provocative comparison, thought experiment, theory collision, cross-domain transfer, visual metaphor, question-driven structure, counterintuitive thesis, unusual protagonist/case, or unconventional format.

Each includes:

- name;
- core idea;
- convention it breaks;
- image or mechanism;
- factual anchor, if any;
- possible video application;
- risk of overreach;
- priority.

The whole section is explicitly creative, so repeated status tags are unnecessary. Each entry must still identify its factual anchor, if any, and its risk of being mistaken for a factual claim.

## 9. Project storage and checkpoints

Each research is an independent project under the current working directory:

```text
./research/<project-slug>/
├── PROJECT.md
├── input/
│   └── original-material.md
├── working/
│   ├── brief.md
│   ├── question-map.md
│   ├── source-ledger.md
│   ├── findings.md
│   ├── creative-lab.md
│   └── open-questions.md
├── output/
│   └── research.md
└── reviews/
    ├── factcheck.md
    ├── critic.md
    └── editorial-review.md
```

`PROJECT.md` stores the project title, date, status, last completed stage, current task, and links to artifacts. HTML is written to `output/research.html` only after an explicit request. Original outputs are not overwritten by post-research reviews.

On resume, the skill reads project state, identifies the last completed stage, and asks whether to continue, return to an earlier stage, or begin a new project. Incomplete material is not treated as final evidence.

## 10. HTML publisher

HTML is an optional visual assembly of the Markdown dossier and available reviews. It may include navigation, cards, restrained evidence styling without repetitive labels, expandable details, clickable sources, build date, project status, review status, and useful visualizations such as timelines, relationship maps, comparison matrices, or cause/effect diagrams.

HTML must not add facts or alter the meaning of Markdown. It should add a `Copy` button next to useful blocks such as theses, quotations, cases, metaphors, concepts, comparisons, and tables. Copying exports clean text only, with relevant source links preserved; interface labels and Markdown markup are excluded.

## 11. Optional post-research skills

- `research-critic`: finds banalities, logical jumps, weak links, and missing counterarguments.
- `research-factcheck`: rechecks claims, sources, quotations, and interpretations.
- `research-editorial-review`: evaluates conflict, clarity, emotional stakes, visuality, and scenario potential.
- `research-concept-refiner`: develops selected directions into stronger editorial concepts without writing the final script.
- `research-html`: assembles the final visual report.

The main skill offers these after the dossier is complete. They read saved project artifacts and write new review files rather than overwriting the research.

## 12. Quality gate

A dossier is ready when it has:

- an approved question map;
- multiple viable angles;
- sourced key claims;
- source limitations and unresolved source-quality questions;
- unexpected or counterintuitive material where relevant;
- real cases or stories where relevant;
- verified or explicitly paraphrased quotations;
- useful media references;
- metaphors and short illustrations;
- ten wild concepts;
- explicit contradictions, gaps, and risks;
- a scenario-use note for strong items;
- a complete source list.

The skill must report missing layers instead of pretending the research is complete.

## 13. Reference case and acceptance test

The repository includes a complete example for `Immunity to Change` / «Иммунитет к изменениям». It demonstrates the whole workflow: audience brief, question map, related concepts, studies and limits, real stories, verified quotes, media references, metaphors, ten wild concepts, reader-friendly evidence language, gaps, citations, checkpoints, and final Markdown. It remains a research dossier, not a finished script.

## 14. Platform and repository documentation

The repository contains a platform-independent core and thin adapters for ChatGPT/Codex, Claude Code, and compatible environments. README must cover purpose, installation, quick start, global audience, project storage, resume behavior, HTML, post-research skills, web-search limitations, privacy responsibility, reference example, and support policy. The project should also include a license, changelog, contribution guide, compatibility notes, and release checklist.

## 15. Non-functional requirements and risks

- Performance: no strict time limit; quality and coverage take priority.
- Scale: local, single-user projects; no centralized service or shared storage.
- Privacy: users are responsible for sensitive input; the skill does not promise automatic anonymization.
- Reliability: checkpoints and human-readable artifacts make interruption recoverable.
- Maintenance: one core contract, thin platform adapters, documented compatibility checks.
- Risk: platform specifications and web-search capabilities may change; adapters and README need version/date checks.
- Risk: creative ambition can drift into unsupported claims; clear language, source links, limitations, and an internal source ledger are mandatory.

## 16. Decision log

1. Use one front-door `Research` skill with modular internals and optional companion skills.
2. Use adaptive depth based on coverage and quality, not a fixed source count or time limit.
3. Require user confirmation after the question map.
4. Separate evidence, interpretation, speculation, and fiction through section structure, precise language, sources, and limitations; keep technical statuses internal.
5. Allow metaphors and short invented examples, but not invented full stories.
6. Put source links beside factual claims and include a complete bibliography.
7. Use a global editable audience profile with a Dashkiev-style default.
8. Store each project locally under `./research/<slug>/` with checkpoints.
9. Produce Markdown first; generate HTML only on request.
10. Make HTML a visual assembly layer with plain-text copy controls.
11. Treat «Иммунитет к изменениям» as the reference case and acceptance test.
12. Prioritize strong video potential while requiring factual verification for key claims.
13. Do not require an editorial line before the open research pass; an early focus is optional.
14. Use a two-pass workflow: broad factual and creative collection first, editorial synthesis second.
15. Ask only high-value clarifying questions, with five topic-specific options per question.
16. Make the editorial card the core research unit: fact, meaning, limitations, source, and scenario use.
17. Put short findings first and possible video structures immediately after them.
18. Remove repetitive evidence tags from the reader-facing report; retain technical evaluation only in `source-ledger.md` and reviews.
19. Keep metaphors, illustrations, and ten wild concepts in a distinct creative layer.
20. Present one recommended video structure plus several alternatives, each mapped to available material and risks.
21. Stop research adaptively when new sources add no meaningful evidence, interpretation, or scenario material, while recording gaps.
