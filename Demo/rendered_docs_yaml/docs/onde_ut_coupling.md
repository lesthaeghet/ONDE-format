# ONDE_UT_COUPLING


```mermaid
classDiagram
  ONDE_UT_COUPLING <|-- ONDE_DUAL_WEDGE
  ONDE_UT_COUPLING <|-- ONDE_IMMERSION
  ONDE_UT_COUPLING <|-- ONDE_SINGLE_WEDGE
  ONDE_UT_COUPLING <|-- ONDE_WEDGE
  click ONDE_IMMERSION href "onde_immersion.html"
  click ONDE_UT_COUPLING href "onde_ut_coupling.html"
  click ONDE_SINGLE_WEDGE href "onde_single_wedge.html"
  click ONDE_WEDGE href "onde_wedge.html"
  click ONDE_DUAL_WEDGE href "onde_dual_wedge.html"
```


No narrative documentation provided for ONDE_UT_COUPLING.


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_coupling-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[1]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_UT_COUPLING`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_coupling-medium_velocity"><code>MEDIUM_VELOCITY</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[2]` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_coupling-medium_density"><code>MEDIUM_DENSITY</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_coupling-incidence_angle"><code>INCIDENCE_ANGLE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

</div>
