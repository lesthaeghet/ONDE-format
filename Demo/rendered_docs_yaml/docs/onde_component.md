# ONDE_COMPONENT


```mermaid
classDiagram
  ONDE_COMPONENT <|-- ONDE_2DCAD
  ONDE_COMPONENT <|-- ONDE_3DCAD
  ONDE_COMPONENT <|-- ONDE_CYLINDER
  ONDE_COMPONENT <|-- ONDE_PLANE
  ONDE_COMPONENT <|-- ONDE_WELD
  click ONDE_CYLINDER href "onde_cylinder.html"
  click ONDE_2DCAD href "onde_2dcad.html"
  click ONDE_COMPONENT href "onde_component.html"
  click ONDE_3DCAD href "onde_3dcad.html"
  click ONDE_WELD href "onde_weld.html"
  click ONDE_PLANE href "onde_plane.html"
```


The component block describes the inspected specimen, including its material properties, geometry, and positioning within the reference frame. This version of the format handles only isotropic materials.

The geometric shape of the inspected component is defined by the subclass of ONDE_COMPONENT. It can be one of the following: "ONDE_PLANE","ONDE_CYLINDER", "ONDE_2DCAD", "ONDE_3DCAD", "ONDE_WELD". While the format is quite generic by handling CAD files, parametric description is available for plane, cylindrical and weld specimens.

### Conventions for planar specimens
In the planar coordinate system, the z direction is defined as the one corresponding to the thickness of the inspected specimen (see Figure 6). The dimensions are given by PLATE_DIMENSIONS, as a triplet with values for length, width, and thickness.

![Trajectory planar coordinate system convention](images/media/figure6.png "Figure 6")

### Conventions for cylindrical components
In the cylindrical coordinate system, the x direction is the one corresponding to the cylinder axis (see Figure 7). The dimensions are given by CYLINDER_DIMENSIONS, with a triplet for outer diameter, thickness, and length.

![Trajectory cylindrical coordinate system convention](images/media/figure7.png "Figure 7")

### Conventions for 2D CAD components
The dxf file gives, in the (X, Z) frame, the 2D CAD description of the component, either for a planar or a cylindrical extrusion. For 2D extruded components, extrusion is provided by EXTRUSION_TYPE (plane or sylindrical) and EXTRUSION_DIMENSION for the length for plane extrusion, the diameter for cylindrical ones.

For 2D CAD specimen with planar extrusion, the origin is implicitly defined as the (0,0) point in the 2D CAD sketch (see Figure 8).

![Convention for the description of a 2D CAD component with planar extrusion](images/media/figure8.png "Figure 8")

For 2D CAD specimen with cylinder extrusion, the rotation is performed along the X axis of the DXF schema and the 3D origin corresponds to the projection on this axis of the 2D CAD sketch origin (see Figure 9)

![Convention for the description of a 2D CAD component with cylinder extrusion](images/media/figure9.png "Figure 9")

### Visualization CAD Conventions
When a dxf is provided for the Visualization CAD, the extrusion of the CAD is implied from the specimen shape : it is of linear nature if the specimen is a plate or a 2D CAD with linear extrusion, it is cylindrical if the specimen is a cylinder or a 2D CAD with cylindrical extrusion.

The CAD profiles that are used for visualization are expressed in the (X,Z) plane as specified in the specimen frame.

![Convention for the positioning of the visualization CAD in a planar component](images/media/figure10.png "Figure 10")

![Convention for the positioning of the visualization CAD in a cylindrical component](images/media/figure11.png "Figure 11")



## Fields

<div class="field-list" markdown="1">

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_component-type"><code>TYPE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `` | **Required:** Yes | **Storage:** attribute | **Allowed:** `ONDE_COMPONENT`

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_component-label"><code>LABEL</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_component-velocities"><code>VELOCITIES</code></strong> &mdash; The two values of the VELOCITIES array indicate the inspected component longitudinal and shear wave velocity respectively.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

The two values of the VELOCITIES array indicate the inspected component longitudinal and shear wave velocity respectively. If both velocities are not available, the missing one should be replaced by a NaN.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[2]` | **Required:** Yes | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_component-density"><code>DENSITY</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_component-visualization_cad"><code>VISUALIZATION_CAD</code></strong> &mdash; VISUALISATION_CAD contains a DXF or STL file for the component visualization.</div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

VISUALISATION_CAD contains a DXF or STL file for the component visualization. When using a dxf file, the profile will be extruded linearly or cylindrically according to the component type.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_component-visualization_cad_frame"><code>VISUALIZATION_CAD_FRAME</code></strong> &mdash; Definition of the frame defining the visualisation CAD with offset and quaternions in the specimen frame- Identity is used if absent</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

Definition of the frame defining the visualisation CAD with offset and quaternions in the specimen frame- Identity is used if absent

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[7]` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_component-component_frame"><code>COMPONENT_FRAME</code></strong> &mdash; The global coordinate system is distinct from the specimen coordinate system: 2D and 3D CAD coordinates are defined in the specimen frame and repositioned in the global coordinate system with the transformation defined in COMPONENT_FRAME.</div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

The global coordinate system is distinct from the specimen coordinate system: 2D and 3D CAD coordinates are defined in the specimen frame and repositioned in the global coordinate system with the transformation defined in COMPONENT_FRAME. Default value is identity with the reference frame.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[7]` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_component-comment"><code>COMMENT</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_STRING</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_STRING</span> | **Dimensions:** `1` | **Required:** No | **Storage:** attribute

</div>
</details>

<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="onde_component-image"><code>IMAGE</code></strong> &mdash; </div><div class="field-summary-bottom" markdown="span">H5T_FLOAT</div></summary>

<div class="field-content" markdown="1">

No detailed description provided.

---

**Type:** <span markdown="span">H5T_FLOAT</span> | **Dimensions:** `[3]` | **Required:** No | **Storage:** attribute

</div>
</details>

</div>
