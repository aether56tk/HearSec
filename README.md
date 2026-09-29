# HearSec

**HearSec is a defensive security and privacy assessment framework for connected hearing technology.**

## Complete software workflow

HearSec now provides:

- Target/system assessment data model
- Authorization/scope documentation
- Asset and threat catalogs
- Control framework
- Risk scoring
- Structured assessment validation
- Evidence/findings model
- Markdown report generation
- Example synthetic assessment
- Automated tests and CI
- Research methodology and validation documentation
- Web UI prototype

Run the synthetic assessment report:

    python -m assessment assessment/example_assessment.json

## Safety boundary

HearSec is for **authorized defensive research and documentation**. It is not an exploitation toolkit. Do not test devices, accounts, networks or services without explicit authorization.

## Validation status

The software workflow is implemented. **Empirical security assessment of real hearing technology remains pending** and must be performed only with explicit authorization and appropriate research/data-governance controls.

Software tests validate HearSec's own logic; they do not prove the security of a third-party hearing device or companion application.

## Privacy

Use synthetic or de-identified data during development. Never commit credentials, patient information, private communications or sensitive vendor vulnerability details.

## License

MIT
