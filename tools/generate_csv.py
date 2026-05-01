import os
import sys
import argparse
import yaml
import glob
import csv

def parse_markdown(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract YAML frontmatter
    if content.startswith('---'):
        end_idx = content.find('---', 3)
        if end_idx != -1:
            frontmatter = content[3:end_idx].strip()
            return yaml.safe_load(frontmatter)
    return None

def parse_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def generate_csv(input_dir, format_type, output_csv):
    files = glob.glob(os.path.join(input_dir, f'*.{"md" if format_type == "markdown" else "yaml"}'))
    
    classes_data = []
    
    for f in files:
        if format_type == 'markdown':
            data = parse_markdown(f)
        else:
            data = parse_yaml(f)
            
        if data and 'onde_class' in data:
            classes_data.append(data)
            
    # Sort to ensure consistent output (ROOT first, then alphabetical)
    classes_data.sort(key=lambda x: ("" if x['onde_class'] == 'ROOT' else x['onde_class']))
    
    header = "Class;Name; Comments                                                                                                   ; M or O; D or A; Class                                                           ; Dims       ; Size or content\n"
    
    with open(output_csv, 'w', encoding='utf-8-sig', newline='') as f:
        f.write(header)
        writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        
        for cls_data in classes_data:
            cls_name = cls_data.get('onde_class', '')
            if cls_name == 'ROOT':
                cls_name = ''
                
            fields = cls_data.get('fields', [])
            
            # YAML format stores fields as a dict, Markdown as a list
            if isinstance(fields, dict):
                fields_list = []
                for k, v in fields.items():
                    v['short_name'] = k
                    fields_list.append(v)
                fields = fields_list
                
            for field in fields:
                m_o = 'M' if field.get('required') else 'O'
                
                storage = field.get('storage', '')
                d_a = 'D' if storage == 'dataset' else 'A'
                if not storage:
                    d_a = ''
                    
                hdf5_type = field.get('hdf5_type', '')
                ref_target = field.get('ref_target', '')
                if ref_target:
                    hdf5_type = f"{hdf5_type}<{ref_target}>"
                    
                row = [
                    cls_name,
                    field.get('full_name', ''),
                    field.get('description', ''),
                    m_o,
                    d_a,
                    hdf5_type,
                    field.get('dimensions', ''),
                    field.get('allowed_values', '')
                ]
                writer.writerow(row)

    print(f"Generated {output_csv} successfully from {len(classes_data)} classes.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate ONDE_fields.csv from SSOT")
    parser.add_argument('--format', choices=['markdown', 'yaml'], required=True)
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    
    args = parser.parse_args()
    generate_csv(args.input, args.format, args.output)
