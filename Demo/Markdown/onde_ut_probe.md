---
onde_class: ONDE_UT_PROBE
inherits: []
fields:
- full_name: ONDE:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '[1]'
  allowed_values: '["ONDE_UT_PROBE"]'
- full_name: ONDE:TYPE_TAGS
  short_name: TYPE_TAGS
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '[1]'
  allowed_values: '["ONDE_UT_ELEMENTS"]'
- full_name: ONDE:LABEL
  short_name: LABEL
  required: false
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '1'
- full_name: ONDE_UT_PROBE:INDEX_POINT_FRAME
  short_name: INDEX_POINT_FRAME
  required: false
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: If absent, identity is assumed
  dimensions: '[7]'
- full_name: ONDE_UT_PROBE:MANUFACTURER
  short_name: MANUFACTURER
  required: false
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '1'
- full_name: ONDE_UT_PROBE:SERIAL_NUMBER
  short_name: SERIAL_NUMBER
  required: false
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '1'
- full_name: ONDE_UT_PROBE:FREQUENCY
  short_name: FREQUENCY
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_UT_PROBE:BANDWIDTH
  short_name: BANDWIDTH
  required: false
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '1'
- full_name: ONDE_UT_PROBE:FOCUSING_SURFACE
  short_name: FOCUSING_SURFACE
  required: false
  storage: attribute
  hdf5_type: H5T_INTEGER
  description: Defines the shape of the surface on which the elements are arranged
    - if absent, FLAT is assumed
  allowed_values: '"FLAT"|"CYLINDRICAL_INC"|"CYLINDRICAL_PERP"|"SPHERICAL"|"BIFOCAL"|"TRIFOCAL"'
- full_name: ONDE_UT_PROBE:FOCUSING_SURFACE_PARAMETERS
  short_name: FOCUSING_SURFACE_PARAMETERS
  required: false
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: 'Multi values : value in mm - FLAT : no value - CYLINDRICAL_INC, CYLINDRICAL_PER
    : Surface radius - SPHERICAL : Surface radius - BIFOCAL : Surface radius in the
    incidence plane, surface radius in the plane perpendicular to the incidence plane
    - TRIFOCAL : Surface radius in the incidence plane (bottom), Surface radius in
    the incidence plane (top), surface radius in the plane perpendicular to the incidence
    plane.'
  dimensions: '[3]'
- full_name: ONDE_UT_PROBE:COUPLING
  short_name: COUPLING
  required: true
  storage: attribute
  hdf5_type: H5T_STD_REF_OBJ
  description: Reference to the coupling system (wedge, immersion, direct)
  ref_target: ONDE_UT_COUPLING
  dimensions: '1'
---

# ONDE_UT_PROBE

No narrative documentation provided for ONDE_UT_PROBE.
