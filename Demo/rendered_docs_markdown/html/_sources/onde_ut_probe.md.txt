# ONDE_UT_PROBE

No narrative documentation provided for ONDE_UT_PROBE.

## Fields

### `TYPE`

- **Full Name:** `ONDE:TYPE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `[1]`
- **Allowed Values:** `["ONDE_UT_PROBE"]`


### `TYPE_TAGS`

- **Full Name:** `ONDE:TYPE_TAGS`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `[1]`
- **Allowed Values:** `["ONDE_UT_ELEMENTS"]`


### `LABEL`

- **Full Name:** `ONDE:LABEL`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `1`


### `INDEX_POINT_FRAME`

- **Full Name:** `ONDE_UT_PROBE:INDEX_POINT_FRAME`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[7]`

  If absent, identity is assumed

### `MANUFACTURER`

- **Full Name:** `ONDE_UT_PROBE:MANUFACTURER`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `1`


### `SERIAL_NUMBER`

- **Full Name:** `ONDE_UT_PROBE:SERIAL_NUMBER`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `1`


### `FREQUENCY`

- **Full Name:** `ONDE_UT_PROBE:FREQUENCY`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`


### `BANDWIDTH`

- **Full Name:** `ONDE_UT_PROBE:BANDWIDTH`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`


### `FOCUSING_SURFACE`

- **Full Name:** `ONDE_UT_PROBE:FOCUSING_SURFACE`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_INTEGER`
- **Allowed Values:** `"FLAT"|"CYLINDRICAL_INC"|"CYLINDRICAL_PERP"|"SPHERICAL"|"BIFOCAL"|"TRIFOCAL"`

  Defines the shape of the surface on which the elements are arranged - if absent, FLAT is assumed

### `FOCUSING_SURFACE_PARAMETERS`

- **Full Name:** `ONDE_UT_PROBE:FOCUSING_SURFACE_PARAMETERS`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[3]`

  Multi values : value in mm - FLAT : no value - CYLINDRICAL_INC, CYLINDRICAL_PER : Surface radius - SPHERICAL : Surface radius - BIFOCAL : Surface radius in the incidence plane, surface radius in the plane perpendicular to the incidence plane - TRIFOCAL : Surface radius in the incidence plane (bottom), Surface radius in the incidence plane (top), surface radius in the plane perpendicular to the incidence plane.

### `COUPLING`

- **Full Name:** `ONDE_UT_PROBE:COUPLING`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STD_REF_OBJ<ONDE_UT_COUPLING>`
- **Dimensions:** `1`

  Reference to the coupling system (wedge, immersion, direct)
