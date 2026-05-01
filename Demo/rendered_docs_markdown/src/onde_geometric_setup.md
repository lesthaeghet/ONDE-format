# ONDE_GEOMETRIC_SETUP

### Geometric setup

**Description**

The geometric setup contains references to the inspected component, the probes and the trajectory. If the specimen
description is missing, a semi-infinite half-plane is assumed, with interface at z=0 and material for z>0.

**Trajectories**

ACQUISITION_TRAJECTORY gives references to the groups describing the trajectory -- references have the same order as
PROBE_LIST. PROBE_COORDINATE_FRAME can be used to define an offset between a referenced trajectory and the probe -
identity is assumed if not provided.

## Fields

### `TYPE`

- **Full Name:** `ONDE:TYPE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Allowed Values:** `["ONDE_GEOMETRIC_SETUP"]`


### `COMPONENT`

- **Full Name:** `ONDE_GEOMETRIC_SETUP:COMPONENT`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_STD_REF_OBJ<ONDE_COMPONENT>`
- **Dimensions:** `[1]`

  Reference to the inspected component. If missing, semi-infinite half plane is assumed, with interface at z=0 and material for z>0

### `PROBE_LIST`

- **Full Name:** `ONDE_GEOMETRIC_SETUP:PROBE_LIST`
- **Requirement:** Mandatory
- **Storage:** dataset
- **Type:** `H5T_STD_REF_OBJ<ONDE_UT_PROBE>`
- **Dimensions:** `[N_Prob<M>]`

  List all probes used in the acquisition of the dataset

### `ACQUISITION_TRAJECTORY`

- **Full Name:** `ONDE_GEOMETRIC_SETUP:ACQUISITION_TRAJECTORY`
- **Requirement:** Mandatory
- **Storage:** dataset
- **Type:** `H5T_STD_REF_OBJ<ONDE_ACQUISITION_TRAJECTORY>`
- **Dimensions:** `[N_Prob<M>]`

  References  to the block describing the trajectory  references have the same order as PROBE_LIST

### `PROBE_COORDINATE_FRAME`

- **Full Name:** `ONDE_GEOMETRIC_SETUP:PROBE_COORDINATE_FRAME`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_Prob<M>,7]`

  Offset and direction of the probe w.r.t the trajectory frame- identity  is assumed if not provided
