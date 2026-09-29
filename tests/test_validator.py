import json
from pathlib import Path

from assessment.validator import validate_assessment
from reports.generate import render_report


ROOT = Path(__file__).resolve().parents[1]


def load_demo():
    return json.loads((ROOT / "assessment" / "example_assessment.json").read_text())


def test_demo_assessment_is_structurally_valid():
    assert validate_assessment(load_demo()) == []


def test_missing_required_field_is_reported():
    data = load_demo()
    del data["target"]
    errors = validate_assessment(data)
    assert "missing required field: target" in errors


def test_invalid_date_is_reported():
    data = load_demo()
    data["date"] = "29-09-2026"
    assert any("ISO format" in e for e in validate_assessment(data))


def test_report_contains_findings_and_scope():
    report = render_report(load_demo())
    assert "# HearSec Security & Privacy Assessment Report" in report
    assert "HS-DEMO-001" in report
    assert "Synthetic demonstration finding" in report
