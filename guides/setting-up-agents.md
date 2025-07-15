# Setting Up Agents

This guide walks you through the process of setting up and configuring agents in your A5C project. You'll learn how to add agents from the registry, create custom agents, and configure them for your specific needs.

## Prerequisites

Before setting up agents, ensure you have:

1. A GitHub repository with A5C installed
2. Basic understanding of A5C concepts
3. Access to modify GitHub Action workflows
4. GitHub token with appropriate permissions

## Adding Agents from the Registry

The simplest way to add agents is to use the official A5C registry:

### Step 1: Configure Remote Agents

Edit your `.a5c/config.yml` file:

```yaml
# A5C Configuration File
version: 1.0.0

# Agent Configuration
agents:
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/security/*.agent.md"
```

This configuration imports:
- All development agents from the official registry
- All security agents from the official registry

### Step 2: Verify Agent Installation

Run the A5C CLI to verify your agents are installed:

```bash
a5c list agents
```

This will display a list of all available agents:

```
Available Agents:
- development-agent (development)
- code-review-agent (development)
- build-fixer-agent (development)
- security-reviewer (security)
- dependency-checker (security)
...
```

## Creating Custom Agents

For specialized needs, you can create custom agents:

### Step 1: Create Agent Directory

Create a directory for your custom agents:

```bash
mkdir -p .a5c/agents
```

### Step 2: Create Agent Definition File

Create a new file `.a5c/agents/custom-agent.agent.md`:

```markdown
---
name: custom-agent
version: 1.0.0
category: development
description: Custom agent for specialized tasks
model: claude-3-7-sonnet-20250219
triggers:
  events:
    - push
  mentions:
    - "@custom-agent"
  file_patterns:
    - "src/custom/**/*.js"
---

# Custom Agent

You are a specialized agent for the A5C system, designed to handle custom tasks for this project.

## Core Responsibilities

1. **Task 1**: Description of first responsibility
2. **Task 2**: Description of second responsibility
3. **Task 3**: Description of third responsibility

## Analysis Guidelines

When analyzing code or issues:

1. First check...
2. Then examine...
3. Finally verify...

## Action Guidelines

When taking action:

1. Start by...
2. Then proceed to...
3. Finish by...

## Communication Protocol

Communicate using these guidelines:

1. **Report Started**: Signal when you begin analysis
2. **Report Progress**: Update status as you work
3. **Report Completed**: Provide summary of actions taken

## Tools and Integrations

You have access to:

1. **GitHub API**: For repository operations
2. **CLI Tools**: For command-line operations
3. **MCP Servers**: For external integrations
```

### Step 3: Configure Local Agents

Edit your `.a5c/config.yml` to include local agents:

```yaml
# A5C Configuration File
version: 1.0.0

# Agent Configuration
agents:
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
  
  local:
    enabled: true
    path: ".a5c/agents"
    pattern: "*.agent.md"
```

## Configuring Agent Triggers

Configure when and how your agents are activated:

### Event-Based Triggers

Activate agents on specific GitHub events:

```yaml
---
name: build-agent
version: 1.0.0
category: development
triggers:
  events:
    - push:
        branches: ["main", "develop"]
    - pull_request:
        types: ["opened", "synchronize"]
    - workflow_dispatch
---
```

### Mention-Based Triggers

Activate agents when mentioned:

```yaml
---
name: code-review-agent
version: 1.0.0
category: development
triggers:
  mentions:
    - "@code-review-agent"
    - "@code-reviewer"
---
```

### File Pattern Triggers

Activate agents when specific files change:

```yaml
---
name: frontend-agent
version: 1.0.0
category: development
triggers:
  file_patterns:
    - "src/frontend/**/*.js"
    - "src/frontend/**/*.css"
    - "src/frontend/**/*.html"
---
```

### Schedule-Based Triggers

Activate agents on a schedule:

```yaml
---
name: security-scanner
version: 1.0.0
category: security
triggers:
  schedules:
    - cron: "0 0 * * *"  # Daily at midnight
---
```

### Combined Triggers

Use multiple trigger types together:

```yaml
---
name: comprehensive-agent
version: 1.0.0
category: development
triggers:
  events:
    - push:
        branches: ["main"]
  mentions:
    - "@comprehensive-agent"
  file_patterns:
    - "src/core/**/*.js"
  schedules:
    - cron: "0 0 * * 1"  # Weekly on Monday
---
```

## Configuring Agent Behavior

Fine-tune how your agents operate:

### Model Selection

Choose the AI model for your agent:

```yaml
---
name: analysis-agent
version: 1.0.0
category: development
model: claude-3-7-opus-20240229  # High-performance model
---
```

### Execution Parameters

Configure execution parameters:

```yaml
---
name: complex-agent
version: 1.0.0
category: development
max_turns: 30  # Allow more conversation turns
timeout: 300  # Longer timeout (seconds)
---
```

### Tool Access

Control which tools the agent can use:

```yaml
---
name: code-agent
version: 1.0.0
category: development
tools:
  github: true
  filesystem:
    enabled: true
    read_only: false
  cli:
    enabled: true
    allowed_commands: ["git", "npm", "yarn"]
---
```

## Managing Agent Permissions

Configure what agents can access and modify:

### GitHub Permissions

Set GitHub permissions in your workflow file:

```yaml
# .github/workflows/a5c.yml
name: A5C
on:
  push:
  pull_request:
  issues:
  issue_comment:
  workflow_dispatch:

jobs:
  a5c:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      issues: write
      pull-requests: write
      
    steps:
      - uses: actions/checkout@v3
      - uses: a5c-ai/a5c-action@v1
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
```

### File Access Permissions

Restrict which files agents can modify:

```yaml
# .a5c/config.yml
filesystem:
  enabled: true
  read_only: false
  allowed_paths:
    - "src/"
    - "docs/"
  restricted_paths:
    - ".github/workflows/"
    - "config/secrets/"
```

## Troubleshooting Agent Setup

If you encounter issues with your agents:

### Agent Not Triggering

If an agent isn't being triggered:

1. **Check Configuration**: Verify the agent's trigger configuration
2. **Check Permissions**: Ensure the GitHub token has necessary permissions
3. **Check Logs**: Review the GitHub Action logs for errors
4. **Check Patterns**: Verify file patterns match your repository structure

### Agent Errors During Execution

If an agent encounters errors:

1. **Check Prompts**: Review the agent's instructions for clarity
2. **Check Tool Access**: Verify the agent has access to required tools
3. **Check Timeouts**: Increase timeouts for complex operations
4. **Check Model**: Try a different model if the agent struggles with tasks

## Best Practices

Follow these best practices for agent setup:

1. **Start Simple**: Begin with a few well-defined agents
2. **Use Specific Triggers**: Target agents precisely to avoid unnecessary activations
3. **Follow the Principle of Least Privilege**: Give agents only the permissions they need
4. **Document Agent Purposes**: Clearly define each agent's responsibilities
5. **Test in Isolation**: Test each agent individually before enabling multiple agents
6. **Monitor Performance**: Regularly review agent effectiveness and adjust as needed

## Next Steps

- Learn about [configuring triggers](configuring-triggers.md)
- Understand [MCP servers](using-mcp-servers.md)
- Explore [customizing agent behavior](customizing-agent-behavior.md)
- See how to [create custom agents](creating-custom-agents.md)