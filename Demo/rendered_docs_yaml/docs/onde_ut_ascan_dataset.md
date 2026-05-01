# ONDE_UT_ASCAN_DATASET


```mermaid
classDiagram
  ONDE_UT_DATASET <|-- ONDE_UT_ASCAN_DATASET
  click ONDE_UT_DATASET href "onde_ut_dataset.html"
  click ONDE_UT_ASCAN_DATASET href "onde_ut_ascan_dataset.html"
```


### Ascan datasets

Ascan datasets are the entry points for the description of data that is stored as time signals. The MFMC equivalent is '
SEQUENCE', and both names are allowed to ensure compatibility.

To allow continuity with existing HDF5 formats, the DATA field can be either a HDF5 dataset or a reference to a
dataset located in another part of the HDF5 structure.


## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_ascan_dataset-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `[2]` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_UT_DATASET","ONDE_UT_ASCAN_DATASET`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_ut_ascan_dataset-data"><code>DATA</code></strong> &mdash; can be either an array or a reference to an array</div><div class="field-summary-bottom" markdown="span">H5T_STD_REF_OBJ&lt;data&gt; or HT5_INTEGER or H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

can be either an array or a reference to an array

---

**Type:** <span markdown="span">H5T_STD_REF_OBJ&lt;data&gt; or HT5_INTEGER or H5T_FLOAT</span> | **Dimensions:** `1 or [N_DF<m>,N_Ascan<m>,Ntime<m>]` | **Required:** Yes | **Storage:** attribute

</div>
</details>

</div>
