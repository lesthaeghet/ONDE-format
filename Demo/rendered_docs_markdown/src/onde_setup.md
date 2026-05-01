# ONDE_SETUP

### Setup

**Setup**

This group contains references to the geometric setup and ultrasonic setup. The reference to the ultrasonic setup is
compulsory for the A-scan data. For TScans, it is allowed to bypass this ultrasonic setup and have a direct reference to
the phased array setup (in order to store the reconstruction information without storing the information related to the
acquisition).

## Fields

### `TYPE`

- **Full Name:** `ONDE_SETUP:TYPE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Allowed Values:** `["ONDE_SETUP"]`


### `ULTRASONIC_SETUP`

- **Full Name:** `ONDE_SETUP:ULTRASONIC_SETUP`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STD_REF_OBJ<ONDE_ULTRASONIC_SETUP>`
- **Dimensions:** `[1]`

  Mandatory for Ascan sequences

### `PHASED_ARRAY_SETUP`

- **Full Name:** `ONDE_SETUP:PHASED_ARRAY_SETUP`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STD_REF_OBJ<ONDE_PHASED_ARRAY_SETUP>`
- **Dimensions:** `[1]`


### `GEOMETRIC_SETUP`

- **Full Name:** `ONDE_SETUP:GEOMETRIC_SETUP`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STD_REF_OBJ<ONDE_GEOMETRIC_SETUP>`
- **Dimensions:** `[1]`

