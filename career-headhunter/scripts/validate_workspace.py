#!/usr/bin/env python3
"""Validate that the candidate workspace contains required files."""

from __future__ import annotations

from pathlib import Path

import sys

_args = sys.argv[1:]
WORKSPACE = (Path(_args[_args.index("--dir") + 1]) if "--dir" in _args else Path.cwd()) / "candidate_workspace"
REQUIRED = [
    "00_intake_notes.md",
    "01_candidate_brief.md",
    "02_search_strategy.md",
    "03_job_evaluations.md",
    "04_job_shortlist.md",
    "05_application_pack.md",
    "06_feedback_loop.md",
    "07_application_tracker.csv",
    "08_learning_log.md",
    "09_source_log.md",
    "10_company_targets.csv",
]


def main() -> None:
    missing = [name for name in REQUIRED if not (WORKSPACE / name).exists()]
    if missing:
        print("Workspace validation failed. Missing files:")
        for name in missing:
            print(f"- {name}")
        raise SystemExit(1)
    print("Workspace validation passed.")


if __name__ == "__main__":
    main()
