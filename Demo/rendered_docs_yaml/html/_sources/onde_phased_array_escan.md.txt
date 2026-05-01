# ONDE_PHASED_ARRAY_ESCAN

**Inherits from:** ONDE_PHASED_ARRAY_SETUP

```{mermaid}
classDiagram
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_ESCAN
  click ONDE_PHASED_ARRAY_SETUP href "onde_phased_array_setup.html"
  click ONDE_PHASED_ARRAY_ESCAN href "onde_phased_array_escan.html"
```

In this configuration consecutive subsets of elements are used in order to form a beam at a specific angle, thus forming a sweeping set of ultrasonic beams. Figure 26 illustrates an Escan for 4 consecutive elements with a step of 3 elements on a 32 element linear transducer.
![EScan configuration](../images/media/figure26.png "Figure 26")

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_phased_array_escan-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[2]` | `["ONDE_PHASED_ARRAY_SETUP","ONDE_PHASED_ARRAY_ESCAN"]` |  |
| [**`NUMBER_OF_ELEMENTS`**](#onde_phased_array_escan-number_of_elements)<br><sub>`ONDE_PHASED_ARRAY_ESCAN:NUMBER_OF_ELEMENTS`</sub> | Mandatory | attribute | H5T_INTEGER | `1` | `` |  |
| [**`STEP`**](#onde_phased_array_escan-step)<br><sub>`ONDE_PHASED_ARRAY_ESCAN:STEP`</sub> | Mandatory | attribute | H5T_INTEGER | `1` | `` |  |
| [**`ANGLE`**](#onde_phased_array_escan-angle)<br><sub>`ONDE_PHASED_ARRAY_ESCAN:ANGLE`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |


## Field Details

(onde_phased_array_escan-type)=
### `TYPE`

*No detailed description provided.*

(onde_phased_array_escan-number_of_elements)=
### `NUMBER_OF_ELEMENTS`

*No detailed description provided.*

(onde_phased_array_escan-step)=
### `STEP`

*No detailed description provided.*

(onde_phased_array_escan-angle)=
### `ANGLE`

*No detailed description provided.*
