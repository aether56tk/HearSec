# HearSec AI Evidence Method

## Purpose

The AI layer assists with evidence organization and interpretation. It does not independently establish the cybersecurity status of a third-party hearing aid.

## Evidence chain

Evidence -> AI interpretation -> Human verification -> Final HearSec finding

Every AI output must remain traceable to supplied evidence.

## Allowed evidence states

- documented
- observed
- user_reported
- laboratory_observation
- not_verified
- unknown

## Final assessment states

- confirmed_observation
- supported_finding
- insufficient_evidence
- not_assessed
- not_applicable

## Non-negotiable rule

If evidence is unknown or not_verified, AI cannot promote the record to supported_finding.

The system must instead retain insufficient_evidence until an authorized human review establishes sufficient evidence.

## Human-in-the-loop

AI output contains:

- source evidence ID
- evidence text
- evidence status
- AI interpretation
- proposed status
- source references
- human verification state

The human reviewer records the final decision separately.

## AI evaluation study

For each assessment item:

1. Provide the AI only the evidence available to the authorized assessor.
2. Require source references for every substantive conclusion.
3. Compare AI output with expert consensus.
4. Record corrections.
5. Record unsupported claims.
6. Record whether the AI introduced facts absent from the evidence.

This permits quantitative evaluation rather than treating AI as an unvalidated feature.

## Example

Evidence:

Firmware update security could not be independently verified.

Unsafe AI output:

The device has an insecure firmware update mechanism.

HearSec-safe output:

Firmware update security could not be verified from the available evidence. No vulnerability is established. Status: insufficient_evidence.

## Scope

The AI layer is deliberately separate from device connectivity and testing. It can operate on exported assessment evidence and therefore does not require privileged access to a hearing aid.
