# ONDE_UT_GATE

No narrative documentation provided for ONDE_UT_GATE.

## Fields

### `TYPE`

- **Full Name:** `ONDE:TYPE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `[1]`
- **Allowed Values:** `["ONDE_UT_GATE"]`


### `START`

- **Full Name:** `ONDE_UT_GATE:START`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`

  For scalar data relying on Ascan data, defines the start time for the gate. Mandatory for data related to Ascans.

### `WIDTH`

- **Full Name:** `ONDE_UT_GATE:WIDTH`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`

  For Cscans scalar data relying on Ascan data, defines the width of the gate. Mandatory for data related to Ascans

### `THRESHOLD`

- **Full Name:** `ONDE_UT_GATE:THRESHOLD`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`

  Defines the threshold of the gate for data to be stored

### `DETECTION`

- **Full Name:** `ONDE_UT_GATE:DETECTION`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `1`
- **Allowed Values:** `" FIRST_PEAK"|"LAST_PEAK"|" MAX_PEAK"|" FIRST_FLANK"|"LAST_FLANK"`

