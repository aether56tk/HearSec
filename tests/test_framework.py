from assessment.framework import domain_coverage, framework_metadata
from assessment.evidence import evidence_confidence, summarize_evidence


def test_framework_has_thirteen_domains():
    metadata = framework_metadata()
    assert len(metadata["domains"]) == 13


def test_unknown_evidence_has_zero_confidence():
    assert evidence_confidence("unknown") == 0.0
    assert evidence_confidence("not_verified") == 0.0


def test_domain_coverage_is_not_a_security_score():
    assessment = {
        "security_domains": {
            "device_identity": {"status": "assessed"},
            "connectivity": {"status": "partial"},
        }
    }
    result = domain_coverage(assessment)
    assert result["assessed"] == 2
    assert result["percentage"] > 0


def test_evidence_summary_counts_unknown():
    result = summarize_evidence(
        [
            {"status": "documented"},
            {"status": "unknown"},
            {"status": "not_verified"},
        ]
    )
    assert result["total"] == 3
    assert result["unverified"] == 2
