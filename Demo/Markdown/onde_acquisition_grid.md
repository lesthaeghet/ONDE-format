---
onde_class: ONDE_ACQUISITION_GRID
inherits:
- ONDE_ACQUISITION_TRAJECTORY
- ONDE_SPATIAL_TRAJECTORY
fields:
- full_name: ONDE:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '[3]'
  allowed_values: '["ONDE_ACQUISITION_TRAJECTORY","ONDE_SPATIAL_TRAJECTORY","ONDE_ACQUISITION_GRID"]'
- full_name: ONDE_ACQUISITION_GRID:REFERENCE_SPECIMEN
  short_name: REFERENCE_SPECIMEN
  required: true
  storage: attribute
  hdf5_type: H5T_STD_REF_OBJ
  description: When defining an acquisition grid, it is necessary to define a reference
    specimen that is either a cylinder or a plane.
  dimensions: '1'
- full_name: ONDE_ACQUISITION_GRID:CYLINDER_DEFINITION
  short_name: CYLINDER_DEFINITION
  required: false
  storage: attribute
  hdf5_type: H5T_STRING
  description: Defines whether the grid is expressed in the inner surface of the cylinder
    or on the outer surface
  allowed_values: '"INNER"|"OUTER"'
- full_name: ONDE_ACQUISITION_GRID:UV_GRID_FRAME
  short_name: UV_GRID_FRAME
  required: false
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: 2D Frame defining the U_GRID and V_GRID directions of the encoding
    in the surface representation of the specimen (X,Y) for planar specimens, (X,THETA)
    for cylindrical specimens. (1,0,) is assumed if missing
  dimensions: '[3]'
- full_name: ONDE_ACQUISITION_GRID:U_GRID_DATA
  short_name: U_GRID_DATA
  required: true
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: The specified values of the first coder at the different positions
  dimensions: '[N_U<m>]'
- full_name: ONDE_ACQUISITION_GRID:V_GRID_DATA
  short_name: V_GRID_DATA
  required: false
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: The specified values of the second coder at the different positions.
    If missing while U_GRID_DATA is present, 1D array of data is assumed.
  dimensions: '[N_V<m>]'
- full_name: ONDE_ACQUISITION_GRID:SCAN_TYPE
  short_name: SCAN_TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: Defines whether the data is ordered in the same direction for each
    scan (COMB) or is inversed every second scan (RASTER)
  dimensions: '1'
  allowed_values: '"COMB"|"RASTER"'
- full_name: ONDE_ACQUISITION_GRID:U_ENCODER
  short_name: U_ENCODER
  required: false
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: Obtained encoder values on the u axis
  dimensions: '[N_V<m>,N_U<m>]'
- full_name: ONDE_ACQUISITION_GRID:V_ENCODER
  short_name: V_ENCODER
  required: false
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: Obtained encoder values on the v axis
  dimensions: '[N_V<m>,N_U<m>]'
- full_name: ONDE_ACQUISITION_GRID:PROBE_DIRECTION
  short_name: PROBE_DIRECTION
  required: false
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: For grid data, direction of the probe in the (u,v,w) coordinate system.
    Defaults to identity matrix.
  dimensions: '[3,3]'
---

# ONDE_ACQUISITION_GRID

No narrative documentation provided for ONDE_ACQUISITION_GRID.
