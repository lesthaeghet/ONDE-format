"""
Generate Documentation for ONDE Format using YAML Single Source of Truth.
This script uses Pydantic for validation, Jinja2 for templating, and MkDocs for rendering.
"""
import os
import sys
import argparse
import yaml
import glob
import shutil
import subprocess

try:
    from pydantic import BaseModel, ValidationError
    from jinja2 import Template
except ImportError:
    print("Missing required packages. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pydantic", "jinja2", "mkdocs", "mkdocs-material"])
    from pydantic import BaseModel, ValidationError
    from jinja2 import Template

from typing import Dict, List, Optional, Any

# ==========================================
# PYDANTIC SCHEMA DEFINITIONS
# ==========================================

class OndeField(BaseModel):
    full_name: str
    required: bool = False
    storage: Optional[str] = None
    hdf5_type: str
    description: str = ""
    short_description: Optional[str] = None
    dimensions: Optional[str] = None
    allowed_values: Optional[str] = None
    ref_target: Optional[str] = None

class OndeClass(BaseModel):
    onde_class: str
    inherits: List[str] = []
    description: str = ""
    fields: Dict[str, OndeField] = {}

# ==========================================
# JINJA2 TEMPLATES
# ==========================================

CLASS_TEMPLATE = """\
# {{ cls.onde_class }}

{% if mermaid_graph %}
```mermaid
classDiagram
{{ mermaid_graph }}
```
{% endif %}

{{ cls.description }}

{% if cls.fields %}
## Fields

<div class="field-list" markdown="1">
{% for name, f in fields_meta %}
<details class="field-details" markdown="1">
<summary markdown="1"><div class="field-summary-top" markdown="span"><strong id="{{ cls.onde_class | lower }}-{{ name | lower | replace(' ', '-') }}"><code>{{ name }}</code></strong> &mdash; {{ f.short_desc }}</div><div class="field-summary-bottom" markdown="span">{{ f.html_type }}</div></summary>

<div class="field-content" markdown="1">

{{ f.description if f.description else "No detailed description provided." }}

---

**Type:** <span markdown="span">{{ f.html_type }}</span> | **Dimensions:** `{{ f.dimensions }}` | **Required:** {{ f.req_str }} | **Storage:** {{ f.storage }}{% if f.allowed %} | **Allowed:** `{{ f.allowed }}`{% endif %}

</div>
</details>
{% endfor %}
</div>
{% endif %}
"""

MKDOCS_YML = """\
site_name: ONDE Format Specification
use_directory_urls: false
theme:
  name: material
markdown_extensions:
  - attr_list
  - md_in_html
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
extra_javascript:
  - javascripts/mathjax.js
  - https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js
extra_css:
  - stylesheets/extra.css
nav:
  - Overview: index.md
{% for cls in classes %}
  - {{ cls }}: {{ cls | lower }}.md
{% endfor %}
"""

def main():
    parser = argparse.ArgumentParser(description="Generate MkDocs HTML docs from SSOT")
    parser.add_argument('--format', choices=['markdown', 'yaml'], required=True)
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    
    if args.format != 'yaml':
        print("Error: The modern generator strictly supports YAML as the Single Source of Truth.")
        sys.exit(1)
        
    docs_dir = os.path.join(args.output, 'docs')
    os.makedirs(docs_dir, exist_ok=True)
    
    # Enable Math rendering via MathJax
    js_dir = os.path.join(docs_dir, 'javascripts')
    os.makedirs(js_dir, exist_ok=True)
    with open(os.path.join(js_dir, 'mathjax.js'), 'w') as f:
        f.write('''window.MathJax = {
  tex: {
    inlineMath: [["\\\\(", "\\\\)"]],
    displayMath: [["\\\\[", "\\\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};''')
    
    # Custom CSS for tighter tables
    css_dir = os.path.join(docs_dir, 'stylesheets')
    os.makedirs(css_dir, exist_ok=True)
    with open(os.path.join(css_dir, 'extra.css'), 'w') as f:
        f.write('''
details.field-details {
    border: 1px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.12));
    border-radius: 0.2rem;
    margin-bottom: 0.5rem;
    background-color: var(--md-default-bg-color);
    box-shadow: 0 2px 2px rgba(0,0,0,0.05);
}
details.field-details > summary {
    padding: 0.8rem 1rem;
    cursor: pointer;
    list-style: none;
    position: relative;
    padding-left: 2.5rem;
    background-color: var(--md-code-bg-color);
}
details.field-details > summary::-webkit-details-marker,
details.field-details > summary::marker {
    display: none;
}
details.field-details > summary::before {
    content: "";
    position: absolute;
    left: 1rem;
    top: 1.2rem;
    width: 6px;
    height: 6px;
    border-right: 2px solid var(--md-default-fg-color--light);
    border-bottom: 2px solid var(--md-default-fg-color--light);
    transform: rotate(-45deg);
    transition: transform 0.2s ease-in-out;
}
details.field-details[open] > summary::before {
    transform: rotate(45deg);
    top: 1rem;
}
details.field-details > summary:hover {
    background-color: rgba(128, 128, 128, 0.05);
}
details.field-details > summary .field-summary-top {
    font-weight: 500;
    margin-bottom: 0.2rem;
    color: var(--md-default-fg-color);
}
details.field-details > summary .field-summary-bottom {
    font-family: var(--md-code-font-family);
    font-size: 0.85em;
    color: var(--md-default-fg-color--light);
    word-break: break-word;
}
details.field-details[open] > summary {
    border-bottom: 1px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.12));
}
details.field-details .field-content {
    padding: 1rem;
}
details.field-details .field-content hr {
    margin: 1rem 0;
}
''')
    
    # Fix the src_images path since it's two levels up (ONDE-format/images)
    src_images = os.path.normpath(os.path.join(args.input, '..', '..', 'images'))
    dest_images = os.path.join(docs_dir, 'images')
    if os.path.exists(src_images):
        if os.path.exists(dest_images):
            shutil.rmtree(dest_images)
        shutil.copytree(src_images, dest_images)
    
    files = glob.glob(os.path.join(args.input, '*.yaml'))
    
    parsed_classes = {}
    children_map = {}
    
    print("Parsing and validating YAML files with Pydantic...")
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            
        try:
            # Validate with Pydantic
            validated_data = OndeClass(**data)
            cls_name = validated_data.onde_class
            parsed_classes[cls_name] = validated_data
            
            for parent in validated_data.inherits:
                children_map.setdefault(parent, []).append(cls_name)
        except ValidationError as e:
            print(f"Validation error in {filepath}:\n{e}")
            sys.exit(1)
            
    print("Building relationships and generating Markdown...")
    class_names = list(parsed_classes.keys())
    class_names.sort(key=lambda x: ("" if x == 'ROOT' else x))
    
    template = Template(CLASS_TEMPLATE)
    
    for cls_name, cls_obj in parsed_classes.items():
        parents = cls_obj.inherits
        children = children_map.get(cls_name, [])
        
        # Build local mermaid graph
        mermaid_lines = []
        unique_classes = set([cls_name])
        
        for parent in parents:
            mermaid_lines.append(f"  {parent} <|-- {cls_name}")
            unique_classes.add(parent)
            
        for child in children:
            mermaid_lines.append(f"  {cls_name} <|-- {child}")
            unique_classes.add(child)
            
        for fname, field in cls_obj.fields.items():
            ref = field.ref_target
            if ref and ref in parsed_classes:
                mermaid_lines.append(f"  {cls_name} o-- {ref} : {fname}")
                unique_classes.add(ref)
                
        for c in unique_classes:
            mermaid_lines.append(f'  click {c} href "{c.lower()}.html"')
            
        mermaid_graph = "\n".join(mermaid_lines) if mermaid_lines else ""
        
        # Prepare template variables
        fields_meta = []
        for fname, f in cls_obj.fields.items():
            # Build short desc
            short_desc = f.short_description or ""
            if not short_desc:
                full_desc = f.description or ""
                short_desc = full_desc.split('.')[0] + '.' if '.' in full_desc else full_desc
                if short_desc == '.': short_desc = ''
            short_desc = short_desc.replace('|', '\\|').replace('\n', '<br>')
            
            # HTML type with hyperlink if ref target exists
            html_type = f.hdf5_type.replace('<', '&lt;').replace('>', '&gt;')
            if f.ref_target:
                if f.ref_target in parsed_classes:
                    html_type += f"&lt;[{f.ref_target}]({f.ref_target.lower()}.md)&gt;"
                else:
                    html_type += f"&lt;{f.ref_target}&gt;"
                    
            allowed = (f.allowed_values or '').replace('|', '\\|')
            allowed = allowed.replace('["', '').replace('"]', '').replace('", "', ', ')
            
            dims = (f.dimensions or '')
            
            meta = {
                'full_name': f.full_name,
                'req_str': 'Yes' if f.required else 'No',
                'storage': f.storage or '',
                'html_type': html_type,
                'dimensions': dims,
                'allowed': allowed,
                'short_desc': short_desc,
                'description': f.description
            }
            fields_meta.append((fname, meta))
            
        md_content = template.render(
            cls=cls_obj,
            mermaid_graph=mermaid_graph,
            fields_meta=fields_meta
        )
        md_content = md_content.replace('../images/', 'images/')
        
        out_filepath = os.path.join(docs_dir, f"{cls_name.lower()}.md")
        with open(out_filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
    # Write Overview
    overview_src = os.path.join(args.input, 'overview.md')
    if os.path.isfile(overview_src):
        # Generate master diagram
        master_lines = []
        unique_classes = set()
        for cls_name, cls_obj in parsed_classes.items():
            unique_classes.add(cls_name)
            for parent in cls_obj.inherits:
                master_lines.append(f"  {parent} <|-- {cls_name}")
                unique_classes.add(parent)
            for fname, field in cls_obj.fields.items():
                ref = field.ref_target
                if ref and ref in parsed_classes:
                    master_lines.append(f"  {cls_name} o-- {ref} : {fname}")
                    unique_classes.add(ref)
                    
        for c in unique_classes:
            master_lines.append(f'  click {c} href "{c.lower()}.html"')
            
        master_mermaid = "classDiagram\n" + "\n".join(master_lines)
        
        with open(overview_src, 'r', encoding='utf-8') as f:
            overview_content = f.read()
            
        overview_content = overview_content.replace('../images/', 'images/')
        overview_content = overview_content.replace('\\<p\\>', '(p)').replace('\\<m\\>', '(m)').replace('\\<k\\>', '(k)')
            
        overview_content = overview_content.replace('<!-- AUTO_GENERATED_DATA_MODEL -->', f"```mermaid\n{master_mermaid}\n```")
        
        with open(os.path.join(docs_dir, 'index.md'), 'w', encoding='utf-8') as f:
            f.write(overview_content)
            
    # Write mkdocs.yml
    mkdocs_yaml_path = os.path.join(args.output, 'mkdocs.yml')
    with open(mkdocs_yaml_path, 'w', encoding='utf-8') as f:
        f.write(Template(MKDOCS_YML).render(classes=class_names))
        
    print("Running mkdocs build...")
    # Need to run mkdocs inside the output directory
    subprocess.check_call([sys.executable, "-m", "mkdocs", "build"], cwd=args.output)
    
    print(f"Documentation successfully generated using MkDocs at {os.path.join(args.output, 'site', 'index.html')}")

if __name__ == '__main__':
    main()
