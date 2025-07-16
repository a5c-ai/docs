# Implementing Custom MCP Servers

This tutorial guides you through the process of creating custom Model Context Protocol (MCP) servers to extend A5C's capabilities with specialized integrations. Custom MCP servers allow agents to interact with external systems, APIs, and services that aren't covered by the built-in servers.

## Prerequisites

Before implementing custom MCP servers, ensure you have:

- A5C set up in your project (see [installation](../getting-started/installation.md))
- Understanding of [MCP concepts](../concepts/mcp.md)
- Familiarity with TypeScript/JavaScript
- Basic knowledge of API design and implementation
- Clear requirements for the external system integration

## Custom MCP Server Overview

A custom MCP server:

1. Implements the `McpServer` interface
2. Provides a specific set of capabilities
3. Handles requests from agents
4. Translates between agent requests and external system APIs
5. Returns structured responses to agents

MCP servers act as bridges between A5C agents and external systems, allowing agents to access databases, APIs, specialized tools, or custom business logic.

## Step 1: Define Your MCP Server's Purpose

Before coding, clearly define:

1. **Server purpose**: What external system will this server connect to?
2. **Capabilities**: What specific actions should agents be able to perform?
3. **Security considerations**: What authentication and permissions are needed?
4. **Error handling**: How will you handle failures and edge cases?
5. **Performance requirements**: What are the throughput and latency expectations?

### Example MCP Server Concept

For this tutorial, we'll create a "database-mcp-server" that:
- Connects to a PostgreSQL database
- Allows agents to run queries with controlled permissions
- Supports read and write operations with validation
- Provides database schema information to agents
- Implements connection pooling for performance

## Step 2: Set Up Your Development Environment

### Create a Project Structure

```bash
mkdir -p custom-mcp-servers/database-mcp
cd custom-mcp-servers/database-mcp
npm init -y
```

### Install Dependencies

```bash
npm install @a5c/core pg dotenv typescript @types/node @types/pg
npm install --save-dev ts-node nodemon
```

### Configure TypeScript

Create a `tsconfig.json` file:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "outDir": "./dist",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "**/*.test.ts"]
}
```

## Step 3: Implement the MCP Server Interface

### Create the Server Class

Create a file at `src/database-mcp-server.ts`:

```typescript
import { McpServer, McpRequest, McpResponse } from '@a5c/core';
import { Pool, PoolClient } from 'pg';

/**
 * Database MCP Server for PostgreSQL
 * Provides a secure interface for agents to interact with a PostgreSQL database
 */
export class DatabaseMcpServer implements McpServer {
  name = 'database';
  version = '1.0.0';
  capabilities = ['query', 'execute', 'schema', 'tableInfo'];
  
  private pool: Pool | null = null;
  private config: any;
  private allowedOperations: string[] = [];
  
  /**
   * Initialize the database connection pool
   */
  async initialize(config: any): Promise<void> {
    this.config = config;
    this.allowedOperations = config.allowed_operations || ['query', 'schema', 'tableInfo'];
    
    this.pool = new Pool({
      host: config.host || 'localhost',
      port: config.port || 5432,
      database: config.database,
      user: config.user,
      password: config.password,
      max: config.max_connections || 10,
      idleTimeoutMillis: config.idle_timeout || 30000
    });
    
    // Test the connection
    try {
      const client = await this.pool.connect();
      client.release();
      console.log(`Database MCP Server connected to ${config.database}`);
    } catch (error) {
      console.error('Failed to connect to database:', error);
      throw error;
    }
  }
  
  /**
   * Handle MCP requests from agents
   */
  async handleRequest(request: McpRequest): Promise<McpResponse> {
    // Validate the request action is allowed
    if (!this.allowedOperations.includes(request.action)) {
      return {
        status: 'error',
        error: `Operation '${request.action}' is not allowed`,
        data: null
      };
    }
    
    // Handle different action types
    switch (request.action) {
      case 'query':
        return await this.handleQuery(request.params);
      case 'execute':
        return await this.handleExecute(request.params);
      case 'schema':
        return await this.handleSchema(request.params);
      case 'tableInfo':
        return await this.handleTableInfo(request.params);
      default:
        return {
          status: 'error',
          error: `Unsupported action: ${request.action}`,
          data: null
        };
    }
  }
  
  /**
   * Close the database connection pool
   */
  async shutdown(): Promise<void> {
    if (this.pool) {
      await this.pool.end();
      console.log('Database MCP Server disconnected');
    }
  }
  
  /**
   * Handle read-only queries
   */
  private async handleQuery(params: any): Promise<McpResponse> {
    // Validate required parameters
    if (!params.query) {
      return {
        status: 'error',
        error: 'Query parameter is required',
        data: null
      };
    }
    
    // Safety check for read-only queries
    const queryLower = params.query.toLowerCase().trim();
    if (!this.isReadOnlyQuery(queryLower)) {
      return {
        status: 'error',
        error: 'Only SELECT queries are allowed for query action',
        data: null
      };
    }
    
    // Execute the query
    try {
      const result = await this.executeQuery(params.query, params.params || []);
      return {
        status: 'success',
        data: result,
        metadata: {
          rowCount: result.rowCount,
          executionTime: result.executionTime
        }
      };
    } catch (error: any) {
      return {
        status: 'error',
        error: error.message,
        data: null
      };
    }
  }
  
  /**
   * Handle data modification queries (INSERT, UPDATE, DELETE)
   */
  private async handleExecute(params: any): Promise<McpResponse> {
    // Validate required parameters
    if (!params.query) {
      return {
        status: 'error',
        error: 'Query parameter is required',
        data: null
      };
    }
    
    // Safety check to prevent schema modifications
    const queryLower = params.query.toLowerCase().trim();
    if (this.containsSchemaModification(queryLower)) {
      return {
        status: 'error',
        error: 'Schema modification queries are not allowed',
        data: null
      };
    }
    
    // Execute the query
    try {
      const result = await this.executeQuery(params.query, params.params || []);
      return {
        status: 'success',
        data: {
          rowCount: result.rowCount,
          command: result.command
        },
        metadata: {
          executionTime: result.executionTime
        }
      };
    } catch (error: any) {
      return {
        status: 'error',
        error: error.message,
        data: null
      };
    }
  }
  
  /**
   * Get database schema information
   */
  private async handleSchema(params: any): Promise<McpResponse> {
    try {
      // Query to get all tables and their schemas
      const query = `
        SELECT 
          table_schema,
          table_name,
          table_type
        FROM 
          information_schema.tables
        WHERE 
          table_schema NOT IN ('pg_catalog', 'information_schema')
        ORDER BY 
          table_schema, table_name
      `;
      
      const result = await this.executeQuery(query);
      return {
        status: 'success',
        data: result.rows,
        metadata: {
          rowCount: result.rowCount
        }
      };
    } catch (error: any) {
      return {
        status: 'error',
        error: error.message,
        data: null
      };
    }
  }
  
  /**
   * Get detailed information about a specific table
   */
  private async handleTableInfo(params: any): Promise<McpResponse> {
    // Validate required parameters
    if (!params.table) {
      return {
        status: 'error',
        error: 'Table parameter is required',
        data: null
      };
    }
    
    try {
      // Query to get column information for the specified table
      const query = `
        SELECT 
          column_name,
          data_type,
          is_nullable,
          column_default
        FROM 
          information_schema.columns
        WHERE 
          table_name = $1
          AND table_schema NOT IN ('pg_catalog', 'information_schema')
        ORDER BY 
          ordinal_position
      `;
      
      const result = await this.executeQuery(query, [params.table]);
      return {
        status: 'success',
        data: result.rows,
        metadata: {
          table: params.table,
          columnCount: result.rowCount
        }
      };
    } catch (error: any) {
      return {
        status: 'error',
        error: error.message,
        data: null
      };
    }
  }
  
  /**
   * Execute a database query with timing information
   */
  private async executeQuery(query: string, params: any[] = []): Promise<any> {
    if (!this.pool) {
      throw new Error('Database connection not initialized');
    }
    
    let client: PoolClient | null = null;
    try {
      const startTime = Date.now();
      client = await this.pool.connect();
      const result = await client.query(query, params);
      const executionTime = Date.now() - startTime;
      
      return {
        ...result,
        executionTime
      };
    } finally {
      if (client) {
        client.release();
      }
    }
  }
  
  /**
   * Check if a query is read-only (SELECT only)
   */
  private isReadOnlyQuery(query: string): boolean {
    // Simple check for SELECT statements
    // A more robust implementation would use a SQL parser
    return query.startsWith('select');
  }
  
  /**
   * Check if a query contains schema modifications
   */
  private containsSchemaModification(query: string): boolean {
    // Check for schema modification statements
    const schemaKeywords = [
      'create table', 'alter table', 'drop table',
      'create index', 'drop index',
      'create database', 'drop database',
      'truncate table'
    ];
    
    return schemaKeywords.some(keyword => query.includes(keyword));
  }
}
```

### Create the Entry Point

Create a file at `src/index.ts`:

```typescript
import { McpRegistry } from '@a5c/core';
import { DatabaseMcpServer } from './database-mcp-server';

// Export the server class
export { DatabaseMcpServer };

// Register the server when this module is imported
McpRegistry.register(new DatabaseMcpServer());
```

## Step 4: Build and Package Your MCP Server

### Add Build Scripts

Update `package.json`:

```json
{
  "name": "database-mcp-server",
  "version": "1.0.0",
  "description": "Custom MCP server for PostgreSQL database access",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "scripts": {
    "build": "tsc",
    "dev": "nodemon --exec ts-node src/index.ts",
    "test": "echo \"Error: no test specified\" && exit 1",
    "prepare": "npm run build"
  },
  "keywords": ["a5c", "mcp", "database", "postgresql"],
  "author": "Your Name",
  "license": "MIT",
  "dependencies": {
    "@a5c/core": "^1.0.0",
    "pg": "^8.7.3",
    "dotenv": "^16.0.1"
  },
  "devDependencies": {
    "@types/node": "^18.0.0",
    "@types/pg": "^8.6.5",
    "nodemon": "^2.0.19",
    "ts-node": "^10.8.1",
    "typescript": "^4.7.4"
  }
}
```

### Build the Package

```bash
npm run build
```

## Step 5: Test Your MCP Server

### Create a Test Script

Create a file at `src/test.ts`:

```typescript
import { DatabaseMcpServer } from './database-mcp-server';
import dotenv from 'dotenv';

// Load environment variables
dotenv.config();

async function testDatabaseMcp() {
  const server = new DatabaseMcpServer();
  
  // Configure with test settings
  const config = {
    host: process.env.DB_HOST || 'localhost',
    port: parseInt(process.env.DB_PORT || '5432'),
    database: process.env.DB_NAME || 'test',
    user: process.env.DB_USER || 'postgres',
    password: process.env.DB_PASSWORD || 'postgres',
    allowed_operations: ['query', 'schema', 'tableInfo']
  };
  
  try {
    // Initialize the server
    await server.initialize(config);
    console.log('Server initialized successfully');
    
    // Test query action
    const queryResult = await server.handleRequest({
      tool: 'database',
      action: 'query',
      params: {
        query: 'SELECT * FROM users LIMIT 5'
      }
    });
    console.log('Query result:', JSON.stringify(queryResult, null, 2));
    
    // Test schema action
    const schemaResult = await server.handleRequest({
      tool: 'database',
      action: 'schema',
      params: {}
    });
    console.log('Schema result:', JSON.stringify(schemaResult, null, 2));
    
    // Test tableInfo action
    const tableInfoResult = await server.handleRequest({
      tool: 'database',
      action: 'tableInfo',
      params: {
        table: 'users'
      }
    });
    console.log('Table info result:', JSON.stringify(tableInfoResult, null, 2));
    
    // Test invalid action
    const invalidResult = await server.handleRequest({
      tool: 'database',
      action: 'execute',
      params: {
        query: 'INSERT INTO users (name, email) VALUES ($1, $2)',
        params: ['Test User', 'test@example.com']
      }
    });
    console.log('Invalid action result:', JSON.stringify(invalidResult, null, 2));
    
  } catch (error) {
    console.error('Test failed:', error);
  } finally {
    // Shutdown the server
    await server.shutdown();
    console.log('Server shut down');
  }
}

// Run the test
testDatabaseMcp().catch(console.error);
```

### Set Up Environment Variables

Create a `.env` file:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_test_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
```

### Run the Test

```bash
npx ts-node src/test.ts
```

## Step 6: Integrate Your MCP Server with A5C

### Package Your MCP Server

```bash
npm pack
```

This will create a `.tgz` file that you can install in your A5C project.

### Install in Your A5C Project

```bash
cd your-a5c-project
npm install ../path/to/database-mcp-server-1.0.0.tgz
```

### Update A5C Configuration

Add your custom MCP server to `.a5c/config.yml`:

```yaml
# MCP Server Configuration
mcp_servers:
  github:
    enabled: true
  filesystem:
    enabled: true
  memory:
    enabled: true
  database:
    enabled: true
    host: localhost
    port: 5432
    database: your_db_name
    user_env_var: DB_USER
    password_env_var: DB_PASSWORD
    allowed_operations: ["query", "schema", "tableInfo"]
```

### Add Environment Variables

Update your GitHub repository secrets or local environment to include database credentials.

## Step 7: Create an Agent That Uses Your MCP Server

### Create a Database Helper Agent

Create a file at `.a5c/agents/database-helper-agent.agent.md`:

```markdown
---
# Agent Metadata
name: database-helper-agent
version: 1.0.0
category: database
description: Assists with database queries and schema information

# Usage Context
usage_context: |
  Use this agent to help with database queries, data analysis,
  and understanding the database schema.

# Invocation Context
invocation_context: |
  Mention this agent when you need help with database operations,
  data queries, or schema information.

# Execution Configuration
model: claude-3-7-sonnet-20250219
max_turns: 15
timeout: 300
verbose: false

# Trigger Configuration
events: ["issues", "issue_comment"]
mentions: "@database-helper-agent,@db-helper"
labels: "database,query"

# MCP Server Configuration
mcp_servers: ["database", "github", "memory"]
---

# Database Helper Agent

You are a Database Helper Agent, part of the A5C agent system. Your primary role is to assist with database operations, query analysis, and schema exploration.

## Core Responsibilities

1. **Database Queries**: Help write and optimize SQL queries
2. **Schema Analysis**: Provide information about database structure
3. **Data Analysis**: Help analyze and visualize database data
4. **Query Troubleshooting**: Identify and fix issues in SQL queries

## Using the Database MCP

You have access to the Database MCP server, which allows you to:

1. **Run read-only queries**:
```javascript
const result = await mcp.database.query({
  query: "SELECT * FROM users WHERE active = true LIMIT 10"
});
```

2. **Get database schema**:
```javascript
const schema = await mcp.database.schema({});
```

3. **Get table information**:
```javascript
const tableInfo = await mcp.database.tableInfo({
  table: "users"
});
```

## Response Guidelines

When responding to database requests:

1. **Understand the request**: Clarify the data needed or question asked
2. **Explore the schema**: If needed, examine the database structure first
3. **Write clear queries**: Ensure queries are efficient and secure
4. **Explain your approach**: Document why you chose a particular query
5. **Format results clearly**: Present data in an organized, readable format

## Example Workflows

### Schema Exploration

When asked about the database structure:
1. Use `mcp.database.schema()` to get all tables
2. For relevant tables, use `mcp.database.tableInfo()` to get column details
3. Provide an overview of the schema with tables and their relationships
4. Suggest useful queries based on the schema

### Query Assistance

When helping with a query:
1. Understand the data requirements
2. Check the relevant table structure
3. Write an efficient query that meets the requirements
4. Test the query using `mcp.database.query()`
5. Explain the query and its results

## Security and Best Practices

1. **Only use read-only queries** unless explicitly authorized
2. **Never expose sensitive data** like passwords or personal information
3. **Use parameterized queries** to prevent SQL injection
4. **Limit result sets** to avoid performance issues
5. **Document assumptions** made about the database structure

When you are asked to help with database operations, first explore the schema to understand the available tables and their relationships before answering questions or writing queries.
```

## Step 8: Test the Integration

### Create a Test Issue

1. Go to your repository on GitHub
2. Click "Issues" → "New issue"
3. Title: "Test database helper agent"
4. Content:

```
@database-helper-agent

Could you please help me understand our database schema? I'd like to see:

1. A list of all tables in the database
2. Detailed information about the users table
3. A sample query to find active users who registered in the last 30 days

Thank you!
```

5. Click "Submit new issue"

### Review the Agent's Response

The database-helper-agent should:
1. Connect to the database using your custom MCP server
2. Retrieve and present the schema information
3. Show details about the users table
4. Provide a sample query for finding recent active users

## Step 9: Advanced MCP Server Techniques

### Implement Caching

Add caching to improve performance for frequently accessed data:

```typescript
import NodeCache from 'node-cache';

// In your MCP server class
private cache: NodeCache;

constructor() {
  this.name = 'database';
  this.version = '1.0.0';
  this.capabilities = ['query', 'execute', 'schema', 'tableInfo'];
  this.cache = new NodeCache({ stdTTL: 300, checkperiod: 60 }); // 5-minute cache
}

// Add caching to schema and tableInfo methods
private async handleSchema(params: any): Promise<McpResponse> {
  const cacheKey = 'schema';
  const cachedResult = this.cache.get(cacheKey);
  
  if (cachedResult) {
    return {
      status: 'success',
      data: cachedResult,
      metadata: {
        cached: true
      }
    };
  }
  
  // Existing code to fetch schema...
  
  // Cache the result
  this.cache.set(cacheKey, result.rows);
  
  return {
    status: 'success',
    data: result.rows,
    metadata: {
      rowCount: result.rowCount,
      cached: false
    }
  };
}
```

### Implement Query Validation

Add more sophisticated query validation:

```typescript
import { Parser } from 'node-sql-parser';

private sqlParser = new Parser();

private validateQuery(query: string, readOnly: boolean = false): { valid: boolean, reason?: string } {
  try {
    // Parse the SQL query
    const ast = this.sqlParser.astify(query);
    
    // Check query type for read-only validation
    if (readOnly && ast.type !== 'select') {
      return {
        valid: false,
        reason: 'Only SELECT queries are allowed in read-only mode'
      };
    }
    
    // Check for prohibited operations
    if (ast.type === 'drop' || ast.type === 'alter') {
      return {
        valid: false,
        reason: 'DROP and ALTER operations are not allowed'
      };
    }
    
    // More validation logic...
    
    return { valid: true };
  } catch (error) {
    return {
      valid: false,
      reason: 'Invalid SQL syntax'
    };
  }
}
```

### Add Logging and Metrics

Implement detailed logging for auditing and performance monitoring:

```typescript
import winston from 'winston';

private logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  defaultMeta: { service: 'database-mcp' },
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});

private async executeQuery(query: string, params: any[] = []): Promise<any> {
  // Existing code...
  
  // Add logging
  this.logger.info('Executing query', {
    query,
    paramCount: params.length,
    startTime
  });
  
  try {
    const result = await client.query(query, params);
    const executionTime = Date.now() - startTime;
    
    this.logger.info('Query completed', {
      query,
      rowCount: result.rowCount,
      executionTime
    });
    
    return {
      ...result,
      executionTime
    };
  } catch (error) {
    this.logger.error('Query error', {
      query,
      error: error.message,
      stack: error.stack
    });
    throw error;
  }
}
```

## Step 10: Best Practices for MCP Servers

### Security Best Practices

1. **Principle of least privilege**: Only grant the minimum necessary permissions
2. **Input validation**: Validate all input parameters
3. **Query parameterization**: Use parameterized queries to prevent SQL injection
4. **Rate limiting**: Implement rate limiting to prevent abuse
5. **Audit logging**: Log all operations for security review
6. **Credential management**: Never hardcode credentials; use environment variables
7. **Error handling**: Return generic error messages to users

### Performance Best Practices

1. **Connection pooling**: Reuse database connections
2. **Query optimization**: Analyze and optimize query performance
3. **Caching**: Cache frequently accessed data
4. **Result pagination**: Limit large result sets
5. **Asynchronous operations**: Use non-blocking code
6. **Resource cleanup**: Properly release resources like connections
7. **Timeout handling**: Implement timeouts for long-running operations

### Reliability Best Practices

1. **Error recovery**: Implement retry logic for transient failures
2. **Circuit breaking**: Prevent cascading failures
3. **Graceful degradation**: Provide limited functionality when dependencies fail
4. **Health checks**: Implement health check endpoints
5. **Logging**: Maintain comprehensive logs for troubleshooting
6. **Monitoring**: Set up alerts for critical failures
7. **Versioning**: Version your MCP server for compatibility

## Conclusion

You've successfully implemented a custom MCP server that extends A5C's capabilities with database integration. By following this pattern, you can create MCP servers for any external system, API, or service that your agents need to interact with.

Custom MCP servers allow you to:
- Integrate A5C with your existing infrastructure
- Add specialized capabilities to your agents
- Enforce security and access controls
- Optimize performance for specific use cases
- Create a unified interface for agents to access external systems

As you develop more MCP servers, consider creating a registry of servers that can be shared across projects and teams.

## Next Steps

- Learn about [agent discovery](../concepts/agent-discovery.md) for agent collaboration
- Explore [creating custom agents](creating-custom-agents.md) that use your MCP server
- Understand [agent configuration](../concepts/configuration.md) for MCP settings
- Learn how to [build a project from scratch](building-project-from-scratch.md) using your custom MCP servers