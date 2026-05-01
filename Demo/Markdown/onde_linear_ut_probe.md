---
onde_class: ONDE_LINEAR_UT_PROBE
inherits:
- ONDE_UT_PROBE
fields:
- full_name: ONDE:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '[2]'
  allowed_values: '["ONDE_UT_PROBE","ONDE_LINEAR_UT_PROBE"]'
- full_name: ONDE_LINEAR_UT_PROBE:TOTAL_NUMBER_OF_ELEMENTS
  short_name: TOTAL_NUMBER_OF_ELEMENTS
  required: true
  storage: attribute
  hdf5_type: H5T_INTEGER
  description: ''
  dimensions: '1'
- full_name: ONDE_LINEAR_UT_PROBE:ELEMENT_DIM_MAJOR
  short_name: ELEMENT_DIM_MAJOR
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_LINEAR_UT_PROBE:ELEMENT_DIM_MINOR
  short_name: ELEMENT_DIM_MINOR
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_LINEAR_UT_PROBE:ELEMENT_PITCH_DIM_MAJOR
  short_name: ELEMENT_PITCH_DIM_MAJOR
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_LINEAR_UT_PROBE:ELEMENT_NUMBERING
  short_name: ELEMENT_NUMBERING
  required: false
  storage: ''
  hdf5_type: ''
  description: Defines the element numbering relating the numbering implicitly defined
    by the probe description and the order defined in the element tables (ELEMENT_POSITION,
    ELEMENT_GEOMETRY, etc
---

# ONDE_LINEAR_UT_PROBE

No narrative documentation provided for ONDE_LINEAR_UT_PROBE.
