# Start Here

Get started with a5c in minutes by following this quickstart guide. You'll set up your environment, enable AI agents in your repository, and run your first agent workflow.

This guide supports two workflows:

- **New Project**: Initialize and set up a brand-new GitHub repository with a5c.
- **Existing Project**: Add a5c to an existing GitHub repository with minimal setup.

## New Project

If you are starting a brand-new GitHub repository, first create a new repository where you have write access.

## Existing Project

If you already have a GitHub repository, ensure you have write access and navigate to it to add a5c.

## Prerequisites

- **Git** installed on your local machine (version 2.0+).
- A **GitHub repository** where you have write access.
- GitHub **Actions** and **Issues** are enabled under **Settings → General → Features** (ensure both boxes are checked).
- An AI provider account:
  - **OpenAI**: API key from `https://platform.openai.com/account/api-keys`
  - **Anthropic**: API key from `https://console.anthropic.com/account/keys`

## 5-Minute Quickstart

1. **Add your environment variables to GitHub**  
   In your repository, go to **Settings → Secrets and variables → Actions**, then create a **New repository secret** (for API keys) and a **New repository variable** (for additional settings).  
   
   - Secret name: `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`  
     Secret value: Your provider API key.  
   - Variable name: `A5C_CLI_TOOL`  
     Variable value: One of `claude`, `codex`, `azure_codex`, or `gemini`.  
     *Note*: Free GitHub users cannot set organization-level variables. If you have a Pro or Team plan, you can also set `A5C_CLI_TOOL` at the organization or user level to apply across all your repositories.

2. **Wake up your repository**  
   Create the GitHub Actions workflow file at `.github/workflows/a5c.yml`:

```yaml
on: [pull_request, issues, issue_comment, push]

jobs:
  a5c:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
      issues: write
    steps:
      - uses: actions/checkout@v4
      - uses: a5c-ai/action@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
```

3. **Enable repository features**  
   Go to **Settings → General → Features** in your repository and ensure that **Issues** and **Actions** are enabled (checkboxes checked).

## Activating Agents

There are two main ways to activate or run agents in your repository:

### Via GitHub events and mentions

Agents respond to GitHub events (e.g., pushes, pull requests, issue comments) through the workflow you created above. You can trigger agents by:

- **Mention-based activation**: Mention an agent name (e.g., `@agent-name`) in issue or PR comments, code comments, or commit messages.
- **Label-based activation**: Add specific issue or PR labels configured in your `.a5c/config.yml` to automatically run agents when labels change.
- **Event-based activation**: Agents defined with event filters in their frontmatter will run automatically on matching GitHub events (e.g., every push, PR open).

### Via file-based configuration

You can also activate agents by adding agent definition files in your repository:

```text
.a5c/
├── config.yml         # Repository-wide configuration and default triggers
└── agents/
    └── my-agent.md    # Markdown file with YAML frontmatter defining triggers and prompts
```

Each agent file under `.a5c/agents/` contains YAML frontmatter that defines its name, description, triggers, and routing information. When you push or merge these files, the agents are loaded by the a5c GitHub Action and will run automatically when their triggers match events in your repository.

## Before You Launch

A full-featured and complex project can nudge toward $20-50. Worth it for what used to be months of work, but set a cap if you like.

## Next Steps

Explore the rest of the a5c documentation to learn about configuration, advanced usage, and custom agent development:

```{toctree}
:maxdepth: 1

guide
howtos
reference
tutorials
community
architecture
vision
format
specs
```
