# User Guide

Welcome to the **a5c User Guide**. This section describes how to install, configure, and get started with a5c — the Git-native AI agent orchestration platform.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Git** (version 2.30 or later)
- **Python** (version 3.8 or later)
- **pip** (for Python package management)
- **GitHub token** with repository permissions (set `GITHUB_TOKEN` environment variable)
- **AI model credentials** (e.g., `AZURE_OPENAI_API_KEY` for Azure OpenAI)

## Installation

Install a5c via pip:

```bash
pip install a5c-ai
```

Alternatively, install from source:

```bash
git clone https://github.com/a5c-ai/action.git a5c
cd a5c
pip install -e .
```

## Configuration

a5c uses a configuration file at `.a5c/config.yml`. To create a default config file, run:

```bash
a5c init
```

Then, edit `.a5c/config.yml` to customize your environment. For example:

```yaml
defaults:
  cli_command: "codex exec --dangerously-bypass-approvals-and-sandbox -c model=codex-mini"
remote_agents:
  enabled: true
  cache_timeout: 120
  retry_attempts: 5
```

Alternatively, you can configure a5c using environment variables:

| Variable               | Description                             |
|------------------------|-----------------------------------------|
| `GITHUB_TOKEN`         | GitHub API token for authentication     |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key for AI model access |

## Basic Usage

To see available commands, run:

```bash
a5c --help
```

Generate documentation or perform analysis with a specific agent:

```bash
a5c run documenter-agent
```

Or execute the default agent workflow:

```bash
a5c run
```

Example workflow:

```bash
git add .
a5c run
git commit -m "Apply a5c recommendations"
```

## Next Steps

Continue to the [Howtos](howtos.md) for step-by-step tutorials on common tasks.
