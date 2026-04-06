.. _ONDE_ULTRASONIC_SETUP:

======================
ONDE_ULTRASONIC_SETUP
======================

:Inherits: --

The ultrasonic setup block describes the electronic acquisition parameters for
a dataset. It defines the digitization settings (sampling rate, gain,
rectification), filtering, and links to the focal law definitions for
multi-element setups.


Field Definitions
-----------------

.. list-table::
   :header-rows: 1
   :widths: 25 4 8 14 20 6 12 11

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
   * - ``ONDE_ULTRASONIC_SETUP:RECTIFICATION``
     - M
     - Attribute
     - ``H5T_INTEGER``
     -
     -
     -
     - Signal rectification mode
   * - ``ONDE_ULTRASONIC_SETUP:FILTER_TYPE``
     - O
     - Attribute
     - ``H5T_INTEGER``
     -
     -
     -
     - Type of filtering applied
   * - ``ONDE_ULTRASONIC_SETUP:FILTER_PARAMETERS``
     - O
     - Attribute
     - ``H5T_FLOAT``
     - ``1`` or ``[N_Ascan<m>]`` or ``[N_DF<m>,N_Ascan<m>]``
     - Hz
     -
     - Filter frequency parameters
   * - ``ONDE_ULTRASONIC_SETUP:FILTER_DESCRIPTION``
     - O
     - Attribute
     - ``H5T_STRING``
     - ``1``
     -
     -
     - Description of filtering
   * - ``ONDE_ULTRASONIC_SETUP:ASCAN_SAMPLE_RATE``
     - M
     - Attribute
     - ``H5T_FLOAT``
     - ``1``
     - Hz
     -
     - A-scan sampling frequency
   * - ``ONDE_ULTRASONIC_SETUP:ASCAN_START``
     - M
     - Dataset
     - ``H5T_FLOAT``
     - ``1`` or ``[N_Ascan<m>]`` or ``[N_Ascan<m>,N_DF<m>]``
     - s
     -
     - Acquisition start time
   * - ``ONDE_ULTRASONIC_SETUP:SIGNAL``
     - O
     - Dataset
     - ``H5T_FLOAT``
     - ``[N_TSig<m>,2]``
     -
     - impulse at t=0.0
     - Emission signal digitization
   * - ``ONDE_ULTRASONIC_SETUP:GAIN``
     - M
     - Dataset
     - ``H5T_FLOAT``
     - ``[N_Ascan<m>]``
     -
     -
     - Total reception gain per A-scan
   * - ``ONDE_ULTRASONIC_SETUP:PRF``
     - O
     - Dataset
     - ``H5T_FLOAT``
     - ``[N_Ascan<m>]`` or ``[2]``
     - Hz
     -
     - Pulse Repetition Frequency
   * - ``ONDE_ULTRASONIC_SETUP:TCG_CURVE``
     - O
     - Dataset
     - ``H5T_FLOAT``
     - ``[N_Ascan<m>,N_TCG<m>]``
     -
     -
     - Time-corrected gain curve
   * - ``ONDE_ULTRASONIC_SETUP:PHASED_ARRAY_SETUP``
     - O
     - Attribute
     - ``H5T_STD_REF_OBJ``
     - ``1``
     -
     -
     - Reference to phased array setup
   * - ``ONDE_ULTRASONIC_SETUP:TRANSMIT_LAW``
     - M
     - Dataset
     - ``H5T_STD_REF_OBJ``
     - ``[N_Ascan<m>]`` or ``[N_DF<m>,N_Ascan<m>]``
     -
     -
     - Transmit focal law references
   * - ``ONDE_ULTRASONIC_SETUP:RECEIVE_LAW``
     - O
     - Dataset
     - ``H5T_STD_REF_OBJ``
     - ``[N_Ascan<m>]`` or ``[N_DF<m>,N_Ascan<m>]``
     -
     -
     - Receive focal law references


Enumerated Values
-----------------

ONDE_ULTRASONIC_SETUP:RECTIFICATION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

ONDE_ULTRASONIC_SETUP:FILTER_TYPE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

- ``ONDE_ULTRASONIC_SETUP:ASCAN_START`` — the starting time (t₀)
- ``ONDE_ULTRASONIC_SETUP:ASCAN_SAMPLE_RATE`` — the sampling frequency
- ``N_Time<m>`` — the number of time-domain data points

The end time is computed as:

.. math::

   t_{end} = \text{ASCAN\_START} + \frac{N_{Time}\langle m \rangle - 1}{\text{ASCAN\_SAMPLE\_RATE}}

ONDE_ULTRASONIC_SETUP:GAIN
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Indicates the total gain for each A-scan during reception. It is a multiplying
factor that was applied at acquisition.

ONDE_ULTRASONIC_SETUP:TCG_CURVE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The TCG (Time-Corrected Gain) curve is applied to the received signals.

.. important::

   The amplification from TCG must be cumulated with the global gain defined
   by the ``ONDE_ULTRASONIC_SETUP:GAIN`` field.

ONDE_ULTRASONIC_SETUP:SIGNAL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Digitization of the emission signal. 2D array with one row for time and one
for amplitude. If missing, impulse emission at time 0.0 is assumed.

ONDE_ULTRASONIC_SETUP:FILTER_PARAMETERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The filtering parameters take different values following the filter type:

- For ``HIGH_PASS`` or ``LOW_PASS``: a single value giving the −3 dB cut-off
  frequency
- For ``BAND_PASS``: two values for the lower and upper −3 dB cut-off
  frequencies
- For ``OTHER``: an ``[3,N_DF<m>]`` matrix with frequency, real, and imaginary
  parts of the filter's transfer function

ONDE_ULTRASONIC_SETUP:TRANSMIT_LAW / RECEIVE_LAW
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each A-scan must be associated with transmit and receive focal laws. These
contain HDF5 references to groups of type :ref:`ONDE_UT_LAW`.

.. important::

   ``TRANSMIT_LAW`` is mandatory for phased array setups. ``RECEIVE_LAW`` is
   optional but recommended.


Notes
-----

Variable gates
^^^^^^^^^^^^^^

Variable gates are not handled in this version — they can be emulated by
zero-padding the data block.

Combination between offsets and trajectories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The offsets provided in the dataset blocks can be combined with the trajectory
block to share common trajectories between probes (common in TOFD controls).

.. figure:: ../../images/media/figure23.png
   :alt: Example of offset and trajectory combination in TOFD

   Figure 23: Offset and trajectory combination in TOFD inspection
