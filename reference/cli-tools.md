# CLI Tools

This page provides comprehensive reference documentation for Command Line Interface (CLI) tools supported by A5C (Agent-based Automated Code Collaboration). These tools enable efficient management, configuration, and interaction with A5C components from the terminal.

## Core CLI Commands

A5C provides a primary command-line tool (`a5c`) with various subcommands for different operations.

### Installation

> **Note**: Ensure you have Node.js version 14 or higher installed before installing the A5C CLI tools.

```bash
# Install globally via npm
npm install -g @a5c/cli

# Or use with npx
npx @a5c/cli [command]
```

### Global Options

These options apply to all commands:

| Option | Description |
|--------|-------------|
| `--help, -h` | Display help information |
| `--version, -v` | Display version information |
| `--config, -c` | Specify custom config file path |
| `--verbose` | Enable verbose output |
| `--quiet` | Suppress all output except errors |
| `--json` | Output in JSON format |
| `--no-color` | Disable colored output |

## Command Reference

### Initialize A5C

```bash
a5c init [options]
```

Creates a new A5C configuration in the current directory.

**Options**:

| Option | Description |
|--------|-------------|
| `--template <name>` | Initialize using a template (`basic`, `advanced`, `minimal`) |
| `--force` | Overwrite existing configuration |
| `--interactive` | Use interactive setup mode |
| `--github` | Configure for GitHub integration |
| `--gitlab` | Configure for GitLab integration |

**Examples**:

```bash
# Basic initialization
a5c init

# Advanced interactive setup
a5c init --interactive --github

# Use minimal template
a5c init --template minimal
```

---

### Manage Agents

```bash
a5c agent [command] [options]
```

Commands for managing A5C agents.

**Subcommands**:

| Command | Description |
|---------|-------------|
| `list` | List all available agents |
| `info <agent-name>` | Display detailed agent information |
| `create <agent-name>` | Create a new agent |
| `edit <agent-name>` | Edit an existing agent |
| `enable <agent-name>` | Enable an agent |
| `disable <agent-name>` | Disable an agent |
| `run <agent-name>` | Run an agent manually |

**Options**:

| Option | Description |
|--------|-------------|
| `--category <category>` | Filter agents by category |
| `--format <format>` | Output format (`table`, `json`, `yaml`) |
| `--all` | Show all agents including disabled ones |

**Examples**:

```bash
# List all enabled agents
a5c agent list

# Get detailed info about an agent
a5c agent info code-review-agent

# Create a new agent from a template
a5c agent create my-custom-agent --template code-review

# Run an agent manually
a5c agent run security-scanner --path ./src
```

---

### Manage Triggers

```bash
a5c trigger [command] [options]
```

Commands for managing A5C triggers.

**Subcommands**:

| Command | Description |
|---------|-------------|
| `list` | List all configured triggers |
| `info <trigger-name>` | Display detailed trigger information |
| `create <trigger-name>` | Create a new trigger |
| `edit <trigger-name>` | Edit an existing trigger |
| `enable <trigger-name>` | Enable a trigger |
| `disable <trigger-name>` | Disable a trigger |
| `test <trigger-name>` | Test a trigger with sample event |

**Options**:

| Option | Description |
|--------|-------------|
| `--agent <agent-name>` | Filter triggers by agent |
| `--event <event-type>` | Filter triggers by event type |
| `--format <format>` | Output format (`table`, `json`, `yaml`) |

**Examples**:

```bash
# List all triggers
a5c trigger list

# Get detailed info about a trigger
a5c trigger info pr-review-trigger

# Create a new trigger
a5c trigger create docs-update --agent content-writer --event push --path "docs/**/*"

# Test a trigger
a5c trigger test pr-review-trigger --payload ./test-payload.json
```

---

### MCP Server Management

```bash
a5c mcp [command] [options]
```

Commands for managing MCP servers.

**Subcommands**:

| Command | Description |
|---------|-------------|
| `start` | Start the MCP server |
| `stop` | Stop the MCP server |
| `status` | Check MCP server status |
| `logs` | View MCP server logs |
| `config` | View or update MCP configuration |
| `memory [subcommand]` | Manage MCP memory store |
| `stats` | View MCP usage statistics |

**Options**:

| Option | Description |
|--------|-------------|
| `--port <port>` | Server port (default: 3000) |
| `--host <host>` | Server host (default: localhost) |
| `--detach, -d` | Run in background mode |

**Examples**:

```bash
# Start MCP server
a5c mcp start

# Start server on custom port in background
a5c mcp start --port 3030 --detach

# View server logs
a5c mcp logs --follow

# Get memory item
a5c mcp memory get my-key

# View usage statistics
a5c mcp stats --period 7d
```

---

### Project Management

```bash
a5c project [command] [options]
```

Commands for managing A5C projects.

**Subcommands**:

| Command | Description |
|---------|-------------|
| `info` | Display project information |
| `validate` | Validate project configuration |
| `stats` | Show project statistics |
| `export` | Export project configuration |
| `import` | Import project configuration |
| `upgrade` | Upgrade project to latest A5C version |

**Options**:

| Option | Description |
|--------|-------------|
| `--format <format>` | Output format (`table`, `json`, `yaml`) |
| `--path <path>` | Project path (default: current directory) |

**Examples**:

```bash
# Display project information
a5c project info

# Validate configuration
a5c project validate

# Export project configuration
a5c project export --format yaml > a5c-config.yaml

# Upgrade project
a5c project upgrade --backup
```

## Development Tools

A5C includes development tools for creating and testing custom components.

### Agent Development

```bash
a5c dev agent [command] [options]
```

Tools for agent development.

**Subcommands**:

| Command | Description |
|---------|-------------|
| `scaffold <name>` | Create agent scaffold |
| `test <name>` | Test agent functionality |
| `lint <name>` | Lint agent code and configuration |
| `package <name>` | Package agent for distribution |

**Options**:

| Option | Description |
|--------|-------------|
| `--template <template>` | Scaffold template to use |
| `--output <directory>` | Output directory |
| `--test-case <file>` | Test case file |

**Examples**:

```bash
# Create new agent scaffold
a5c dev agent scaffold my-agent --template python

# Test agent
a5c dev agent test my-agent --test-case ./tests/test-case.json

# Package agent for distribution
a5c dev agent package my-agent --output ./dist
```

---

### MCP Development

```bash
a5c dev mcp [command] [options]
```

Tools for MCP server development.

**Subcommands**:

| Command | Description |
|---------|-------------|
| `scaffold <name>` | Create MCP server scaffold |
| `test <name>` | Test MCP server functionality |
| `mock` | Start mock MCP server for testing |
| `benchmark <name>` | Benchmark MCP server performance |

**Options**:

| Option | Description |
|--------|-------------|
| `--template <template>` | Scaffold template to use |
| `--port <port>` | Port for mock server |
| `--delay <ms>` | Simulate response delay in mock server |

**Examples**:

```bash
# Create new MCP server scaffold
a5c dev mcp scaffold custom-mcp --template node

# Start mock MCP server
a5c dev mcp mock --port 3030

# Benchmark MCP server
a5c dev mcp benchmark my-mcp --requests 1000 --concurrency 10
```

## Integration Tools

A5C provides tools for integration with version control systems and CI/CD platforms.

### GitHub Integration

```bash
a5c github [command] [options]
```

Commands for GitHub integration.

**Subcommands**:

| Command | Description |
|---------|-------------|
| `setup` | Set up GitHub integration |
| `workflow <action>` | Manage GitHub workflows |
| `token` | Manage GitHub tokens |
| `test` | Test GitHub integration |

**Options**:

| Option | Description |
|--------|-------------|
| `--repo <repo>` | GitHub repository (format: owner/repo) |
| `--token <token>` | GitHub token (or use GITHUB_TOKEN env var) |

**Examples**:

```bash
# Set up GitHub integration
a5c github setup

# Add workflow file
a5c github workflow add --template basic

# Test GitHub integration
a5c github test --event pull_request
```

---

### GitLab Integration

```bash
a5c gitlab [command] [options]
```

Commands for GitLab integration.

**Subcommands**:

| Command | Description |
|---------|-------------|
| `setup` | Set up GitLab integration |
| `ci <action>` | Manage GitLab CI configuration |
| `token` | Manage GitLab tokens |
| `test` | Test GitLab integration |

**Options**:

| Option | Description |
|--------|-------------|
| `--project <project>` | GitLab project path |
| `--token <token>` | GitLab token (or use GITLAB_TOKEN env var) |

**Examples**:

```bash
# Set up GitLab integration
a5c gitlab setup

# Add CI configuration
a5c gitlab ci add --template basic

# Test GitLab integration
a5c gitlab test --event merge_request
```

## Configuration Management

Tools for managing A5C configuration.

### Configuration Commands

```bash
a5c config [command] [options]
```

Commands for configuration management.

**Subcommands**:

| Command | Description |
|---------|-------------|
| `get <key>` | Get configuration value |
| `set <key> <value>` | Set configuration value |
| `list` | List all configuration values |
| `edit` | Open configuration in editor |
| `validate` | Validate configuration |
| `reset` | Reset to default configuration |

**Options**:

| Option | Description |
|--------|-------------|
| `--global` | Use global configuration |
| `--format <format>` | Output format (`json`, `yaml`, `table`) |

**Examples**:

```bash
# Get configuration value
a5c config get mcp.port

# Set configuration value
a5c config set agents.default_model gpt-4

# List all configuration
a5c config list --format yaml

# Edit configuration in default editor
a5c config edit
```

## Debugging Tools

A5C includes tools for debugging and troubleshooting.

### Debug Commands

```bash
a5c debug [command] [options]
```

Commands for debugging.

**Subcommands**:

| Command | Description |
|---------|-------------|
| `info` | Show system information |
| `logs` | View and filter logs |
| `event <type>` | Simulate trigger event |
| `trace <id>` | Trace execution of operation |
| `doctor` | Check for common issues |

**Options**:

| Option | Description |
|--------|-------------|
| `--verbose` | Show detailed output |
| `--format <format>` | Output format |
| `--since <time>` | Show logs since timestamp |

**Examples**:

```bash
# Show system information
a5c debug info

# View recent logs
a5c debug logs --since 1h

# Simulate pull request event
a5c debug event pull_request --payload ./test/pr-payload.json

# Run diagnostics
a5c debug doctor
```

## Environment Variables

A5C CLI tools respect the following environment variables:

| Variable | Description |
|----------|-------------|
| `A5C_CONFIG_PATH` | Path to A5C configuration file |
| `A5C_LOG_LEVEL` | Log level (`debug`, `info`, `warn`, `error`) |
| `A5C_MCP_URL` | URL of MCP server |
| `A5C_MCP_TOKEN` | Authentication token for MCP server |
| `GITHUB_TOKEN` | GitHub personal access token |
| `GITLAB_TOKEN` | GitLab personal access token |
| `A5C_NO_COLOR` | Disable colored output if set |
| `A5C_EDITOR` | Editor for interactive commands |

## Related Resources

- [CLI Installation Guide](/getting-started/installation#cli-installation) (Coming soon)
- [CLI Usage Tutorial](/tutorials/cli-basics) (Coming soon)
- [Automating A5C with CLI](/guides/cli-automation) (Coming soon)
- [Custom CLI Plugin Development](/guides/custom-cli-plugins) (Coming soon)