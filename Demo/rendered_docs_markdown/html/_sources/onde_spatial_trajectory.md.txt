# ONDE_SPATIAL_TRAJECTORY

**Inherits from:** ONDE_ACQUISITION_TRAJECTORY

No narrative documentation provided for ONDE_SPATIAL_TRAJECTORY.

## Fields

### `TYPE`

- **Full Name:** `ONDE:TYPE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `[2]`
- **Allowed Values:** `["ONDE_ACQUISITION_TRAJECTORY","ONDE_SPATIAL_TRAJECTORY"]`


### `TRAJECTORY`

- **Full Name:** `ONDE_SPATIAL_TRAJECTORY:TRAJECTORY`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_Pos<m>,7]`

  List of positions and quaternions   giving the positions and orientations of the trajectory frame    at the different positions
