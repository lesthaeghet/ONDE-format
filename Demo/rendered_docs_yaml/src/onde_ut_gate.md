# ONDE_UT_GATE

No narrative documentation provided for ONDE_UT_GATE.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_ut_gate-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[1]` | `["ONDE_UT_GATE"]` |  |
| [**`START`**](#onde_ut_gate-start)<br><sub>`ONDE_UT_GATE:START`</sub> | Optional | attribute | H5T_FLOAT | `1` | `` | For scalar data relying on Ascan data, defines the start time for the gate. |
| [**`WIDTH`**](#onde_ut_gate-width)<br><sub>`ONDE_UT_GATE:WIDTH`</sub> | Optional | attribute | H5T_FLOAT | `1` | `` | For Cscans scalar data relying on Ascan data, defines the width of the gate. |
| [**`THRESHOLD`**](#onde_ut_gate-threshold)<br><sub>`ONDE_UT_GATE:THRESHOLD`</sub> | Optional | attribute | H5T_FLOAT | `1` | `` | Defines the threshold of the gate for data to be stored |
| [**`DETECTION`**](#onde_ut_gate-detection)<br><sub>`ONDE_UT_GATE:DETECTION`</sub> | Optional | attribute | H5T_STRING | `1` | `" FIRST_PEAK"\|"LAST_PEAK"\|" MAX_PEAK"\|" FIRST_FLANK"\|"LAST_FLANK"` |  |


## Field Details

(onde_ut_gate-type)=
### `TYPE`

*No detailed description provided.*

(onde_ut_gate-start)=
### `START`

For scalar data relying on Ascan data, defines the start time for the gate. Mandatory for data related to Ascans.

(onde_ut_gate-width)=
### `WIDTH`

For Cscans scalar data relying on Ascan data, defines the width of the gate. Mandatory for data related to Ascans

(onde_ut_gate-threshold)=
### `THRESHOLD`

Defines the threshold of the gate for data to be stored

(onde_ut_gate-detection)=
### `DETECTION`

*No detailed description provided.*
