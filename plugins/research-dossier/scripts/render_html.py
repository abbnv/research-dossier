#!/usr/bin/env python3
"""Render a small, portable Markdown dossier as a navigable HTML report."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path


LINK_PATTERN = re.compile(r"\[([^\]]+)\]\((https?://(?:[^()\s]|\([^()\s]*\))*)\)")


def plain_text(value: str) -> str:
    value = LINK_PATTERN.sub(r"\1 (\2)", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"\1", value)
    value = re.sub(r"__([^_]+)__", r"\1", value)
    value = value.replace("`", "")
    return value


def inline(value: str) -> str:
    escaped = html.escape(value, quote=True)
    escaped = LINK_PATTERN.sub(r'<a href="\2" target="_blank" rel="noreferrer">\1</a>', escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    return escaped


def copy_button(text: str) -> str:
    payload = html.escape(json.dumps(plain_text(text), ensure_ascii=False), quote=True)
    return f'<button class="copy-button" data-copy="{payload}">Скопировать</button>'


def render_table(lines: list[str]) -> str:
    rows = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells or all(set(cell) <= {"-", ":", " "} for cell in cells):
            continue
        rows.append(cells)
    if not rows:
        return ""
    head, *body = rows
    result = ["<table><thead><tr>"]
    result.extend(f"<th>{inline(cell)}</th>" for cell in head)
    result.append("</tr></thead><tbody>")
    for row in body:
        result.append("<tr>")
        result.extend(f"<td>{inline(cell)}</td>" for cell in row)
        result.append("</tr>")
    result.append("</tbody></table>")
    result.append(copy_button("\n".join(" | ".join(row) for row in rows)))
    return "".join(result)


def render(markdown: str) -> str:
    lines = markdown.splitlines()
    body: list[str] = []
    headings: list[tuple[str, str]] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            title = heading.group(2).strip()
            anchor = re.sub(r"[^a-z0-9-]+", "-", title.lower()).strip("-") or f"section-{index}"
            tag = f"h{level}"
            body.append(f'<{tag} id="{anchor}">{inline(title)}</{tag}>')
            if level <= 2:
                headings.append((anchor, title))
            index += 1
            continue
        if line.startswith("|"):
            table_lines = []
            while index < len(lines) and lines[index].startswith("|"):
                table_lines.append(lines[index])
                index += 1
            body.append(render_table(table_lines))
            continue
        if line.startswith("> "):
            quote = line[2:]
            body.append(f'<blockquote>{inline(quote)}{copy_button(quote)}</blockquote>')
            index += 1
            continue
        if re.match(r"^[-*]\s+", line):
            items = []
            while index < len(lines) and re.match(r"^[-*]\s+", lines[index]):
                item = re.sub(r"^[-*]\s+", "", lines[index])
                items.append(f"<li>{inline(item)}</li>")
                index += 1
            text = "\n".join(re.sub(r"<[^>]+>", "", item) for item in items)
            body.append(f'<ul>{"".join(items)}</ul>{copy_button(text)}')
            continue
        paragraph = [line]
        index += 1
        while index < len(lines) and lines[index].strip() and not re.match(r"^(#{1,3})\s+|^\||^>\s|^[-*]\s+", lines[index]):
            paragraph.append(lines[index])
            index += 1
        text = "\n".join(paragraph)
        status_class = ""
        if "[ДОКАЗАНО]" in text:
            status_class = " evidence-proven"
        elif "[КРЕАТИВНАЯ ГИПОТЕЗА]" in text:
            status_class = " evidence-creative"
        body.append(f'<div class="content-block{status_class}"><p>{inline(text)}</p>{copy_button(text)}</div>')
    nav = "".join(f'<a href="#{anchor}">{html.escape(title)}</a>' for anchor, title in headings)
    script = """document.querySelectorAll('.copy-button').forEach((b)=>b.addEventListener('click',async()=>{await navigator.clipboard.writeText(JSON.parse(b.dataset.copy));const t=b.textContent;b.textContent='Скопировано';setTimeout(()=>b.textContent=t,1200)}));"""
    return f"""<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Research Dossier</title><style>{CSS}</style></head><body>
<aside><h2>Навигация</h2>{nav}</aside><main>{''.join(body)}</main>
<script>{script}</script>
</body></html>"""


CSS = """
:root{font-family:Inter,ui-sans-serif,system-ui,sans-serif;color:#172033;background:#f5f7fb;line-height:1.5}
body{display:flex;max-width:1400px;margin:0 auto}aside{position:sticky;top:0;width:230px;height:100vh;padding:28px 20px;background:#101827;color:#dbe6f5;box-sizing:border-box}aside a{display:block;color:#b9c8de;text-decoration:none;padding:7px 0;font-size:14px}main{background:white;min-height:100vh;flex:1;padding:44px clamp(24px,5vw,80px)}h1{font-size:38px}h2{margin-top:42px;border-bottom:1px solid #e6eaf0;padding-bottom:8px}h3{margin-top:28px}.content-block,blockquote,table{margin:14px 0;padding:14px 16px;border:1px solid #e4e9f1;border-radius:10px;background:#fff}.content-block evidence{}.evidence-proven{border-left:5px solid #22a06b}.evidence-creative{border-left:5px solid #8b5cf6;background:#fbf9ff}blockquote{border-left:5px solid #f59e0b;color:#5a3d05}table{border-collapse:collapse;width:100%;padding:0}th,td{padding:10px;border-bottom:1px solid #e8edf4;text-align:left;vertical-align:top}th{background:#f2f5f9}.copy-button{float:right;border:0;border-radius:6px;background:#e8eef8;color:#1c4e89;padding:5px 9px;cursor:pointer;font-size:12px}.copy-button:hover{background:#d8e5f7}code{background:#eef2f7;padding:2px 4px;border-radius:4px}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(args.source.read_text(encoding="utf-8")), encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
