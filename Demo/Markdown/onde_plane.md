---
onde_class: ONDE_PLANE
inherits:
- ONDE_COMPONENT
fields:
- full_name: ONDE:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '[2]'
  allowed_values: '["ONDE_COMPONENT","ONDE_PLANE"]'
- full_name: ONDE_PLANE:PLATE_DIMENSIONS
  short_name: PLATE_DIMENSIONS
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '[3]'
---

# ONDE_PLANE

No narrative documentation provided for ONDE_PLANE.
