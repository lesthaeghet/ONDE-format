---
onde_class: ONDE_UT_ELEMENTS
inherits: []
fields:
- full_name: ONDE:TYPE_TAGS
  short_name: TYPE_TAGS
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: Defines the ONDE_UT_ELEMENTS accessory class
  dimensions: '[1]'
  allowed_values: '["ONDE_UT_ELEMENTS"]'
- full_name: ONDE_UT_ELEMENTS:FRAME
  short_name: FRAME
  required: true
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: Array defining the location of the elements of the probe
  dimensions: '[N_Elem<p>,7]'
- full_name: ONDE_UT_ELEMENTS:SHAPE
  short_name: SHAPE
  required: true
  storage: dataset
  hdf5_type: H5T_INTEGER
  description: 'The shape of each element will be defined as one of the following:
    rectangle (ELE_GEOM_REC), part of a ring (ELE_GEOM_RING_PART), part of an elliptical
    ring (ELE_GEOM_ELLIPSE_PART),'
  dimensions: '[N_Elem<p>]'
- full_name: ONDE_UT_ELEMENTS:SIZE
  short_name: SIZE
  required: true
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: ''
  dimensions: '[N_Elem<p>,6]'
- full_name: ONDE_UT_ELEMENTS:RADIUS_OF_CURVATURE
  short_name: RADIUS_OF_CURVATURE
  required: false
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: If absent, flat elements are assumed
  dimensions: '[N_Elem<p>]'
- full_name: ONDE_UT_ELEMENTS:AXIS_OF_CURVATURE
  short_name: AXIS_OF_CURVATURE
  required: false
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: If absent, flat elements are assumed
  dimensions: '[N_Elem<p>,3]'
- full_name: ONDE_UT_ELEMENTS:DEAD_ELEMENT
  short_name: DEAD_ELEMENT
  required: false
  storage: dataset
  hdf5_type: H5T_INTEGER
  description: Datafield of logical values (0 = false, 1 = true) used to flag non-functioning
    elements in an array probe (if not present, assumption should be that all elements
    are performing correctly);
  dimensions: '[N_Elem<p>]'
---

# ONDE_UT_ELEMENTS

No narrative documentation provided for ONDE_UT_ELEMENTS.
