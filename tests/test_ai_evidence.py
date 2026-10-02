from ai.evidence import (
    build_ai_assessment,
    compare_ai_to_expert,
    validate_ai_assessment,
)


def test_unknown_evidence_cannot_become_supported_finding():
    record = build_ai_assessment(
        evidence_id="E-001",
        evidence_text="Firmware security could not be verified.",
        evidence_status="unknown",
        ai_interpretation="Insufficient evidence.",
        proposed_status="supported_finding",
        source_refs=["E-001"],
    )
    assert record["proposed_status"] == "insufficient_evidence"
    assert validate_ai_assessment(record)["valid"]


def test_ai_record_requires_traceable_source():
    record = build_ai_assessment(
        evidence_id="E-002",
        evidence_text="Manufacturer documentation describes authenticated updates.",
        evidence_status="documented",
        ai_interpretation="Update authentication is documented but not independently verified.",
        proposed_status="confirmed_observation",
        source_refs=["E-002"],
    )
    assert validate_ai_assessment(record)["valid"]


def test_ai_expert_comparison():
    record = build_ai_assessment(
        evidence_id="E-003",
        evidence_text="Pairing requires user confirmation.",
        evidence_status="observed",
        ai_interpretation="Confirmed observation.",
        proposed_status="confirmed_observation",
        source_refs=["E-003"],
    )
    result = compare_ai_to_expert(record, "confirmed_observation")
    assert result["agreement"] is True
    assert result["human_correction_required"] is False
