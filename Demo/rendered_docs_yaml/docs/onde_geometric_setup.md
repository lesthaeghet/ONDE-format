# ONDE_GEOMETRIC_SETUP


```mermaid
classDiagram
  ONDE_GEOMETRIC_SETUP o-- ONDE_COMPONENT : COMPONENT
  ONDE_GEOMETRIC_SETUP o-- ONDE_UT_PROBE : PROBE_LIST
  ONDE_GEOMETRIC_SETUP o-- ONDE_ACQUISITION_TRAJECTORY : ACQUISITION_TRAJECTORY
  click ONDE_GEOMETRIC_SETUP href "onde_geometric_setup.html"
  click ONDE_ACQUISITION_TRAJECTORY href "onde_acquisition_trajectory.html"
  click ONDE_UT_PROBE href "onde_ut_probe.html"
  click ONDE_COMPONENT href "onde_component.html"
```


### Geometric setup

**Description**

The geometric setup contains references to the inspected component, the probes and the trajectory. If the specimen
description is missing, a semi-infinite half-plane is assumed, with interface at z=0 and material for z>0.

**Trajectories**

ACQUISITION_TRAJECTORY gives references to the groups describing the trajectory -- references have the same order as
PROBE_LIST. PROBE_COORDINATE_FRAME can be used to define an offset between a referenced trajectory and the probe -
identity is assumed if not provided.


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_geometric_setup-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_GEOMETRIC_SETUP`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_geometric_setup-component"><code>COMPONENT</code></strong> &mdash; Reference to the inspected component.</div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_COMPONENT](onde_component.md)&gt;</div></summary>

<div class="field-content" markdown="1">

Reference to the inspected component. If missing, semi-infinite half plane is assumed, with interface at z=0 and material for z>0

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_COMPONENT](onde_component.md)&gt;</span> | **Dimensions:** `[1]` | **Required:** No | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_geometric_setup-probe_list"><code>PROBE_LIST</code></strong> &mdash; List all probes used in the acquisition of the dataset</div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_UT_PROBE](onde_ut_probe.md)&gt;</div></summary>

<div class="field-content" markdown="1">

List all probes used in the acquisition of the dataset

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_UT_PROBE](onde_ut_probe.md)&gt;</span> | **Dimensions:** `[N_Prob<M>]` | **Required:** Yes | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_geometric_setup-acquisition_trajectory"><code>ACQUISITION_TRAJECTORY</code></strong> &mdash; References  to the block describing the trajectory  references have the same order as PROBE_LIST</div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_ACQUISITION_TRAJECTORY](onde_acquisition_trajectory.md)&gt;</div></summary>

<div class="field-content" markdown="1">

References  to the block describing the trajectory  references have the same order as PROBE_LIST

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_ACQUISITION_TRAJECTORY](onde_acquisition_trajectory.md)&gt;</span> | **Dimensions:** `[N_Prob<M>]` | **Required:** Yes | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_geometric_setup-probe_coordinate_frame"><code>PROBE_COORDINATE_FRAME</code></strong> &mdash; Offset and direction of the probe w.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

Offset and direction of the probe w.r.t the trajectory frame- identity  is assumed if not provided

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_Prob<M>,7]` | **Required:** No | **Storage:** dataset

</div>
</details>

</div>
