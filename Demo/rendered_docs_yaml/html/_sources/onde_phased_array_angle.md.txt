# ONDE_PHASED_ARRAY_ANGLE

**Inherits from:** ONDE_PHASED_ARRAY_SETUP

```{mermaid}
classDiagram
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_ANGLE
  click ONDE_PHASED_ARRAY_SETUP href "onde_phased_array_setup.html"
  click ONDE_PHASED_ARRAY_ANGLE href "onde_phased_array_angle.html"
```

In this configuration, a single angle is provided for the specification of the ultrasonic ray direction.
![Inspection using a single angle](../images/media/figure24.png "Figure 24")

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_phased_array_angle-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[2]` | `["ONDE_PHASED_ARRAY_SETUP","ONDE_PHASED_ARRAY_ANGLE"]` |  |
| [**`BSCAN_ANGLE`**](#onde_phased_array_angle-bscan_angle)<br><sub>`ONDE_PHASED_ARRAY_ANGLE:BSCAN_ANGLE`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |


## Field Details

(onde_phased_array_angle-type)=
### `TYPE`

*No detailed description provided.*

(onde_phased_array_angle-bscan_angle)=
### `BSCAN_ANGLE`

*No detailed description provided.*
