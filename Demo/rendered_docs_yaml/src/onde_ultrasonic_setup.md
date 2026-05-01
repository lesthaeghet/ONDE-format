# ONDE_ULTRASONIC_SETUP

The ultrasonic setup block describes the electronic acquisition parameters for a dataset. It defines the digitization settings (sampling rate, gain, rectification), filtering, and links to the focal law definitions for multi-element setups.

### Combination between offsets and trajectories
The offsets and directions provided in the dataset blocks can be combined to the data of the trajectory block in order to share common trajectories between different probes (as is common in TOFD controls for example). In this case, the trajectories links point to the same trajectory objects and the offsets/rotation between the trajectory and the probe PCF describe the relative positions of the different probes with respect to the trajectory frame. A typical example is illustrated in Figure 23, with a trajectory frame given at the Probe Center Separation and offsets used to define the PCF locations. If the offset is not provided, the PCF and trajectory frame are assumed to be the same.

![Example of offset and trajectory combination in the case of a TOFD inspection](../images/media/figure23.png "Figure 23")


## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_ultrasonic_setup-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[1]` | `["ONDE_ULTRASONIC_SETUP"]` |  |
| [**`LABEL`**](#onde_ultrasonic_setup-label)<br><sub>`ONDE:LABEL`</sub> | Optional | attribute | H5T_STRING | `1` | `` |  |
| [**`RECTIFICATION`**](#onde_ultrasonic_setup-rectification)<br><sub>`ONDE_ULTRASONIC_SETUP:RECTIFICATION`</sub> | Mandatory | attribute | H5T_INTEGER | `` | `"FULL_WAVE","RECTIFIED_POSITIVE","RECTIFIED_NEGATIVE","RECTIFIED_FULL"` | Defines if the data are FULL_WAVE or RECTIFIED_POSITIVE, RECTIFIED_NEGATIVE, RECTIFIED_FULL |
| [**`FILTER_TYPE`**](#onde_ultrasonic_setup-filter_type)<br><sub>`ONDE_ULTRASONIC_SETUP:FILTER_TYPE`</sub> | Optional | attribute | H5T_INTEGER | `` | `"NO_FILTER","LOW_PASS","HIGH_PASS","BAND_PASS","OTHER"` | Defines the type of filtering applied to the signals : NO_FILTER, LOW_PASS, HIGH_PASS, BAND_PASS, OTHER |
| [**`FILTER_PARAMETERS`**](#onde_ultrasonic_setup-filter_parameters)<br><sub>`ONDE_ULTRASONIC_SETUP:FILTER_PARAMETERS`</sub> | Optional | attribute | H5T_FLOAT | `1 or [N_Ascan<m>] or [ N_DF<m>,N_Ascan<m>]` | `` | The filtering parameters take different values following the filter type: For HIGH_PASS or LOW_PASS this is a single value giving the -3 dB cut-off frequency. |
| [**`FILTER_DESCRIPTION`**](#onde_ultrasonic_setup-filter_description)<br><sub>`ONDE_ULTRASONIC_SETUP:FILTER_DESCRIPTION`</sub> | Optional | attribute | H5T_STRING | `1` | `` | Description of the filtering applied |
| [**`ASCAN_SAMPLE_RATE`**](#onde_ultrasonic_setup-ascan_sample_rate)<br><sub>`ONDE_ULTRASONIC_SETUP:ASCAN_SAMPLE_RATE`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` | This indicates the sampling frequency of A-scan data points. |
| [**`ASCAN_START`**](#onde_ultrasonic_setup-ascan_start)<br><sub>`ONDE_ULTRASONIC_SETUP:ASCAN_START`</sub> | Mandatory | dataset | H5T_FLOAT | `1 or [N_Ascan<m>] or [ N_Ascan<m>,N_DF<m>]` | `` | This indicates the starting time for data acquisition. |
| [**`SIGNAL`**](#onde_ultrasonic_setup-signal)<br><sub>`ONDE_ULTRASONIC_SETUP:SIGNAL`</sub> | Optional | dataset | H5T_FLOAT | `[N_TSig<m>,2]` | `` | Digitization of the emission signal (can be used to store arbitrary  signals). |
| [**`GAIN`**](#onde_ultrasonic_setup-gain)<br><sub>`ONDE_ULTRASONIC_SETUP:GAIN`</sub> | Mandatory | dataset | H5T_FLOAT | `[ N_Ascan<m> ]` | `` | GAIN indicates the total gain for each A-scan during reception. |
| [**`PRF`**](#onde_ultrasonic_setup-prf)<br><sub>`ONDE_ULTRASONIC_SETUP:PRF`</sub> | Optional | dataset | H5T_FLOAT | `[N_Ascan<m>] or [2]` | `` | Pulse Repetition Frequency |
| [**`TCG_CURVE`**](#onde_ultrasonic_setup-tcg_curve)<br><sub>`ONDE_ULTRASONIC_SETUP:TCG_CURVE`</sub> | Optional | dataset | H5T_FLOAT | `[N_Ascan<m>,N_TCG<m> ]` | `` | TCG curve applied to the received signals. |
| [**`PHASED_ARRAY_SETUP`**](#onde_ultrasonic_setup-phased_array_setup)<br><sub>`ONDE_ULTRASONIC_SETUP:PHASED_ARRAY_SETUP`</sub> | Optional | attribute | H5T_STD_REF_OBJ | `1` | `` |  |
| [**`TRANSMIT_LAW`**](#onde_ultrasonic_setup-transmit_law)<br><sub>`ONDE_ULTRASONIC_SETUP:TRANSMIT_LAW`</sub> | Mandatory | dataset | H5T_STD_REF_OBJ | `[N_Ascan<m>] or [N_DF<m>,N_Ascan<m>]` | `` | Each A-scan in a dataframe must be associated with both a transmit and a receive focal law through the datafields. |
| [**`RECEIVE_LAW`**](#onde_ultrasonic_setup-receive_law)<br><sub>`ONDE_ULTRASONIC_SETUP:RECEIVE_LAW`</sub> | Optional | dataset | H5T_STD_REF_OBJ | `[N_Ascan<m>] or [N_DF<m>,N_Ascan<m>]` | `` | Each A-scan in a dataframe must be associated with both a transmit and a receive focal law through the datafields. |


## Field Details

(onde_ultrasonic_setup-type)=
### `TYPE`

*No detailed description provided.*

(onde_ultrasonic_setup-label)=
### `LABEL`

*No detailed description provided.*

(onde_ultrasonic_setup-rectification)=
### `RECTIFICATION`

Defines if the data are FULL_WAVE or RECTIFIED_POSITIVE, RECTIFIED_NEGATIVE, RECTIFIED_FULL

(onde_ultrasonic_setup-filter_type)=
### `FILTER_TYPE`

Defines the type of filtering applied to the signals : NO_FILTER, LOW_PASS, HIGH_PASS, BAND_PASS, OTHER

(onde_ultrasonic_setup-filter_parameters)=
### `FILTER_PARAMETERS`

The filtering parameters take different values following the filter type: For HIGH_PASS or LOW_PASS this is a single value giving the -3 dB cut-off frequency. For BAND_PASS this should contain two values for the lower and upper -3 dB cut-off frequencies. For OTHER, this should be an [3,N_DF<m>] matrix where the first row is frequency and the second and third rows provide the real and imaginary parts of the filters transfer function at that frequency.

(onde_ultrasonic_setup-filter_description)=
### `FILTER_DESCRIPTION`

Description of the filtering applied

(onde_ultrasonic_setup-ascan_sample_rate)=
### `ASCAN_SAMPLE_RATE`

This indicates the sampling frequency of A-scan data points. It is assumed that a uniform sampling rate is used throughout A-scan data collection.

(onde_ultrasonic_setup-ascan_start)=
### `ASCAN_START`

This indicates the starting time for data acquisition. If dimension is 1, the same start time is used for all A-Scans, else a different start time is specified for each A-Scan.

(onde_ultrasonic_setup-signal)=
### `SIGNAL`

Digitization of the emission signal (can be used to store arbitrary  signals). If missing impulse emission at time 0.0 is assumed. 2D Array with one row for time and one for amplitude.

(onde_ultrasonic_setup-gain)=
### `GAIN`

GAIN indicates the total gain for each A-scan during reception. It is a multiplying factor that was applied at acquisition.

(onde_ultrasonic_setup-prf)=
### `PRF`

Pulse Repetition Frequency

(onde_ultrasonic_setup-tcg_curve)=
### `TCG_CURVE`

TCG curve applied to the received signals. It is provided for the entire acquisition gate. The amplitude correction is given for each time sample as a multiplying factor, and must be cumulated to the global one defined by the GAIN attribute.

(onde_ultrasonic_setup-phased_array_setup)=
### `PHASED_ARRAY_SETUP`

*No detailed description provided.*

(onde_ultrasonic_setup-transmit_law)=
### `TRANSMIT_LAW`

Each A-scan in a dataframe must be associated with both a transmit and a receive focal law through the datafields. These contain HDF5 references  to the groups which provide the detailed description of each focal laws (the same structure is used for both transmit and receive focal laws). Mandatory for phased array setups.

(onde_ultrasonic_setup-receive_law)=
### `RECEIVE_LAW`

Each A-scan in a dataframe must be associated with both a transmit and a receive focal law through the datafields. These contain HDF5 references  to the groups which provide the detailed description of each focal laws (the same structure is used for both transmit and receive focal laws).Mandatory for phased array setups.
