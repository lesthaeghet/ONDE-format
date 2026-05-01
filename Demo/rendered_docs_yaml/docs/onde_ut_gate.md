# ONDE_UT_GATE


```mermaid
classDiagram
  click ONDE_UT_GATE href "onde_ut_gate.html"
```


No narrative documentation provided for ONDE_UT_GATE.


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_gate-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[1]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_UT_GATE`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_gate-start"><code>START</code></strong> &mdash; For scalar data relying on Ascan data, defines the start time for the gate.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

For scalar data relying on Ascan data, defines the start time for the gate. Mandatory for data related to Ascans.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_gate-width"><code>WIDTH</code></strong> &mdash; For Cscans scalar data relying on Ascan data, defines the width of the gate.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

For Cscans scalar data relying on Ascan data, defines the width of the gate. Mandatory for data related to Ascans

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_gate-threshold"><code>THRESHOLD</code></strong> &mdash; Defines the threshold of the gate for data to be stored</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

Defines the threshold of the gate for data to be stored

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_gate-detection"><code>DETECTION</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute | **Allowed:** `" FIRST_PEAK"\|"LAST_PEAK"\|" MAX_PEAK"\|" FIRST_FLANK"\|"LAST_FLANK"`

</div>
</details>

</div>
