# Customizing Agent Behavior

This guide explains how to customize the behavior of A5C agents to match your specific needs. You'll learn how to modify agent instructions, adjust execution parameters, and fine-tune agent capabilities.

## Introduction

A5C agents can be customized in several ways:

1. **Instruction Customization**: Modifying the agent's prompt and instructions
2. **Parameter Adjustments**: Changing execution parameters like model, turns, and timeouts
3. **Capability Configuration**: Enabling or restricting specific tools and integrations
4. **Trigger Customization**: Adjusting when and how agents are activated
5. **Response Templates**: Defining structured formats for agent responses

These customizations allow you to create agents that perfectly match your workflow requirements.

## Agent Instruction Customization

The primary way to customize agent behavior is by modifying its instructions.

### Agent Definition File Structure

A5C agent definitions follow this structure:

```markdown
---
name: custom-agent
version: 1.0.0
category: development
description: Custom agent for specialized tasks
model: claude-3-7-sonnet-20250219
max_turns: 20
timeout: 60
---

# Custom Agent

You are a specialized agent for the A5C system, designed to handle custom tasks for this project.

## Core Responsibilities

1. **Task 1**: Description of first responsibility
2. **Task 2**: Description of second responsibility
3. **Task 3**: Description of third responsibility

## Analysis Guidelines

When analyzing code or issues:

1. First check...
2. Then examine...
3. Finally verify...

## Action Guidelines

When taking action:

1. Start by...
2. Then proceed to...
3. Finish by...

## Communication Protocol

Communicate using these guidelines:

1. **Report Started**: Signal when you begin analysis
2. **Report Progress**: Update status as you work
3. **Report Completed**: Provide summary of actions taken

## Tools and Integrations

You have access to:

1. **GitHub API**: For repository operations
2. **CLI Tools**: For command-line operations
3. **MCP Servers**: For external integrations
```

### Modifying Agent Instructions

To customize agent behavior, modify these key sections:

#### Core Responsibilities

Define the primary tasks the agent should perform:

```markdown
## Core Responsibilities

1. **Code Review**: Review pull requests for code quality, bugs, and performance issues
2. **Documentation Check**: Ensure code is properly documented with comments and examples
3. **Style Enforcement**: Verify code follows project style guidelines
4. **Security Review**: Check for common security vulnerabilities
5. **Test Coverage**: Ensure adequate test coverage for new code
```

#### Analysis Guidelines

Specify how the agent should approach analysis tasks:

```markdown
## Analysis Guidelines

When reviewing code:

1. **Check Functionality**: First verify the code works as intended
2. **Review Readability**: Ensure code is readable and well-structured
3. **Examine Performance**: Look for performance bottlenecks and inefficiencies
4. **Verify Security**: Check for security vulnerabilities
5. **Test Coverage**: Confirm adequate test coverage
6. **Style Compliance**: Verify adherence to coding standards
```

#### Action Guidelines

Define how the agent should take action:

```markdown
## Action Guidelines

When providing feedback:

1. **Be Specific**: Point to exact lines and files
2. **Be Constructive**: Offer solutions, not just criticisms
3. **Prioritize Issues**: Focus on critical issues first
4. **Show Examples**: Provide examples of better approaches
5. **Explain Reasoning**: Explain why changes are recommended
6. **Consider Context**: Account for project constraints and goals
```

#### Communication Protocol

Specify how the agent should communicate:

```markdown
## Communication Protocol

Format your feedback as follows:

1. **Summary**: Brief overview of your findings
2. **Critical Issues**: List of critical issues that must be addressed
3. **Improvements**: Suggested improvements that are beneficial but optional
4. **Positive Aspects**: Highlight good practices in the code
5. **Next Steps**: Recommended actions for the developer
```

### Instruction Best Practices

Follow these best practices when customizing agent instructions:

1. **Be Specific**: Provide clear, actionable guidelines
2. **Use Examples**: Include examples of desired behavior
3. **Define Priorities**: Indicate what the agent should focus on
4. **Set Boundaries**: Clarify what the agent should NOT do
5. **Structured Format**: Use consistent sections and formatting
6. **Include Edge Cases**: Address common exceptions and special cases
7. **Reinforce Key Points**: Repeat critical instructions in different sections

## Parameter Customization

Adjust agent execution parameters in the frontmatter:

```yaml
---
name: performance-agent
version: 1.0.0
category: performance
description: Agent for identifying and fixing performance issues

# Model configuration
model: claude-3-7-opus-20240229  # High-performance model

# Execution parameters
max_turns: 30  # More conversation turns for complex analysis
timeout: 300  # Longer timeout for detailed analysis
temperature: 0.2  # Lower temperature for more deterministic responses

# Tool access
tools:
  github: true
  filesystem: true
  memory: true
  cli:
    enabled: true
    allowed_commands: ["git", "npm", "jest", "benchmark"]
---
```

### Model Selection

Choose the appropriate model for your agent:

- **claude-3-7-sonnet-20250219**: Balanced performance for general tasks
- **claude-3-7-opus-20240229**: Higher performance for complex reasoning
- **claude-3-5-sonnet-20240620**: Faster responses for simpler tasks

### Execution Parameters

Adjust these parameters to control agent execution:

- **max_turns**: Maximum conversation turns (default: 20)
- **timeout**: Maximum execution time in seconds (default: 60)
- **temperature**: Randomness in responses (0.0-1.0, default: 0.7)
- **top_p**: Nucleus sampling parameter (0.0-1.0, default: 0.9)
- **top_k**: Limits token selection (default: 40)

### Advanced Parameters

Fine-tune agent behavior with advanced parameters:

```yaml
---
# Advanced configuration
max_tokens_to_sample: 8000  # Maximum response length
stop_sequences: ["<end>", "END OF RESPONSE"]  # Stop generation at these sequences
system_instructions:
  priority: "Always prioritize security over performance"
  restrictions: "Never modify configuration files directly"
---
```

## Tool Access Customization

Control which tools and capabilities the agent can use:

### GitHub Tool Access

```yaml
---
tools:
  github:
    enabled: true
    operations:
      read: true
      write: true
      delete: false  # Prevent deletion operations
    repositories:
      - "owner/repo"
      - "owner/*"  # All repositories in this organization
---
```

### Filesystem Tool Access

```yaml
---
tools:
  filesystem:
    enabled: true
    read_only: false
    allowed_paths:
      - "src/"
      - "docs/"
    restricted_paths:
      - ".github/workflows/"
      - "config/secrets/"
    max_file_size: 10485760  # 10MB in bytes
---
```

### CLI Tool Access

```yaml
---
tools:
  cli:
    enabled: true
    allowed_commands:
      - "git"
      - "npm"
      - "yarn"
      - "jest"
    restricted_commands:
      - "rm -rf"
      - "chmod 777"
      - "sudo"
    working_directory: "."  # Relative to repository root
---
```

### MCP Server Access

```yaml
---
tools:
  mcp_servers:
    github: true
    filesystem: true
    memory: true
    custom:
      - "jira-server"
      - "slack-server"
---
```

## Response Formatting

Customize how agent responses are formatted:

### GitHub Comment Templates

Define templates for GitHub comments:

```yaml
---
response_templates:
  github_comment:
    success: |
      ## Analysis Complete ✅
      
      I've analyzed the code and found:
      
      ### Summary
      {summary}
      
      ### Issues
      {issues}
      
      ### Recommendations
      {recommendations}
    
    error: |
      ## Analysis Failed ❌
      
      I encountered an error during analysis:
      
      ```
      {error_message}
      ```
      
      Please fix the issue and try again.
---
```

### Commit Message Templates

Define templates for commit messages:

```yaml
---
response_templates:
  commit_message:
    fix: "fix: {issue_description}\n\nFixes {issue_reference}\n\nBy: {agent_name}"
    feat: "feat: {feature_description}\n\nImplements {feature_reference}\n\nBy: {agent_name}"
    docs: "docs: {docs_description}\n\nUpdates documentation for {subject}\n\nBy: {agent_name}"
---
```

### Code Comment Templates

Define templates for code comments:

```yaml
---
response_templates:
  code_comments:
    javascript: "// {comment_text}"
    python: "# {comment_text}"
    html: "<!-- {comment_text} -->"
    css: "/* {comment_text} */"
---
```

## Specialized Agent Customization

Customize agents for specific roles:

### Code Review Agent

```markdown
# Code Review Agent

You are a Code Review Agent for A5C. Your job is to review code changes and provide feedback.

## Review Process

1. **Read the PR Description**: Understand the context and purpose of the changes
2. **Examine Changed Files**: Review all files modified in the pull request
3. **Check Functionality**: Verify the code implements the intended functionality
4. **Review Quality**: Assess code quality, readability, and maintainability
5. **Verify Tests**: Ensure appropriate tests are included
6. **Security Check**: Look for potential security issues
7. **Style Compliance**: Verify adherence to project coding standards

## Review Criteria

Rate each aspect on a scale of 1-5:

1. **Functionality**: Does the code work as intended?
2. **Readability**: Is the code easy to understand?
3. **Maintainability**: Will the code be easy to maintain?
4. **Test Coverage**: Are there sufficient tests?
5. **Security**: Is the code secure?
6. **Performance**: Is the code efficient?

## Feedback Format

Structure your feedback as follows:

```
## Code Review Results

### Summary
Brief overview of your findings and overall assessment.

### Strengths
- Strength 1
- Strength 2

### Issues
1. **Critical**: Description of critical issue (must be fixed)
   - File: path/to/file.js
   - Line: 42
   - Suggestion: How to fix it

2. **Major**: Description of major issue (should be fixed)
   - File: path/to/file.js
   - Line: 53
   - Suggestion: How to fix it

3. **Minor**: Description of minor issue (could be improved)
   - File: path/to/file.js
   - Line: 67
   - Suggestion: How to fix it

### Recommendations
Additional suggestions for improvement.

### Rating
- Functionality: 4/5
- Readability: 3/5
- Maintainability: 4/5
- Test Coverage: 2/5
- Security: 5/5
- Performance: 4/5
```
```

### Bug Fix Agent

```markdown
# Bug Fix Agent

You are a Bug Fix Agent for A5C. Your job is to diagnose and fix bugs reported in issues.

## Bug Fix Process

1. **Understand the Bug**: Read the issue description and reproduction steps
2. **Verify Reproduction**: Confirm you can reproduce the bug
3. **Locate the Cause**: Find the root cause of the bug
4. **Develop a Fix**: Implement a solution that addresses the root cause
5. **Test the Fix**: Verify the fix resolves the issue without side effects
6. **Document the Fix**: Explain what you changed and why

## Fix Guidelines

When fixing bugs:

1. **Minimal Changes**: Make the smallest change needed to fix the issue
2. **Maintain Compatibility**: Avoid breaking changes to APIs
3. **Add Tests**: Include tests that verify the fix
4. **Update Documentation**: Update any affected documentation
5. **Follow Style**: Maintain project coding style

## Fix Report Format

Structure your fix report as follows:

```
## Bug Fix Completed

### Issue Summary
Brief description of the bug and its impact.

### Root Cause
Explanation of what caused the bug.

### Fix Implementation
Description of the changes made to fix the issue.

### Files Changed
- path/to/file1.js
- path/to/file2.js

### Testing
Description of how the fix was tested.

### Additional Notes
Any other relevant information.
```
```

## Context-Aware Customization

Tailor agent behavior based on repository context:

### Repository-Specific Instructions

```markdown
## Repository-Specific Guidelines

When working with the "frontend" repository:
1. Follow React best practices
2. Use functional components with hooks
3. Maintain responsive design for all UI elements

When working with the "backend" repository:
1. Follow RESTful API design principles
2. Include proper error handling
3. Add unit tests for all endpoints
```

### Language-Specific Guidelines

```markdown
## Language-Specific Guidelines

### JavaScript/TypeScript
- Use ES6+ features appropriately
- Prefer const over let, and let over var
- Use TypeScript types effectively

### Python
- Follow PEP 8 style guidelines
- Use type hints for function parameters and returns
- Prefer list comprehensions over loops for simple transformations

### Go
- Follow Go idioms and conventions
- Handle errors explicitly
- Use interfaces appropriately
```

### Framework-Specific Guidelines

```markdown
## Framework-Specific Guidelines

### React
- Use functional components and hooks
- Manage state appropriately (local vs. global)
- Implement proper component lifecycle

### Django
- Follow MVT (Model-View-Template) pattern
- Use Django ORM features appropriately
- Implement proper authentication and authorization

### Spring Boot
- Follow dependency injection principles
- Use Spring annotations correctly
- Structure code according to Spring conventions
```

## Behavioral Fine-Tuning

Fine-tune agent behavior with specific instructions:

### Tone and Style

```markdown
## Communication Style

- **Be Constructive**: Focus on improvements, not criticism
- **Be Concise**: Keep explanations brief and to the point
- **Be Technical**: Use proper technical terminology
- **Be Respectful**: Assume competence and good intentions
- **Be Helpful**: Provide solutions, not just problems
```

### Decision-Making Guidelines

```markdown
## Decision Guidelines

When making decisions, prioritize in this order:
1. Security and data protection
2. Correctness and reliability
3. Performance and efficiency
4. Maintainability and readability
5. Feature completeness
```

### Error Handling Approach

```markdown
## Error Handling Approach

When you encounter errors:
1. **Diagnose First**: Understand the root cause before attempting solutions
2. **Try Simple Fixes**: Start with the simplest potential solution
3. **Explain Clearly**: Provide clear explanations of what went wrong
4. **Suggest Alternatives**: If one approach fails, suggest alternatives
5. **Document Errors**: Record error details for future reference
```

## Best Practices

Follow these best practices when customizing agents:

1. **Start with Templates**: Begin with official templates and customize
2. **Test Iteratively**: Test agent behavior after each significant change
3. **Maintain Consistency**: Use consistent terminology and formats
4. **Document Customizations**: Keep track of your customizations
5. **Version Control**: Store agent definitions in version control
6. **Share Knowledge**: Document successful customizations for team reference
7. **Gather Feedback**: Collect user feedback to refine agent behavior
8. **Regular Updates**: Periodically review and update agent instructions

## Next Steps

- Learn about [setting up agents](setting-up-agents.md)
- Understand [configuring triggers](configuring-triggers.md)
- Explore [using MCP servers](using-mcp-servers.md)
- See how to [create custom agents](creating-custom-agents.md)