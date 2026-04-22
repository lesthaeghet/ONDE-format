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
    """Parse Markdown files with field properties as bullet points."""
    records = []
    for fpath in files:
        text = fpath.read_text(encoding="utf-8")

        # Find all class sections: look for "# ONDE_XXXX" at start of line
        heading_pattern = re.compile(r'^# (ONDE_[A-Z0-9_]+)\s*$', re.MULTILINE)
        headings = list(heading_pattern.finditer(text))

        for idx, match in enumerate(headings):
            class_name = match.group(1)
            start = match.end()
            end = headings[idx + 1].start() if idx + 1 < len(headings) else len(text)
            section = text[start:end]

            field_pattern = re.compile(r'^### `(.*?)`\s*$', re.MULTILINE)
            fields = list(field_pattern.finditer(section))

            for fidx, fmatch in enumerate(fields):
                field_name = fmatch.group(1)
                fstart = fmatch.end()
                fend = fields[fidx + 1].start() if fidx + 1 < len(fields) else len(section)

                # Stop field at next H2 (e.g. ## Notes)
                next_h2 = re.search(r'^## ', section[fstart:fend], re.MULTILINE)
                if next_h2:
                    fend = fstart + next_h2.start()

                field_text = section[fstart:fend].strip()

                rec = {
                    "Class": class_name, "Field": field_name, "Required": "Optional",
                    "Storage": "", "Type": "", "Dimensions": "", "Units": "",
                    "Default": "", "Description": ""
                }

                desc_lines = []
                in_metadata = True
                for line in field_text.split('\n'):
                    m = re.match(r'^- \*\*(.*?):\*\* (.*)', line.strip())
                    if m and in_metadata:
                        key, val = m.group(1).strip(), m.group(2).strip().strip('`')
                        if key == 'Required': rec['Required'] = "Mandatory" if "Mandatory" in val else "Optional"
                        elif key == 'Storage': rec['Storage'] = val
                        elif key == 'Type': rec['Type'] = val
                        elif key == 'Dimensions': rec['Dimensions'] = val
                        elif key == 'Units': rec['Units'] = val
                        elif key == 'Default': rec['Default'] = val
                    elif line.strip() == "" and in_metadata:
                        continue
                    elif in_metadata and (line.strip().startswith('- ') or line.strip().startswith('Enum:')):
                        pass
                    else:
                        in_metadata = False
                        if line.strip(): desc_lines.append(line.strip())

                # Description is first paragraph
                desc = []
                for line in desc_lines:
                    if not line.strip() and desc: break
                    if line.strip(): desc.append(line.strip())
                rec["Description"] = " ".join(desc)
                records.append(rec)

    return records


# ================================================================
# 2. RST PARSER
# ================================================================
def parse_rst(files):
    """Parse reStructuredText files with field properties as field lists."""
    records = []
    for fpath in files:
        text = fpath.read_text(encoding="utf-8")

        title_pattern = re.compile(r'^=+\n(ONDE_[A-Z0-9_]+)\n=+', re.MULTILINE)
        titles = list(title_pattern.finditer(text))

        for idx, match in enumerate(titles):
            class_name = match.group(1)
            start = match.end()
            end = titles[idx + 1].start() if idx + 1 < len(titles) else len(text)
            section = text[start:end]

            field_pattern = re.compile(r'^``(.*?)``\n\^\^\^\^\^+', re.MULTILINE)
            fields = list(field_pattern.finditer(section))

            for fidx, fmatch in enumerate(fields):
                field_name = fmatch.group(1)
                fstart = fmatch.end()
                fend = fields[fidx + 1].start() if fidx + 1 < len(fields) else len(section)

                # Stop field at next section (e.g. Notes\n-----)
                next_sec = re.search(r'^\w+\n-+', section[fstart:fend], re.MULTILINE)
                if next_sec:
                    fend = fstart + next_sec.start()

                field_text = section[fstart:fend].strip()

                rec = {
                    "Class": class_name, "Field": field_name, "Required": "Optional",
                    "Storage": "", "Type": "", "Dimensions": "", "Units": "",
                    "Default": "", "Description": ""
                }

                desc_lines = []
                in_metadata = True
                for line in field_text.split('\n'):
                    m = re.match(r'^:(.*?):\s*(.*)', line.strip())
                    if m and in_metadata:
                        key, val = m.group(1).strip(), m.group(2).strip().strip('`')
                        if key == 'Required': rec['Required'] = "Mandatory" if "Mandatory" in val else "Optional"
                        elif key == 'Storage': rec['Storage'] = val
                        elif key == 'Type': rec['Type'] = val
                        elif key == 'Dimensions': rec['Dimensions'] = val
                        elif key == 'Units': rec['Units'] = val
                        elif key == 'Default': rec['Default'] = val
                    elif not line.strip() and in_metadata:
                        continue
                    elif in_metadata and line.strip().startswith('- '):
                        pass
                    else:
                        in_metadata = False
                        if line.strip(): desc_lines.append(line.strip())

                desc = []
                for line in desc_lines:
                    if not line.strip() and desc: break
                    if line.strip(): desc.append(line.strip())
                rec["Description"] = " ".join(desc)
                records.append(rec)

    return records


# ================================================================
# 3. MYST PARSER
# ================================================================
def parse_myst(files):
    """Parse MyST Markdown files with field properties as definition lists."""
    records = []
    for fpath in files:
        text = fpath.read_text(encoding="utf-8")

        heading_pattern = re.compile(r'^# (ONDE_[A-Z0-9_]+)\s*$', re.MULTILINE)
        headings = list(heading_pattern.finditer(text))

        for idx, match in enumerate(headings):
            class_name = match.group(1)
            start = match.end()
            end = headings[idx + 1].start() if idx + 1 < len(headings) else len(text)
            section = text[start:end]

            field_pattern = re.compile(r'^### `(.*?)`\s*$', re.MULTILINE)
            fields = list(field_pattern.finditer(section))

            for fidx, fmatch in enumerate(fields):
                field_name = fmatch.group(1)
                fstart = fmatch.end()
                fend = fields[fidx + 1].start() if fidx + 1 < len(fields) else len(section)

                next_h2 = re.search(r'^## ', section[fstart:fend], re.MULTILINE)
                if next_h2:
                    fend = fstart + next_h2.start()

                field_text = section[fstart:fend].strip()

                rec = {
                    "Class": class_name, "Field": field_name, "Required": "Optional",
                    "Storage": "", "Type": "", "Dimensions": "", "Units": "",
                    "Default": "", "Description": ""
                }

                desc_lines = []
                in_metadata = True
                lines = field_text.split('\n')
                i = 0
                while i < len(lines):
                    line = lines[i].strip()
                    if in_metadata and line in ["Required", "Storage", "Type", "Dimensions", "Units", "Default", "Enum"]:
                        if i + 1 < len(lines) and lines[i+1].strip().startswith(':'):
                            val = lines[i+1].strip()[1:].strip().strip('`')
                            key = line
                            if key == 'Required': rec['Required'] = "Mandatory" if "Mandatory" in val else "Optional"
                            elif key == 'Storage': rec['Storage'] = val
                            elif key == 'Type': rec['Type'] = val
                            elif key == 'Dimensions': rec['Dimensions'] = val
                            elif key == 'Units': rec['Units'] = val
                            elif key == 'Default': rec['Default'] = val
                            i += 2
                            continue
                    if not line and in_metadata:
                        i += 1
                        continue
                    if in_metadata and line.startswith('- '):
                        i += 1
                        continue
                    
                    in_metadata = False
                    if line: desc_lines.append(line)
                    i += 1

                desc = []
                for line in desc_lines:
                    if not line and desc: break
                    if line: desc.append(line)
                rec["Description"] = " ".join(desc)
                records.append(rec)

    return records


# ================================================================
# 4. ASCIIDOC PARSER
# ================================================================
def parse_asciidoc(files):
    """Parse AsciiDoc files with field properties as definition lists."""
    records = []
    for fpath in files:
        text = fpath.read_text(encoding="utf-8")

        heading_pattern = re.compile(r'^= (ONDE_[A-Z0-9_]+)\s*$', re.MULTILINE)
        headings = list(heading_pattern.finditer(text))

        for idx, match in enumerate(headings):
            class_name = match.group(1)
            start = match.end()
            end = headings[idx + 1].start() if idx + 1 < len(headings) else len(text)
            section = text[start:end]

            field_pattern = re.compile(r'^=== `(.*?)`\s*$', re.MULTILINE)
            fields = list(field_pattern.finditer(section))

            for fidx, fmatch in enumerate(fields):
                field_name = fmatch.group(1)
                fstart = fmatch.end()
                fend = fields[fidx + 1].start() if fidx + 1 < len(fields) else len(section)

                next_h2 = re.search(r'^== ', section[fstart:fend], re.MULTILINE)
                if next_h2:
                    fend = fstart + next_h2.start()

                field_text = section[fstart:fend].strip()

                rec = {
                    "Class": class_name, "Field": field_name, "Required": "Optional",
                    "Storage": "", "Type": "", "Dimensions": "", "Units": "",
                    "Default": "", "Description": ""
                }

                desc_lines = []
                in_metadata = True
                for line in field_text.split('\n'):
                    m = re.match(r'^(.*?)::\s*(.*)', line.strip())
                    if m and in_metadata:
                        key, val = m.group(1).strip(), m.group(2).strip().strip('`')
                        if key == 'Required': rec['Required'] = "Mandatory" if "Mandatory" in val else "Optional"
                        elif key == 'Storage': rec['Storage'] = val
                        elif key == 'Type': rec['Type'] = val
                        elif key == 'Dimensions': rec['Dimensions'] = val
                        elif key == 'Units': rec['Units'] = val
                        elif key == 'Default': rec['Default'] = val
                    elif not line.strip() and in_metadata:
                        continue
                    elif in_metadata and (line.strip().startswith('* ') or line.strip().startswith('Enum::')):
                        pass
                    else:
                        in_metadata = False
                        if line.strip(): desc_lines.append(line.strip())

                desc = []
                for line in desc_lines:
                    if not line.strip() and desc: break
                    if line.strip(): desc.append(line.strip())
                rec["Description"] = " ".join(desc)
                records.append(rec)

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
