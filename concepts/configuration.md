# Configuration

A5C uses a flexible, hierarchical configuration system that allows for both global and agent-specific settings. This page explains the configuration options and how they affect agent behavior.

## Configuration Hierarchy

A5C configuration follows a hierarchical structure with multiple levels:

1. **Default settings**: Built-in defaults that apply when no other configuration is specified
2. **Global configuration**: Settings that apply to all agents in the system
3. **Category configuration**: Settings that apply to all agents in a specific category
4. **Agent-specific configuration**: Settings that apply only to individual agents

Each level overrides the settings from the previous level, allowing for both broad defaults and specific customizations.

## Configuration Files

A5C uses several configuration files:

### 1. Global Configuration (.a5c/config.yml)

The main configuration file located at `.a5c/config.yml` defines global settings:

```yaml
# A5C Global Configuration
version: 1.0.0

# System Settings
system:
  log_level: info
  execution_mode: parallel
  max_concurrent_agents: 5
  timeout: 60  # Global timeout in seconds
  retry_attempts: 3
  allowed_models:
    - claude-3-7-sonnet-20250219
    - claude-3-5-sonnet-20240620
    - claude-3-opus-20240229

# Default Agent Settings
defaults:
  model: claude-3-7-sonnet-20250219
  max_turns: 20
  verbose: false
  mcp_servers:
    - github
    - filesystem
  priority: 50


# MCP Server Configuration
mcp_servers:
  github:
    enabled: true
    rate_limit: 5000
  filesystem:
    enabled: true
    root_path: ./
  memory:
    enabled: true
    persistence: session

# Agent Discovery Settings
agent_discovery:
  enabled: true
  discovery_depth: 2
  max_agents_in_context: 5

# Category-specific Settings
categories:
  development:
    priority: 70
    model: claude-3-7-sonnet-20250219
  security:
    priority: 80
    mcp_servers:
      - github
      - security_scanner
  communication:
    priority: 60
    model: claude-3-5-sonnet-20240620
```

### 2. Agent Configuration (.agent.md)

Individual agent configuration is defined in the YAML frontmatter of `.agent.md` files:

```yaml
---
# Agent Metadata
name: code-reviewer
version: 1.0.0
category: development
description: Reviews code for quality, security, and best practices

# Execution Configuration (overrides category and global defaults)
model: claude-3-7-sonnet-20250219
max_turns: 30
timeout: 45
verbose: true

# Trigger Configuration
events: ["pull_request.opened", "pull_request.synchronize"]
mentions: "@code-reviewer,@review"
labels: "needs-review"
branches: "main,develop,feature/*"
paths: "src/**/*.js,src/**/*.ts,src/**/*.py"
activation_cron: "0 9 * * 1-5"

# Priority
priority: 75

# MCP Server Configuration
mcp_servers: ["filesystem", "github", "security_scanner"]

# Agent Discovery
agent_discovery:
  enabled: true
  include_same_directory: true
  max_agents_in_context: 3
---
```

### 3. Environment Variables

Environment variables can override configuration settings, which is useful for CI/CD environments:

```
A5C_LOG_LEVEL=debug
A5C_MAX_CONCURRENT_AGENTS=10
A5C_DEFAULT_MODEL=claude-3-7-sonnet-20250219
A5C_GITHUB_TOKEN=ghp_123456789abcdef
```

## Configuration Options

### System Settings

| Option | Description | Default |
|--------|-------------|---------|
| `system.log_level` | Logging verbosity (debug, info, warn, error) | `info` |
| `system.execution_mode` | How agents are executed (parallel, sequential) | `parallel` |
| `system.max_concurrent_agents` | Maximum number of agents running simultaneously | `5` |
| `system.timeout` | Global timeout in seconds | `60` |
| `system.retry_attempts` | Number of retry attempts for failed operations | `3` |
| `system.allowed_models` | List of allowed AI models | *varies* |

### Agent Settings

| Option | Description | Default |
|--------|-------------|---------|
| `model` | AI model to use for the agent | `claude-3-7-sonnet-20250219` |
| `max_turns` | Maximum conversation turns allowed | `20` |
| `timeout` | Agent-specific timeout in seconds | `60` |
| `verbose` | Enable detailed logging | `false` |
| `priority` | Execution priority (0-100, higher runs first) | `50` |

### Trigger Settings

| Option | Description | Default |
|--------|-------------|---------|
| `events` | GitHub events that trigger the agent | `[]` |
| `mentions` | Agent mentions that trigger activation | `[]` |
| `labels` | Issue/PR labels that trigger the agent | `[]` |
| `branches` | Branch patterns that trigger the agent | `[]` |
| `paths` | File patterns that trigger the agent | `[]` |
| `activation_cron` | Schedule for timed activation | `null` |

### MCP Server Settings

| Option | Description | Default |
|--------|-------------|---------|
| `mcp_servers` | List of MCP servers available to the agent | `["github", "filesystem"]` |
| `mcp_servers.*.enabled` | Whether a specific MCP server is enabled | `true` |
| `mcp_servers.*.rate_limit` | Rate limit for API calls | *varies* |

### Agent Discovery Settings

| Option | Description | Default |
|--------|-------------|---------|
| `agent_discovery.enabled` | Enable agent discovery | `true` |
| `agent_discovery.discovery_depth` | How many levels to search for agents | `2` |
| `agent_discovery.max_agents_in_context` | Maximum agents to include in context | `5` |
| `agent_discovery.include_same_directory` | Include agents from the same directory | `true` |

## Configuration Best Practices

When configuring A5C:

1. **Use the hierarchy effectively**
   - Set common defaults at the global level
   - Use category settings for shared behavior
   - Only override at the agent level when necessary

2. **Optimize for performance**
   - Set appropriate timeouts and retry attempts
   - Limit concurrent agents based on available resources
   - Choose models appropriate for the task complexity

3. **Set precise triggers**
   - Avoid overly broad triggers that activate agents unnecessarily
   - Combine trigger types for more specific activation conditions
   - Use path patterns to limit scope to relevant files

4. **Secure your configuration**
   - Use environment variables for sensitive information
   - Restrict access to configuration files
   - Regularly audit and update allowed models and MCP servers

5. **Document your configuration**
   - Add comments to explain non-obvious settings
   - Document overrides and their purpose
   - Keep a change log of major configuration changes

## Dynamic Configuration

A5C supports dynamic configuration that can change based on runtime conditions:

### Context-based Configuration

```yaml
# Dynamic configuration based on context
context_rules:
  - condition: "event.type == 'pull_request' && event.action == 'opened'"
    settings:
      max_turns: 40
      priority: 90
  - condition: "repository.language == 'python'"
    settings:
      paths: ["**/*.py", "requirements.txt"]
```

### Feature Flags

```yaml
# Feature flags for experimental features
features:
  enhanced_code_review: true
  security_scanning: false
  performance_profiling: true
```

## Migrating Configuration

When upgrading A5C, configuration migration may be necessary:

1. Check the migration guide for your target version
2. Back up your existing configuration files
3. Use the `a5c config migrate` command to automatically update your configuration
4. Review the changes and adjust as needed
5. Test with a limited set of agents before full deployment

## Next Steps

- Learn about [Model Context Protocol](mcp.md)
- Understand [agent discovery](agent-discovery.md)
- Explore [CLI integration](cli-integration.md)
- See the [A5C Registry Repository](https://github.com/a5c-ai/registry) for agent configuration examples
