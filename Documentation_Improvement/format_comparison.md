# Format Comparison: Seven Candidate Formats for ONDE Specification

All seven prototype formats have been written to `Documentation_Improvement/` using
the same two representative classes (ONDE_COMPONENT family and ONDE_ULTRASONIC_SETUP).

**Design principle:** Each file contains only the minimum authoritative data needed —
class name, inheritance parent, field definitions (with full prefixed names), and
narrative documentation. Properties that can be inferred (e.g., subclass lists,
format version) are omitted and derived automatically by tooling.

## Files Created

| Format | Folder | Files |
|---|---|---|
| Markdown | `Markdown/` | `component.md`, `ultrasonic_setup.md` |
| reStructuredText | `reStructuredText/` | `component.rst`, `ultrasonic_setup.rst` |
| MyST Markdown | `MyST/` | `component.md`, `ultrasonic_setup.md` |
| AsciiDoc | `AsciiDoc/` | `component.adoc`, `ultrasonic_setup.adoc` |
| YAML+Markdown | `YAML/` | `component.yaml`, `ultrasonic_setup.yaml` |
| XML | `XML/` | `component.xml`, `ultrasonic_setup.xml` |
| JSON | `JSON/` | `component.json`, `ultrasonic_setup.json` |

---

## Feature Comparison

| Criteria | Markdown | RST | MyST | AsciiDoc | YAML+MD | XML | JSON |
|---|---|---|---|---|---|---|---|
| **GitHub rendering** | Excellent | Poor | Partial | Good | None | None | None |
| **Class metadata** | YAML frontmatter | Field lists | YAML-like directive | Doc attributes | Native YAML | XML attributes | Object keys |
| **Field metadata** | Bullet lists | Field lists (`:key: val`) | Definition lists | Definition lists | YAML dict | `<field>` elements | Array of objects |
| **Machine parseability** | Good | Good | Good | Good | Trivial | Trivial | Trivial |
| **Inline figures** | Native | Directive | Directive | Image macro | MD in YAML | MD in CDATA | MD in strings |
| **Math/formulas** | Limited | Excellent | Excellent | Good (stem) | Limited | Limited | Limited |
| **Cross-references** | Manual links | `:ref:` role | `{ref}` role | `<<anchor>>` | Manual | Manual | Manual |
| **Admonitions** | Blockquotes | Native dirs | `:::` dirs | Single-word | MD in YAML | Custom elements | N/A |
| **Doc generation** | MkDocs/Jekyll | Sphinx | Sphinx | Asciidoctor | Custom | XSLT / Custom | Custom |
| **Collaboration ease** | Very easy | Hard | Easy | Moderate | Moderate | Hard | Moderate |
| **Extensibility** | Limited | Excellent | Good | Moderate | N/A | XSD/Schematron | JSON Schema |
| **Spec/standards use** | Rare | Moderate | New | Common | Moderate | Common | Common |
| **Parser stdlib?** | No | No | No | No | No (PyYAML) | Yes (xml.etree) | Yes (json) |

---

## Key Trade-offs

### Markdown Strengths
- **GitHub-native**: Files render beautifully right in the repository — no build step needed for review
- **Low barrier**: Every developer already knows markdown; PR reviews are natural
- **YAML frontmatter**: Clean, standard way to embed machine-parseable class metadata
- **Mermaid diagrams**: Render directly on GitHub

### Markdown Weaknesses
- **No native extensibility**: Can't define custom structured elements (e.g., a "field definition" directive)
- **Table fragility**: Pipe tables break alignment with long content; no easy way to have multi-line cells
- **Subclass metadata**: Awkward to embed YAML for subclasses within the same file (used HTML comments as workaround)
- **Math support**: Limited compared to RST/LaTeX

### RST Strengths
- **Sphinx ecosystem**: Mature doc generation, cross-reference validation, multi-format output (HTML, PDF, ePub)
- **Custom directives**: Could create `.. onde-field::` directives for perfectly structured field definitions
- **Native math**: Full LaTeX math rendering
- **List-tables**: Handle complex content much better than pipe tables

### RST Weaknesses
- **Poor GitHub rendering**: Directives, list-tables, and math don't render on GitHub — requires a build step to preview
- **Contributor barrier**: RST is less familiar; indentation errors cause cryptic failures
- **Verbosity**: List-tables are ~4x more lines than equivalent markdown tables
- **Custom parsers**: Harder to write simple extraction scripts compared to YAML+markdown tables

### MyST Markdown Strengths
- **Best of both worlds**: Markdown readability with Sphinx's full power (cross-refs, math, directives)
- **Sphinx-native**: Processed by `myst-parser`; full Sphinx toolchain for HTML/PDF output
- **Familiar syntax**: Base syntax is markdown; directives use `:::` fences which feel natural
- **Cross-references**: `{ref}` role provides validated cross-references like RST
- **Math**: Full LaTeX `$$` support, rendered by Sphinx

### MyST Markdown Weaknesses
- **Partial GitHub rendering**: Base markdown renders; but `:::` directives, `{ref}` roles, and `list-table` show as raw text on GitHub
- **Newer ecosystem**: Less mature than RST/Sphinx; fewer examples and community resources
- **Directive syntax**: `:::` fence blocks don't render on GitHub (shows raw content with `:::` markers)
- **Metadata**: No standard equivalent to YAML frontmatter for class metadata (used `:::{metadata}` which is non-standard)

### AsciiDoc Strengths
- **Purpose-built for specs**: Used by IETF, Eclipse, Spring — designed for technical specifications
- **Good GitHub rendering**: Tables, admonitions, images, cross-references all render on GitHub
- **Tables**: Handle multi-line cells and complex content naturally
- **Document attributes**: `:key: value` pairs in the header work like YAML frontmatter for metadata
- **Admonitions**: Single-word syntax (`WARNING:`, `IMPORTANT:`) is the simplest of all formats
- **Cross-references**: `<<anchor>>` syntax works within and across files

### AsciiDoc Weaknesses
- **Less familiar**: Most developers don't know AsciiDoc syntax
- **Ruby toolchain**: Asciidoctor is Ruby-based (though JavaScript and Java versions exist)
- **No Sphinx integration**: Separate ecosystem from Sphinx; fewer academic/scientific extensions
- **Table parsing**: AsciiDoc tables are parseable but require an AsciiDoc-specific parser
- **Math**: `stem` blocks support LaTeX but less mature than Sphinx's math rendering

### YAML+Markdown Strengths
- **Trivially machine-parseable**: Just `yaml.safe_load()` — no custom parser needed at all
- **Structured-first**: Field definitions are first-class data, not text to be parsed from tables
- **Enum support**: Enum values naturally map to YAML dicts with descriptions
- **Validation-friendly**: Easiest format to generate JSON Schema or CSV from
- **Explicit metadata**: Every property (default, units, ref_target, conditional_requirement) is a named key

### YAML+Markdown Weaknesses
- **Not human-documentation**: YAML files don't render as documentation on GitHub or anywhere
- **Painful for prose**: Multi-line text in YAML requires `|` blocks with careful indentation
- **Figures in YAML**: Markdown image links inside YAML strings feel unnatural and don't preview
- **No direct rendering**: Requires a custom rendering tool to produce any human-readable output
- **Collaboration friction**: Editing YAML is less intuitive than editing a document format for many contributors

### XML Strengths
- **Trivially machine-parseable**: `xml.etree.ElementTree` is in Python's stdlib — zero dependencies
- **Self-describing schema**: Field metadata maps naturally to XML attributes; descriptions to child elements
- **XSD validation**: Can define an XML Schema (XSD) to validate source files before processing
- **Enum support**: Enum values as `<value>` child elements with descriptions — clean and structured
- **Widely supported**: Every programming language has a mature XML parser
- **Common for specifications**: Used by many standards bodies (W3C, OASIS, OMG) for format definitions

### XML Weaknesses
- **Not human-friendly**: XML is verbose and visually noisy (closing tags, entity escaping like `&lt;` for `<`)
- **No GitHub rendering**: XML files show as raw markup on GitHub — no documentation preview
- **Entity escaping burden**: Angle brackets in dimension expressions (`N_Ascan<m>`) must be escaped as `&lt;` / `&gt;`
- **Painful for prose**: Multi-paragraph descriptions inside XML elements feel unnatural
- **Merge conflicts**: XML's nesting makes diff/merge harder than flat text formats
- **Requires transformation**: XSLT or custom tool needed to produce readable documentation

### JSON Strengths
- **Trivially machine-parseable**: `json.loads()` is in Python's stdlib — zero dependencies
- **No escaping burden**: Angle brackets in dimension strings are plain text (unlike XML's `&lt;`)
- **Ubiquitous**: Every programming language has native JSON support
- **JSON Schema**: Can define a formal JSON Schema to validate source files with standard tooling
- **Clean structure**: Fields as arrays of objects are intuitive and diff-friendly (one field per object)
- **IDE support**: Excellent autocomplete and validation via JSON Schema in editors

### JSON Weaknesses
- **No comments**: JSON has no comment syntax — can't annotate source files inline
- **No GitHub rendering**: Raw JSON on GitHub is readable but not documentation
- **Trailing commas**: JSON forbids trailing commas — common source of syntax errors during editing
- **Painful for prose**: Multi-line descriptions require `\n` escaping or single long strings
- **No direct rendering**: Requires custom tool to produce human-readable documentation
- **Less readable than YAML**: More syntactic noise (braces, quotes, commas on every line)

---

## Open Questions

1. **How important is GitHub rendering?** If collaborators primarily review rendered docs on a GitHub Pages site, poor GitHub rendering matters less. If they review directly in PRs, Markdown or AsciiDoc are strongly preferred.

2. **Sphinx vs. other toolchains?** MyST and RST tie you to Sphinx (powerful but Python-specific). AsciiDoc uses Asciidoctor. Plain Markdown has many options. YAML needs a custom tool.

3. **Machine parseability priority?** If generating validation schemas is a primary concern, YAML is unbeatable. If documentation comes first and schema extraction is secondary, a document format with structured tables is better.

4. **Contributor profile?** If contributors are primarily NDE engineers (not software developers), simpler formats (Markdown, AsciiDoc) win. If they're comfortable with structured data, YAML or MyST could work.

5. **Could a hybrid work?** For example, YAML for field definitions plus Markdown files for narrative documentation, linked together by class name. This separates concerns but adds complexity.

