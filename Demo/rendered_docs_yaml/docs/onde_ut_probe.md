# ONDE_UT_PROBE


```mermaid
classDiagram
  ONDE_UT_PROBE <|-- ONDE_LINEAR_UT_PROBE
  ONDE_UT_PROBE <|-- ONDE_MATRIX_UT_PROBE
  ONDE_UT_PROBE <|-- ONDE_MONO_UT_PROBE
  ONDE_UT_PROBE o-- ONDE_UT_COUPLING : COUPLING
  click ONDE_MATRIX_UT_PROBE href "onde_matrix_ut_probe.html"
  click ONDE_LINEAR_UT_PROBE href "onde_linear_ut_probe.html"
  click ONDE_UT_COUPLING href "onde_ut_coupling.html"
  click ONDE_MONO_UT_PROBE href "onde_mono_ut_probe.html"
  click ONDE_UT_PROBE href "onde_ut_probe.html"
```


No narrative documentation provided for ONDE_UT_PROBE.


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_probe-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[1]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_UT_PROBE`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_probe-type_tags"><code>TYPE_TAGS</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[1]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_UT_ELEMENTS`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_probe-label"><code>LABEL</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_probe-index_point_frame"><code>INDEX_POINT_FRAME</code></strong> &mdash; If absent, identity is assumed</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

If absent, identity is assumed

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[7]` | **Required:** No | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_probe-manufacturer"><code>MANUFACTURER</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_probe-serial_number"><code>SERIAL_NUMBER</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_probe-frequency"><code>FREQUENCY</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_probe-bandwidth"><code>BANDWIDTH</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_probe-focusing_surface"><code>FOCUSING_SURFACE</code></strong> &mdash; Defines the shape of the surface on which the elements are arranged - if absent, FLAT is assumed</div><div class="field-summary-bottom" markdown="span">H5T_INTEGER</div></summary>

<div class="field-content" markdown="1">

Defines the shape of the surface on which the elements are arranged - if absent, FLAT is assumed

---

**Type:** <span markdown="span">H5T_INTEGER</span> | **Dimensions:** `` | **Required:** No | **Storage:** attribute | **Allowed:** `"FLAT"\|"CYLINDRICAL_INC"\|"CYLINDRICAL_PERP"\|"SPHERICAL"\|"BIFOCAL"\|"TRIFOCAL"`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_probe-focusing_surface_parameters"><code>FOCUSING_SURFACE_PARAMETERS</code></strong> &mdash; Multi values : value in mm - FLAT : no value - CYLINDRICAL_INC, CYLINDRICAL_PER : Surface radius - SPHERICAL : Surface radius - BIFOCAL : Surface radius in the incidence plane, surface radius in the plane perpendicular to the incidence plane - TRIFOCAL : Surface radius in the incidence plane (bottom), Surface radius in the incidence plane (top), surface radius in the plane perpendicular to the incidence plane.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

Multi values : value in mm - FLAT : no value - CYLINDRICAL_INC, CYLINDRICAL_PER : Surface radius - SPHERICAL : Surface radius - BIFOCAL : Surface radius in the incidence plane, surface radius in the plane perpendicular to the incidence plane - TRIFOCAL : Surface radius in the incidence plane (bottom), Surface radius in the incidence plane (top), surface radius in the plane perpendicular to the incidence plane.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[3]` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_probe-coupling"><code>COUPLING</code></strong> &mdash; Reference to the coupling system (wedge, immersion, direct)</div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_UT_COUPLING](onde_ut_coupling.md)&gt;</div></summary>

<div class="field-content" markdown="1">

Reference to the coupling system (wedge, immersion, direct)

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_UT_COUPLING](onde_ut_coupling.md)&gt;</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

</div>
