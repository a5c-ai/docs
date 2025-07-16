# Adding A5C to Existing Projects

This tutorial walks you through the process of integrating the A5C agent system into your existing projects, allowing you to leverage AI-powered development assistance without starting from scratch.

## Prerequisites

Before integrating A5C into your project, ensure you have:

- A GitHub repository for your existing project
- Administrator access to the repository
- Basic understanding of Git workflows
- An Anthropic API key for Claude access
- Completed the [installation](../getting-started/installation.md) process

## Integration Overview

Adding A5C to an existing project involves:

1. Creating the A5C configuration structure
2. Setting up GitHub workflows for agent execution
3. Configuring repository secrets
4. Testing the integration with a simple agent task
5. Adapting your development workflow to leverage agents

## Step 1: Configure A5C in Your Project

### Clone Your Repository

First, clone your existing repository if you don't have it locally:

```bash
git clone https://github.com/your-username/your-project.git
cd your-project
```

### Create A5C Configuration Structure

Create the A5C configuration directory:

```bash
mkdir -p .a5c
```

### Create the Configuration File

Create `.a5c/config.yml` with the following content, adjusting as needed for your project:

```yaml
# A5C Configuration
version: 1.0.0

# Global settings
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false
  timeout: 600  # 10 minutes

# Agent configuration
agents:
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/**/*.agent.md"
  local:
    enabled: true
    paths:
      - "./.a5c/agents"

# MCP servers configuration
mcp_servers:
  github:
    enabled: true
  filesystem:
    enabled: true
  memory:
    enabled: true
    persistence: session
```

### Optional: Create a Custom Agent Directory

If you plan to create custom agents specific to your project:

```bash
mkdir -p .a5c/agents
```

## Step 2: Set Up GitHub Workflow

### Create Workflow Directory

```bash
mkdir -p .github/workflows
```

### Create A5C Workflow File

Create `.github/workflows/a5c.yml`:

```yaml
name: A5C Agent System
on:
  pull_request:
    types: [opened, synchronize]
  issues:
    types: [opened, edited]
  issue_comment:
    types: [created]
  push:
    branches: [main, master, develop]

jobs:
  run-agents:
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

### Customize Workflow Triggers

Modify the triggers in the workflow file to match your project's workflow:

```yaml
on:
  pull_request:
    types: [opened, synchronize]
    paths:
      - 'src/**'
      - 'tests/**'
      - 'package.json'
  issues:
    types: [opened, edited, labeled]
  issue_comment:
    types: [created]
  push:
    branches: [main, develop, feature/*]
    paths-ignore:
      - '*.md'
      - 'docs/**'
```

## Step 3: Add Repository Secrets

### Add Anthropic API Key

1. Go to your repository on GitHub
2. Navigate to Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `ANTHROPIC_API_KEY`
5. Value: Your Anthropic API key
6. Click "Add secret"

### Optional: Add Additional Secrets

Depending on your project and the agents you'll use, you might need additional secrets like:

- `OPENAI_API_KEY` for OpenAI integrations
- `DATABASE_URL` for database access
- `DEPLOYMENT_TOKEN` for deployment agents

## Step 4: Commit and Push Configuration

```bash
git add .a5c .github
git commit -m "Add A5C configuration"
git push
```

## Step 5: Verify Integration

### Create a Test Issue

1. Go to your repository on GitHub
2. Click "Issues" → "New issue"
3. Title: "Test A5C integration"
4. Content:

```
@developer-agent

Please analyze this repository and provide a brief overview of:
1. The project structure
2. Key components and their relationships
3. Potential areas where A5C agents could provide the most value
4. Any initial recommendations for improving the codebase

This is a test to verify A5C integration.
```

5. Click "Submit new issue"

### Check GitHub Actions

1. Go to the "Actions" tab in your repository
2. You should see the A5C workflow running
3. Click on the workflow run to see the details
4. Verify that the workflow completes successfully

### Review Agent Response

Once the workflow completes, check the issue for the agent's response. If the integration is successful, the developer-agent will respond with an analysis of your project.

## Step 6: Project-Specific Configuration

Based on your project's specific needs, you might want to:

### Add Language-Specific Settings

For JavaScript/TypeScript projects:

```yaml
# Add to .a5c/config.yml
settings:
  language_settings:
    javascript:
      linter: "eslint"
      package_manager: "npm"
      test_command: "npm test"
```

For Python projects:

```yaml
# Add to .a5c/config.yml
settings:
  language_settings:
    python:
      linter: "flake8"
      package_manager: "pip"
      test_command: "pytest"
```

### Configure Project-Specific Agent Triggers

```yaml
# Add to .a5c/config.yml
triggers:
  pull_request:
    labeled:
      - label: "needs-review"
        agent: "code-review-agent"
      - label: "security"
        agent: "security-scanner-agent"
  push:
    paths:
      - pattern: "*.js"
        agent: "javascript-linter-agent"
      - pattern: "*.py"
        agent: "python-linter-agent"
```

## Step 7: Integrating A5C into Your Development Workflow

### Document Agent Usage for Team Members

Create a document explaining how to use A5C agents in your project. Include:

1. Available agents and their capabilities
2. How to mention agents in issues and pull requests
3. Best practices for writing effective agent requests
4. Examples of common agent tasks

### Update Contributing Guidelines

Update your `CONTRIBUTING.md` or equivalent document to include A5C workflows:

```markdown
## Using A5C Agents

This project uses A5C for AI-assisted development. You can leverage agents by:

1. Mentioning them in issues and pull requests (e.g., `@code-review-agent`)
2. Adding specific labels to trigger automated reviews
3. Following the agent request templates

For detailed documentation on available agents and their usage, see [A5C Agents](./docs/a5c-agents.md).
```

### Create Agent Request Templates

Add issue and PR templates for common agent requests:

Example `.github/ISSUE_TEMPLATE/feature_request.md`:

```markdown
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: enhancement
assignees: ''
---

## Feature Description

[Describe the feature you'd like]

## Implementation Details

[Any specific implementation details or requirements]

## Agent Request (Optional)

@developer-agent

Please help implement this feature with the following requirements:
1. [Requirement 1]
2. [Requirement 2]
3. [Requirement 3]

## Additional Context

[Add any other context or screenshots about the feature request here]
```

## Step 8: Advanced Configurations

As your team becomes more familiar with A5C, consider these advanced configurations:

### Custom Agent Creation

Create custom agents tailored to your project's specific needs. See the [Creating Custom Agents](creating-custom-agents.md) tutorial for details.

### Workflow Automation

Set up automated workflows for common tasks:

```yaml
# Add to .a5c/config.yml
automations:
  - name: "Code Review on PR"
    triggers:
      - event: "pull_request.opened"
      - event: "pull_request.synchronize"
    actions:
      - agent: "code-review-agent"
        params:
          level: "thorough"
          comment: true
  
  - name: "Documentation Check"
    triggers:
      - event: "push"
        paths: ["docs/**", "README.md"]
    actions:
      - agent: "documentation-validator-agent"
```

### Integration with CI/CD

Integrate A5C with your existing CI/CD pipeline:

```yaml
# In your main CI workflow
jobs:
  tests:
    # Your test job configuration...
    
  a5c-analysis:
    needs: tests
    if: success()
    uses: ./.github/workflows/a5c.yml
```

## Troubleshooting

### Common Issues and Solutions

| Issue | Possible Causes | Solutions |
|-------|-----------------|-----------|
| Workflow fails to start | Misconfigured workflow file | Check YAML syntax and path to config file |
| Agent doesn't respond | Incorrect agent mention, API key issue | Verify agent name, check API key in secrets |
| Permission errors | Insufficient GitHub token permissions | Use `permissions:` section in workflow to add required permissions |
| Rate limiting | Too many API calls | Implement more specific workflow triggers |

### Checking Logs

To troubleshoot issues, check the GitHub Actions logs:

1. Go to the "Actions" tab in your repository
2. Find the failed workflow run
3. Click on the job name to expand details
4. Check the logs for error messages

## Best Practices for A5C in Existing Projects

1. **Start small**: Begin with a few simple agent integrations before expanding
2. **Document agent usage**: Ensure team members understand how to use agents
3. **Standardize requests**: Create templates for common agent tasks
4. **Review agent outputs**: Always review code or suggestions from agents
5. **Gather feedback**: Regularly collect team feedback on agent effectiveness
6. **Iterate configuration**: Refine your A5C configuration based on team needs
7. **Share knowledge**: Document successful agent usage patterns for the team

## Conclusion

By adding A5C to your existing project, you've equipped your team with powerful AI assistance for development tasks. As your team becomes more familiar with agent capabilities, you can customize and expand your A5C configuration to further enhance productivity.

## Next Steps

- Learn more about [A5C agents](../concepts/agents.md) and their capabilities
- Explore [creating custom agents](creating-custom-agents.md) for your specific needs
- Discover how to [build a project from scratch](building-project-from-scratch.md) with A5C
- Learn about [implementing custom MCP servers](implementing-custom-mcp-servers.md) for specialized integrations