# ONDE_PHASED_ARRAY_ESCAN


```mermaid
classDiagram
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_ESCAN
  click ONDE_PHASED_ARRAY_SETUP href "onde_phased_array_setup.html"
  click ONDE_PHASED_ARRAY_ESCAN href "onde_phased_array_escan.html"
```


In this configuration consecutive subsets of elements are used in order to form a beam at a specific angle, thus forming a sweeping set of ultrasonic beams. Figure 26 illustrates an Escan for 4 consecutive elements with a step of 3 elements on a 32 element linear transducer.
![EScan configuration](images/media/figure26.png "Figure 26")


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_escan-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[2]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_PHASED_ARRAY_SETUP","ONDE_PHASED_ARRAY_ESCAN`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_escan-number_of_elements"><code>NUMBER_OF_ELEMENTS</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_INTEGER</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_INTEGER</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_escan-step"><code>STEP</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_INTEGER</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_INTEGER</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_escan-angle"><code>ANGLE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

</div>
