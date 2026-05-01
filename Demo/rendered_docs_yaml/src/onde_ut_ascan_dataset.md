# ONDE_UT_ASCAN_DATASET

**Inherits from:** ONDE_UT_DATASET

```{mermaid}
classDiagram
  ONDE_UT_DATASET <|-- ONDE_UT_ASCAN_DATASET
  click ONDE_UT_DATASET href "onde_ut_dataset.html"
  click ONDE_UT_ASCAN_DATASET href "onde_ut_ascan_dataset.html"
```

### Ascan datasets

Ascan datasets are the entry points for the description of data that is stored as time signals. The MFMC equivalent is '
SEQUENCE', and both names are allowed to ensure compatibility.

To allow continuity with existing HDF5 formats, the DATA field can be either a HDF5 dataset or a reference to a
dataset located in another part of the HDF5 structure.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_ut_ascan_dataset-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[2]` | `["ONDE_UT_DATASET","ONDE_UT_ASCAN_DATASET"]` |  |
| [**`DATA`**](#onde_ut_ascan_dataset-data)<br><sub>`ONDE_UT_ASCAN_DATASET:DATA`</sub> | Mandatory | attribute | H5T_STD_REF_OBJ<data> or HT5_INTEGER or H5T_FLOAT | `1 or [N_DF<m>,N_Ascan<m>,Ntime<m>]` | `` | can be either an array or a reference to an array |


## Field Details

(onde_ut_ascan_dataset-type)=
### `TYPE`

*No detailed description provided.*

(onde_ut_ascan_dataset-data)=
### `DATA`

can be either an array or a reference to an array
