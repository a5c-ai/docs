# Installation

This guide explains how to install and set up a5c in your GitHub repository.

## Prerequisites

Before setting up a5c, you'll need:

- A GitHub repository with appropriate permissions
- An Anthropic API key for Claude access
- Any additional service tokens needed for your specific use case (e.g., VERCEL_TOKEN)

## Basic Setup

### 1. Create the Configuration Directory

Create a `.a5c` directory in the root of your repository:

```bash
mkdir -p .a5c
```

### 2. Create the Configuration File

Create a `config.yml` file in the `.a5c` directory:

```yaml
# Basic a5c configuration
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

# Agents to use
agents:
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
```

### 3. Set Up GitHub Action

Create a `.github/workflows/a5c.yml` file:

```yaml
name: a5c Agent System
on:
  pull_request:
    types: [opened, synchronize, reopened, closed]
  issues:
    types: [opened, edited, labeled]
  issue_comment:
    types: [created, edited]
  push:
    branches: [main, develop, master]
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight
  workflow_dispatch:
    inputs:
      agent_uri:
        description: 'Specific agent to run'
        required: false

jobs:
  run-agents:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Run a5c Agents
        uses: a5c-ai/action@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          config_file: ".a5c/config.yml"
```

> **Note**: This configuration includes all supported trigger types. You can customize it based on your specific needs.

### 4. Add Required Secrets

Add the following secrets to your GitHub repository:

1. Go to your repository's Settings
2. Select "Secrets and variables" → "Actions"
3. Add the following secrets:
   - `ANTHROPIC_API_KEY`: Your Anthropic API key for Claude access
   - Any other API keys needed by your specific agents

## Advanced Setup

### Custom MCP Servers

Model Context Protocol (MCP) servers extend Claude's capabilities, allowing it to interact with external systems and services. a5c includes several built-in MCP servers:

- **filesystem**: For reading and writing files
- **memory**: For maintaining context across interactions
- **time**: For time-related operations
- **search**: For web search capabilities
- **github**: For GitHub API integration

To configure additional custom MCP servers, create a `mcps.json` file in the `.a5c` directory:

```json
{
  "custom-server": {
    "uri": "https://api.example.com/mcp",
    "auth": {
      "type": "bearer",
      "token": "${{ secrets.CUSTOM_SERVER_TOKEN }}"
    }
  }
}
```

These MCP servers can be referenced in your agent configurations to provide specific capabilities to each agent.

### Local Agents

To use local agents, create an `agents` directory in the `.a5c` directory and add your agent markdown files:

```bash
mkdir -p .a5c/agents
# Add your agent.md files to this directory
```

## Available Agents

a5c comes with several pre-configured agents in the registry, each with specific capabilities:

- **@developer-agent**: General-purpose development assistant for code implementation and problem-solving
- **@code-review-agent**: Specialized in analyzing and reviewing code quality, security, and best practices
- **@project-seeder-agent**: Sets up new projects with appropriate structure and initial configuration
- **@security-scanner**: Identifies security vulnerabilities and provides remediation advice
- **@documentation-agent**: Creates and updates documentation based on code and specifications

These agents can be activated by mentioning them in issues, pull requests, or commit messages.

## Verification

To verify your installation:

1. Push your changes to GitHub
2. Create a new issue with the text "@developer-agent hello"
3. The agent should respond to your mention

## Troubleshooting

If agents aren't responding:

1. Check the GitHub Actions logs for error messages
2. Verify that your API keys are correctly set up
3. Ensure your configuration file is properly formatted
4. Check that the agents you're trying to use are available in the repository you're referencing

For more help, see the [a5c Registry Repository](https://github.com/a5c-ai/registry) or [open an issue](https://github.com/a5c-ai/registry/issues/new) in the a5c registry repository.