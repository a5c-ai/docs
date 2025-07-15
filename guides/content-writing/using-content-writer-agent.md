# Using the Content Writer Agent

The content-writer-agent helps transform technical information into clear, engaging documentation. This guide explains how to effectively use this agent to improve your project's documentation.

## What is the Content Writer Agent?

The content-writer-agent is a specialized AI agent that excels at:

- Translating complex technical concepts into accessible language
- Creating consistent, well-structured documentation
- Adapting content for different audiences and formats
- Ensuring documentation follows project style guidelines
- Optimizing content for readability and discoverability

## When to Use the Content Writer Agent

Use the content-writer-agent when you need to:

- Create new documentation for features or processes
- Improve existing technical documentation
- Update documentation after code changes
- Ensure consistent style across documentation
- Generate README files, guides, or tutorials
- Prepare release notes or changelog entries
- Create user-facing help content

## Setting Up the Content Writer Agent

### Basic Setup

1. Ensure you have the content-writer-agent in your `.a5c/agents` directory
2. Configure the agent in your main configuration file:

```yaml
# .a5c/config.yml
agents:
  content-writer-agent:
    enabled: true
    template_directory: .a5c/templates/content/
    style_guide_path: .a5c/style-guide.md
    glossary_path: .a5c/glossary.md
```

### Optional Configuration

For advanced usage, configure these additional options:

```yaml
# .a5c/config.yml
agents:
  content-writer-agent:
    # Basic options from above, plus:
    max_content_length: 10000
    default_format: markdown
    audience_types:
      - technical
      - non-technical
      - mixed
    output_formats:
      - markdown
      - rst
      - html
```

### Creating Style Guidelines

For consistent documentation, create a style guide:

1. Create a `.a5c/style-guide.md` file
2. Include guidelines for:
   - Voice and tone
   - Terminology and glossary
   - Formatting conventions
   - Document structure
   - Example usage

Example style guide:

```markdown
# Documentation Style Guide

## Voice and Tone
- Use active voice
- Write in second person ("you")
- Be concise and direct
- Maintain a professional but approachable tone

## Terminology
- Use consistent terms for key concepts
- Define acronyms on first use
- Link to glossary for technical terms

## Formatting
- Use ATX-style headers
- Limit paragraph length to 3-5 sentences
- Use code blocks with syntax highlighting
- Include examples for complex concepts
```

## Triggering the Content Writer Agent

### Manual Triggering

You can manually trigger the content-writer-agent using:

1. **Direct Mention**: Mention the agent in issues, pull requests, or comments:
   ```
   @content-writer Please create documentation for our new authentication system
   ```

2. **CLI Command**: Use the A5C CLI:
   ```bash
   a5c run content-writer-agent --task "Update API documentation"
   ```

### Automatic Triggering

Configure triggers to automatically activate the agent:

1. **File Change Triggers**: Activate when code files change that might need documentation updates:
   ```yaml
   # .a5c/triggers/docs-update.yml
   name: docs-update-trigger
   agent: content-writer-agent
   events: ["push"]
   paths: 
     - "src/**/*.js"
     - "src/**/*.ts"
   conditions:
     files_match: "src/api/*"
   ```

2. **Issue Label Triggers**: Activate when issues are labeled for documentation:
   ```yaml
   # .a5c/triggers/docs-request.yml
   name: docs-request-trigger
   agent: content-writer-agent
   events: ["issues.labeled"]
   conditions:
     labels_include: "documentation-needed"
   ```

3. **Schedule-based Triggers**: Regularly review and update documentation:
   ```yaml
   # .a5c/triggers/docs-refresh.yml
   name: docs-refresh-trigger
   agent: content-writer-agent
   schedule: "0 0 * * 1"  # Run weekly on Mondays
   ```

## Working with the Content Writer Agent

### Providing Clear Instructions

When working with the content-writer-agent, provide clear instructions:

1. **Specify the audience**:
   ```
   @content-writer Create API documentation for our authentication endpoints. Audience: technical developers familiar with REST APIs.
   ```

2. **Define the scope**:
   ```
   @content-writer Update the installation guide to include the new Docker setup. Focus only on the Docker installation method.
   ```

3. **Provide context**:
   ```
   @content-writer Our users are confused about the configuration options. Please revise the configuration.md file to be more clear about required vs optional settings.
   ```

### Task Types

The content-writer-agent excels at various documentation tasks:

1. **New Documentation**:
   ```
   @content-writer Create documentation for the new file upload feature
   ```

2. **Documentation Updates**:
   ```
   @content-writer Update the authentication docs to reflect the new OAuth2 integration
   ```

3. **Content Review**:
   ```
   @content-writer Review README.md for clarity and consistency with our style guide
   ```

4. **Format Conversion**:
   ```
   @content-writer Convert our Markdown installation guide to reStructuredText
   ```

### Providing Templates

Create documentation templates for consistent output:

1. Create template files in your `.a5c/templates/content/` directory
2. Reference templates when triggering the agent:
   ```
   @content-writer Create API documentation for the user endpoints using the api-template
   ```

Example API documentation template:

```markdown
# {{endpoint_name}} API

## Overview

{{overview_description}}

## Endpoints

### {{http_method}} {{endpoint_path}}

**Description**: {{endpoint_description}}

**Parameters**:

| Name | Type | Required | Description |
|------|------|----------|-------------|
{{#each parameters}}
| {{name}} | {{type}} | {{required}} | {{description}} |
{{/each}}

**Response**:

```json
{{example_response}}
```

**Status Codes**:

| Code | Description |
|------|-------------|
{{#each status_codes}}
| {{code}} | {{description}} |
{{/each}}
```

## Reviewing and Improving Content

After the content-writer-agent generates documentation:

1. **Review for accuracy**: Verify technical details are correct
2. **Check completeness**: Ensure all necessary information is included
3. **Verify style consistency**: Confirm the content follows style guidelines
4. **Provide feedback**: Give the agent feedback for future improvements

To request revisions:
```
@content-writer Please revise the authentication docs to include more examples of token usage
```

## Integrating with Development Workflow

### Continuous Documentation

Integrate the content-writer-agent into your development workflow:

1. **Code Change Triggers**: When code changes, trigger documentation updates
2. **PR Reviews**: Have the agent review PRs for documentation needs
3. **Release Notes**: Generate release notes before each release

Example workflow integration:

```yaml
# .github/workflows/docs-update.yml
name: Update Documentation
on:
  pull_request:
    types: [closed]
    branches: [main]
jobs:
  update-docs:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run A5C
        uses: a5c-ai/github-action@v1
        with:
          agent: content-writer-agent
          task: "Update documentation based on recent changes"
```

### Collaborative Documentation

Use the content-writer-agent collaboratively:

1. **Draft Generation**: Have the agent create initial drafts
2. **Human Review**: Technical team reviews for accuracy
3. **Agent Refinement**: Agent refines based on feedback
4. **Final Approval**: Human approves the final version

## Best Practices

### DO:

- Provide clear, specific instructions
- Include relevant context and background
- Specify target audience and purpose
- Review generated content for accuracy
- Give feedback to improve future results

### DON'T:

- Expect perfect output without review
- Provide vague or ambiguous instructions
- Forget to specify technical constraints
- Skip final human review of critical documentation
- Assume the agent knows all project-specific terminology

## Troubleshooting

### Common Issues

| Issue | Possible Cause | Solution |
|-------|----------------|----------|
| Content too technical | Audience not specified | Explicitly specify audience level |
| Missing information | Incomplete context | Provide necessary background information |
| Style inconsistencies | No style guide | Create and reference a style guide |
| Incorrect terminology | Missing glossary | Create a project glossary file |
| Output too long/short | No length guidance | Specify desired content length |

### Getting Help

If you encounter issues with the content-writer-agent:

1. Check the agent logs: `a5c logs content-writer-agent`
2. Verify your configuration is correct
3. Update to the latest A5C version
4. Check for known issues in the repository

## Next Steps

- Learn about [creating custom documentation templates](../custom-templates.md)
- Explore [integrating documentation with CI/CD](../ci-cd-integration.md)
- See [agent collaboration patterns](../../concepts/agent-discovery.md) for multi-agent workflows