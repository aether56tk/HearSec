# HearSec

**Defensive security, privacy and evidence-assessment framework for connected hearing technology.**

HearSec is a browser + Python research platform for documenting and assessing the security and privacy posture of connected hearing ecosystems. It connects **hearing-aid/device metadata, authorised browser Bluetooth observations, threat modelling, evidence, controls, transparent risk assessment, validation and reporting** into one workflow.

> **Important:** HearSec is an assessment and evidence platform — not an exploitation toolkit. An observed device, Bluetooth service or missing control is **not automatically a vulnerability**.

## 🛡️ What HearSec does

HearSec is designed around the real ecosystem surrounding modern hearing technology:

```text
                         ┌──────────────────┐
                         │ Clinical / Fitting│
                         │     Software      │
                         └─────────┬────────┘
                                   │
┌──────────────┐          ┌────────▼────────┐          ┌──────────────┐
│ Hearing Aid  │◄────────►│ Smartphone /    │◄────────►│ Cloud /      │
│ / Device     │          │ Companion App   │          │ Services     │
└──────┬───────┘          └─────────────────┘          └──────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────────┐
│ HearSec: identity → connection evidence → threats → controls │
│          → risk → findings → validation → report             │
└──────────────────────────────────────────────────────────────┘
```

## ⚡ Current platform capabilities

### 1. Security assessment engine
- Structured assessment schema
- Asset and threat modelling
- Security/privacy control assessment
- Evidence and finding records
- Transparent **likelihood × impact** risk calculation
- 1–5 numeric or labelled risk inputs
- Explicit `not_rated` handling when risk information is unknown
- Automated assessment validation
- Machine-readable assessment/report data

### 2. Live browser hearing-aid connection
The browser UI can establish an **authorised Web Bluetooth connection** where the browser, operating system and device expose compatible functionality.

Current flow:

```text
Connect device
    ↓
User-approved Bluetooth selection
    ↓
GATT connection
    ↓
Primary-service discovery
    ↓
Observed device/service evidence
    ↓
Live assessment bridge
    ↓
Threat / Control / Risk / Finding workflow
```

The connection layer:
- Shows connection state
- Detects disconnects
- Discovers exposed primary GATT services
- Records observed service metadata
- Feeds live observations into the assessment workflow
- Keeps evidence provenance separate from assumptions

**Browser limitation:** Web Bluetooth cannot silently pair with devices or bypass operating-system/device authentication. Commercial hearing aids may expose proprietary interfaces that are unavailable to generic browser applications.

### 3. Live Security Dashboard
The dashboard provides a current assessment overview:

- Assets
- Threats
- Controls
- Findings
- Rated risk
- Not-rated items
- Metadata completeness
- Evidence posture
- Authorisation/scope status
- Risk breakdown
- Last refresh

### 4. Linked Security Assessment Workflow

```text
ASSET
  ↓
THREAT
  ↓
EVIDENCE
  ↓
CONTROL
  ↓
RISK
  ↓
FINDING
  ↓
REPORT
```

The browser workflow can synchronise the existing HearSec assessment state into a single assessment snapshot and generate downloadable JSON.

### 5. Evidence-first research tooling
HearSec supports evidence from:
- Device identity records
- Device-management records
- Regulatory/public-source research
- Safety intelligence
- DSP/audio measurements
- Reference-vs-processed recordings
- Test-session metadata
- Browser-observed Bluetooth/GATT information

Evidence is treated as **observed, documented information with provenance**, rather than proof of a security weakness.

### 6. DSP / audio research
The browser UI includes authorised research utilities for:
- Controlled test-tone generation
- WAV analysis
- Reference-vs-processed comparison
- Recording-level measurements
- DSP test-session metadata
- Quality-gate checks

These measurements describe the tested recording/session. They do not expose proprietary internal DSP algorithms.

### 7. Device research & lifecycle workspace
The platform includes browser-local tooling for:
- Device identity
- Serial/UDI metadata
- Manufacturer information
- Regulatory information
- Safety/recall research
- Device history
- Evidence confidence
- Privacy/de-identification mode
- Dataset export
- Device comparison
- Research reports
- Audit logging

## 🧪 Validation

Run the synthetic assessment:

```bash
python -m assessment assessment/example_assessment.json
```

Run the automated tests:

```bash
PYTHONPATH=. pytest -q
```

The repository also contains GitHub Actions CI for the Python validation suite.

### What the tests prove

Software tests validate **HearSec's own implementation**, including assessment/risk logic and workflow behaviour.

They do **not** prove that:
- a commercial hearing aid is secure;
- a manufacturer application is secure;
- a Bluetooth implementation has no vulnerabilities;
- a cloud service is secure.

Real-device findings require separate authorised research and evidence.

## 🔬 Research methodology

A typical authorised assessment follows:

```text
1. Define scope + authorization
             ↓
2. Identify device / software / data flows
             ↓
3. Record observable evidence
             ↓
4. Model threats
             ↓
5. Map existing controls
             ↓
6. Rate documented risks
             ↓
7. Record findings + limitations
             ↓
8. Validate the HearSec record
             ↓
9. Generate reproducible report
```

Unknown information remains unknown. HearSec does not manufacture evidence to fill gaps.

## 🔐 Safety boundary

HearSec is intended for **authorized defensive security and privacy research**.

Do not use it to:
- bypass authentication or pairing;
- intercept communications without authorization;
- collect credentials;
- access another person's patient/device data;
- establish persistence;
- extract protected information;
- test third-party systems outside an approved scope.

The browser connection functionality requires explicit user interaction and follows normal browser Bluetooth security boundaries.

For real-device research, define:
- written authorization;
- target devices/accounts;
- permitted techniques;
- data-handling requirements;
- testing window;
- responsible-disclosure process;
- rollback/stop conditions.

## 🔒 Privacy & data handling

Development should use synthetic or de-identified information whenever possible.

Do not commit:
- patient identifiers;
- credentials/tokens;
- private communications;
- clinical records;
- sensitive unpublished vulnerability details.

The browser UI is designed to keep many research operations local to the browser. Local processing does not automatically make sensitive data safe; researchers remain responsible for appropriate data governance.

## 📁 Repository structure

```text
HearSec/
├── assessment/             # Assessment schema, risk logic and examples
├── docs/                   # Architecture, methodology and workflows
├── reports/                # Report generation
├── tests/                  # Automated software tests
├── ui/                     # Browser-based assessment workspace
├── SECURITY.md             # Security/research boundary
└── VALIDATION_STATUS.md    # Current validation status
```

## 📚 Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Assessment workflow](docs/ASSESSMENT_WORKFLOW.md)
- [Methodology](docs/METHODOLOGY.md)
- [Research validation](docs/RESEARCH_VALIDATION.md)
- [Validation status](VALIDATION_STATUS.md)
- [Security policy](SECURITY.md)

## 🚀 Quick start

### Python assessment

```bash
git clone <your-authorized-copy-of-the-repository>
cd HearSec

python -m assessment assessment/example_assessment.json
PYTHONPATH=. pytest -q
```

### Browser UI

Open:

```text
ui/index.html
```

For Web Bluetooth, use a compatible browser/environment and a secure context as required by the browser. The user must explicitly choose the device from the Bluetooth prompt.

## 📌 Project status

**Current focus:** turning HearSec into a reproducible hearing-technology security research platform.

Implemented areas include:
- assessment/risk engine;
- structured threat/control workflow;
- browser assessment dashboard;
- live authorised Bluetooth/GATT observation;
- live connection monitoring;
- evidence-to-assessment bridge;
- DSP/audio research utilities;
- device research and lifecycle workspace;
- validation and quality gates;
- local reports and JSON exports.

**Important distinction:** platform capability is not the same as validated security of a third-party product. Real-world security conclusions require authorised testing, suitable evidence and reproducible documentation.

## License

MIT
