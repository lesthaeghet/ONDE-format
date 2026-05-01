# ONDE_DUAL_WEDGE

**Inherits from:** ONDE_UT_COUPLING, ONDE_WEDGE

```{mermaid}
classDiagram
  ONDE_UT_COUPLING <|-- ONDE_DUAL_WEDGE
  ONDE_WEDGE <|-- ONDE_DUAL_WEDGE
  click ONDE_DUAL_WEDGE href "onde_dual_wedge.html"
  click ONDE_WEDGE href "onde_wedge.html"
  click ONDE_UT_COUPLING href "onde_ut_coupling.html"
```

No narrative documentation provided for ONDE_DUAL_WEDGE.

## Fields Summary

| Field | Req | Storage | Type | Dims | Allowed | Description |
|---|---|---|---|---|---|---|
| [**`TYPE`**](#onde_dual_wedge-type)<br><sub>`ONDE:TYPE`</sub> | Mandatory | attribute | H5T_STRING | `[3]` | `["ONDE_UT_COUPLING","ONDE_WEDGE","ONDE_DUAL_WEDGE"]` |  |
| [**`PROBE_SEPARATION`**](#onde_dual_wedge-probe_separation)<br><sub>`ONDE_DUAL_WEDGE:PROBE_SEPARATION`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` | For dual probes, inter-probes distance (L6) (See Figure 15) |
| [**`ROOF_ANGLE`**](#onde_dual_wedge-roof_angle)<br><sub>`ONDE_DUAL_WEDGE:ROOF_ANGLE`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` | For dual probes and only for dual probes defines the roof angle (See Figure 15) |
| [**`SQUINT_ANGLE`**](#onde_dual_wedge-squint_angle)<br><sub>`ONDE_DUAL_WEDGE:SQUINT_ANGLE`</sub> | Mandatory | attribute | H5T_FLOAT | `1` | `` | For dual probes, squint angle (A2) (See Figure 15) |


## Field Details

(onde_dual_wedge-type)=
### `TYPE`

*No detailed description provided.*

(onde_dual_wedge-probe_separation)=
### `PROBE_SEPARATION`

For dual probes, inter-probes distance (L6) (See Figure 15)

(onde_dual_wedge-roof_angle)=
### `ROOF_ANGLE`

For dual probes and only for dual probes defines the roof angle (See Figure 15)

(onde_dual_wedge-squint_angle)=
### `SQUINT_ANGLE`

For dual probes, squint angle (A2) (See Figure 15)
