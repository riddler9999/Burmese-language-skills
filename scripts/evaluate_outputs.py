#!/usr/bin/env python3
"""Check structured model outputs against benchmark safety constraints."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        if not isinstance(row, dict):
            raise ValueError(f"{path}:{line_number}: expected a JSON object")
        rows.append(row)
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path)
    parser.add_argument("outputs", type=Path)
    return parser.parse_args()


def evaluate_case(case: dict[str, Any], result: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    case_id = case["id"]
    output = result.get("output", "")
    decision = result.get("decision")
    labels = result.get("labels", [])

    if decision not in case["allowed_decisions"]:
        failures.append(f"decision {decision} is not allowed")

    if not isinstance(output, str):
        failures.append("output must be a string")
        return failures

    if not isinstance(labels, list):
        failures.append("labels must be an array")
        labels = []

    for label in case["expected_labels"]:
        if label not in labels:
            failures.append(f"missing expected label {label}")

    for token in case["preserve_exact"]:
        if token not in output:
            failures.append(f"missing protected token {token!r}")

    for token in case["forbid_exact"]:
        if token in output:
            failures.append(f"forbidden text added {token!r}")

    return [f"{case_id}: {failure}" for failure in failures]


def main() -> int:
    args = parse_args()
    cases = read_jsonl(args.fixture)
    outputs = read_jsonl(args.outputs)
    failures: list[str] = []
    passed = 0
    output_by_id: dict[Any, dict[str, Any]] = {}

    for row in outputs:
        output_id = row.get("id")
        if output_id in output_by_id:
            failures.append(f"{output_id}: duplicate output id {output_id}")
        else:
            output_by_id[output_id] = row

    for case in cases:
        case_id = case["id"]
        result = output_by_id.get(case_id)
        if result is None:
            failures.append(f"{case_id}: missing output for {case_id}")
            continue
        case_failures = evaluate_case(case, result)
        if case_failures:
            failures.extend(case_failures)
        else:
            passed += 1

    for failure in failures:
        print(f"FAIL {failure}")
    print(f"{passed}/{len(cases)} outputs passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
