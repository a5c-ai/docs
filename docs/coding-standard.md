---
title: Coding Standards
---

# Coding Standards

This document defines the coding standards for the a5c documentation repository. It covers repository structure, documentation conventions, agent formatting rules, and pre-commit hooks to ensure consistency and quality across contributions.

## Repository Structure

The repository follows a clear layout to separate content types and configuration:

- `docs/` — Sphinx documentation source (Markdown and reStructuredText files).
- `articles/` — blog-style articles and deep-dive posts.
- `.github_workflows/` — CI/CD workflows and GitHub Actions definitions.
- `.a5c/` — agent configuration and registry settings.
- `README.md` — overview of the project and quick links.

## Documentation Conventions

- **File naming**: Use lowercase file names with hyphens (e.g., `quick-start.md`).
- **Frontmatter**: Add YAML frontmatter at the top of Markdown files:
  ```yaml
  ---
  title: Descriptive page title
  description: A brief summary (optional)
  ---
  ```
- **Headings**: Use ATX-style headings (`#`, `##`, `###`) and limit to six levels.
- **Code blocks**: Use fenced code blocks with language tags:
  ```bash
  git commit -m "Add new feature"
  ```

## Agent Formatting Rules

a5c agents are defined as Markdown files with specific frontmatter fields. Follow these rules when authoring or updating agents:

- Required YAML fields:
  - `id`: unique agent identifier (e.g., `developer-agent`).
  - `name`: human-friendly name.
  - `description`: short summary of the agent's purpose.
  - `category`: agent category (e.g., `development`, `communication`).
- Content structure:
  1. Frontmatter block.
  2. One-line summary under the title.
  3. Detailed sections (`Capabilities`, `Configuration`, `Examples`).

Example:
```markdown
---
id: example-agent
name: Example Agent
description: Demonstrates agent formatting rules.
category: development
---

# Example Agent

This agent is an example showing frontmatter and content layout.

## Capabilities

- Describe agent capabilities here.

## Configuration

- List frontmatter options.

## Examples

```bash
# Example usage
a5c run example-agent
```
```

## Pre-Commit Hooks

We use pre-commit to enforce formatting and linting standards. Ensure your branch includes the following configuration in `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer

  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black

  - repo: https://github.com/PyCQA/isort
    rev: 5.12.0
    hooks:
      - id: isort

  - repo: https://github.com/markdownlint/markdownlint
    rev: v0.37.0
    hooks:
      - id: markdownlint
```

Run `pre-commit install` once to activate the hooks locally.

## Related Resources

- See [Format](format.md) for file format details and conventions.
- See [Specs](specs.md) for specification guidelines and contribution processes.

*** End of File
