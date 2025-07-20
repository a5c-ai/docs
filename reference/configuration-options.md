# Configuration Options

This page provides a comprehensive reference for all configuration options available in a5c. Configuration plays a crucial role in customizing agent behavior, setting up triggers, and defining system integration points.

## Configuration Files

a5c uses the following configuration files:

| File | Purpose | Location |
|------|---------|----------|
| `a5c.yml` | Main configuration file | Repository root |
| `agent-config.yml` | Agent-specific configuration | `.a5c/agents/` directory |
| `triggers.yml` | Trigger definitions | `.a5c/triggers/` directory |
| `mcp-config.yml` | MCP server configuration | `.a5c/mcp/` directory |

## Main Configuration Options (a5c.yml)

The main configuration file controls global settings for your a5c implementation.

### General Settings

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `version` | String | `"1.0"` | a5c configuration version |
| `project_name` | String | Repository name | Name of your project |
| `description` | String | `""` | Short description of your a5c implementation |
| `default_branch` | String | `"main"` | Default branch for a5c operations |
| `log_level` | String | `"info"` | Logging level (`debug`, `info`, `warn`, `error`) |

### Agent Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `agents_directory` | String | `.a5c/agents` | Directory containing agent configurations |
| `default_agent_model` | String | `"gpt-4"` | Default AI model for agents |
| `agent_timeout` | Integer | `300` | Default timeout for agent execution (seconds) |
| `max_tokens` | Integer | `4096` | Maximum token limit for agent responses |
| `temperature` | Float | `0.7` | Default temperature for agent responses |

### Trigger Settings

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `triggers_directory` | String | `.a5c/triggers` | Directory containing trigger definitions |
| `default_trigger_mode` | String | `"auto"` | Default trigger activation mode (`auto`, `manual`) |
| `max_concurrent_triggers` | Integer | `5` | Maximum number of concurrent trigger activations |

### MCP Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `mcp_enabled` | Boolean | `true` | Enable/disable MCP functionality |
| `mcp_directory` | String | `.a5c/mcp` | Directory containing MCP configurations |
| `mcp_server_url` | String | `""` | URL of the MCP server (if using remote server) |
| `mcp_token` | String | `""` | Authentication token for MCP server |
| `mcp_fallback_model` | String | `"gpt-3.5-turbo"` | Fallback model when primary is unavailable |

## Agent Configuration Options (agent-config.yml)

Each agent can have its own configuration file with the following options:

### Basic Agent Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `name` | String | Required | Name of the agent |
| `description` | String | `""` | Description of the agent's purpose |
| `model` | String | From `a5c.yml` | AI model to use for this agent |
| `version` | String | `"1.0"` | Version of this agent |
| `enabled` | Boolean | `true` | Whether this agent is active |
| `category` | String | `"general"` | Category for organizing agents |

### Agent Capabilities

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `capabilities` | Array | `[]` | List of capabilities this agent provides |
| `permissions` | Object | `{}` | Permission scopes for this agent |
| `tools` | Array | `[]` | External tools this agent can use |
| `rate_limit` | Integer | `100` | Maximum calls per hour |
| `memory_enabled` | Boolean | `true` | Whether agent has persistent memory |

### Agent Response Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `temperature` | Float | From `a5c.yml` | Response randomness (0.0-1.0) |
| `max_tokens` | Integer | From `a5c.yml` | Maximum token limit for responses |
| `top_p` | Float | `1.0` | Nucleus sampling parameter |
| `presence_penalty` | Float | `0.0` | Penalty for new topics (-2.0 to 2.0) |
| `frequency_penalty` | Float | `0.0` | Penalty for repetition (-2.0 to 2.0) |

## Trigger Configuration Options (triggers.yml)

Define when and how agents are activated with these options:

### Basic Trigger Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `name` | String | Required | Name of the trigger |
| `description` | String | `""` | Description of the trigger's purpose |
| `enabled` | Boolean | `true` | Whether this trigger is active |
| `agent` | String | Required | Name of the agent to trigger |
| `mode` | String | From `a5c.yml` | Activation mode (`auto`, `manual`) |

### Event-based Triggers

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `events` | Array | `[]` | GitHub events that activate this trigger |
| `conditions` | Object | `{}` | Conditions that must be met to activate |
| `branches` | Array | `[]` | Branch patterns that activate this trigger |
| `paths` | Array | `[]` | File path patterns that activate this trigger |

### Schedule-based Triggers

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `schedule` | String | `""` | Cron expression for scheduled triggers |
| `timezone` | String | `"UTC"` | Timezone for scheduled triggers |
| `max_runs` | Integer | `0` | Maximum number of runs (0 for unlimited) |

### Mention-based Triggers

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `mention_patterns` | Array | `[]` | Patterns that activate when mentioned |
| `mention_locations` | Array | `[]` | Where to detect mentions (`commits`, `issues`, `comments`, `code`) |
| `mention_users` | Array | `[]` | Users whose mentions activate the trigger |

## Environment Variables

a5c also supports configuration through environment variables:

| Environment Variable | Description | Overrides |
|---------------------|-------------|-----------|
| `A5C_PROJECT_NAME` | Project name | `project_name` in a5c.yml |
| `A5C_DEFAULT_BRANCH` | Default branch | `default_branch` in a5c.yml |
| `A5C_LOG_LEVEL` | Logging level | `log_level` in a5c.yml |
| `A5C_AGENT_MODEL` | Default agent model | `default_agent_model` in a5c.yml |
| `A5C_MCP_SERVER_URL` | MCP server URL | `mcp_server_url` in a5c.yml |
| `A5C_MCP_TOKEN` | MCP auth token | `mcp_token` in a5c.yml |
| `A5C_GITHUB_TOKEN` | GitHub authentication token | N/A |

## Configuration Best Practices

- Store sensitive information (tokens, keys) in environment variables, not in configuration files
- Use version control for configuration files to track changes
- Implement the principle of least privilege when configuring agent permissions
- Test configuration changes in a development environment before deploying to production
- Document custom configuration options for your specific implementation

## Related Resources

- [Configuration Guide](/guides/configuration): Step-by-step guide to configuring a5c
- [Agent Setup](/guides/setting-up-agents): How to set up and configure agents
- [Trigger Configuration](/guides/configuring-triggers): Detailed guide for trigger setup
- [MCP Configuration](/guides/using-mcp-servers): How to configure and use MCP servers