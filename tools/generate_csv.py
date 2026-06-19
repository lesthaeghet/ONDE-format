import os
import sys
import yaml
import glob
import csv


def parse_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def generate_csv():
    input_dir = 'schema'
    output_csv = 'build/ONDE_fields.csv'
    
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    
    files = glob.glob(os.path.join(input_dir, '*.yaml'))
    
    classes_data = []
    
    for f in files:
        data = parse_yaml(f)
            
        if data and 'onde_class' in data:
            classes_data.append(data)
            
    # Sort to ensure consistent output (ROOT first, then alphabetical)
    classes_data.sort(key=lambda x: ("" if x['onde_class'] == 'ROOT' else x['onde_class']))
    
    with open(output_csv, 'w', encoding='utf-8-sig', newline='') as f:
        header = ['Class', 'Name', 'Comments', 'M or O', 'D or A', 'Class', 'Dims', 'Size or content', 'Min', 'Max', 'Accessory Class']
        f.write(';'.join(header) + '\n')
        
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
                # Retain original "A or D" value if specified exactly like that
                if storage == 'A or D':
                    d_a = 'A or D'
                    
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
                    field.get('allowed_values', ''),
                    field.get('min_value', ''),
                    field.get('max_value', ''),
                    ''
                ]
                
                # Format without strict CSV quoting to preserve intended json-like arrays and pipe-separations
                row_str = ';'.join(str(x).replace('\\n', ' ').replace(';', ',') for x in row) + '\\n'
                f.write(row_str)

    print(f"Generated {output_csv} successfully from {len(classes_data)} classes.")

if __name__ == '__main__':
    generate_csv()
