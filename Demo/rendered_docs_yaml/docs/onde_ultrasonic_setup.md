# ONDE_ULTRASONIC_SETUP


```mermaid
classDiagram
  click ONDE_ULTRASONIC_SETUP href "onde_ultrasonic_setup.html"
```


The ultrasonic setup block describes the electronic acquisition parameters for a dataset. It defines the digitization settings (sampling rate, gain, rectification), filtering, and links to the focal law definitions for multi-element setups.

### Combination between offsets and trajectories
The offsets and directions provided in the dataset blocks can be combined to the data of the trajectory block in order to share common trajectories between different probes (as is common in TOFD controls for example). In this case, the trajectories links point to the same trajectory objects and the offsets/rotation between the trajectory and the probe PCF describe the relative positions of the different probes with respect to the trajectory frame. A typical example is illustrated in Figure 23, with a trajectory frame given at the Probe Center Separation and offsets used to define the PCF locations. If the offset is not provided, the PCF and trajectory frame are assumed to be the same.

![Example of offset and trajectory combination in the case of a TOFD inspection](images/media/figure23.png "Figure 23")



## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[1]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_ULTRASONIC_SETUP`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-label"><code>LABEL</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-rectification"><code>RECTIFICATION</code></strong> &mdash; Defines if the data are FULL_WAVE or RECTIFIED_POSITIVE, RECTIFIED_NEGATIVE, RECTIFIED_FULL</div><div class="field-summary-bottom" markdown="span">H5T_INTEGER</div></summary>

<div class="field-content" markdown="1">

Defines if the data are FULL_WAVE or RECTIFIED_POSITIVE, RECTIFIED_NEGATIVE, RECTIFIED_FULL

---

**Type:** <span markdown="span">H5T_INTEGER</span> | **Dimensions:** `` | **Required:** Yes | **Storage:** attribute | **Allowed:** `"FULL_WAVE","RECTIFIED_POSITIVE","RECTIFIED_NEGATIVE","RECTIFIED_FULL"`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-filter_type"><code>FILTER_TYPE</code></strong> &mdash; Defines the type of filtering applied to the signals : NO_FILTER, LOW_PASS, HIGH_PASS, BAND_PASS, OTHER</div><div class="field-summary-bottom" markdown="span">H5T_INTEGER</div></summary>

<div class="field-content" markdown="1">

Defines the type of filtering applied to the signals : NO_FILTER, LOW_PASS, HIGH_PASS, BAND_PASS, OTHER

---

**Type:** <span markdown="span">H5T_INTEGER</span> | **Dimensions:** `` | **Required:** No | **Storage:** attribute | **Allowed:** `"NO_FILTER","LOW_PASS","HIGH_PASS","BAND_PASS","OTHER"`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-filter_parameters"><code>FILTER_PARAMETERS</code></strong> &mdash; The filtering parameters take different values following the filter type: For HIGH_PASS or LOW_PASS this is a single value giving the -3 dB cut-off frequency.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

The filtering parameters take different values following the filter type: For HIGH_PASS or LOW_PASS this is a single value giving the -3 dB cut-off frequency. For BAND_PASS this should contain two values for the lower and upper -3 dB cut-off frequencies. For OTHER, this should be an [3,N_DF<m>] matrix where the first row is frequency and the second and third rows provide the real and imaginary parts of the filters transfer function at that frequency.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1 or [N_Ascan<m>] or [ N_DF<m>,N_Ascan<m>]` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-filter_description"><code>FILTER_DESCRIPTION</code></strong> &mdash; Description of the filtering applied</div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

Description of the filtering applied

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-ascan_sample_rate"><code>ASCAN_SAMPLE_RATE</code></strong> &mdash; This indicates the sampling frequency of A-scan data points.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

This indicates the sampling frequency of A-scan data points. It is assumed that a uniform sampling rate is used throughout A-scan data collection.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-ascan_start"><code>ASCAN_START</code></strong> &mdash; This indicates the starting time for data acquisition.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

This indicates the starting time for data acquisition. If dimension is 1, the same start time is used for all A-Scans, else a different start time is specified for each A-Scan.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1 or [N_Ascan<m>] or [ N_Ascan<m>,N_DF<m>]` | **Required:** Yes | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-signal"><code>SIGNAL</code></strong> &mdash; Digitization of the emission signal (can be used to store arbitrary  signals).</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

Digitization of the emission signal (can be used to store arbitrary  signals). If missing impulse emission at time 0.0 is assumed. 2D Array with one row for time and one for amplitude.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_TSig<m>,2]` | **Required:** No | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-gain"><code>GAIN</code></strong> &mdash; GAIN indicates the total gain for each A-scan during reception.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

GAIN indicates the total gain for each A-scan during reception. It is a multiplying factor that was applied at acquisition.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[ N_Ascan<m> ]` | **Required:** Yes | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-prf"><code>PRF</code></strong> &mdash; Pulse Repetition Frequency</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

Pulse Repetition Frequency

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_Ascan<m>] or [2]` | **Required:** No | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-tcg_curve"><code>TCG_CURVE</code></strong> &mdash; TCG curve applied to the received signals.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

TCG curve applied to the received signals. It is provided for the entire acquisition gate. The amplitude correction is given for each time sample as a multiplying factor, and must be cumulated to the global one defined by the GAIN attribute.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_Ascan<m>,N_TCG<m> ]` | **Required:** No | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-phased_array_setup"><code>PHASED_ARRAY_SETUP</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-transmit_law"><code>TRANSMIT_LAW</code></strong> &mdash; Each A-scan in a dataframe must be associated with both a transmit and a receive focal law through the datafields.</div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ</div></summary>

<div class="field-content" markdown="1">

Each A-scan in a dataframe must be associated with both a transmit and a receive focal law through the datafields. These contain HDF5 references  to the groups which provide the detailed description of each focal laws (the same structure is used for both transmit and receive focal laws). Mandatory for phased array setups.

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ</span> | **Dimensions:** `[N_Ascan<m>] or [N_DF<m>,N_Ascan<m>]` | **Required:** Yes | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ultrasonic_setup-receive_law"><code>RECEIVE_LAW</code></strong> &mdash; Each A-scan in a dataframe must be associated with both a transmit and a receive focal law through the datafields.</div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ</div></summary>

<div class="field-content" markdown="1">

Each A-scan in a dataframe must be associated with both a transmit and a receive focal law through the datafields. These contain HDF5 references  to the groups which provide the detailed description of each focal laws (the same structure is used for both transmit and receive focal laws).Mandatory for phased array setups.

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ</span> | **Dimensions:** `[N_Ascan<m>] or [N_DF<m>,N_Ascan<m>]` | **Required:** No | **Storage:** dataset

</div>
</details>

</div>
