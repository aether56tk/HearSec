from assessment.hearing_aid import analyze_assessment, completeness_report


def test_completeness_does_not_call_unknown_insecure():
    assessment = {
        "target": {
            "device_type": "Connected hearing aid",
            "manufacturer": "Example",
            "model": "Model-X",
            "firmware": "Unknown",
            "companion_app": "Example App",
            "app_version": "1.0",
            "platform": "Android",
        },
        "security_domains": {
            "connectivity": {"status": "assessed", "evidence_ids": ["E1"]},
            "privacy": {"status": "not_assessed", "evidence_ids": []},
        },
        "evidence": [{"id": "E1", "type": "laboratory_observation", "description": "Synthetic"}],
    }
    report = completeness_report(assessment)
    assert report["coverage_status"] == "partial"
    assert "firmware" in report["missing_target_fields"]


def test_analysis_counts_and_risk_distribution():
    assessment = {
        "assessment_id": "HS-TEST-001",
        "target": {"device_type": "Connected hearing aid"},
        "evidence": [{"id": "E1", "type": "laboratory_observation", "description": "Synthetic"}],
        "controls": [{"id": "C1", "category": "pairing", "status": "documented"}],
        "data_flows": [{"source": "Hearing Aid", "destination": "Phone"}],
        "findings": [
            {
                "id": "F1",
                "category": "Authentication",
                "title": "Synthetic rated finding",
                "evidence": "E1",
                "risk": {"likelihood": 4, "impact": 4},
            },
            {
                "id": "F2",
                "category": "Privacy",
                "title": "Synthetic unknown finding",
                "evidence": "E1",
                "risk": {"likelihood": "Unknown", "impact": "Unknown"},
            },
        ],
    }
    result = analyze_assessment(assessment)
    assert result["counts"]["findings"] == 2
    assert result["counts"]["rated_findings"] == 1
    assert result["counts"]["not_rated_findings"] == 1
    assert result["risk_distribution"]["high"] == 1
