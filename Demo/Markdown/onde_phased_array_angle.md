---
onde_class: ONDE_PHASED_ARRAY_ANGLE
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
  allowed_values: '["ONDE_PHASED_ARRAY_SETUP","ONDE_PHASED_ARRAY_ANGLE"]'
- full_name: ONDE_PHASED_ARRAY_ANGLE:BSCAN_ANGLE
  short_name: BSCAN_ANGLE
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
---

# ONDE_PHASED_ARRAY_ANGLE

No narrative documentation provided for ONDE_PHASED_ARRAY_ANGLE.
