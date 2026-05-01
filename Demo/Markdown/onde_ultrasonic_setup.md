---
onde_class: ONDE_ULTRASONIC_SETUP
inherits: []
fields:
- full_name: ONDE:TYPE
  short_name: TYPE
  required: true
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '[1]'
  allowed_values: '["ONDE_ULTRASONIC_SETUP"]'
- full_name: ONDE:LABEL
  short_name: LABEL
  required: false
  storage: attribute
  hdf5_type: H5T_STRING
  description: ''
  dimensions: '1'
- full_name: ONDE_ULTRASONIC_SETUP:RECTIFICATION
  short_name: RECTIFICATION
  required: true
  storage: attribute
  hdf5_type: H5T_INTEGER
  description: "Defines if the data are \x91FULL_WAVE\x92 or \x91RECTIFIED_POSITIVE\x92\
    , \x91RECTIFIED_NEGATIVE\x92, \x91RECTIFIED_FULL\x92"
  allowed_values: '"FULL_WAVE","RECTIFIED_POSITIVE","RECTIFIED_NEGATIVE","RECTIFIED_FULL"'
- full_name: ONDE_ULTRASONIC_SETUP:FILTER_TYPE
  short_name: FILTER_TYPE
  required: false
  storage: attribute
  hdf5_type: H5T_INTEGER
  description: "Defines the type of filtering applied to the signals : \x93NO_FILTER\x94\
    , LOW_PASS\x94, \x93HIGH_PASS\x94, \x93BAND_PASS\x94, \x93OTHER\x94"
  allowed_values: '"NO_FILTER","LOW_PASS","HIGH_PASS","BAND_PASS","OTHER"'
- full_name: ONDE_ULTRASONIC_SETUP:FILTER_PARAMETERS
  short_name: FILTER_PARAMETERS
  required: false
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: "Optional datafield providing analogue filter parameters \x96 see notes\
    \ for detailed explanation"
  dimensions: 1 or [N_Ascan<m>] or [ N_DF<m>,N_Ascan<m>]
- full_name: ONDE_ULTRASONIC_SETUP:FILTER_DESCRIPTION
  short_name: FILTER_DESCRIPTION
  required: false
  storage: attribute
  hdf5_type: H5T_STRING
  description: Description of the filtering applied
  dimensions: '1'
- full_name: ONDE_ULTRASONIC_SETUP:ASCAN_SAMPLE_RATE
  short_name: ASCAN_SAMPLE_RATE
  required: true
  storage: attribute
  hdf5_type: H5T_FLOAT
  description: This indicates the sampling frequency of A-scan data points. It is
    assumed that a uniform sampling rate is used throughout A-scan data collection.
  dimensions: '1'
- full_name: ONDE_ULTRASONIC_SETUP:ASCAN_START
  short_name: ASCAN_START
  required: true
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: This indicates the starting time for data acquisition. If dimension
    is 1, the same start time is used for all A-Scans, else a different start time
    is specified for each A-Scan.
  dimensions: 1 or [N_Ascan<m>] or [ N_Ascan<m>,N_DF<m>]
- full_name: ONDE_ULTRASONIC_SETUP:SIGNAL
  short_name: SIGNAL
  required: false
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: Digitization of the emission signal (can be used to store arbitrary  signals).
    If missing impulse emission at time 0.0 is assumed. 2D Array with one row for
    time and one for amplitude.
  dimensions: '[N_TSig<m>,2]'
- full_name: ONDE_ULTRASONIC_SETUP:GAIN
  short_name: GAIN
  required: true
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: This indicates the total gain for each A-scan during reception. Multiplying
    factor that was applied at acquisition.
  dimensions: '[ N_Ascan<m> ]'
- full_name: ONDE_ULTRASONIC_SETUP:PRF
  short_name: PRF
  required: false
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: Pulse Repetition Frequency
  dimensions: '[N_Ascan<m>] or [2]'
- full_name: ONDE_ULTRASONIC_SETUP:TCG_CURVE
  short_name: TCG_CURVE
  required: false
  storage: dataset
  hdf5_type: H5T_FLOAT
  description: TCG curve applied to the received signals. The amplitude correction
    is given for each time sample as a multiplying factor.
  dimensions: '[N_Ascan<m>,N_TCG<m> ]'
- full_name: ONDE_ULTRASONIC_SETUP:PHASED_ARRAY_SETUP
  short_name: PHASED_ARRAY_SETUP
  required: false
  storage: attribute
  hdf5_type: H5T_STD_REF_OBJ
  description: ''
  dimensions: '1'
- full_name: ONDE_ULTRASONIC_SETUP:TRANSMIT_LAW
  short_name: TRANSMIT_LAW
  required: true
  storage: dataset
  hdf5_type: H5T_STD_REF_OBJ
  description: "Each A-scan in a dataframe must be associated with both a transmit\
    \ and a receive focal law through the datafields. These contain HDF5 references\
    \ \_to the groups which provide the detailed description of each focal laws (the\
    \ same structure is used for both transmit and receive focal laws). Mandatory\
    \ for phased array setups."
  dimensions: '[N_Ascan<m>] or [N_DF<m>,N_Ascan<m>]'
- full_name: ONDE_ULTRASONIC_SETUP:RECEIVE_LAW
  short_name: RECEIVE_LAW
  required: false
  storage: dataset
  hdf5_type: H5T_STD_REF_OBJ
  description: "Each A-scan in a dataframe must be associated with both a transmit\
    \ and a receive focal law through the datafields. These contain HDF5 references\
    \ \_to the groups which provide the detailed description of each focal laws (the\
    \ same structure is used for both transmit and receive focal laws).Mandatory for\
    \ phased array setups."
  dimensions: '[N_Ascan<m>] or [N_DF<m>,N_Ascan<m>]'
---

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