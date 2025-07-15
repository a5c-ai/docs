# Quick Start

This guide will help you get up and running with A5C in minutes using the zero-to-demo template.

## Using the Zero-to-Demo Template

The fastest way to start with A5C is to use the zero-to-demo template repository.

### 1. Create a New Repository from the Template

1. Go to [a5c-ai/zero-to-demo](https://github.com/a5c-ai/zero-to-demo)
2. Click the "Use this template" button
3. Name your repository and set its visibility
4. Click "Create repository from template"

### 2. Add Required Secrets

Add the following secrets to your new repository:

1. Go to your repository's Settings
2. Select "Secrets and variables" → "Actions"
3. Add the following secrets:
   - `ANTHROPIC_API_KEY`: Your Anthropic API key for Claude access
   - Any other API keys needed by your specific project

### 3. Set Project Requirements

Edit your repository's description to include your project requirements. Be as specific as possible about:

- Project type (web app, mobile app, API, etc.)
- Technologies to use (React, Node.js, etc.)
- Key features and functionality

For example:
> A NextJS web application with Prisma ORM for a task management system. Features include user authentication, task creation with priorities, due dates, and categories, and a dashboard with task statistics.

### 4. Wait for the Project Seeder Agent

The project-seeder-agent will automatically:

1. Analyze your requirements
2. Set up the project structure
3. Install necessary dependencies
4. Configure appropriate A5C agents
5. Create GitHub issues for the development tasks

This typically takes a few minutes to complete.

### 5. Start Development

Once the project-seeder-agent has finished, you can:

1. Clone the repository to your local machine
2. Follow the setup instructions in the README.md
3. Start working on the issues created by the agent

## Manual Setup

If you prefer to add A5C to an existing project:

### 1. Create the Basic Configuration

Create a `.a5c/config.yml` file in your repository:

```yaml
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

agents:
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
```

### 2. Set Up GitHub Action

Create a `.github/workflows/a5c.yml` file:

```yaml
name: A5C Agent System
on:
  pull_request:
    types: [opened, synchronize]
  issues:
    types: [opened, edited]
  issue_comment:
    types: [created]
  push:
    branches: [main, develop]

jobs:
  run-agents:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Run A5C Agents
        uses: a5c-ai/action@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          config_file: ".a5c/config.yml"
```

### 3. Add Repository Secrets

Add your `ANTHROPIC_API_KEY` to your repository's secrets.

### 4. Test the Setup

Create a new issue with "@developer-agent Hello world" to test if your setup is working correctly.

## Next Steps

Now that you have A5C set up, you can:

- Learn about [different agent types](../concepts/agents.md)
- Understand [how to configure triggers](../concepts/triggers.md)
- See how to [customize agent behavior](../guides/customizing-agent-behavior.md)
- Follow our [first project tutorial](first-project.md) for a guided experience