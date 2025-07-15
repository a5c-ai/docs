# Troubleshooting

This guide helps you diagnose and resolve common issues with A5C. It covers problems related to agent execution, GitHub integration, configuration issues, and performance concerns.

## Common Issues and Solutions

### Agent Not Triggering

#### Symptoms
- Agent doesn't respond to events, mentions, or other triggers
- No agent activity appears in GitHub Action logs
- No agent comments or actions are visible

#### Possible Causes and Solutions

##### 1. Incorrect Trigger Configuration

**Problem**: Agent trigger configuration doesn't match the actual events.

**Solution**: Verify your trigger configuration:

```yaml
# Check agent definition frontmatter
---
name: agent-name
triggers:
  events:
    - push:
        branches: ["main", "develop"]
    - pull_request:
        types: ["opened", "synchronize"]
  mentions:
    - "@agent-name"
  file_patterns:
    - "src/**/*.js"
---
```

Ensure branches, file patterns, and event types match your workflow.

##### 2. GitHub Token Permissions

**Problem**: The GitHub token lacks necessary permissions.

**Solution**: Update your workflow file:

```yaml
# .github/workflows/a5c.yml
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

##### 3. Agent Not Enabled

**Problem**: The agent isn't enabled in your configuration.

**Solution**: Check your `.a5c/config.yml`:

```yaml
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

##### 4. Workflow Not Running

**Problem**: The GitHub Action workflow isn't running.

**Solution**: Check your GitHub repository's Actions tab to verify workflow execution. If not running, check:

- Repository permissions for GitHub Actions
- Workflow trigger configuration
- GitHub Actions quota and limits

### Agent Errors During Execution

#### Symptoms
- Agent starts but fails to complete tasks
- Error messages in GitHub Action logs
- Incomplete or missing agent responses

#### Possible Causes and Solutions

##### 1. Model API Issues

**Problem**: Issues with the underlying AI model API.

**Solution**: 
- Check if the model is operational
- Verify API keys and authentication
- Try a different model in your configuration:

```yaml
---
name: agent-name
model: claude-3-7-sonnet-20250219  # Try a different model
---
```

##### 2. Context Size Limitations

**Problem**: Agent input exceeds model context size limits.

**Solution**:
- Reduce input size by focusing on specific files
- Use file patterns to limit scope
- Adjust max tokens parameter:

```yaml
---
name: agent-name
max_tokens_to_sample: 4096
---
```

##### 3. Timeout Issues

**Problem**: Agent execution exceeds timeout limits.

**Solution**: Increase timeout in your configuration:

```yaml
---
name: agent-name
timeout: 300  # Increase timeout (in seconds)
---
```

Or in global settings:

```yaml
settings:
  timeout: 300  # Global timeout for all agents
```

##### 4. Tool Access Problems

**Problem**: Agent lacks access to required tools.

**Solution**: Verify tool configuration:

```yaml
---
name: agent-name
tools:
  github: true
  filesystem: true
  cli:
    enabled: true
    allowed_commands: ["git", "npm"]
---
```

### Configuration Issues

#### Symptoms
- A5C doesn't load agents as expected
- Configuration changes don't take effect
- Error messages about invalid configuration

#### Possible Causes and Solutions

##### 1. YAML Syntax Errors

**Problem**: YAML syntax errors in configuration files.

**Solution**: Validate your YAML with a linter. Common issues include:
- Improper indentation
- Missing quotes around special characters
- Incorrect list formatting

```yaml
# Correct YAML syntax
agents:
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
```

##### 2. Invalid File Paths

**Problem**: Configuration references invalid file paths.

**Solution**: Verify all paths are correct and files exist:

```yaml
local:
  enabled: true
  path: ".a5c/agents"  # Ensure this directory exists
  pattern: "*.agent.md"
```

##### 3. Environment Variable Issues

**Problem**: Environment variables not properly set or referenced.

**Solution**: Check environment variable usage:

```yaml
github:
  auth:
    type: "token"
    token: "${{ secrets.GITHUB_TOKEN }}"  # Ensure this secret exists
```

Use the GitHub repository settings to verify secrets are configured correctly.

##### 4. Configuration Not Committed

**Problem**: Configuration changes aren't committed to the repository.

**Solution**: Ensure your configuration changes are committed and pushed:

```bash
git add .a5c/config.yml
git commit -m "Update A5C configuration"
git push
```

### GitHub Integration Problems

#### Symptoms
- Authentication errors when accessing GitHub
- Permission denied for repository operations
- GitHub API rate limit exceeded

#### Possible Causes and Solutions

##### 1. Token Permission Issues

**Problem**: GitHub token lacks necessary permissions.

**Solution**: Use a token with appropriate permissions:

```yaml
# .github/workflows/a5c.yml
jobs:
  a5c:
    permissions:
      contents: write
      issues: write
      pull-requests: write
```

For organization repositories, ensure the token has organization access.

##### 2. Rate Limit Exceeded

**Problem**: GitHub API rate limit exceeded.

**Solution**: 
- Reduce frequency of GitHub API calls
- Use conditional triggers to limit agent activations
- Configure rate limiting in your configuration:

```yaml
github:
  rate_limit:
    max_requests: 5000
    per_hour: true
```

##### 3. Repository Access Issues

**Problem**: Token can't access private repositories.

**Solution**: For accessing private repositories, use a personal access token (PAT) with appropriate scope:

```yaml
remote:
  sources:
    repositories:
      - uri: "https://github.com/your-org/private-repo"
        pattern: "agents/*.agent.md"
        auth:
          type: "token"
          token: "${{ secrets.PAT_TOKEN }}"
```

### Performance Issues

#### Symptoms
- Slow agent response times
- High resource usage in GitHub Actions
- Timeouts during complex operations

#### Possible Causes and Solutions

##### 1. Large Repository Size

**Problem**: Repository is too large for efficient processing.

**Solution**: 
- Use sparse checkout to reduce checkout size
- Use specific file patterns for agent triggers
- Exclude large directories:

```yaml
triggers:
  file_patterns:
    - "src/**/*.js"
    - "!src/vendor/**"
    - "!node_modules/**"
```

##### 2. Inefficient Agent Instructions

**Problem**: Agent instructions cause inefficient execution.

**Solution**: Optimize agent instructions:
- Focus instructions on specific tasks
- Reduce ambiguity in directions
- Streamline decision processes
- Use clearer examples

##### 3. Too Many Concurrent Agents

**Problem**: Too many agents running simultaneously.

**Solution**: Limit concurrency in your configuration:

```yaml
settings:
  concurrency: 3  # Limit to 3 concurrent agents
```

##### 4. Resource-Intensive Operations

**Problem**: Agents performing resource-intensive operations.

**Solution**: 
- Optimize CLI commands
- Limit scope of file operations
- Use more efficient search patterns
- Break complex tasks into smaller operations

### MCP Server Issues

#### Symptoms
- Errors when accessing MCP servers
- Timeouts during MCP operations
- Missing or incorrect MCP functionality

#### Possible Causes and Solutions

##### 1. Configuration Issues

**Problem**: Incorrect MCP server configuration.

**Solution**: Verify your MCP configuration:

```yaml
mcp_servers:
  github:
    enabled: true
    auth:
      type: "token"
      token: "${{ secrets.GITHUB_TOKEN }}"
  
  filesystem:
    enabled: true
    read_only: false
  
  memory:
    enabled: true
    storage: "local"
```

##### 2. Authentication Problems

**Problem**: MCP server authentication failures.

**Solution**: Check authentication configuration:
- Verify tokens and credentials
- Ensure secrets are properly configured
- Check for token expiration

##### 3. Custom Server Connectivity

**Problem**: Custom MCP servers unreachable.

**Solution**: Verify custom server configuration:

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

Ensure the server is accessible from GitHub Actions and properly configured.

### Agent Instruction Issues

#### Symptoms
- Agent misinterprets instructions
- Inconsistent agent behavior
- Agent actions don't match expectations

#### Possible Causes and Solutions

##### 1. Ambiguous Instructions

**Problem**: Agent instructions are unclear or ambiguous.

**Solution**: Clarify your agent instructions:
- Use concrete examples
- Provide step-by-step procedures
- Specify expected outputs
- Define priorities explicitly

##### 2. Contradictory Guidelines

**Problem**: Instructions contain contradictory guidelines.

**Solution**: Review and reconcile instructions:
- Eliminate contradictions
- Create clear decision hierarchies
- Specify exception handling
- Prioritize guidelines

##### 3. Missing Context

**Problem**: Instructions lack necessary context.

**Solution**: Add context to your instructions:
- Include project background
- Explain domain-specific terminology
- Provide references to conventions
- Show examples from the codebase

## Debugging Techniques

### GitHub Action Logs

Use GitHub Action logs to diagnose issues:

1. Go to your repository's Actions tab
2. Find the relevant workflow run
3. Click on the "a5c" job
4. Examine logs for errors and warnings

Look for:
- Error messages
- Warning signs
- Timeouts
- Rate limit notifications
- Authentication issues

### Agent Diagnostics

Enable diagnostic mode for detailed information:

```yaml
settings:
  verbose: true
  debug: true
  log_level: "debug"
```

This provides additional information about:
- Agent initialization
- Trigger matching
- Context processing
- Tool usage
- API calls

### Testing Isolated Components

Test components in isolation to identify issues:

1. **Test Triggers**: Verify trigger conditions with simple events
2. **Test Configuration**: Validate configuration files separately
3. **Test MCP Servers**: Check MCP server connectivity independently
4. **Test Agent Instructions**: Try agent instructions with controlled inputs

### Common Error Messages

Interpret common error messages:

| Error Message | Possible Cause | Solution |
|---------------|----------------|----------|
| "Token authentication failed" | Invalid or expired GitHub token | Update GitHub token or permissions |
| "Context length exceeded" | Input too large for model | Reduce input size or use a larger model |
| "Rate limit exceeded" | Too many GitHub API calls | Reduce API calls or increase rate limits |
| "Timeout exceeded" | Operation took too long | Increase timeout or optimize operations |
| "File not found" | Referencing non-existent file | Verify file paths and existence |
| "Permission denied" | Insufficient permissions | Update token permissions |
| "Invalid YAML" | YAML syntax errors | Fix YAML syntax issues |

## Advanced Troubleshooting

### Debugging Mode

Enable debugging mode for advanced troubleshooting:

```yaml
# .a5c/config.yml
settings:
  debug:
    enabled: true
    log_level: "trace"
    output_dir: ".a5c/logs"
    include_prompts: true
    include_responses: true
```

This generates detailed logs for in-depth analysis.

### Log Analysis

Analyze logs to identify patterns:

1. Look for recurring errors
2. Identify timing patterns
3. Check for resource constraints
4. Examine API call sequences
5. Review model inputs and outputs

### Custom Diagnostic Agents

Create diagnostic agents for troubleshooting:

```markdown
---
name: diagnostic-agent
version: 1.0.0
category: system
description: Agent for diagnosing A5C issues
---

# Diagnostic Agent

You are a Diagnostic Agent for A5C. Your purpose is to diagnose and report on system issues.

## Core Responsibilities

1. **Configuration Analysis**: Review A5C configuration for issues
2. **Log Analysis**: Examine logs for error patterns
3. **Performance Monitoring**: Identify performance bottlenecks
4. **System Verification**: Test system components
5. **Report Generation**: Create detailed diagnostic reports
```

### Health Checks

Implement regular health checks:

```yaml
# .github/workflows/a5c-health.yml
name: A5C Health Check
on:
  schedule:
    - cron: "0 0 * * *"  # Daily at midnight
  workflow_dispatch:

jobs:
  health-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: a5c-ai/a5c-health@v1
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
```

This runs regular diagnostics to catch issues early.

## Getting Help

If you're still experiencing issues:

1. **Check Documentation**: Review the complete A5C documentation
2. **Search Issues**: Check existing GitHub issues for similar problems
3. **Community Support**: Ask in the A5C community forums
4. **Create Issue**: Open an issue in the A5C repository with:
   - Detailed description of the problem
   - Steps to reproduce
   - Error messages and logs
   - Configuration files (with sensitive data removed)
   - Environment information

## Preventative Measures

Avoid future issues with these practices:

1. **Version Control**: Keep configuration in version control
2. **Gradual Changes**: Make incremental configuration changes
3. **Testing**: Test changes in development environment first
4. **Monitoring**: Implement regular monitoring and alerts
5. **Documentation**: Document your A5C setup and customizations
6. **Updates**: Keep A5C and its components updated
7. **Backups**: Maintain backups of working configurations

## Next Steps

- Learn about [setting up agents](setting-up-agents.md)
- Understand [configuring triggers](configuring-triggers.md)
- Explore [using MCP servers](using-mcp-servers.md)
- See how to [create custom agents](creating-custom-agents.md)