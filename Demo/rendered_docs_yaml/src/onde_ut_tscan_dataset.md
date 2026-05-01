# ONDE_UT_TSCAN_DATASET

**Inherits from:** ONDE_UT_DATASET

```{mermaid}
classDiagram
  ONDE_UT_DATASET <|-- ONDE_UT_TSCAN_DATASET
  ONDE_UT_TSCAN_DATASET o-- ONDE_ACQUISITION_TRAJECTORY : ONDE_UT_TSCAN_DATASET:REFERENCE_TRAJECTORY
  ONDE_UT_TSCAN_DATASET o-- ONDE_UT_ASCAN_DATASET : ONDE_UT_TSCAN_DATASET:ELEMENTARY_CHANNELS_DATASET
  click ONDE_UT_TSCAN_DATASET href "onde_ut_tscan_dataset.html"
  click ONDE_UT_DATASET href "onde_ut_dataset.html"
  click ONDE_ACQUISITION_TRAJECTORY href "onde_acquisition_trajectory.html"
  click ONDE_UT_ASCAN_DATASET href "onde_ut_ascan_dataset.html"
```

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

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_ut_tscan_dataset-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[2]` | `["ONDE_UT_DATASET","ONDE_UT_TSCAN_DATASET"]` |  |
| [**`DATA`**](#onde_ut_tscan_dataset-data)<br><sub>`ONDE_UT_TSCAN_DATASET:DATA`</sub> | Mandatory | attribute | H5T_STD_REF_OBJ or HT5_INTEGER | `1 or [N_DF<m>,N_ROW<m>,N_COL<m>] or [N_DF<m>,NROW<m>,NCOL<m>,N_PLANE<m>]` | `` | can be either an array or a reference to an array |
| [**`REFERENCE_TRAJECTORY`**](#onde_ut_tscan_dataset-reference_trajectory)<br><sub>`ONDE_UT_TSCAN_DATASET:REFERENCE_TRAJECTORY`</sub> | Mandatory | attribute | H5T_STD_REF_OBJ<[ONDE_ACQUISITION_TRAJECTORY](onde_acquisition_trajectory.md)> | `1` | `` |  |
| [**`ZONE_FRAME`**](#onde_ut_tscan_dataset-zone_frame)<br><sub>`ONDE_UT_TSCAN_DATASET:ZONE_FRAME`</sub> | Mandatory | attribute | H5T_FLOAT | `[7]` | `` | frame associated with the center of the image zone |
| [**`ZONE_DIMENSION`**](#onde_ut_tscan_dataset-zone_dimension)<br><sub>`ONDE_UT_TSCAN_DATASET:ZONE_DIMENSION`</sub> | Mandatory | attribute | H5T_FLOAT | `[3]` | `` | physical dimension of the zone |
| [**`ZONE_SIZE`**](#onde_ut_tscan_dataset-zone_size)<br><sub>`ONDE_UT_TSCAN_DATASET:ZONE_SIZE`</sub> | Mandatory | attribute | H5T_INTEGER | `[3]` | `` | number of pixels of the zone |
| [**`RECONSTRUCTION_MODE`**](#onde_ut_tscan_dataset-reconstruction_mode)<br><sub>`ONDE_UT_TSCAN_DATASET:RECONSTRUCTION_MODE`</sub> | Optional | attribute | H5T_STRING | `1` | `` |  |
| [**`ELEMENTARY_CHANNELS_DATASET`**](#onde_ut_tscan_dataset-elementary_channels_dataset)<br><sub>`ONDE_UT_TSCAN_DATASET:ELEMENTARY_CHANNELS_DATASET`</sub> | Optional | attribute | H5T_STD_REF_OBJ<[ONDE_UT_ASCAN_DATASET](onde_ut_ascan_dataset.md)> | `1` | `` | optional reference to the elementary channels ascans that were used for the reconstruction |


## Field Details

(onde_ut_tscan_dataset-type)=
### `TYPE`

*No detailed description provided.*

(onde_ut_tscan_dataset-data)=
### `DATA`

can be either an array or a reference to an array

(onde_ut_tscan_dataset-reference_trajectory)=
### `REFERENCE_TRAJECTORY`

*No detailed description provided.*

(onde_ut_tscan_dataset-zone_frame)=
### `ZONE_FRAME`

frame associated with the center of the image zone

(onde_ut_tscan_dataset-zone_dimension)=
### `ZONE_DIMENSION`

physical dimension of the zone

(onde_ut_tscan_dataset-zone_size)=
### `ZONE_SIZE`

number of pixels of the zone

(onde_ut_tscan_dataset-reconstruction_mode)=
### `RECONSTRUCTION_MODE`

*No detailed description provided.*

(onde_ut_tscan_dataset-elementary_channels_dataset)=
### `ELEMENTARY_CHANNELS_DATASET`

optional reference to the elementary channels ascans that were used for the reconstruction
