#!/usr/bin/env python3
"""Initialize a candidate workspace from templates."""

from __future__ import annotations

import shutil
from pathlib import Path

import os, sys

# Il workspace del candidato vive SEMPRE nella cartella di lavoro corrente (o in --dir),
# MAI nella cartella di installazione della skill (condivisa tra progetti).
TEMPLATES = Path(__file__).resolve().parents[1] / "templates"
_args = sys.argv[1:]
WORKSPACE = (Path(_args[_args.index("--dir") + 1]) if "--dir" in _args else Path.cwd()) / "candidate_workspace"

TEMPLATE_MAP = {
    "00_intake_notes.md": "00_intake_notes.md",
    "01_candidate_brief.md": "01_candidate_brief.md",
    "02_search_strategy.md": "02_search_strategy.md",
    "03_job_evaluations.md": "03_job_evaluations.md",
    "04_job_shortlist.md": "04_job_shortlist.md",
    "05_application_pack.md": "05_application_pack.md",
    "06_feedback_loop.md": "06_feedback_loop.md",
    "07_application_tracker.csv": "07_application_tracker.csv",
    "08_learning_log.md": "08_learning_log.md",
    "09_source_log.md": "09_source_log.md",
    "10_company_targets.csv": "10_company_targets.csv",
}


def main() -> None:
    WORKSPACE.mkdir(exist_ok=True)
    created = []
    skipped = []

    for template_name, output_name in TEMPLATE_MAP.items():
        src = TEMPLATES / template_name
        dst = WORKSPACE / output_name
        if not src.exists():
            raise FileNotFoundError(f"Missing template: {src}")
        if dst.exists():
            skipped.append(dst.name)
            continue
        shutil.copyfile(src, dst)
        created.append(dst.name)

    print(f"Workspace: {WORKSPACE}")
    if created:
        print("Created:")
        for name in created:
            print(f"- {name}")
    if skipped:
        print("Skipped existing files:")
        for name in skipped:
            print(f"- {name}")


if __name__ == "__main__":
    main()
