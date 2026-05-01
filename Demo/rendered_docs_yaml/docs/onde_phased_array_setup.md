# ONDE_PHASED_ARRAY_SETUP


```mermaid
classDiagram
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_ANGLE
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_COMPOUND
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_ESCAN
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_FMC
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_PWI
  ONDE_PHASED_ARRAY_SETUP <|-- ONDE_PHASED_ARRAY_SSCAN
  click ONDE_PHASED_ARRAY_PWI href "onde_phased_array_pwi.html"
  click ONDE_PHASED_ARRAY_SSCAN href "onde_phased_array_sscan.html"
  click ONDE_PHASED_ARRAY_FMC href "onde_phased_array_fmc.html"
  click ONDE_PHASED_ARRAY_ESCAN href "onde_phased_array_escan.html"
  click ONDE_PHASED_ARRAY_ANGLE href "onde_phased_array_angle.html"
  click ONDE_PHASED_ARRAY_SETUP href "onde_phased_array_setup.html"
  click ONDE_PHASED_ARRAY_COMPOUND href "onde_phased_array_compound.html"
```


The phased array setup block describes the high-level electronic configuration for Phased Array ultrasonic testing. This optional group has no vocation to be exhaustive in terms of electronic configurations (unlike the law block that permits any description and is fully generic). However, it is intended to cover most of the situations that are common in industrial controls and represent a large share of the acquisition files produced in the industry. In this version of the specification, it encompasses only the most basic setups.

The specific sequencing (Angle, SScan, EScan, Compound, FMC, PWI) is defined by subclasses of this block. The propagation mode used for the settings is given in SEQUENCE_ANGLE_MODE.


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_setup-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_PHASED_ARRAY_SETUP`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_setup-emitter_probe"><code>EMITTER_PROBE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_setup-receiving_probe"><code>RECEIVING_PROBE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_phased_array_setup-sequence_angle_mode"><code>SEQUENCE_ANGLE_MODE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_INTEGER</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_INTEGER</span> | **Dimensions:** `` | **Required:** Yes | **Storage:** attribute | **Allowed:** `"L"\|"T"`

</div>
</details>

</div>
