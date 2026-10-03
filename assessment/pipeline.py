"""End-to-end deterministic HearSec assessment pipeline."""

from __future__ import annotations

from typing import Any

from assessment.evidence import summarize_evidence
from assessment.framework import framework_metadata, domain_coverage
from assessment.hearing_aid import analyze_assessment
from assessment.risk import summarize_findings


def build_assessment_snapshot(assessment: dict[str, Any]) -> dict[str, Any]:
    """Build a reproducible analysis snapshot without modifying the input."""
    analysis = analyze_assessment(assessment)
    evidence = assessment.get("evidence", [])
    findings = assessment.get("findings", [])

    if not isinstance(evidence, list):
        evidence = []
    if not isinstance(findings, list):
        findings = []

    return {
        "framework": framework_metadata(),
        "assessment_id": assessment.get("assessment_id", ""),
        "target": assessment.get("target", {}),
        "coverage": domain_coverage(assessment),
        "evidence": summarize_evidence(evidence),
        "risk": summarize_findings(findings),
        "analysis": analysis,
        "limitations": [
            "The snapshot is limited to supplied assessment evidence.",
            "Unknown and unverified information is not converted into a vulnerability.",
            "Security status of a third-party device requires appropriate authorized evidence.",
        ],
    }
