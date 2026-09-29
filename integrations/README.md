# HearSec Manufacturer Adapter Architecture

HearSec uses adapters so different hearing-aid ecosystems can feed the same assessment pipeline.

## Adapter interface

Each adapter should expose only data that is available through an authorized interface:

- manufacturer
- model
- serial number
- firmware version
- connectivity path
- app/software version
- exported configuration metadata
- available DSP/audio evidence
- security-relevant observations

## Planned adapters

- generic — manual/exported data
- GN / ReSound ecosystem
- Signia / WS Audiology ecosystem
- Oticon / Demant ecosystem
- Phonak / Sonova ecosystem
- Starkey ecosystem
- Widex / WS Audiology ecosystem
- Beltone / GN ecosystem
- platform adapters for Android/iOS where applicable

## Design rule

Adapters normalize vendor-specific information into the HearSec common schema. They must not bypass pairing, authentication, access controls, licensing restrictions, or other protections.

A vendor adapter should be implemented only when an authorized SDK, API, app export, clinical software export, or documented interface is available.
