---
onde_class: ONDE_UT_GATE
inherits: []
fields:
- full_name: ONDE:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '[1]'
  allowed_values: '["ONDE_UT_GATE"]'
- full_name: ONDE_UT_GATE:START
  short_name: START
  required: false
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: For scalar data relying on Ascan data, defines the start time for the
    gate. Mandatory for data related to Ascans.
  dimensions: '1'
- full_name: ONDE_UT_GATE:WIDTH
  short_name: WIDTH
  required: false
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: For Cscans scalar data relying on Ascan data, defines the width of
    the gate. Mandatory for data related to Ascans
  dimensions: '1'
- full_name: ONDE_UT_GATE:THRESHOLD
  short_name: THRESHOLD
  required: false
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: Defines the threshold of the gate for data to be stored
  dimensions: '1'
- full_name: ONDE_UT_GATE:DETECTION
  short_name: DETECTION
  required: false
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '1'
  allowed_values: '" FIRST_PEAK"|"LAST_PEAK"|" MAX_PEAK"|" FIRST_FLANK"|"LAST_FLANK"'
---

# ONDE_UT_GATE

No narrative documentation provided for ONDE_UT_GATE.
