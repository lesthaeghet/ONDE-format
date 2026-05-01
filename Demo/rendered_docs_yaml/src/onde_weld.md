# ONDE_WELD

**Inherits from:** ONDE_COMPONENT

```{mermaid}
classDiagram
  ONDE_COMPONENT <|-- ONDE_WELD
  click ONDE_WELD href "onde_weld.html"
  click ONDE_COMPONENT href "onde_component.html"
```

No narrative documentation provided for ONDE_WELD.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_weld-type)<br><sub>`ONDE_WELD:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[2]` | `["ONDE_COMPONENT","ONDE_WELD"]` |  |
| [**`EXTRUSION_TYPE`**](#onde_weld-extrusion_type)<br><sub>`ONDE_WELD:EXTRUSION_TYPE`</sub> | Mandatory | attribute | H5T_STRING | `1` | `"PLANE" \|"CYLINDER"` |  |
| [**`EXTRUSION_DIMENSION`**](#onde_weld-extrusion_dimension)<br><sub>`ONDE_WELD:EXTRUSION_DIMENSION`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`WELD_TYPE`**](#onde_weld-weld_type)<br><sub>`ONDE_WELD:WELD_TYPE`</sub> | Mandatory | attribute | H5T_STRING | `1` | `"V"\|"U"` |  |
| [**`WELD_SYMMETRY`**](#onde_weld-weld_symmetry)<br><sub>`ONDE_WELD:WELD_SYMMETRY`</sub> | Mandatory | attribute | H5T_STRING | `1` | `"SYMMETRIC"\|"STRAIGHT_LEFT"\|"STRAIGHT_RIGHT"` |  |
| [**`WELD_UPPER_CAP_WIDTH`**](#onde_weld-weld_upper_cap_width)<br><sub>`ONDE_WELD:WELD_UPPER_CAP_WIDTH`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`WELD_UPPER_CAP_HEIGHT`**](#onde_weld-weld_upper_cap_height)<br><sub>`ONDE_WELD:WELD_UPPER_CAP_HEIGHT`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`WELD_FILL_ANGLE`**](#onde_weld-weld_fill_angle)<br><sub>`ONDE_WELD:WELD_FILL_ANGLE`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`WELD_FILL_HEIGHT`**](#onde_weld-weld_fill_height)<br><sub>`ONDE_WELD:WELD_FILL_HEIGHT`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`WELD_HOT_PASS_ANGLE`**](#onde_weld-weld_hot_pass_angle)<br><sub>`ONDE_WELD:WELD_HOT_PASS_ANGLE`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`WELD_HOT_PASS_HEIGHT`**](#onde_weld-weld_hot_pass_height)<br><sub>`ONDE_WELD:WELD_HOT_PASS_HEIGHT`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`WELD_LAND_OFFSET`**](#onde_weld-weld_land_offset)<br><sub>`ONDE_WELD:WELD_LAND_OFFSET`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`WELD_LAND_HEIGHT`**](#onde_weld-weld_land_height)<br><sub>`ONDE_WELD:WELD_LAND_HEIGHT`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`WELD_ROOT_ANGLE`**](#onde_weld-weld_root_angle)<br><sub>`ONDE_WELD:WELD_ROOT_ANGLE`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`WELD_ROOT_HEIGHT`**](#onde_weld-weld_root_height)<br><sub>`ONDE_WELD:WELD_ROOT_HEIGHT`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`WELD_LOWER_CAP_HEIGHT`**](#onde_weld-weld_lower_cap_height)<br><sub>`ONDE_WELD:WELD_LOWER_CAP_HEIGHT`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`WELD_LOWER_CAP_WIDTH`**](#onde_weld-weld_lower_cap_width)<br><sub>`ONDE_WELD:WELD_LOWER_CAP_WIDTH`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`WELD_HAZ_WIDTH`**](#onde_weld-weld_haz_width)<br><sub>`ONDE_WELD:WELD_HAZ_WIDTH`</sub> | Optional | attribute | H5T_FLOAT | `1` | `` |  |


## Field Details

(onde_weld-type)=
### `TYPE`

*No detailed description provided.*

(onde_weld-extrusion_type)=
### `EXTRUSION_TYPE`

*No detailed description provided.*

(onde_weld-extrusion_dimension)=
### `EXTRUSION_DIMENSION`

*No detailed description provided.*

(onde_weld-weld_type)=
### `WELD_TYPE`

*No detailed description provided.*

(onde_weld-weld_symmetry)=
### `WELD_SYMMETRY`

*No detailed description provided.*

(onde_weld-weld_upper_cap_width)=
### `WELD_UPPER_CAP_WIDTH`

*No detailed description provided.*

(onde_weld-weld_upper_cap_height)=
### `WELD_UPPER_CAP_HEIGHT`

*No detailed description provided.*

(onde_weld-weld_fill_angle)=
### `WELD_FILL_ANGLE`

*No detailed description provided.*

(onde_weld-weld_fill_height)=
### `WELD_FILL_HEIGHT`

*No detailed description provided.*

(onde_weld-weld_hot_pass_angle)=
### `WELD_HOT_PASS_ANGLE`

*No detailed description provided.*

(onde_weld-weld_hot_pass_height)=
### `WELD_HOT_PASS_HEIGHT`

*No detailed description provided.*

(onde_weld-weld_land_offset)=
### `WELD_LAND_OFFSET`

*No detailed description provided.*

(onde_weld-weld_land_height)=
### `WELD_LAND_HEIGHT`

*No detailed description provided.*

(onde_weld-weld_root_angle)=
### `WELD_ROOT_ANGLE`

*No detailed description provided.*

(onde_weld-weld_root_height)=
### `WELD_ROOT_HEIGHT`

*No detailed description provided.*

(onde_weld-weld_lower_cap_height)=
### `WELD_LOWER_CAP_HEIGHT`

*No detailed description provided.*

(onde_weld-weld_lower_cap_width)=
### `WELD_LOWER_CAP_WIDTH`

*No detailed description provided.*

(onde_weld-weld_haz_width)=
### `WELD_HAZ_WIDTH`

*No detailed description provided.*
