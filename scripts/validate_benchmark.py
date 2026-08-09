#!/usr/bin/env python3
"""Validate machine-readable Burmese Language Skills benchmark fixtures."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = (
    "id",
    "skill",
    "category",
    "input",
    "expected_labels",
    "allowed_decisions",
    "expected_behavior",
    "acceptable_alternatives",
    "preserve_exact",
    "forbid_exact",
    "confidence",
    "source",
    "review_status",
)

LIST_FIELDS = (
    "expected_labels",
    "allowed_decisions",
    "acceptable_alternatives",
    "preserve_exact",
    "forbid_exact",
)

SKILL_PREFIXES = {
    "myanmar-text-normalizer": "N",
    "myanmar-grammar-checker": "G",
    "myanmar-style-guide": "S",
    "myanmar-humanizer": "H",
    "integration": "I",
}

KNOWN_DECISIONS = {
    "ask",
    "convert",
    "correct",
    "no_change",
    "no_content",
    "normalize",
    "report",
    "rewrite",
    "route",
}


def read_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    rows: list[dict[str, Any]] = []
    errors: list[str] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return rows, [f"{path}: cannot read file: {exc}"]

    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{line_number}: invalid JSON: {exc.msg}")
            continue
        if not isinstance(row, dict):
            errors.append(f"{path}:{line_number}: case must be a JSON object")
            continue
        row["__location__"] = f"{path}:{line_number}"
        rows.append(row)
    return rows, errors


def validate_case(case: dict[str, Any]) -> list[str]:
    location = case.get("__location__", "case")
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in case:
            errors.append(f"{location}: missing required field {field}")

    if errors:
        return errors

    for field in LIST_FIELDS:
        if not isinstance(case[field], list):
            errors.append(f"{location}: {field} must be an array")

    if not isinstance(case["input"], str):
        errors.append(f"{location}: input must be a string")
        return errors

    case_id = case["id"]
    skill = case["skill"]
    if isinstance(case_id, str) and isinstance(skill, str):
        prefix = SKILL_PREFIXES.get(skill)
        if prefix is None:
            errors.append(f"{location}: unknown skill {skill}")
        elif not re.fullmatch(rf"{prefix}-\d{{3}}", case_id):
            errors.append(f"{location}: id {case_id} does not match skill {skill}")

    if isinstance(case["allowed_decisions"], list):
        for decision in case["allowed_decisions"]:
            if decision not in KNOWN_DECISIONS:
                errors.append(f"{location}: unknown allowed_decision {decision}")

    if isinstance(case["preserve_exact"], list):
        for token in case["preserve_exact"]:
            if not isinstance(token, str) or not token:
                errors.append(f"{location}: preserve_exact tokens must be non-empty strings")
            elif token not in case["input"]:
                errors.append(
                    f"{location}: preserve_exact token not found in input: {token!r}"
                )
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixtures", nargs="+", type=Path)
    parser.add_argument("--min-cases", type=int, default=50)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cases: list[dict[str, Any]] = []
    errors: list[str] = []
    seen_ids: dict[str, str] = {}

    for fixture in args.fixtures:
        file_cases, file_errors = read_jsonl(fixture)
        cases.extend(file_cases)
        errors.extend(file_errors)

    for case in cases:
        errors.extend(validate_case(case))
        case_id = case.get("id")
        location = case.get("__location__", "case")
        if isinstance(case_id, str):
            if case_id in seen_ids:
                errors.append(
                    f"{location}: duplicate id {case_id}; first seen at {seen_ids[case_id]}"
                )
            else:
                seen_ids[case_id] = location

    if len(cases) < args.min_cases:
        errors.append(
            f"benchmark has {len(cases)} cases; minimum required is {args.min_cases}"
        )

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    noun = "case" if len(cases) == 1 else "cases"
    print(f"Validated {len(cases)} benchmark {noun} across {len(args.fixtures)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
