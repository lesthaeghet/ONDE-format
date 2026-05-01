---
onde_class: ONDE_SPATIAL_TRAJECTORY
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
  allowed_values: '["ONDE_ACQUISITION_TRAJECTORY","ONDE_SPATIAL_TRAJECTORY"]'
- full_name: ONDE_SPATIAL_TRAJECTORY:TRAJECTORY
  short_name: TRAJECTORY
  required: false
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: "List of positions and quaternions \_\_giving the positions and orientations\
    \ of the trajectory frame\_\_\_ at the different positions"
  dimensions: '[N_Pos<m>,7]'
---

# ONDE_SPATIAL_TRAJECTORY

No narrative documentation provided for ONDE_SPATIAL_TRAJECTORY.
