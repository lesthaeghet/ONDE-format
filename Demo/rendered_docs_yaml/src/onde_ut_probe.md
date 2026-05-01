# ONDE_UT_PROBE

```{mermaid}
classDiagram
  ONDE_UT_PROBE <|-- ONDE_LINEAR_UT_PROBE
  ONDE_UT_PROBE <|-- ONDE_MATRIX_UT_PROBE
  ONDE_UT_PROBE <|-- ONDE_MONO_UT_PROBE
  ONDE_UT_PROBE o-- ONDE_UT_COUPLING : ONDE_UT_PROBE:COUPLING
  click ONDE_LINEAR_UT_PROBE href "onde_linear_ut_probe.html"
  click ONDE_MONO_UT_PROBE href "onde_mono_ut_probe.html"
  click ONDE_UT_PROBE href "onde_ut_probe.html"
  click ONDE_UT_COUPLING href "onde_ut_coupling.html"
  click ONDE_MATRIX_UT_PROBE href "onde_matrix_ut_probe.html"
```

No narrative documentation provided for ONDE_UT_PROBE.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_ut_probe-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[1]` | `["ONDE_UT_PROBE"]` |  |
| [**`TYPE_TAGS`**](#onde_ut_probe-type_tags)<br><sub>`ONDE:TYPE_TAGS`</sub> | Mandatory | attribute | H5T_STRING | `[1]` | `["ONDE_UT_ELEMENTS"]` |  |
| [**`LABEL`**](#onde_ut_probe-label)<br><sub>`ONDE:LABEL`</sub> | Optional | attribute | H5T_STRING | `1` | `` |  |
| [**`INDEX_POINT_FRAME`**](#onde_ut_probe-index_point_frame)<br><sub>`ONDE_UT_PROBE:INDEX_POINT_FRAME`</sub> | Optional | dataset | H5T_FLOAT | `[7]` | `` | If absent, identity is assumed |
| [**`MANUFACTURER`**](#onde_ut_probe-manufacturer)<br><sub>`ONDE_UT_PROBE:MANUFACTURER`</sub> | Optional | attribute | H5T_STRING | `1` | `` |  |
| [**`SERIAL_NUMBER`**](#onde_ut_probe-serial_number)<br><sub>`ONDE_UT_PROBE:SERIAL_NUMBER`</sub> | Optional | attribute | H5T_STRING | `1` | `` |  |
| [**`FREQUENCY`**](#onde_ut_probe-frequency)<br><sub>`ONDE_UT_PROBE:FREQUENCY`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`BANDWIDTH`**](#onde_ut_probe-bandwidth)<br><sub>`ONDE_UT_PROBE:BANDWIDTH`</sub> | Optional | attribute | H5T_FLOAT | `1` | `` |  |
| [**`FOCUSING_SURFACE`**](#onde_ut_probe-focusing_surface)<br><sub>`ONDE_UT_PROBE:FOCUSING_SURFACE`</sub> | Optional | attribute | H5T_INTEGER | `` | `"FLAT"\|"CYLINDRICAL_INC"\|"CYLINDRICAL_PERP"\|"SPHERICAL"\|"BIFOCAL"\|"TRIFOCAL"` | Defines the shape of the surface on which the elements are arranged - if absent, FLAT is assumed |
| [**`FOCUSING_SURFACE_PARAMETERS`**](#onde_ut_probe-focusing_surface_parameters)<br><sub>`ONDE_UT_PROBE:FOCUSING_SURFACE_PARAMETERS`</sub> | Optional | attribute | H5T_FLOAT | `[3]` | `` | Multi values : value in mm - FLAT : no value - CYLINDRICAL_INC, CYLINDRICAL_PER : Surface radius - SPHERICAL : Surface radius - BIFOCAL : Surface radius in the incidence plane, surface radius in the plane perpendicular to the incidence plane - TRIFOCAL : Surface radius in the incidence plane (bottom), Surface radius in the incidence plane (top), surface radius in the plane perpendicular to the incidence plane. |
| [**`COUPLING`**](#onde_ut_probe-coupling)<br><sub>`ONDE_UT_PROBE:COUPLING`</sub> | Mandatory | attribute | H5T_STD_REF_OBJ<[ONDE_UT_COUPLING](onde_ut_coupling.md)> | `1` | `` | Reference to the coupling system (wedge, immersion, direct) |


## Field Details

(onde_ut_probe-type)=
### `TYPE`

*No detailed description provided.*

(onde_ut_probe-type_tags)=
### `TYPE_TAGS`

*No detailed description provided.*

(onde_ut_probe-label)=
### `LABEL`

*No detailed description provided.*

(onde_ut_probe-index_point_frame)=
### `INDEX_POINT_FRAME`

If absent, identity is assumed

(onde_ut_probe-manufacturer)=
### `MANUFACTURER`

*No detailed description provided.*

(onde_ut_probe-serial_number)=
### `SERIAL_NUMBER`

*No detailed description provided.*

(onde_ut_probe-frequency)=
### `FREQUENCY`

*No detailed description provided.*

(onde_ut_probe-bandwidth)=
### `BANDWIDTH`

*No detailed description provided.*

(onde_ut_probe-focusing_surface)=
### `FOCUSING_SURFACE`

Defines the shape of the surface on which the elements are arranged - if absent, FLAT is assumed

(onde_ut_probe-focusing_surface_parameters)=
### `FOCUSING_SURFACE_PARAMETERS`

Multi values : value in mm - FLAT : no value - CYLINDRICAL_INC, CYLINDRICAL_PER : Surface radius - SPHERICAL : Surface radius - BIFOCAL : Surface radius in the incidence plane, surface radius in the plane perpendicular to the incidence plane - TRIFOCAL : Surface radius in the incidence plane (bottom), Surface radius in the incidence plane (top), surface radius in the plane perpendicular to the incidence plane.

(onde_ut_probe-coupling)=
### `COUPLING`

Reference to the coupling system (wedge, immersion, direct)
