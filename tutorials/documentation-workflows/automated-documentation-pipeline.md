# Building an Automated Documentation Pipeline

This tutorial guides you through setting up an end-to-end documentation pipeline using the A5C content-writer-agent. You'll create a fully automated system that keeps your documentation in sync with code changes.

## Learning Objectives

By the end of this tutorial, you'll know how to:

- Configure the content-writer-agent for your project
- Set up automated documentation triggers
- Create a documentation review process
- Implement a continuous documentation strategy
- Integrate documentation with your code review process

## Prerequisites

Before you start, you need:

- A GitHub repository with A5C installed
- Basic understanding of GitHub Actions
- Familiarity with Markdown or reStructuredText
- Access to configure repository settings

## Step 1: Configure the Content Writer Agent

First, set up the content-writer-agent with custom settings for your project.

1. Create the agent configuration directory:

```bash
mkdir -p .a5c/agents
```

2. Create a content writer agent definition file:

```bash
touch .a5c/agents/content-writer.agent.md
```

3. Add the following configuration to the file:

```markdown
---
name: content-writer-agent
version: 1.0.0
category: communication
description: Creates and refines documentation, READMEs, and other content

# Usage Context
usage_context: |
  Use this agent for creating and updating documentation, READMEs,
  API references, and other technical content.

# Execution Configuration
model: claude-3-7-sonnet-20250219
max_turns: 20
timeout: 300
verbose: false

# Trigger Configuration
events: ["push", "pull_request", "issues.labeled"]
mentions: "@content-writer,@docs"
labels: "documentation,docs-needed,update-docs"
branches: "main,develop"
paths: 
  - "docs/**/*"
  - "src/**/*.js"
  - "src/**/*.ts"
  - "**/*.md"

# MCP Server Configuration
mcp_servers: ["filesystem", "github", "memory"]

# Additional Configuration
template_directory: .a5c/templates/content/
style_guide_path: .a5c/style-guide.md
glossary_path: .a5c/glossary.md
---

# Content Writer Agent

You are a Content Writer Agent, part of the A5C agent system. Your primary role is to create and maintain high-quality documentation for software projects.

## Core Responsibilities

1. **Technical Documentation**: Create clear, accurate technical documentation
2. **Content Refinement**: Improve existing documentation for clarity and completeness
3. **Style Consistency**: Ensure all content follows the project's style guidelines
4. **Audience Adaptation**: Adjust content for different technical levels and purposes

## Content Creation Guidelines

When creating or updating documentation:

1. **Understand the subject matter** by analyzing code, comments, and existing documentation
2. **Follow the project's documentation structure and style guide**
3. **Include relevant examples, diagrams, and explanations**
4. **Consider different user personas** (beginners, experts, administrators)
5. **Cross-reference related documentation** when appropriate
6. **Ensure technical accuracy** while maintaining readability

## Documentation Types

You should be capable of creating various types of documentation:

- **User Guides**: End-user focused instructions
- **API References**: Technical details of interfaces and methods
- **Tutorials**: Step-by-step instructions for specific tasks
- **Conceptual Guides**: Explanations of system concepts and architecture
- **READMEs**: Project overviews and quick-start guides
- **Change Logs**: Summaries of changes between versions

## Collaboration Guidelines

When working with developers and other agents:

1. **Ask clarifying questions** when requirements are unclear
2. **Suggest improvements** to existing documentation structure
3. **Request technical review** for accuracy
4. **Acknowledge feedback** and incorporate it into revisions

Always maintain a helpful, professional tone, and prioritize clarity and accuracy above all else.
```

4. Create a style guide for documentation:

```bash
mkdir -p .a5c/templates/content
touch .a5c/style-guide.md
```

5. Add style guidelines to the file:

```markdown
# Documentation Style Guide

## Voice and Tone

- Use an active, direct voice
- Write in second person ("you") when addressing the reader
- Maintain a professional but approachable tone
- Be concise and focused

## Document Structure

- Start with a clear purpose statement
- Use consistent heading hierarchy (# for title, ## for sections)
- Include a table of contents for documents longer than 3 sections
- End with next steps or related resources

## Formatting

- Use ATX-style headers (`#` for titles, `##` for sections)
- Keep paragraphs short (3-5 sentences maximum)
- Use bullet points for lists of items
- Use numbered lists for sequential steps
- Include code blocks with appropriate syntax highlighting

## Code Examples

- Provide complete, working examples
- Include comments to explain key points
- Show expected output when relevant
- Use consistent naming conventions in examples

## Terminology

- Define acronyms on first use
- Use consistent terminology throughout
- Link to glossary entries for technical terms
- Avoid jargon and slang

## Images and Diagrams

- Include descriptive alt text
- Keep file sizes reasonable
- Use consistent styling
- Place diagrams immediately after their introduction
```

## Step 2: Create Documentation Templates

Next, create templates for different documentation types.

1. Create template files:

```bash
touch .a5c/templates/content/api-reference.md
touch .a5c/templates/content/tutorial.md
touch .a5c/templates/content/user-guide.md
```

2. Create an API reference template:

```markdown
# {{api_name}} Reference

## Overview

{{overview_description}}

## Base URL

```
{{base_url}}
```

## Authentication

{{authentication_description}}

## Rate Limiting

{{rate_limiting_description}}

## Endpoints

{{#each endpoints}}
### {{http_method}} {{path}}

**Description**: {{description}}

**Parameters**:

| Name | Type | Required | Description |
|------|------|----------|-------------|
{{#each parameters}}
| {{name}} | {{type}} | {{required}} | {{description}} |
{{/each}}

**Example Request**:

```bash
{{example_request}}
```

**Example Response**:

```json
{{example_response}}
```

**Status Codes**:

| Code | Description |
|------|-------------|
{{#each status_codes}}
| {{code}} | {{description}} |
{{/each}}

{{/each}}

## Error Handling

{{error_handling_description}}

## SDK Examples

{{#each sdk_examples}}
### {{language}}

```{{language}}
{{code}}
```
{{/each}}
```

3. Create a tutorial template:

```markdown
# {{tutorial_title}}

## Overview

{{overview_description}}

## Learning Objectives

By the end of this tutorial, you'll know how to:
{{#each learning_objectives}}
- {{this}}
{{/each}}

## Prerequisites

Before you start, you need:
{{#each prerequisites}}
- {{this}}
{{/each}}

## Step 1: {{step_1_title}}

{{step_1_description}}

```
{{step_1_code}}
```

## Step 2: {{step_2_title}}

{{step_2_description}}

```
{{step_2_code}}
```

## Step 3: {{step_3_title}}

{{step_3_description}}

```
{{step_3_code}}
```

## Step 4: {{step_4_title}}

{{step_4_description}}

```
{{step_4_code}}
```

## Step 5: {{step_5_title}}

{{step_5_description}}

```
{{step_5_code}}
```

## Next Steps

Now that you've completed this tutorial, you can:
{{#each next_steps}}
- {{this}}
{{/each}}

## Troubleshooting

{{#each troubleshooting_items}}
### {{issue}}

**Problem**: {{problem_description}}

**Solution**: {{solution_description}}
{{/each}}
```

## Step 3: Set Up Automated Documentation Triggers

Now, create triggers to automatically activate the content-writer-agent.

1. Create the triggers directory:

```bash
mkdir -p .a5c/triggers
```

2. Create a trigger for code changes:

```bash
touch .a5c/triggers/code-change-docs.yml
```

3. Add the following configuration:

```yaml
name: code-change-docs
description: Trigger documentation updates when code changes
agent: content-writer-agent
enabled: true
mode: auto

# Trigger on code changes to specific files
events: ["push", "pull_request.opened", "pull_request.synchronized"]
paths:
  - "src/**/*.js"
  - "src/**/*.ts"
  - "lib/**/*.js"
  - "lib/**/*.ts"

# Only trigger if docs might be affected
conditions:
  files_match: "src/api/*|src/core/*"
  commit_message_not_match: "^docs:"

# Additional context for the agent
context:
  task: "Review code changes and update related documentation"
  audience: "developers"
  output_location: "docs/"
```

4. Create a trigger for documentation requests:

```bash
touch .a5c/triggers/docs-request.yml
```

5. Add the following configuration:

```yaml
name: docs-request
description: Trigger documentation creation when requested via issues
agent: content-writer-agent
enabled: true
mode: auto

# Trigger on issue creation or labeling
events: ["issues.opened", "issues.labeled"]

# Only trigger for documentation requests
conditions:
  labels_include: "documentation,docs-needed"
  title_match: "docs|documentation"

# Additional context for the agent
context:
  task: "Create documentation based on issue description"
  audience: "varies by request"
  output_location: "docs/"
```

6. Create a scheduled documentation review trigger:

```bash
touch .a5c/triggers/docs-review.yml
```

7. Add the following configuration:

```yaml
name: docs-review
description: Regularly review and improve documentation
agent: content-writer-agent
enabled: true
mode: auto

# Run weekly on Monday morning
schedule: "0 9 * * 1"

# Focus on the main documentation directory
paths:
  - "docs/**/*.md"
  - "README.md"

# Additional context for the agent
context:
  task: "Review documentation for clarity, completeness, and consistency"
  focus_areas: "getting-started,api-reference,tutorials"
  style_check: true
```

## Step 4: Create a Documentation Review Process

Set up a documentation review workflow involving both the agent and human reviewers.

1. Create a documentation review GitHub workflow:

```bash
mkdir -p .github/workflows
touch .github/workflows/docs-review.yml
```

2. Add the following workflow configuration:

```yaml
name: Documentation Review
on:
  pull_request:
    paths:
      - 'docs/**'
      - '**/*.md'
      - 'README.md'

jobs:
  docs-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Run content-writer-agent review
        uses: a5c-ai/github-action@v1
        with:
          agent: content-writer-agent
          task: "Review documentation changes for style and clarity"
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Run link checker
        uses: gaurav-nelson/github-action-markdown-link-check@v1
        with:
          use-quiet-mode: 'yes'
          folder-path: 'docs'

      - name: Check markdown formatting
        uses: DavidAnson/markdownlint-cli2-action@v9
        with:
          globs: "**/*.md"
```

3. Create a pull request template for documentation changes:

```bash
mkdir -p .github/PULL_REQUEST_TEMPLATE
touch .github/PULL_REQUEST_TEMPLATE/documentation.md
```

4. Add the following template content:

```markdown
## Documentation Change Request

### Description
[Describe the documentation changes you're making]

### Type of Change
- [ ] New documentation
- [ ] Documentation update
- [ ] Bug fix
- [ ] Style improvement
- [ ] Other (please specify)

### Affected Documentation Areas
- [ ] README
- [ ] Installation guides
- [ ] API reference
- [ ] Tutorials
- [ ] Conceptual guides
- [ ] Other (please specify)

### Target Audience
- [ ] Beginners
- [ ] Intermediate users
- [ ] Advanced users
- [ ] All users

### Validation
- [ ] I have verified all technical information is accurate
- [ ] I have checked for broken links
- [ ] I have followed the style guide
- [ ] I have included appropriate examples

### Additional Context
[Add any other context about the documentation changes here]

### Mentions
@content-writer Please review these documentation changes for style and clarity
```

## Step 5: Implement a Continuous Documentation Strategy

Now, set up a strategy to keep documentation synchronized with code changes.

1. Create a documentation configuration file:

```bash
touch .a5c/config.yml
```

2. Add the following configuration:

```yaml
version: "1.0"
project_name: "Your Project Name"

# General settings
settings:
  log_level: info
  default_branch: main
  
# Agent configurations
agents:
  directories:
    - .a5c/agents
  
  # Global agent settings
  defaults:
    model: claude-3-7-sonnet-20250219
    timeout: 300
    max_tokens: 8000
  
  # Agent-specific overrides
  overrides:
    content-writer-agent:
      priority: 70
      model: claude-3-7-sonnet-20250219
      timeout: 600
      max_tokens: 16000
      memory_enabled: true

# Trigger configurations
triggers:
  directories:
    - .a5c/triggers
  
  # Default trigger settings
  defaults:
    mode: auto
    enabled: true

# Documentation-specific settings
documentation:
  primary_directory: docs
  style_guide: .a5c/style-guide.md
  glossary: .a5c/glossary.md
  templates_directory: .a5c/templates/content
  
  # Documentation-code mappings
  code_mappings:
    "src/api/": "docs/api-reference/"
    "src/components/": "docs/components/"
    "src/core/": "docs/core-concepts/"
  
  # Review settings
  review:
    required_approvers: 1
    technical_review_required: true
    style_check_required: true
```

3. Set up a documentation generation workflow that runs on code changes:

```bash
touch .github/workflows/generate-docs.yml
```

4. Add the following workflow configuration:

```yaml
name: Generate Documentation
on:
  push:
    branches:
      - main
    paths:
      - 'src/**'
      - 'lib/**'
      - 'package.json'
  workflow_dispatch:
    inputs:
      force_full_rebuild:
        description: 'Force full documentation rebuild'
        required: false
        default: 'false'

jobs:
  update-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Set up environment
        uses: actions/setup-node@v3
        with:
          node-version: '16'
          
      - name: Install dependencies
        run: npm install

      - name: Determine changed files
        id: changed-files
        uses: tj-actions/changed-files@v35
        with:
          files: |
            src/**
            lib/**
            package.json

      - name: Run A5C content-writer-agent
        uses: a5c-ai/github-action@v1
        with:
          agent: content-writer-agent
          task: "Update documentation based on code changes"
          input: ${{ steps.changed-files.outputs.all_changed_files }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
        if: steps.changed-files.outputs.any_changed == 'true' || github.event.inputs.force_full_rebuild == 'true'

      - name: Commit documentation changes
        uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: "docs: Update documentation based on code changes"
          file_pattern: "docs/**/*.md README.md"
          branch: docs-update
          create_branch: true

      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "docs: Update documentation based on code changes"
          title: "docs: Update documentation based on code changes"
          body: |
            This PR updates documentation based on recent code changes.
            
            Changes were automatically generated by the content-writer-agent.
            
            @technical-reviewer Please review for technical accuracy
          branch: docs-update
          base: main
          labels: documentation,automated-pr
```

## Step 6: Integrate with Your Development Process

Finally, integrate documentation into your development process.

1. Create a documentation checklist for developers:

```bash
touch DOCUMENTATION_CHECKLIST.md
```

2. Add the following content:

```markdown
# Documentation Checklist

Use this checklist when making code changes to ensure documentation stays current.

## For All Changes

- [ ] Check if existing documentation needs updating
- [ ] Add a comment with `@content-writer` mention if documentation needs updating
- [ ] Include JSDoc/TSDoc comments in your code for API documentation

## For New Features

- [ ] Create a new documentation file in the appropriate section
- [ ] Add entry to the relevant index or table of contents
- [ ] Include code examples demonstrating usage
- [ ] Document any configuration options or parameters
- [ ] Add to the changelog for the next release

## For API Changes

- [ ] Update API reference documentation
- [ ] Note any breaking changes prominently
- [ ] Update examples to reflect new API
- [ ] Consider creating a migration guide if needed

## For Bug Fixes

- [ ] Update documentation if the fix changes behavior
- [ ] Consider adding to troubleshooting section if appropriate

## Review Process

- [ ] Run the content-writer-agent to review documentation: `a5c run content-writer-agent --task "Review docs"`
- [ ] Address any style or clarity issues identified
- [ ] Request technical review from a team member
```

3. Update your project's README to include documentation guidelines:

```bash
# Assuming you have a README.md file already
```

4. Add the following section to your README:

```markdown
## Documentation

We use an automated documentation system powered by A5C to keep our documentation up-to-date.

### Documentation Structure

- **Getting Started**: Installation and quick-start guides
- **API Reference**: Complete API documentation
- **Tutorials**: Step-by-step guides for common tasks
- **Concepts**: Explanations of core concepts and architecture
- **Guides**: How-to guides for specific scenarios

### Contributing to Documentation

We welcome documentation improvements! There are several ways to contribute:

1. **Direct edits**: Edit markdown files and submit a PR
2. **Request updates**: File an issue with the "documentation" label
3. **Automated updates**: Add `@content-writer` mention in your comments

All documentation changes are reviewed by both our automated content-writer-agent and human reviewers for quality and accuracy.

See the [DOCUMENTATION_CHECKLIST.md](./DOCUMENTATION_CHECKLIST.md) for our documentation standards.
```

5. Create a documentation contribution guide:

```bash
touch CONTRIBUTING_DOCS.md
```

6. Add the following content:

```markdown
# Contributing to Documentation

Thank you for your interest in improving our documentation! This guide explains how to contribute effectively.

## Ways to Contribute

### 1. Direct Documentation Edits

For simple changes:

1. Fork the repository
2. Make your changes to files in the `docs/` directory
3. Submit a pull request using the documentation PR template
4. Request review from the documentation team

### 2. Request Documentation Updates

If you notice a documentation gap but don't want to write it yourself:

1. Open an issue with the "documentation" label
2. Describe what's missing or incorrect
3. Mention `@content-writer` to alert our documentation agent

### 3. Code with Documentation

When adding or changing code:

1. Include thorough code comments (JSDoc/TSDoc for JavaScript/TypeScript)
2. Mention documentation impact in your PR description
3. Add the "documentation-needed" label if docs need updating

## Documentation Standards

All documentation should:

- Follow our [style guide](.a5c/style-guide.md)
- Include examples for any functionality described
- Consider both beginner and advanced users
- Be technically accurate and up-to-date
- Use consistent terminology (see our [glossary](.a5c/glossary.md))

## Working with the Content Writer Agent

Our `content-writer-agent` can help with documentation tasks:

```
@content-writer Please update the API reference for the authentication endpoints
```

The agent can:

- Create new documentation from templates
- Update existing documentation
- Review documentation for style and clarity
- Suggest improvements to documentation structure

## Review Process

All documentation changes go through:

1. Automated style and clarity review
2. Link checking and validation
3. Technical accuracy review
4. Final approval from a documentation maintainer

## Questions?

If you have questions about documentation, please open an issue with the "documentation-question" label or contact the documentation team.
```

## Step 7: Test Your Documentation Pipeline

Now, test the complete documentation pipeline.

1. Commit all the files you've created:

```bash
git add .
git commit -m "Set up automated documentation pipeline with content-writer-agent"
git push
```

2. Create a test code change that should trigger documentation updates:

```bash
# Create a new API endpoint in your source code
mkdir -p src/api
touch src/api/new-endpoint.js
```

3. Add content to the new file:

```javascript
/**
 * @api {get} /api/users Get all users
 * @apiName GetUsers
 * @apiGroup User
 * @apiVersion 1.0.0
 *
 * @apiDescription Retrieves a list of all users in the system.
 *
 * @apiParam {Number} [limit=20] Maximum number of users to return
 * @apiParam {Number} [offset=0] Number of users to skip
 * @apiParam {String} [sort=created_at] Field to sort by
 * @apiParam {String} [order=desc] Sort order (asc or desc)
 *
 * @apiSuccess {Object[]} users List of user objects
 * @apiSuccess {String} users.id User's unique ID
 * @apiSuccess {String} users.name User's full name
 * @apiSuccess {String} users.email User's email address
 * @apiSuccess {Date} users.created_at When the user was created
 * @apiSuccess {Date} users.updated_at When the user was last updated
 *
 * @apiSuccessExample {json} Success-Response:
 *     HTTP/1.1 200 OK
 *     {
 *       "users": [
 *         {
 *           "id": "123456",
 *           "name": "John Doe",
 *           "email": "john@example.com",
 *           "created_at": "2025-01-01T00:00:00Z",
 *           "updated_at": "2025-01-01T00:00:00Z"
 *         }
 *       ],
 *       "meta": {
 *         "total": 100,
 *         "limit": 20,
 *         "offset": 0
 *       }
 *     }
 *
 * @apiError (404) NotFound The requested resource was not found
 * @apiError (401) Unauthorized Authentication is required
 *
 * @returns {Promise<Object>} The users list response
 */
async function getUsers(req, res) {
  const { limit = 20, offset = 0, sort = 'created_at', order = 'desc' } = req.query;
  
  try {
    const users = await db.users.findAll({
      limit,
      offset,
      order: [[sort, order.toUpperCase()]],
    });
    
    const total = await db.users.count();
    
    return res.json({
      users,
      meta: {
        total,
        limit,
        offset
      }
    });
  } catch (error) {
    console.error('Error fetching users:', error);
    return res.status(500).json({ error: 'Internal server error' });
  }
}

/**
 * @api {get} /api/users/:id Get user by ID
 * @apiName GetUserById
 * @apiGroup User
 * @apiVersion 1.0.0
 *
 * @apiDescription Retrieves a specific user by their ID.
 *
 * @apiParam {String} id User's unique ID
 *
 * @apiSuccess {String} id User's unique ID
 * @apiSuccess {String} name User's full name
 * @apiSuccess {String} email User's email address
 * @apiSuccess {Date} created_at When the user was created
 * @apiSuccess {Date} updated_at When the user was last updated
 *
 * @apiSuccessExample {json} Success-Response:
 *     HTTP/1.1 200 OK
 *     {
 *       "id": "123456",
 *       "name": "John Doe",
 *       "email": "john@example.com",
 *       "created_at": "2025-01-01T00:00:00Z",
 *       "updated_at": "2025-01-01T00:00:00Z"
 *     }
 *
 * @apiError (404) NotFound The requested user was not found
 * @apiError (401) Unauthorized Authentication is required
 *
 * @returns {Promise<Object>} The user object
 */
async function getUserById(req, res) {
  const { id } = req.params;
  
  try {
    const user = await db.users.findByPk(id);
    
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    
    return res.json(user);
  } catch (error) {
    console.error(`Error fetching user ${id}:`, error);
    return res.status(500).json({ error: 'Internal server error' });
  }
}

module.exports = {
  getUsers,
  getUserById
};
```

4. Commit and push the new endpoint:

```bash
git add src/api/new-endpoint.js
git commit -m "feat: Add user API endpoints"
git push
```

5. Verify that the documentation workflow runs and creates a PR with updated documentation.

6. Check that the content-writer-agent has:
   - Created API reference documentation for the new endpoints
   - Formatted the documentation according to your style guide
   - Included all the necessary information from the JSDoc comments

7. Review and merge the documentation PR after verifying its accuracy.

## Next Steps

Now that you have a complete documentation pipeline, consider these next steps:

1. **Expand templates**: Create additional templates for different documentation types
2. **Improve integration**: Connect your documentation to CI/CD systems
3. **Add metrics**: Track documentation coverage and quality
4. **User feedback**: Add mechanisms for users to provide feedback on documentation
5. **Multi-language support**: Set up localization for documentation

By completing this tutorial, you've created a robust documentation system that will:
- Keep documentation synchronized with code changes
- Maintain consistent style and quality
- Reduce manual documentation effort
- Improve the overall documentation experience for your users

For more advanced documentation workflows, see:
- [Advanced Documentation Templates](../advanced-templates.md)
- [Documentation Localization](../localization.md)
- [Documentation Analytics](../documentation-analytics.md)