# ONDE_TIME_TRAJECTORY


```mermaid
classDiagram
  ONDE_ACQUISITION_TRAJECTORY <|-- ONDE_TIME_TRAJECTORY
  click ONDE_TIME_TRAJECTORY href "onde_time_trajectory.html"
  click ONDE_ACQUISITION_TRAJECTORY href "onde_acquisition_trajectory.html"
```


No narrative documentation provided for ONDE_TIME_TRAJECTORY.


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_time_trajectory-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[2]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_ACQUISITION_TRAJECTORY","ONDE_TIME_TRAJECTORY`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_time_trajectory-acquisition_rate"><code>ACQUISITION_RATE</code></strong> &mdash; For time encoded trajectories, defines the acquisition rate</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

For time encoded trajectories, defines the acquisition rate

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

</div>
