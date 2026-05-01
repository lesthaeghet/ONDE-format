# ONDE_UT_TSCAN_DATASET

**Inherits from:** ONDE_UT_DATASET

### Tscan datasets

**General**

Even though the name (Tscans coming from TFM Scans) implicitly refers to the TFM reconstruction images, the block can
apply to any reconstruction method producing data on a rectangular/parallelepiped grid that moves with the sensor (be it
obtained by TFM, Adaptive TFM, PWI, Adaptive PWI, frequency reconstruction, or any variant of these methods)

**3D Zones**

The format allows for the description of 3D zones. Taking into account the dimension related to positions, this implies
that the dimension of the data array depends on the zone dimension (3D array for 2D zones 4D array for 3D zones),

**Zone dimension and position**

The zone physical dimension is given by the ZONE_DIMENSION field, (DX,DY,DZ) being the physical dimensions of the zone,
a zero or a NaN for one of the dimension implies a 2D zone.

ZONE_SIZE is a triplet which gives the number of pixels of the zone for each dimension (NX,NY,NZ).

The zone position is given by ZONE_FRAME and is expressed relatively to the trajectory frame pointed to by
REFERENCE_TRAJECTORY.

![Example of TFM zone positioning](../images/media/figure5.png "Figure 5")

*Figure 5: Example of TFM zone positioning*

In the example displayed in Figure 5, the trajectory frame is located at the index point and the zone is positioned
accordingly.

**Pixel ordering**

The pixels are stored in the (X,Y,Z) order (X being the outer loop, Z the inner loop in the array)

## Fields

### `TYPE`

- **Full Name:** `ONDE:TYPE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `[2]`
- **Allowed Values:** `["ONDE_UT_DATASET","ONDE_UT_TSCAN_DATASET"]`


### `DATA`

- **Full Name:** `ONDE_UT_TSCAN_DATASET:DATA`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STD_REF_OBJ or HT5_INTEGER`
- **Dimensions:** `1 or [N_DF<m>,N_ROW<m>,N_COL<m>] or [N_DF<m>,NROW<m>,NCOL<m>,N_PLANE<m>]`

  can be either an array or a reference to an array

### `REFERENCE_TRAJECTORY`

- **Full Name:** `ONDE_UT_TSCAN_DATASET:REFERENCE_TRAJECTORY`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STD_REF_OBJ<ONDE_ACQUISITION_TRAJECTORY>`
- **Dimensions:** `1`


### `ZONE_FRAME`

- **Full Name:** `ONDE_UT_TSCAN_DATASET:ZONE_FRAME`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[7]`

  frame associated with the center of the image zone

### `ZONE_DIMENSION`

- **Full Name:** `ONDE_UT_TSCAN_DATASET:ZONE_DIMENSION`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[3]`

  physical dimension of the zone

### `ZONE_SIZE`

- **Full Name:** `ONDE_UT_TSCAN_DATASET:ZONE_SIZE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_INTEGER`
- **Dimensions:** `[3]`

  number of pixels of the zone

### `RECONSTRUCTION_MODE`

- **Full Name:** `ONDE_UT_TSCAN_DATASET:RECONSTRUCTION_MODE`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `1`


### `ELEMENTARY_CHANNELS_DATASET`

- **Full Name:** `ONDE_UT_TSCAN_DATASET:ELEMENTARY_CHANNELS_DATASET`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STD_REF_OBJ<ONDE_UT_ASCAN_DATASET>`
- **Dimensions:** `1`

  optional reference to the elementary channels ascans that were used for the reconstruction
