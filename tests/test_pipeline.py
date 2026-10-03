from assessment.pipeline import build_assessment_snapshot


def test_pipeline_snapshot_contains_framework_coverage_and_risk():
    assessment = {
        "assessment_id": "HS-TEST-PIPELINE",
        "target": {"device_type": "Connected hearing aid"},
        "security_domains": {
            "device_identity": {"status": "assessed"},
            "privacy": {"status": "partial"},
        },
        "evidence": [
            {"id": "E1", "status": "documented", "type": "manufacturer_documentation",
             "description": "Synthetic documentation"}
        ],
        "findings": [
            {"id": "F1", "category": "privacy", "title": "Synthetic",
             "evidence": "E1", "risk": {"likelihood": 3, "impact": 3}}
        ],
    }
    result = build_assessment_snapshot(assessment)
    assert result["framework"]["name"] == "HearSec"
    assert result["coverage"]["assessed"] == 2
    assert result["evidence"]["total"] == 1
    assert result["risk"]["rated"] == 1
