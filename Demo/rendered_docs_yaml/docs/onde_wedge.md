# ONDE_WEDGE


```mermaid
classDiagram
  ONDE_UT_COUPLING <|-- ONDE_WEDGE
  ONDE_WEDGE <|-- ONDE_DUAL_WEDGE
  click ONDE_UT_COUPLING href "onde_ut_coupling.html"
  click ONDE_WEDGE href "onde_wedge.html"
  click ONDE_DUAL_WEDGE href "onde_dual_wedge.html"
```


No narrative documentation provided for ONDE_WEDGE.


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_wedge-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[2]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_UT_COUPLING","ONDE_WEDGE`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_wedge-label"><code>LABEL</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_wedge-manufacturer"><code>MANUFACTURER</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_wedge-serial_number"><code>SERIAL_NUMBER</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_wedge-contact_surface"><code>CONTACT_SURFACE</code></strong> &mdash; Type of the wedge contact surface - PLANAR, SPHERICAL, CYLINDRICAL_MAJOR, CYLINDRICAL_MINOR - If missing PLANAR assumed</div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

Type of the wedge contact surface - PLANAR, SPHERICAL, CYLINDRICAL_MAJOR, CYLINDRICAL_MINOR - If missing PLANAR assumed

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `` | **Required:** Yes | **Storage:** attribute | **Allowed:** `"PLANAR"\|"SPHERICAL"\|"CYLINDRICAL_MAJOR"\|"CYLINDRICAL_MINOR"`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_wedge-curvature_radius"><code>CURVATURE_RADIUS</code></strong> &mdash; Wedge curvature radius - Concave : positive - Convex : negative - 0 in the case of a planar wedge - If missing 0 assumed.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

Wedge curvature radius - Concave : positive - Convex : negative - 0 in the case of a planar wedge - If missing 0 assumed.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_wedge-contact_area"><code>CONTACT_AREA</code></strong> &mdash; Equivalent to L1, L2 and L3 (See Figure 15)</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

Equivalent to L1, L2 and L3 (See Figure 15)

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[3]` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_wedge-height"><code>HEIGHT</code></strong> &mdash; For a wedge, distance of the ultrasonic beam between the probe center and the index point (See Figure 15)</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

For a wedge, distance of the ultrasonic beam between the probe center and the index point (See Figure 15)

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_wedge-skew_angle"><code>SKEW_ANGLE</code></strong> &mdash; wedge /skew angle (B) (See Figure 15)</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

wedge /skew angle (B) (See Figure 15)

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_wedge-disorientation_angle"><code>DISORIENTATION_ANGLE</code></strong> &mdash; wedge /disorientation angle (D) (See Figure 15)</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

wedge /disorientation angle (D) (See Figure 15)

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

</div>
