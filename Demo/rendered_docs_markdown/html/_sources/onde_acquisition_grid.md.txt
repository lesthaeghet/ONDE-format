# ONDE_ACQUISITION_GRID

**Inherits from:** ONDE_ACQUISITION_TRAJECTORY, ONDE_SPATIAL_TRAJECTORY

No narrative documentation provided for ONDE_ACQUISITION_GRID.

## Fields

### `TYPE`

- **Full Name:** `ONDE:TYPE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `[3]`
- **Allowed Values:** `["ONDE_ACQUISITION_TRAJECTORY","ONDE_SPATIAL_TRAJECTORY","ONDE_ACQUISITION_GRID"]`


### `REFERENCE_SPECIMEN`

- **Full Name:** `ONDE_ACQUISITION_GRID:REFERENCE_SPECIMEN`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STD_REF_OBJ`
- **Dimensions:** `1`

  When defining an acquisition grid, it is necessary to define a reference specimen that is either a cylinder or a plane.

### `CYLINDER_DEFINITION`

- **Full Name:** `ONDE_ACQUISITION_GRID:CYLINDER_DEFINITION`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Allowed Values:** `"INNER"|"OUTER"`

  Defines whether the grid is expressed in the inner surface of the cylinder or on the outer surface

### `UV_GRID_FRAME`

- **Full Name:** `ONDE_ACQUISITION_GRID:UV_GRID_FRAME`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[3]`

  2D Frame defining the U_GRID and V_GRID directions of the encoding in the surface representation of the specimen (X,Y) for planar specimens, (X,THETA) for cylindrical specimens. (1,0,) is assumed if missing

### `U_GRID_DATA`

- **Full Name:** `ONDE_ACQUISITION_GRID:U_GRID_DATA`
- **Requirement:** Mandatory
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_U<m>]`

  The specified values of the first coder at the different positions

### `V_GRID_DATA`

- **Full Name:** `ONDE_ACQUISITION_GRID:V_GRID_DATA`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_V<m>]`

  The specified values of the second coder at the different positions. If missing while U_GRID_DATA is present, 1D array of data is assumed.

### `SCAN_TYPE`

- **Full Name:** `ONDE_ACQUISITION_GRID:SCAN_TYPE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `1`
- **Allowed Values:** `"COMB"|"RASTER"`

  Defines whether the data is ordered in the same direction for each scan (COMB) or is inversed every second scan (RASTER)

### `U_ENCODER`

- **Full Name:** `ONDE_ACQUISITION_GRID:U_ENCODER`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_V<m>,N_U<m>]`

  Obtained encoder values on the u axis

### `V_ENCODER`

- **Full Name:** `ONDE_ACQUISITION_GRID:V_ENCODER`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_V<m>,N_U<m>]`

  Obtained encoder values on the v axis

### `PROBE_DIRECTION`

- **Full Name:** `ONDE_ACQUISITION_GRID:PROBE_DIRECTION`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[3,3]`

  For grid data, direction of the probe in the (u,v,w) coordinate system. Defaults to identity matrix.
