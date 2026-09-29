from __future__ import annotations

from typing import Any


def render_report(assessment: dict[str, Any]) -> str:
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
            f"- Target device: {target.get('device_type', '')} {target.get('model', '')}".strip(),
            f"- Companion application: {target.get('companion_app', '')}",
            f"- Platform: {target.get('platform', '')}",
        ])

    lines.extend(["", "## 2. Data flows"])
    for flow in assessment.get("data_flows", []):
        lines.append(
            f"- {flow.get('source', '')} → {flow.get('destination', '')}: "
            f"{flow.get('data_category', '')}"
        )

    lines.extend(["", "## 3. Findings"])
    for finding in assessment.get("findings", []):
        risk = finding.get("risk", {})
        lines.extend([
            f"### {finding.get('id', '')} — {finding.get('title', '')}",
            f"- Category: {finding.get('category', '')}",
            f"- Evidence: {finding.get('evidence', '')}",
            f"- Likelihood: {risk.get('likelihood', '')}",
            f"- Impact: {risk.get('impact', '')}",
            f"- Risk level: {risk.get('level', '')}",
            f"- Recommendation: {finding.get('recommendation', '')}",
            "",
        ])

    lines.extend([
        "## 4. Limitations",
        "This report reflects only documented evidence within the assessment scope. "
        "It does not imply exploitation, penetration testing, vendor confirmation, "
        "or clinical validation unless separately documented.",
    ])
    return "\n".join(lines)
