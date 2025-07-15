# Using MCP Servers

This guide explains how to configure and use Model Context Protocol (MCP) servers in your A5C projects. MCP servers extend agent capabilities by providing access to external systems, APIs, and resources.

## What Are MCP Servers?

MCP (Model Context Protocol) servers act as bridges between A5C agents and external systems. They provide:

1. **Extended Capabilities**: Access to external APIs, databases, and services
2. **Tool Integration**: Specialized tools for specific tasks
3. **Shared Resources**: Common utilities across agents
4. **Persistent State**: Storage for long-running operations
5. **Security Controls**: Managed access to sensitive systems

## Built-in MCP Servers

A5C includes several built-in MCP servers:

### GitHub MCP Server

Provides access to GitHub APIs and repository operations.

### Filesystem MCP Server

Enables file operations in the repository.

### Memory MCP Server

Offers persistent storage for agent state and shared data.

## Configuring MCP Servers

Configure MCP servers in your `.a5c/config.yml` file:

```yaml
# A5C Configuration File
version: 1.0.0

# MCP Server Configuration
mcp_servers:
  github:
    enabled: true
    auth:
      type: "token"
      token: "${{ secrets.GITHUB_TOKEN }}"
  
  filesystem:
    enabled: true
    read_only: false
    allowed_paths:
      - "src/"
      - "docs/"
    restricted_paths:
      - ".github/workflows/"
  
  memory:
    enabled: true
    storage: "local"
    retention_days: 30
  
  custom_servers:
    config_path: ".a5c/mcps.json"
```

## GitHub MCP Server

The GitHub MCP server provides access to GitHub APIs and repository operations.

### Configuration

```yaml
mcp_servers:
  github:
    enabled: true
    auth:
      type: "token"
      token: "${{ secrets.GITHUB_TOKEN }}"
    rate_limit:
      max_requests: 5000
      per_hour: true
```

### Capabilities

The GitHub MCP server provides these operations:

#### Repository Operations

```markdown
# Read repository files
github.getFileContents(owner, repo, path, [ref])

# Get repository information
github.getRepository(owner, repo)

# List repository contents
github.listContents(owner, repo, path, [ref])
```

#### Issue Operations

```markdown
# Create an issue
github.createIssue(owner, repo, title, body, [labels], [assignees])

# Get issue details
github.getIssue(owner, repo, issue_number)

# List repository issues
github.listIssues(owner, repo, [state], [labels])

# Add issue comment
github.addIssueComment(owner, repo, issue_number, body)

# Update issue
github.updateIssue(owner, repo, issue_number, [title], [body], [state], [labels])
```

#### Pull Request Operations

```markdown
# Create a pull request
github.createPullRequest(owner, repo, title, body, head, base, [draft])

# Get pull request details
github.getPullRequest(owner, repo, pull_number)

# List pull requests
github.listPullRequests(owner, repo, [state], [base])

# Merge pull request
github.mergePullRequest(owner, repo, pull_number, [merge_method])

# Add pull request review
github.createPullRequestReview(owner, repo, pull_number, body, event)
```

#### Commit Operations

```markdown
# Get commit details
github.getCommit(owner, repo, ref)

# List commits
github.listCommits(owner, repo, [sha], [path])

# Compare commits
github.compareCommits(owner, repo, base, head)
```

### Usage Example

```markdown
To create an issue for a bug:

```javascript
const response = await github.createIssue(
  "a5c-ai",
  "docs",
  "Bug: Navigation breaks on mobile",
  "The navigation menu doesn't display correctly on mobile devices.",
  ["bug", "mobile"]
);

console.log(`Created issue #${response.number}`);
```
```

## Filesystem MCP Server

The Filesystem MCP server provides access to repository files.

### Configuration

```yaml
mcp_servers:
  filesystem:
    enabled: true
    read_only: false  # Set to true to prevent modifications
    allowed_paths:
      - "src/"
      - "docs/"
    restricted_paths:
      - ".github/workflows/"
      - "config/secrets/"
    max_file_size: 10485760  # 10MB in bytes
```

### Capabilities

The Filesystem MCP server provides these operations:

#### File Operations

```markdown
# Read file contents
filesystem.readFile(path)

# Write file contents
filesystem.writeFile(path, content)

# Check if file exists
filesystem.fileExists(path)

# Delete file
filesystem.deleteFile(path)

# Get file metadata
filesystem.getFileMetadata(path)
```

#### Directory Operations

```markdown
# List directory contents
filesystem.listDirectory(path)

# Create directory
filesystem.createDirectory(path)

# Check if directory exists
filesystem.directoryExists(path)
```

#### Search Operations

```markdown
# Find files by pattern
filesystem.findFiles(pattern)

# Search file contents
filesystem.searchFiles(pattern, content_pattern)
```

### Usage Example

```markdown
To read and update a configuration file:

```javascript
// Read the current configuration
const config = await filesystem.readFile("config/app.json");
const configObj = JSON.parse(config);

// Update the configuration
configObj.version = "1.2.0";
configObj.features.darkMode = true;

// Write the updated configuration
await filesystem.writeFile(
  "config/app.json",
  JSON.stringify(configObj, null, 2)
);
```
```

## Memory MCP Server

The Memory MCP server provides persistent storage for agent state.

### Configuration

```yaml
mcp_servers:
  memory:
    enabled: true
    storage: "local"  # Options: local, redis, s3
    retention_days: 30
    
    # For Redis storage
    redis:
      url: "${{ secrets.REDIS_URL }}"
    
    # For S3 storage
    s3:
      bucket: "a5c-memory"
      region: "us-west-2"
      prefix: "agent-memory/"
```

### Capabilities

The Memory MCP server provides these operations:

#### Data Operations

```markdown
# Store data with a key
memory.set(key, value)

# Retrieve data by key
memory.get(key)

# Check if key exists
memory.has(key)

# Delete data by key
memory.delete(key)

# List all keys
memory.listKeys([prefix])
```

#### Namespace Operations

```markdown
# Store data in a namespace
memory.setInNamespace(namespace, key, value)

# Retrieve data from a namespace
memory.getFromNamespace(namespace, key)

# List keys in a namespace
memory.listKeysInNamespace(namespace)

# Clear a namespace
memory.clearNamespace(namespace)
```

### Usage Example

```markdown
To store analysis results for future reference:

```javascript
// Store analysis results
await memory.set(
  "security-analysis-123",
  {
    vulnerabilities: [
      { file: "src/auth.js", line: 42, severity: "high", description: "Insecure password handling" },
      { file: "src/api.js", line: 17, severity: "medium", description: "Missing input validation" }
    ],
    scanDate: new Date().toISOString(),
    score: 72
  }
);

// Later, retrieve the results
const analysis = await memory.get("security-analysis-123");
console.log(`Found ${analysis.vulnerabilities.length} vulnerabilities`);
```
```

## Custom MCP Servers

You can extend A5C with custom MCP servers for specialized integrations.

### Configuration

First, reference custom servers in your `.a5c/config.yml`:

```yaml
mcp_servers:
  custom_servers:
    config_path: ".a5c/mcps.json"
```

Then, define the custom servers in `.a5c/mcps.json`:

```json
{
  "jira-server": {
    "uri": "https://api.example.com/jira-mcp",
    "auth": {
      "type": "bearer",
      "token": "${{ secrets.JIRA_TOKEN }}"
    },
    "config": {
      "project_key": "PROJ",
      "default_assignee": "username"
    }
  },
  "slack-server": {
    "uri": "https://api.example.com/slack-mcp",
    "auth": {
      "type": "bearer",
      "token": "${{ secrets.SLACK_TOKEN }}"
    },
    "config": {
      "default_channel": "dev-notifications"
    }
  }
}
```

### Using Custom MCP Servers

Include usage instructions in your agent definitions:

```markdown
# Development Agent

You are a Development Agent with access to these MCP capabilities:

## Jira MCP
Use this to interact with Jira:
- Create issue: `jira.createIssue(summary, description, type)`
- Update issue: `jira.updateIssue(key, fields)`
- Get issue: `jira.getIssue(key)`

## Slack MCP
Use this to send Slack notifications:
- Send message: `slack.sendMessage(channel, message)`
- Post file: `slack.postFile(channel, file, comment)`
```

### Custom MCP Server Implementation

To implement a custom MCP server:

1. Create an API endpoint that follows the MCP protocol
2. Implement the required operations
3. Handle authentication and security
4. Return results in the expected format

For detailed implementation guidelines, see [Implementing Custom MCP Servers](../tutorials/implementing-custom-mcp-servers.md).

## MCP Server Security

Secure your MCP servers with these best practices:

### Authentication

Use secure authentication methods:

```yaml
mcp_servers:
  github:
    auth:
      type: "token"
      token: "${{ secrets.GITHUB_TOKEN }}"
  
  custom_api:
    auth:
      type: "bearer"
      token: "${{ secrets.API_TOKEN }}"
  
  database:
    auth:
      type: "basic"
      username: "${{ secrets.DB_USERNAME }}"
      password: "${{ secrets.DB_PASSWORD }}"
```

### Access Control

Limit access to sensitive resources:

```yaml
mcp_servers:
  filesystem:
    allowed_paths:
      - "src/"
      - "docs/"
    restricted_paths:
      - ".github/workflows/"
      - "config/secrets/"
  
  github:
    allowed_repositories:
      - "a5c-ai/docs"
      - "a5c-ai/registry"
    restricted_operations:
      - "deleteRepository"
      - "updateProtectedBranch"
```

### Secrets Management

Store all sensitive values in GitHub Secrets:

```yaml
mcp_servers:
  api:
    auth:
      type: "bearer"
      token: "${{ secrets.API_TOKEN }}"  # Never hardcode tokens
```

## Monitoring MCP Usage

Monitor your MCP servers to ensure efficient operation:

### Logging

Enable detailed logging for debugging:

```yaml
mcp_servers:
  global_settings:
    logging:
      level: "info"  # Options: debug, info, warn, error
      include_request_body: false
      include_response_body: false
```

### Rate Limiting

Implement rate limits to prevent abuse:

```yaml
mcp_servers:
  github:
    rate_limit:
      max_requests: 5000
      per_hour: true
  
  custom_api:
    rate_limit:
      max_requests: 100
      per_minute: true
```

### Usage Metrics

Track MCP server usage:

```yaml
mcp_servers:
  global_settings:
    metrics:
      enabled: true
      retention_days: 30
      include_agents: true
```

## Troubleshooting MCP Servers

If you encounter issues with MCP servers:

### Connection Issues

If agents can't connect to MCP servers:

1. **Check Configuration**: Verify server URIs and authentication
2. **Check Network**: Ensure GitHub Actions can access the server
3. **Check Logs**: Review action logs for connection errors
4. **Check Rate Limits**: Verify you haven't exceeded rate limits

### Authentication Issues

If authentication fails:

1. **Check Secrets**: Ensure GitHub Secrets are set correctly
2. **Check Token Permissions**: Verify tokens have necessary permissions
3. **Check Token Expiration**: Renew expired tokens
4. **Check Environment**: Ensure secrets are available in the workflow

### Operation Errors

If operations fail:

1. **Check Parameters**: Verify operation parameters are correct
2. **Check Permissions**: Ensure the agent has necessary permissions
3. **Check Input Validation**: Verify inputs meet server requirements
4. **Check Server Logs**: Review server logs for detailed error information

## Best Practices

Follow these best practices when using MCP servers:

1. **Use Built-in Servers**: Prefer built-in MCP servers for common operations
2. **Limit Permissions**: Give MCP servers only the permissions they need
3. **Validate Inputs**: Sanitize all inputs before passing to MCP servers
4. **Handle Errors**: Implement proper error handling for failed operations
5. **Cache Results**: Store frequently used data to minimize MCP requests
6. **Batch Operations**: Combine related operations to reduce round-trips
7. **Document Usage**: Clearly document MCP capabilities in agent instructions
8. **Monitor Performance**: Track MCP server usage and performance

## Next Steps

- Learn about [setting up agents](setting-up-agents.md)
- Understand [configuring triggers](configuring-triggers.md)
- Explore [customizing agent behavior](customizing-agent-behavior.md)
- See how to [implement custom MCP servers](../tutorials/implementing-custom-mcp-servers.md)