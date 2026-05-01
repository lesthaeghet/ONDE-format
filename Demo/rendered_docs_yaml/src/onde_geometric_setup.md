# ONDE_GEOMETRIC_SETUP

```{mermaid}
classDiagram
  ONDE_GEOMETRIC_SETUP o-- ONDE_COMPONENT : ONDE_GEOMETRIC_SETUP:COMPONENT
  ONDE_GEOMETRIC_SETUP o-- ONDE_UT_PROBE : ONDE_GEOMETRIC_SETUP:PROBE_LIST
  ONDE_GEOMETRIC_SETUP o-- ONDE_ACQUISITION_TRAJECTORY : ONDE_GEOMETRIC_SETUP:ACQUISITION_TRAJECTORY
  click ONDE_ACQUISITION_TRAJECTORY href "onde_acquisition_trajectory.html"
  click ONDE_UT_PROBE href "onde_ut_probe.html"
  click ONDE_GEOMETRIC_SETUP href "onde_geometric_setup.html"
  click ONDE_COMPONENT href "onde_component.html"
```

### Geometric setup

**Description**

The geometric setup contains references to the inspected component, the probes and the trajectory. If the specimen
description is missing, a semi-infinite half-plane is assumed, with interface at z=0 and material for z>0.

**Trajectories**

ACQUISITION_TRAJECTORY gives references to the groups describing the trajectory -- references have the same order as
PROBE_LIST. PROBE_COORDINATE_FRAME can be used to define an offset between a referenced trajectory and the probe -
identity is assumed if not provided.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_geometric_setup-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `` | `["ONDE_GEOMETRIC_SETUP"]` |  |
| [**`COMPONENT`**](#onde_geometric_setup-component)<br><sub>`ONDE_GEOMETRIC_SETUP:COMPONENT`</sub> | Optional | dataset | H5T_STD_REF_OBJ<[ONDE_COMPONENT](onde_component.md)> | `[1]` | `` | Reference to the inspected component. |
| [**`PROBE_LIST`**](#onde_geometric_setup-probe_list)<br><sub>`ONDE_GEOMETRIC_SETUP:PROBE_LIST`</sub> | Mandatory | dataset | H5T_STD_REF_OBJ<[ONDE_UT_PROBE](onde_ut_probe.md)> | `[N_Prob<M>]` | `` | List all probes used in the acquisition of the dataset |
| [**`ACQUISITION_TRAJECTORY`**](#onde_geometric_setup-acquisition_trajectory)<br><sub>`ONDE_GEOMETRIC_SETUP:ACQUISITION_TRAJECTORY`</sub> | Mandatory | dataset | H5T_STD_REF_OBJ<[ONDE_ACQUISITION_TRAJECTORY](onde_acquisition_trajectory.md)> | `[N_Prob<M>]` | `` | References  to the block describing the trajectory  references have the same order as PROBE_LIST |
| [**`PROBE_COORDINATE_FRAME`**](#onde_geometric_setup-probe_coordinate_frame)<br><sub>`ONDE_GEOMETRIC_SETUP:PROBE_COORDINATE_FRAME`</sub> | Optional | dataset | H5T_FLOAT | `[N_Prob<M>,7]` | `` | Offset and direction of the probe w. |


## Field Details

(onde_geometric_setup-type)=
### `TYPE`

*No detailed description provided.*

(onde_geometric_setup-component)=
### `COMPONENT`

Reference to the inspected component. If missing, semi-infinite half plane is assumed, with interface at z=0 and material for z>0

(onde_geometric_setup-probe_list)=
### `PROBE_LIST`

List all probes used in the acquisition of the dataset

(onde_geometric_setup-acquisition_trajectory)=
### `ACQUISITION_TRAJECTORY`

References  to the block describing the trajectory  references have the same order as PROBE_LIST

(onde_geometric_setup-probe_coordinate_frame)=
### `PROBE_COORDINATE_FRAME`

Offset and direction of the probe w.r.t the trajectory frame- identity  is assumed if not provided
