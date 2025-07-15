# Content Creation Workflows

This guide explains how to use A5C agents to streamline content creation workflows for your documentation.

## Prerequisites

Before implementing content creation workflows with A5C, ensure you have:

- A5C configured in your documentation repository
- The content-writer-agent and researcher-agent added to your `.a5c/config.yml`
- GitHub Actions set up for A5C integration

## Common Documentation Workflows

### 1. Creating New Documentation

When you need to create new documentation pages:

1. **Create an issue** with a clear description of the documentation needed
2. **Mention the content-writer-agent** with specific requirements
3. **Review and refine** the generated content
4. **Merge** the changes into your documentation

**Example Issue:**

```
@content-writer-agent

Please create a new guide explaining how to use the CLI integration feature.

Requirements:
- Explain the purpose and benefits of CLI integration
- Include setup instructions for different CLIs
- Provide examples for common use cases
- Include troubleshooting section
```

### 2. Updating Existing Documentation

When documentation needs to be updated:

1. **Create an issue** describing what needs to be updated
2. **Mention the content-writer-agent** with the file path and changes needed
3. **Review** the suggested updates
4. **Merge** the approved changes

**Example Issue:**

```
@content-writer-agent

Please update the installation guide at `/getting-started/installation.md` to include:
- New Docker installation method
- Updated requirements
- New screenshots for the process
```

### 3. Documentation Research

When you need research to support documentation:

1. **Create an issue** with the research topic
2. **Mention the researcher-agent** with specific questions
3. **Use the research** to inform content creation
4. **Create or update** documentation based on the research

**Example Issue:**

```
@researcher-agent

Please research best practices for documenting GraphQL APIs. 
I need information on:
- Standard patterns for GraphQL documentation
- Tools that help generate GraphQL docs
- Examples of well-documented GraphQL projects
```

### 4. Documentation Review

To ensure documentation quality:

1. **Create a pull request** with documentation changes
2. **Mention the validator-agent** in a comment
3. **Address feedback** from the validator
4. **Merge** after validation

**Example PR Comment:**

```
@validator-agent

Please review this documentation for:
- Technical accuracy
- Consistency with style guidelines
- Completeness
- Readability
```

### 5. Documentation Fixes

When documentation has issues:

1. **Create an issue** describing the problems
2. **Mention the build-fixer-agent** for structural issues
3. **Mention the content-writer-agent** for content issues
4. **Verify fixes** before merging

**Example Issue:**

```
@build-fixer-agent

The documentation build is failing due to broken references in the following files:
- guides/agent-workflows.md
- reference/configuration-options.md

Please fix these issues.
```

## Automating Documentation with Triggers

You can automate documentation workflows using A5C triggers:

### Code Change Triggers

Configure your content-writer-agent to automatically update documentation when code changes:

```yaml
# In your content-writer-agent configuration
events: ["push"]
branches: ["main", "develop"]
paths: ["src/**/*.js", "src/**/*.ts"]
```

### Regular Documentation Reviews

Schedule regular documentation reviews:

```yaml
# In your validator-agent configuration
activation_cron: "0 9 * * 1"  # Every Monday at 9 AM
```

### Issue-based Documentation

Automatically generate documentation for features and bug fixes:

```yaml
# In your content-writer-agent configuration
events: ["issues.closed"]
labels: ["needs-docs"]
```

## Best Practices

When implementing documentation workflows with A5C:

1. **Use Clear Issue Templates**: Create issue templates for different documentation needs
2. **Be Specific with Requirements**: Provide detailed requirements for content creation
3. **Implement Structured Review**: Use checklist-based reviews for consistency
4. **Maintain a Style Guide**: Reference your style guide in agent requests
5. **Version Documentation**: Align documentation versions with software releases

## Common Patterns

These patterns have proven effective for documentation workflows:

### Documentation-as-Code

Treat documentation like code with:

- Pull request reviews
- Automated testing (links, formatting)
- Version control
- Release processes

### Progressive Documentation

Build documentation in layers:

1. **Conceptual Overview**: High-level explanations
2. **Getting Started**: Basic usage
3. **How-To Guides**: Task-oriented guides
4. **Reference**: Comprehensive details
5. **Examples**: Real-world applications

### Living Documentation

Keep documentation current with:

- Regular automated reviews
- Deprecation notices
- Version indicators
- "Last updated" timestamps

## Troubleshooting

Common issues and solutions for A5C documentation workflows:

### Agents Not Responding

If agents aren't responding to mentions:

- Check your `.a5c/config.yml` file for correct agent configuration
- Verify GitHub Actions is running correctly
- Check for error messages in the Actions logs

### Content Quality Issues

If content quality is inconsistent:

- Create a more detailed style guide
- Use the validator-agent more frequently
- Provide more specific requirements in your requests

### Build Problems

If documentation fails to build:

- Use the build-fixer-agent to diagnose and fix issues
- Check for syntax errors in Markdown or reStructuredText
- Verify that all references and links are valid

## Next Steps

- Explore [customizing agent behavior](customizing-agent-behavior.md) for documentation
- Learn about [A5C Integration with CI/CD](ci-cd-integration.md)
- See how to [create custom agents](../tutorials/creating-custom-agents.md) for specialized documentation needs