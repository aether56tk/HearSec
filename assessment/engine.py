from dataclasses import dataclass


@dataclass
class Finding:
    finding_id: str
    title: str
    severity: str
    likelihood: int
    impact: int
    evidence: str = ""
    recommendation: str = ""


def calculate_risk(likelihood: int, impact: int) -> int:
    if not 1 <= likelihood <= 5 or not 1 <= impact <= 5:
        raise ValueError("likelihood and impact must be between 1 and 5")
    return likelihood * impact


def severity_from_score(score: int) -> str:
    if score >= 20:
        return "critical"
    if score >= 15:
        return "high"
    if score >= 8:
        return "medium"
    if score >= 4:
        return "low"
    return "informational"


def build_finding(
    finding_id: str,
    title: str,
    likelihood: int,
    impact: int,
    evidence: str = "",
    recommendation: str = "",
) -> Finding:
    score = calculate_risk(likelihood, impact)
    return Finding(
        finding_id,
        title,
        severity_from_score(score),
        likelihood,
        impact,
        evidence,
        recommendation,
    )
