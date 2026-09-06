#!/usr/bin/env python3
"""Read the lightweight state stored in a research project's PROJECT.md."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def read_state(project: Path) -> dict[str, str | list[str]]:
    project_file = project / "PROJECT.md"
    if not project_file.is_file():
        raise FileNotFoundError(project_file)
    values: dict[str, str | list[str]] = {}
    for line in project_file.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^-\s+([\w-]+):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip("`")
    required = ("working/brief.md", "working/question-map.md", "working/source-ledger.md", "output/research.md")
    values["missing_artifacts"] = [item for item in required if not (project / item).is_file()]
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    args = parser.parse_args()
    state = read_state(args.project)
    for key, value in state.items():
        if isinstance(value, list):
            value = ", ".join(value) if value else "none"
        print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
