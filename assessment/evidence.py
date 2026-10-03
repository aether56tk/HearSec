"""Evidence provenance and completeness helpers for HearSec."""

from __future__ import annotations

from typing import Any

EVIDENCE_STATUSES = (
    "observed",
    "laboratory_observation",
    "documented",
    "user_reported",
    "not_verified",
    "unknown",
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
    "user_report",
)

STATUS_ALIASES = {
    "observed": "observed",
    "documented": "documented",
    "lab": "laboratory_observation",
    "laboratory": "laboratory_observation",
    "laboratory_observation": "laboratory_observation",
    "user_report": "user_reported",
    "user_reported": "user_reported",
    "not_verified": "not_verified",
    "not verified": "not_verified",
    "unknown": "unknown",
    "": "unknown",
}


def normalize_status(value: Any) -> str:
    status = "" if value is None else str(value).strip().casefold()
    return STATUS_ALIASES.get(status, "unknown")


def evidence_confidence(status: Any) -> float:
    """Return a conservative provenance weight, not a probability of vulnerability."""
    weights = {
        "laboratory_observation": 1.0,
        "observed": 0.9,
        "documented": 0.8,
        "user_reported": 0.4,
        "not_verified": 0.0,
        "unknown": 0.0,
    }
    return weights[normalize_status(status)]


def summarize_evidence(evidence: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize evidence provenance without turning provenance into risk."""
    counts = {status: 0 for status in EVIDENCE_STATUSES}
    for record in evidence:
        status = normalize_status(record.get("status"))
        counts[status] += 1

    total = len(evidence)
    verified = total - counts["unknown"] - counts["not_verified"]

    return {
        "total": total,
        "verified_or_documented": verified,
        "unverified": counts["unknown"] + counts["not_verified"],
        "by_status": counts,
    }


def evidence_completeness(
    *,
    domain_count: int,
    assessed_domains: int,
    evidence_count: int,
) -> dict[str, Any]:
    """Report assessment completeness; this is not a security score."""
    if domain_count <= 0:
        percentage = 0.0
    else:
        percentage = round((assessed_domains / domain_count) * 100, 2)

    return {
        "domains_total": domain_count,
        "domains_assessed": assessed_domains,
        "evidence_records": evidence_count,
        "percentage": percentage,
        "meaning": (
            "Completeness describes how much of the defined assessment "
            "was evaluated; it does not indicate whether the device is secure."
        ),
    }
