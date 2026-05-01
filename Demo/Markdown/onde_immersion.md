---
onde_class: ONDE_IMMERSION
inherits:
- ONDE_UT_COUPLING
fields:
- full_name: ONDE:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '[2]'
  allowed_values: '["ONDE_UT_COUPLING","ONDE_IMMERSION"]'
- full_name: ONDE_IMMERSION:WATER_PATH
  short_name: WATER_PATH
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
---

# ONDE_IMMERSION

No narrative documentation provided for ONDE_IMMERSION.
