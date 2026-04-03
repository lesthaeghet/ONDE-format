#!/usr/bin/env python
"""
parse_onde_schema.py - Parse the ONDE field specification CSV into a structured
                       Python object model.

This script reads the semicolon-delimited CSV file that defines the ONDE file
format specification and builds a hierarchical data structure representing:

  - Classes (HDF5 group types) with their inheritance relationships
  - Fields within each class, including:
    - Name, description, mandatory/optional status
    - HDF5 storage type (attribute vs dataset)
    - HDF5 data type (with reference target extraction)
    - Dimensions and allowed values / size constraints

The parsed structure is intended to be the foundation for:
  1. Exporting field definitions in various documentation formats
  2. Generating schema/validation files
  3. Producing human-readable documentation via tools like Sphinx

Usage:
    python parse_onde_schema.py [path_to_csv]

If no path is given, defaults to ../ONDE_fields/ONDE_fields.csv relative to
this script's location.
"""

import csv
import re
import sys
import os
from dataclasses import dataclass, field
from typing import Optional
from collections import OrderedDict


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class ONDEField:
    """A single field (attribute or dataset) within an ONDE class."""

    # Full qualified name as it appears in the CSV, e.g. "ONDE_UT_DATASET:DATA"
    full_name: str

    # Short name without the class prefix, e.g. "DATA"
    short_name: str

    # Human-readable description / comments from the CSV
    description: str

    # True if the field is Mandatory ("M"), False if Optional ("O")
    required: bool

    # "attribute" or "dataset"
    storage: str

    # Raw HDF5 type string, e.g. "H5T_FLOAT", "H5T_STD_REF_OBJ"
    hdf5_type: str

    # For reference types (H5T_STD_REF_OBJ<TARGET>), the target class name.
    # None if not a reference type.
    ref_target: Optional[str] = None

    # Dimension specification string, e.g. "[N_Ascan<m>]", "1", "[7]"
    dimensions: str = ""

    # Allowed values or size constraints from the last CSV column
    allowed_values: str = ""

    # The owning class name (empty string for root-level fields)
    owner_class: str = ""


@dataclass
class ONDEClass:
    """An ONDE class (HDF5 group type) such as ONDE_UT_DATASET or ONDE_COMPONENT."""

    # Class name, e.g. "ONDE_UT_DATASET"
    name: str

    # Ordered list of parent class names derived from the ONDE:TYPE value.
    # For example, ONDE_PLANE has parent_classes=["ONDE_COMPONENT"]
    # Root-level classes have an empty list.
    parent_classes: list = field(default_factory=list)

    # Fields belonging to this class, keyed by short_name for easy lookup
    fields: OrderedDict = field(default_factory=OrderedDict)

    # Raw TYPE value string (the allowed values for ONDE:TYPE in this class)
    type_value: str = ""

    def add_field(self, f: ONDEField):
        self.fields[f.short_name] = f

    @property
    def field_list(self) -> list:
        return list(self.fields.values())

    @property
    def is_subclass(self) -> bool:
        return len(self.parent_classes) > 0


@dataclass
class ONDESchema:
    """Top-level container for the entire parsed ONDE specification."""

    # All classes keyed by name
    classes: OrderedDict = field(default_factory=OrderedDict)

    # Root-level fields (those with no class in column 1)
    root_fields: OrderedDict = field(default_factory=OrderedDict)

    def get_or_create_class(self, name: str) -> ONDEClass:
        if name not in self.classes:
            self.classes[name] = ONDEClass(name=name)
        return self.classes[name]

    @property
    def all_classes(self) -> list:
        return list(self.classes.values())

    def get_children(self, class_name: str) -> list:
        """Return all classes that list class_name as a parent."""
        return [
            c for c in self.all_classes
            if class_name in c.parent_classes
        ]

    def get_inheritance_tree(self) -> dict:
        """Build a dict mapping parent class names to their children."""
        tree = {}
        for cls in self.all_classes:
            for parent in cls.parent_classes:
                tree.setdefault(parent, []).append(cls.name)
        return tree


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def _strip(s: str) -> str:
    """Strip whitespace and control characters."""
    return s.strip().strip('\r\n\t ')


def _parse_required(value: str) -> bool:
    """Parse 'M' / 'O' into boolean."""
    return _strip(value).upper().startswith('M')


def _parse_storage(value: str) -> str:
    """Parse 'D' / 'A' into 'dataset' / 'attribute'."""
    v = _strip(value).upper()
    if v == 'D':
        return 'dataset'
    elif v == 'A':
        return 'attribute'
    return v  # return raw if unexpected


def _parse_hdf5_type(raw: str):
    """
    Parse the HDF5 type column which may contain a reference target, e.g.:
      "H5T_STD_REF_OBJ<ONDE_COMPONENT>"
    Returns (base_type, ref_target_or_None).
    """
    raw = _strip(raw)
    m = re.match(r'^(H5T_\w+)\s*<\s*(\w+)\s*>$', raw)
    if m:
        return m.group(1), m.group(2)
    return raw, None


def _parse_type_value(raw: str) -> list:
    """
    Parse the ONDE:TYPE allowed-values string to extract the class hierarchy.

    Examples:
        '[\"ONDE_UT_DATASET\"]'         -> ["ONDE_UT_DATASET"]
        '[\"ONDE_COMPONENT\",\"ONDE_PLANE\"]' -> ["ONDE_COMPONENT", "ONDE_PLANE"]
    """
    # Remove outer whitespace and quotes
    raw = _strip(raw).strip('"').strip("'").strip()
    if not raw:
        return []

    # Find all ONDE_xxx identifiers
    return re.findall(r'(ONDE_\w+)', raw)


def _split_field_name(full_name: str):
    """
    Split a field name like 'ONDE_UT_DATASET:DATA' into (prefix, short_name).
    For names like 'ONDE:TYPE' or 'ONDE:LABEL', prefix='ONDE'.
    """
    full_name = _strip(full_name)
    if ':' in full_name:
        parts = full_name.split(':', 1)
        return parts[0], parts[1]
    return '', full_name


# ---------------------------------------------------------------------------
# Main CSV parser
# ---------------------------------------------------------------------------

def parse_csv(csv_path: str) -> ONDESchema:
    """
    Parse the ONDE fields CSV file and return an ONDESchema.

    The CSV is semicolon-delimited with the following columns:
      0: Class           - Owning class name (empty for root-level fields)
      1: Name            - Full field name (e.g. ONDE_UT_DATASET:DATA)
      2: Comments        - Description
      3: M or O          - Mandatory / Optional
      4: D or A          - Dataset / Attribute
      5: HDF5 Type       - e.g. H5T_FLOAT, H5T_STD_REF_OBJ<ONDE_COMPONENT>
      6: Dims            - Dimension specification
      7: Size or content - Allowed values / size constraints
    """
    schema = ONDESchema()

    # The CSV may contain non-UTF-8 characters (e.g. en-dashes from
    # Windows-1252 encoding). Try UTF-8 first, fall back to latin-1.
    raw = open(csv_path, 'rb').read()
    try:
        text = raw.decode('utf-8-sig')
    except UnicodeDecodeError:
        text = raw.decode('latin-1')

    reader = csv.reader(text.splitlines(), delimiter=';')
    rows = list(reader)

    if not rows:
        print("ERROR: CSV file is empty.", file=sys.stderr)
        return schema

    # Skip header row
    header = rows[0]
    data_rows = rows[1:]

    for row_num, row in enumerate(data_rows, start=2):
        # Skip empty rows
        if not row or all(c.strip() == '' for c in row):
            continue

        # Pad short rows
        while len(row) < 8:
            row.append('')

        class_name   = _strip(row[0])
        field_name   = _strip(row[1])
        comments     = _strip(row[2])
        mandatory    = _strip(row[3])
        storage_type = _strip(row[4])
        hdf5_type_raw = _strip(row[5])
        dims         = _strip(row[6])
        size_content = _strip(row[7])

        if not field_name:
            continue  # skip rows with no field name

        # Parse derived values
        prefix, short_name = _split_field_name(field_name)
        required = _parse_required(mandatory)
        storage = _parse_storage(storage_type)
        hdf5_type, ref_target = _parse_hdf5_type(hdf5_type_raw)

        # Build the field object
        fld = ONDEField(
            full_name=field_name,
            short_name=short_name,
            description=comments,
            required=required,
            storage=storage,
            hdf5_type=hdf5_type,
            ref_target=ref_target,
            dimensions=dims,
            allowed_values=size_content,
            owner_class=class_name,
        )

        # Determine where this field belongs
        if class_name:
            # Field belongs to a class
            cls = schema.get_or_create_class(class_name)
            cls.add_field(fld)

            # If this is the ONDE:TYPE field, extract inheritance info
            if short_name == 'TYPE' and size_content:
                type_chain = _parse_type_value(size_content)
                cls.type_value = size_content
                if len(type_chain) > 1:
                    # Last element is the class itself, the rest are parents
                    # e.g. ["ONDE_COMPONENT", "ONDE_PLANE"] -> parent is ONDE_COMPONENT
                    cls.parent_classes = type_chain[:-1]
        else:
            # Root-level field
            schema.root_fields[fld.full_name] = fld

    return schema


# ---------------------------------------------------------------------------
# Diagnostic summary
# ---------------------------------------------------------------------------

def print_summary(schema: ONDESchema):
    """Print a human-readable summary of the parsed schema."""

    print("=" * 72)
    print("ONDE Schema Summary")
    print("=" * 72)

    # Root-level fields
    print(f"\n--- Root-Level Fields ({len(schema.root_fields)}) ---")
    for fld in schema.root_fields.values():
        req = "REQUIRED" if fld.required else "optional"
        print(f"  {fld.full_name:40s}  {req:10s}  {fld.hdf5_type}")

    # Classes
    print(f"\n--- Classes ({len(schema.classes)}) ---")
    inheritance_tree = schema.get_inheritance_tree()

    for cls in schema.all_classes:
        parent_str = ""
        if cls.parent_classes:
            parent_str = f"  (inherits from: {', '.join(cls.parent_classes)})"
        children = inheritance_tree.get(cls.name, [])
        child_str = ""
        if children:
            child_str = f"  [subclasses: {', '.join(children)}]"

        print(f"\n  {cls.name}{parent_str}{child_str}")
        print(f"  {'-' * (len(cls.name) + 2)}")

        for fld in cls.field_list:
            req_marker = "M" if fld.required else "O"
            ref_str = f" -> {fld.ref_target}" if fld.ref_target else ""
            dim_str = f" {fld.dimensions}" if fld.dimensions else ""
            print(f"    [{req_marker}] {fld.short_name:40s}  "
                  f"{fld.storage:10s}  {fld.hdf5_type}{ref_str}{dim_str}")

    # Statistics
    print(f"\n{'=' * 72}")
    print("Statistics:")
    total_fields = len(schema.root_fields)
    for cls in schema.all_classes:
        total_fields += len(cls.fields)
    n_mandatory = sum(1 for f in _all_fields(schema) if f.required)
    n_optional = total_fields - n_mandatory
    n_datasets = sum(1 for f in _all_fields(schema) if f.storage == 'dataset')
    n_attrs = sum(1 for f in _all_fields(schema) if f.storage == 'attribute')
    n_refs = sum(1 for f in _all_fields(schema) if f.ref_target)
    base_classes = [c for c in schema.all_classes if not c.is_subclass]
    sub_classes = [c for c in schema.all_classes if c.is_subclass]

    print(f"  Total classes:     {len(schema.classes)}")
    print(f"    Base classes:    {len(base_classes)}")
    print(f"    Subclasses:      {len(sub_classes)}")
    print(f"  Total fields:      {total_fields}")
    print(f"    Mandatory:       {n_mandatory}")
    print(f"    Optional:        {n_optional}")
    print(f"    Attributes:      {n_attrs}")
    print(f"    Datasets:        {n_datasets}")
    print(f"    HDF5 references: {n_refs}")
    print(f"{'=' * 72}")


def _all_fields(schema: ONDESchema):
    """Iterate over every field in the schema."""
    yield from schema.root_fields.values()
    for cls in schema.all_classes:
        yield from cls.field_list


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    # Determine CSV path
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
    else:
        # Default: look relative to this script's location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, '..', 'ONDE_fields', 'ONDE_fields.csv')

    csv_path = os.path.normpath(csv_path)

    if not os.path.isfile(csv_path):
        print(f"ERROR: CSV file not found: {csv_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Parsing: {csv_path}\n")
    schema = parse_csv(csv_path)
    print_summary(schema)

    return schema


if __name__ == '__main__':
    main()
