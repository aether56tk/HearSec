import pytest\nfrom assessment.engine import calculate_risk, severity_from_score, build_finding\n\n\ndef test_calculate_risk():\n    assert calculate_risk(3, 4) == 12\n\n\ndef test_severity_boundaries():\n    assert severity_from_score(1) == "informational"\n    assert severity_from_score(4) == "low"\n    assert severity_from_score(8) == "medium"\n    assert severity_from_score(15) == "high"\n    assert severity_from_score(20) == "critical"\n\n\ndef test_build_finding():\n    finding = build_finding("F-001", "Example", 4, 4)\n    assert finding.severity == "high"\n

def test_invalid_risk_inputs():
    import pytest
    with pytest.raises(ValueError):
        calculate_risk(0, 3)
    with pytest.raises(ValueError):
        calculate_risk(3, 6)


def test_all_severity_boundaries():
    assert severity_from_score(3) == "informational"
    assert severity_from_score(7) == "low"
    assert severity_from_score(14) == "medium"
    assert severity_from_score(19) == "high"
    assert severity_from_score(25) == "critical"


def test_build_finding_risk_consistency():
    f = build_finding("F-1", "Test", 4, 5, "evidence", "recommendation")
    assert f.likelihood == 4
    assert f.impact == 5
    assert f.severity == "critical"
