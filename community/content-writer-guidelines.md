# Content Writer Guidelines for A5C Documentation

This guide provides specific instructions for content writers contributing to the A5C documentation, whether you're a human writer or an AI agent like the content-writer-agent.

## Content Writer Responsibilities

As a content writer for A5C documentation, you are responsible for:

1. **Creating clear, accessible documentation** that explains complex technical concepts
2. **Translating technical features** into user-focused benefits and workflows
3. **Maintaining consistency** across the documentation ecosystem
4. **Structuring content** for optimal discoverability and readability
5. **Collaborating with technical teams** to ensure accuracy and completeness

## Understanding Your Audience

A5C documentation serves several distinct audiences:

### Primary Audiences

- **Software Developers**: Implementing A5C in their projects
- **DevOps Engineers**: Setting up and maintaining A5C infrastructure
- **Project Managers**: Understanding A5C capabilities and workflows
- **Technical Writers**: Integrating A5C into documentation processes

### Audience Needs

When writing, address these common audience needs:

- **Conceptual understanding**: How A5C works and its core principles
- **Practical implementation**: Step-by-step guidance for specific tasks
- **Problem-solving**: Troubleshooting common issues
- **Reference material**: Comprehensive details for configuration and APIs
- **Best practices**: Guidance on optimal usage patterns

## Content Types and Purposes

Different content types serve different purposes in the documentation:

### Concept Guides

- **Purpose**: Explain core concepts and principles
- **Style**: Clear explanations with diagrams and metaphors
- **Length**: Typically 500-1500 words
- **Example**: [Agent Discovery](../concepts/agent-discovery.md)

### How-To Guides

- **Purpose**: Provide step-by-step instructions for specific tasks
- **Style**: Procedural, direct, with clear code examples
- **Length**: Typically 1000-2000 words
- **Example**: [Content Creation Workflows](../guides/content-creation-workflows.md)

### Reference Documentation

- **Purpose**: Offer comprehensive technical details
- **Style**: Structured, precise, comprehensive
- **Length**: As long as needed for completeness
- **Example**: [Configuration Options](../reference/configuration-options.md)

### Tutorials

- **Purpose**: Guide users through complete processes from start to finish
- **Style**: Progressive, hands-on, with context and explanation
- **Length**: Typically 2000-5000 words
- **Example**: [Building a Project from Scratch](../tutorials/building-a-project-from-scratch.md)

## Style and Formatting Guidelines

Follow these guidelines to maintain consistency across documentation:

### Voice and Tone

- Use **active voice** whenever possible
- Write in **second person** ("you") to address the reader directly
- Maintain a **professional but conversational** tone
- Be **direct and concise** without being abrupt
- **Avoid humor** as it can be culturally specific and doesn't translate well

### Writing Style

- Use **clear, straightforward language**
- **Define technical terms** on first use
- Break complex concepts into **smaller, digestible chunks**
- Use **parallel structure** in lists and headings
- Include **real-world examples** to illustrate concepts
- **Avoid unnecessary jargon** and explain technical terms when used

### Formatting Conventions

- Use **ATX-style headers** (`#` for titles, `##` for sections)
- Maintain a **consistent heading hierarchy**
- Format **code snippets** with appropriate syntax highlighting
- Use **bold** for emphasis, UI elements, and important terms
- Use **italics** sparingly for introducing new terms
- Use **numbered lists** for sequential steps
- Use **bullet lists** for non-sequential items

### Code Examples

- Provide **complete, working examples** whenever possible
- Include **comments** to explain key concepts
- Use **consistent naming conventions** in examples
- Show **expected output** where helpful
- Follow **language-specific conventions** for syntax and style

## Documentation Structure

When creating or updating documentation, follow this structure:

### Document Template

```markdown
# Title (Clear, Descriptive, Contains Key Terms)

Brief introduction (1-2 paragraphs explaining what this document covers and why it matters)

## Prerequisites (if applicable)

- Required knowledge
- Required software or tools
- Required configuration

## Core Content Sections

### Section 1

Content with examples, code snippets, and explanations

### Section 2

More content with appropriate illustrations, tables, or diagrams

## Best Practices (if applicable)

- Recommended approaches
- Performance considerations
- Security considerations

## Troubleshooting (if applicable)

Common issues and their solutions

## Next Steps

Links to related documentation
```

### Navigation Principles

- **Start with why**: Explain the purpose before diving into details
- **Progressive disclosure**: Present basic information before advanced topics
- **Logical grouping**: Keep related information together
- **Clear signposting**: Use informative headings and subheadings
- **Connected content**: Link to related documentation

## Working with Technical Content

When documenting technical features:

### Technical Accuracy

- **Verify all technical information** with subject matter experts
- **Test all code examples** in a realistic environment
- **Update documentation** when features change
- **Indicate version-specific information** clearly
- **Link to official specifications** when relevant

### Technical Depth

- **Balance detail with accessibility**
- **Layer information** from basic to advanced
- **Provide context** for technical decisions
- **Explain the why** not just the how
- **Include diagrams** for complex systems

## Content Creation Process

Follow this process when creating documentation:

### 1. Planning

- **Define the document purpose** and audience
- **Outline the structure** and key sections
- **Identify required examples** and diagrams
- **Determine integration** with existing content

### 2. Research

- **Gather technical information** from relevant sources
- **Interview subject matter experts** if needed
- **Review existing documentation** for consistency
- **Test features** to understand behavior

### 3. Writing

- **Follow the structure** from the planning phase
- **Write the first draft** focusing on clarity and completeness
- **Include all necessary examples** and explanations
- **Add cross-references** to related documentation

### 4. Review

- **Self-review** for clarity, structure, and style
- **Technical review** for accuracy and completeness
- **Editorial review** for style and consistency
- **User testing** if possible for usability

### 5. Revision

- **Address all feedback** from reviews
- **Improve examples** based on feedback
- **Enhance clarity** where needed
- **Ensure consistency** with other documentation

### 6. Publication

- **Final check** for links and formatting
- **Publish** to the appropriate channel
- **Announce updates** to relevant stakeholders
- **Monitor feedback** for further improvements

## Collaboration Guidelines

When collaborating with other writers and technical teams:

### Working with Developers

- **Ask specific questions** about functionality
- **Request examples** for complex features
- **Verify technical details** before publishing
- **Share drafts early** for technical review

### Working with Other Writers

- **Maintain consistent terminology** across documentation
- **Share templates and patterns** for common content
- **Review each other's work** for consistency
- **Coordinate on cross-linked content**

### Working with A5C Agents

- **Provide clear, specific instructions** in issue templates
- **Include audience and purpose** in your requests
- **Reference style guidelines** explicitly
- **Review agent-generated content** thoroughly
- **Provide feedback** to improve future output

## Quality Checklist

Before submitting documentation, check that it:

- [ ] Addresses the target audience's needs
- [ ] Follows the style and formatting guidelines
- [ ] Contains accurate and verified technical information
- [ ] Includes complete and tested code examples
- [ ] Uses consistent terminology
- [ ] Provides clear structure with informative headings
- [ ] Links to related documentation
- [ ] Covers common troubleshooting scenarios
- [ ] Includes next steps or related information
- [ ] Has been reviewed for technical accuracy

## Resources for Content Writers

- [A5C Documentation Guidelines](../CLAUDE.md)
- [Sphinx Documentation](https://www.sphinx-doc.org/en/master/)
- [Markdown Guide](https://www.markdownguide.org/)
- [A5C Content Creation Workflows](../guides/content-creation-workflows.md)
- [A5C Documentation CI](../guides/documentation-ci.md)

## Content Maintenance

Documentation requires ongoing maintenance:

### Regular Review Cycle

- **Conduct quarterly reviews** of critical documentation
- **Update version-specific information** with each release
- **Refresh examples** to reflect current best practices
- **Address user feedback** continuously

### Deprecation Process

- **Mark deprecated features** clearly
- **Provide migration paths** for deprecated functionality
- **Archive obsolete documentation** appropriately
- **Update navigation** to reflect current priorities

## Contributing Your First Document

To contribute a new document:

1. **Review existing content** to understand the style and structure
2. **Check the documentation roadmap** for priorities
3. **Create an issue** describing your proposed content
4. **Draft your content** following these guidelines
5. **Submit a pull request** for review
6. **Address feedback** from reviewers
7. **Celebrate your contribution** to A5C documentation!

---

By following these guidelines, you'll create documentation that helps users understand and effectively use A5C's powerful capabilities.