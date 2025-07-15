# Interactive Documentation Templates

This guide provides ready-to-use templates for common documentation workflows with A5C agents. These templates can be copied directly into GitHub issues, pull requests, or commit messages to trigger specific documentation tasks.

## Agent Selection Guide

Before using these templates, determine which agent is best suited for your task:

| Agent | Best For | Examples |
|-------|----------|----------|
| `content-writer-agent` | Creating and updating documentation content | New guides, updates to existing content |
| `researcher-agent` | Gathering information and research | Topic research, best practices research |
| `validator-agent` | Reviewing and validating documentation | Quality checks, technical validation |
| `developer-agent` | Technical documentation and code examples | API documentation, code samples |
| `build-fixer-agent` | Fixing documentation build issues | Broken links, formatting problems |

## New Documentation Templates

### Create New Concept Page

```markdown
@content-writer-agent

Please create a new concept page explaining [CONCEPT NAME].

Requirements:
- Title: [CONCEPT NAME]
- Location: concepts/[filename].md
- Target audience: [AUDIENCE LEVEL]

This concept page should cover:
- Definition and purpose of [CONCEPT]
- Key components and how they work together
- Benefits and use cases
- Relationship to other A5C concepts
- Diagrams or visualizations where helpful

Reference materials:
- Related existing documentation: [LINKS]
- Technical specifications: [LINKS/FILES]
- Example implementations: [LINKS/FILES]
```

### Create New How-To Guide

```markdown
@content-writer-agent

Please create a new how-to guide for [TASK].

Requirements:
- Title: [GUIDE TITLE]
- Location: guides/[filename].md
- Target audience: [AUDIENCE LEVEL]

This guide should include:
- Prerequisites and requirements
- Step-by-step instructions with code examples
- Configuration options with explanations
- Common errors and troubleshooting
- Next steps and related guides

The guide should follow our style guidelines in CLAUDE.md and be written for [AUDIENCE LEVEL] users.

Reference materials:
- Related guides: [LINKS]
- API documentation: [LINKS]
- Example implementation: [LINKS/FILES]
```

### Create New Tutorial

```markdown
@content-writer-agent

Please create a new tutorial for [TUTORIAL TOPIC].

Requirements:
- Title: [TUTORIAL TITLE]
- Location: tutorials/[filename].md
- Target audience: [AUDIENCE LEVEL]
- Estimated completion time: [TIME]

This tutorial should guide users through:
- Initial setup and prerequisites
- Step 1: [DESCRIPTION]
- Step 2: [DESCRIPTION]
- ...
- Step N: [DESCRIPTION]
- Verification of successful completion
- Next steps and advanced topics

Include complete code examples and expected outputs for each step.

Reference materials:
- Related concepts: [LINKS]
- API documentation: [LINKS]
- Example project: [LINKS/FILES]
```

## Documentation Update Templates

### Update Existing Documentation

```markdown
@content-writer-agent

Please update the [DOCUMENT TYPE] at [FILE PATH] to include:

- [NEW SECTION/CONTENT 1]
  * [DETAILS]
  * [EXAMPLES]
- [NEW SECTION/CONTENT 2]
  * [DETAILS]
  * [EXAMPLES]
- Update [EXISTING SECTION] to reflect [CHANGES]
- [ADDITIONAL UPDATES]

Please maintain the current structure and style while ensuring the content is accessible to [AUDIENCE LEVEL] users.

Reference materials:
- Related documentation: [LINKS]
- Technical specifications: [LINKS/FILES]
- Example implementations: [LINKS/FILES]
```

### Add Examples to Existing Documentation

```markdown
@developer-agent

Please add code examples to the [DOCUMENT TYPE] at [FILE PATH].

Requirements:
- Add examples for the following scenarios:
  * [SCENARIO 1]: [DESCRIPTION]
  * [SCENARIO 2]: [DESCRIPTION]
  * [SCENARIO 3]: [DESCRIPTION]
- Each example should include:
  * Context and purpose
  * Complete, working code
  * Expected output or result
  * Key points highlighted in comments
- Language/format: [LANGUAGE]
- Follow code style guidelines in CLAUDE.md

Reference implementation:
- [LINK TO REFERENCE CODE]
```

## Research Templates

### Research for Documentation Planning

```markdown
@researcher-agent

Please research [TOPIC] to inform our upcoming documentation.

I need information on:
- Current best practices for [ASPECT 1]
- Industry standards for [ASPECT 2]
- Examples of well-implemented [TOPIC] in:
  * [EXAMPLE 1]
  * [EXAMPLE 2]
  * [EXAMPLE 3]
- Common challenges and solutions
- Emerging trends in [TOPIC]

This research will inform our upcoming [DOCUMENT TYPE] on [DOCUMENT TOPIC].

Please organize your findings with clear headings and include links to all sources.
```

### Technical Research for Accuracy

```markdown
@researcher-agent

Please research the technical details of [TECHNICAL TOPIC] for documentation accuracy.

Specifically, I need to understand:
- Exact API parameters and their formats
- Performance considerations and limits
- Security implications
- Version-specific differences
- Common implementation patterns

This information will be used to update our [DOCUMENT TYPE] on [DOCUMENT TOPIC].

Please include code examples where helpful and cite authoritative sources.
```

## Review Templates

### Documentation Quality Review

```markdown
@validator-agent

Please review [DOCUMENT PATH] for quality and compliance with our standards.

Check for:
- Adherence to style guidelines in CLAUDE.md
- Consistency with existing documentation
- Completeness of coverage
- Clarity and accessibility for [AUDIENCE LEVEL]
- Appropriate use of examples and code samples
- Correct formatting and structure
- Valid links and references

Please provide specific suggestions for improvement rather than general feedback.
```

### Technical Accuracy Review

```markdown
@developer-agent

Please review the technical accuracy of [DOCUMENT PATH].

Specifically verify:
- Correctness of API references and parameters
- Validity of code examples (do they work as described?)
- Accuracy of configuration options and their effects
- Completeness of error handling and edge cases
- Correctness of architectural descriptions
- Accuracy of performance and scaling information

If you find inaccuracies, please suggest specific corrections.
```

## Documentation Fix Templates

### Fix Broken Documentation Links

```markdown
@build-fixer-agent

Please fix broken links in our documentation:

The following broken links were identified:
- In [FILE PATH 1], lines [LINE NUMBERS]: [ERROR DETAILS]
- In [FILE PATH 2], lines [LINE NUMBERS]: [ERROR DETAILS]
- In [FILE PATH 3], lines [LINE NUMBERS]: [ERROR DETAILS]

Please correct these links while preserving the intended references.

Build log with errors:
```

### Fix Documentation Formatting Issues

```markdown
@build-fixer-agent

Please fix formatting issues in our documentation:

The following formatting problems were identified:
- In [FILE PATH 1], lines [LINE NUMBERS]: [ISSUE DETAILS]
- In [FILE PATH 2], lines [LINE NUMBERS]: [ISSUE DETAILS]
- In [FILE PATH 3], lines [LINE NUMBERS]: [ISSUE DETAILS]

Please correct these formatting issues while preserving the content and structure.

Build log with errors:
```

## Collaborative Workflows

### Sequential Multi-Agent Workflow

```markdown
@researcher-agent

Please research [TOPIC] focusing on:
- [ASPECT 1]
- [ASPECT 2]
- [ASPECT 3]

Once complete, please notify @content-writer-agent to create a new [DOCUMENT TYPE] based on your findings.

@content-writer-agent, after creating the document, please notify @validator-agent to review it.

@validator-agent, after your review, please either:
1. Approve the document if it meets our standards
2. Request specific changes from @content-writer-agent
```

### Parallel Multi-Agent Workflow

```markdown
@researcher-agent

Please research the technical details of [TOPIC] for our documentation, focusing on implementation details and best practices.

@developer-agent

Please develop code examples for [TOPIC] that demonstrate:
- Basic implementation
- Advanced features
- Error handling
- Performance optimization

@content-writer-agent

Using the research from @researcher-agent and code examples from @developer-agent, please create a comprehensive guide for [TOPIC].
```

## Customizing Templates

These templates are starting points. Customize them by:

1. **Adding specific requirements** for your documentation needs
2. **Adjusting the technical depth** based on your audience
3. **Including additional sections** relevant to your project
4. **Specifying formatting requirements** based on your documentation system
5. **Adding context** about how this document fits into your overall documentation

## Best Practices for Using Templates

1. **Be specific** about requirements and expectations
2. **Include relevant references** to existing documentation
3. **Specify the audience** clearly to get appropriate tone and technical depth
4. **Provide examples** of similar documentation you like
5. **Include key information** that must be covered
6. **Set clear success criteria** for the documentation task

## Next Steps

- Learn about [Documentation Quality Standards](documentation-quality-standards.md)
- Explore [Advanced Content Creation Workflows](advanced-content-workflows.md)
- See [Agent Collaboration Patterns](agent-collaboration-patterns.md) for complex documentation projects