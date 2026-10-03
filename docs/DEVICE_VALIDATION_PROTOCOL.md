# HearSec Authorized Device Validation Protocol

## Purpose
Evaluate the framework against a real connected hearing technology environment only when explicit authorization and scope are documented.

## Required authorization
Before testing, document:
- owner/vendor authorization
- permitted devices and accounts
- permitted firmware/app versions
- test dates
- network/environment boundaries
- prohibited actions
- evidence-handling rules

## Assessment record
For each observation retain:
- test identifier
- component/data-flow location
- expected security control
- observed behavior
- evidence reference
- reproducibility steps
- impact/risk rationale
- remediation or disclosure status

Do not store credentials, personal data, or sensitive vendor material in the public repository.

## Reproducibility
Freeze and record:
- HearSec commit SHA
- device/app/firmware versions
- mobile OS version
- test environment
- assessment configuration
- evidence identifiers

## Evidence chain
Separate:
1. documented expectation
2. observed evidence
3. analyst interpretation
4. risk rating

Do not infer a vulnerability from a missing public document alone.

## Reporting
Produce a versioned report containing scope, methodology, observations, limitations, evidence references, and responsible-disclosure handling.

Synthetic examples and unit tests must remain clearly separated from real-device findings.
