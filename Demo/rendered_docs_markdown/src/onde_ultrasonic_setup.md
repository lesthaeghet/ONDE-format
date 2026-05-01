# ONDE_ULTRASONIC_SETUP

### Ultrasonic setup

**Acquisition gate**

The acquisition gate is implicitly defined by:

- the value of Ascan_Astart
- the sampling frequency
- the dimension of data N_Time\<m\>

t0 : ASCAN_ASTART

tend : ASCAN_ASTART + (N_Time\<m\> - 1)/ASCAN_SAMPLE_RATE

**Gain**

GAIN indicates the total gain for each A-scan during reception. It is a multiplying factor that was applied at
acquisition.

**TCG curves**. The curve is specified in the TCG_CURVE field. It is provided for the entire acquisition gate. The
amplification must be cumulated to the global one defined by the GAIN attribute.

**Laws**

Each A-scan in a dataframe must be associated with both a transmit and a receive focal law through the RECEIVE_LAW and
TRANSMIT_LAW datafields. These contain HDF5 references to the groups which provide the detailed description of each
focal laws (the same structure is used for both transmit and receive focal laws). PRF indicates the pulse repetition
frequency for each Tx/Rx combination

**Dynamic laws**

In order to allow advanced setups with different laws defined for each acquisition position, the cardinality of the
transmission and reception can be either a 1D-array (same laws applied for each dataframe) or 2D (differentiated laws).

**Filter Parameters**

The filtering parameters take different values following the filter type.

- For FILTER_TYPE HIGH_PASS or LOW_PASS this is a single value giving the -3 dB cut-off frequency
- For FILTER_TYPE BAND_PASS this should contain two values for the lower and upper -3 dB cut-off frequencies
- For FILTER_TYPE OTHER, this should be an \[3,N_DF\<m\>\] matrix where the first row is frequency and the second and
  third rows provide the real and imaginary parts of the filter's transfer function at that frequency.

**Combination between offsets and trajectories**

The offsets and directions provided in the dataset blocks can be combined to the data of the trajectory block in order
to share common trajectories between different probes (as is common in TOFD controls for example). In this case, the
trajectories links point to the same trajectory objects and the offsets/rotation between the trajectory and the probe
PCF describe the relative positions of the different probes with respect to the trajectory frame. A typical example is
illustrated in Figure 23, with a trajectory frame given at the Probe Center Separation and offsets used to define the
PCF locations. If the offset is not provided, the PCF and trajectory frame are assumed to be the same.

![Example of offset and trajectory combination in the case of a TOFD inspection](../images/media/figure23.png "Figure 23")

*Figure 23: Example of offset and trajectory combination in the case of a TOFD inspection*

**Variable gates**

Variable gates are not handled in this version -- it can be emulated by zero---padding the data block

## Fields

### `TYPE`

- **Full Name:** `ONDE:TYPE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `[1]`
- **Allowed Values:** `["ONDE_ULTRASONIC_SETUP"]`


### `LABEL`

- **Full Name:** `ONDE:LABEL`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `1`


### `RECTIFICATION`

- **Full Name:** `ONDE_ULTRASONIC_SETUP:RECTIFICATION`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_INTEGER`
- **Allowed Values:** `"FULL_WAVE","RECTIFIED_POSITIVE","RECTIFIED_NEGATIVE","RECTIFIED_FULL"`

  Defines if the data are FULL_WAVE or RECTIFIED_POSITIVE, RECTIFIED_NEGATIVE, RECTIFIED_FULL

### `FILTER_TYPE`

- **Full Name:** `ONDE_ULTRASONIC_SETUP:FILTER_TYPE`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_INTEGER`
- **Allowed Values:** `"NO_FILTER","LOW_PASS","HIGH_PASS","BAND_PASS","OTHER"`

  Defines the type of filtering applied to the signals : NO_FILTER, LOW_PASS, HIGH_PASS, BAND_PASS, OTHER

### `FILTER_PARAMETERS`

- **Full Name:** `ONDE_ULTRASONIC_SETUP:FILTER_PARAMETERS`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1 or [N_Ascan<m>] or [ N_DF<m>,N_Ascan<m>]`

  Optional datafield providing analogue filter parameters  see notes for detailed explanation

### `FILTER_DESCRIPTION`

- **Full Name:** `ONDE_ULTRASONIC_SETUP:FILTER_DESCRIPTION`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `1`

  Description of the filtering applied

### `ASCAN_SAMPLE_RATE`

- **Full Name:** `ONDE_ULTRASONIC_SETUP:ASCAN_SAMPLE_RATE`
- **Requirement:** Mandatory
- **Storage:** attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`

  This indicates the sampling frequency of A-scan data points. It is assumed that a uniform sampling rate is used throughout A-scan data collection.

### `ASCAN_START`

- **Full Name:** `ONDE_ULTRASONIC_SETUP:ASCAN_START`
- **Requirement:** Mandatory
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1 or [N_Ascan<m>] or [ N_Ascan<m>,N_DF<m>]`

  This indicates the starting time for data acquisition. If dimension is 1, the same start time is used for all A-Scans, else a different start time is specified for each A-Scan.

### `SIGNAL`

- **Full Name:** `ONDE_ULTRASONIC_SETUP:SIGNAL`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_TSig<m>,2]`

  Digitization of the emission signal (can be used to store arbitrary  signals). If missing impulse emission at time 0.0 is assumed. 2D Array with one row for time and one for amplitude.

### `GAIN`

- **Full Name:** `ONDE_ULTRASONIC_SETUP:GAIN`
- **Requirement:** Mandatory
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[ N_Ascan<m> ]`

  This indicates the total gain for each A-scan during reception. Multiplying factor that was applied at acquisition.

### `PRF`

- **Full Name:** `ONDE_ULTRASONIC_SETUP:PRF`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_Ascan<m>] or [2]`

  Pulse Repetition Frequency

### `TCG_CURVE`

- **Full Name:** `ONDE_ULTRASONIC_SETUP:TCG_CURVE`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[N_Ascan<m>,N_TCG<m> ]`

  TCG curve applied to the received signals. The amplitude correction is given for each time sample as a multiplying factor.

### `PHASED_ARRAY_SETUP`

- **Full Name:** `ONDE_ULTRASONIC_SETUP:PHASED_ARRAY_SETUP`
- **Requirement:** Optional
- **Storage:** attribute
- **Type:** `H5T_STD_REF_OBJ`
- **Dimensions:** `1`


### `TRANSMIT_LAW`

- **Full Name:** `ONDE_ULTRASONIC_SETUP:TRANSMIT_LAW`
- **Requirement:** Mandatory
- **Storage:** dataset
- **Type:** `H5T_STD_REF_OBJ`
- **Dimensions:** `[N_Ascan<m>] or [N_DF<m>,N_Ascan<m>]`

  Each A-scan in a dataframe must be associated with both a transmit and a receive focal law through the datafields. These contain HDF5 references  to the groups which provide the detailed description of each focal laws (the same structure is used for both transmit and receive focal laws). Mandatory for phased array setups.

### `RECEIVE_LAW`

- **Full Name:** `ONDE_ULTRASONIC_SETUP:RECEIVE_LAW`
- **Requirement:** Optional
- **Storage:** dataset
- **Type:** `H5T_STD_REF_OBJ`
- **Dimensions:** `[N_Ascan<m>] or [N_DF<m>,N_Ascan<m>]`

  Each A-scan in a dataframe must be associated with both a transmit and a receive focal law through the datafields. These contain HDF5 references  to the groups which provide the detailed description of each focal laws (the same structure is used for both transmit and receive focal laws).Mandatory for phased array setups.
