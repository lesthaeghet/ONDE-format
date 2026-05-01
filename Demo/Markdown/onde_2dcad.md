---
onde_class: ONDE_2DCAD
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
  allowed_values: '["ONDE_COMPONENT","ONDE_2DCAD"]'
- full_name: ONDE_2DCAD:EXTRUSION_TYPE
  short_name: EXTRUSION_TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '1'
  allowed_values: '"PLANE" |"CYLINDER"'
- full_name: ONDE_2DCAD:EXTRUSION_DIMENSION
  short_name: EXTRUSION_DIMENSION
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_2DCAD:CAD
  short_name: CAD
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '1'
---

# ONDE_2DCAD

No narrative documentation provided for ONDE_2DCAD.
