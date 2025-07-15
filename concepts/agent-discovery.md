# Agent Discovery

Agent Discovery is a core feature of A5C that allows agents to find and collaborate with each other. This page explains how agent discovery works and how to use it effectively in your A5C projects.

## What is Agent Discovery?

Agent Discovery is the mechanism through which:

1. **Agents Find Each Other**: Locate other agents in the system
2. **Agents Share Information**: Exchange data and context
3. **Agents Collaborate**: Work together on complex tasks
4. **Agents Delegate Tasks**: Hand off specialized work to other agents

This system enables a network of specialized agents to work together, each handling tasks they're optimized for.

## How Agent Discovery Works

The Agent Discovery system consists of:

1. **Agent Registry**: A catalog of available agents and their capabilities
2. **Discovery Protocol**: The mechanism for finding and communicating with agents
3. **Context Sharing**: Methods for exchanging information between agents

When an agent needs to collaborate with another agent:

1. It queries the Agent Registry to find appropriate agents
2. It initiates communication through the Discovery Protocol
3. It shares necessary context with the selected agent
4. The selected agent performs its task and returns results
5. The original agent incorporates these results into its workflow

## Agent Registry

The Agent Registry maintains information about all available agents:

```yaml
agents:
  # Remote agents from registry
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/security/*.agent.md"
  
  # Local agents
  local:
    enabled: true
    path: ".a5c/agents"
    pattern: "*.agent.md"
```

Each agent entry includes:

- **Name**: Unique identifier for the agent
- **Category**: Classification for organization (e.g., development, security)
- **Description**: Summary of the agent's purpose and capabilities
- **Metadata**: Additional attributes for discovery and filtering
- **Trigger Conditions**: When the agent should be activated

## Discovery Methods

Agents can discover and interact with each other through several methods:

### 1. Mention-Based Discovery

Agents can mention other agents in their outputs:

```markdown
I've identified a security vulnerability in the authentication code. 
@security-reviewer should examine this code for potential exploits.
```

This creates a direct link to the security-reviewer agent.

### 2. Category-Based Discovery

Agents can find others by category:

```markdown
This task requires a security review. I'll find an agent in the "security" category to assist.
```

The system will locate appropriate security agents.

### 3. Capability-Based Discovery

Agents can discover others based on capabilities:

```markdown
This task requires SQL expertise. I'll find an agent with "database" capabilities.
```

The system will match agents with the required skills.

### 4. Context-Based Discovery

The system can automatically suggest relevant agents based on context:

```markdown
/* This code contains sensitive data handling that requires security review */
```

The system might automatically involve security agents.

## Agent Communication

Once agents discover each other, they communicate through:

### 1. Direct Mentions

```markdown
@code-review-agent I've implemented the authentication feature. Please review for security issues.
```

### 2. GitHub Comments

Agents can communicate via GitHub issue and PR comments:

```markdown
**Review Request**
I'm requesting a code review from @code-review-agent for this pull request.
```

### 3. Commit Messages

Agents can include mentions in commit messages:

```
feat: Implement user authentication

Implemented JWT-based authentication system with refresh tokens.
@security-reviewer please check this implementation.
```

### 4. Code Comments

Agents can leave comments in code for other agents:

```javascript
// @security-reviewer: This password hashing function needs review
function hashPassword(password) {
  // Implementation details
}
```

## Context Sharing

When agents collaborate, they share context through:

### 1. Direct Content

Agents can include relevant information directly:

```markdown
@database-agent I need help optimizing this query:

```sql
SELECT * FROM users 
WHERE last_login > DATE_SUB(NOW(), INTERVAL 7 DAY)
AND status = 'active'
```

Please suggest improvements for performance.
```

### 2. File References

Agents can refer to specific files:

```markdown
@security-reviewer Please review src/auth/login.js for security vulnerabilities.
```

### 3. Diff References

Agents can reference specific changes:

```markdown
@code-review-agent Please review the changes to the authentication flow in PR #123.
```

### 4. Shared Memory

Agents can use the Memory MCP server to share persistent context:

```markdown
I've stored the security analysis results in the Memory MCP with key "security-analysis-123".
@fix-security-issues can retrieve this data to implement the necessary fixes.
```

## Agent Discovery Configuration

Configure agent discovery in your `.a5c/config.yml`:

```yaml
# Agent Discovery Configuration
discovery:
  enabled: true
  
  # Discovery methods
  methods:
    mention: true
    category: true
    capability: true
    context: true
  
  # Communication channels
  channels:
    github_comments: true
    commit_messages: true
    code_comments: true
  
  # Context sharing
  context_sharing:
    max_size: 10240  # Maximum context size in bytes
    include_files: true
    include_diffs: true
    use_memory_mcp: true
```

## Best Practices

When using Agent Discovery:

1. **Be Specific**: Clearly state which agent you need and why
2. **Provide Context**: Include all necessary information for the task
3. **Set Expectations**: Clearly define what you need from the other agent
4. **Follow Up**: Check if the requested agent completed the task
5. **Document Interactions**: Keep track of agent collaborations

## Common Agent Interactions

Here are common patterns for agent collaboration:

### Development → Security Review

```markdown
@security-reviewer I've implemented a new authentication system in src/auth/*.
Please review for security vulnerabilities, focusing on:
1. Password handling
2. Session management
3. CSRF protection
```

### Bug Fix → Testing

```markdown
@test-agent I've fixed the login issue in PR #123.
Please verify that:
1. Login works with valid credentials
2. Invalid logins are properly rejected
3. Password reset flow functions correctly
```

### Code Generation → Code Review

```markdown
@code-review-agent I've generated the API endpoints for user management.
Please review the code in src/api/users/*.
Focus on:
1. RESTful design principles
2. Error handling
3. Performance considerations
```

## Next Steps

- Learn about [MCP integration](mcp.md)
- Understand [CLI integration](cli-integration.md)
- Explore [configuring triggers](../guides/configuring-triggers.md)
- See how to [create custom agents](../guides/creating-custom-agents.md)