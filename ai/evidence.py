"""Evidence-grounded AI-assessment helpers for HearSec.

This module provides deterministic structures and validation rules for an AI
assistant. It does not connect to an LLM and does not perform device testing.

Design principle:
    evidence -> AI interpretation -> human verification -> final finding

An AI result must never upgrade missing/unknown evidence into a vulnerability.
"""

from __future__ import annotations

from typing import Any

FINAL_STATUSES = {
    "confirmed_observation",
    "supported_finding",
    "insufficient_evidence",
    "not_assessed",
    "not_applicable",
}


def normalize_evidence_status(value: Any) -> str:
    """Normalize evidence status without inventing certainty."""
    status = "" if value is None else str(value).strip().casefold()
    aliases = {
        "documented": "documented",
        "observed": "observed",
        "lab": "laboratory_observation",
        "laboratory": "laboratory_observation",
        "user reported": "user_reported",
        "user_reported": "user_reported",
        "not verified": "not_verified",
        "not_verified": "not_verified",
        "unknown": "unknown",
        "": "unknown",
    }
    return aliases.get(status, "unknown")


def build_ai_assessment(
    *,
    evidence_id: str,
    evidence_text: str,
    evidence_status: str,
    ai_interpretation: str,
    proposed_status: str,
    source_refs: list[str] | None = None,
) -> dict[str, Any]:
    """Create an auditable AI assessment record."""
    status = normalize_evidence_status(evidence_status)
    proposed = str(proposed_status or "insufficient_evidence").strip().casefold()
    if proposed not in FINAL_STATUSES:
        proposed = "insufficient_evidence"

    if status in {"unknown", "not_verified"} and proposed == "supported_finding":
        proposed = "insufficient_evidence"

    refs = [str(ref) for ref in (source_refs or []) if str(ref).strip()]
    return {
        "evidence_id": evidence_id,
        "evidence_text": evidence_text,
        "evidence_status": status,
        "ai_interpretation": ai_interpretation,
        "proposed_status": proposed,
        "source_refs": refs,
        "human_verification": {
            "status": "pending",
            "reviewer": None,
            "decision": None,
            "notes": None,
        },
    }


def validate_ai_assessment(record: dict[str, Any]) -> dict[str, Any]:
    """Validate traceability and safety constraints on an AI result."""
    errors: list[str] = []
    evidence_id = record.get("evidence_id")
    status = normalize_evidence_status(record.get("evidence_status"))
    proposed = str(record.get("proposed_status", "")).strip().casefold()
    refs = record.get("source_refs", [])

    if not evidence_id:
        errors.append("evidence_id is required")
    if not str(record.get("evidence_text", "")).strip():
        errors.append("evidence_text is required")
    if proposed not in FINAL_STATUSES:
        errors.append("proposed_status is not an allowed HearSec status")
    if not isinstance(refs, list) or not refs:
        errors.append("at least one source reference is required")
    if status in {"unknown", "not_verified"} and proposed == "supported_finding":
        errors.append("unknown or unverified evidence cannot support a finding")

    return {"valid": not errors, "errors": errors}


def compare_ai_to_expert(
    ai_record: dict[str, Any],
    expert_status: str,
) -> dict[str, Any]:
    """Return simple evaluation fields for an AI-vs-expert study."""
    ai_status = str(ai_record.get("proposed_status", "")).strip().casefold()
    expert = str(expert_status or "").strip().casefold()
    agreement = ai_status == expert
    return {
        "ai_status": ai_status,
        "expert_status": expert,
        "agreement": agreement,
        "human_correction_required": not agreement,
    }
