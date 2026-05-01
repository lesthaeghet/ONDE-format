# ONDE_SETUP


```mermaid
classDiagram
  ONDE_SETUP o-- ONDE_ULTRASONIC_SETUP : ULTRASONIC_SETUP
  ONDE_SETUP o-- ONDE_PHASED_ARRAY_SETUP : PHASED_ARRAY_SETUP
  ONDE_SETUP o-- ONDE_GEOMETRIC_SETUP : GEOMETRIC_SETUP
  click ONDE_ULTRASONIC_SETUP href "onde_ultrasonic_setup.html"
  click ONDE_GEOMETRIC_SETUP href "onde_geometric_setup.html"
  click ONDE_PHASED_ARRAY_SETUP href "onde_phased_array_setup.html"
  click ONDE_SETUP href "onde_setup.html"
```



### Setup

**Setup**

This group contains references to the geometric setup and ultrasonic setup. The reference to the ultrasonic setup is
compulsory for the A-scan data. For TScans, it is allowed to bypass this ultrasonic setup and have a direct reference to
the phased array setup (in order to store the reconstruction information without storing the information related to the
acquisition).


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_setup-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_SETUP`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_setup-ultrasonic_setup"><code>ULTRASONIC_SETUP</code></strong> &mdash; Mandatory for Ascan sequences</div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_ULTRASONIC_SETUP](onde_ultrasonic_setup.md)&gt;</div></summary>

<div class="field-content" markdown="1">

Mandatory for Ascan sequences

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_ULTRASONIC_SETUP](onde_ultrasonic_setup.md)&gt;</span> | **Dimensions:** `[1]` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_setup-phased_array_setup"><code>PHASED_ARRAY_SETUP</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_PHASED_ARRAY_SETUP](onde_phased_array_setup.md)&gt;</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_PHASED_ARRAY_SETUP](onde_phased_array_setup.md)&gt;</span> | **Dimensions:** `[1]` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_setup-geometric_setup"><code>GEOMETRIC_SETUP</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_GEOMETRIC_SETUP](onde_geometric_setup.md)&gt;</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_GEOMETRIC_SETUP](onde_geometric_setup.md)&gt;</span> | **Dimensions:** `[1]` | **Required:** Yes | **Storage:** attribute

</div>
</details>

</div>
