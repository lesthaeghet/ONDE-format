---
onde_class: ONDE_UT_CSCAN_DATASET
inherits:
- ONDE_UT_DATASET
fields:
- full_name: ONDE:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '[2]'
  allowed_values: '["ONDE_UT_DATASET","ONDE_UT_CSCAN_DATASET"]'
- full_name: ONDE_UT_CSCAN_DATASET:DATA
  short_name: DATA
  required: true
  storage: dataset
  hdf5_type: H5T_STD_REF_OBJ or HT5_INTEGER
  description: references to arrays containing the different values stored in the
    dataset
  dimensions: '[N_CS<m>] |[N_CS<m>,N_Gate<m>]'
- full_name: ONDE_UT_CSCAN_DATASET:DATATYPE
  short_name: DATATYPE
  required: true
  storage: dataset
  hdf5_type: H5T_STRING
  description: 'string defining the stored data - the name can be either custom  (MY_MATERIAL_PROPERTY
    for instance) or a standardized name : THICKNESS, TIME_OF_FLIGHT, DEPTH, AMAX'
  dimensions: '[N_CS<m>]'
- full_name: ONDE_UT_CSCAN_DATASET:UNDERLYING_DATA
  short_name: UNDERLYING_DATA
  required: false
  storage: attribute
  hdf5_type: H5T_STD_REF_OBJ<ONDE_UT_ASCAN_DATASET> or H5T_STD_REF_OBJ<ONDE_UT_TSCAN_DATASET>
  description: reference to the dataset containing the underlying data
  dimensions: '1'
- full_name: ONDE_UT_CSCAN_DATASET:UNDERLYING_DATA_REFERENCE
  short_name: UNDERLYING_DATA_REFERENCE
  required: false
  storage: dataset
  hdf5_type: H5T_INTEGER
  description: Correspondancy between the C-Scan scalar data and the scan originating.
    For a A-Scan, the scan is expressed in terms of (dataframe, law). For a 2D Tscan,
    it will be (dataframe, column), for a 3D Tscan, it will be (dataframe, plane,
    column)
  dimensions: '[N_DF<m>,2] or [N_DF<m>,3]'
- full_name: ONDE_UT_CSCAN_DATASET:REFERENCE_TRAJECTORY
  short_name: REFERENCE_TRAJECTORY
  required: true
  storage: attribute
  hdf5_type: H5T_STD_REF_OBJ
  description: ''
  ref_target: ONDE_ACQUISITION_TRAJECTORY
  dimensions: '1'
- full_name: ONDE_UT_CSCAN_DATASET:GATES
  short_name: GATES
  required: false
  storage: dataset
  hdf5_type: H5T_STD_REF_OBJ
  description: ''
  ref_target: ONDE_UT_GATE
  dimensions: '[N_Gate<m>]'
---

# ONDE_UT_CSCAN_DATASET

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
