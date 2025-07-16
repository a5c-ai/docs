# A5C Configuration Patterns

This document provides real-world examples of common A5C configuration patterns to help you effectively set up your agents and workflows.

## Basic Repository Setup

This example shows a minimal A5C setup for a typical development repository:

```yaml
# .a5c/config.yml
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

agents:
  local:
    enabled: true
    paths:
      - ".a5c/agents/*.agent.md"
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
```

```yaml
# .github/workflows/a5c.yml
name: A5C
on:
  pull_request:
    types: [opened, synchronize]
  issues:
    types: [opened, edited]
  issue_comment:
    types: [created]
  push:
    branches: [main, develop]

jobs:
  a5c:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Run A5C Agents
        uses: a5c-ai/action@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          config_file: ".a5c/config.yml"
```

## Web Application Development Team

This example configuration is optimized for a web development team working on a React/Node.js application:

```yaml
# .a5c/config.yml
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

system:
  log_level: info
  execution_mode: parallel
  max_concurrent_agents: 5
  timeout: 60
  retry_attempts: 3

defaults:
  mcp_servers:
    - github
    - filesystem
    - npm

# MCP Server Configuration
mcp_servers:
  github:
    enabled: true
    rate_limit: 5000
  filesystem:
    enabled: true
    root_path: ./
  npm:
    enabled: true
    registry: https://registry.npmjs.org
  jest:
    enabled: true
    config_path: ./jest.config.js

# Agent types specific to web development
agents:
  local:
    enabled: true
    paths:
      - ".a5c/agents/*.agent.md"
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/frontend/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/backend/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/testing/*.agent.md"
```

## Microservice Architecture Project

For a project with multiple microservices, you might use a configuration like this:

```yaml
# .a5c/config.yml
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

system:
  log_level: info
  execution_mode: parallel
  max_concurrent_agents: 8
  timeout: 120

# Service-specific configurations
categories:
  api_gateway:
    priority: 80
    paths: ["services/api-gateway/**/*"]
    mcp_servers: ["github", "filesystem", "docker", "kubernetes"]
  
  auth_service:
    priority: 85
    paths: ["services/auth-service/**/*"]
    mcp_servers: ["github", "filesystem", "docker", "database"]
  
  user_service:
    priority: 70
    paths: ["services/user-service/**/*"]
    mcp_servers: ["github", "filesystem", "docker", "database"]
  
  notification_service:
    priority: 65
    paths: ["services/notification-service/**/*"]
    mcp_servers: ["github", "filesystem", "docker", "messaging"]

# MCP Server Configuration
mcp_servers:
  github:
    enabled: true
  filesystem:
    enabled: true
  docker:
    enabled: true
    image_registry: "gcr.io/my-project"
  kubernetes:
    enabled: true
    context: "dev-cluster"
  database:
    enabled: true
    type: "postgres"
  messaging:
    enabled: true
    type: "kafka"

agents:
  local:
    enabled: true
    paths:
      - ".a5c/agents/*.agent.md"
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/microservices/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/devops/*.agent.md"
```

## Machine Learning Project

For a machine learning project, you might use this configuration:

```yaml
# .a5c/config.yml
version: 1.0.0
settings:
  model: claude-3-opus-20240229  # Using a more powerful model for ML tasks
  verbose: true

system:
  log_level: debug
  execution_mode: parallel
  max_concurrent_agents: 3
  timeout: 300  # Longer timeout for complex ML tasks

# ML-specific configurations
categories:
  data_preprocessing:
    priority: 85
    paths: ["data/**/*", "preprocessing/**/*"]
    mcp_servers: ["github", "filesystem", "data_warehouse"]
  
  model_training:
    priority: 90
    paths: ["models/**/*", "training/**/*"]
    mcp_servers: ["github", "filesystem", "ml_platform", "experiment_tracker"]
  
  evaluation:
    priority: 80
    paths: ["evaluation/**/*"]
    mcp_servers: ["github", "filesystem", "ml_platform", "experiment_tracker"]
  
  deployment:
    priority: 75
    paths: ["deployment/**/*", "api/**/*"]
    mcp_servers: ["github", "filesystem", "docker", "kubernetes", "model_registry"]

# MCP Server Configuration
mcp_servers:
  github:
    enabled: true
  filesystem:
    enabled: true
  data_warehouse:
    enabled: true
    type: "snowflake"
  ml_platform:
    enabled: true
    type: "sagemaker"
  experiment_tracker:
    enabled: true
    type: "mlflow"
  model_registry:
    enabled: true
    type: "mlflow"
  docker:
    enabled: true
  kubernetes:
    enabled: true

agents:
  local:
    enabled: true
    paths:
      - ".a5c/agents/*.agent.md"
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/machine-learning/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/data-science/*.agent.md"
```

## Open Source Project

For an open source project with community contributions:

```yaml
# .a5c/config.yml
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

system:
  log_level: info
  execution_mode: parallel
  max_concurrent_agents: 5

# Configure for community contributions
defaults:
  mcp_servers:
    - github
    - filesystem
  agent_discovery:
    enabled: true
    max_agents_in_context: 8

# Trigger configurations focused on PRs and issues
trigger_defaults:
  events: ["pull_request.opened", "pull_request.synchronize", "issues.opened", "issue_comment.created"]
  branches: ["main", "develop", "feature/*"]

# Community-focused agent categories
categories:
  triage:
    priority: 90
    description: "Agents that handle initial issue and PR triage"
  
  review:
    priority: 80
    description: "Agents that review community contributions"
  
  documentation:
    priority: 70
    description: "Agents that help with documentation tasks"
  
  community:
    priority: 60
    description: "Agents that handle community interactions"

mcp_servers:
  github:
    enabled: true
    rate_limit: 5000
  filesystem:
    enabled: true
  
agents:
  local:
    enabled: true
    paths:
      - ".a5c/agents/*.agent.md"
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/community/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/opensource/*.agent.md"
```

## GitHub Actions Optimization

If you want to optimize your GitHub Actions workflow for faster agent execution:

```yaml
# .github/workflows/a5c.yml
name: A5C
on:
  pull_request:
    types: [opened, synchronize]
  issues:
    types: [opened, edited]
  issue_comment:
    types: [created]
  push:
    branches: [main, develop]

jobs:
  # Fast pre-check to determine if any agents need to run
  check-triggers:
    runs-on: ubuntu-latest
    outputs:
      should_run: ${{ steps.check.outputs.should_run }}
      triggered_agents: ${{ steps.check.outputs.triggered_agents }}
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Check for triggered agents
        id: check
        uses: a5c-ai/trigger-check@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          config_file: ".a5c/config.yml"
  
  # Only run agents if triggers are detected
  run-agents:
    needs: check-triggers
    if: needs.check-triggers.outputs.should_run == 'true'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Cache dependencies
        uses: actions/cache@v3
        with:
          path: ~/.cache/a5c
          key: a5c-${{ hashFiles('.a5c/config.yml') }}
      
      - name: Run A5C Agents
        uses: a5c-ai/action@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          config_file: ".a5c/config.yml"
          triggered_agents: ${{ needs.check-triggers.outputs.triggered_agents }}
```

## Environment-Specific Configuration

For projects with different environments (development, staging, production):

```yaml
# .a5c/config.yml
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

# Base configuration for all environments
defaults:
  mcp_servers:
    - github
    - filesystem

# Environment-specific configurations
environments:
  development:
    system:
      log_level: debug
      execution_mode: parallel
      max_concurrent_agents: 8
    mcp_servers:
      database:
        connection_string: "postgres://user:pass@dev-db:5432/myapp"
      kubernetes:
        context: "dev-cluster"
  
  staging:
    system:
      log_level: info
      execution_mode: parallel
      max_concurrent_agents: 5
    mcp_servers:
      database:
        connection_string: "postgres://user:pass@staging-db:5432/myapp"
      kubernetes:
        context: "staging-cluster"
  
  production:
    system:
      log_level: warn
      execution_mode: sequential
      max_concurrent_agents: 3
    mcp_servers:
      database:
        connection_string: "postgres://user:pass@prod-db:5432/myapp"
      kubernetes:
        context: "production-cluster"

# Use environment-specific configuration based on branch
context_rules:
  - condition: "branch == 'main'"
    environment: "production"
  - condition: "branch == 'staging'"
    environment: "staging"
  - condition: "branch.startsWith('feature/') || branch == 'develop'"
    environment: "development"
```

## Dynamic Context-Based Configuration

For projects that need different behavior based on context:

```yaml
# .a5c/config.yml
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

# Dynamic configuration based on context
context_rules:
  # New pull requests get more attention
  - condition: "event.type == 'pull_request' && event.action == 'opened'"
    settings:
      max_turns: 40
      priority: 90
      enabled_agents: ["code-reviewer", "security-scanner", "documentation-checker"]
  
  # Issues with bug label get priority
  - condition: "event.type == 'issues' && event.labels.includes('bug')"
    settings:
      max_turns: 35
      priority: 85
      enabled_agents: ["bug-analyzer", "reproducer", "triage-agent"]
  
  # Different behavior for different file types
  - condition: "event.changed_files.some(file => file.endsWith('.py'))"
    settings:
      enabled_agents: ["python-linter", "python-test-writer"]
  
  - condition: "event.changed_files.some(file => file.endsWith('.js') || file.endsWith('.ts'))"
    settings:
      enabled_agents: ["js-linter", "typescript-validator", "frontend-test-writer"]
  
  - condition: "event.changed_files.some(file => file.includes('Dockerfile') || file.includes('docker-compose.yml'))"
    settings:
      enabled_agents: ["dockerfile-linter", "security-scanner"]
  
  # Handle documentation changes
  - condition: "event.changed_files.some(file => file.endsWith('.md') || file.endsWith('.rst'))"
    settings:
      enabled_agents: ["documentation-checker", "link-validator", "spelling-grammar"]
```

## Feature Flag Configuration

Using feature flags to gradually roll out new agent capabilities:

```yaml
# .a5c/config.yml
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

# Feature flags for experimental features
features:
  enhanced_code_review: true
  security_scanning: true
  performance_profiling: false
  automated_refactoring: false
  test_generation: true
  dependency_management: true

# Feature-specific configuration
feature_config:
  enhanced_code_review:
    enabled_agents: ["advanced-reviewer", "style-checker"]
    mcp_servers: ["github", "filesystem", "code_quality"]
  
  security_scanning:
    enabled_agents: ["security-scanner", "vulnerability-analyzer"]
    mcp_servers: ["github", "filesystem", "security_tools"]
  
  performance_profiling:
    enabled_agents: ["performance-analyzer", "bottleneck-detector"]
    mcp_servers: ["github", "filesystem", "profiling_tools"]
  
  automated_refactoring:
    enabled_agents: ["refactoring-agent", "code-modernizer"]
    mcp_servers: ["github", "filesystem"]
  
  test_generation:
    enabled_agents: ["test-generator", "test-analyzer"]
    mcp_servers: ["github", "filesystem", "test_runner"]
  
  dependency_management:
    enabled_agents: ["dependency-updater", "vulnerability-checker"]
    mcp_servers: ["github", "filesystem", "package_registry"]
```

These examples demonstrate the flexibility of A5C configuration for different project types and requirements. Adapt them to your specific needs and combine elements from different patterns as necessary.