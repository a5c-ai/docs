# MCP (Model Context Protocol)

The Model Context Protocol (MCP) enables A5C agents to interact with external services and tools. This page explains MCP concepts, built-in servers, and integration options.

## What is MCP?

MCP (Model Context Protocol) is:

1. **A standardized interface** for AI models to interact with external systems
2. **A tool-based system** that allows agents to perform specific actions
3. **An extensible framework** for adding custom capabilities to agents
4. **A security boundary** that controls what agents can access and modify

MCP enables agents to:
- Access file systems and code repositories
- Interact with GitHub and other platforms
- Query databases and APIs
- Execute commands with controlled permissions
- Store and retrieve information in memory
- Analyze code, security vulnerabilities, and performance issues

## MCP Architecture

The MCP system consists of:

### 1. MCP Clients

MCP clients are embedded within agents and provide interfaces to access MCP servers. Clients handle:
- Request formatting
- Authentication
- Rate limiting
- Retries
- Response parsing

### 2. MCP Servers

MCP servers provide specific capabilities and respond to agent requests. A5C includes built-in MCP servers for common operations.

### 3. MCP Protocol

The protocol defines the message format and communication patterns between clients and servers:

```
{
  "request": {
    "tool": "filesystem",
    "action": "readFile",
    "params": {
      "path": "src/main.js"
    }
  }
}
```

```
{
  "response": {
    "status": "success",
    "data": "// File content here",
    "metadata": {
      "size": 1024,
      "modified": "2025-01-01T00:00:00Z"
    }
  }
}
```

## Built-in MCP Servers

A5C includes several built-in MCP servers:

### 1. GitHub MCP Server

Provides access to GitHub APIs and repository operations.

**Key capabilities:**
- Repository access (clone, push, pull)
- Issue and PR management
- Comment handling
- Commit operations
- Code search
- Repository statistics

**Example usage:**
```
// Read a file from GitHub
const content = await mcp.github.getFileContent({
  owner: 'a5c-ai',
  repo: 'docs',
  path: 'README.md'
});

// Create a new issue
await mcp.github.createIssue({
  owner: 'a5c-ai',
  repo: 'docs',
  title: 'Update documentation',
  body: 'The installation instructions need updating.'
});
```

### 2. Filesystem MCP Server

Provides access to the local file system with appropriate permissions.

**Key capabilities:**
- File reading and writing
- Directory listing and creation
- File search and pattern matching
- File metadata access
- File watching for changes

**Example usage:**
```
// Read a file
const content = await mcp.filesystem.readFile({
  path: '/path/to/file.txt'
});

// Write a file
await mcp.filesystem.writeFile({
  path: '/path/to/output.txt',
  content: 'New content'
});

// List directory contents
const files = await mcp.filesystem.listDirectory({
  path: '/path/to/directory',
  pattern: '*.js'
});
```

### 3. Memory MCP Server

Provides persistent and shared memory storage for agents.

**Key capabilities:**
- Key-value storage
- Session and persistent memory
- Shared data between agent runs
- Context retention
- Memory search and querying

**Example usage:**
```
// Store a value
await mcp.memory.set({
  key: 'last_execution',
  value: { timestamp: Date.now(), status: 'success' },
  persistent: true
});

// Retrieve a value
const lastExecution = await mcp.memory.get({
  key: 'last_execution'
});

// List all memory keys
const keys = await mcp.memory.keys({
  prefix: 'config_'
});
```

### 4. Security Scanner MCP Server

Analyzes code for security vulnerabilities.

**Key capabilities:**
- Static code analysis
- Dependency scanning
- Secret detection
- License compliance
- SAST (Static Application Security Testing)
- Container scanning

**Example usage:**
```
// Scan a file for vulnerabilities
const results = await mcp.securityScanner.scanFile({
  path: 'src/login.js',
  scanType: 'vulnerability'
});

// Scan dependencies
const dependencies = await mcp.securityScanner.scanDependencies({
  path: 'package.json'
});
```

### 5. Code Analysis MCP Server

Provides code analysis and understanding capabilities.

**Key capabilities:**
- Code parsing and AST generation
- Symbol extraction
- Code quality metrics
- Complexity analysis
- Type inference
- Code structure analysis

**Example usage:**
```
// Analyze code structure
const structure = await mcp.codeAnalysis.analyzeStructure({
  path: 'src/component.js'
});

// Find function definitions
const functions = await mcp.codeAnalysis.findDefinitions({
  pattern: 'login*',
  type: 'function'
});
```

## MCP Configuration

MCP servers are configured in the global config and agent definitions:

### Global Configuration (.a5c/config.yml)

```yaml
# MCP Server Configuration
mcp_servers:
  github:
    enabled: true
    rate_limit: 5000
    token_env_var: GITHUB_TOKEN
  filesystem:
    enabled: true
    root_path: ./
    allowed_operations: ["read", "write", "list"]
  memory:
    enabled: true
    persistence: session
    max_size: 10485760  # 10MB
  security_scanner:
    enabled: true
    scan_timeout: 300  # 5 minutes
  code_analysis:
    enabled: true
    parser_timeout: 60  # 1 minute
```

### Agent-specific Configuration (.agent.md)

```yaml
# MCP Server Configuration in agent definition
mcp_servers: ["filesystem", "github", "memory"]
```

## Custom MCP Servers

You can create custom MCP servers to extend agent capabilities:

### 1. Define the MCP Server Interface

```typescript
// mcp-server.interface.ts
export interface McpServer {
  name: string;
  version: string;
  capabilities: string[];
  
  initialize(config: any): Promise<void>;
  handleRequest(request: McpRequest): Promise<McpResponse>;
  shutdown(): Promise<void>;
}
```

### 2. Implement the Server

```typescript
// custom-database-mcp.ts
import { McpServer, McpRequest, McpResponse } from './mcp-server.interface';

export class CustomDatabaseMcp implements McpServer {
  name = 'database';
  version = '1.0.0';
  capabilities = ['query', 'update', 'schema'];
  
  private connection: any;
  
  async initialize(config: any): Promise<void> {
    this.connection = await createDatabaseConnection(config);
  }
  
  async handleRequest(request: McpRequest): Promise<McpResponse> {
    switch (request.action) {
      case 'query':
        return this.handleQuery(request.params);
      case 'update':
        return this.handleUpdate(request.params);
      case 'schema':
        return this.handleSchema(request.params);
      default:
        throw new Error(`Unsupported action: ${request.action}`);
    }
  }
  
  async shutdown(): Promise<void> {
    await this.connection.close();
  }
  
  // Implementation of specific handlers...
}
```

### 3. Register the Server

```typescript
// mcp-registry.ts
import { McpRegistry } from '@a5c/core';
import { CustomDatabaseMcp } from './custom-database-mcp';

// Register the custom MCP server
McpRegistry.register(new CustomDatabaseMcp());
```

### 4. Configure in A5C

```yaml
# .a5c/config.yml
mcp_servers:
  database:
    enabled: true
    host: localhost
    port: 5432
    database: a5c
    username_env_var: DB_USERNAME
    password_env_var: DB_PASSWORD
```

## MCP Security Model

MCP includes a comprehensive security model:

### 1. Permission System

MCP servers implement a permission system that controls what actions agents can perform:

```yaml
# Permission configuration
permissions:
  filesystem:
    read: ["src/**", "docs/**"]
    write: ["docs/**"]
    deny: ["**/secrets.json", "**/config.prod.js"]
  github:
    issue: ["read", "create"]
    pullRequest: ["read"]
    deny: ["delete", "admin"]
```

### 2. Rate Limiting

MCP servers implement rate limiting to prevent abuse:

```yaml
# Rate limit configuration
rate_limits:
  github: 
    max_requests: 5000
    per_hour: true
  filesystem:
    max_operations: 1000
    per_minute: true
```

### 3. Audit Logging

MCP operations are logged for security auditing:

```yaml
# Audit logging configuration
audit:
  enabled: true
  log_path: ./logs/mcp-audit.log
  detail_level: high  # low, medium, high
  retention_days: 30
```

## MCP Best Practices

When working with MCP:

1. **Limit access to necessary servers**: Only enable the MCP servers an agent actually needs
2. **Use specific permissions**: Restrict access to only the operations and resources required
3. **Handle errors gracefully**: Implement proper error handling for MCP requests
4. **Cache frequently accessed data**: Use the memory MCP server to cache results
5. **Respect rate limits**: Implement backoff strategies for rate-limited services
6. **Secure sensitive data**: Never expose tokens or credentials in MCP requests
7. **Validate input and output**: Always validate data passed to and from MCP servers

## Troubleshooting MCP Issues

Common MCP issues and their solutions:

| Issue | Possible Causes | Solutions |
|-------|-----------------|-----------|
| Connection failures | Network issues, misconfiguration | Check connectivity, verify server configuration |
| Authentication errors | Invalid or expired tokens | Update authentication tokens, check permissions |
| Rate limiting | Too many requests | Implement backoff, cache results, optimize request patterns |
| Timeout errors | Long-running operations | Increase timeout settings, optimize operations |
| Permission denied | Insufficient permissions | Check permission configuration, verify agent roles |

## Next Steps

- Learn about [agent discovery](agent-discovery.md) for agent collaboration
- Explore [CLI integration](cli-integration.md) for command-line tools
- See [implementing custom MCP servers](../tutorials/implementing-custom-mcp-servers.md) for custom integrations
- Understand [agent configuration](configuration.md) for MCP settings