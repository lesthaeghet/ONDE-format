# ONDE_TIME_TRAJECTORY

**Inherits from:** ONDE_ACQUISITION_TRAJECTORY

```{mermaid}
classDiagram
  ONDE_ACQUISITION_TRAJECTORY <|-- ONDE_TIME_TRAJECTORY
  click ONDE_ACQUISITION_TRAJECTORY href "onde_acquisition_trajectory.html"
  click ONDE_TIME_TRAJECTORY href "onde_time_trajectory.html"
```

No narrative documentation provided for ONDE_TIME_TRAJECTORY.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_time_trajectory-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[2]` | `["ONDE_ACQUISITION_TRAJECTORY","ONDE_TIME_TRAJECTORY"]` |  |
| [**`ACQUISITION_RATE`**](#onde_time_trajectory-acquisition_rate)<br><sub>`ONDE_TIME_TRAJECTORY:ACQUISITION_RATE`</sub> | Optional | attribute | H5T_FLOAT | `1` | `` | For time encoded trajectories, defines the acquisition rate |


## Field Details

(onde_time_trajectory-type)=
### `TYPE`

*No detailed description provided.*

(onde_time_trajectory-acquisition_rate)=
### `ACQUISITION_RATE`

For time encoded trajectories, defines the acquisition rate
