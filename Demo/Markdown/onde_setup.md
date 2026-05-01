---
onde_class: ONDE_SETUP
inherits: []
fields:
- full_name: ONDE_SETUP:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  allowed_values: '["ONDE_SETUP"]'
- full_name: ONDE_SETUP:ULTRASONIC_SETUP
  short_name: ULTRASONIC_SETUP
  required: false
  storage: attribute
  hdf5_type: H5T_STD_REF_OBJ
  description: Mandatory for Ascan sequences
  ref_target: ONDE_ULTRASONIC_SETUP
  dimensions: '[1]'
- full_name: ONDE_SETUP:PHASED_ARRAY_SETUP
  short_name: PHASED_ARRAY_SETUP
  required: false
  storage: attribute
  hdf5_type: H5T_STD_REF_OBJ
  description: ''
  ref_target: ONDE_PHASED_ARRAY_SETUP
  dimensions: '[1]'
- full_name: ONDE_SETUP:GEOMETRIC_SETUP
  short_name: GEOMETRIC_SETUP
  required: true
  storage: attribute
  hdf5_type: H5T_STD_REF_OBJ
  description: ''
  ref_target: ONDE_GEOMETRIC_SETUP
  dimensions: '[1]'
---

# ONDE_SETUP


### Setup

**Setup**

This group contains references to the geometric setup and ultrasonic setup. The reference to the ultrasonic setup is
compulsory for the A-scan data. For TScans, it is allowed to bypass this ultrasonic setup and have a direct reference to
the phased array setup (in order to store the reconstruction information without storing the information related to the
acquisition).