# ONDE_DUAL_WEDGE


```mermaid
classDiagram
  ONDE_UT_COUPLING <|-- ONDE_DUAL_WEDGE
  ONDE_WEDGE <|-- ONDE_DUAL_WEDGE
  click ONDE_UT_COUPLING href "onde_ut_coupling.html"
  click ONDE_WEDGE href "onde_wedge.html"
  click ONDE_DUAL_WEDGE href "onde_dual_wedge.html"
```


No narrative documentation provided for ONDE_DUAL_WEDGE.


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_dual_wedge-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[3]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_UT_COUPLING","ONDE_WEDGE","ONDE_DUAL_WEDGE`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_dual_wedge-probe_separation"><code>PROBE_SEPARATION</code></strong> &mdash; For dual probes, inter-probes distance (L6) (See Figure 15)</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

For dual probes, inter-probes distance (L6) (See Figure 15)

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_dual_wedge-roof_angle"><code>ROOF_ANGLE</code></strong> &mdash; For dual probes and only for dual probes defines the roof angle (See Figure 15)</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

For dual probes and only for dual probes defines the roof angle (See Figure 15)

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_dual_wedge-squint_angle"><code>SQUINT_ANGLE</code></strong> &mdash; For dual probes, squint angle (A2) (See Figure 15)</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

For dual probes, squint angle (A2) (See Figure 15)

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

</div>
