---
onde_class: ONDE_CYLINDER
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
  allowed_values: '["ONDE_COMPONENT","ONDE_CYLINDER"]'
- full_name: ONDE_CYLINDER:DIMENSIONS
  short_name: DIMENSIONS
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '[3]'
---

# ONDE_CYLINDER

No narrative documentation provided for ONDE_CYLINDER.
