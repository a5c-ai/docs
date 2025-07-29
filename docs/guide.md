# User Guide

This guide provides detailed instructions for installing, configuring, and using **a5c** in your projects. You'll learn how to set up the documentation environment, configure AI agents, and run common workflows.

## Installation

Install the required dependencies and set up your local environment to build the a5c documentation and enable AI agents in your repository.

### Prerequisites

- **Python 3.8+** installed
- **Git** (version 2.20+)
- A GitHub repository where you have write access

### Install Dependencies

Clone the a5c docs repository and install Python dependencies:

```bash
git clone https://github.com/a5c-ai/docs.git
cd docs
pip install -U pip setuptools wheel
pip install -r ../requirements.txt
```

Build the documentation locally:

```bash
sphinx-build -b html . _build/html
# or
# make html  (if you have a Makefile)
```

## Configuration

Configure your repository to use a5c AI agents and specify project settings.

### Sphinx Configuration

The docs use the `sphinx_nefertiti` theme and MyST parser. See [conf.py](conf.py) for details:

```python
extensions = [
    "myst_parser",
]
html_theme = "sphinx_nefertiti"
myst_enable_extensions = [
    "deflist",
    "html_admonition",
]
```

### Agent Configuration

Define your remote agents and CLI settings in `.a5c/config.yml`. For example:

```yaml
defaults:
  cli_command: "..."
remote_agents:
  enabled: true
  sources:
    ...
```

Consult the [formatting guide](format.md) for more details on customizing agent behavior.

## Basic Usage

Learn how to invoke common a5c tasks and generate content.

### Running Agents

Use the CLI to run a specific agent:

```bash
# Run the documenter-agent locally
a5c agent run documenter-agent --prompt "Generate user guide section"
```

### Building Documentation

Whenever you update markdown files, rebuild your docs:

```bash
sphinx-build -b html . _build/html
```

or integrate with GitHub Actions to automate builds on push (see [start_here.md](start_here.md)).

## Examples

Below is an example of running a5c to generate an issue comment:

```bash
a5c issue comment --body "@documenter-agent generate docs for new feature"
```

## Integration Points

- **Spec repository**: https://github.com/a5c-ai/spec
- **Action repository**: https://github.com/a5c-ai/action
- **Seed Generic repository**: https://github.com/a5c-ai/seed-generic
- **Registry repository**: https://github.com/a5c-ai/registry

For conceptual overviews and deep dives, see the articles in the [articles directory](https://github.com/a5c-ai/docs/tree/main/articles).
