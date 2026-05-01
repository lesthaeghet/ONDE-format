# ONDE_UT_ELEMENTS

No narrative documentation provided for ONDE_UT_ELEMENTS.

## Fields

### `TYPE_TAGS`

- **Full Name:** `ONDE:TYPE_TAGS`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `[1]`
- **Allowed Values:** `["ONDE_UT_ELEMENTS"]`

  Defines the ONDE_UT_ELEMENTS accessory class

### `FRAME`

- **Full Name:** `ONDE_UT_ELEMENTS:FRAME`
- **Requirement:** Mandatory
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_Elem<p>,7]`

  Array defining the location of the elements of the probe

### `SHAPE`

- **Full Name:** `ONDE_UT_ELEMENTS:SHAPE`
- **Requirement:** Mandatory
- **Storage:** dataset
- **Type:** `H5T_INTEGER`
- **Dimensions:** `[N_Elem<p>]`

  The shape of each element will be defined as one of the following: rectangle (ELE_GEOM_REC), part of a ring (ELE_GEOM_RING_PART), part of an elliptical ring (ELE_GEOM_ELLIPSE_PART),

### `SIZE`

- **Full Name:** `ONDE_UT_ELEMENTS:SIZE`
- **Requirement:** Mandatory
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_Elem<p>,6]`


### `RADIUS_OF_CURVATURE`

- **Full Name:** `ONDE_UT_ELEMENTS:RADIUS_OF_CURVATURE`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_Elem<p>]`

  If absent, flat elements are assumed

### `AXIS_OF_CURVATURE`

- **Full Name:** `ONDE_UT_ELEMENTS:AXIS_OF_CURVATURE`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_Elem<p>,3]`

  If absent, flat elements are assumed

### `DEAD_ELEMENT`

- **Full Name:** `ONDE_UT_ELEMENTS:DEAD_ELEMENT`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_INTEGER`
- **Dimensions:** `[N_Elem<p>]`

  Datafield of logical values (0 = false, 1 = true) used to flag non-functioning elements in an array probe (if not present, assumption should be that all elements are performing correctly);
