# ONDE_ACQUISITION_GRID

**Inherits from:** ONDE_ACQUISITION_TRAJECTORY, ONDE_SPATIAL_TRAJECTORY

```{mermaid}
classDiagram
  ONDE_ACQUISITION_TRAJECTORY <|-- ONDE_ACQUISITION_GRID
  ONDE_SPATIAL_TRAJECTORY <|-- ONDE_ACQUISITION_GRID
  click ONDE_ACQUISITION_GRID href "onde_acquisition_grid.html"
  click ONDE_ACQUISITION_TRAJECTORY href "onde_acquisition_trajectory.html"
  click ONDE_SPATIAL_TRAJECTORY href "onde_spatial_trajectory.html"
```

No narrative documentation provided for ONDE_ACQUISITION_GRID.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_acquisition_grid-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[3]` | `["ONDE_ACQUISITION_TRAJECTORY","ONDE_SPATIAL_TRAJECTORY","ONDE_ACQUISITION_GRID"]` |  |
| [**`REFERENCE_SPECIMEN`**](#onde_acquisition_grid-reference_specimen)<br><sub>`ONDE_ACQUISITION_GRID:REFERENCE_SPECIMEN`</sub> | Mandatory | attribute | H5T_STD_REF_OBJ | `1` | `` | When defining an acquisition grid, it is necessary to define a reference specimen that is either a cylinder or a plane. |
| [**`CYLINDER_DEFINITION`**](#onde_acquisition_grid-cylinder_definition)<br><sub>`ONDE_ACQUISITION_GRID:CYLINDER_DEFINITION`</sub> | Optional | attribute | H5T_STRING | `` | `"INNER"\|"OUTER"` | Defines whether the grid is expressed in the inner surface of the cylinder or on the outer surface |
| [**`UV_GRID_FRAME`**](#onde_acquisition_grid-uv_grid_frame)<br><sub>`ONDE_ACQUISITION_GRID:UV_GRID_FRAME`</sub> | Optional | attribute | H5T_FLOAT | `[3]` | `` | 2D Frame defining the U_GRID and V_GRID directions of the encoding in the surface representation of the specimen (X,Y) for planar specimens, (X,THETA) for cylindrical specimens. |
| [**`U_GRID_DATA`**](#onde_acquisition_grid-u_grid_data)<br><sub>`ONDE_ACQUISITION_GRID:U_GRID_DATA`</sub> | Mandatory | dataset | H5T_FLOAT | `[N_U<m>]` | `` | The specified values of the first coder at the different positions |
| [**`V_GRID_DATA`**](#onde_acquisition_grid-v_grid_data)<br><sub>`ONDE_ACQUISITION_GRID:V_GRID_DATA`</sub> | Optional | dataset | H5T_FLOAT | `[N_V<m>]` | `` | The specified values of the second coder at the different positions. |
| [**`SCAN_TYPE`**](#onde_acquisition_grid-scan_type)<br><sub>`ONDE_ACQUISITION_GRID:SCAN_TYPE`</sub> | Mandatory | attribute | H5T_STRING | `1` | `"COMB"\|"RASTER"` | Defines whether the data is ordered in the same direction for each scan (COMB) or is inversed every second scan (RASTER) |
| [**`U_ENCODER`**](#onde_acquisition_grid-u_encoder)<br><sub>`ONDE_ACQUISITION_GRID:U_ENCODER`</sub> | Optional | dataset | H5T_FLOAT | `[N_V<m>,N_U<m>]` | `` | Obtained encoder values on the u axis |
| [**`V_ENCODER`**](#onde_acquisition_grid-v_encoder)<br><sub>`ONDE_ACQUISITION_GRID:V_ENCODER`</sub> | Optional | dataset | H5T_FLOAT | `[N_V<m>,N_U<m>]` | `` | Obtained encoder values on the v axis |
| [**`PROBE_DIRECTION`**](#onde_acquisition_grid-probe_direction)<br><sub>`ONDE_ACQUISITION_GRID:PROBE_DIRECTION`</sub> | Optional | dataset | H5T_FLOAT | `[3,3]` | `` | For grid data, direction of the probe in the (u,v,w) coordinate system. |


## Field Details

(onde_acquisition_grid-type)=
### `TYPE`

*No detailed description provided.*

(onde_acquisition_grid-reference_specimen)=
### `REFERENCE_SPECIMEN`

When defining an acquisition grid, it is necessary to define a reference specimen that is either a cylinder or a plane.

(onde_acquisition_grid-cylinder_definition)=
### `CYLINDER_DEFINITION`

Defines whether the grid is expressed in the inner surface of the cylinder or on the outer surface

(onde_acquisition_grid-uv_grid_frame)=
### `UV_GRID_FRAME`

2D Frame defining the U_GRID and V_GRID directions of the encoding in the surface representation of the specimen (X,Y) for planar specimens, (X,THETA) for cylindrical specimens. (1,0,) is assumed if missing

(onde_acquisition_grid-u_grid_data)=
### `U_GRID_DATA`

The specified values of the first coder at the different positions

(onde_acquisition_grid-v_grid_data)=
### `V_GRID_DATA`

The specified values of the second coder at the different positions. If missing while U_GRID_DATA is present, 1D array of data is assumed.

(onde_acquisition_grid-scan_type)=
### `SCAN_TYPE`

Defines whether the data is ordered in the same direction for each scan (COMB) or is inversed every second scan (RASTER)

(onde_acquisition_grid-u_encoder)=
### `U_ENCODER`

Obtained encoder values on the u axis

(onde_acquisition_grid-v_encoder)=
### `V_ENCODER`

Obtained encoder values on the v axis

(onde_acquisition_grid-probe_direction)=
### `PROBE_DIRECTION`

For grid data, direction of the probe in the (u,v,w) coordinate system. Defaults to identity matrix.
