# Documentation Gap Analysis: CSV vs. Markdown Content

This analysis identifies what information exists in the current markdown files (and would be needed by automated documentation generators) that is **not representable** in the current CSV structure or our parsed data model.

---

## 1. Schema-Level Metadata (Global)

These exist in `UT_file_format.md` but have no home in the CSV structure:

| Missing Field | Where It Currently Lives | Example |
|---|---|---|
| **Format version** | Hardcoded in `ONDE:VERSION` allowed value `"0.4.0"` | `0.4.0` |
| **Glossary / Term definitions** | `UT_file_format.md` lines 68-96 | "Ultrasonic Element", "Focal law", "A-Scan", etc. (16 terms) |
| **Dimension variables table** | `UT_file_format.md` lines 98-117 | `N_Probes`, `N_Elem<p>`, `N_DF<m>`, etc. (17 variables) — these appear throughout dimension specs but are only defined narratively |
| **General HDF5 rules** | `UT_file_format.md` lines 209-236 | File extension `.onde`, group naming rules, type polymorphism, array ordering, compression |
| **Frame conventions** | `UT_file_format.md` lines 238-284 | 3D frames (quaternions), 2D frames (Δa,Δb,α), hierarchy of frames |
| **External references** | `UT_file_format.md` footnotes | MFMC 2.0.0b, ECUF 1.0, NDE 4.0 textbook |
| **Appendices** | `UT_file_format.md` lines 353-387 | Quaternion↔matrix conversion formulas |

---

## 2. Class-Level Documentation

The CSV has **zero class-level metadata** — classes are only implied by grouping field rows. Every markdown file adds substantial class-level content:

| Missing Field | Description | Examples from Markdown Files |
|---|---|---|
| **Class description** | Narrative explanation of the class's purpose | *"Ascan datasets are the entry points for the description of data that is stored as time signals"* (ascan_datasets.md) |
| **Usage notes** | Conventions, rules, and practices for the class | Element ordering conventions, wedge angle conventions, pixel ordering (UT_probes.md, tscan_datasets.md) |
| **Figures** | Associated diagrams/images with captions | 27 figures (figure1.png–figure27.png) tied to specific classes. E.g., figures 12-21 belong to Probes, figures 24-27 to Phased Array Setup. **Note:** Figures should be placed via inline markup within narrative documentation text (e.g., description, notes) so they appear in context — not as a standalone metadata field on the class. |
| **Mermaid diagrams** | Embedded relationship diagrams | Component inheritance diagram (component.md), PA setup hierarchy (UT_phased_array_setup.md), full data model (UT_file_format.md) |
| **Compatibility notes** | References to equivalent structures in other formats | *"The MFMC equivalent is 'SEQUENCE', and both names are allowed"* (ascan_datasets.md) |
| **Limitations / caveats** | Known restrictions for the current version | *"Variable gates are not handled in this version"* (UT_ultrasonic_setup.md), *"This block has no vocation to be exhaustive"* (UT_phased_array_setup.md) |
| **Version notes** | When features were introduced or changed | *"Other parameterized shapes can be added in future versions"* (component.md) |
| **See also / cross-references** | Links to related classes | The setup.md file references ultrasonic_setup and geometric_setup |

### Class-to-Figure mapping (discovered from markdown)

> **IMPORTANT:**
> Figures should not be treated as a class-level metadata field (e.g., a list of figure paths).
> Instead, the documentation format must support **inline figure markup** within narrative text
> (descriptions, notes, conventions) so that each figure appears in the specific context where
> it is meaningful. This is a markup/syntax concern for whatever definition format is chosen,
> not a data model field.

The following mapping shows which classes currently reference which figures:

| Class | Figures |
|---|---|
| General (frames) | 2, 3, 4 |
| Tscan Dataset | 5 |
| Component (general) | 6, 7 |
| Component (2DCAD) | 8, 9 |
| Component (visualization) | 10, 11 |
| Probe (elements) | 12, 13, 14 |
| Probe (wedges) | 15, 16, 17, 18, 19, 20, 21 |
| Trajectory (grid) | 22 |
| Ultrasonic Setup (TOFD) | 23 |
| Phased Array (angle) | 24 |
| Phased Array (sscan) | 25 |
| Phased Array (escan) | 26 |
| Phased Array (compound) | 27 |

---

## 3. Field-Level Documentation Gaps

The CSV "Comments" column has brief one-liners. The markdown files expand on fields in ways the CSV cannot capture:

| Missing Field | Description | Examples |
|---|---|---|
| **Default value** | What is assumed when the field is absent | *"If absent, identity is assumed"* (INDEX_POINT_FRAME), *"If missing, impulse emission at time 0.0 is assumed"* (SIGNAL), *"semi-infinite half plane is assumed, with interface at z=0"* (COMPONENT) |
| **Units** | Specific unit for the field | Global rule is SI (meters, kg, seconds) with degrees for angles, but individual fields don't state their unit |
| **Conditional requirements** | When an "Optional" field becomes effectively mandatory | *"Mandatory for phased array setups"* (TRANSMIT_LAW), *"Mandatory for Ascan sequences"* (ULTRASONIC_SETUP) |
| **Inter-field relationships** | How fields interact with each other | Acquisition gate defined by ASCAN_START + N_Time/ASCAN_SAMPLE_RATE; GAIN must be cumulated with TCG_CURVE |
| **Detailed explanation** | Extended prose beyond the brief comment | GAIN explanation, filter parameter interpretation by filter type, grid position conventions |
| **Enum value meanings** | What each allowed value means | FILTER_TYPE: meanings of NO_FILTER, LOW_PASS, HIGH_PASS, BAND_PASS, OTHER. DETECTION: FIRST_PEAK vs MAX_PEAK vs FIRST_FLANK etc. |
| **Examples** | Concrete example values | Not currently present in any file, but would be valuable |
| **Deprecated / since version** | Versioning at the field level | Not currently tracked |
| **Validation rules** | Constraints beyond type and dimensions | *"ISO 8601 extended format: 'yyyy-mm-dd HH:MM:SS'"* for DATE_AND_TIME |

---

## 4. Summary of Needed Additions to Data Model

### Schema Level (new fields on `ONDESchema`)
```
version: str                    # Format version string
glossary: dict[str, str]        # Term -> definition
dimension_variables: dict       # Variable name -> description  
general_rules: list[str]        # HDF5 implementation rules (free-form text blocks)
references: list[Reference]     # External specification references
appendices: list[Appendix]      # Supplementary material
```

### Class Level (new fields on `ONDEClass`)
```
description: str                # Narrative purpose/overview
notes: list[str]                # Usage notes, conventions, practices  
diagrams: list[str]             # Mermaid diagram source blocks
compatibility: dict[str, str]   # Format name -> equivalence note
limitations: list[str]          # Known restrictions
see_also: list[str]             # Cross-references to other class names
```

Note: Figures are intentionally omitted from the class-level data model. They
should be embedded via inline markup within the narrative text fields
(description, notes) so they appear in context.

### Field Level (new fields on `ONDEField`)
```
default_value: str              # Value assumed when absent
units: str                      # SI unit (e.g., "m", "s", "degrees", "Hz")
conditional_requirement: str    # When optional becomes mandatory
inter_field_notes: list[str]    # Relationships with other fields
detailed_description: str       # Extended prose (vs. the brief CSV comment)
enum_descriptions: dict         # Enum value -> meaning
validation_format: str          # Format pattern (e.g., ISO 8601)
examples: list[str]             # Example values
since_version: str              # Version when introduced
deprecated: bool                # Whether the field is deprecated
```

---

## 5. Key Observations

> **IMPORTANT:**
> The most critical gap is **class-level documentation** — the CSV has no concept of it at all. Every markdown file is essentially a class-level document, yet this information would need to live alongside the field definitions in any unified format.

> **NOTE:**
> The **figures/images** (27 PNGs) are significant documentation assets. They are not just decorative — they define geometric conventions that are normative. Rather than treating figures as a class-level metadata field, the chosen documentation format must support **inline figure markup** within narrative text blocks (descriptions, notes, conventions). This allows each figure to appear in the specific context where it is referenced, just as it does in the current markdown files.

> **TIP:**
> The **dimension variables** (N_Probes, N_DF\<m\>, etc.) deserve first-class treatment since they appear throughout dimension specifications. Defining them in one place and referencing them in field definitions would improve consistency and enable automated validation.
