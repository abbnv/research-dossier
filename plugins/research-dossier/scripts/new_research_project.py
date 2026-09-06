#!/usr/bin/env python3
"""Create a non-destructive local research project layout."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


FILES = {
    "input/original-material.md": "# Исходный материал\n\nДобавьте сюда тему, заметки, ссылку или транскрибацию.\n",
    "working/brief.md": "# Бриф\n\nСтатус: не заполнен\n",
    "working/question-map.md": "# Карта исследовательских задач\n\nСтатус: не подтверждена\n\nКарта будет заполнена после брифа и подтверждена до начала широкого ресерча.\n",
    "working/source-ledger.md": "# Внутренний реестр источников\n\nТехническая проверка источников хранится здесь и не дублируется в читательском отчёте.\n\n| Источник | Тезис | Метод / тип | Качество | Ограничения | Статус проверки | Следующий запрос |\n| --- | --- | --- | --- | --- | --- | --- |\n",
    "working/findings.md": "# Редакторские карточки находок\n\nПока нет собранных материалов. Важные источники оформляются карточками: факт, смысл, ограничения и сценарное применение.\n",
    "working/creative-lab.md": "# Креативная лаборатория\n\nСюда попадают сырые метафоры, короткие иллюстрации, визуальные решения и необычные концепции. В финальном отчёте творческий материал будет отделён от доказательной базы.\n",
    "working/open-questions.md": "# Открытые вопросы\n\nПока нет.\n",
    "output/research.md": "# Итоговый ресерч\n\nСтатус: не готов\n\nФинальный отчёт собирается после широкого прохода и сценарного синтеза.\n",
    "reviews/factcheck.md": "# Фактчек\n\nНе запускался.\n",
    "reviews/critic.md": "# Критика\n\nНе запускалась.\n",
    "reviews/editorial-review.md": "# Редакторский анализ\n\nНе запускался.\n",
}


def normalize_slug(value: str) -> str:
    value = value.strip().lower().replace("_", "-")
    value = re.sub(r"[^a-z0-9-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    if not value:
        raise ValueError("Project slug must contain at least one letter or digit")
    return value


def create_project(workdir: Path, slug: str, title: str) -> Path:
    normalized = normalize_slug(slug)
    project = workdir / "research" / normalized
    project.mkdir(parents=True, exist_ok=True)
    for relative, initial in FILES.items():
        path = project / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text(initial, encoding="utf-8")
    project_file = project / "PROJECT.md"
    if not project_file.exists():
        project_file.write_text(
            f"# {title}\n\n"
            f"- slug: `{normalized}`\n"
            f"- created: {date.today().isoformat()}\n"
            "- status: intake\n"
            "- last_completed: none\n"
            "- current_task: add source material and complete the brief\n",
            encoding="utf-8",
        )
    return project


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workdir", default=".")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", default=None)
    args = parser.parse_args()
    title = args.title or args.slug.replace("-", " ").title()
    project = create_project(Path(args.workdir).resolve(), args.slug, title)
    print(project)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
