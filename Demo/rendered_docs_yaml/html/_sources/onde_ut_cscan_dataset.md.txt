# ONDE_UT_CSCAN_DATASET

**Inherits from:** ONDE_UT_DATASET

```{mermaid}
classDiagram
  ONDE_UT_DATASET <|-- ONDE_UT_CSCAN_DATASET
  ONDE_UT_CSCAN_DATASET o-- ONDE_ACQUISITION_TRAJECTORY : ONDE_UT_CSCAN_DATASET:REFERENCE_TRAJECTORY
  ONDE_UT_CSCAN_DATASET o-- ONDE_UT_GATE : ONDE_UT_CSCAN_DATASET:GATES
  click ONDE_ACQUISITION_TRAJECTORY href "onde_acquisition_trajectory.html"
  click ONDE_UT_DATASET href "onde_ut_dataset.html"
  click ONDE_UT_CSCAN_DATASET href "onde_ut_cscan_dataset.html"
  click ONDE_UT_GATE href "onde_ut_gate.html"
```

### CScan datasets and gates

**CScan data and peaks**

While this Cscan dataset is mostly meant for the storage of peak-like data (amplitude, time of flight, etc...) it is
more generic and can accommodate different values.

DATA contains a vector of references to datasets containing scalar raw data. The size of the data can be either
N_DF\<m\> x N_Ascan\<m\> arrays (for data resulting from analysis of signals or N_DF\<m\> arrays for encoder data or
data
resulting from Tscan or monoelement scans.

**Data description**

The DATATYPE field contains a name defining the nature of the data- the name can be either custom (MY_MATERIAL_PROPERTY
for instance) or a standardized name: THICKNESS, TIME_OF_FLIGHT, DEPTH, AMAX.

**Data numbering**

To be efficient for relatively small amounts of data, as opposed to other blocks, the Cscan block allows for
the handling of several data inside the block. The DATA, DATA_TYPE vectors must have the same length and be ordered
coherently.

**Data positioning**

The Cscan data can be positioned through a trajectory block which is defined in REFERENCE_TRAJECTORY.

**Underlying raw data**

UNDERLYING_DATA is used to point to the dataset that corresponds to the originating raw data. LINKED_DATASET_REFERENCE
gives the correspondence between the scalar data and the originating scan. For a A-Scan, the correspondence to the scan
is expressed in terms of (dataframe, law). For a 2D Tscan, it will be (dataframe, column), for a 3D Tscan, it will be (
dataframe, plane, column).

**Gates**

The gates are stored as a separate group of type ONDE_UT_GATE. The gates are referenced in the ONDE_UT_CSCAN_DATASET group via the 
ONDE_UT_CSCAN_DATASET:GATES field.
The gates used for the acquisition are defined through four parameters.\
GATE_START and GATE_WIDTH define the time window and GATE_THRESHOLD defines the threshold that was used to trigger the
storage of the data. GATE_DETECTION defines the type of triggering event that was used to define the gate.


## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_ut_cscan_dataset-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[2]` | `["ONDE_UT_DATASET","ONDE_UT_CSCAN_DATASET"]` |  |
| [**`DATA`**](#onde_ut_cscan_dataset-data)<br><sub>`ONDE_UT_CSCAN_DATASET:DATA`</sub> | Mandatory | dataset | H5T_STD_REF_OBJ or HT5_INTEGER | `[N_CS<m>] |[N_CS<m>,N_Gate<m>]` | `` | references to arrays containing the different values stored in the dataset |
| [**`DATATYPE`**](#onde_ut_cscan_dataset-datatype)<br><sub>`ONDE_UT_CSCAN_DATASET:DATATYPE`</sub> | Mandatory | dataset | H5T_STRING | `[N_CS<m>]` | `` | string defining the stored data - the name can be either custom  (MY_MATERIAL_PROPERTY for instance) or a standardized name : THICKNESS, TIME_OF_FLIGHT, DEPTH, AMAX |
| [**`UNDERLYING_DATA`**](#onde_ut_cscan_dataset-underlying_data)<br><sub>`ONDE_UT_CSCAN_DATASET:UNDERLYING_DATA`</sub> | Optional | attribute | H5T_STD_REF_OBJ<ONDE_UT_ASCAN_DATASET> or H5T_STD_REF_OBJ<ONDE_UT_TSCAN_DATASET> | `1` | `` | reference to the dataset containing the underlying data |
| [**`UNDERLYING_DATA_REFERENCE`**](#onde_ut_cscan_dataset-underlying_data_reference)<br><sub>`ONDE_UT_CSCAN_DATASET:UNDERLYING_DATA_REFERENCE`</sub> | Optional | dataset | H5T_INTEGER | `[N_DF<m>,2] or [N_DF<m>,3]` | `` | Correspondancy between the C-Scan scalar data and the scan originating. |
| [**`REFERENCE_TRAJECTORY`**](#onde_ut_cscan_dataset-reference_trajectory)<br><sub>`ONDE_UT_CSCAN_DATASET:REFERENCE_TRAJECTORY`</sub> | Mandatory | attribute | H5T_STD_REF_OBJ<[ONDE_ACQUISITION_TRAJECTORY](onde_acquisition_trajectory.md)> | `1` | `` |  |
| [**`GATES`**](#onde_ut_cscan_dataset-gates)<br><sub>`ONDE_UT_CSCAN_DATASET:GATES`</sub> | Optional | dataset | H5T_STD_REF_OBJ<[ONDE_UT_GATE](onde_ut_gate.md)> | `[N_Gate<m>]` | `` |  |


## Field Details

(onde_ut_cscan_dataset-type)=
### `TYPE`

*No detailed description provided.*

(onde_ut_cscan_dataset-data)=
### `DATA`

references to arrays containing the different values stored in the dataset

(onde_ut_cscan_dataset-datatype)=
### `DATATYPE`

string defining the stored data - the name can be either custom  (MY_MATERIAL_PROPERTY for instance) or a standardized name : THICKNESS, TIME_OF_FLIGHT, DEPTH, AMAX

(onde_ut_cscan_dataset-underlying_data)=
### `UNDERLYING_DATA`

reference to the dataset containing the underlying data

(onde_ut_cscan_dataset-underlying_data_reference)=
### `UNDERLYING_DATA_REFERENCE`

Correspondancy between the C-Scan scalar data and the scan originating. For a A-Scan, the scan is expressed in terms of (dataframe, law). For a 2D Tscan, it will be (dataframe, column), for a 3D Tscan, it will be (dataframe, plane, column)

(onde_ut_cscan_dataset-reference_trajectory)=
### `REFERENCE_TRAJECTORY`

*No detailed description provided.*

(onde_ut_cscan_dataset-gates)=
### `GATES`

*No detailed description provided.*
