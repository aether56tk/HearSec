# HearSec DSP & Hearing-Aid Connectivity Architecture

HearSec uses a manufacturer-agnostic architecture rather than assuming that every hearing aid exposes the same interface.

## Supported assessment paths

1. **Bluetooth LE Audio / Hearing Access Profile (HAP)** — standard connectivity path where the device and host expose the relevant profiles.
2. **Android ASHA** — Android hearing-aid streaming path for compatible devices.
3. **Apple MFi Hearing Aids** — Apple ecosystem path requiring the applicable manufacturer/platform authorization.
4. **Manufacturer SDK/API** — preferred route when a vendor provides an authorized integration interface.
5. **Manufacturer app export** — analyze exported device metadata/configuration supplied by an authorized app.
6. **Clinical fitting software export** — analyze authorized fitting/configuration exports.
7. **Audio/DSP file import** — analyze recordings or exported DSP measurements without connecting directly to the physical device.

## Important limitation

There is no single public universal API that exposes the internal DSP parameters of every hearing-aid manufacturer and model. Proprietary fitting protocols, vendor SDKs, platform frameworks, and device generations differ.

Therefore HearSec separates:

- **Connectivity identification**
- **Device identity**
- **DSP/audio evidence**
- **Security controls**
- **Vendor-specific integration**

A device should only be connected or queried through an interface that the researcher is authorized to use.

## DSP evidence model

Where authorized data are available, HearSec can record:

- input/output audio samples
- sampling rate and channel count
- codec/transport information
- latency measurements
- gain/program configuration when exposed
- compression/processing observations
- directional/noise-reduction observations when measurable
- firmware and configuration metadata
- security-relevant communication observations

HearSec should not infer hidden proprietary DSP parameters from a serial number alone.
