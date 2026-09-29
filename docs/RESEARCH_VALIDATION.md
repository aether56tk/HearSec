# HearSec Research Validation Protocol

## Purpose
Validate data integrity, reproducibility, measurement quality, and workflow consistency before using HearSec outputs in research.

## Minimum workflow
1. Create or identify a device record.
2. Record UDI/model/serial evidence and its source.
3. Record protocol version and pseudonymous operator ID.
4. Generate the controlled stimulus when applicable.
5. Capture reference and processed recordings.
6. Run alignment and DSP comparison.
7. Run the Quality Gate.
8. Preserve the exported JSON and source evidence.
9. Repeat trials when assessing reproducibility.
10. Document exclusions and limitations.

## Quality principles
- Do not infer manufacturer from a serial-number pattern alone.
- Do not treat MAUDE counts as incidence or causation.
- Do not treat recording-level DSP measurements as clinical real-ear measurements.
- Do not treat company-level sales as model-level sales.
- Use de-identified research identifiers.
- Preserve protocol version and timestamps.

## Suggested validation study
Use multiple known devices and repeated trials. Report measurement repeatability, task completion, missing-data rate, false-match rate, and inter-rater agreement where applicable.
