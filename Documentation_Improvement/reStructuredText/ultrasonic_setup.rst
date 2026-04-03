.. _ONDE_ULTRASONIC_SETUP:

======================
ONDE_ULTRASONIC_SETUP
======================

:Version: 0.4.0
:Inherits: --
:Subclasses: --
:See Also: :ref:`ONDE_SETUP`, :ref:`ONDE_UT_LAW`, :ref:`ONDE_PHASED_ARRAY_SETUP`

The ultrasonic setup block describes the electronic acquisition parameters for
a dataset. It defines the digitization settings (sampling rate, gain,
rectification), filtering, and links to the focal law definitions for
multi-element setups.


Field Definitions
-----------------

..
   MACHINE-PARSEABLE: This table is the authoritative field schema.
   Automated tools extract field definitions from this table.

.. list-table::
   :header-rows: 1
   :widths: 18 4 8 14 20 6 12 18

   * - Field
     - Req
     - Storage
     - Type
     - Dimensions
     - Units
     - Default
     - Brief Description
   * - ``ONDE:TYPE``
     - M
     - Attribute
     - ``H5T_STRING``
     - ``[1]``
     -
     - ``["ONDE_ULTRASONIC_SETUP"]``
     - Class type identifier
   * - ``ONDE:LABEL``
     - O
     - Attribute
     - ``H5T_STRING``
     - ``1``
     -
     -
     - Human-readable label
   * - ``RECTIFICATION``
     - M
     - Attribute
     - ``H5T_INTEGER``
     -
     -
     -
     - Signal rectification mode
   * - ``FILTER_TYPE``
     - O
     - Attribute
     - ``H5T_INTEGER``
     -
     -
     -
     - Type of filtering applied
   * - ``FILTER_PARAMETERS``
     - O
     - Attribute
     - ``H5T_FLOAT``
     - ``1`` or ``[N_Ascan<m>]`` or ``[N_DF<m>,N_Ascan<m>]``
     - Hz
     -
     - Filter frequency parameters
   * - ``FILTER_DESCRIPTION``
     - O
     - Attribute
     - ``H5T_STRING``
     - ``1``
     -
     -
     - Description of filtering
   * - ``ASCAN_SAMPLE_RATE``
     - M
     - Attribute
     - ``H5T_FLOAT``
     - ``1``
     - Hz
     -
     - A-scan sampling frequency
   * - ``ASCAN_START``
     - M
     - Dataset
     - ``H5T_FLOAT``
     - ``1`` or ``[N_Ascan<m>]`` or ``[N_Ascan<m>,N_DF<m>]``
     - s
     -
     - Acquisition start time
   * - ``SIGNAL``
     - O
     - Dataset
     - ``H5T_FLOAT``
     - ``[N_TSig<m>,2]``
     -
     - impulse at t=0.0
     - Emission signal digitization
   * - ``GAIN``
     - M
     - Dataset
     - ``H5T_FLOAT``
     - ``[N_Ascan<m>]``
     -
     -
     - Total reception gain per A-scan
   * - ``PRF``
     - O
     - Dataset
     - ``H5T_FLOAT``
     - ``[N_Ascan<m>]`` or ``[2]``
     - Hz
     -
     - Pulse Repetition Frequency
   * - ``TCG_CURVE``
     - O
     - Dataset
     - ``H5T_FLOAT``
     - ``[N_Ascan<m>,N_TCG<m>]``
     -
     -
     - Time-corrected gain curve
   * - ``PHASED_ARRAY_SETUP``
     - O
     - Attribute
     - ``H5T_STD_REF_OBJ``
     - ``1``
     -
     -
     - Reference to phased array setup
   * - ``TRANSMIT_LAW``
     - M
     - Dataset
     - ``H5T_STD_REF_OBJ``
     - ``[N_Ascan<m>]`` or ``[N_DF<m>,N_Ascan<m>]``
     -
     -
     - Transmit focal law references
   * - ``RECEIVE_LAW``
     - O
     - Dataset
     - ``H5T_STD_REF_OBJ``
     - ``[N_Ascan<m>]`` or ``[N_DF<m>,N_Ascan<m>]``
     -
     -
     - Receive focal law references


Enumerated Values
-----------------

RECTIFICATION
^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Value
     - Description
   * - ``FULL_WAVE``
     - No rectification applied
   * - ``RECTIFIED_POSITIVE``
     - Positive half-wave rectification
   * - ``RECTIFIED_NEGATIVE``
     - Negative half-wave rectification
   * - ``RECTIFIED_FULL``
     - Full-wave rectification

FILTER_TYPE
^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Value
     - Description
   * - ``NO_FILTER``
     - No filtering applied
   * - ``LOW_PASS``
     - Low-pass filter
   * - ``HIGH_PASS``
     - High-pass filter
   * - ``BAND_PASS``
     - Band-pass filter
   * - ``OTHER``
     - Custom filter (see ``FILTER_PARAMETERS``)


Detailed Field Documentation
-----------------------------

Acquisition gate
^^^^^^^^^^^^^^^^

The acquisition gate is implicitly defined by three values:

- ``ASCAN_START`` — the starting time (t₀)
- ``ASCAN_SAMPLE_RATE`` — the sampling frequency
- ``N_Time<m>`` — the number of time-domain data points

The end time is computed as:

.. math::

   t_{end} = \text{ASCAN\_START} + \frac{N_{Time}\langle m \rangle - 1}{\text{ASCAN\_SAMPLE\_RATE}}

ASCAN_START
^^^^^^^^^^^

This indicates the starting time for data acquisition. If dimension is ``1``,
the same start time is used for all A-Scans; otherwise a different start time
is specified for each A-Scan.

GAIN
^^^^

``GAIN`` indicates the total gain for each A-scan during reception. It is a
multiplying factor that was applied at acquisition.

TCG_CURVE
^^^^^^^^^

The TCG (Time-Corrected Gain) curve is applied to the received signals.
The amplitude correction is given for each time sample as a multiplying
factor. It is provided for the entire acquisition gate.

.. important::

   The amplification from TCG must be cumulated with the global gain defined
   by the ``GAIN`` field.

SIGNAL
^^^^^^

Digitization of the emission signal (can be used to store arbitrary signals).
2D array with one row for time and one for amplitude. If missing, impulse
emission at time 0.0 is assumed.

FILTER_PARAMETERS
^^^^^^^^^^^^^^^^^

The filtering parameters take different values following the filter type:

- For ``HIGH_PASS`` or ``LOW_PASS``: a single value giving the −3 dB cut-off
  frequency
- For ``BAND_PASS``: two values for the lower and upper −3 dB cut-off
  frequencies
- For ``OTHER``: an ``[3,N_DF<m>]`` matrix where the first row is frequency
  and the second and third rows provide the real and imaginary parts of the
  filter's transfer function at that frequency

TRANSMIT_LAW / RECEIVE_LAW
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each A-scan in a dataframe must be associated with both a transmit and a
receive focal law through the ``TRANSMIT_LAW`` and ``RECEIVE_LAW`` datafields.
These contain HDF5 references to the groups (of type :ref:`ONDE_UT_LAW`) which
provide the detailed description of each focal law. The same structure is used
for both transmit and receive focal laws.

.. important::

   ``TRANSMIT_LAW`` is mandatory for phased array setups. ``RECEIVE_LAW`` is
   optional but recommended.

**Dynamic laws:**

In order to allow advanced setups with different laws defined for each
acquisition position, the cardinality of the transmission and reception can
be either:

- **1D array** ``[N_Ascan<m>]`` — same laws applied for each dataframe
- **2D array** ``[N_DF<m>,N_Ascan<m>]`` — differentiated laws per dataframe

PRF
^^^

Pulse Repetition Frequency for each Tx/Rx combination.


Notes
-----

Variable gates
^^^^^^^^^^^^^^

Variable gates are not handled in this version of the specification — they can
be emulated by zero-padding the data block.

Combination between offsets and trajectories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The offsets and directions provided in the dataset blocks can be combined with
the data of the trajectory block in order to share common trajectories between
different probes (as is common in TOFD controls). In this case, the trajectory
links point to the same trajectory objects and the offsets/rotation between the
trajectory and the probe PCF describe the relative positions of the different
probes with respect to the trajectory frame.

.. figure:: ../../images/media/figure23.png
   :alt: Example of offset and trajectory combination in TOFD

   Figure 23: Example of offset and trajectory combination in the case of a
   TOFD inspection
