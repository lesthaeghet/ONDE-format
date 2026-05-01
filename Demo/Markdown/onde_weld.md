---
onde_class: ONDE_WELD
inherits:
- ONDE_COMPONENT
fields:
- full_name: ONDE_WELD:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '[2]'
  allowed_values: '["ONDE_COMPONENT","ONDE_WELD"]'
- full_name: ONDE_WELD:EXTRUSION_TYPE
  short_name: EXTRUSION_TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '1'
  allowed_values: '"PLANE" |"CYLINDER"'
- full_name: ONDE_WELD:EXTRUSION_DIMENSION
  short_name: EXTRUSION_DIMENSION
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_WELD:WELD_TYPE
  short_name: WELD_TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '1'
  allowed_values: '"V"|"U"'
- full_name: ONDE_WELD:WELD_SYMMETRY
  short_name: WELD_SYMMETRY
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '1'
  allowed_values: '"SYMMETRIC"|"STRAIGHT_LEFT"|"STRAIGHT_RIGHT"'
- full_name: ONDE_WELD:WELD_UPPER_CAP_WIDTH
  short_name: WELD_UPPER_CAP_WIDTH
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_WELD:WELD_UPPER_CAP_HEIGHT
  short_name: WELD_UPPER_CAP_HEIGHT
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_WELD:WELD_FILL_ANGLE
  short_name: WELD_FILL_ANGLE
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_WELD:WELD_FILL_HEIGHT
  short_name: WELD_FILL_HEIGHT
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_WELD:WELD_HOT_PASS_ANGLE
  short_name: WELD_HOT_PASS_ANGLE
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_WELD:WELD_HOT_PASS_HEIGHT
  short_name: WELD_HOT_PASS_HEIGHT
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_WELD:WELD_LAND_OFFSET
  short_name: WELD_LAND_OFFSET
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_WELD:WELD_LAND_HEIGHT
  short_name: WELD_LAND_HEIGHT
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_WELD:WELD_ROOT_ANGLE
  short_name: WELD_ROOT_ANGLE
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_WELD:WELD_ROOT_HEIGHT
  short_name: WELD_ROOT_HEIGHT
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_WELD:WELD_LOWER_CAP_HEIGHT
  short_name: WELD_LOWER_CAP_HEIGHT
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_WELD:WELD_LOWER_CAP_WIDTH
  short_name: WELD_LOWER_CAP_WIDTH
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_WELD:WELD_HAZ_WIDTH
  short_name: WELD_HAZ_WIDTH
  required: false
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
---

# ONDE_WELD

No narrative documentation provided for ONDE_WELD.
