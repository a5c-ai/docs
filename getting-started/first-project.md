# Your First Project


This guide walks you through creating your first project with A5C, demonstrating how to set up a simple application with AI agent assistance.

## Prerequisites

Before starting your first A5C project, ensure you have:

- Completed the [Installation](installation.md) process
- A GitHub repository with A5C configured
- Basic understanding of the [Quick Start](quick-start.md) concepts
- An Anthropic API key for Claude access
- Git installed on your local machine

## Project Overview

In this tutorial, we'll build a simple task management API using:

- Node.js and Express for the backend
- A5C agents for development assistance
- GitHub for source control and collaboration

## Step 1: Create a New Repository

1. Create a new GitHub repository:
   - Go to GitHub and click "New repository"
   - Name it "a5c-task-manager" (or choose your own name)
   - Set it to Private or Public
   - Initialize with a README

2. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/a5c-task-manager.git
cd a5c-task-manager
```

## Step 2: Set Up A5C Configuration

1. Create the A5C configuration directory:

```bash
mkdir -p .a5c
```

2. Create a basic `config.yml` file in the `.a5c` directory:

```yaml
# Basic A5C configuration
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

# Agents to use
agents:
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
```

3. Set up the GitHub workflow file:

```bash
mkdir -p .github/workflows
```

4. Create a `.github/workflows/a5c.yml` file:

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

5. Commit and push these files to your repository:

```bash
git add .a5c .github
git commit -m "Set up A5C configuration"
git push
```

6. Add your `ANTHROPIC_API_KEY` to your repository secrets:
   - Go to your repository on GitHub
   - Navigate to Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `ANTHROPIC_API_KEY`
   - Value: Your Anthropic API key
   - Click "Add secret"

## Step 3: Initialize the Project

1. Create a new issue in your repository with the following content:

```
@project-seeder-agent

Please initialize a Node.js Express API project with the following features:
- Express.js for API routes
- Simple in-memory task management (no database needed)
- Basic CRUD operations for tasks (create, read, update, delete)
- Basic structure with routes, controllers, and models
- Jest for testing
```

2. Wait for the project-seeder-agent to respond and initialize your project. This typically takes a few minutes.

3. Once the agent has finished, clone the updated repository:

```bash
git pull
```

## Step 4: Implement a New Feature

Now that you have a basic project structure, let's implement a new feature with agent assistance.

1. Create a new feature branch:

```bash
git checkout -b feature/task-priorities
```

2. Create a new issue in your repository:

```
@developer-agent

Please add a priority field to the task model with the following requirements:
- Priority can be "low", "medium", or "high"
- Default priority should be "medium"
- Add validation to ensure only valid priorities are accepted
- Update relevant controllers and routes to support filtering by priority
- Add tests for the new functionality
```

3. Wait for the developer-agent to provide a solution.

4. Review the agent's solution and implement the changes:
   - Copy the code provided by the agent
   - Create or modify the necessary files
   - Commit your changes

```bash
git add .
git commit -m "Add task priority functionality"
git push --set-upstream origin feature/task-priorities
```

5. Create a pull request:
   - Go to your repository on GitHub
   - Click "Compare & pull request"
   - Add a description of your changes
   - Click "Create pull request"

6. Mention the code-review-agent in a comment on your pull request:

```
@code-review-agent Please review this PR for the task priority implementation.
```

7. Wait for the agent to review your code and provide feedback.

8. Address any feedback from the code-review-agent.

9. Merge your pull request.

## Step 5: Test Your Application

1. Pull the latest changes to your local machine:

```bash
git checkout main
git pull
```

2. Install dependencies:

```bash
npm install
```

3. Run the tests:

```bash
npm test
```

4. Start the application:

```bash
npm start
```

5. Test the API endpoints using curl or a tool like Postman:

```bash
# Create a new task
curl -X POST http://localhost:3000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn A5C", "description": "Complete the first project tutorial", "priority": "high"}'

# Get all tasks
curl http://localhost:3000/api/tasks

# Filter tasks by priority
curl http://localhost:3000/api/tasks?priority=high
```

## Next Steps

Now that you've completed your first A5C project, you can:

- Learn more about [A5C Agents](../concepts/agents.md) and their capabilities
- Explore different [trigger mechanisms](../concepts/triggers.md) for agent activation
- Try creating [custom agents](../tutorials/creating-custom-agents.md) for your specific needs
- Add more advanced features to your task management API

## Troubleshooting

If you encounter issues:

- Check the GitHub Actions logs for error messages
- Verify your API keys are correctly configured
- Ensure your mentions of agents use the correct format (e.g., @developer-agent)
- See the [Troubleshooting Guide](../guides/troubleshooting.md) for common issues and solutions

> **Tip**: Always provide clear, specific instructions when communicating with agents. The more context you provide, the better the agent can assist you.
