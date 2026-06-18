#!/usr/bin/env python3
import os
import sys
import yaml
from pydantic import ValidationError

# Ensure we can import from tools even if called from root
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema_classes import OndeClass

def validate_all():
    schema_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'schema')
    if not os.path.isdir(schema_dir):
        print(f"Directory {schema_dir} not found.")
        sys.exit(1)

    yaml_files = [os.path.join(schema_dir, f) for f in os.listdir(schema_dir) if f.endswith('.yaml')]
    
    errors = 0
    parsed_classes = {}

    print(f"Found {len(yaml_files)} YAML files to validate.")
    
    # Pass 1: Validate individual file schemas
    for f in yaml_files:
        with open(f, 'r', encoding='utf-8') as file:
            try:
                data = yaml.safe_load(file)
                if data is None:
                    print(f"❌ Error: {os.path.basename(f)} is empty.")
                    errors += 1
                    continue
                c = OndeClass(**data)
                parsed_classes[c.onde_class] = c
                print(f"✅ {os.path.basename(f)} valid")
            except ValidationError as e:
                print(f"❌ Validation error in {os.path.basename(f)}:")
                print(e)
                errors += 1
            except Exception as e:
                print(f"❌ Failed to parse {os.path.basename(f)}: {e}")
                errors += 1
                
    if errors > 0:
        print(f"\n❌ Failed parsing with {errors} errors.")
        sys.exit(1)
        
    # Pass 2: Validate relationship references
    print("\nValidating cross-references...")
    for c_name, c_obj in parsed_classes.items():
        # Check inherits
        for parent in c_obj.inherits:
            if parent not in parsed_classes:
                print(f"❌ Error in {c_name}: Inherits from unknown class '{parent}'")
                errors += 1
        # Check accessories
        for acc in c_obj.accessories:
            if acc not in parsed_classes:
                print(f"❌ Error in {c_name}: Accessory '{acc}' is unknown")
                errors += 1
                
    if errors > 0:
        print(f"\n❌ Validation failed with {errors} cross-reference errors.")
        sys.exit(1)

    print("\n🎉 All schema files validated successfully!")
    sys.exit(0)

if __name__ == "__main__":
    validate_all()
