from __future__ import annotations

from typing import Any

from assessment.hearing_aid import analyze_assessment
from assessment.risk import assess_risk, summarize_findings


def render_report(assessment: dict[str, Any]) -> str:
    analysis = analyze_assessment(assessment)
    lines = [
        "# HearSec Security & Privacy Assessment Report",
        "",
        "## 1. Assessment scope",
        f"- Assessment ID: {assessment.get('assessment_id', '')}",
        f"- Date: {assessment.get('date', '')}",
    ]

    authorization = assessment.get("authorization", {})
    if isinstance(authorization, dict):
        lines.append(f"- Authorization / scope: {authorization.get('scope', '')}")

    target = assessment.get("target", {})
    if isinstance(target, dict):
        lines.extend([
            f"- Device type: {target.get('device_type', '')}",
            f"- Manufacturer: {target.get('manufacturer', '')}",
            f"- Model: {target.get('model', '')}",
            f"- Serial / research ID: {target.get('serial_number', '')}",
            f"- Firmware: {target.get('firmware', '')}",
            f"- Companion application: {target.get('companion_app', '')}",
            f"- App version: {target.get('app_version', '')}",
            f"- Platform: {target.get('platform', '')}",
            f"- Clinical software: {target.get('clinical_software', '')}",
            f"- Connectivity: {', '.join(target.get('connectivity', [])) if isinstance(target.get('connectivity'), list) else target.get('connectivity', '')}",
        ])

    lines.extend(["", "## 2. Assessment coverage"])
    coverage = analysis["coverage"]
    lines.extend([
        f"- Coverage status: {coverage['coverage_status']}",
        f"- Target fields present: {coverage['target_fields_present']}/{coverage['target_fields_total']}",
        f"- Security domains assessed: {coverage['domains_assessed']}/{coverage['domains_total']}",
        f"- Evidence records: {analysis['counts']['evidence']}",
        f"- Controls documented: {analysis['counts']['controls']}",
        f"- Data flows documented: {analysis['counts']['data_flows']}",
    ])
    if coverage["unassessed_domains"]:
        lines.append("- Unassessed domains: " + ", ".join(coverage["unassessed_domains"]))

    lines.extend(["", "## 3. Data flows"])
    for flow in assessment.get("data_flows", []):
        lines.append(
            f"- {flow.get('source', '')} → {flow.get('destination', '')}: "
            f"{flow.get('data_category', '')}; protection: {flow.get('protection', '')}"
        )

    lines.extend(["", "## 4. Evidence"])
    for evidence in assessment.get("evidence", []):
        lines.append(
            f"- {evidence.get('id', '')}: {evidence.get('type', '')} — "
            f"{evidence.get('description', '')} "
            f"(source: {evidence.get('source', '')})"
        )

    lines.extend(["", "## 5. Controls"])
    for control in assessment.get("controls", []):
        lines.append(
            f"- {control.get('id', '')}: {control.get('category', '')} — "
            f"{control.get('status', '')}; {control.get('description', '')}"
        )

    lines.extend(["", "## 6. Findings"])
    for finding in assessment.get("findings", []):
        risk = finding.get("risk", {})
        calculated = assess_risk(risk.get("likelihood"), risk.get("impact"))
        displayed_level = risk.get("level", "")
        if calculated["score"] is not None:
            displayed_level = calculated["level"]
        else:
            displayed_level = displayed_level or "not_rated"
        lines.extend([
            f"### {finding.get('id', '')} — {finding.get('title', '')}",
            f"- Category: {finding.get('category', '')}",
            f"- Evidence: {finding.get('evidence', '')}",
            f"- Evidence IDs: {', '.join(finding.get('evidence_ids', [])) if isinstance(finding.get('evidence_ids'), list) else finding.get('evidence_ids', '')}",
            f"- Likelihood: {risk.get('likelihood', '')}",
            f"- Impact: {risk.get('impact', '')}",
            f"- Risk score: {calculated['score'] if calculated['score'] is not None else 'Not calculated'}",
            f"- Risk level: {displayed_level}",
            f"- Recommendation: {finding.get('recommendation', '')}",
            "",
        ])

    summary = summarize_findings(assessment.get("findings", []))
    lines.extend([
        "## 7. Risk summary",
        f"- Total findings: {summary['total']}",
        f"- Rated findings: {summary['rated']}",
        f"- Not rated: {summary['not_rated']}",
        "",
        "## 8. Limitations",
        "This report reflects only documented evidence within the assessment scope. "
        "Unknown or unassessed information is not treated as a vulnerability. "
        "It does not imply exploitation, penetration testing, vendor confirmation, "
        "or clinical validation unless separately documented.",
    ])
    return "\n".join(lines)
