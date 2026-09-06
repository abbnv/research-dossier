---
name: research-html
description: Assemble a completed local research dossier and available reviews into a navigable HTML report with plain-text copy controls.
---

# Research HTML

Run `scripts/render_html.py output/research.md output/research.html` from the project directory, or use the equivalent absolute paths. Include available review files only when the source dossier has them. Do not add facts or change the meaning of Markdown.

The HTML report should provide navigation, readable tables, evidence-status styling, clickable sources, review status, and useful visualizations only when they clarify relationships. Every useful block gets a `Скопировать` control that copies clean text only, preserving relevant source URLs while excluding interface labels and Markdown markup.
