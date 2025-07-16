# GitHub Action

This page provides comprehensive reference documentation for the A5C (Agent-based Automated Code Collaboration) GitHub Action. The action enables seamless integration of A5C with GitHub repositories, workflows, and events.

## Overview

The A5C GitHub Action automates the deployment and execution of A5C agents within GitHub workflows. It handles agent activation, coordination, and reporting based on GitHub events.

## Usage

Add the A5C GitHub Action to your workflow file (`.github/workflows/a5c.yml`):

```yaml
name: A5C

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  issues:
    types: [opened, edited, labeled]
  issue_comment:
    types: [created, edited]

jobs:
  a5c:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
      issues: write
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Run A5C
        uses: a5c-ai/a5c-action@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          openai_api_key: ${{ secrets.OPENAI_API_KEY }}
          config_path: .a5c/config.yml
```

## Inputs

The A5C GitHub Action accepts the following inputs:

### Required Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `github_token` | GitHub token for repository access | N/A |

### API Keys

| Input | Description | Default |
|-------|-------------|---------|
| `openai_api_key` | OpenAI API key | N/A |
| `anthropic_api_key` | Anthropic API key | N/A |
| `huggingface_api_key` | HuggingFace API key | N/A |
| `custom_api_keys` | JSON string of custom API keys | `{}` |

### Configuration

| Input | Description | Default |
|-------|-------------|---------|
| `config_path` | Path to A5C configuration file | `.a5c/config.yml` |
| `agent_config_path` | Path to agent configuration directory | `.a5c/agents` |
| `mcp_config_path` | Path to MCP configuration file | `.a5c/mcp.yml` |
| `triggers_config_path` | Path to triggers configuration file | `.a5c/triggers.yml` |

### Runtime Options

| Input | Description | Default |
|-------|-------------|---------|
| `log_level` | Logging level (`debug`, `info`, `warn`, `error`) | `info` |
| `timeout` | Maximum execution time in seconds | `300` |
| `concurrency` | Maximum concurrent agent executions | `3` |
| `agent_memory` | Enable persistent agent memory | `true` |
| `mcp_server_url` | URL of external MCP server | `""` |

### Agent Selection

| Input | Description | Default |
|-------|-------------|---------|
| `enabled_agents` | Comma-separated list of agents to enable | All agents |
| `disabled_agents` | Comma-separated list of agents to disable | None |
| `agent_categories` | Comma-separated list of agent categories to enable | All categories |

### Event Filtering

| Input | Description | Default |
|-------|-------------|---------|
| `enabled_events` | Comma-separated list of GitHub events to process | All events |
| `disabled_events` | Comma-separated list of GitHub events to ignore | None |
| `path_patterns` | Comma-separated list of file path patterns to monitor | All paths |
| `branch_patterns` | Comma-separated list of branch patterns to monitor | All branches |

## Outputs

The A5C GitHub Action provides the following outputs:

| Output | Description |
|--------|-------------|
| `activated_agents` | JSON array of agents that were activated during execution |
| `created_issues` | JSON array of issues created by agents |
| `created_prs` | JSON array of pull requests created by agents |
| `execution_time` | Total execution time in seconds |
| `token_usage` | Total number of tokens used |
| `error_count` | Number of errors encountered during execution |

Access outputs in subsequent workflow steps:

```yaml
steps:
  - name: Run A5C
    id: a5c
    uses: a5c-ai/a5c-action@v1
    with:
      github_token: ${{ secrets.GITHUB_TOKEN }}

  - name: Use A5C outputs
    run: |
      echo "Activated agents: ${{ steps.a5c.outputs.activated_agents }}"
      echo "Created PRs: ${{ steps.a5c.outputs.created_prs }}"
```

## Advanced Configuration

### Custom MCP Server

Connect to a custom MCP server:

```yaml
- name: Run A5C with custom MCP
  uses: a5c-ai/a5c-action@v1
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    mcp_server_url: "https://mcp.example.com"
    mcp_token: ${{ secrets.MCP_TOKEN }}
```

### Filter by File Paths

Only trigger A5C for specific file changes:

```yaml
- name: Run A5C for specific files
  uses: a5c-ai/a5c-action@v1
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    path_patterns: "src/**/*.js,src/**/*.ts,docs/**/*.md"
```

### Agent-Specific Configuration

Provide custom configuration for specific agents:

```yaml
- name: Run A5C with agent config
  uses: a5c-ai/a5c-action@v1
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    agent_config: |
      {
        "code-review-agent": {
          "max_files": 10,
          "review_level": "detailed"
        },
        "security-scanner-agent": {
          "scan_level": "deep",
          "ignore_patterns": ["vendor/**", "node_modules/**"]
        }
      }
```

### Custom Environments

Run A5C in custom CI environments:

```yaml
- name: Run A5C in custom environment
  uses: a5c-ai/a5c-action@v1
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    environment: "production"
    environment_variables: |
      {
        "NODE_ENV": "production",
        "DATABASE_URL": "${{ secrets.DATABASE_URL }}"
      }
```

## Using with Matrix Strategy

> **Tip**: For complex repositories with different agent needs across multiple parts of the codebase, use GitHub's matrix strategy to run different agent configurations in parallel.

Run A5C for multiple configurations using GitHub's matrix strategy:

```yaml
jobs:
  a5c:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        config: [
          {agent_category: "security", log_level: "debug"},
          {agent_category: "development", log_level: "info"}
        ]
    steps:
      - uses: actions/checkout@v3
      
      - name: Run A5C
        uses: a5c-ai/a5c-action@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          agent_categories: ${{ matrix.config.agent_category }}
          log_level: ${{ matrix.config.log_level }}
```

## Environment Variables

The A5C GitHub Action respects the following environment variables:

| Variable | Description |
|----------|-------------|
| `A5C_CONFIG_PATH` | Path to A5C configuration file |
| `A5C_LOG_LEVEL` | Log level |
| `A5C_OPENAI_API_KEY` | OpenAI API key |
| `A5C_ANTHROPIC_API_KEY` | Anthropic API key |
| `A5C_MCP_URL` | URL of MCP server |
| `A5C_MCP_TOKEN` | Authentication token for MCP server |
| `A5C_GITHUB_TOKEN` | GitHub token (falls back to `GITHUB_TOKEN`) |

Environment variables take precedence over input parameters.

## Permissions

The A5C GitHub Action requires the following permissions:

| Permission | Description |
|------------|-------------|
| `contents: write` | Read and write repository contents |
| `pull-requests: write` | Create and comment on pull requests |
| `issues: write` | Create and comment on issues |

For self-hosted runners, you may need to set additional permissions:

```yaml
jobs:
  a5c:
    runs-on: self-hosted
    permissions:
      contents: write
      pull-requests: write
      issues: write
      id-token: write  # For OIDC authentication
      packages: read   # For package access
```

## Event Support

The A5C GitHub Action supports the following GitHub events:

| Event | Supported | Description |
|-------|-----------|-------------|
| `push` | ✅ | Code pushed to repository |
| `pull_request` | ✅ | Pull request opened, synchronized, etc. |
| `issues` | ✅ | Issue opened, edited, labeled, etc. |
| `issue_comment` | ✅ | Comment added to issue or pull request |
| `pull_request_review` | ✅ | Review submitted on pull request |
| `pull_request_review_comment` | ✅ | Comment added to pull request review |
| `workflow_dispatch` | ✅ | Workflow manually triggered |
| `repository_dispatch` | ✅ | Custom webhook event |
| `schedule` | ✅ | Scheduled execution |
| `release` | ✅ | Release created, edited, published |
| `discussion` | ✅ | GitHub Discussion created or edited |

## Error Handling

The A5C GitHub Action provides detailed error handling and reporting:

1. **Soft Failures**: By default, agent errors don't cause the workflow to fail
2. **Strict Mode**: Enable strict mode to fail the workflow on any agent error
3. **Error Reporting**: Errors are reported as annotations in the GitHub Actions UI
4. **Retry Logic**: Configurable retry mechanism for transient errors

Enable strict mode:

```yaml
- name: Run A5C in strict mode
  uses: a5c-ai/a5c-action@v1
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    strict_mode: true
    max_retries: 3
    retry_delay: 5
```

## Security Considerations

When using the A5C GitHub Action:

1. **API Keys**: Store all API keys as GitHub Secrets
2. **Permissions**: Use the principle of least privilege for tokens
3. **Token Scope**: Limit token scope to required permissions only
4. **Forked Repositories**: Restrict sensitive operations in PRs from forks
5. **Audit Logs**: Monitor GitHub Action usage in organization audit logs

Secure configuration for public repositories:

```yaml
name: A5C

on:
  pull_request:
    branches: [main]

jobs:
  a5c:
    runs-on: ubuntu-latest
    # Only run on PRs from the same repository, not forks
    if: github.event.pull_request.head.repo.full_name == github.repository
    permissions:
      contents: read  # Reduced permissions for security
      pull-requests: write
    steps:
      - uses: actions/checkout@v3
      
      - name: Run A5C
        uses: a5c-ai/a5c-action@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          openai_api_key: ${{ secrets.OPENAI_API_KEY }}
```

## Related Resources

- [GitHub Actions Setup Guide](/getting-started/github-integration) (Coming soon)
- [CI/CD Integration](/guides/cicd-integration) (Coming soon)
- [A5C Security Best Practices](/guides/security-best-practices) (Coming soon)
- [Customizing A5C Workflows](/guides/custom-workflows) (Coming soon)
- [Event-Driven Agent Activation](/concepts/triggers) (Coming soon)