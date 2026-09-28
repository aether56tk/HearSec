# HearSec

HearSec is a cybersecurity and privacy assessment framework for connected hearing technology.

## Scope

HearSec maps the hearing-aid–smartphone–cloud ecosystem and provides a structured workflow for documenting:

- Device and application inventory
- Bluetooth/BLE communication characteristics
- Authentication and authorization observations
- Mobile application permissions
- Data storage and transmission
- Privacy/data-flow considerations
- Threats, assets, mitigations, and risk
- Assessment evidence and reproducible findings

HearSec is designed for authorized research and controlled assessment. It is not an exploitation toolkit and must not be used against devices, applications, networks, accounts, or services without explicit permission.

## Initial architecture

```
Connected Hearing System
  ├── Hearing Aid
  ├── BLE / Wireless Link
  ├── Smartphone
  ├── Companion App
  ├── Local Storage
  └── Cloud / Clinical Service
             ↓
        HearSec Assessment
             ↓
   Evidence → Finding → Risk
             ↓
          Report
```

## Project status

Early research prototype. The initial release focuses on a transparent, auditable assessment workflow before adding any automated technical collection.

## Planned modules

- assessment/ — assessment data model and logic
- threat_model/ — assets, threats, mitigations, risk
- reports/ — human-readable assessment reports
- ui/ — future web interface
- docs/ — methodology and research documentation
- tests/ — automated tests

## Ethics & safety

Only test equipment and software that you own or are explicitly authorized to assess. Avoid collecting real patient information. Prefer synthetic data during development.

## License

MIT
