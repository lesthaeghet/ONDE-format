# ONDE_SPATIAL_TRAJECTORY


```mermaid
classDiagram
  ONDE_ACQUISITION_TRAJECTORY <|-- ONDE_SPATIAL_TRAJECTORY
  ONDE_SPATIAL_TRAJECTORY <|-- ONDE_ACQUISITION_GRID
  click ONDE_ACQUISITION_GRID href "onde_acquisition_grid.html"
  click ONDE_SPATIAL_TRAJECTORY href "onde_spatial_trajectory.html"
  click ONDE_ACQUISITION_TRAJECTORY href "onde_acquisition_trajectory.html"
```


No narrative documentation provided for ONDE_SPATIAL_TRAJECTORY.


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_spatial_trajectory-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[2]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_ACQUISITION_TRAJECTORY","ONDE_SPATIAL_TRAJECTORY`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_spatial_trajectory-trajectory"><code>TRAJECTORY</code></strong> &mdash; List of positions and quaternions   giving the positions and orientations of the trajectory frame    at the different positions</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

List of positions and quaternions   giving the positions and orientations of the trajectory frame    at the different positions

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_Pos<m>,7]` | **Required:** No | **Storage:** dataset

</div>
</details>

</div>
