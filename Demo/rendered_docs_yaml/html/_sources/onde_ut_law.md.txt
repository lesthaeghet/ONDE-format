# ONDE_UT_LAW

### Law

For multielements, these groups describe the settings of a given transmit or receive law. PROBE and ELEMENT give the
probe and element number to which the DELAY and WEIGHTING apply.

The format also allows to store an information about the corresponding ultrasonic path.

PROPAGATION_LINE represents the ultrasonic ray along which the data is to be represented in a true visualisation. It
contains at least two points in the Probe Coordinates Frame corresponding to the start and end of the ray. (x,y,z)
positions in Probe Coordinate Frame and time of flight are stored.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_ut_law-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `` | `["ONDE_UT_LAW"]` |  |
| [**`PROBE`**](#onde_ut_law-probe)<br><sub>`ONDE_UT_LAW:PROBE`</sub> | Mandatory | dataset | H5T_STD_REF_OBJ | `[N_C<k>]` | `` |  |
| [**`ELEMENT`**](#onde_ut_law-element)<br><sub>`ONDE_UT_LAW:ELEMENT`</sub> | Mandatory | dataset | H5T_INTEGER | `[N_C<k>]` | `` |  |
| [**`DELAY`**](#onde_ut_law-delay)<br><sub>`ONDE_UT_LAW:DELAY`</sub> | Optional | dataset | H5T_FLOAT | `[N_C<k>]` | `` | Specifies the relative delay (in ultrasonic time) between the different Probe Element Combinations in the focal law. |
| [**`WEIGHTING`**](#onde_ut_law-weighting)<br><sub>`ONDE_UT_LAW:WEIGHTING`</sub> | Optional | dataset | H5T_FLOAT | `[N_C<k>]` | `` | Specifies the weighting between the different Probe Element Combinations in the focal law. |
| [**`PROPAGATION_LINE`**](#onde_ut_law-propagation_line)<br><sub>`ONDE_UT_LAW:PROPAGATION_LINE`</sub> | Optional | dataset | H5T_FLOAT | `[N_Points<k>,4]` | `` | Represents the ultrasonic ray along which the data is to be represented in a true visualisation. |


## Field Details

(onde_ut_law-type)=
### `TYPE`

*No detailed description provided.*

(onde_ut_law-probe)=
### `PROBE`

*No detailed description provided.*

(onde_ut_law-element)=
### `ELEMENT`

*No detailed description provided.*

(onde_ut_law-delay)=
### `DELAY`

Specifies the relative delay (in ultrasonic time) between the different Probe Element Combinations in the focal law. The default value is zero delay for all Probe Element Combinations.

(onde_ut_law-weighting)=
### `WEIGHTING`

Specifies the weighting between the different Probe Element Combinations in the focal law. The default is one for all Probe Element Combinations.

(onde_ut_law-propagation_line)=
### `PROPAGATION_LINE`

Represents the ultrasonic ray along which the data is to be represented in a true visualisation. It contains at least two points in the Probe Coordinates Frame corresponding to the start and end of the ray. (x,y,z) positions in Probe Coordinate Frame and time of flight are stored).
