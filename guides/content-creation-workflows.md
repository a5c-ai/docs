# Content Creation Workflows

This guide explains how to use A5C agents to streamline content creation workflows for your documentation.

## Prerequisites

Before implementing content creation workflows with A5C, ensure you have:

- A5C configured in your documentation repository
- The content-writer-agent and researcher-agent added to your `.a5c/config.yml`
- GitHub Actions set up for A5C integration
- A clear understanding of your documentation structure and style guidelines

## Common Documentation Workflows

### 1. Creating New Documentation

When you need to create new documentation pages:

1. **Create an issue** with a clear description of the documentation needed
2. **Mention the content-writer-agent** with specific requirements
3. **Review and refine** the generated content
4. **Merge** the changes into your documentation

**Example Issue:**

```markdown
@content-writer-agent

Please create a new guide explaining how to use the CLI integration feature.

Requirements:
- Explain the purpose and benefits of CLI integration
- Include setup instructions for different CLIs (Bash, PowerShell, Zsh)
- Provide examples for common use cases:
  * Basic command execution
  * Configuration management
  * Pipeline integration
- Include troubleshooting section addressing common errors
- Target audience: Developers with basic CLI familiarity

Reference materials:
- API documentation: /reference/cli-tools.md
- Existing examples: /tutorials/first-project.md (CLI section)
```

### 2. Updating Existing Documentation

When documentation needs to be updated:

1. **Create an issue** describing what needs to be updated
2. **Mention the content-writer-agent** with the file path and changes needed
3. **Review** the suggested updates
4. **Merge** the approved changes

**Example Issue:**

```markdown
@content-writer-agent

Please update the installation guide at `/getting-started/installation.md` to include:

- New Docker installation method:
  * Docker Hub repository: a5c-ai/a5c-core
  * Required environment variables and volume mounts
  * Resource recommendations
- Updated system requirements:
  * Node.js v16+ (previously v14+)
  * Python 3.8+ (previously 3.6+)
  * 4GB RAM minimum (previously 2GB)
- Add section on cloud-based installation options
- Update screenshots to reflect the new UI (v2.3)

Please maintain the current structure and style while ensuring the content is accessible to beginners.
```

### 3. Documentation Research

When you need research to support documentation:

1. **Create an issue** with the research topic
2. **Mention the researcher-agent** with specific questions
3. **Use the research** to inform content creation
4. **Create or update** documentation based on the research

**Example Issue:**

```markdown
@researcher-agent

Please research best practices for documenting GraphQL APIs. 

I need information on:
- Standard patterns for GraphQL documentation (schema documentation, query examples, playground integration)
- Tools that help generate GraphQL docs (GraphQL Docs, Spectaql, GraphiQL, etc.)
- Examples of well-documented GraphQL projects (GitHub, Shopify, Apollo)
- Key differences in documenting GraphQL vs REST APIs
- Best practices for documenting mutations and subscriptions

This research will inform our upcoming guide on documenting A5C's GraphQL interfaces.
```

### 4. Documentation Review

To ensure documentation quality:

1. **Create a pull request** with documentation changes
2. **Mention the validator-agent** in a comment
3. **Address feedback** from the validator
4. **Merge** after validation

**Example PR Comment:**

```markdown
@validator-agent

Please review this documentation for:
- Technical accuracy (especially in the configuration section)
- Consistency with our style guidelines (see CLAUDE.md)
- Completeness of the API reference
- Readability for our target audience (junior to mid-level developers)
- Appropriate cross-linking to related documentation
- Effectiveness of code examples

Focus particularly on the authentication section which introduces new concepts.
```

### 5. Documentation Fixes

When documentation has issues:

1. **Create an issue** describing the problems
2. **Mention the build-fixer-agent** for structural issues
3. **Mention the content-writer-agent** for content issues
4. **Verify fixes** before merging

**Example Issue:**

```markdown
@build-fixer-agent

The documentation build is failing due to broken references in the following files:
- guides/agent-workflows.md (lines 54, 67, 92)
- reference/configuration-options.md (lines 128-130)

Error messages from the build log:
- "Unknown reference: :ref:`agent-discovery`"
- "Could not resolve image reference: ../images/workflow-diagram.png"

Please fix these issues while preserving the intended content and connections.
```

## Collaborative Workflows

### 1. Multi-Agent Collaboration

For complex documentation projects, use multiple agents in sequence:

```markdown
@researcher-agent

Please research the latest agent communication protocols for AI systems focusing on:
- Message passing structures
- Event-driven communication
- Asynchronous notification patterns

Once complete, please notify @content-writer-agent to create documentation based on your findings.
```

### 2. Author-Agent Pairing

Work collaboratively with agents to improve your documentation:

1. **Create a draft document** with your initial structure and content
2. **Request assistance** from the content-writer-agent for specific sections
3. **Refine together** through multiple iterations

**Example:**

```markdown
@content-writer-agent

I've created a draft guide for agent configuration at `/guides/draft-agent-config.md`.

Please help improve these specific sections:
1. The "Advanced Configuration" section needs more detailed examples
2. The "Troubleshooting" section needs expanded common error scenarios
3. The introduction needs a more compelling explanation of benefits

Please maintain my existing structure and technical approach while enhancing readability.
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
actions:
  - type: "issue"
    title: "Documentation update needed for code changes"
    body: |
      Recent code changes in the following files may require documentation updates:
      {{changed_files}}
      
      Please review and update the relevant documentation.
    labels: ["documentation", "needs-attention"]
```

### Regular Documentation Reviews

Schedule regular documentation reviews:

```yaml
# In your validator-agent configuration
activation_cron: "0 9 * * 1"  # Every Monday at 9 AM
actions:
  - type: "issue"
    title: "Weekly documentation review: {{date}}"
    body: |
      This is a scheduled weekly documentation review.
      
      Please review the following sections for accuracy and completeness:
      - Recently updated pages
      - Pages without updates in the last 30 days
      - Top 5 most visited documentation pages
    assignees: ["documentation-team"]
    labels: ["documentation", "review"]
```

### Issue-based Documentation

Automatically generate documentation for features and bug fixes:

```yaml
# In your content-writer-agent configuration
events: ["issues.closed"]
labels: ["needs-docs"]
actions:
  - type: "pull_request"
    title: "Documentation: {{issue.title}}"
    body: |
      This PR adds documentation for issue #{{issue.number}}: {{issue.title}}
      
      Key changes:
      - Add documentation for the feature described in the issue
      - Update relevant reference sections
      - Add examples demonstrating the feature
      
      Closes #{{issue.number}}
    branch: "docs/issue-{{issue.number}}"
    base: "main"
```

## Content Planning Strategies

### Documentation Roadmap

Create a documentation roadmap to guide your content creation efforts:

1. **Audit existing documentation** to identify gaps and opportunities
2. **Prioritize documentation needs** based on user feedback and feature importance
3. **Create a timeline** for documentation development
4. **Assign resources** to specific documentation tasks
5. **Track progress** and adjust as needed

Example roadmap structure:

```markdown
# Q3 2025 Documentation Roadmap

## High Priority
- Complete API reference for all endpoints
- Create onboarding guide for new users
- Update deployment guides for v3.0 release

## Medium Priority
- Add advanced tutorials for custom agent creation
- Improve troubleshooting guides with common scenarios
- Create video tutorials for key workflows

## Low Priority
- Refactor examples for consistency
- Add glossary of terms
- Create printable quick reference guides
```

### User-Centered Documentation

Plan your documentation around user journeys:

1. **Identify user personas** (beginner developer, system administrator, advanced user)
2. **Map documentation needs** to each persona
3. **Create documentation pathways** for different user journeys
4. **Test documentation** with representative users
5. **Iterate based on feedback**

## Best Practices

When implementing documentation workflows with A5C:

1. **Use Clear Issue Templates**: Create issue templates for different documentation needs with structured sections for requirements, audience, and expected outcomes
2. **Be Specific with Requirements**: Provide detailed requirements for content creation, including audience, purpose, technical depth, and examples needed
3. **Implement Structured Review**: Use checklist-based reviews for consistency, covering technical accuracy, style compliance, readability, and completeness
4. **Maintain a Style Guide**: Reference your style guide in agent requests and ensure agents understand your documentation standards
5. **Version Documentation**: Align documentation versions with software releases and clearly mark version-specific information
6. **Measure Documentation Effectiveness**: Track user engagement, feedback, and support requests to identify areas for improvement
7. **Create Content Templates**: Develop templates for common documentation types (guide, reference, tutorial) to ensure consistency

## Common Patterns

These patterns have proven effective for documentation workflows:

### Documentation-as-Code

Treat documentation like code with:

- Pull request reviews and approvals
- Automated testing (links, formatting, spelling)
- Version control and branching strategies
- Release processes aligned with software releases
- Continuous integration and deployment

### Progressive Documentation

Build documentation in layers:

1. **Conceptual Overview**: High-level explanations of key concepts and system architecture
2. **Getting Started**: Basic usage instructions for common scenarios
3. **How-To Guides**: Task-oriented guides for specific use cases
4. **Reference**: Comprehensive details of all features and APIs
5. **Examples**: Real-world applications and sample projects
6. **Advanced Topics**: In-depth exploration of complex scenarios and customizations

### Living Documentation

Keep documentation current with:

- Regular automated reviews and update schedules
- Deprecation notices for outdated content
- Version indicators for feature availability
- "Last updated" timestamps and change logs
- User feedback mechanisms on each page
- Analytics to identify popular and problematic pages

## Measuring Documentation Success

Track these metrics to evaluate your documentation effectiveness:

- **User engagement**: Time spent on documentation pages
- **Support ticket reduction**: Decrease in questions covered by documentation
- **Search effectiveness**: Successful search rates in documentation
- **Completion rates**: Users completing tasks after reading documentation
- **User satisfaction**: Feedback ratings on documentation pages
- **Contribution metrics**: Community contributions to documentation

## Troubleshooting

Common issues and solutions for A5C documentation workflows:

### Agents Not Responding

If agents aren't responding to mentions:

- Check your `.a5c/config.yml` file for correct agent configuration
- Verify GitHub Actions is running correctly with sufficient permissions
- Check for error messages in the Actions logs
- Ensure the agent mention format is correct (@agent-name)
- Verify the agent is configured for the event type you're using

### Content Quality Issues

If content quality is inconsistent:

- Create a more detailed style guide with specific examples
- Use the validator-agent more frequently for ongoing quality checks
- Provide more specific requirements in your requests, including audience and purpose
- Develop documentation templates for common content types
- Implement a peer review process for agent-generated content

### Build Problems

If documentation fails to build:

- Use the build-fixer-agent to diagnose and fix issues
- Check for syntax errors in Markdown or reStructuredText
- Verify that all references and links are valid
- Ensure images and other assets are correctly placed and referenced
- Test builds locally before pushing to the repository

### Collaboration Challenges

If coordinating multiple agents is difficult:

- Create clear workflows with defined handoffs between agents
- Use issue comments to track progress and changes
- Set up automation to notify the next agent in sequence
- Document common collaboration patterns for your team
- Use labels to indicate the current status of documentation work

## Next Steps

- Explore [customizing agent behavior](customizing-agent-behavior.md) for documentation
- Learn about [A5C Integration with CI/CD](documentation-ci.md)
- See how to [create custom agents](../tutorials/creating-custom-agents.md) for specialized documentation needs
- Discover [advanced content strategies](../guides/advanced-content-strategies.md) for complex documentation projects