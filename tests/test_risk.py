import pytest

from assessment.risk import assess_risk, summarize_findings


def test_numeric_risk():
    result = assess_risk(4, 5)
    assert result["score"] == 20
    assert result["level"] == "critical"


def test_label_risk():
    result = assess_risk("likely", "major")
    assert result["likelihood_score"] == 4
    assert result["impact_score"] == 4
    assert result["score"] == 16
    assert result["level"] == "high"


def test_unknown_risk_is_not_rated():
    result = assess_risk("Unknown", "Low")
    assert result["score"] is None
    assert result["level"] == "not_rated"


def test_invalid_risk_value():
    with pytest.raises(ValueError):
        assess_risk(6, 3)


def test_summary():
    findings = [
        {"risk": {"likelihood": 5, "impact": 5}},
        {"risk": {"likelihood": "likely", "impact": "major"}},
        {"risk": {"likelihood": "Unknown", "impact": "Low"}},
    ]
    summary = summarize_findings(findings)
    assert summary["total"] == 3
    assert summary["rated"] == 2
    assert summary["not_rated"] == 1
    assert summary["by_level"]["critical"] == 1
    assert summary["by_level"]["high"] == 1
