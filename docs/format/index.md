# Format

This section defines the documentation **format guidelines**, the **directory structure**, and **file naming conventions** used across the a5c documentation site. It also provides placeholders for format examples and conventions.

## Format Guidelines

- Write all content in Markdown (`.md`) using MyST Markdown for Sphinx compatibility.
- Use headings to organize content:
  - `#` for top-level titles (one per page).
  - `##` for major sections.
  - `###` for subsections.
- Include code blocks with language identifiers for clarity:

````markdown
```bash
# example command
```
````

- Use horizontal rules (`---`) to separate logical sections when needed.
- Add admonitions for notes, warnings, and tips using MyST syntax:

```markdown
::: note
This is a note.
:::
```

## Directory Structure

The documentation repository follows a consistent directory layout:

```text
docs/
├── specs/
├── howtos/
├── guide/
├── vision/
├── architecture/
├── format/
│   └── index.md
├── community/
├── tutorials/
├── start_here/
└── reference/
```

Each main section resides in its own folder containing an `index.md` and related pages.

## File Naming Conventions

- Use lowercase letters and hyphens (`-`) to separate words.
- Filenames should be descriptive and end with the `.md` extension.
- Avoid spaces, special characters, or uppercase letters.
- Example filenames:
  - `getting-started.md`
  - `api-reference.md`
  - `formatting-examples.md`

## Placeholders for Examples

<!-- Add concrete examples of markdown formatting, table templates, admonitions, and code snippets below -->

````markdown
<!-- Example: Table template -->
| Column A | Column B |
|----------|----------|
| Value 1  | Value 2  |

<!-- Example: Code snippet -->
```python
def hello():
    print("Hello, a5c!")
```

<!-- Example: Admonition -->
::: warning
This is a warning placeholder.
:::
````
