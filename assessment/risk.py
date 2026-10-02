from __future__ import annotations

from typing import Any

from assessment.engine import calculate_risk, severity_from_score

LIKELIHOOD_LABELS = {
    "rare": 1,
    "unlikely": 2,
    "possible": 3,
    "likely": 4,
    "almost_certain": 5,
}

IMPACT_LABELS = {
    "negligible": 1,
    "minor": 2,
    "moderate": 3,
    "major": 4,
    "severe": 5,
}


def _to_score(value: Any, labels: dict[str, int], field: str) -> int | None:
    if isinstance(value, bool):
        raise ValueError(f"{field} must be 1-5 or a supported label")
    if isinstance(value, int):
        if 1 <= value <= 5:
            return value
        raise ValueError(f"{field} must be between 1 and 5")
    if isinstance(value, str):
        key = value.strip().lower().replace(" ", "_")
        if key in {"unknown", "not_rated", "not_assessed", "n/a"}:
            return None
        if key in labels:
            return labels[key]
    raise ValueError(f"{field} must be 1-5 or a supported label")


def assess_risk(likelihood: Any, impact: Any) -> dict[str, Any]:
    """Return transparent risk metadata without inventing a rating for unknown inputs."""
    likelihood_score = _to_score(likelihood, LIKELIHOOD_LABELS, "likelihood")
    impact_score = _to_score(impact, IMPACT_LABELS, "impact")

    if likelihood_score is None or impact_score is None:
        return {
            "likelihood_score": None,
            "impact_score": None,
            "score": None,
            "level": "not_rated",
        }

    score = calculate_risk(likelihood_score, impact_score)
    return {
        "likelihood_score": likelihood_score,
        "impact_score": impact_score,
        "score": score,
        "level": severity_from_score(score),
    }


def summarize_findings(findings: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize only findings with calculable numeric risk."""
    summary = {
        "total": len(findings),
        "rated": 0,
        "not_rated": 0,
        "by_level": {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "informational": 0,
        },
    }

    for finding in findings:
        risk = finding.get("risk", {})
        result = assess_risk(risk.get("likelihood"), risk.get("impact"))
        if result["score"] is None:
            summary["not_rated"] += 1
        else:
            summary["rated"] += 1
            summary["by_level"][result["level"]] += 1

    return summary
