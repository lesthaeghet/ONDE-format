---
onde_class: ONDE_TIME_TRAJECTORY
inherits:
- ONDE_ACQUISITION_TRAJECTORY
fields:
- full_name: ONDE:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '[2]'
  allowed_values: '["ONDE_ACQUISITION_TRAJECTORY","ONDE_TIME_TRAJECTORY"]'
- full_name: ONDE_TIME_TRAJECTORY:ACQUISITION_RATE
  short_name: ACQUISITION_RATE
  required: false
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: For time encoded trajectories, defines the acquisition rate
  dimensions: '1'
---

# ONDE_TIME_TRAJECTORY

No narrative documentation provided for ONDE_TIME_TRAJECTORY.
