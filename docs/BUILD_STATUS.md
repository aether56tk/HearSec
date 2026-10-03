# HearSec Build Status

## Build target

HearSec is being built as an evidence-grounded, AI-assisted cybersecurity and
privacy assessment platform for connected hearing-aid ecosystems.

## Implemented build components

- Structured hearing-aid assessment schema
- 13-domain assessment framework
- Deterministic likelihood × impact risk engine
- Explicit not-rated handling
- Evidence provenance and completeness helpers
- Evidence-grounded AI assessment records
- Human verification state
- Clinical translation layer
- Research validation metric helpers
- End-to-end assessment snapshot pipeline
- Markdown report generation
- Browser import → analyse → report workflow
- Serial number / de-identified research ID intake
- Automated software test suite and CI configuration

## Research boundary

The build does not establish that a commercial hearing aid is secure or
insecure. Real-device conclusions require authorized testing and evidence.

The build does not require or implement authentication bypass, credential
collection, unauthorized interception, persistence, or exploitation.

## Build versus validation

This document describes implementation scope only. Passing software tests,
once executed, will validate implementation behaviour; it will not validate
the scientific framework or security of third-party hearing aids.

Scientific validation remains a separate research phase involving expert
review, authorized device assessment, AI evaluation, and inter-rater reliability.
