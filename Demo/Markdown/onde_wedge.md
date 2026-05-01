---
onde_class: ONDE_WEDGE
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
  allowed_values: '["ONDE_UT_COUPLING","ONDE_WEDGE"]'
- full_name: ONDE:LABEL
  short_name: LABEL
  required: false
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '1'
- full_name: ONDE_WEDGE:MANUFACTURER
  short_name: MANUFACTURER
  required: false
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '1'
- full_name: ONDE_WEDGE:SERIAL_NUMBER
  short_name: SERIAL_NUMBER
  required: false
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '1'
- full_name: ONDE_WEDGE:CONTACT_SURFACE
  short_name: CONTACT_SURFACE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: Type of the wedge contact surface - PLANAR, SPHERICAL, CYLINDRICAL_MAJOR,
    CYLINDRICAL_MINOR - If missing PLANAR assumed
  allowed_values: '"PLANAR"|"SPHERICAL"|"CYLINDRICAL_MAJOR"|"CYLINDRICAL_MINOR"'
- full_name: ONDE_WEDGE:CURVATURE_RADIUS
  short_name: CURVATURE_RADIUS
  required: false
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: 'Wedge curvature radius - Concave : positive - Convex : negative -
    0 in the case of a planar wedge - If missing 0 assumed.'
  dimensions: '1'
- full_name: ONDE_WEDGE:CONTACT_AREA
  short_name: CONTACT_AREA
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: Equivalent to L1, L2 and L3 (See Figure 15)
  dimensions: '[3]'
- full_name: ONDE_WEDGE:HEIGHT
  short_name: HEIGHT
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: For a wedge, distance of the ultrasonic beam between the probe center
    and the index point (See Figure 15)
  dimensions: '1'
- full_name: ONDE_WEDGE:SKEW_ANGLE
  short_name: SKEW_ANGLE
  required: false
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: wedge /skew angle (B) (See Figure 15)
  dimensions: '1'
- full_name: ONDE_WEDGE:DISORIENTATION_ANGLE
  short_name: DISORIENTATION_ANGLE
  required: false
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: wedge /disorientation angle (D) (See Figure 15)
  dimensions: '1'
---

# ONDE_WEDGE

No narrative documentation provided for ONDE_WEDGE.
