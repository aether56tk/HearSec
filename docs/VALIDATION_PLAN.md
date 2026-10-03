# HearSec Validation Plan

Validation starts only after the implementation build is frozen.

## Phase 1 — Software validation

- Run the complete automated test suite.
- Test schema handling.
- Test risk calculations and unknown handling.
- Test evidence provenance.
- Test AI safety guardrails.
- Test report generation.
- Test browser import/export workflow.

## Phase 2 — Synthetic assessment validation

Create controlled synthetic assessments containing:
- complete evidence;
- partial evidence;
- unknown evidence;
- rated findings;
- not-rated findings;
- multiple domains;
- AI-supported and AI-rejected records.

Verify deterministic outputs against expected results.

## Phase 3 — Expert framework validation

Independent experts review:
- domain relevance;
- terminology;
- evidence requirements;
- clinical interpretability;
- workflow usability.

Use a prespecified agreement method appropriate to the study design.

## Phase 4 — Authorized device assessment

Apply the same HearSec protocol to authorized devices and associated software.
Record scope, authorization, device identity, firmware/app versions, evidence
provenance, and limitations.

No unsupported security conclusion should be produced from missing evidence.

## Phase 5 — AI evaluation

Compare AI outputs with expert reference labels and record:
- agreement;
- evidence grounding;
- unsupported claims;
- hallucinations;
- omissions;
- correction rate;
- assessment time.

## Phase 6 — Inter-rater reliability

Independent assessors apply the frozen protocol to the same evidence dossiers.
Select Cohen's kappa, Fleiss' kappa, ICC, or another statistic according to
the variable and number of raters.

No target value should be treated as achieved until measured.
