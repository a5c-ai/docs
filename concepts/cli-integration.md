# CLI Integration

A5C provides command-line interface (CLI) integration to allow agents to interact with various CLI tools and processes. This page explains how to configure and use CLI integration in A5C.

## Overview

CLI integration enables A5C agents to:

1. Execute shell commands
2. Interact with command-line tools
3. Manage project dependencies
4. Run tests and builds
5. Deploy applications
6. Automate repetitive tasks

This integration is particularly useful for development workflows, build processes, and deployment automation.

## Supported CLI Tools

A5C agents can interact with many CLI tools, including:

- **Version Control**: git, GitHub CLI (gh)
- **Package Managers**: npm, yarn, pip, composer, cargo
- **Build Tools**: make, gradle, maven, webpack
- **Testing Frameworks**: jest, pytest, mocha
- **Deployment Tools**: docker, kubectl, terraform
- **Cloud CLIs**: AWS CLI, Azure CLI, Google Cloud CLI

## Configuration

### Basic Configuration

To enable CLI integration, include it in your `.a5c/config.yml` file:

```yaml
# A5C Configuration File
version: 1.0.0

# CLI Integration
cli:
  enabled: true
  secure_mode: true  # Restricts potentially dangerous commands
  allowed_tools:
    - git
    - npm
    - yarn
    - docker
    - gh
  working_directory: "."  # Relative to repository root
```

### Agent-Specific CLI Configuration

You can also configure CLI integration for specific agents in their YAML frontmatter:

```yaml
---
name: build-agent
version: 1.0.0
category: development

# CLI configuration for this agent
cli:
  enabled: true
  allowed_tools:
    - npm
    - yarn
    - jest
  working_directory: "./frontend"
---
```

### Security Restrictions

A5C includes security restrictions for CLI integration:

```yaml
cli:
  enabled: true
  secure_mode: true
  restricted_commands:
    - rm -rf /  # Explicitly blocked commands
    - sudo
    - chmod 777
  allowed_patterns:
    - "npm (install|run|test)"  # Regex patterns for allowed commands
    - "git (status|add|commit|push)"
```

## Usage in Agents

Agents can use CLI integration through their prompt instructions:

```markdown
# Build Agent

You are a Build Agent for A5C. You have access to CLI tools to build, test, and deploy applications.

## CLI Usage Guidelines

1. **Always check the current state** before running commands:
   - Use `git status` to check repository state
   - Use `npm list` to check installed packages

2. **Use standard commands** for common operations:
   - `npm install` to install dependencies
   - `npm run build` to build the application
   - `npm test` to run tests

3. **Handle errors appropriately**:
   - Check exit codes and error messages
   - Provide detailed error reporting
   - Suggest fixes for common issues
```

## Command Execution Context

When an agent executes a CLI command, it receives:

1. **Command output**: Standard output from the command
2. **Error output**: Standard error from the command
3. **Exit code**: Indicating success (0) or failure (non-zero)
4. **Execution time**: How long the command took to run

This context helps agents understand the result and take appropriate action.

## Best Practices

### Security Considerations

1. **Use secure_mode**: Always enable secure_mode in production
2. **Restrict commands**: Limit allowed commands to necessary tools
3. **Avoid destructive operations**: Block dangerous commands
4. **Use read-only operations**: Prefer commands that don't modify critical systems

### Performance Optimization

1. **Minimize command executions**: Group operations when possible
2. **Cache results**: Avoid repeating identical commands
3. **Set timeouts**: Prevent long-running commands from blocking

### Reliability

1. **Check prerequisites**: Verify tools are installed before using them
2. **Handle failures gracefully**: Implement retry logic for transient failures
3. **Provide clear error messages**: Help troubleshoot command failures

## Common Use Cases

### Project Setup

```markdown
To set up a new project:

1. Check if dependencies are installed:
   ```
   npm list
   ```

2. Install missing dependencies:
   ```
   npm install
   ```

3. Run project setup script:
   ```
   npm run setup
   ```
```

### Continuous Integration

```markdown
For CI workflow:

1. Run tests:
   ```
   npm test
   ```

2. Build the application:
   ```
   npm run build
   ```

3. Check for linting issues:
   ```
   npm run lint
   ```
```

### Deployment

```markdown
To deploy the application:

1. Build for production:
   ```
   npm run build:prod
   ```

2. Run pre-deployment checks:
   ```
   npm run verify
   ```

3. Deploy using the deployment script:
   ```
   npm run deploy
   ```
```

## GitHub CLI Integration

A5C provides special integration with the GitHub CLI (`gh`) to allow agents to interact with GitHub:

```markdown
To work with GitHub:

1. Check PR status:
   ```
   gh pr view
   ```

2. Create a new issue:
   ```
   gh issue create --title "Bug: Login failure" --body "The login form is not submitting correctly."
   ```

3. Create a pull request:
   ```
   gh pr create --title "Fix login form" --body "Fixes the login form submission issue."
   ```
```

## Troubleshooting

If you encounter issues with CLI integration:

1. **Check permissions**: Ensure the GitHub Action has necessary permissions
2. **Verify tool installation**: Confirm required tools are installed in the runner
3. **Review command restrictions**: Make sure your commands aren't blocked by security rules
4. **Check timeouts**: Long-running commands may time out
5. **Review logs**: GitHub Action logs often contain helpful error information

## Next Steps

- Learn about [agent discovery](agent-discovery.md)
- Understand [MCP integration](mcp.md)
- Explore [configuring triggers](../guides/configuring-triggers.md)
- See examples in [automation workflows](../guides/automation-workflows.md)