from __future__ import annotations

from datetime import date
from typing import Any


def validate_assessment(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = ("assessment_id", "target", "date", "findings")
    for key in required:
        if key not in data:
            errors.append(f"missing required field: {key}")

    if "date" in data:
        try:
            date.fromisoformat(str(data["date"]))
        except ValueError:
            errors.append("date must use ISO format YYYY-MM-DD")

    target = data.get("target")
    if not isinstance(target, dict):
        errors.append("target must be an object")
    elif not target.get("device_type"):
        errors.append("target.device_type is required")

    findings = data.get("findings")
    if not isinstance(findings, list):
        errors.append("findings must be an array")
    else:
        for i, finding in enumerate(findings):
            prefix = f"findings[{i}]"
            if not isinstance(finding, dict):
                errors.append(f"{prefix} must be an object")
                continue
            for key in ("id", "category", "title", "evidence", "risk"):
                if key not in finding:
                    errors.append(f"{prefix}: missing {key}")
            risk = finding.get("risk")
            if isinstance(risk, dict):
                for key in ("likelihood", "impact"):
                    if key not in risk:
                        errors.append(f"{prefix}.risk: missing {key}")
            else:
                errors.append(f"{prefix}.risk must be an object")

    return errors


def assert_valid_assessment(data: dict[str, Any]) -> None:
    errors = validate_assessment(data)
    if errors:
        raise ValueError("; ".join(errors))
