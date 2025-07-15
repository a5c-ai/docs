# Configuration

This page explains how to configure A5C for your project using the `.a5c/config.yml` file and related configuration files.

## Configuration File Structure

The main configuration file for A5C is `.a5c/config.yml`. This file defines:

- Global settings
- Agent configuration
- MCP server configuration
- Execution settings

Here's a complete example of a configuration file:

```yaml
# A5C Configuration File
version: 1.0.0

# Global Settings
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false
  max_turns: 20
  timeout: 60
  concurrency: 3
  global_branch_pattern: "main,develop,feature/*"

# Agent Configuration
agents:
  # Remote agents from registry
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/security/*.agent.md"
          auth:
            type: "token"
            token: "${{ secrets.GH_TOKEN }}"
  
  # Local agents
  local:
    enabled: true
    path: ".a5c/agents"
    pattern: "*.agent.md"
  
  # Exclude specific agents
  exclude:
    - "unused-agent-1"
    - "unused-agent-2"

# MCP Server Configuration
mcp_servers:
  github:
    enabled: true
  filesystem:
    enabled: true
  memory:
    enabled: true
  custom_servers:
    config_path: ".a5c/mcps.json"

# History Management
history:
  enabled: true
  storage: "local"  # Options: local, redis, s3
  retention_days: 30
```

## Global Settings

The `settings` section defines global parameters for all agents:

```yaml
settings:
  # Default model to use for agents
  model: claude-3-7-sonnet-20250219
  
  # Detailed logs for debugging
  verbose: false
  
  # Maximum conversation turns per agent
  max_turns: 20
  
  # Timeout in seconds for agent execution
  timeout: 60
  
  # Maximum number of agents to run concurrently
  concurrency: 3
  
  # Global branch pattern for all agents
  global_branch_pattern: "main,develop,feature/*"
```

## Agent Configuration

The `agents` section defines which agents are available:

### Remote Agents

Remote agents are loaded from external repositories:

```yaml
agents:
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
          ref: "main"  # Optional: specific branch or tag
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/security/*.agent.md"
          auth:
            type: "token"
            token: "${{ secrets.GH_TOKEN }}"
```

### Local Agents

Local agents are stored in your repository:

```yaml
agents:
  local:
    enabled: true
    path: ".a5c/agents"
    pattern: "*.agent.md"
```

### Excluding Agents

You can exclude specific agents:

```yaml
agents:
  exclude:
    - "unused-agent-1"
    - "unused-agent-2"
```

## MCP Server Configuration

MCP (Model Control Protocol) servers provide additional capabilities to agents:

```yaml
mcp_servers:
  github:
    enabled: true
  filesystem:
    enabled: true
  memory:
    enabled: true
  custom_servers:
    config_path: ".a5c/mcps.json"
```

For custom MCP servers, create a `.a5c/mcps.json` file:

```json
{
  "custom-server": {
    "uri": "https://api.example.com/mcp",
    "auth": {
      "type": "bearer",
      "token": "${{ secrets.CUSTOM_SERVER_TOKEN }}"
    }
  },
  "another-server": {
    "uri": "https://another-api.example.com/mcp",
    "auth": {
      "type": "basic",
      "username": "${{ secrets.USERNAME }}",
      "password": "${{ secrets.PASSWORD }}"
    }
  }
}
```

## History Management

The `history` section configures conversation history storage:

```yaml
history:
  enabled: true
  storage: "local"  # Options: local, redis, s3
  retention_days: 30
  
  # For Redis storage
  redis:
    url: "${{ secrets.REDIS_URL }}"
  
  # For S3 storage
  s3:
    bucket: "a5c-history"
    region: "us-west-2"
    prefix: "conversations/"
```

## Environment Variables

A5C supports configuration through environment variables:

- `A5C_CONFIG_PATH`: Path to the configuration file (default: `.a5c/config.yml`)
- `A5C_MODEL`: Override the default model
- `A5C_VERBOSE`: Enable verbose logging (`true` or `false`)
- `A5C_MAX_TURNS`: Maximum conversation turns
- `A5C_TIMEOUT`: Execution timeout in seconds
- `A5C_CONCURRENCY`: Maximum concurrent agent executions

Environment variables take precedence over values in the configuration file.

## Advanced Configuration

### Agent-Specific Settings

You can specify agent-specific settings in the agent's YAML frontmatter:

```yaml
---
name: security-reviewer
version: 1.0.0
category: security
description: Security code review agent
model: claude-3-7-opus-20240229  # Agent-specific model
max_turns: 30  # Agent-specific turns
timeout: 120  # Agent-specific timeout
---
```

Agent-specific settings override global settings.

### Multiple Agent Sources

You can combine agents from multiple sources:

```yaml
agents:
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
        - uri: "https://github.com/your-org/your-registry"
          pattern: "custom-agents/*.agent.md"
  local:
    enabled: true
    path: ".a5c/agents"
```

### Authentication for Private Repositories

For private repositories, add authentication:

```yaml
agents:
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/your-org/private-registry"
          pattern: "agents/*.agent.md"
          auth:
            type: "token"
            token: "${{ secrets.GH_TOKEN }}"
```

## Best Practices

When configuring A5C:

1. **Start Simple**: Begin with the basic configuration and expand as needed
2. **Use Remote Agents**: Leverage the official registry for well-tested agents
3. **Customize Gradually**: Add custom agents as you become familiar with the system
4. **Secure Tokens**: Always use repository secrets for sensitive values
5. **Test Changes**: Test configuration changes in a development environment first
6. **Version Control**: Include A5C configuration in version control
7. **Documentation**: Comment your configuration for clarity

## Next Steps

- Learn about [agent discovery](agent-discovery.md)
- Understand [MCP integration](mcp.md)
- Explore [CLI integration](cli-integration.md)
- See how to [customize agent behavior](../guides/customizing-agent-behavior.md)