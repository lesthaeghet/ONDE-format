---
onde_class: ONDE_COMPONENT
inherits: []
---

# ONDE_COMPONENT

The component block describes the inspected specimen, including its material
properties, geometry, and positioning within the reference frame. This version
of the format handles only isotropic materials.

The geometric shape of the inspected component is defined by the subclass of
`ONDE_COMPONENT`. It can be one of the following: `ONDE_PLANE`, `ONDE_CYLINDER`,
`ONDE_2DCAD`, `ONDE_3DCAD`, `ONDE_WELD`. While the format is quite generic by
handling CAD files, parametric description is available for plane, cylindrical,
and weld specimens. Other parameterized shapes can be added in future versions.

The MFMC equivalent is the SPECIMEN block (MFMC 2.0.0b).

```mermaid
classDiagram
  component <|-- plane
  component <|-- cylinder
  component <|-- 2d_cad
  component <|-- 3d_cad
  component <|-- weld
```

## Fields

### `ONDE:TYPE`

- **Required:** Mandatory
- **Storage:** Attribute
- **Type:** `H5T_STRING`

Class type identifier.

### `ONDE:LABEL`

- **Required:** Optional
- **Storage:** Attribute
- **Type:** `H5T_STRING`

Human-readable label.

### `ONDE_COMPONENT:VELOCITIES`

- **Required:** Mandatory
- **Storage:** Attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[2]`
- **Units:** m/s

Longitudinal and shear wave velocities. The two values indicate the inspected
component longitudinal and shear wave velocity respectively. If both velocities
(Longitudinal and Shear) are not available, the missing one should be replaced
by a NaN.

> **Limitation:** This version of the format handles only isotropic materials.

### `ONDE_COMPONENT:DENSITY`

- **Required:** Optional
- **Storage:** Attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `1`
- **Units:** kg/m³

Material density.

### `ONDE_COMPONENT:VISUALIZATION_CAD`

- **Required:** Optional
- **Storage:** Attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `1`

Contains a DXF or STL file for the component visualization. When using a DXF
file, the profile will be extruded linearly or cylindrically according to the
component type.

### `ONDE_COMPONENT:VISUALIZATION_CAD_FRAME`

- **Required:** Optional
- **Storage:** Attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[7]`
- **Default:** identity

Definition of the frame defining the visualization CAD with offset and
quaternions in the specimen frame. Identity is used if absent.

See the frame conventions section for details on the 7-value frame
representation (3 offset + 4 quaternion).

### `ONDE_COMPONENT:COMPONENT_FRAME`

- **Required:** Optional
- **Storage:** Attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[7]`
- **Default:** identity

Definition of the specimen frame in the reference frame. If not provided, the
default value is identity with the reference frame.

### `ONDE_COMPONENT:COMMENT`

- **Required:** Optional
- **Storage:** Attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `1`

Free-form comment.

### `ONDE_COMPONENT:IMAGE`

- **Required:** Optional
- **Storage:** Attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[3]`

Image reference.

## Notes

### Conventions for planar specimens

In the planar coordinate system, the z direction is defined as the one
corresponding to the thickness of the inspected specimen (see Figure 6). The
dimensions are given by `ONDE_PLANE:PLATE_DIMENSIONS`, as a triplet with
values for length, width, and thickness.

![Trajectory planar coordinate system convention](../../images/media/figure6.png)

*Figure 6: Trajectory planar coordinate system convention*

### Conventions for cylindrical components

In the cylindrical coordinate system, the x direction is the one corresponding
to the cylinder axis (see Figure 7). The dimensions are given by
`ONDE_CYLINDER:DIMENSIONS`, with a triplet for outer diameter, thickness, and
length.

![Trajectory cylindrical coordinate system convention](../../images/media/figure7.png)

*Figure 7: Trajectory cylindrical coordinate system convention*

### Conventions for 2D CAD components

The DXF file gives, in the (X, Z) frame, the 2D CAD description of the
component, either for a planar or a cylindrical extrusion.

![Convention for 2D CAD component with planar extrusion](../../images/media/figure8.png)

*Figure 8: Convention for the description of a 2D CAD component with planar extrusion*

![Convention for 2D CAD component with cylinder extrusion](../../images/media/figure9.png)

*Figure 9: Convention for the description of a 2D CAD component with cylinder extrusion*

### Visualization CAD

When a DXF is provided for the Visualization CAD, the extrusion of the CAD is
implied from the specimen shape.

![Convention for visualization CAD in a planar component](../../images/media/figure10.png)

*Figure 10: Convention for the positioning of the visualization CAD in a planar component*

![Convention for visualization CAD in a cylindrical component](../../images/media/figure11.png)

*Figure 11: Convention for the positioning of the visualization CAD in a cylindrical component*

### Transformations

The global coordinate system is distinct from the specimen coordinate system:
2D and 3D CAD coordinates are defined in the specimen frame and repositioned
in the global coordinate system with the transformation defined in
`ONDE_COMPONENT:COMPONENT_FRAME`.

---

# ONDE_PLANE

---
onde_class: ONDE_PLANE
inherits: [ONDE_COMPONENT]
---

A planar component. Inherits all fields from ONDE_COMPONENT.

For plane components, the dimensions are given by `ONDE_PLANE:PLATE_DIMENSIONS`,
with a triplet for length, width, and height.

## Fields

### `ONDE:TYPE`

- **Required:** Mandatory
- **Storage:** Attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `[2]`
- **Default:** `["ONDE_COMPONENT","ONDE_PLANE"]`

Type chain including parent.

### `ONDE_PLANE:PLATE_DIMENSIONS`

- **Required:** Mandatory
- **Storage:** Attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[3]`
- **Units:** m

Length, width, thickness.

---

# ONDE_CYLINDER

---
onde_class: ONDE_CYLINDER
inherits: [ONDE_COMPONENT]
---

A cylindrical component. Inherits all fields from ONDE_COMPONENT.

## Fields

### `ONDE:TYPE`

- **Required:** Mandatory
- **Storage:** Attribute
- **Type:** `H5T_STRING`
- **Dimensions:** `[2]`
- **Default:** `["ONDE_COMPONENT","ONDE_CYLINDER"]`

Type chain including parent.

### `ONDE_CYLINDER:DIMENSIONS`

- **Required:** Mandatory
- **Storage:** Attribute
- **Type:** `H5T_FLOAT`
- **Dimensions:** `[3]`
- **Units:** m

Outer diameter, thickness, length.
