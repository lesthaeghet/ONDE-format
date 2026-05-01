# ONDE_ACQUISITION_TRAJECTORY

```{mermaid}
classDiagram
  ONDE_ACQUISITION_TRAJECTORY <|-- ONDE_ACQUISITION_GRID
  ONDE_ACQUISITION_TRAJECTORY <|-- ONDE_SPATIAL_TRAJECTORY
  ONDE_ACQUISITION_TRAJECTORY <|-- ONDE_TIME_TRAJECTORY
  click ONDE_ACQUISITION_GRID href "onde_acquisition_grid.html"
  click ONDE_ACQUISITION_TRAJECTORY href "onde_acquisition_trajectory.html"
  click ONDE_TIME_TRAJECTORY href "onde_time_trajectory.html"
  click ONDE_SPATIAL_TRAJECTORY href "onde_spatial_trajectory.html"
```

No narrative documentation provided for ONDE_ACQUISITION_TRAJECTORY.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_acquisition_trajectory-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[1]` | `["ONDE_ACQUISITION_TRAJECTORY"]` |  |


## Field Details

(onde_acquisition_trajectory-type)=
### `TYPE`

*No detailed description provided.*
