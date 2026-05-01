# ONDE_DUAL_WEDGE

**Inherits from:** ONDE_UT_COUPLING, ONDE_WEDGE

No narrative documentation provided for ONDE_DUAL_WEDGE.

## Fields

### `TYPE`

- **Full Name:** `ONDE:TYPE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `[3]`
- **Allowed Values:** `["ONDE_UT_COUPLING","ONDE_WEDGE","ONDE_DUAL_WEDGE"]`


### `PROBE_SEPARATION`

- **Full Name:** `ONDE_DUAL_WEDGE:PROBE_SEPARATION`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`

  For dual probes, inter-probes distance (L6) (See Figure 15)

### `ROOF_ANGLE`

- **Full Name:** `ONDE_DUAL_WEDGE:ROOF_ANGLE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`

  For dual probes and only for dual probes defines the roof angle (See Figure 15)

### `SQUINT_ANGLE`

- **Full Name:** `ONDE_DUAL_WEDGE:SQUINT_ANGLE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`

  For dual probes, squint angle (A2) (See Figure 15)
