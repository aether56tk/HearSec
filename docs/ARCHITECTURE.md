# HearSec Architecture

HearSec is organised as a defensive assessment workflow rather than an exploitation toolkit.

## Data flow

```
Target metadata
      |
      v
Assessment JSON -----> Validator
      |                    |
      |                    v
      |               Structural errors
      v
Threat / control catalogues
      |
      v
Risk engine
      |
      v
Evidence + findings
      |
      v
Markdown report / Web UI
```

## Assessment layers

1. **Scope and authorisation** — records what may be assessed and under what authority.
2. **System model** — represents hearing aid, smartphone, companion application, cloud and data-flow components.
3. **Threat model** — maps assets to plausible security and privacy threats.
4. **Controls** — records expected security controls and evidence sources.
5. **Risk** — calculates likelihood × impact only when both values are known and valid.
6. **Evidence** — preserves observations and their limitations.
7. **Reporting** — produces a reproducible human-readable assessment.
8. **Validation** — tests HearSec's own software independently from claims about third-party devices.

## Safety boundary

HearSec must not perform unauthorised interception, credential collection, authentication bypass, exploitation, persistence or extraction of patient information.

Real-device research requires explicit authorisation, a defined scope, appropriate data governance and responsible-disclosure handling.
