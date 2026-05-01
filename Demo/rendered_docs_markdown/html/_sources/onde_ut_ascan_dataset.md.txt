# ONDE_UT_ASCAN_DATASET

**Inherits from:** ONDE_UT_DATASET

### Ascan datasets

Ascan datasets are the entry points for the description of data that is stored as time signals. The MFMC equivalent is '
SEQUENCE', and both names are allowed to ensure compatibility.

To allow continuity with existing HDF5 formats, the DATA field can be either a HDF5 dataset or a reference to a
dataset located in another part of the HDF5 structure.

## Fields

### `TYPE`

- **Full Name:** `ONDE:TYPE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `[2]`
- **Allowed Values:** `["ONDE_UT_DATASET","ONDE_UT_ASCAN_DATASET"]`


### `DATA`

- **Full Name:** `ONDE_UT_ASCAN_DATASET:DATA`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STD_REF_OBJ<data> or HT5_INTEGER or H5T_FLOAT`
- **Dimensions:** `1 or [N_DF<m>,N_Ascan<m>,Ntime<m>]`

  can be either an array or a reference to an array
