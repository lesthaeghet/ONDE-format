# ONDE_PHASED_ARRAY_SSCAN


```mermaid
classDiagram
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_SSCAN
  click ONDE_PHASED_ARRAY_SSCAN href "onde_phased_array_sscan.html"
  click ONDE_PHASED_ARRAY_SETUP href "onde_phased_array_setup.html"
```


In this configuration, the probe is configured to emit/receive at a set of angles. The angles are linearly varying, therefore the first and last angles and the number of shots define the set of angles.
![SScan configuration](images/media/figure25.png "Figure 25")


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_sscan-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[2]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_PHASED_ARRAY_SETUP","ONDE_PHASED_ARRAY_SSCAN`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_sscan-starting_angle"><code>STARTING_ANGLE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_sscan-finishing_angle"><code>FINISHING_ANGLE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_sscan-number_of_angles"><code>NUMBER_OF_ANGLES</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_INTEGER</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_INTEGER</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

</div>
