# ONDE_SPATIAL_TRAJECTORY

**Inherits from:** ONDE_ACQUISITION_TRAJECTORY

```{mermaid}
classDiagram
  ONDE_ACQUISITION_TRAJECTORY <|-- ONDE_SPATIAL_TRAJECTORY
  ONDE_SPATIAL_TRAJECTORY <|-- ONDE_ACQUISITION_GRID
  click ONDE_ACQUISITION_GRID href "onde_acquisition_grid.html"
  click ONDE_ACQUISITION_TRAJECTORY href "onde_acquisition_trajectory.html"
  click ONDE_SPATIAL_TRAJECTORY href "onde_spatial_trajectory.html"
```

No narrative documentation provided for ONDE_SPATIAL_TRAJECTORY.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_spatial_trajectory-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[2]` | `["ONDE_ACQUISITION_TRAJECTORY","ONDE_SPATIAL_TRAJECTORY"]` |  |
| [**`TRAJECTORY`**](#onde_spatial_trajectory-trajectory)<br><sub>`ONDE_SPATIAL_TRAJECTORY:TRAJECTORY`</sub> | Optional | dataset | H5T_FLOAT | `[N_Pos<m>,7]` | `` | List of positions and quaternions   giving the positions and orientations of the trajectory frame    at the different positions |


## Field Details

(onde_spatial_trajectory-type)=
### `TYPE`

*No detailed description provided.*

(onde_spatial_trajectory-trajectory)=
### `TRAJECTORY`

List of positions and quaternions   giving the positions and orientations of the trajectory frame    at the different positions
