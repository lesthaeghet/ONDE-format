# ONDE_LINEAR_UT_PROBE

**Inherits from:** ONDE_UT_PROBE

No narrative documentation provided for ONDE_LINEAR_UT_PROBE.

## Fields

### `TYPE`

- **Full Name:** `ONDE:TYPE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `[2]`
- **Allowed Values:** `["ONDE_UT_PROBE","ONDE_LINEAR_UT_PROBE"]`


### `TOTAL_NUMBER_OF_ELEMENTS`

- **Full Name:** `ONDE_LINEAR_UT_PROBE:TOTAL_NUMBER_OF_ELEMENTS`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_INTEGER`
- **Dimensions:** `1`


### `ELEMENT_DIM_MAJOR`

- **Full Name:** `ONDE_LINEAR_UT_PROBE:ELEMENT_DIM_MAJOR`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`


### `ELEMENT_DIM_MINOR`

- **Full Name:** `ONDE_LINEAR_UT_PROBE:ELEMENT_DIM_MINOR`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`


### `ELEMENT_PITCH_DIM_MAJOR`

- **Full Name:** `ONDE_LINEAR_UT_PROBE:ELEMENT_PITCH_DIM_MAJOR`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`


### `ELEMENT_NUMBERING`

- **Full Name:** `ONDE_LINEAR_UT_PROBE:ELEMENT_NUMBERING`
- **Requirement:** Optional
- **Storage:** 
- **Type:** ``

  Defines the element numbering relating the numbering implicitly defined by the probe description and the order defined in the element tables (ELEMENT_POSITION, ELEMENT_GEOMETRY, etc
