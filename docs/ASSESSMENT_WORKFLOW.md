# HearSec Assessment Workflow

## 1. Define scope

Record:

- target device/system
- companion application
- firmware/app versions
- assessment date
- authorised scope
- assessor or approving authority

Use synthetic identifiers where possible.

## 2. Map the ecosystem

Document relevant flows such as:

```
Hearing aid <-> Smartphone <-> Cloud
        |
        +---- Audiologist / clinical software
```

Record the data category and protection mechanism for each flow.

## 3. Identify threats

Use the threat catalogue as a starting point. Do not treat a catalogue entry as proof that a vulnerability exists.

## 4. Collect evidence

Evidence should be:

- reproducible
- scoped
- attributable to the assessed system
- free of unnecessary patient information
- clearly separated from assumptions

## 5. Rate risk

Use a 1–5 likelihood and 1–5 impact scale when the evidence supports a rating.

```
Risk score = likelihood × impact
```

If either value is unknown, HearSec reports **not_rated** instead of inventing a score.

## 6. Apply controls

Map findings to relevant controls such as:

- authentication and authorisation
- secure configuration
- data protection
- privacy
- secure communication
- vulnerability/update management
- incident response
- secure development

## 7. Report limitations

Every assessment should distinguish:

- observed evidence
- inferred risk
- untested areas
- vendor-confirmed information
- synthetic demonstration data

## 8. Validate the software

Run:

```bash
PYTHONPATH=. pytest -q
python -m assessment assessment/example_assessment.json
```

Passing tests demonstrate that HearSec's own software behaves as expected; they do not establish the security of a real hearing aid or vendor system.
