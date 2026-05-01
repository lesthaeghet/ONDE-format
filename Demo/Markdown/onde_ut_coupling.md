---
onde_class: ONDE_UT_COUPLING
inherits: []
fields:
- full_name: ONDE:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '[1]'
  allowed_values: '["ONDE_UT_COUPLING"]'
- full_name: ONDE_UT_COUPLING:MEDIUM_VELOCITY
  short_name: MEDIUM_VELOCITY
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '[2]'
- full_name: ONDE_UT_COUPLING:MEDIUM_DENSITY
  short_name: MEDIUM_DENSITY
  required: false
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_UT_COUPLING:INCIDENCE_ANGLE
  short_name: INCIDENCE_ANGLE
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
---

# ONDE_UT_COUPLING

No narrative documentation provided for ONDE_UT_COUPLING.
