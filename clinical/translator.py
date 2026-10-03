"""Clinical translation helpers for HearSec.

The translator intentionally uses conservative language. It maps a verified
technical category to a clinical communication template; it does not infer
patient harm or diagnose compromise.
"""

from __future__ import annotations

from typing import Any

CLINICAL_TEMPLATES = {
    "connectivity": {
        "clinical_context": "Wireless connectivity and device communication.",
        "action": "Review documented pairing, connection, and update guidance.",
    },
    "pairing_authentication": {
        "clinical_context": "Who is permitted to establish or maintain a device connection.",
        "action": "Review authorized host devices and follow manufacturer pairing guidance.",
    },
    "privacy": {
        "clinical_context": "Handling of personal or health-related information.",
        "action": "Review application permissions, data-sharing settings, and privacy documentation.",
    },
    "companion_app": {
        "clinical_context": "Security and privacy controls in the patient-facing application.",
        "action": "Use the current official application version and review documented permissions.",
    },
    "firmware_updates": {
        "clinical_context": "Security and integrity of device software updates.",
        "action": "Use only official update mechanisms and document the evaluated firmware version.",
    },
    "clinical_software": {
        "clinical_context": "Security controls surrounding clinical fitting software.",
        "action": "Follow authorized clinical software access and account-management procedures.",
    },
    "access_control": {
        "clinical_context": "Authorization and privilege management across the ecosystem.",
        "action": "Review roles, accounts, session controls, and authorized access.",
    },
}


def translate_finding(
    category: str,
    *,
    status: str,
    evidence_strength: str = "documented",
) -> dict[str, Any]:
    """Create a conservative clinician-facing interpretation."""
    key = str(category or "").strip().casefold()
    template = CLINICAL_TEMPLATES.get(
        key,
        {
            "clinical_context": "Connected hearing-aid cybersecurity assessment.",
            "action": "Review the documented evidence and follow authorized clinical/security procedures.",
        },
    )

    status_key = str(status or "insufficient_evidence").strip().casefold()
    if status_key in {"confirmed_observation", "supported_finding"}:
        message = "A documented assessment finding requires human review and appropriate follow-up."
    elif status_key == "not_applicable":
        message = "This assessment item is not applicable to the evaluated configuration."
    elif status_key == "not_assessed":
        message = "This assessment item was not evaluated."
    else:
        message = "Available evidence is insufficient to establish a cybersecurity vulnerability."

    return {
        "category": key,
        "status": status_key,
        "evidence_strength": evidence_strength,
        "clinical_context": template["clinical_context"],
        "message": message,
        "recommended_action": template["action"],
        "patient_safe_language": (
            "No conclusion beyond the available assessment evidence should be made."
        ),
    }
