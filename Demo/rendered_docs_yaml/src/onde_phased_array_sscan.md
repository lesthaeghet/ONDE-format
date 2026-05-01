# ONDE_PHASED_ARRAY_SSCAN

**Inherits from:** ONDE_PHASED_ARRAY_SETUP

```{mermaid}
classDiagram
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_SSCAN
  click ONDE_PHASED_ARRAY_SETUP href "onde_phased_array_setup.html"
  click ONDE_PHASED_ARRAY_SSCAN href "onde_phased_array_sscan.html"
```

In this configuration, the probe is configured to emit/receive at a set of angles. The angles are linearly varying, therefore the first and last angles and the number of shots define the set of angles.
![SScan configuration](../images/media/figure25.png "Figure 25")

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_phased_array_sscan-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[2]` | `["ONDE_PHASED_ARRAY_SETUP","ONDE_PHASED_ARRAY_SSCAN"]` |  |
| [**`STARTING_ANGLE`**](#onde_phased_array_sscan-starting_angle)<br><sub>`ONDE_PHASED_ARRAY_SSCAN:STARTING_ANGLE`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`FINISHING_ANGLE`**](#onde_phased_array_sscan-finishing_angle)<br><sub>`ONDE_PHASED_ARRAY_SSCAN:FINISHING_ANGLE`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`NUMBER_OF_ANGLES`**](#onde_phased_array_sscan-number_of_angles)<br><sub>`ONDE_PHASED_ARRAY_SSCAN:NUMBER_OF_ANGLES`</sub> | Mandatory | attribute | H5T_INTEGER | `1` | `` |  |


## Field Details

(onde_phased_array_sscan-type)=
### `TYPE`

*No detailed description provided.*

(onde_phased_array_sscan-starting_angle)=
### `STARTING_ANGLE`

*No detailed description provided.*

(onde_phased_array_sscan-finishing_angle)=
### `FINISHING_ANGLE`

*No detailed description provided.*

(onde_phased_array_sscan-number_of_angles)=
### `NUMBER_OF_ANGLES`

*No detailed description provided.*
