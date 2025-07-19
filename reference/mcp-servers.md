# MCP Servers

This page provides comprehensive reference documentation for Model Context Protocol (MCP) servers in A5C. MCP servers manage AI model access, provide shared memory, and enable advanced agent capabilities.

## What are MCP Servers?

Model Context Protocol (MCP) servers act as intermediaries between A5C agents and AI models. They provide:

1. **Centralized Model Access**: Unified interface to AI models (OpenAI, Anthropic, etc.)
2. **Shared Memory**: Persistent storage accessible to all agents
3. **Advanced Capabilities**: Vector embeddings, tool execution, and more
4. **Resource Management**: Token usage tracking and rate limiting
5. **Security Controls**: Authentication and permission management

## Built-in MCP Servers

A5C includes several built-in MCP server implementations for different use cases.

### Standard MCP Server

**Name**: `standard-mcp`  
**Description**: Default MCP server suitable for most projects.

**Features**:
- Multi-model support (OpenAI, Anthropic, etc.)
- Basic shared memory
- Tool invocation
- Token usage tracking

**Configuration**:

```yaml
mcp:
  type: standard-mcp
  models:
    default: gpt-4
    fallback: gpt-3.5-turbo
  memory:
    enabled: true
    ttl: 86400  # 24 hours
  api_keys:
    openai: ${OPENAI_API_KEY}
    anthropic: ${ANTHROPIC_API_KEY}
  max_tokens_per_request: 4096
  request_timeout: 60
```

---

### High-Performance MCP Server

**Name**: `high-performance-mcp`  
**Description**: Optimized for high-throughput environments.

**Features**:
- Request batching and caching
- Load balancing across model providers
- Distributed memory store
- Performance monitoring

**Configuration**:

```yaml
mcp:
  type: high-performance-mcp
  models:
    providers:
      - name: openai
        api_key: ${OPENAI_API_KEY}
        models: [gpt-4, gpt-3.5-turbo]
        weight: 0.7
      - name: anthropic
        api_key: ${ANTHROPIC_API_KEY}
        models: [claude-2, claude-instant]
        weight: 0.3
  cache:
    enabled: true
    ttl: 3600
    max_size: "1GB"
  memory:
    type: redis
    connection_string: ${REDIS_URL}
  performance:
    request_timeout: 30
    max_retries: 3
    circuit_breaker_threshold: 5
```

---

### Enterprise MCP Server

**Name**: `enterprise-mcp`  
**Description**: Enterprise-grade server with advanced security and compliance features.

**Features**:
- Fine-grained access controls
- Audit logging
- Data retention policies
- Compliance controls (GDPR, HIPAA, etc.)
- SSO integration

**Configuration**:

```yaml
mcp:
  type: enterprise-mcp
  security:
    authentication:
      type: jwt
      secret: ${JWT_SECRET}
      issuer: "a5c-enterprise"
    authorization:
      roles:
        - name: admin
          permissions: [read, write, execute]
        - name: developer
          permissions: [read, execute]
        - name: viewer
          permissions: [read]
  compliance:
    data_retention: 90  # days
    pii_detection: true
    audit_logging: true
    audit_log_path: "/var/log/a5c/audit.log"
  models:
    allowed: [gpt-4, claude-2]
    blocked: [gpt-3.5-turbo]
  storage:
    type: encrypted
    key_rotation: 30  # days
```

---

### Edge MCP Server

**Name**: `edge-mcp`  
**Description**: Lightweight server designed for edge deployment.

**Features**:
- Minimal resource requirements
- Offline model support
- Local tool execution
- Synchronization with central MCP

**Configuration**:

```yaml
mcp:
  type: edge-mcp
  offline_mode: true
  local_models:
    - path: "/opt/models/llama-7b"
      name: llama-7b
      type: llama
    - path: "/opt/models/gpt-j-6b"
      name: gpt-j
      type: gpt-j
  sync:
    enabled: true
    central_mcp_url: "https://central-mcp.example.com"
    sync_interval: 3600  # seconds
    sync_on_connection: true
  storage:
    path: "/var/lib/a5c/edge-storage"
    max_size: "10GB"
```

## MCP Server API

All MCP servers implement a standard API for agent interaction:

### API Overview

MCP servers provide a standardized API for agent interactions. This API includes endpoints for:

- Model completions and chat interactions
- Vector embeddings generation
- Memory storage and retrieval
- Tool discovery and execution

### Authentication

MCP servers support various authentication methods based on your deployment configuration. Consult your specific MCP server documentation for authentication requirements.
```

## Custom MCP Servers

You can implement custom MCP servers for specialized needs.

### Implementation Requirements

Custom MCP servers must:

1. Implement the core MCP API endpoints
2. Support standard authentication methods
3. Handle proper error responses
4. Provide logging and monitoring capabilities

### Registration

Register custom MCP servers in your A5C configuration:

```yaml
mcp:
  type: custom
  implementation: "org.example.CustomMCPServer"
  config_path: ".a5c/custom-mcp-config.yml"
```

## Memory Management

MCP servers provide shared memory storage for agents:

### Memory Types

| Type | Description | Best For |
|------|-------------|----------|
| `simple` | Key-value store with TTL | Temporary data sharing |
| `vector` | Vector database for embeddings | Semantic search |
| `structured` | Schema-based data storage | Complex data relationships |
| `file` | File-based storage | Large documents, binaries |

### Memory Operations

MCP servers provide a consistent interface for memory operations including:

- Storing and retrieving key-value data
- Managing time-to-live (TTL) for stored information
- Vector storage for semantic search capabilities
- Structured data management

## Security Best Practices

When configuring MCP servers:

1. **Use Environment Variables**: Never hardcode API keys or secrets
2. **Implement Least Privilege**: Restrict agent permissions to only what's needed
3. **Enable Audit Logging**: Track all operations for security monitoring
4. **Regular Token Rotation**: Rotate API keys and authentication tokens regularly
5. **Network Security**: Use TLS and restrict network access to MCP servers

## Performance Tuning

Optimize MCP server performance with these settings:

| Setting | Description | Recommended Value |
|---------|-------------|-------------------|
| `request_timeout` | Maximum time for model requests | 30-60 seconds |
| `max_tokens_per_request` | Token limit per request | Model-dependent |
| `batch_size` | Number of requests to batch | 10-50 |
| `cache_ttl` | Cache time-to-live | 1-24 hours |
| `max_retries` | Request retry attempts | 3-5 |
| `backoff_factor` | Exponential backoff multiplier | 1.5-2.0 |

## Monitoring and Observability

MCP servers provide monitoring endpoints and metrics:

| Metric | Description |
|--------|-------------|
| `requests_total` | Total number of requests |
| `request_duration_seconds` | Request duration histogram |
| `tokens_used` | Token usage by model and operation |
| `cache_hit_ratio` | Cache hit/miss ratio |
| `error_rate` | Request error rate |
| `memory_usage` | Memory store size and usage |

Access metrics via the `/metrics` endpoint (Prometheus format).

## Related Resources

- [MCP Server Setup Guide](/guides/using-mcp-servers)
- [Custom MCP Implementation](/guides/custom-mcp-servers)
- [MCP API Specification](/architecture/mcp-protocol)
- [Memory Management](/concepts/mcp-memory)
- [MCP Security](/guides/securing-mcp)