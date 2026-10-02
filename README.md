# HearSec

**HearSec is a defensive security and privacy assessment framework for connected hearing technology.**

HearSec maps the hearing aid–smartphone–cloud ecosystem and turns documented observations into structured threats, controls, transparent risk calculations, evidence and reports.

## Workflow

```
Scope & authorization
        ↓
System / data-flow model
        ↓
Threat catalogue
        ↓
Evidence & findings
        ↓
Risk assessment
        ↓
Controls
        ↓
Validation
        ↓
Report / dashboard
```

## Current capabilities

- Target/system assessment data model
- Authorization and scope documentation
- Hearing-technology asset and threat catalogues
- Control framework
- Transparent 1–5 likelihood × impact risk scoring
- Explicit **not_rated** handling for unknown risk inputs
- Structured assessment validation
- Evidence/findings model
- Markdown report generation
- Example synthetic assessment
- Automated tests and CI
- Research methodology and validation documentation
- Web UI prototype
- Architecture and repeatable assessment workflow documentation

Run the synthetic assessment report:

```bash
python -m assessment assessment/example_assessment.json
```

Run tests:

```bash
PYTHONPATH=. pytest -q
```

## Hearing-technology scope

HearSec is designed around connected hearing ecosystems including:

```
Hearing Aid ↔ Smartphone / Companion App ↔ Cloud
                 ↕
          Clinical software
```

Assessment areas include authentication, authorization, BLE/communication protection, configuration, local storage, privacy, updates, incident response and secure development.

## Safety boundary

HearSec is for **authorized defensive research and documentation**. It is not an exploitation toolkit. Do not test devices, accounts, networks or services without explicit authorization.

HearSec does not perform authentication bypass, unauthorised interception, credential collection, persistence or extraction of patient information.

## Validation status

The software workflow is implemented and tested. **Empirical security assessment of real hearing technology remains a separate research activity** and must only be performed with explicit authorization, defined scope, appropriate research/data-governance controls and responsible-disclosure procedures.

Software tests validate HearSec's own logic; they do not prove the security of a third-party hearing device or companion application.

## Privacy

Use synthetic or de-identified data during development. Never commit credentials, patient information, private communications or sensitive vendor vulnerability details.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Assessment workflow](docs/ASSESSMENT_WORKFLOW.md)
- [Methodology](docs/METHODOLOGY.md)
- [Research validation](docs/RESEARCH_VALIDATION.md)
- [Validation status](VALIDATION_STATUS.md)
- [Security policy](SECURITY.md)

## License

MIT
