---
onde_class: ONDE_PHASED_ARRAY_SSCAN
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
  allowed_values: '["ONDE_PHASED_ARRAY_SETUP","ONDE_PHASED_ARRAY_SSCAN"]'
- full_name: ONDE_PHASED_ARRAY_SSCAN:STARTING_ANGLE
  short_name: STARTING_ANGLE
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_PHASED_ARRAY_SSCAN:FINISHING_ANGLE
  short_name: FINISHING_ANGLE
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_PHASED_ARRAY_SSCAN:NUMBER_OF_ANGLES
  short_name: NUMBER_OF_ANGLES
  required: true
  storage: attribute
  hdf5_type: H5T_INTEGER
  description: ''
  dimensions: '1'
---

# ONDE_PHASED_ARRAY_SSCAN

No narrative documentation provided for ONDE_PHASED_ARRAY_SSCAN.
