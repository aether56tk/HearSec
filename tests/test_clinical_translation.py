from clinical.translator import translate_finding


def test_insufficient_evidence_is_conservative():
    result = translate_finding(
        "privacy",
        status="insufficient_evidence",
        evidence_strength="unknown",
    )
    assert "insufficient" in result["message"].lower()
    assert "vulnerability" in result["message"].lower()


def test_confirmed_status_requires_follow_up():
    result = translate_finding(
        "pairing_authentication",
        status="supported_finding",
    )
    assert result["recommended_action"]
