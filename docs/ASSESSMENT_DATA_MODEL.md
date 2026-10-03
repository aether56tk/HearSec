# HearSec Assessment Data Model

## Core object

Each assessment contains:

1. assessment_id
2. date
3. authorization
4. target
5. security_domains
6. data_flows
7. evidence
8. controls
9. findings
10. assessment_notes
11. ai_assessments
12. optional clinical translations and evidence summaries

## Evidence chain

source
  ↓
evidence record
  ↓
domain mapping
  ↓
control / finding
  ↓
risk calculation
  ↓
AI interpretation (optional)
  ↓
human verification
  ↓
report

Every substantive finding should be traceable to one or more evidence IDs.

## Status semantics

unknown, not_verified, and not_assessed represent information gaps.
They do not mean insecure.

AI may propose an interpretation, but the final assessment status remains
human-verifiable and auditable.

## Risk semantics

HearSec calculates risk only when valid likelihood and impact values are
available. Otherwise the result remains not_rated.

Risk is an assessment output, not a probability of compromise.
