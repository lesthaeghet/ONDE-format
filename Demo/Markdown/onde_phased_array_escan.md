---
onde_class: ONDE_PHASED_ARRAY_ESCAN
inherits:
- ONDE_PHASED_ARRAY_SETUP
fields:
- full_name: ONDE:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '[2]'
  allowed_values: '["ONDE_PHASED_ARRAY_SETUP","ONDE_PHASED_ARRAY_ESCAN"]'
- full_name: ONDE_PHASED_ARRAY_ESCAN:NUMBER_OF_ELEMENTS
  short_name: NUMBER_OF_ELEMENTS
  required: true
  storage: attribute
  hdf5_type: H5T_INTEGER
  description: ''
  dimensions: '1'
- full_name: ONDE_PHASED_ARRAY_ESCAN:STEP
  short_name: STEP
  required: true
  storage: attribute
  hdf5_type: H5T_INTEGER
  description: ''
  dimensions: '1'
- full_name: ONDE_PHASED_ARRAY_ESCAN:ANGLE
  short_name: ANGLE
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
---

# ONDE_PHASED_ARRAY_ESCAN

No narrative documentation provided for ONDE_PHASED_ARRAY_ESCAN.
