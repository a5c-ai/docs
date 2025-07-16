# Creating Custom Agents

This tutorial guides you through the process of creating custom A5C agents tailored to your specific project needs. Custom agents can automate specialized tasks, enforce team standards, or provide domain-specific assistance.

## Prerequisites

Before creating custom agents, ensure you have:

- A5C set up in your project (see [installation](../getting-started/installation.md))
- Basic understanding of [A5C agents](../concepts/agents.md) and their capabilities
- Familiarity with Markdown and YAML syntax
- Clear requirements for what your custom agent should accomplish

## Custom Agent Overview

A custom A5C agent consists of:

1. **YAML frontmatter**: Configuration that defines the agent's behavior, triggers, and metadata
2. **Markdown prompt**: Instructions that guide the AI model's responses and actions

Custom agents are stored as `.agent.md` files and can be:
- **Local agents**: Stored in your repository's `.a5c/agents` directory
- **Remote agents**: Stored in a registry repository and referenced by your project

## Step 1: Define Your Agent's Purpose

Before writing code, clearly define:

1. **Agent purpose**: What specific problem will this agent solve?
2. **Target users**: Who will interact with this agent?
3. **Key capabilities**: What tasks should the agent perform?
4. **Activation methods**: How will the agent be triggered?
5. **Required access**: What systems or data will the agent need?

### Example Agent Concept

For this tutorial, we'll create a "documentation-validator-agent" that:
- Verifies documentation completeness and quality
- Checks for broken links and references
- Suggests improvements for clarity and readability
- Ensures consistent formatting and style

## Step 2: Create the Agent File Structure

### Create the Agents Directory

If you don't already have one, create a directory for local agents:

```bash
mkdir -p .a5c/agents
```

### Create the Agent File

Create a new file with the `.agent.md` extension:

```bash
touch .a5c/agents/documentation-validator-agent.agent.md
```

## Step 3: Configure the Agent Frontmatter

The YAML frontmatter defines how and when your agent runs. Let's configure our example agent:

```yaml
---
# Agent Metadata
name: documentation-validator-agent
version: 1.0.0
category: documentation
description: Validates documentation quality, completeness, and consistency

# Usage Context
usage_context: |
  Use this agent to validate documentation files, check for broken references,
  and ensure documentation meets quality standards.

# Invocation Context
invocation_context: |
  Mention this agent when you need to validate documentation files or
  improve documentation quality.

# Execution Configuration
model: claude-3-7-sonnet-20250219
max_turns: 10
timeout: 300
verbose: false

# Trigger Configuration
events: ["pull_request", "push"]
mentions: "@documentation-validator-agent,@doc-validator"
labels: "documentation,docs"
branches: "main,develop,feature/*"
paths: "docs/**/*.md,**/*.rst,README.md"

# Priority (higher runs first)
priority: 60

# MCP Server Configuration
mcp_servers: ["filesystem", "github"]

# Agent Discovery
agent_discovery:
  enabled: true
  include_same_directory: true
  max_agents_in_context: 5
---
```

Let's break down the key configuration sections:

### Metadata and Context

- `name`: Unique identifier for your agent
- `version`: Agent version for tracking changes
- `category`: Classification for organization
- `description`: Brief explanation of the agent's purpose
- `usage_context`: When and how to use this agent
- `invocation_context`: How users should invoke the agent

### Execution Configuration

- `model`: The AI model to use (Claude version)
- `max_turns`: Maximum conversation turns for a single task
- `timeout`: Maximum execution time in seconds
- `verbose`: Whether to include detailed logs

### Trigger Configuration

- `events`: GitHub events that activate the agent
- `mentions`: @ mentions that trigger the agent
- `labels`: Issue/PR labels that trigger the agent
- `branches`: Git branches that trigger the agent
- `paths`: File paths that trigger the agent

### Advanced Configuration

- `priority`: Execution priority compared to other agents
- `mcp_servers`: External services the agent can access
- `agent_discovery`: Settings for agent collaboration

## Step 4: Write the Agent Prompt

After the frontmatter, add the agent prompt that guides the AI's behavior:

```markdown
# Documentation Validator Agent

You are a Documentation Validator Agent, part of the A5C agent system. Your primary role is to ensure documentation quality, completeness, and consistency across the project.

## Core Responsibilities

1. **Documentation Validation**: Verify that documentation is complete, accurate, and follows standards
2. **Reference Checking**: Identify and report broken links or missing references
3. **Quality Assessment**: Evaluate documentation clarity, readability, and organization
4. **Improvement Suggestions**: Provide actionable feedback to enhance documentation

## Validation Process

When validating documentation, follow this process:

### 1. Structural Analysis

- Verify that documentation has proper headings and organization
- Check for required sections (Overview, Usage, API Reference, etc.)
- Ensure consistent formatting of lists, code blocks, and callouts
- Verify that tables are properly formatted and aligned

### 2. Content Evaluation

- Check for comprehensive coverage of features and functionality
- Verify that examples are current and functional
- Ensure terminology is consistent throughout documentation
- Check for clear explanations of complex concepts
- Verify that prerequisite knowledge is clearly stated

### 3. Reference Validation

- Check all internal links between documentation files
- Verify external links are accessible and relevant
- Ensure code references match actual implementation
- Check that image references are valid and images are accessible

### 4. Quality Assessment

- Evaluate readability using clear, simple language
- Check for grammatical errors and typos
- Ensure documentation follows the project style guide
- Verify appropriate use of formatting for clarity

## Response Guidelines

When responding to documentation validation requests:

1. **Provide a summary assessment** of overall documentation quality
2. **List specific issues** organized by category (structure, content, references, quality)
3. **Include specific locations** of issues (file path, line number, section)
4. **Offer concrete suggestions** for addressing each issue
5. **Prioritize issues** by importance (critical, major, minor)

## Example Output Format

```
# Documentation Validation Report

## Summary
[Overall assessment of documentation quality with key strengths and weaknesses]

## Critical Issues
- [Issue description with location and suggestion]
- [Issue description with location and suggestion]

## Major Issues
- [Issue description with location and suggestion]
- [Issue description with location and suggestion]

## Minor Issues
- [Issue description with location and suggestion]
- [Issue description with location and suggestion]

## Recommendations
[Strategic recommendations for improving documentation]
```

## Special Considerations

1. **Documentation Standards**: Always reference the project's style guide or documentation standards when available
2. **Technical Accuracy**: Focus on structural and quality issues rather than technical accuracy
3. **Progressive Enhancement**: Suggest improvements that can be implemented incrementally
4. **Context Awareness**: Consider the target audience when evaluating documentation
5. **Positive Reinforcement**: Acknowledge good practices alongside improvement suggestions

When invoked, first examine the repository structure to understand the documentation organization before providing feedback.
```

## Step 5: Test Your Custom Agent

### Add the Agent to Your A5C Configuration

Ensure your `.a5c/config.yml` includes local agents:

```yaml
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
```

### Commit and Push Your Agent

```bash
git add .a5c/agents/documentation-validator-agent.agent.md
git commit -m "Add custom documentation validator agent"
git push
```

### Create a Test Issue

1. Go to your repository on GitHub
2. Click "Issues" → "New issue"
3. Title: "Test documentation validator agent"
4. Content:

```
@documentation-validator-agent

Please validate the documentation in this repository and provide a report on its quality, completeness, and consistency.

Focus especially on:
1. README.md
2. The docs/ directory
3. Any broken links or references

Thank you!
```

5. Click "Submit new issue"

### Review the Agent's Response

Wait for the GitHub Action to complete and review the agent's response in the issue. Evaluate if the agent behaves as expected and make adjustments to the configuration or prompt as needed.

## Step 6: Refine Your Agent

Based on the initial test, refine your agent:

### Improve the Prompt

Enhance the prompt to better guide the agent's behavior:
- Add more specific instructions
- Include examples of good and bad documentation
- Clarify evaluation criteria
- Add context about your project's documentation standards

### Adjust the Configuration

Fine-tune the YAML configuration:
- Refine trigger conditions
- Adjust execution parameters
- Update priority if needed
- Add or remove MCP server access

### Test Again

After making changes, test again to verify improvements.

## Step 7: Advanced Agent Techniques

### Agent Inheritance

You can create specialized agents that inherit from a base agent:

```yaml
---
name: api-documentation-validator
from: documentation-validator-agent  # Inherits from our base validator
category: documentation
priority: 65
paths: "docs/api/**/*.md"
---

{{base-prompt}}

# API Documentation Specific Validation

In addition to the base validation process, perform these API-specific checks:

1. **Endpoint Documentation**
   - Verify all endpoints are documented with URL, method, and description
   - Check that request parameters and response formats are clearly specified
   - Ensure authentication requirements are explained

2. **Status Codes**
   - Verify all possible status codes are documented
   - Check that error responses are explained

3. **Examples**
   - Ensure each endpoint has request and response examples
   - Verify that examples are valid and match the described format
```

### Agent Collaboration

Configure agents to work together through agent discovery:

```yaml
agent_discovery:
  enabled: true
  allowed_agents:
    - "code-review-agent"
    - "security-scanner-agent"
  include_same_directory: true
  max_agents_in_context: 5
```

This allows your documentation validator to reference or collaborate with other agents when needed.

### Environment-Aware Behavior

Make your agent adapt to different environments:

```markdown
## Environment-Specific Behavior

Adjust validation based on the current context:

1. **Pull Request Context**
   - Focus validation on files changed in the PR
   - Provide concise feedback suitable for PR comments
   - Highlight changes that impact existing documentation

2. **Issue Context**
   - Provide comprehensive documentation assessment
   - Include strategic recommendations for improvement
   - Suggest documentation structure enhancements

3. **Push Context**
   - Focus on quick validation of recent changes
   - Flag critical issues that should be addressed immediately
   - Verify consistency with existing documentation
```

## Step 8: Sharing Your Agent

### Adding to a Registry

If your agent would be useful to others, consider adding it to a registry:

1. Fork the agent registry repository
2. Add your agent file to the appropriate category
3. Create a pull request to contribute your agent

### Documentation

Create documentation for your agent:

1. Usage instructions and examples
2. Configuration options
3. Best practices for interaction
4. Common issues and solutions

## Best Practices for Custom Agents

1. **Focused purpose**: Create agents with specific, well-defined responsibilities
2. **Clear instructions**: Provide detailed guidance in the prompt
3. **Progressive refinement**: Start simple and add complexity as needed
4. **Consistent format**: Use a standard output format for easy parsing
5. **Error handling**: Include instructions for handling edge cases
6. **Performance consideration**: Limit scope to avoid timeouts
7. **User feedback**: Include mechanisms for users to provide feedback
8. **Version tracking**: Increment version numbers when making significant changes

## Common Agent Patterns

### Review Agent Pattern

```markdown
1. **Analysis Phase**: Examine content against standards
2. **Issues Identification**: List specific problems found
3. **Prioritization**: Categorize issues by severity
4. **Recommendations**: Provide actionable suggestions
5. **Summary**: Overall assessment and next steps
```

### Creator Agent Pattern

```markdown
1. **Requirement Analysis**: Understand what needs to be created
2. **Planning**: Outline the approach and structure
3. **Implementation**: Create the requested content or code
4. **Validation**: Verify the result meets requirements
5. **Explanation**: Document what was created and why
```

### Helper Agent Pattern

```markdown
1. **Question Understanding**: Parse the user's request
2. **Context Gathering**: Collect relevant information
3. **Answer Formulation**: Prepare a helpful response
4. **Additional Resources**: Suggest related information
5. **Follow-up**: Anticipate follow-up questions
```

## Conclusion

By creating custom agents tailored to your project's specific needs, you can significantly enhance your team's productivity and code quality. Custom agents can automate repetitive tasks, enforce standards, and provide specialized assistance that generic agents cannot.

As you develop more agents, consider creating an agent ecosystem that works together to cover different aspects of your development process.

## Next Steps

- Learn about [agent triggers](../concepts/triggers.md) for advanced activation methods
- Explore [MCP integration](../concepts/mcp.md) for expanded capabilities
- Understand [agent discovery](../concepts/agent-discovery.md) for agent collaboration
- Learn how to [implement custom MCP servers](implementing-custom-mcp-servers.md) for specialized integrations