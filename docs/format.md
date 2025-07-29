# Format

This section explains the overall documentation structure, supported file formats,
directory layout, and style conventions for the a5c documentation site.

## Document Structure

The documentation sources live under the `docs/` directory and are rendered with
Sphinx using the MyST parser. The top-level table of contents is defined in
`docs/index.md`:

```rst
```{toctree}
:maxdepth: 2

specs
howtos
guide
vision
architecture
format
community
tutorials
start_here
reference
```
```

Each entry corresponds to a major topic in the documentation:

- **specs**: Detailed specifications and design decisions.
- **howtos**: Task-oriented step-by-step guides.
- **guide**: User guide and overview.
- **vision**: Project goals and roadmap.
- **architecture**: System architecture and components.
- **format**: (This file) Documentation source conventions.
- **community**: Contribution and community guidelines.
- **tutorials**: Hands-on tutorials and examples.
- **start_here**: Quick start and prerequisites.
- **reference**: API reference and command-line docs.

## Supported File Formats

a5c documentation supports two markup syntaxes:

### Markdown (MyST)

- Files with the `.md` extension are parsed by the MyST parser, enabling Sphinx
  directives and roles within Markdown.
- Use fenced code blocks with language identifiers. For example:

  ```markdown
  ```python
  def example():
      return True
  ```
  ```

### reStructuredText (RST)

- Files with the `.rst` extension follow standard reStructuredText syntax.
- Use literal blocks and directives as usual. For example:

  ```rst
  .. warning::
     Be careful when editing configuration files.
  ```

## Directory Layout

Maintain a flat layout under `docs/` for core pages. A typical directory tree:

```text
docs/
├── architecture.md
├── community.md
├── format.md        ← this file
├── guide.md
├── howtos.md
├── index.md
├── reference.md
├── specs.md
├── start_here.md
├── tutorials.md
└── conf.py
```

For larger topics or multiple examples, create subdirectories (e.g., `docs/howtos/`)
and reference them in the toctree.

## Formatting Guidelines

Follow these conventions to keep the documentation consistent and reader-friendly:

### Headings

- Use ATX-style headings (`#`, `##`, `###`, `####`). Do not exceed four levels.

### Lists

- Use hyphens (`-`) for unordered lists and numbers for ordered steps:

  ```markdown
  - First item
  - Second item

  1. Step one
  2. Step two
  ```

### Code Blocks

- Use fenced code blocks with the language tag.
- Include brief captions or comments if the intent is not obvious.

### Links and Cross-References

- Use relative links for internal pages:

  ```markdown
  See [Quick Start](start_here.md) for setup instructions.
  ```
- For API or section links, prefer MyST roles when available.

### Admonitions (Notes, Warnings, Tips)

- Use MyST directive syntax for emphasis:

  ```markdown
  ```{tip}
  You can run `make docs` to build locally.
  ```
  ```

### General Style

- Write in plain, active voice and second person (“you”).
- Keep paragraphs short and focused on a single idea.
- Use whitespace to separate sections and improve readability.
