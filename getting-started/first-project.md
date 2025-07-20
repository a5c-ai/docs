# Your First Project


This guide walks you through creating your first project with a5c, demonstrating how to set up a simple application with AI agent assistance.

## Prerequisites

Before starting your first a5c project, ensure you have:

- Completed the [Installation](installation.md) process
- A GitHub repository with a5c configured
- Basic understanding of the [Quick Start](quick-start.md) concepts
- An Anthropic API key for Claude access
- Git installed on your local machine

## Project Overview

In this tutorial, we'll build a simple task management API using:

- Node.js and Express for the backend
- a5c agents for development assistance
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

## Step 2: Set Up a5c Configuration

1. Create the a5c configuration directory:

```bash
mkdir -p .a5c
```

2. Create a basic `config.yml` file in the `.a5c` directory:

```yaml
# Basic a5c configuration
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
name: a5c Agent System
on:
  pull_request:
    types: [opened, synchronize, reopened, closed]
  issues:
    types: [opened, edited, labeled]
  issue_comment:
    types: [created, edited]
  push:
    branches: [main, develop, master]
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight
  workflow_dispatch:
    inputs:
      agent_uri:
        description: 'Specific agent to run'
        required: false

jobs:
  run-agents:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Run a5c Agents
        uses: a5c-ai/action@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          config_file: ".a5c/config.yml"
```

> **Note**: This configuration includes all supported trigger types. You can customize it based on your specific needs.

5. Commit and push these files to your repository:

```bash
git add .a5c .github
git commit -m "Set up a5c configuration"
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
  -d '{"title": "Learn a5c", "description": "Complete the first project tutorial", "priority": "high"}'

# Get all tasks
curl http://localhost:3000/api/tasks

# Filter tasks by priority
curl http://localhost:3000/api/tasks?priority=high
```

## Next Steps

Now that you've completed your first a5c project, you can:

- Learn more about a5c Agents and their capabilities in the [a5c Registry Repository](https://github.com/a5c-ai/registry)
- Explore different trigger mechanisms for agent activation in the [a5c GitHub Action documentation](https://github.com/a5c-ai/action)
- Try creating custom agents by following examples in the [a5c Registry](https://github.com/a5c-ai/registry)
- Add more advanced features to your task management API

## Troubleshooting

If you encounter issues:

- Check the GitHub Actions logs for error messages
- Verify your API keys are correctly configured
- Ensure your mentions of agents use the correct format (e.g., @developer-agent)
- See the [a5c GitHub Action repository](https://github.com/a5c-ai/action) for common issues and solutions

> **Tip**: Always provide clear, specific instructions when communicating with agents. The more context you provide, the better the agent can assist you.
