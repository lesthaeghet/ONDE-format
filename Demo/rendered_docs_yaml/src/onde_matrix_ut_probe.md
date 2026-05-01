# ONDE_MATRIX_UT_PROBE

**Inherits from:** ONDE_UT_PROBE

```{mermaid}
classDiagram
  ONDE_UT_PROBE <|-- ONDE_MATRIX_UT_PROBE
  click ONDE_UT_PROBE href "onde_ut_probe.html"
  click ONDE_MATRIX_UT_PROBE href "onde_matrix_ut_probe.html"
```

No narrative documentation provided for ONDE_MATRIX_UT_PROBE.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_matrix_ut_probe-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[2]` | `["ONDE_UT_PROBE","ONDE_MATRIX_UT_PROBE"]` |  |
| [**`TOTAL_NUMBER_OF_ELEMENTS`**](#onde_matrix_ut_probe-total_number_of_elements)<br><sub>`ONDE_MATRIX_UT_PROBE:TOTAL_NUMBER_OF_ELEMENTS`</sub> | Mandatory | attribute | H5T_INTEGER | `1` | `` |  |
| [**`NUMBER_OF_ELEMENTS_DIM_MINOR`**](#onde_matrix_ut_probe-number_of_elements_dim_minor)<br><sub>`ONDE_MATRIX_UT_PROBE:NUMBER_OF_ELEMENTS_DIM_MINOR`</sub> | Mandatory | attribute | H5T_INTEGER | `1` | `` |  |
| [**`ELEMENT_DIM_MAJOR`**](#onde_matrix_ut_probe-element_dim_major)<br><sub>`ONDE_MATRIX_UT_PROBE:ELEMENT_DIM_MAJOR`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`ELEMENT_DIM_MINOR`**](#onde_matrix_ut_probe-element_dim_minor)<br><sub>`ONDE_MATRIX_UT_PROBE:ELEMENT_DIM_MINOR`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`ELEMENT_PITCH_DIM_MAJOR`**](#onde_matrix_ut_probe-element_pitch_dim_major)<br><sub>`ONDE_MATRIX_UT_PROBE:ELEMENT_PITCH_DIM_MAJOR`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`ELEMENT_PITCH_DIM_MINOR`**](#onde_matrix_ut_probe-element_pitch_dim_minor)<br><sub>`ONDE_MATRIX_UT_PROBE:ELEMENT_PITCH_DIM_MINOR`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`ELEMENT_NUMBERING`**](#onde_matrix_ut_probe-element_numbering)<br><sub>`ONDE_MATRIX_UT_PROBE:ELEMENT_NUMBERING`</sub> | Optional |  |  | `` | `` | Defines the element numbering relating the numbering implicitly defined by the probe description and the order defined in the element tables (ELEMENT_POSITION, ELEMENT_GEOMETRY, etc |


## Field Details

(onde_matrix_ut_probe-type)=
### `TYPE`

*No detailed description provided.*

(onde_matrix_ut_probe-total_number_of_elements)=
### `TOTAL_NUMBER_OF_ELEMENTS`

*No detailed description provided.*

(onde_matrix_ut_probe-number_of_elements_dim_minor)=
### `NUMBER_OF_ELEMENTS_DIM_MINOR`

*No detailed description provided.*

(onde_matrix_ut_probe-element_dim_major)=
### `ELEMENT_DIM_MAJOR`

*No detailed description provided.*

(onde_matrix_ut_probe-element_dim_minor)=
### `ELEMENT_DIM_MINOR`

*No detailed description provided.*

(onde_matrix_ut_probe-element_pitch_dim_major)=
### `ELEMENT_PITCH_DIM_MAJOR`

*No detailed description provided.*

(onde_matrix_ut_probe-element_pitch_dim_minor)=
### `ELEMENT_PITCH_DIM_MINOR`

*No detailed description provided.*

(onde_matrix_ut_probe-element_numbering)=
### `ELEMENT_NUMBERING`

Defines the element numbering relating the numbering implicitly defined by the probe description and the order defined in the element tables (ELEMENT_POSITION, ELEMENT_GEOMETRY, etc
