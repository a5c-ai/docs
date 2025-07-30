# Start Here

Get started with a5c in minutes by following this quickstart guide. You'll set up your environment, enable AI agents in your repository, and run your first agent workflow.

## Prerequisites

- **Git** installed on your local machine (version 2.0+).
- A **GitHub repository** where you have write access.
- GitHub **Actions** and **Issues** are enabled in the repository settings.
- An AI provider account:
  - **OpenAI**: API key from `https://platform.openai.com/account/api-keys`
  - **Anthropic**: API key from `https://console.anthropic.com/account/keys`

## 5-Minute Quickstart

1. **Add your API key to GitHub**  
   In your repository, go to **Settings → Secrets and variables → Actions → New repository secret**.  
   - Secret name: `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`  
   - Secret value: Your provider API key.

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
   Ensure **Issues** and **Actions** are enabled under **Settings → General → Features**.

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
