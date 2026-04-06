#!/usr/bin/env python3
"""
Parse each prototype format and generate a CSV file from the extracted
field definitions.  Demonstrates the parsing complexity for each format.

Usage:
    python parse_format_prototypes.py

Generates one CSV per format in Documentation_Improvement/<Format>/extracted.csv
"""

import csv
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DOC_DIR = REPO_ROOT / "Documentation_Improvement"

CSV_COLUMNS = [
    "Class", "Field", "Required", "Storage", "Type",
    "Dimensions", "Units", "Default", "Description"
]


def write_csv(records, output_path):
    """Write parsed records to a semicolon-delimited CSV."""
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, delimiter=";")
        writer.writeheader()
        for rec in records:
            writer.writerow(rec)
    print(f"  -> Wrote {len(records)} fields to {output_path.name}")


def req_str(val):
    return "Mandatory" if val.strip() == "M" else "Optional"


# ================================================================
# 1. MARKDOWN PARSER
# ================================================================
def parse_markdown(files):
    """Parse Markdown files with YAML frontmatter and pipe tables."""
    records = []
    for fpath in files:
        text = fpath.read_text(encoding="utf-8")

        # Find all class sections: look for "# ONDE_XXXX" at start of line
        # (but not inside YAML comments like "# ONDE Class Definition")
        heading_pattern = re.compile(r'^# (ONDE_[A-Z0-9_]+)\s*$', re.MULTILINE)
        headings = list(heading_pattern.finditer(text))

        for idx, match in enumerate(headings):
            class_name = match.group(1)
            start = match.end()
            end = headings[idx + 1].start() if idx + 1 < len(headings) else len(text)
            section = text[start:end]

            # Find pipe table rows after "## Field Definitions"
            fd_pos = section.find("## Field Definitions")
            if fd_pos == -1:
                continue

            fd_section = section[fd_pos:]
            # Collect all pipe-table lines (|...|)
            table_lines = []
            in_table = False
            for line in fd_section.split("\n"):
                stripped = line.strip()
                if stripped.startswith("|") and stripped.endswith("|"):
                    in_table = True
                    table_lines.append(stripped)
                elif in_table:
                    break  # table ended

            # Skip header (row 0) and separator (row 1)
            for row_line in table_lines[2:]:
                cells = [c.strip().strip('`') for c in row_line.split("|")]
                # split on | gives empty first and last elements
                cells = [c for c in cells if c or c == ""]
                cells = row_line.split("|")[1:-1]
                cells = [c.strip().strip('`') for c in cells]
                if len(cells) >= 8:
                    records.append({
                        "Class": class_name,
                        "Field": cells[0],
                        "Required": req_str(cells[1]),
                        "Storage": cells[2],
                        "Type": cells[3],
                        "Dimensions": cells[4],
                        "Units": cells[5],
                        "Default": cells[6],
                        "Description": cells[7],
                    })

    return records


# ================================================================
# 2. RST PARSER
# ================================================================
def parse_rst(files):
    """Parse reStructuredText files with list-tables."""
    records = []
    for fpath in files:
        text = fpath.read_text(encoding="utf-8")

        # Find class titles: line of === above and below the name
        title_pattern = re.compile(
            r'^=+\n(ONDE_[A-Z0-9_]+)\n=+', re.MULTILINE
        )
        titles = list(title_pattern.finditer(text))

        for idx, match in enumerate(titles):
            class_name = match.group(1)
            start = match.end()
            end = titles[idx + 1].start() if idx + 1 < len(titles) else len(text)
            section = text[start:end]

            # Find list-table rows: "   * - " marks a new row
            row_pattern = re.compile(r'^\s+\*\s-\s', re.MULTILINE)
            row_starts = list(row_pattern.finditer(section))

            if not row_starts:
                continue

            rows = []
            for ridx, rmatch in enumerate(row_starts):
                rstart = rmatch.end()
                rend = row_starts[ridx + 1].start() if ridx + 1 < len(row_starts) else len(section)
                row_text = section[rstart:rend].strip()

                # First cell is the rest of the "* - " line
                lines = row_text.split("\n")
                first_cell = lines[0].strip()
                # Remaining cells: "     - value" or bare "     -" (empty cell)
                rest = []
                for line in lines[1:]:
                    m = re.match(r'^\s+-\s*(.*)', line)
                    if m:
                        rest.append(m.group(1).strip())
                cells = [first_cell] + rest
                cells = [c.strip().strip('`').replace('``', '') for c in cells]
                rows.append(cells)

            # Skip header row (row 0)
            for row in rows[1:]:
                if len(row) >= 8:
                    records.append({
                        "Class": class_name,
                        "Field": row[0],
                        "Required": req_str(row[1]),
                        "Storage": row[2],
                        "Type": row[3],
                        "Dimensions": row[4],
                        "Units": row[5],
                        "Default": row[6],
                        "Description": row[7],
                    })

    return records


# ================================================================
# 3. MYST PARSER
# ================================================================
def parse_myst(files):
    """Parse MyST Markdown files with ::: fenced list-tables."""
    records = []
    for fpath in files:
        text = fpath.read_text(encoding="utf-8")

        # Find class sections by H1 headings
        heading_pattern = re.compile(r'^# (ONDE_[A-Z0-9_]+)\s*$', re.MULTILINE)
        headings = list(heading_pattern.finditer(text))

        for idx, match in enumerate(headings):
            class_name = match.group(1)
            start = match.end()
            end = headings[idx + 1].start() if idx + 1 < len(headings) else len(text)
            section = text[start:end]

            # Find the list-table fence block: :::{list-table}...:::
            table_match = re.search(
                r':::\{list-table\}.*?\n(.*?)\n:::',
                section, re.DOTALL
            )
            if not table_match:
                continue

            table_text = table_match.group(1)

            # Rows start with "* - " (no leading indent in MyST)
            row_pattern = re.compile(r'^\*\s-\s', re.MULTILINE)
            row_starts = list(row_pattern.finditer(table_text))

            if not row_starts:
                continue

            rows = []
            for ridx, rmatch in enumerate(row_starts):
                rstart = rmatch.end()
                rend = row_starts[ridx + 1].start() if ridx + 1 < len(row_starts) else len(table_text)
                row_text = table_text[rstart:rend].strip()

                lines = row_text.split("\n")
                first_cell = lines[0].strip()
                rest = []
                for line in lines[1:]:
                    m = re.match(r'^\s+-\s*(.*)', line)
                    if m:
                        rest.append(m.group(1).strip())
                cells = [first_cell] + rest
                cells = [c.strip().strip('`') for c in cells]
                rows.append(cells)

            # Skip header row
            for row in rows[1:]:
                if len(row) >= 8:
                    records.append({
                        "Class": class_name,
                        "Field": row[0],
                        "Required": req_str(row[1]),
                        "Storage": row[2],
                        "Type": row[3],
                        "Dimensions": row[4],
                        "Units": row[5],
                        "Default": row[6],
                        "Description": row[7],
                    })

    return records


# ================================================================
# 4. ASCIIDOC PARSER
# ================================================================
def parse_asciidoc(files):
    """Parse AsciiDoc files with multi-line table cells."""
    records = []
    for fpath in files:
        text = fpath.read_text(encoding="utf-8")

        # Find class sections by "= ONDE_XXX" headings
        heading_pattern = re.compile(r'^= (ONDE_[A-Z0-9_]+)\s*$', re.MULTILINE)
        headings = list(heading_pattern.finditer(text))

        for idx, match in enumerate(headings):
            class_name = match.group(1)
            start = match.end()
            end = headings[idx + 1].start() if idx + 1 < len(headings) else len(text)
            section = text[start:end]

            # Find table blocks between |=== markers
            table_blocks = re.findall(r'\|===\n(.*?)\|===', section, re.DOTALL)

            for table_text in table_blocks:
                # In AsciiDoc, each cell is "|value" on its own line.
                # Header row has all cells on ONE line: "|F1 |F2 |F3 ..."
                # Data cells are one per line: "|value\n"
                lines = table_text.strip().split("\n")

                # First non-empty line is the header (all on one line)
                header_line = ""
                data_start = 0
                for li, line in enumerate(lines):
                    if line.strip().startswith("|"):
                        header_line = line
                        data_start = li + 1
                        break

                header_cells = [c.strip().strip('`') for c in header_line.split("|")[1:] if True]
                num_cols = len([c for c in header_cells if c.strip() or c == ""])
                # Count actual | delimiters
                num_cols = header_line.count("|")

                if num_cols < 8:
                    continue  # Skip non-field tables (e.g., enum tables)

                # Collect data cells: each "|value" line is one cell
                # Empty lines separate rows but cells can also just flow
                data_cells = []
                for line in lines[data_start:]:
                    stripped = line.strip()
                    if stripped == "":
                        continue  # blank line between rows
                    if stripped.startswith("|"):
                        cell_val = stripped[1:].strip().strip('`')
                        data_cells.append(cell_val)

                # Group into rows of num_cols cells
                for j in range(0, len(data_cells), num_cols):
                    row = data_cells[j:j + num_cols]
                    if len(row) >= 8:
                        records.append({
                            "Class": class_name,
                            "Field": row[0],
                            "Required": req_str(row[1]),
                            "Storage": row[2],
                            "Type": row[3],
                            "Dimensions": row[4],
                            "Units": row[5],
                            "Default": row[6],
                            "Description": row[7],
                        })
                break  # Only first 8+ column table per section

    return records


# ================================================================
# 5. YAML PARSER
# ================================================================
def parse_yaml(files):
    """Parse YAML files with structured field definitions."""
    try:
        import yaml
    except ImportError:
        print("  !! PyYAML not installed. Install with: pip install pyyaml")
        return None

    records = []
    for fpath in files:
        text = fpath.read_text(encoding="utf-8")

        for doc in yaml.safe_load_all(text):
            if doc is None:
                continue
            class_name = doc.get("onde_class", "UNKNOWN")
            fields = doc.get("fields", {})

            for key, fdef in fields.items():
                full_name = fdef.get("full_name", key)
                records.append({
                    "Class": class_name,
                    "Field": full_name,
                    "Required": "Mandatory" if fdef.get("required") else "Optional",
                    "Storage": fdef.get("storage", ""),
                    "Type": fdef.get("hdf5_type", ""),
                    "Dimensions": fdef.get("dimensions", ""),
                    "Units": str(fdef.get("units", "")),
                    "Default": str(fdef.get("default", "")),
                    "Description": fdef.get("description", "").strip(),
                })

    return records


# ================================================================
# 6. XML PARSER
# ================================================================
def parse_xml(files):
    """Parse XML files with element tree — stdlib, no external deps."""
    records = []
    for fpath in files:
        tree = ET.parse(fpath)
        root = tree.getroot()

        for cls in root.findall("class"):
            class_name = cls.get("name", "UNKNOWN")

            for field in cls.findall("fields/field"):
                brief_el = field.find("brief")
                records.append({
                    "Class": class_name,
                    "Field": field.get("name", ""),
                    "Required": req_str(field.get("required", "O")),
                    "Storage": field.get("storage", ""),
                    "Type": field.get("type", ""),
                    "Dimensions": field.get("dimensions", ""),
                    "Units": field.get("units", ""),
                    "Default": field.get("default", ""),
                    "Description": brief_el.text.strip() if brief_el is not None else "",
                })

    return records


# ================================================================
# 7. JSON PARSER
# ================================================================
def parse_json(files):
    """Parse JSON files — stdlib, no external deps."""
    records = []
    for fpath in files:
        data = json.loads(fpath.read_text(encoding="utf-8"))

        for cls in data.get("classes", []):
            class_name = cls.get("onde_class", "UNKNOWN")

            for field in cls.get("fields", []):
                records.append({
                    "Class": class_name,
                    "Field": field.get("name", ""),
                    "Required": req_str(field.get("required", "O")),
                    "Storage": field.get("storage", ""),
                    "Type": field.get("type", ""),
                    "Dimensions": field.get("dimensions", ""),
                    "Units": field.get("units", ""),
                    "Default": field.get("default", ""),
                    "Description": field.get("brief", ""),
                })

    return records


# ================================================================
# MAIN
# ================================================================
def main():
    formats = {
        "Markdown": {
            "parser": parse_markdown,
            "ext": "*.md",
            "dir": DOC_DIR / "Markdown",
        },
        "reStructuredText": {
            "parser": parse_rst,
            "ext": "*.rst",
            "dir": DOC_DIR / "reStructuredText",
        },
        "MyST": {
            "parser": parse_myst,
            "ext": "*.md",
            "dir": DOC_DIR / "MyST",
        },
        "AsciiDoc": {
            "parser": parse_asciidoc,
            "ext": "*.adoc",
            "dir": DOC_DIR / "AsciiDoc",
        },
        "YAML": {
            "parser": parse_yaml,
            "ext": "*.yaml",
            "dir": DOC_DIR / "YAML",
        },
        "XML": {
            "parser": parse_xml,
            "ext": "*.xml",
            "dir": DOC_DIR / "XML",
        },
        "JSON": {
            "parser": parse_json,
            "ext": "*.json",
            "dir": DOC_DIR / "JSON",
        },
    }

    print("=" * 70)
    print("Parsing prototype formats and generating CSV files")
    print("=" * 70)

    all_results = {}

    for name, cfg in formats.items():
        print(f"\n--- {name} ---")
        fmt_dir = cfg["dir"]
        files = sorted(fmt_dir.glob(cfg["ext"]))
        print(f"  Files: {[f.name for f in files]}")

        records = cfg["parser"](files)
        if records is None:
            continue

        all_results[name] = records

        if records:
            output = fmt_dir / "extracted.csv"
            write_csv(records, output)

            print(f"  Preview:")
            for rec in records:
                print(f"    {rec['Class']:30s} | {rec['Field']:45s} | "
                      f"{rec['Required']:9s} | {rec['Storage']:9s} | "
                      f"{rec['Type']:15s} | {rec['Dimensions']}")
        else:
            print("  !! No fields extracted.")

    # Summary comparison
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for name, records in all_results.items():
        print(f"  {name:25s}: {len(records):3d} fields extracted")
    print("=" * 70)


if __name__ == "__main__":
    main()
