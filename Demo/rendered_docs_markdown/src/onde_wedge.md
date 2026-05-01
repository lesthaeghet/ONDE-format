# ONDE_WEDGE

**Inherits from:** ONDE_UT_COUPLING

No narrative documentation provided for ONDE_WEDGE.

## Fields

### `TYPE`

- **Full Name:** `ONDE:TYPE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `[2]`
- **Allowed Values:** `["ONDE_UT_COUPLING","ONDE_WEDGE"]`


### `LABEL`

- **Full Name:** `ONDE:LABEL`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `1`


### `MANUFACTURER`

- **Full Name:** `ONDE_WEDGE:MANUFACTURER`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `1`


### `SERIAL_NUMBER`

- **Full Name:** `ONDE_WEDGE:SERIAL_NUMBER`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `1`


### `CONTACT_SURFACE`

- **Full Name:** `ONDE_WEDGE:CONTACT_SURFACE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Allowed Values:** `"PLANAR"|"SPHERICAL"|"CYLINDRICAL_MAJOR"|"CYLINDRICAL_MINOR"`

  Type of the wedge contact surface - PLANAR, SPHERICAL, CYLINDRICAL_MAJOR, CYLINDRICAL_MINOR - If missing PLANAR assumed

### `CURVATURE_RADIUS`

- **Full Name:** `ONDE_WEDGE:CURVATURE_RADIUS`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`

  Wedge curvature radius - Concave : positive - Convex : negative - 0 in the case of a planar wedge - If missing 0 assumed.

### `CONTACT_AREA`

- **Full Name:** `ONDE_WEDGE:CONTACT_AREA`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[3]`

  Equivalent to L1, L2 and L3 (See Figure 15)

### `HEIGHT`

- **Full Name:** `ONDE_WEDGE:HEIGHT`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`

  For a wedge, distance of the ultrasonic beam between the probe center and the index point (See Figure 15)

### `SKEW_ANGLE`

- **Full Name:** `ONDE_WEDGE:SKEW_ANGLE`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`

  wedge /skew angle (B) (See Figure 15)

### `DISORIENTATION_ANGLE`

- **Full Name:** `ONDE_WEDGE:DISORIENTATION_ANGLE`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`

  wedge /disorientation angle (D) (See Figure 15)
