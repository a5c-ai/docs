# Format

This document describes the formatting conventions for a5c documentation content, including file organization, supported file formats, and style guidelines for Markdown and reStructuredText.

## Document Structure

- All source files live under the `docs/` directory.
- Chapters and topics are defined via Sphinx `toctree` directives in `index.md`.
- Keep related files together and use clear, descriptive file names.

## Supported File Formats

- **Markdown (`.md`)** — Primary format for user-facing content.
- **reStructuredText (`.rst`)** — Used for low-level Sphinx directives or extensions.

## Style Guidelines

- Use ATX-style headings (`#`, `##`, `###`), with a single space after the hash symbols.
- Write in plain, active voice and address the reader as "you".
- Keep paragraphs short (2–4 sentences) and break up long sections with subheadings or bullet lists.
- Limit line length to ~80 characters for better readability in editors.

### Code Blocks and Syntax Highlighting

- Use fenced code blocks with an explicit language tag:
  ```bash
  git commit -m "Add feature"
  ```
- For Python examples:
  ```python
  def greet(name: str) -> None:
      print(f"Hello, {name}")
  ```

### Sphinx Directives

- **Toctree**: Group related topics.
  ```rst
  .. toctree::
     :maxdepth: 2

     guide
     howtos
  ```
- **Admonitions**: Use for notes, warnings, and tips.
  ```rst
  .. note::
     Always run `make clean` before rebuilding.
  ```

### Links and Cross-Referencing

- Use relative links for internal references (e.g., `[Guide](guide.md)`).
- Link to external resources sparingly and open them in a new context when appropriate.

## Acceptance Criteria

- Document structure and conventions are clearly defined.
- Examples illustrate key formatting rules.
