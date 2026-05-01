# ONDE_PHASED_ARRAY_SETUP

```{mermaid}
classDiagram
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_ANGLE
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_COMPOUND
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_ESCAN
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_FMC
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_PWI
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_SSCAN
  click ONDE_PHASED_ARRAY_COMPOUND href "onde_phased_array_compound.html"
  click ONDE_PHASED_ARRAY_SETUP href "onde_phased_array_setup.html"
  click ONDE_PHASED_ARRAY_SSCAN href "onde_phased_array_sscan.html"
  click ONDE_PHASED_ARRAY_ANGLE href "onde_phased_array_angle.html"
  click ONDE_PHASED_ARRAY_PWI href "onde_phased_array_pwi.html"
  click ONDE_PHASED_ARRAY_ESCAN href "onde_phased_array_escan.html"
  click ONDE_PHASED_ARRAY_FMC href "onde_phased_array_fmc.html"
```

The phased array setup block describes the high-level electronic configuration for Phased Array ultrasonic testing. This optional group has no vocation to be exhaustive in terms of electronic configurations (unlike the law block that permits any description and is fully generic). However, it is intended to cover most of the situations that are common in industrial controls and represent a large share of the acquisition files produced in the industry. In this version of the specification, it encompasses only the most basic setups.

The specific sequencing (Angle, SScan, EScan, Compound, FMC, PWI) is defined by subclasses of this block. The propagation mode used for the settings is given in SEQUENCE_ANGLE_MODE.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_phased_array_setup-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `` | `["ONDE_PHASED_ARRAY_SETUP"]` |  |
| [**`EMITTER_PROBE`**](#onde_phased_array_setup-emitter_probe)<br><sub>`ONDE_PHASED_ARRAY_SETUP:EMITTER_PROBE`</sub> | Mandatory | attribute | H5T_STD_REF_OBJ | `1` | `` |  |
| [**`RECEIVING_PROBE`**](#onde_phased_array_setup-receiving_probe)<br><sub>`ONDE_PHASED_ARRAY_SETUP:RECEIVING_PROBE`</sub> | Mandatory | attribute | H5T_STD_REF_OBJ | `1` | `` |  |
| [**`SEQUENCE_ANGLE_MODE`**](#onde_phased_array_setup-sequence_angle_mode)<br><sub>`ONDE_PHASED_ARRAY_SETUP:SEQUENCE_ANGLE_MODE`</sub> | Mandatory | attribute | H5T_INTEGER | `` | `"L"\|"T"` |  |


## Field Details

(onde_phased_array_setup-type)=
### `TYPE`

*No detailed description provided.*

(onde_phased_array_setup-emitter_probe)=
### `EMITTER_PROBE`

*No detailed description provided.*

(onde_phased_array_setup-receiving_probe)=
### `RECEIVING_PROBE`

*No detailed description provided.*

(onde_phased_array_setup-sequence_angle_mode)=
### `SEQUENCE_ANGLE_MODE`

*No detailed description provided.*
