# ONDE_PHASED_ARRAY_COMPOUND

**Inherits from:** ONDE_PHASED_ARRAY_SETUP

```{mermaid}
classDiagram
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_COMPOUND
  click ONDE_PHASED_ARRAY_SETUP href "onde_phased_array_setup.html"
  click ONDE_PHASED_ARRAY_COMPOUND href "onde_phased_array_compound.html"
```

The compound type mixes Escan and Sscan behavior. COMPOUND_INITIAL_ANGLE, COMPOUND_FINAL_ANGLE and COMPOUND_NUMBER_OF_ANGLES give the angle scope, while COMPOUND_NUMBER_OF_ELEMENTS gives the number of elements in the electronic scanning.
![Compound configuration](../images/media/figure27.png "Figure 27")

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_phased_array_compound-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[2]` | `["ONDE_PHASED_ARRAY_SETUP","ONDE_PHASED_ARRAY_COMPOUND"]` |  |
| [**`INITIAL_ANGLE`**](#onde_phased_array_compound-initial_angle)<br><sub>`ONDE_PHASED_ARRAY_COMPOUND:INITIAL_ANGLE`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`FINAL_ANGLE`**](#onde_phased_array_compound-final_angle)<br><sub>`ONDE_PHASED_ARRAY_COMPOUND:FINAL_ANGLE`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`NUMBER_OF_ANGLES`**](#onde_phased_array_compound-number_of_angles)<br><sub>`ONDE_PHASED_ARRAY_COMPOUND:NUMBER_OF_ANGLES`</sub> | Mandatory | attribute | H5T_INTEGER | `1` | `` |  |
| [**`NUMBER_OF_ELEMENTS`**](#onde_phased_array_compound-number_of_elements)<br><sub>`ONDE_PHASED_ARRAY_COMPOUND:NUMBER_OF_ELEMENTS`</sub> | Mandatory | attribute | H5T_INTEGER | `1` | `` |  |


## Field Details

(onde_phased_array_compound-type)=
### `TYPE`

*No detailed description provided.*

(onde_phased_array_compound-initial_angle)=
### `INITIAL_ANGLE`

*No detailed description provided.*

(onde_phased_array_compound-final_angle)=
### `FINAL_ANGLE`

*No detailed description provided.*

(onde_phased_array_compound-number_of_angles)=
### `NUMBER_OF_ANGLES`

*No detailed description provided.*

(onde_phased_array_compound-number_of_elements)=
### `NUMBER_OF_ELEMENTS`

*No detailed description provided.*
