# Agent Registry

This page provides comprehensive reference documentation for all available agents in the a5c registry. Each agent has specific capabilities, triggers, and configuration options.

## Core Agents

These agents form the foundation of the a5c system and provide essential functionality.

### Coordination Agent

**Name**: `coordination-agent`  
**Category**: System  
**Description**: Manages communication between agents and orchestrates workflows.

| Capability | Description |
|------------|-------------|
| Agent Discovery | Identifies which agents are needed for a task |
| Workflow Management | Creates and manages task sequences |
| Resource Allocation | Assigns appropriate resources to agents |
| Status Tracking | Monitors the progress of all active agents |

**Configuration Options**:

```yaml
name: coordination-agent
enabled: true
priority: high
max_concurrent_tasks: 10
workflow_templates_path: .a5c/workflows/
agent_timeout: 300
```

**Default Triggers**:
- GitHub events: `workflow_dispatch`, `repository_dispatch`
- Branch patterns: All branches
- Mention pattern: `@coordinator`

---

### Content Writer Agent

**Name**: `content-writer-agent`  
**Category**: Communication  
**Description**: Creates and refines documentation, READMEs, and other content.

| Capability | Description |
|------------|-------------|
| Technical Writing | Transforms technical concepts into clear documentation |
| Content Formatting | Applies consistent styling and formatting |
| Documentation Structure | Creates organized, hierarchical content |
| SEO Optimization | Implements best practices for discoverability |

**Configuration Options**:

```yaml
name: content-writer-agent
enabled: true
template_directory: .a5c/templates/content/
style_guide_path: .a5c/style-guide.md
glossary_path: .a5c/glossary.md
max_content_length: 10000
```

**Default Triggers**:
- GitHub events: `push` to documentation files
- File patterns: `**/*.md`, `**/*.rst`, `docs/**/*`
- Mention patterns: `@content-writer`, `@documentation`

---

### Code Review Agent

**Name**: `code-review-agent`  
**Category**: Development  
**Description**: Analyzes code for quality, performance, and security issues.

| Capability | Description |
|------------|-------------|
| Code Quality Analysis | Identifies code smells and anti-patterns |
| Security Scanning | Detects potential security vulnerabilities |
| Performance Review | Suggests optimizations for better performance |
| Style Compliance | Ensures adherence to coding standards |

**Configuration Options**:

```yaml
name: code-review-agent
enabled: true
review_depth: comprehensive
ignore_patterns: ["**/node_modules/**", "**/vendor/**"]
max_files_per_review: 20
coding_standards: [".a5c/standards/javascript.yml", ".a5c/standards/python.yml"]
```

**Default Triggers**:
- GitHub events: `pull_request.opened`, `pull_request.synchronize`
- Branch patterns: All except `main`, `master`
- Mention pattern: `@code-review`

## Specialized Agents

These agents provide more focused capabilities for specific tasks or domains.

### Security Scanner Agent

**Name**: `security-scanner-agent`  
**Category**: Security  
**Description**: Identifies security vulnerabilities and suggests remediations.

| Capability | Description |
|------------|-------------|
| Dependency Scanning | Checks for vulnerable dependencies |
| Code Analysis | Identifies insecure coding patterns |
| Secret Detection | Finds hardcoded secrets and credentials |
| SAST Integration | Integrates with static analysis tools |

**Configuration Options**:

```yaml
name: security-scanner-agent
enabled: true
scan_level: deep
database_update_frequency: daily
notify_on: [critical, high]
ignore_false_positives_path: .a5c/security/false-positives.yml
```

**Default Triggers**:
- GitHub events: `push` to production branches, `pull_request` to protected branches
- Labels: `security`, `needs-security-review`
- Schedule: Daily on default branch
- Mention pattern: `@security-scanner`

---

### Test Generator Agent

**Name**: `test-generator-agent`  
**Category**: Quality Assurance  
**Description**: Creates test cases and test implementations for code.

| Capability | Description |
|------------|-------------|
| Unit Test Generation | Creates focused tests for individual functions |
| Integration Test Planning | Designs tests for component interactions |
| Test Coverage Analysis | Identifies untested code paths |
| Test Data Generation | Creates realistic test fixtures and data |

**Configuration Options**:

```yaml
name: test-generator-agent
enabled: true
test_frameworks: ["jest", "pytest"]
coverage_target: 80
generate_mocks: true
test_directory_pattern: "{src_dir}/../tests/"
```

**Default Triggers**:
- GitHub events: `push` with new or modified code files
- File patterns: `**/*.js`, `**/*.py`, `**/*.ts`, `**/*.go`
- Labels: `needs-tests`
- Mention pattern: `@test-generator`

---

### Data Processor Agent

**Name**: `data-processor-agent`  
**Category**: Data  
**Description**: Transforms, analyzes, and visualizes data.

| Capability | Description |
|------------|-------------|
| Data Transformation | Converts between data formats |
| Data Analysis | Performs statistical analysis |
| Data Visualization | Creates charts and graphs |
| ETL Pipeline Management | Manages data extraction and loading |

**Configuration Options**:

```yaml
name: data-processor-agent
enabled: true
supported_formats: ["csv", "json", "parquet", "excel"]
max_data_size: "100MB"
visualization_library: "matplotlib"
data_cache_ttl: 3600
```

**Default Triggers**:
- GitHub events: `push` to data files
- File patterns: `**/*.csv`, `**/*.json`, `data/**/*`
- Labels: `data-processing`
- Mention pattern: `@data-processor`

## DevOps Agents

These agents assist with infrastructure, deployment, and operational tasks.

### Deployment Agent

**Name**: `deployment-agent`  
**Category**: DevOps  
**Description**: Manages deployment processes and configurations.

| Capability | Description |
|------------|-------------|
| Deployment Planning | Creates step-by-step deployment plans |
| Configuration Management | Handles environment-specific configs |
| Deployment Verification | Validates successful deployments |
| Rollback Coordination | Manages rollback procedures if needed |

**Configuration Options**:

```yaml
name: deployment-agent
enabled: true
environments: ["development", "staging", "production"]
deployment_templates: .a5c/deployment/
require_approval_for: ["staging", "production"]
post_deployment_tests: true
```

**Default Triggers**:
- GitHub events: `release.published`, `workflow_dispatch`
- Branch patterns: `main`, `release/*`
- Labels: `deploy`
- Mention pattern: `@deployment`

---

### Infrastructure Agent

**Name**: `infrastructure-agent`  
**Category**: DevOps  
**Description**: Manages cloud resources and infrastructure as code.

| Capability | Description |
|------------|-------------|
| IaC Management | Helps with Terraform, CloudFormation, etc. |
| Resource Optimization | Suggests efficient resource configurations |
| Architecture Planning | Assists with infrastructure design |
| Cost Estimation | Provides cost estimates for infrastructure |

**Configuration Options**:

```yaml
name: infrastructure-agent
enabled: true
cloud_providers: ["aws", "azure", "gcp"]
iac_tools: ["terraform", "cloudformation", "pulumi"]
state_file_path: .a5c/infrastructure/state/
cost_optimization: true
```

**Default Triggers**:
- GitHub events: `push` to infrastructure files
- File patterns: `**/*.tf`, `**/*.yaml`, `infrastructure/**/*`
- Labels: `infrastructure`
- Mention pattern: `@infrastructure`

## Custom Agent Development

a5c supports creating custom agents for specialized tasks. Custom agents must follow the a5c agent protocol and implement required interfaces.

### Agent Structure

Custom agents should be structured as follows:

```
.a5c/agents/my-custom-agent/
├── agent-config.yml  # Agent configuration
├── prompts/          # Agent prompts
│   ├── system.md     # System prompt
│   └── templates/    # Response templates
├── tools/            # Custom tools
└── README.md         # Agent documentation
```

### Agent Configuration Template

```yaml
name: my-custom-agent
version: 1.0.0
description: Description of what your agent does
category: custom
enabled: true
model: gpt-4
capabilities:
  - capability-one
  - capability-two
triggers:
  - type: mention
    patterns: ["@my-custom-agent"]
  - type: event
    events: ["push"]
    conditions:
      paths: ["custom/**/*"]
tools:
  - tool-one
  - tool-two
permissions:
  read: true
  write: false
  execute: false
```

## Integration with Other Agents

Agents can collaborate through the following mechanisms:

1. **Direct Mentions**: Use `@agent-name` in commits or comments
2. **Shared Memory**: Access data from the MCP shared memory store
3. **Event Subscriptions**: Subscribe to events from other agents
4. **Workflow Integration**: Participate in multi-agent workflows

## Related Resources

- [A5C Registry Repository](https://github.com/a5c-ai/registry)
- [Agent Interactions](/concepts/agent-discovery)
- [A5C GitHub Action Repository](https://github.com/a5c-ai/action)