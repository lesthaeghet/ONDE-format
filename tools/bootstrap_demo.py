import os
import sys
import yaml
import re

# Add current directory to path to import parse_onde_schema
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import parse_onde_schema

def get_mapping():
    return {
        'ONDE_UT_DATASET': 'UT_file_format.md',
        'ONDE_UT_LAW': 'UT_law.md',
        'ONDE_PHASED_ARRAY_SETUP': 'UT_phased_array_setup.md',
        'ONDE_PROBE': 'UT_probes.md',
        'ONDE_SETUP': 'UT_setup.md',
        'ONDE_ULTRASONIC_SETUP': 'UT_ultrasonic_setup.md',
        'ONDE_UT_ASCAN_DATASET': 'ascan_datasets.md',
        'ONDE_COMPONENT': 'component.md',
        'ONDE_PLANE': 'component.md',
        'ONDE_CYLINDER': 'component.md',
        'ONDE_TRAJECTORY': 'trajectory.md',
        'ONDE_UT_TSCAN_DATASET': 'tscan_datasets.md',
        'ONDE_UT_CSCAN_DATASET': 'ut_cscan_datasets.md',
        'ONDE_GEOMETRIC_SETUP': 'ut_geometric_setup.md',
    }

def read_markdown_file(filename):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'UT_specification', filename)
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def generate_markdown(cls, narrative_text, md_dir):
    filename = f"{cls.name.lower()}.md"
    filepath = os.path.join(md_dir, filename)
    
    frontmatter = {
        'onde_class': cls.name,
        'inherits': cls.parent_classes,
        'fields': []
    }
    
    for f in cls.field_list:
        field_info = {
            'full_name': f.full_name,
            'short_name': f.short_name,
            'required': f.required,
            'storage': f.storage,
            'hdf5_type': f.hdf5_type,
            'description': f.description,
        }
        if f.ref_target:
            field_info['ref_target'] = f.ref_target
        if f.dimensions:
            field_info['dimensions'] = f.dimensions
        if f.allowed_values:
            field_info['allowed_values'] = f.allowed_values
            
        frontmatter['fields'].append(field_info)
        
    yaml_str = yaml.dump(frontmatter, sort_keys=False, Dumper=yaml.SafeDumper)
    
    content = f"---\n{yaml_str}---\n\n"
    content += f"# {cls.name}\n\n"
    if narrative_text:
        content += narrative_text
    else:
        content += f"No narrative documentation provided for {cls.name}.\n"
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_yaml(cls, narrative_text, yaml_dir):
    filename = f"{cls.name.lower()}.yaml"
    filepath = os.path.join(yaml_dir, filename)
    
    data = {
        'onde_class': cls.name,
        'inherits': cls.parent_classes,
        'description': narrative_text if narrative_text else f"No narrative documentation provided for {cls.name}.",
        'fields': {}
    }
    
    for f in cls.field_list:
        field_info = {
            'full_name': f.full_name,
            'required': f.required,
            'storage': f.storage,
            'hdf5_type': f.hdf5_type,
            'description': f.description,
        }
        if f.ref_target:
            field_info['ref_target'] = f.ref_target
        if f.dimensions:
            field_info['dimensions'] = f.dimensions
        if f.allowed_values:
            field_info['allowed_values'] = f.allowed_values
            
        data['fields'][f.short_name] = field_info
        
    with open(filepath, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, sort_keys=False, default_flow_style=False, Dumper=yaml.SafeDumper)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, '..', 'ONDE_fields', 'ONDE_fields.csv')
    md_dir = os.path.join(script_dir, '..', 'Demo', 'Markdown')
    yaml_dir = os.path.join(script_dir, '..', 'Demo', 'YAML')
    
    print("Parsing ONDE schema...")
    schema = parse_onde_schema.parse_csv(csv_path)
    
    mapping = get_mapping()
    
    # We should only include each markdown file once. 
    # If a markdown file is mapped to multiple classes (like component.md), 
    # we embed it into the base class, and leave the sub-classes with empty narrative.
    included_files = set()
    
    for cls in schema.all_classes:
        if not cls.name or cls.name == ')':
            continue
        narrative_text = ""
        mapped_file = mapping.get(cls.name)
        if mapped_file and mapped_file not in included_files:
            narrative_text = read_markdown_file(mapped_file)
            included_files.add(mapped_file)
            
        print(f"Generating Markdown/YAML for {cls.name}...")
        generate_markdown(cls, narrative_text, md_dir)
        generate_yaml(cls, narrative_text, yaml_dir)
        
    # Handle root-level fields
    if schema.root_fields:
        print("Generating Markdown/YAML for ROOT fields...")
        # Create a dummy class for root fields
        root_cls = parse_onde_schema.ONDEClass(name="ROOT")
        for f in schema.root_fields.values():
            root_cls.add_field(f)
        generate_markdown(root_cls, "Root level fields for ONDE format.", md_dir)
        generate_yaml(root_cls, "Root level fields for ONDE format.", yaml_dir)
        
    print("Bootstrapping complete.")

if __name__ == '__main__':
    main()
