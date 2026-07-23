#!/usr/bin/env python3
"""Calculate a job-fit score from component scores.

Usage:
  python scripts/score_job.py --seniority 12 --domain 10 --functional 17 --achievement 8 --skill 12 --motivation 9 --constraint 10 --narrative 4 --penalty -3
"""

from __future__ import annotations

import argparse

MAXIMA = {
    "seniority": 15,
    "domain": 15,
    "functional": 20,
    "achievement": 10,
    "skill": 15,
    "motivation": 10,
    "constraint": 10,
    "narrative": 5,
}


def decision(score: int) -> str:
    if score >= 90:
        return "Strong Apply"
    if score >= 80:
        return "Apply"
    if score >= 70:
        return "Network First"
    if score >= 60:
        return "Monitor / Stretch"
    return "Ignore"


def bounded(value: int, low: int, high: int, name: str) -> int:
    if value < low or value > high:
        raise ValueError(f"{name} must be between {low} and {high}; got {value}")
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate job-fit score.")
    for name, max_value in MAXIMA.items():
        parser.add_argument(f"--{name}", type=int, required=True, help=f"0-{max_value}")
    parser.add_argument("--penalty", type=int, default=0, help="0 to -20")
    args = parser.parse_args()

    values = {}
    for name, max_value in MAXIMA.items():
        values[name] = bounded(getattr(args, name), 0, max_value, name)
    penalty = bounded(args.penalty, -20, 0, "penalty")

    total = sum(values.values()) + penalty
    total = max(0, min(100, total))

    print(f"Fit Score: {total}/100")
    print(f"Decision: {decision(total)}")


if __name__ == "__main__":
    main()
