import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "scripts" / "validate_benchmark.py"
EVALUATOR = ROOT / "scripts" / "evaluate_outputs.py"


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
    )


def valid_case(case_id: str = "H-001") -> dict:
    return {
        "id": case_id,
        "skill": "myanmar-humanizer",
        "category": "meaning-preservation",
        "input": "AI Automation ကို ၃ ကြိမ် စမ်းသပ်မယ်။",
        "expected_labels": ["H2"],
        "allowed_decisions": ["rewrite"],
        "expected_behavior": "ထပ်နေသောစာကို လျှော့ပြီး အချက်အလက်ကို ထိန်းသိမ်းရန်",
        "acceptable_alternatives": ["AI Automation ကို ၃ ကြိမ် စမ်းမယ်။"],
        "preserve_exact": ["AI Automation", "၃"],
        "forbid_exact": ["၅ ကြိမ်"],
        "confidence": "recommended_change",
        "source": "native-review-pending",
        "review_status": "draft",
    }


class ValidateBenchmarkTests(unittest.TestCase):
    def run_validator(self, rows: list[dict], *args: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / "cases.jsonl"
            write_jsonl(fixture, rows)
            return subprocess.run(
                [sys.executable, str(VALIDATOR), str(fixture), "--min-cases", "1", *args],
                text=True,
                capture_output=True,
                check=False,
            )

    def test_accepts_a_valid_fixture(self) -> None:
        result = self.run_validator([valid_case()])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Validated 1 benchmark case", result.stdout)

    def test_rejects_duplicate_case_ids(self) -> None:
        result = self.run_validator([valid_case(), valid_case()])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate id H-001", result.stderr)

    def test_rejects_missing_required_fields(self) -> None:
        case = valid_case()
        del case["expected_behavior"]
        result = self.run_validator([case])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing required field expected_behavior", result.stderr)

    def test_rejects_preservation_tokens_absent_from_input(self) -> None:
        case = valid_case()
        case["preserve_exact"].append("မူရင်းမှာမရှိ")
        result = self.run_validator([case])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("preserve_exact token not found in input", result.stderr)

    def test_rejects_unknown_decision_names(self) -> None:
        case = valid_case()
        case["allowed_decisions"] = ["invent"]
        result = self.run_validator([case])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown allowed_decision invent", result.stderr)

    def test_rejects_id_prefix_that_does_not_match_skill(self) -> None:
        case = valid_case("G-001")
        result = self.run_validator([case])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("id G-001 does not match skill myanmar-humanizer", result.stderr)


class EvaluateOutputsTests(unittest.TestCase):
    def run_evaluator(
        self, cases: list[dict], outputs: list[dict]
    ) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / "cases.jsonl"
            result_file = Path(tmp) / "outputs.jsonl"
            write_jsonl(fixture, cases)
            write_jsonl(result_file, outputs)
            return subprocess.run(
                [sys.executable, str(EVALUATOR), str(fixture), str(result_file)],
                text=True,
                capture_output=True,
                check=False,
            )

    def test_accepts_output_that_preserves_protected_text(self) -> None:
        result = self.run_evaluator(
            [valid_case()],
            [
                {
                    "id": "H-001",
                    "decision": "rewrite",
                    "labels": ["H2"],
                    "output": "AI Automation ကို ၃ ကြိမ် စမ်းမယ်။",
                }
            ],
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("1/1 outputs passed", result.stdout)

    def test_rejects_output_that_drops_a_protected_token(self) -> None:
        result = self.run_evaluator(
            [valid_case()],
            [
                {
                    "id": "H-001",
                    "decision": "rewrite",
                    "labels": ["H2"],
                    "output": "AI စနစ်ကို စမ်းမယ်။",
                }
            ],
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing protected token", result.stdout)

    def test_rejects_output_that_adds_a_forbidden_claim(self) -> None:
        result = self.run_evaluator(
            [valid_case()],
            [
                {
                    "id": "H-001",
                    "decision": "rewrite",
                    "labels": ["H2"],
                    "output": "AI Automation ကို ၃ ကြိမ်မဟုတ်ဘဲ ၅ ကြိမ် စမ်းမယ်။",
                }
            ],
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("forbidden text added", result.stdout)

    def test_rejects_an_unexpected_decision(self) -> None:
        result = self.run_evaluator(
            [valid_case()],
            [
                {
                    "id": "H-001",
                    "decision": "no_change",
                    "labels": ["H2"],
                    "output": "AI Automation ကို ၃ ကြိမ် စမ်းသပ်မယ်။",
                }
            ],
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("decision no_change is not allowed", result.stdout)

    def test_rejects_missing_output_ids(self) -> None:
        result = self.run_evaluator([valid_case()], [])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing output for H-001", result.stdout)

    def test_rejects_output_missing_an_expected_label(self) -> None:
        result = self.run_evaluator(
            [valid_case()],
            [
                {
                    "id": "H-001",
                    "decision": "rewrite",
                    "labels": [],
                    "output": "AI Automation ကို ၃ ကြိမ် စမ်းမယ်။",
                }
            ],
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing expected label H2", result.stdout)

    def test_rejects_duplicate_output_ids(self) -> None:
        output = {
            "id": "H-001",
            "decision": "rewrite",
            "labels": ["H2"],
            "output": "AI Automation ကို ၃ ကြိမ် စမ်းမယ်။",
        }
        result = self.run_evaluator([valid_case()], [output, output])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate output id H-001", result.stdout)


if __name__ == "__main__":
    unittest.main()
