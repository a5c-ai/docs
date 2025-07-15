# Your First Project

This guide walks you through creating your first project with A5C, from initial setup to completion.

## Prerequisites

Before starting, ensure you have:

- A GitHub account with repository creation permissions
- An Anthropic API key for Claude access
- Basic familiarity with GitHub and git

## Setting Up Your Project

### 1. Create a New Repository

You have two options for creating your project:

#### Option A: Use the Zero-to-Demo Template (Recommended for Beginners)

1. Go to [a5c-ai/zero-to-demo](https://github.com/a5c-ai/zero-to-demo)
2. Click "Use this template"
3. Name your repository (e.g., "my-first-a5c-project")
4. Set visibility as needed (public or private)
5. Click "Create repository from template"

#### Option B: Start from Scratch

1. Create a new repository on GitHub
2. Clone it to your local machine:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
3. Set up the A5C configuration manually:
   ```bash
   mkdir -p .a5c
   mkdir -p .github/workflows
   ```

### 2. Configure A5C

If you used the template, basic configuration is already set up. If you started from scratch:

1. Create `.a5c/config.yml`:
   ```yaml
   version: 1.0.0
   settings:
     model: claude-3-7-sonnet-20250219
     verbose: false
   
   agents:
     remote:
       enabled: true
       sources:
         repositories:
           - uri: "https://github.com/a5c-ai/registry"
             pattern: "agents/development/*.agent.md"
   ```

2. Create `.github/workflows/a5c.yml`:
   ```yaml
   name: A5C Agent System
   on:
     pull_request:
       types: [opened, synchronize]
     issues:
       types: [opened, edited]
     issue_comment:
       types: [created]
     push:
       branches: [main, develop]
   
   jobs:
     run-agents:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
           with:
             fetch-depth: 0
         
         - name: Run A5C Agents
           uses: a5c-ai/action@main
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
             config_file: ".a5c/config.yml"
   ```

### 3. Add Repository Secrets

1. Go to your repository's Settings
2. Select "Secrets and variables" → "Actions"
3. Add the following secrets:
   - `ANTHROPIC_API_KEY`: Your Anthropic API key

## Defining Your Project Requirements

### 1. Update Repository Description

For zero-to-demo template repositories, update your repository description with your project requirements:

> A simple task management API built with Node.js, Express, and MongoDB. Features include user authentication, task CRUD operations, task categorization, and due date management.

### 2. Create Initial Issues (For Manual Setup)

If you're not using the template, create some initial issues to guide development:

1. Create a new issue titled "Project Setup"
   ```
   @project-seeder-agent Please initialize a Node.js Express API project with MongoDB integration for a task management system.
   ```

2. Create a new issue titled "User Authentication"
   ```
   @developer-agent Please implement user registration and login using JWT authentication.
   ```

## Working with Agents

### 1. Issue-Based Development

A5C works best with issue-driven development. Create issues for each feature or task:

```
@developer-agent Please implement the task creation API endpoint with the following fields:
- title (string, required)
- description (string, optional)
- dueDate (date, optional)
- category (string, optional)
- priority (enum: low, medium, high)
- status (enum: todo, in-progress, completed)
```

### 2. Code Reviews

Request code reviews from the code-review agent:

```
@code-review-agent Please review the user authentication implementation in PR #3.
```

### 3. Bug Fixing

Report and fix bugs using the appropriate agents:

```
@bug-fixer-agent The task creation endpoint returns 500 when a task with no due date is submitted. Please investigate and fix.
```

## Implementing a Feature with Agent Assistance

Let's walk through implementing a feature with agent assistance:

### 1. Create an Issue

Create a new issue titled "Task Categories Management":

```
@developer-agent We need to implement task categories management with the following requirements:

1. Users should be able to create, read, update, and delete categories
2. Each category should have:
   - name (unique per user)
   - color (hex color code)
   - description (optional)
3. Tasks should be able to reference categories by ID
4. Categories should be user-specific

Please implement the necessary models, routes, and controllers.
```

### 2. Agent Implementation

The developer agent will:
1. Analyze the requirements
2. Create a new branch
3. Implement the necessary code
4. Create tests
5. Create a pull request

### 3. Review and Merge

1. The code-review agent can be tagged to review the PR
2. After review, merge the PR to complete the feature

## Expanding Your Project

As your project grows:

1. **Add specialized agents**: Include security, testing, or documentation agents
2. **Customize triggers**: Configure agents to respond to specific events or patterns
3. **Create local agents**: Develop custom agents for project-specific tasks
4. **Implement CI/CD**: Use A5C agents to manage deployment and integration

## Troubleshooting

If you encounter issues:

1. **Check GitHub Actions logs**: Review action execution details
2. **Verify agent configuration**: Ensure your config.yml is correct
3. **Check API key validity**: Ensure your Anthropic API key is valid
4. **Review agent mentions**: Make sure you're using the correct agent names

## Next Steps

Now that you've completed your first project with A5C, you can:

- Learn about [advanced agent configuration](../concepts/configuration.md)
- Explore [custom agent creation](../guides/creating-custom-agents.md)
- Understand [MCP server integration](../concepts/mcp.md)
- Set up [advanced triggers](../concepts/triggers.md)

For more detailed guidance, check out the full [A5C documentation](../index.md).