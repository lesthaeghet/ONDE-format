# ONDE_UT_ELEMENTS

No narrative documentation provided for ONDE_UT_ELEMENTS.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE_TAGS`**](#onde_ut_elements-type_tags)<br><sub>`ONDE:TYPE_TAGS`</sub> | Mandatory | attribute | H5T_STRING | `[1]` | `["ONDE_UT_ELEMENTS"]` | Defines the ONDE_UT_ELEMENTS accessory class |
| [**`FRAME`**](#onde_ut_elements-frame)<br><sub>`ONDE_UT_ELEMENTS:FRAME`</sub> | Mandatory | dataset | H5T_FLOAT | `[N_Elem<p>,7]` | `` | Array defining the location of the elements of the probe |
| [**`SHAPE`**](#onde_ut_elements-shape)<br><sub>`ONDE_UT_ELEMENTS:SHAPE`</sub> | Mandatory | dataset | H5T_INTEGER | `[N_Elem<p>]` | `` | The shape of each element will be defined as one of the following: rectangle (ELE_GEOM_REC), part of a ring (ELE_GEOM_RING_PART), part of an elliptical ring (ELE_GEOM_ELLIPSE_PART), |
| [**`SIZE`**](#onde_ut_elements-size)<br><sub>`ONDE_UT_ELEMENTS:SIZE`</sub> | Mandatory | dataset | H5T_FLOAT | `[N_Elem<p>,6]` | `` |  |
| [**`RADIUS_OF_CURVATURE`**](#onde_ut_elements-radius_of_curvature)<br><sub>`ONDE_UT_ELEMENTS:RADIUS_OF_CURVATURE`</sub> | Optional | dataset | H5T_FLOAT | `[N_Elem<p>]` | `` | If absent, flat elements are assumed |
| [**`AXIS_OF_CURVATURE`**](#onde_ut_elements-axis_of_curvature)<br><sub>`ONDE_UT_ELEMENTS:AXIS_OF_CURVATURE`</sub> | Optional | dataset | H5T_FLOAT | `[N_Elem<p>,3]` | `` | If absent, flat elements are assumed |
| [**`DEAD_ELEMENT`**](#onde_ut_elements-dead_element)<br><sub>`ONDE_UT_ELEMENTS:DEAD_ELEMENT`</sub> | Optional | dataset | H5T_INTEGER | `[N_Elem<p>]` | `` | Datafield of logical values (0 = false, 1 = true) used to flag non-functioning elements in an array probe (if not present, assumption should be that all elements are performing correctly); |


## Field Details

(onde_ut_elements-type_tags)=
### `TYPE_TAGS`

Defines the ONDE_UT_ELEMENTS accessory class

(onde_ut_elements-frame)=
### `FRAME`

Array defining the location of the elements of the probe

(onde_ut_elements-shape)=
### `SHAPE`

The shape of each element will be defined as one of the following: rectangle (ELE_GEOM_REC), part of a ring (ELE_GEOM_RING_PART), part of an elliptical ring (ELE_GEOM_ELLIPSE_PART),

(onde_ut_elements-size)=
### `SIZE`

*No detailed description provided.*

(onde_ut_elements-radius_of_curvature)=
### `RADIUS_OF_CURVATURE`

If absent, flat elements are assumed

(onde_ut_elements-axis_of_curvature)=
### `AXIS_OF_CURVATURE`

If absent, flat elements are assumed

(onde_ut_elements-dead_element)=
### `DEAD_ELEMENT`

Datafield of logical values (0 = false, 1 = true) used to flag non-functioning elements in an array probe (if not present, assumption should be that all elements are performing correctly);
