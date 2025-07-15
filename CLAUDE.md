# A5C Documentation Guidelines

This file contains guidelines for creating effective documentation for the A5C project.

## Do's — What to Prioritize

- **Plan a clear hierarchy**: Separate beginner, intermediate, and advanced sections (e.g., Quick Start, How-To, Reference).
- **Write in plain, active language**: Use second person ("you") and imperative verbs ("Run this command").
- **Include real examples**: Show code blocks, commands, screenshots, or diagrams with expected results.
- **Chunk information**: Break content with headings, bullet lists, tables, and call-outs (Note, Tip, Warning).
- **Cross-link related topics**: Add internal links so users can jump to prerequisites, concepts, or deep dives.
- **Highlight critical info**: Use warnings and tips sparingly to surface must-know constraints or best practices.
- **Maintain consistency**: Follow a style guide for terminology, capitalization, and formatting across all pages.
- **Invite feedback**: Provide "Edit this page" or issue links to keep docs current and accurate.

## Don'ts — Common Pitfalls to Avoid

- **Assume prior knowledge**: Always list prerequisites and define acronyms on first use.
- **Overload beginner material**: Keep Quick Start lean; move edge cases and advanced configs elsewhere.
- **Write walls of text**: Long unbroken paragraphs discourage readers—use whitespace and concise sentences.
- **Mix terminology**: Don't change names for the same concept; inconsistency confuses users.
- **Let docs stagnate**: Out-of-date information erodes trust; update docs with every release.
- **Use slang or jokes**: Humor and colloquialisms often misfire globally; stick to clear, neutral language.

## Document Structure

Documentation should follow this general structure:

1. **Getting Started**
   - Installation
   - Quick Start
   - First Project

2. **Concepts**
   - Agents
   - Triggers
   - Configuration
   - MCP
   - Agent Discovery
   - CLI Integration

3. **Guides (How-To)**
   - Setting Up Agents
   - Configuring Triggers
   - Using MCP Servers
   - Customizing Agent Behavior
   - Troubleshooting

4. **Reference**
   - Configuration Options
   - Agent Registry
   - MCP Servers
   - CLI Tools
   - GitHub Action Configuration

5. **Tutorials**
   - Building a Project from Scratch
   - Adding A5C to Existing Projects
   - Creating Custom Agents
   - Implementing Custom MCP Servers

6. **Architecture**
   - System Overview
   - Components
   - Data Flow
   - Integration Points

7. **Community**
   - Contributing
   - Roadmap
   - Support
   - FAQ

## Style Guide

### Formatting

- Use Markdown or reStructuredText according to the file extension
- Use ATX-style headers (`#` for titles, `##` for sections)
- Use code blocks with syntax highlighting:
  ```yaml
  # Example code block
  key: value
  ```
- Use blockquotes for notes, tips, and warnings:
  > **Note**: This is important information.

### Writing Style

- Write in present tense
- Use active voice
- Use second person ("you") to address the reader
- Keep paragraphs short (3-5 sentences)
- Use bullet points for lists
- Define acronyms and technical terms on first use

### Code Examples

- Provide complete, working examples
- Include comments to explain key points
- Show expected output when relevant
- For long examples, provide links to full code samples

### Images and Diagrams

- Use clear, simple diagrams to illustrate concepts
- Include alt text for accessibility
- Keep file sizes reasonable
- Use consistent visual style across all diagrams

## File Organization

- Use directories to organize content by topic
- Include an index file in each directory
- Use consistent file naming conventions
- Link related content across sections