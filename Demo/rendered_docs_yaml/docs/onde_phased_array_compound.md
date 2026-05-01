# ONDE_PHASED_ARRAY_COMPOUND


```mermaid
classDiagram
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_COMPOUND
  click ONDE_PHASED_ARRAY_COMPOUND href "onde_phased_array_compound.html"
  click ONDE_PHASED_ARRAY_SETUP href "onde_phased_array_setup.html"
```


The compound type mixes Escan and Sscan behavior. COMPOUND_INITIAL_ANGLE, COMPOUND_FINAL_ANGLE and COMPOUND_NUMBER_OF_ANGLES give the angle scope, while COMPOUND_NUMBER_OF_ELEMENTS gives the number of elements in the electronic scanning.
![Compound configuration](images/media/figure27.png "Figure 27")


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_compound-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[2]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_PHASED_ARRAY_SETUP","ONDE_PHASED_ARRAY_COMPOUND`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_compound-initial_angle"><code>INITIAL_ANGLE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_compound-final_angle"><code>FINAL_ANGLE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_compound-number_of_angles"><code>NUMBER_OF_ANGLES</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_INTEGER</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_INTEGER</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_compound-number_of_elements"><code>NUMBER_OF_ELEMENTS</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_INTEGER</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_INTEGER</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

</div>
