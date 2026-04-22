# ONDE_ULTRASONIC_SETUP

:::{metadata}
onde_class: ONDE_ULTRASONIC_SETUP
inherits: []
:::

The ultrasonic setup block describes the electronic acquisition parameters for
a dataset. It defines the digitization settings (sampling rate, gain,
rectification), filtering, and links to the focal law definitions for
multi-element setups.

## Fields

### `ONDE:TYPE`

Required
: Mandatory

Storage
: Attribute

Type
: `H5T_STRING`

Dimensions
: `[1]`

Default
: `["ONDE_ULTRASONIC_SETUP"]`

Class type identifier.

### `ONDE:LABEL`

Required
: Optional

Storage
: Attribute

Type
: `H5T_STRING`

Dimensions
: `1`

Human-readable label.

### `ONDE_ULTRASONIC_SETUP:RECTIFICATION`

Required
: Mandatory

Storage
: Attribute

Type
: `H5T_INTEGER`

Enum
: - `FULL_WAVE` — No rectification applied
  - `RECTIFIED_POSITIVE` — Positive half-wave rectification
  - `RECTIFIED_NEGATIVE` — Negative half-wave rectification
  - `RECTIFIED_FULL` — Full-wave rectification

Signal rectification mode.

### `ONDE_ULTRASONIC_SETUP:FILTER_TYPE`

Required
: Optional

Storage
: Attribute

Type
: `H5T_INTEGER`

Enum
: - `NO_FILTER` — No filtering applied
  - `LOW_PASS` — Low-pass filter
  - `HIGH_PASS` — High-pass filter
  - `BAND_PASS` — Band-pass filter
  - `OTHER` — Custom filter (see `FILTER_PARAMETERS`)

Type of filtering applied.

### `ONDE_ULTRASONIC_SETUP:FILTER_PARAMETERS`

Required
: Optional

Storage
: Attribute

Type
: `H5T_FLOAT`

Dimensions
: `1` or `[N_Ascan<m>]` or `[N_DF<m>,N_Ascan<m>]`

Units
: Hz

Filter frequency parameters. The values depend on the filter type:

- For `HIGH_PASS` or `LOW_PASS`: a single value giving the −3 dB cut-off frequency
- For `BAND_PASS`: two values for the lower and upper −3 dB cut-off frequencies
- For `OTHER`: an `[3,N_DF<m>]` matrix with frequency, real, and imaginary parts

### `ONDE_ULTRASONIC_SETUP:FILTER_DESCRIPTION`

Required
: Optional

Storage
: Attribute

Type
: `H5T_STRING`

Dimensions
: `1`

Description of filtering.

### `ONDE_ULTRASONIC_SETUP:ASCAN_SAMPLE_RATE`

Required
: Mandatory

Storage
: Attribute

Type
: `H5T_FLOAT`

Dimensions
: `1`

Units
: Hz

A-scan sampling frequency.

### `ONDE_ULTRASONIC_SETUP:ASCAN_START`

Required
: Mandatory

Storage
: Dataset

Type
: `H5T_FLOAT`

Dimensions
: `1` or `[N_Ascan<m>]` or `[N_Ascan<m>,N_DF<m>]`

Units
: s

Acquisition start time. If dimension is 1, the same start time is used for all
A-Scans.

### `ONDE_ULTRASONIC_SETUP:SIGNAL`

Required
: Optional

Storage
: Dataset

Type
: `H5T_FLOAT`

Dimensions
: `[N_TSig<m>,2]`

Default
: impulse at t=0.0

Digitization of the emission signal. 2D array with one row for time and one
for amplitude. If missing, impulse emission at time 0.0 is assumed.

### `ONDE_ULTRASONIC_SETUP:GAIN`

Required
: Mandatory

Storage
: Dataset

Type
: `H5T_FLOAT`

Dimensions
: `[N_Ascan<m>]`

Total reception gain per A-scan. Indicates the total gain during reception as
a multiplying factor that was applied at acquisition.

### `ONDE_ULTRASONIC_SETUP:PRF`

Required
: Optional

Storage
: Dataset

Type
: `H5T_FLOAT`

Dimensions
: `[N_Ascan<m>]` or `[2]`

Units
: Hz

Pulse Repetition Frequency.

### `ONDE_ULTRASONIC_SETUP:TCG_CURVE`

Required
: Optional

Storage
: Dataset

Type
: `H5T_FLOAT`

Dimensions
: `[N_Ascan<m>,N_TCG<m>]`

Time-corrected gain curve. The amplitude correction is given for each time
sample as a multiplying factor.

:::{important}
The amplification from TCG must be cumulated with the global gain
defined by `ONDE_ULTRASONIC_SETUP:GAIN`.
:::

### `ONDE_ULTRASONIC_SETUP:PHASED_ARRAY_SETUP`

Required
: Optional

Storage
: Attribute

Type
: `H5T_STD_REF_OBJ`

Dimensions
: `1`

Reference to phased array setup.

### `ONDE_ULTRASONIC_SETUP:TRANSMIT_LAW`

Required
: Mandatory

Storage
: Dataset

Type
: `H5T_STD_REF_OBJ`

Dimensions
: `[N_Ascan<m>]` or `[N_DF<m>,N_Ascan<m>]`

Transmit focal law references. Each A-scan must be associated with a transmit
focal law. Contains HDF5 references to groups of type ONDE_UT_LAW.

:::{note}
`TRANSMIT_LAW` is mandatory for phased array setups.
:::

### `ONDE_ULTRASONIC_SETUP:RECEIVE_LAW`

Required
: Optional

Storage
: Dataset

Type
: `H5T_STD_REF_OBJ`

Dimensions
: `[N_Ascan<m>]` or `[N_DF<m>,N_Ascan<m>]`

Receive focal law references. Optional but recommended. Same cardinality
rules as `TRANSMIT_LAW`.

## Notes

### Variable gates

Variable gates are not handled in this version — emulate by zero-padding.

### TCG and GAIN interaction

The amplification from TCG must be cumulated with the global gain
defined by `ONDE_ULTRASONIC_SETUP:GAIN`.
