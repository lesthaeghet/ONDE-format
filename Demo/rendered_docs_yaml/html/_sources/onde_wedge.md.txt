# ONDE_WEDGE

**Inherits from:** ONDE_UT_COUPLING

```{mermaid}
classDiagram
  ONDE_UT_COUPLING <|-- ONDE_WEDGE
  ONDE_WEDGE <|-- ONDE_DUAL_WEDGE
  click ONDE_DUAL_WEDGE href "onde_dual_wedge.html"
  click ONDE_UT_COUPLING href "onde_ut_coupling.html"
  click ONDE_WEDGE href "onde_wedge.html"
```

No narrative documentation provided for ONDE_WEDGE.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_wedge-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[2]` | `["ONDE_UT_COUPLING","ONDE_WEDGE"]` |  |
| [**`LABEL`**](#onde_wedge-label)<br><sub>`ONDE:LABEL`</sub> | Optional | attribute | H5T_STRING | `1` | `` |  |
| [**`MANUFACTURER`**](#onde_wedge-manufacturer)<br><sub>`ONDE_WEDGE:MANUFACTURER`</sub> | Optional | attribute | H5T_STRING | `1` | `` |  |
| [**`SERIAL_NUMBER`**](#onde_wedge-serial_number)<br><sub>`ONDE_WEDGE:SERIAL_NUMBER`</sub> | Optional | attribute | H5T_STRING | `1` | `` |  |
| [**`CONTACT_SURFACE`**](#onde_wedge-contact_surface)<br><sub>`ONDE_WEDGE:CONTACT_SURFACE`</sub> | Mandatory | attribute | H5T_STRING | `` | `"PLANAR"\|"SPHERICAL"\|"CYLINDRICAL_MAJOR"\|"CYLINDRICAL_MINOR"` | Type of the wedge contact surface - PLANAR, SPHERICAL, CYLINDRICAL_MAJOR, CYLINDRICAL_MINOR - If missing PLANAR assumed |
| [**`CURVATURE_RADIUS`**](#onde_wedge-curvature_radius)<br><sub>`ONDE_WEDGE:CURVATURE_RADIUS`</sub> | Optional | attribute | H5T_FLOAT | `1` | `` | Wedge curvature radius - Concave : positive - Convex : negative - 0 in the case of a planar wedge - If missing 0 assumed. |
| [**`CONTACT_AREA`**](#onde_wedge-contact_area)<br><sub>`ONDE_WEDGE:CONTACT_AREA`</sub> | Mandatory | attribute | H5T_FLOAT | `[3]` | `` | Equivalent to L1, L2 and L3 (See Figure 15) |
| [**`HEIGHT`**](#onde_wedge-height)<br><sub>`ONDE_WEDGE:HEIGHT`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` | For a wedge, distance of the ultrasonic beam between the probe center and the index point (See Figure 15) |
| [**`SKEW_ANGLE`**](#onde_wedge-skew_angle)<br><sub>`ONDE_WEDGE:SKEW_ANGLE`</sub> | Optional | attribute | H5T_FLOAT | `1` | `` | wedge /skew angle (B) (See Figure 15) |
| [**`DISORIENTATION_ANGLE`**](#onde_wedge-disorientation_angle)<br><sub>`ONDE_WEDGE:DISORIENTATION_ANGLE`</sub> | Optional | attribute | H5T_FLOAT | `1` | `` | wedge /disorientation angle (D) (See Figure 15) |


## Field Details

(onde_wedge-type)=
### `TYPE`

*No detailed description provided.*

(onde_wedge-label)=
### `LABEL`

*No detailed description provided.*

(onde_wedge-manufacturer)=
### `MANUFACTURER`

*No detailed description provided.*

(onde_wedge-serial_number)=
### `SERIAL_NUMBER`

*No detailed description provided.*

(onde_wedge-contact_surface)=
### `CONTACT_SURFACE`

Type of the wedge contact surface - PLANAR, SPHERICAL, CYLINDRICAL_MAJOR, CYLINDRICAL_MINOR - If missing PLANAR assumed

(onde_wedge-curvature_radius)=
### `CURVATURE_RADIUS`

Wedge curvature radius - Concave : positive - Convex : negative - 0 in the case of a planar wedge - If missing 0 assumed.

(onde_wedge-contact_area)=
### `CONTACT_AREA`

Equivalent to L1, L2 and L3 (See Figure 15)

(onde_wedge-height)=
### `HEIGHT`

For a wedge, distance of the ultrasonic beam between the probe center and the index point (See Figure 15)

(onde_wedge-skew_angle)=
### `SKEW_ANGLE`

wedge /skew angle (B) (See Figure 15)

(onde_wedge-disorientation_angle)=
### `DISORIENTATION_ANGLE`

wedge /disorientation angle (D) (See Figure 15)
