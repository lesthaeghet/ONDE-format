# ONDE_2DCAD

**Inherits from:** ONDE_COMPONENT

```{mermaid}
classDiagram
  ONDE_COMPONENT <|-- ONDE_2DCAD
  click ONDE_COMPONENT href "onde_component.html"
  click ONDE_2DCAD href "onde_2dcad.html"
```

No narrative documentation provided for ONDE_2DCAD.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_2dcad-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[2]` | `["ONDE_COMPONENT","ONDE_2DCAD"]` |  |
| [**`EXTRUSION_TYPE`**](#onde_2dcad-extrusion_type)<br><sub>`ONDE_2DCAD:EXTRUSION_TYPE`</sub> | Mandatory | attribute | H5T_STRING | `1` | `"PLANE" \|"CYLINDER"` |  |
| [**`EXTRUSION_DIMENSION`**](#onde_2dcad-extrusion_dimension)<br><sub>`ONDE_2DCAD:EXTRUSION_DIMENSION`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` |  |
| [**`CAD`**](#onde_2dcad-cad)<br><sub>`ONDE_2DCAD:CAD`</sub> | Mandatory | attribute | H5T_STRING | `1` | `` |  |


## Field Details

(onde_2dcad-type)=
### `TYPE`

*No detailed description provided.*

(onde_2dcad-extrusion_type)=
### `EXTRUSION_TYPE`

*No detailed description provided.*

(onde_2dcad-extrusion_dimension)=
### `EXTRUSION_DIMENSION`

*No detailed description provided.*

(onde_2dcad-cad)=
### `CAD`

*No detailed description provided.*
