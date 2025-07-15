# MCP (Model Context Protocol)

MCP (Model Context Protocol) is a key component of A5C that enables agents to interact with external services, tools, and resources. This page explains what MCP is, how it works, and how to use it in your A5C projects.

## What is MCP?

MCP is a standardized protocol that allows AI agents to:

1. **Access External Data**: Retrieve information from APIs, databases, and other sources
2. **Execute Operations**: Perform actions in external systems
3. **Use Specialized Tools**: Leverage purpose-built tools for specific tasks
4. **Share Context**: Exchange information with other agents and services

Think of MCP as the bridge between AI agents and the external world, providing a structured way for agents to interact with various systems and tools.

## How MCP Works

The MCP architecture consists of:

1. **MCP Clients**: Built into A5C agents
2. **MCP Servers**: Services that provide specific capabilities
3. **MCP Protocol**: The standardized communication format

When an agent needs to perform an operation that requires external resources:

1. The agent formulates a request using the MCP protocol
2. The request is sent to the appropriate MCP server
3. The server processes the request and performs the operation
4. The server returns the result to the agent
5. The agent incorporates the result into its reasoning

## Built-in MCP Servers

A5C includes several built-in MCP servers:

### GitHub MCP Server

The GitHub MCP server enables agents to interact with GitHub:

```yaml
mcp_servers:
  github:
    enabled: true
    auth:
      type: "token"
      token: "${{ secrets.GITHUB_TOKEN }}"
```

This server provides capabilities like:

- Reading repository files
- Creating issues and pull requests
- Adding comments to discussions
- Managing repository settings
- Accessing GitHub Actions

### Filesystem MCP Server

The filesystem MCP server provides access to the local filesystem:

```yaml
mcp_servers:
  filesystem:
    enabled: true
    read_only: false  # Set to true to prevent file modifications
    allowed_paths:
      - "src/"
      - "docs/"
    restricted_paths:
      - ".github/workflows/"
```

This server enables:

- Reading file contents
- Writing to files
- Creating directories
- Searching for files by pattern

### Memory MCP Server

The memory MCP server provides persistent storage for agent state:

```yaml
mcp_servers:
  memory:
    enabled: true
    storage: "local"  # Options: local, redis, s3
    retention_days: 30
```

This server allows agents to:

- Store and retrieve information across sessions
- Share data between agents
- Maintain context for long-running operations

## Custom MCP Servers

You can extend A5C with custom MCP servers:

```yaml
mcp_servers:
  custom_servers:
    config_path: ".a5c/mcps.json"
```

In `.a5c/mcps.json`:

```json
{
  "jira-server": {
    "uri": "https://api.example.com/jira-mcp",
    "auth": {
      "type": "bearer",
      "token": "${{ secrets.JIRA_TOKEN }}"
    }
  },
  "database-server": {
    "uri": "https://api.example.com/db-mcp",
    "auth": {
      "type": "basic",
      "username": "${{ secrets.DB_USERNAME }}",
      "password": "${{ secrets.DB_PASSWORD }}"
    }
  }
}
```

## Using MCP in Agent Instructions

You can include MCP usage instructions in your agent's prompt:

```markdown
# Development Agent

You are a Development Agent with access to these MCP capabilities:

## GitHub MCP
Use this to interact with GitHub repositories:
- Read file contents: `github.getFileContents(owner, repo, path)`
- Create issues: `github.createIssue(owner, repo, title, body)`
- Add comments: `github.addComment(owner, repo, issue_number, body)`

## Filesystem MCP
Use this to work with local files:
- Read files: `filesystem.readFile(path)`
- Write files: `filesystem.writeFile(path, content)`
- Search files: `filesystem.findFiles(pattern)`

## Memory MCP
Use this to store and retrieve information:
- Store data: `memory.set(key, value)`
- Retrieve data: `memory.get(key)`
- List stored keys: `memory.listKeys()`
```

## Security Considerations

When using MCP:

1. **Limit Permissions**: Only enable necessary MCP servers
2. **Use Secure Authentication**: Store tokens in repository secrets
3. **Restrict Access**: Use read-only mode when possible
4. **Validate Inputs**: Sanitize inputs to prevent injection attacks
5. **Audit Usage**: Monitor MCP server access and operations

## MCP Protocol Specification

The MCP protocol uses a standard request/response format:

### Request Format

```json
{
  "operation": "readFile",
  "parameters": {
    "path": "src/main.js"
  },
  "metadata": {
    "agent": "development-agent",
    "requestId": "req-12345"
  }
}
```

### Response Format

```json
{
  "status": "success",
  "data": "// File content here",
  "metadata": {
    "contentType": "text/javascript",
    "size": 1024,
    "requestId": "req-12345"
  }
}
```

## Best Practices

When working with MCP:

1. **Use Built-in Servers**: Prefer built-in MCP servers for common operations
2. **Document Server Usage**: Clearly document MCP capabilities in agent instructions
3. **Handle Errors**: Implement proper error handling for MCP operations
4. **Batch Operations**: Combine related operations to reduce round-trips
5. **Cache Results**: Store frequently used data to minimize MCP requests

## Next Steps

- Learn about [agent discovery](agent-discovery.md)
- Understand [CLI integration](cli-integration.md)
- See how to [use MCP servers](../guides/using-mcp-servers.md)
- Explore [implementing custom MCP servers](../tutorials/implementing-custom-mcp-servers.md)