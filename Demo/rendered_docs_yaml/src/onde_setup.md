# ONDE_SETUP

```{mermaid}
classDiagram
  ONDE_SETUP o-- ONDE_ULTRASONIC_SETUP : ONDE_SETUP:ULTRASONIC_SETUP
  ONDE_SETUP o-- ONDE_PHASED_ARRAY_SETUP : ONDE_SETUP:PHASED_ARRAY_SETUP
  ONDE_SETUP o-- ONDE_GEOMETRIC_SETUP : ONDE_SETUP:GEOMETRIC_SETUP
  click ONDE_PHASED_ARRAY_SETUP href "onde_phased_array_setup.html"
  click ONDE_GEOMETRIC_SETUP href "onde_geometric_setup.html"
  click ONDE_SETUP href "onde_setup.html"
  click ONDE_ULTRASONIC_SETUP href "onde_ultrasonic_setup.html"
```


### Setup

**Setup**

This group contains references to the geometric setup and ultrasonic setup. The reference to the ultrasonic setup is
compulsory for the A-scan data. For TScans, it is allowed to bypass this ultrasonic setup and have a direct reference to
the phased array setup (in order to store the reconstruction information without storing the information related to the
acquisition).

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_setup-type)<br><sub>`ONDE_SETUP:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `` | `["ONDE_SETUP"]` |  |
| [**`ULTRASONIC_SETUP`**](#onde_setup-ultrasonic_setup)<br><sub>`ONDE_SETUP:ULTRASONIC_SETUP`</sub> | Optional | attribute | H5T_STD_REF_OBJ<[ONDE_ULTRASONIC_SETUP](onde_ultrasonic_setup.md)> | `[1]` | `` | Mandatory for Ascan sequences |
| [**`PHASED_ARRAY_SETUP`**](#onde_setup-phased_array_setup)<br><sub>`ONDE_SETUP:PHASED_ARRAY_SETUP`</sub> | Optional | attribute | H5T_STD_REF_OBJ<[ONDE_PHASED_ARRAY_SETUP](onde_phased_array_setup.md)> | `[1]` | `` |  |
| [**`GEOMETRIC_SETUP`**](#onde_setup-geometric_setup)<br><sub>`ONDE_SETUP:GEOMETRIC_SETUP`</sub> | Mandatory | attribute | H5T_STD_REF_OBJ<[ONDE_GEOMETRIC_SETUP](onde_geometric_setup.md)> | `[1]` | `` |  |


## Field Details

(onde_setup-type)=
### `TYPE`

*No detailed description provided.*

(onde_setup-ultrasonic_setup)=
### `ULTRASONIC_SETUP`

Mandatory for Ascan sequences

(onde_setup-phased_array_setup)=
### `PHASED_ARRAY_SETUP`

*No detailed description provided.*

(onde_setup-geometric_setup)=
### `GEOMETRIC_SETUP`

*No detailed description provided.*
