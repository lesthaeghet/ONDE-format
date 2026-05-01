---
onde_class: ONDE_PHASED_ARRAY_COMPOUND
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
  allowed_values: '["ONDE_PHASED_ARRAY_SETUP","ONDE_PHASED_ARRAY_COMPOUND"]'
- full_name: ONDE_PHASED_ARRAY_COMPOUND:INITIAL_ANGLE
  short_name: INITIAL_ANGLE
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_PHASED_ARRAY_COMPOUND:FINAL_ANGLE
  short_name: FINAL_ANGLE
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_PHASED_ARRAY_COMPOUND:NUMBER_OF_ANGLES
  short_name: NUMBER_OF_ANGLES
  required: true
  storage: attribute
  hdf5_type: H5T_INTEGER
  description: ''
  dimensions: '1'
- full_name: ONDE_PHASED_ARRAY_COMPOUND:NUMBER_OF_ELEMENTS
  short_name: NUMBER_OF_ELEMENTS
  required: true
  storage: attribute
  hdf5_type: H5T_INTEGER
  description: ''
  dimensions: '1'
---

# ONDE_PHASED_ARRAY_COMPOUND

No narrative documentation provided for ONDE_PHASED_ARRAY_COMPOUND.
