"""Hearing-aid assessment helpers.

This module analyzes documented, authorized assessment evidence. It does not
perform device exploitation, interception, credential collection, or pairing
bypass.
"""

from __future__ import annotations

from typing import Any

from assessment.evidence import evidence_completeness, summarize_evidence
from assessment.framework import domain_coverage, framework_metadata

REQUIRED_TARGET_FIELDS = (
    "device_type",
    "manufacturer",
    "model",
    "firmware",
    "companion_app",
    "app_version",
    "platform",
)

ASSESSMENT_DOMAINS = (
    "device_identity",
    "connectivity",
    "pairing_authentication",
    "services_interfaces",
    "firmware_updates",
    "companion_app",
    "cloud_services",
    "privacy",
    "clinical_software",
    "access_control",
    "logging_monitoring",
    "resilience",
    "physical_service",
)

EVIDENCE_TYPES = (
    "manufacturer_documentation",
    "clinical_software_export",
    "companion_app_export",
    "authorized_sdk_api",
    "browser_observation",
    "laboratory_observation",
    "configuration_export",
    "security_test_record",
)


def _present(value: Any) -> bool:
    normalized = "" if value is None else str(value).strip().casefold()
    return normalized not in {"", "unknown", "not_assessed", "n/a", "na"}


def completeness_report(assessment: dict[str, Any]) -> dict[str, Any]:
    """Return coverage information without treating missing data as insecure."""
    target = assessment.get("target", {})
    if not isinstance(target, dict):
        target = {}

    missing_target = [
        field for field in REQUIRED_TARGET_FIELDS
        if not _present(target.get(field))
    ]

    evidence = assessment.get("evidence", [])
    if not isinstance(evidence, list):
        evidence = []

    domains = assessment.get("security_domains", {})
    if not isinstance(domains, dict):
        domains = {}

    assessed_domains = [
        domain for domain in ASSESSMENT_DOMAINS
        if isinstance(domains.get(domain), dict)
        and _present(domains[domain].get("status"))
        and str(domains[domain].get("status")).strip().casefold() != "not_assessed"
    ]

    return {
        "target_fields_total": len(REQUIRED_TARGET_FIELDS),
        "target_fields_present": len(REQUIRED_TARGET_FIELDS) - len(missing_target),
        "missing_target_fields": missing_target,
        "evidence_records": len(evidence),
        "domains_total": len(ASSESSMENT_DOMAINS),
        "domains_assessed": len(assessed_domains),
        "unassessed_domains": [
            d for d in ASSESSMENT_DOMAINS if d not in assessed_domains
        ],
        "coverage_status": (
            "complete"
            if not missing_target and len(assessed_domains) == len(ASSESSMENT_DOMAINS)
            else "partial"
        ),
    }


def analyze_assessment(assessment: dict[str, Any]) -> dict[str, Any]:
    """Produce a deterministic analysis summary from supplied assessment data."""
    findings = assessment.get("findings", [])
    if not isinstance(findings, list):
        findings = []

    evidence = assessment.get("evidence", [])
    if not isinstance(evidence, list):
        evidence = []

    controls = assessment.get("controls", [])
    if not isinstance(controls, list):
        controls = []

    data_flows = assessment.get("data_flows", [])
    if not isinstance(data_flows, list):
        data_flows = []

    completeness = completeness_report(assessment)
    domain_summary = domain_coverage(assessment)
    evidence_summary = summarize_evidence(evidence)
    completeness["domain_coverage"] = domain_summary
    completeness["evidence_summary"] = evidence_summary
    completeness["evidence_completeness"] = evidence_completeness(
        domain_count=domain_summary["total"],
        assessed_domains=domain_summary["assessed"],
        evidence_count=len(evidence),
    )

    rated = 0
    not_rated = 0
    risk_levels: dict[str, int] = {}
    for finding in findings:
        risk = finding.get("risk", {}) if isinstance(finding, dict) else {}
        if not isinstance(risk, dict):
            risk = {}
        likelihood = risk.get("likelihood")
        impact = risk.get("impact")
        try:
            likelihood_i = int(likelihood)
            impact_i = int(impact)
        except (TypeError, ValueError):
            likelihood_i = impact_i = 0

        if 1 <= likelihood_i <= 5 and 1 <= impact_i <= 5:
            score = likelihood_i * impact_i
            rated += 1
            level = (
                "critical" if score >= 20 else
                "high" if score >= 15 else
                "medium" if score >= 8 else
                "low" if score >= 4 else
                "informational"
            )
            risk_levels[level] = risk_levels.get(level, 0) + 1
        else:
            not_rated += 1

    return {
        "framework": framework_metadata(),
        "assessment_id": assessment.get("assessment_id", ""),
        "target": assessment.get("target", {}),
        "counts": {
            "findings": len(findings),
            "rated_findings": rated,
            "not_rated_findings": not_rated,
            "evidence": len(evidence),
            "controls": len(controls),
            "data_flows": len(data_flows),
        },
        "risk_distribution": risk_levels,
        "coverage": completeness,
        "limitations": [
            "Analysis is limited to evidence supplied in the assessment.",
            "Missing or unknown information is not treated as a vulnerability.",
            "Third-party security status is not established without appropriate authorized testing and evidence.",
        ],
    }
