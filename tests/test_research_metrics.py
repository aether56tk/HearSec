from research.metrics import (
    agreement_rate,
    binary_rates,
    evidence_grounding_score,
    hallucination_index,
)


def test_binary_rates():
    result = binary_rates(
        [True, True, False, False],
        [True, False, False, True],
    )
    assert result["true_positive"] == 1
    assert result["false_positive"] == 1
    assert result["false_negative"] == 1


def test_agreement_rate():
    assert agreement_rate(["a", "b", "a"], ["a", "b", "c"]) == 2 / 3


def test_grounding_and_hallucination_metrics():
    assert evidence_grounding_score(100, 95) == 0.95
    assert hallucination_index(100, 2) == 0.02
