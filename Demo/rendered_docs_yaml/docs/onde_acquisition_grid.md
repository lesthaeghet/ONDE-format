# ONDE_ACQUISITION_GRID


```mermaid
classDiagram
  ONDE_ACQUISITION_TRAJECTORY <|-- ONDE_ACQUISITION_GRID
  ONDE_SPATIAL_TRAJECTORY <|-- ONDE_ACQUISITION_GRID
  click ONDE_ACQUISITION_GRID href "onde_acquisition_grid.html"
  click ONDE_SPATIAL_TRAJECTORY href "onde_spatial_trajectory.html"
  click ONDE_ACQUISITION_TRAJECTORY href "onde_acquisition_trajectory.html"
```


No narrative documentation provided for ONDE_ACQUISITION_GRID.


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_acquisition_grid-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[3]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_ACQUISITION_TRAJECTORY","ONDE_SPATIAL_TRAJECTORY","ONDE_ACQUISITION_GRID`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_acquisition_grid-reference_specimen"><code>REFERENCE_SPECIMEN</code></strong> &mdash; When defining an acquisition grid, it is necessary to define a reference specimen that is either a cylinder or a plane.</div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ</div></summary>

<div class="field-content" markdown="1">

When defining an acquisition grid, it is necessary to define a reference specimen that is either a cylinder or a plane.

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_acquisition_grid-cylinder_definition"><code>CYLINDER_DEFINITION</code></strong> &mdash; Defines whether the grid is expressed in the inner surface of the cylinder or on the outer surface</div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

Defines whether the grid is expressed in the inner surface of the cylinder or on the outer surface

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `` | **Required:** No | **Storage:** attribute | **Allowed:** `"INNER"\|"OUTER"`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_acquisition_grid-uv_grid_frame"><code>UV_GRID_FRAME</code></strong> &mdash; 2D Frame defining the U_GRID and V_GRID directions of the encoding in the surface representation of the specimen (X,Y) for planar specimens, (X,THETA) for cylindrical specimens.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

2D Frame defining the U_GRID and V_GRID directions of the encoding in the surface representation of the specimen (X,Y) for planar specimens, (X,THETA) for cylindrical specimens. (1,0,) is assumed if missing

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[3]` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_acquisition_grid-u_grid_data"><code>U_GRID_DATA</code></strong> &mdash; The specified values of the first coder at the different positions</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

The specified values of the first coder at the different positions

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_U<m>]` | **Required:** Yes | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_acquisition_grid-v_grid_data"><code>V_GRID_DATA</code></strong> &mdash; The specified values of the second coder at the different positions.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

The specified values of the second coder at the different positions. If missing while U_GRID_DATA is present, 1D array of data is assumed.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_V<m>]` | **Required:** No | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_acquisition_grid-scan_type"><code>SCAN_TYPE</code></strong> &mdash; Defines whether the data is ordered in the same direction for each scan (COMB) or is inversed every second scan (RASTER)</div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

Defines whether the data is ordered in the same direction for each scan (COMB) or is inversed every second scan (RASTER)

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute | **Allowed:** `"COMB"\|"RASTER"`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_acquisition_grid-u_encoder"><code>U_ENCODER</code></strong> &mdash; Obtained encoder values on the u axis</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

Obtained encoder values on the u axis

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_V<m>,N_U<m>]` | **Required:** No | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_acquisition_grid-v_encoder"><code>V_ENCODER</code></strong> &mdash; Obtained encoder values on the v axis</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

Obtained encoder values on the v axis

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[N_V<m>,N_U<m>]` | **Required:** No | **Storage:** dataset

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_acquisition_grid-probe_direction"><code>PROBE_DIRECTION</code></strong> &mdash; For grid data, direction of the probe in the (u,v,w) coordinate system.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

For grid data, direction of the probe in the (u,v,w) coordinate system. Defaults to identity matrix.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[3,3]` | **Required:** No | **Storage:** dataset

</div>
</details>

</div>
