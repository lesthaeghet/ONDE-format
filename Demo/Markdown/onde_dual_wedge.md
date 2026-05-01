---
onde_class: ONDE_DUAL_WEDGE
inherits:
- ONDE_UT_COUPLING
- ONDE_WEDGE
fields:
- full_name: ONDE:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '[3]'
  allowed_values: '["ONDE_UT_COUPLING","ONDE_WEDGE","ONDE_DUAL_WEDGE"]'
- full_name: ONDE_DUAL_WEDGE:PROBE_SEPARATION
  short_name: PROBE_SEPARATION
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: For dual probes, inter-probes distance (L6) (See Figure 15)
  dimensions: '1'
- full_name: ONDE_DUAL_WEDGE:ROOF_ANGLE
  short_name: ROOF_ANGLE
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: For dual probes and only for dual probes defines the roof angle (See
    Figure 15)
  dimensions: '1'
- full_name: ONDE_DUAL_WEDGE:SQUINT_ANGLE
  short_name: SQUINT_ANGLE
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: For dual probes, squint angle (A2) (See Figure 15)
  dimensions: '1'
---

# ONDE_DUAL_WEDGE

No narrative documentation provided for ONDE_DUAL_WEDGE.
