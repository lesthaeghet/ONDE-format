# ONDE_UT_LAW


```mermaid
classDiagram
  click ONDE_UT_LAW href "onde_ut_law.html"
```


### Law

For multielements, these groups describe the settings of a given transmit or receive law. PROBE and ELEMENT give the
probe and element number to which the DELAY and WEIGHTING apply.

The format also allows to store an information about the corresponding ultrasonic path.

PROPAGATION_LINE represents the ultrasonic ray along which the data is to be represented in a true visualisation. It
contains at least two points in the Probe Coordinates Frame corresponding to the start and end of the ray. (x,y,z)
positions in Probe Coordinate Frame and time of flight are stored.


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_law-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_UT_LAW`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_law-probe"><code>PROBE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ</span> | **Dimensions:** `[N_C<k>]` | **Required:** Yes | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_law-element"><code>ELEMENT</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_INTEGER</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_INTEGER</span> | **Dimensions:** `[N_C<k>]` | **Required:** Yes | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_law-delay"><code>DELAY</code></strong> &mdash; Specifies the relative delay (in ultrasonic time) between the different Probe Element Combinations in the focal law.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

Specifies the relative delay (in ultrasonic time) between the different Probe Element Combinations in the focal law. The default value is zero delay for all Probe Element Combinations.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_C<k>]` | **Required:** No | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_law-weighting"><code>WEIGHTING</code></strong> &mdash; Specifies the weighting between the different Probe Element Combinations in the focal law.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

Specifies the weighting between the different Probe Element Combinations in the focal law. The default is one for all Probe Element Combinations.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_C<k>]` | **Required:** No | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_law-propagation_line"><code>PROPAGATION_LINE</code></strong> &mdash; Represents the ultrasonic ray along which the data is to be represented in a true visualisation.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

Represents the ultrasonic ray along which the data is to be represented in a true visualisation. It contains at least two points in the Probe Coordinates Frame corresponding to the start and end of the ray. (x,y,z) positions in Probe Coordinate Frame and time of flight are stored).

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_Points<k>,4]` | **Required:** No | **Storage:** dataset

</div>
</details>

</div>
