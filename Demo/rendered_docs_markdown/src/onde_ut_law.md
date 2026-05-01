# ONDE_UT_LAW

### Law

For multielements, these groups describe the settings of a given transmit or receive law. PROBE and ELEMENT give the
probe and element number to which the DELAY and WEIGHTING apply.

The format also allows to store an information about the corresponding ultrasonic path.

PROPAGATION_LINE represents the ultrasonic ray along which the data is to be represented in a true visualisation. It
contains at least two points in the Probe Coordinates Frame corresponding to the start and end of the ray. (x,y,z)
positions in Probe Coordinate Frame and time of flight are stored.

## Fields

### `TYPE`

- **Full Name:** `ONDE:TYPE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Allowed Values:** `["ONDE_UT_LAW"]`


### `PROBE`

- **Full Name:** `ONDE_UT_LAW:PROBE`
- **Requirement:** Mandatory
- **Storage:** dataset
- **Type:** `H5T_STD_REF_OBJ`
- **Dimensions:** `[N_C<k>]`


### `ELEMENT`

- **Full Name:** `ONDE_UT_LAW:ELEMENT`
- **Requirement:** Mandatory
- **Storage:** dataset
- **Type:** `H5T_INTEGER`
- **Dimensions:** `[N_C<k>]`


### `DELAY`

- **Full Name:** `ONDE_UT_LAW:DELAY`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_C<k>]`

  Specifies the relative delay (in ultrasonic time) between the different Probe Element Combinations in the focal law. The default value is zero delay for all Probe Element Combinations.

### `WEIGHTING`

- **Full Name:** `ONDE_UT_LAW:WEIGHTING`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_C<k>]`

  Specifies the weighting between the different Probe Element Combinations in the focal law. The default is one for all Probe Element Combinations.

### `PROPAGATION_LINE`

- **Full Name:** `ONDE_UT_LAW:PROPAGATION_LINE`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_Points<k>,4]`

  Represents the ultrasonic ray along which the data is to be represented in a true visualisation. It contains at least two points in the Probe Coordinates Frame corresponding to the start and end of the ray. (x,y,z) positions in Probe Coordinate Frame and time of flight are stored).
