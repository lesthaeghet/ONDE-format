---
onde_class: ROOT
inherits: []
fields:
- full_name: ONDE:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: For detailed information, see https://github.com/COFREND/ONDE-format/blob/main/UT_specification/UT_file_format.md
  dimensions: '1'
  allowed_values: '["ONDE_UT"]'
- full_name: ONDE:VERSION
  short_name: VERSION
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '1'
  allowed_values: '"0.4.0"'
---

# ROOT

Root level fields for ONDE format.