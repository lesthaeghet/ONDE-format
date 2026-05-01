# ONDE_UT_ELEMENTS


```mermaid
classDiagram
  click ONDE_UT_ELEMENTS href "onde_ut_elements.html"
```


No narrative documentation provided for ONDE_UT_ELEMENTS.


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_elements-type_tags"><code>TYPE_TAGS</code></strong> &mdash; Defines the ONDE_UT_ELEMENTS accessory class</div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

Defines the ONDE_UT_ELEMENTS accessory class

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[1]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_UT_ELEMENTS`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_elements-frame"><code>FRAME</code></strong> &mdash; Array defining the location of the elements of the probe</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

Array defining the location of the elements of the probe

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_Elem<p>,7]` | **Required:** Yes | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_elements-shape"><code>SHAPE</code></strong> &mdash; The shape of each element will be defined as one of the following: rectangle (ELE_GEOM_REC), part of a ring (ELE_GEOM_RING_PART), part of an elliptical ring (ELE_GEOM_ELLIPSE_PART),</div><div class="field-summary-bottom" markdown="span">H5T_INTEGER</div></summary>

<div class="field-content" markdown="1">

The shape of each element will be defined as one of the following: rectangle (ELE_GEOM_REC), part of a ring (ELE_GEOM_RING_PART), part of an elliptical ring (ELE_GEOM_ELLIPSE_PART),

---

**Type:** <span markdown="span">H5T_INTEGER</span> | **Dimensions:** `[N_Elem<p>]` | **Required:** Yes | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_elements-size"><code>SIZE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_Elem<p>,6]` | **Required:** Yes | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_elements-radius_of_curvature"><code>RADIUS_OF_CURVATURE</code></strong> &mdash; If absent, flat elements are assumed</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

If absent, flat elements are assumed

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_Elem<p>]` | **Required:** No | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_elements-axis_of_curvature"><code>AXIS_OF_CURVATURE</code></strong> &mdash; If absent, flat elements are assumed</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

If absent, flat elements are assumed

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_Elem<p>,3]` | **Required:** No | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_elements-dead_element"><code>DEAD_ELEMENT</code></strong> &mdash; Datafield of logical values (0 = false, 1 = true) used to flag non-functioning elements in an array probe (if not present, assumption should be that all elements are performing correctly);</div><div class="field-summary-bottom" markdown="span">H5T_INTEGER</div></summary>

<div class="field-content" markdown="1">

Datafield of logical values (0 = false, 1 = true) used to flag non-functioning elements in an array probe (if not present, assumption should be that all elements are performing correctly);

---

**Type:** <span markdown="span">H5T_INTEGER</span> | **Dimensions:** `[N_Elem<p>]` | **Required:** No | **Storage:** dataset

</div>
</details>

</div>
