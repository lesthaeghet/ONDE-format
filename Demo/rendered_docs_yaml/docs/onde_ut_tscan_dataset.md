# ONDE_UT_TSCAN_DATASET


```mermaid
classDiagram
  ONDE_UT_DATASET <|-- ONDE_UT_TSCAN_DATASET
  ONDE_UT_TSCAN_DATASET o-- ONDE_ACQUISITION_TRAJECTORY : REFERENCE_TRAJECTORY
  ONDE_UT_TSCAN_DATASET o-- ONDE_UT_ASCAN_DATASET : ELEMENTARY_CHANNELS_DATASET
  click ONDE_UT_DATASET href "onde_ut_dataset.html"
  click ONDE_UT_ASCAN_DATASET href "onde_ut_ascan_dataset.html"
  click ONDE_ACQUISITION_TRAJECTORY href "onde_acquisition_trajectory.html"
  click ONDE_UT_TSCAN_DATASET href "onde_ut_tscan_dataset.html"
```


### Tscan datasets

**General**

Even though the name (Tscans coming from TFM Scans) implicitly refers to the TFM reconstruction images, the block can
apply to any reconstruction method producing data on a rectangular/parallelepiped grid that moves with the sensor (be it
obtained by TFM, Adaptive TFM, PWI, Adaptive PWI, frequency reconstruction, or any variant of these methods)

**3D Zones**

The format allows for the description of 3D zones. Taking into account the dimension related to positions, this implies
that the dimension of the data array depends on the zone dimension (3D array for 2D zones 4D array for 3D zones),

**Zone dimension and position**

The zone physical dimension is given by the ZONE_DIMENSION field, (DX,DY,DZ) being the physical dimensions of the zone,
a zero or a NaN for one of the dimension implies a 2D zone.

ZONE_SIZE is a triplet which gives the number of pixels of the zone for each dimension (NX,NY,NZ).

The zone position is given by ZONE_FRAME and is expressed relatively to the trajectory frame pointed to by
REFERENCE_TRAJECTORY.

![Example of TFM zone positioning](images/media/figure5.png "Figure 5")

*Figure 5: Example of TFM zone positioning*

In the example displayed in Figure 5, the trajectory frame is located at the index point and the zone is positioned
accordingly.

**Pixel ordering**

The pixels are stored in the (X,Y,Z) order (X being the outer loop, Z the inner loop in the array)


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_tscan_dataset-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[2]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_UT_DATASET","ONDE_UT_TSCAN_DATASET`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_tscan_dataset-data"><code>DATA</code></strong> &mdash; can be either an array or a reference to an array</div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ or HT5_INTEGER</div></summary>

<div class="field-content" markdown="1">

can be either an array or a reference to an array

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ or HT5_INTEGER</span> | **Dimensions:** `1 or [N_DF<m>,N_ROW<m>,N_COL<m>] or [N_DF<m>,NROW<m>,NCOL<m>,N_PLANE<m>]` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_tscan_dataset-reference_trajectory"><code>REFERENCE_TRAJECTORY</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_ACQUISITION_TRAJECTORY](onde_acquisition_trajectory.md)&gt;</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_ACQUISITION_TRAJECTORY](onde_acquisition_trajectory.md)&gt;</span> | **Dimensions:** `1` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_tscan_dataset-zone_frame"><code>ZONE_FRAME</code></strong> &mdash; frame associated with the center of the image zone</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

frame associated with the center of the image zone

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[7]` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_tscan_dataset-zone_dimension"><code>ZONE_DIMENSION</code></strong> &mdash; physical dimension of the zone</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

physical dimension of the zone

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[3]` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_tscan_dataset-zone_size"><code>ZONE_SIZE</code></strong> &mdash; number of pixels of the zone</div><div class="field-summary-bottom" markdown="span">H5T_INTEGER</div></summary>

<div class="field-content" markdown="1">

number of pixels of the zone

---

**Type:** <span markdown="span">H5T_INTEGER</span> | **Dimensions:** `[3]` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_tscan_dataset-reconstruction_mode"><code>RECONSTRUCTION_MODE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_tscan_dataset-elementary_channels_dataset"><code>ELEMENTARY_CHANNELS_DATASET</code></strong> &mdash; optional reference to the elementary channels ascans that were used for the reconstruction</div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_UT_ASCAN_DATASET](onde_ut_ascan_dataset.md)&gt;</div></summary>

<div class="field-content" markdown="1">

optional reference to the elementary channels ascans that were used for the reconstruction

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ&lt;[ONDE_UT_ASCAN_DATASET](onde_ut_ascan_dataset.md)&gt;</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

</div>
