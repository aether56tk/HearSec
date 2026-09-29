import pytest

from assessment.engine import calculate_risk, severity_from_score, build_finding


def test_calculate_risk():
    assert calculate_risk(3, 4) == 12


def test_severity_boundaries():
    assert severity_from_score(1) == "informational"
    assert severity_from_score(4) == "low"
    assert severity_from_score(8) == "medium"
    assert severity_from_score(15) == "high"
    assert severity_from_score(20) == "critical"


def test_build_finding():
    finding = build_finding("F-001", "Example", 4, 4)
    assert finding.severity == "high"


def test_invalid_risk_inputs():
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
    finding = build_finding("F-1", "Test", 4, 5, "evidence", "recommendation")
    assert finding.likelihood == 4
    assert finding.impact == 5
    assert finding.severity == "critical"
