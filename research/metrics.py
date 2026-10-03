"""Validation metrics used by HearSec research studies."""

from __future__ import annotations

from typing import Iterable


def binary_rates(
    truth: Iterable[bool],
    predicted: Iterable[bool],
) -> dict[str, float]:
    """Calculate simple binary classification rates."""
    pairs = list(zip(truth, predicted))
    tp = sum(t and p for t, p in pairs)
    tn = sum((not t) and (not p) for t, p in pairs)
    fp = sum((not t) and p for t, p in pairs)
    fn = sum(t and (not p) for t, p in pairs)

    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    fpr = fp / (fp + tn) if fp + tn else 0.0
    fnr = fn / (fn + tp) if fn + tp else 0.0

    return {
        "true_positive": tp,
        "true_negative": tn,
        "false_positive": fp,
        "false_negative": fn,
        "precision": precision,
        "recall": recall,
        "false_positive_rate": fpr,
        "false_negative_rate": fnr,
    }


def agreement_rate(ai_statuses: Iterable[str], expert_statuses: Iterable[str]) -> float:
    ai = list(ai_statuses)
    expert = list(expert_statuses)
    if len(ai) != len(expert) or not ai:
        return 0.0
    return sum(
        str(a).strip().casefold() == str(e).strip().casefold()
        for a, e in zip(ai, expert)
    ) / len(ai)


def evidence_grounding_score(total_claims: int, grounded_claims: int) -> float:
    if total_claims <= 0:
        return 0.0
    return max(0.0, min(1.0, grounded_claims / total_claims))


def hallucination_index(total_claims: int, unsupported_claims: int) -> float:
    if total_claims <= 0:
        return 0.0
    return max(0.0, min(1.0, unsupported_claims / total_claims))
