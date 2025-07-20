# Agents

Agents are the core building blocks of a5c. Each agent is a specialized AI assistant with specific capabilities and responsibilities.

## What is an Agent?

An a5c agent is:

1. **An AI-powered automation unit** with specific capabilities and responsibilities
2. **Triggered by specific events** like GitHub events, mentions, schedules, or labels
3. **Defined in `.agent.md` files** with YAML frontmatter and prompt instructions
4. **Executed through a CLI tool** like Claude, Aider, or Cursor

## Agent Structure

An agent definition consists of:

### 1. YAML Frontmatter

The YAML frontmatter defines the agent's metadata, configuration, and trigger conditions:

```yaml
---
# Agent Metadata
name: developer-agent
version: 1.0.0
category: development
description: General-purpose development agent for code generation and implementation

# Usage Context
usage_context: |
  Use this agent for general development tasks like implementing features,
  fixing bugs, and answering code-related questions.

# Invocation Context
invocation_context: |
  Mention this agent when you need help with code implementation or have
  technical questions about your codebase.

# Execution Configuration
model: claude-3-7-sonnet-20250219
max_turns: 30
timeout: 30
verbose: false

# Trigger Configuration
events: ["pull_request", "push", "issues"]
mentions: "@developer-agent,@dev"
labels: "enhancement,bug,feature"
branches: "main,develop,feature/*"
paths: "src/**/*.js,src/**/*.ts"
activation_cron: "0 9 * * 1-5"

# Priority (higher runs first)
priority: 70

# MCP Server Configuration
mcp_servers: ["filesystem", "github", "memory"]

# Agent Discovery
agent_discovery:
  enabled: true
  include_same_directory: true
  max_agents_in_context: 8
---
```

### 2. Prompt Instructions

The prompt section provides detailed instructions for the agent, including:

- Role and responsibilities
- Task execution approach
- Response formatting
- Special considerations
- Examples

For example:

```markdown
# Developer Agent

You are a Developer Agent, part of the a5c agent system. Your primary role is to assist with code development tasks including implementation, debugging, and code improvement.

## Core Responsibilities

1. **Code Implementation**: Write high-quality code based on requirements
2. **Bug Fixing**: Identify and fix issues in existing code
3. **Code Review**: Provide feedback on code quality and suggest improvements
4. **Technical Guidance**: Answer questions about implementation approaches

## Response Guidelines

Always follow these guidelines when responding:

1. **Read the repository thoroughly** before making recommendations
2. **Follow existing code patterns** and maintain stylistic consistency
3. **Provide complete solutions** with all necessary implementation details
4. **Explain your reasoning** when making significant decisions
5. **Consider edge cases** and include error handling
```

## Agent Categories

a5c organizes agents into different categories based on their primary function:

### Development Agents

Focused on code and development tasks:

- **developer-agent**: General development assistance
- **project-seeder-agent**: Bootstraps new projects
- **validator-agent**: Code quality and validation
- **build-fixer-agent**: Resolves build issues

### Communication Agents

Handle various communication tasks:

- **discord-manager-agent**: Discord integration
- **slack-manager-agent**: Slack integration
- **content-writer-agent**: Content creation

### Media Agents

Create and manage different media types:

- **video-generation-agent**: Video content
- **image-generation-agent**: Image creation
- **music-generation-agent**: Music composition
- **speech-generation-agent**: Audio generation

### News Agents

Process and deliver news information:

- **news-aggregator-agent**: News collection
- **project-news-analyzer-agent**: Project-specific news

### Research Agents

Conduct research on various topics:

- **researcher-base-agent**: Base research capabilities

## Agent Inheritance

a5c supports agent inheritance, allowing you to extend base agents with specialized functionality:

```yaml
---
name: security-reviewer
from: base-reviewer  # Inherits from base-reviewer
category: security
priority: 80
---

{{base-prompt}}

Additional security-specific instructions...
```

The `{{base-prompt}}` placeholder will be replaced with the prompt from the parent agent.

## Using Agents

There are several ways to use agents in your project:

### 1. Direct Mentions

Mention an agent directly in GitHub issues, pull requests, or comments:

```
@developer-agent Please implement a login page using NextAuth.js
```

### 2. Event-Based Triggers

Configure agents to respond to specific GitHub events:

```yaml
events: ["pull_request.opened", "issues.labeled"]
```

### 3. Label-Based Triggers

Activate agents by applying specific labels:

```yaml
labels: "bug,enhancement,question"
```

### 4. Schedule-Based Triggers

Run agents on a schedule using cron expressions:

```yaml
activation_cron: "0 9 * * 1-5"  # Weekdays at 9 AM
```

### 5. Branch-Based Triggers

Trigger agents based on branch name patterns:

```yaml
branches: "feature/*,hotfix/*"
```

### 6. File Path-Based Triggers

Activate agents when specific files are modified:

```yaml
paths: "src/**/*.js,src/**/*.ts"
```

## Creating Custom Agents

To create a custom agent:

1. Create a `.agent.md` file in your `.a5c/agents` directory
2. Define the YAML frontmatter with agent configuration
3. Write the prompt instructions for the agent
4. Add the agent to your `.a5c/config.yml` file

For a detailed guide on creating custom agents, see the [a5c Registry Repository](https://github.com/a5c-ai/registry) for examples.

## Best Practices

When working with agents:

- **Use specific agents** for specific tasks
- **Provide clear instructions** when mentioning agents
- **Include relevant context** to help agents understand the task
- **Review agent responses** before implementing their suggestions
- **Give feedback** to help agents improve

## Next Steps

- Learn about [agent triggers](triggers.md)
- Understand [agent configuration](configuration.md)
- Explore [MCP integration](mcp.md)
- See [agent discovery](agent-discovery.md) for agent collaboration