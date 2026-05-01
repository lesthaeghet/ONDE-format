# ONDE_UT_COUPLING

```{mermaid}
classDiagram
  ONDE_UT_COUPLING <|-- ONDE_DUAL_WEDGE
  ONDE_UT_COUPLING <|-- ONDE_IMMERSION
  ONDE_UT_COUPLING <|-- ONDE_SINGLE_WEDGE
  ONDE_UT_COUPLING <|-- ONDE_WEDGE
  click ONDE_SINGLE_WEDGE href "onde_single_wedge.html"
  click ONDE_WEDGE href "onde_wedge.html"
  click ONDE_IMMERSION href "onde_immersion.html"
  click ONDE_DUAL_WEDGE href "onde_dual_wedge.html"
  click ONDE_UT_COUPLING href "onde_ut_coupling.html"
```

No narrative documentation provided for ONDE_UT_COUPLING.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_ut_coupling-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[1]` | `["ONDE_UT_COUPLING"]` |  |
| [**`MEDIUM_VELOCITY`**](#onde_ut_coupling-medium_velocity)<br><sub>`ONDE_UT_COUPLING:MEDIUM_VELOCITY`</sub> | Mandatory | attribute | H5T_FLOAT | `[2]` | `` |  |
| [**`MEDIUM_DENSITY`**](#onde_ut_coupling-medium_density)<br><sub>`ONDE_UT_COUPLING:MEDIUM_DENSITY`</sub> | Optional | attribute | H5T_FLOAT | `1` | `` |  |
| [**`INCIDENCE_ANGLE`**](#onde_ut_coupling-incidence_angle)<br><sub>`ONDE_UT_COUPLING:INCIDENCE_ANGLE`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |


## Field Details

(onde_ut_coupling-type)=
### `TYPE`

*No detailed description provided.*

(onde_ut_coupling-medium_velocity)=
### `MEDIUM_VELOCITY`

*No detailed description provided.*

(onde_ut_coupling-medium_density)=
### `MEDIUM_DENSITY`

*No detailed description provided.*

(onde_ut_coupling-incidence_angle)=
### `INCIDENCE_ANGLE`

*No detailed description provided.*
