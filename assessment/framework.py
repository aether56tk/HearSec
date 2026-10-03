"""HearSec framework metadata and domain helpers.

This module defines the research framework used by the assessment workflow.
It is descriptive and deterministic: it does not infer vulnerabilities.
"""

from __future__ import annotations

from typing import Any

FRAMEWORK_VERSION = "0.2.0"

DOMAINS = (
    ("device_identity", "Device Identity"),
    ("connectivity", "Connectivity"),
    ("pairing_authentication", "Pairing & Authentication"),
    ("services_interfaces", "Services & Interfaces"),
    ("firmware_updates", "Firmware Updates"),
    ("companion_app", "Companion Application"),
    ("cloud_services", "Cloud Services"),
    ("privacy", "Privacy & Data Handling"),
    ("clinical_software", "Clinical Fitting Software"),
    ("access_control", "Access Control & Authorization"),
    ("logging_monitoring", "Logging & Monitoring"),
    ("resilience", "System Resilience"),
    ("physical_service", "Physical & Service Boundaries"),
)

DOMAIN_IDS = tuple(item[0] for item in DOMAINS)


def framework_metadata() -> dict[str, Any]:
    """Return machine-readable HearSec framework metadata."""
    return {
        "name": "HearSec",
        "version": FRAMEWORK_VERSION,
        "purpose": (
            "Evidence-grounded cybersecurity and privacy assessment "
            "for connected hearing-aid ecosystems."
        ),
        "domains": [
            {"id": domain_id, "name": name, "order": index}
            for index, (domain_id, name) in enumerate(DOMAINS, start=1)
        ],
        "principles": [
            "Evidence before conclusion",
            "Unknown remains unknown",
            "Human verification for AI-generated interpretations",
            "Authorized research only",
            "Clinical translation without alarmist claims",
        ],
    }


def validate_domain_status(value: Any) -> str:
    """Normalize a domain status without inventing assessment certainty."""
    status = "" if value is None else str(value).strip().casefold()
    allowed = {
        "not_assessed",
        "assessed",
        "partial",
        "not_applicable",
        "insufficient_evidence",
    }
    return status if status in allowed else "not_assessed"


def domain_coverage(assessment: dict[str, Any]) -> dict[str, Any]:
    """Calculate transparent domain coverage."""
    domains = assessment.get("security_domains", {})
    if not isinstance(domains, dict):
        domains = {}

    states: dict[str, str] = {}
    for domain_id in DOMAIN_IDS:
        record = domains.get(domain_id, {})
        states[domain_id] = validate_domain_status(
            record.get("status") if isinstance(record, dict) else None
        )

    assessed = sum(
        state in {"assessed", "partial", "insufficient_evidence"}
        for state in states.values()
    )

    return {
        "total": len(DOMAIN_IDS),
        "assessed": assessed,
        "unassessed": len(DOMAIN_IDS) - assessed,
        "percentage": round((assessed / len(DOMAIN_IDS)) * 100, 2),
        "states": states,
    }
