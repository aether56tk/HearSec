# HearSec Assessment Checklist

A compact, repeatable checklist for conducting an authorized HearSec assessment.

## 1. Scope and authorization
- [ ] Confirm the device, companion app, fitting software, and cloud components in scope.
- [ ] Confirm explicit authorization for all observations and testing.
- [ ] Record assessment date, assessor, device/app versions, and environment.
- [ ] Do not treat an observation alone as a confirmed vulnerability.

## 2. Asset and data-flow inventory
- [ ] Identify the hearing device and relevant interfaces.
- [ ] Identify the smartphone/companion application.
- [ ] Identify fitting/clinical software where applicable.
- [ ] Identify cloud or backend services that handle device or patient-related data.
- [ ] Record trust boundaries and important data flows.

## 3. Evidence collection
- [ ] Record each observation with a clear source/provenance.
- [ ] Separate observed facts from assumptions or interpretations.
- [ ] Capture relevant service, permission, configuration, or workflow evidence.
- [ ] Mark unavailable or unknown information explicitly rather than guessing.

## 4. Control assessment
- [ ] Authentication and identity controls assessed.
- [ ] Authorization/access-control boundaries assessed.
- [ ] Bluetooth/BLE exposure assessed within the authorized scope.
- [ ] Application permissions and sensitive-data handling assessed.
- [ ] Local data storage and logging assessed.
- [ ] Cloud/API security and privacy controls assessed where applicable.

## 5. Risk and findings
- [ ] Map each finding to supporting evidence.
- [ ] Assess likelihood and impact using the project's defined scale.
- [ ] Use the `not_rated` state when evidence is insufficient for a defensible rating.
- [ ] Record rationale for each risk decision.
- [ ] Distinguish confirmed findings from observations requiring further validation.

## 6. Validation and reporting
- [ ] Run the assessment validator before reporting.
- [ ] Check that evidence, findings, controls, and risk values are internally consistent.
- [ ] Record limitations and unknowns.
- [ ] Generate the report from the structured assessment data.
- [ ] Preserve enough provenance for another assessor to reproduce the reasoning.

## Assessment principle

> Evidence first, interpretation second, risk decision third.

HearSec is an assessment framework for authorized research and medical-device security evaluation; this checklist is not a guide for unauthorized exploitation.