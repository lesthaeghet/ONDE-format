# Format Comparison: Five Candidate Formats for ONDE Specification

All five prototype formats have been written to `Documentation_Improvement/` using
the same two representative classes (ONDE_COMPONENT family and ONDE_ULTRASONIC_SETUP).

## Files Created

| Format | Folder | Files |
|---|---|---|
| Markdown | `Markdown/` | `component.md`, `ultrasonic_setup.md` |
| reStructuredText | `reStructuredText/` | `component.rst`, `ultrasonic_setup.rst` |
| MyST Markdown | `MyST/` | `component.md`, `ultrasonic_setup.md` |
| AsciiDoc | `AsciiDoc/` | `component.adoc`, `ultrasonic_setup.adoc` |
| YAML+Markdown | `YAML/` | `component.yaml`, `ultrasonic_setup.yaml` |

---

## Feature Comparison

| Criteria | Markdown | RST | MyST | AsciiDoc | YAML+MD |
|---|---|---|---|---|---|
| **GitHub rendering** | Excellent | Poor | Partial | Good | None |
| **Class metadata** | YAML frontmatter | Field lists | YAML-like directive | Doc attributes | Native YAML |
| **Field def table** | Pipe tables | list-table | list-table | AsciiDoc tables | YAML dict |
| **Machine parseability** | Good | Hard | Good | Moderate | Trivial |
| **Inline figures** | Native | Directive | Directive | Image macro | Markdown in YAML |
| **Math/formulas** | Limited | Excellent | Excellent | Good (stem) | Limited |
| **Cross-references** | Manual links | `:ref:` role | `{ref}` role | `<<anchor>>` | Manual |
| **Admonitions** | Blockquotes | Native directives | `:::` directives | Single-word | Markdown in YAML |
| **Doc generation** | MkDocs/Jekyll | Sphinx | Sphinx | Asciidoctor | Custom tool |
| **Collaboration ease** | Very easy | Hard | Easy | Moderate | Moderate |
| **Extensibility** | Limited | Excellent | Good | Moderate | N/A |
| **Spec/standards use** | Rare | Moderate | New | Common | Moderate |

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

---

## Open Questions

1. **How important is GitHub rendering?** If collaborators primarily review rendered docs on a GitHub Pages site, poor GitHub rendering matters less. If they review directly in PRs, Markdown or AsciiDoc are strongly preferred.

2. **Sphinx vs. other toolchains?** MyST and RST tie you to Sphinx (powerful but Python-specific). AsciiDoc uses Asciidoctor. Plain Markdown has many options. YAML needs a custom tool.

3. **Machine parseability priority?** If generating validation schemas is a primary concern, YAML is unbeatable. If documentation comes first and schema extraction is secondary, a document format with structured tables is better.

4. **Contributor profile?** If contributors are primarily NDE engineers (not software developers), simpler formats (Markdown, AsciiDoc) win. If they're comfortable with structured data, YAML or MyST could work.

5. **Could a hybrid work?** For example, YAML for field definitions plus Markdown files for narrative documentation, linked together by class name. This separates concerns but adds complexity.

