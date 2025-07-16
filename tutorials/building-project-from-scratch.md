# Building a Project from Scratch

This tutorial guides you through building a complete project from scratch using A5C, providing a hands-on introduction to the A5C agent system.

## Prerequisites

Before starting, ensure you have:

- Completed the [installation](../getting-started/installation.md) process
- A GitHub account with permissions to create repositories
- Basic understanding of Git commands
- An Anthropic API key for Claude access
- Node.js installed (for this specific example)

## Project Overview

In this tutorial, we'll build a simple task management API with:

- Node.js and Express for the backend
- A5C agents for development assistance
- GitHub for source control and agent execution
- Automated tests with Jest

The final project will include:
- API endpoints for creating, reading, updating, and deleting tasks
- Basic data validation
- Test coverage for all functionality
- Proper project structure following best practices

## Step 1: Repository Setup

### Create a New Repository

1. Log in to GitHub and click "New repository"
2. Name it "a5c-task-manager" (or choose your own name)
3. Add a description: "Task management API built with A5C assistance"
4. Choose public or private visibility
5. Initialize with a README.md
6. Click "Create repository"

### Clone the Repository

```bash
git clone https://github.com/your-username/a5c-task-manager.git
cd a5c-task-manager
```

## Step 2: Configure A5C

### Create Configuration Directory

```bash
mkdir -p .a5c
```

### Create Configuration File

Create `.a5c/config.yml` with the following content:

```yaml
# A5C Configuration
version: 1.0.0

# Global settings
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false
  timeout: 600  # 10 minutes

# Agent configuration
agents:
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
  local:
    enabled: true
    paths:
      - "./.a5c/agents"

# MCP servers configuration
mcp_servers:
  github:
    enabled: true
  filesystem:
    enabled: true
  memory:
    enabled: true
    persistence: session
```

### Set Up GitHub Workflow

Create `.github/workflows` directory:

```bash
mkdir -p .github/workflows
```

Create `.github/workflows/a5c.yml`:

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

### Add API Key to Repository Secrets

1. Go to your repository on GitHub
2. Navigate to Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `ANTHROPIC_API_KEY`
5. Value: Your Anthropic API key
6. Click "Add secret"

### Commit and Push Configuration

```bash
git add .a5c .github
git commit -m "Add A5C configuration"
git push
```

## Step 3: Project Initialization

### Create a Project Seeding Issue

1. Go to your repository on GitHub
2. Click "Issues" → "New issue"
3. Title: "Initialize Node.js Express API project"
4. Content:

```
@project-seeder-agent

Please initialize a Node.js Express API project with:

1. Express.js for handling HTTP requests
2. Simple in-memory task storage (no database required)
3. RESTful API endpoints for task CRUD operations
4. Basic project structure with:
   - Routes
   - Controllers
   - Models
   - Middleware
5. Jest for testing
6. ESLint for code quality
7. README with setup and usage instructions

Thank you!
```

5. Click "Submit new issue"

### Wait for Project Initialization

The project-seeder-agent will:
1. Analyze your request
2. Create the initial project structure
3. Implement the basic functionality
4. Add tests and documentation
5. Comment on the issue when finished

This typically takes 5-10 minutes depending on the complexity.

### Pull the Changes

Once the agent has finished, pull the changes to your local repository:

```bash
git pull
```

## Step 4: Explore the Project Structure

The project-seeder-agent will have created a structure similar to:

```
.
├── .a5c/
├── .github/
├── src/
│   ├── controllers/
│   │   └── taskController.js
│   ├── models/
│   │   └── taskModel.js
│   ├── routes/
│   │   └── taskRoutes.js
│   ├── middleware/
│   │   └── errorHandler.js
│   └── app.js
├── tests/
│   └── tasks.test.js
├── .eslintrc.js
├── .gitignore
├── jest.config.js
├── package.json
└── README.md
```

Examine the code to understand the implementation:

```bash
# Install dependencies
npm install

# Run tests to verify functionality
npm test
```

## Step 5: Add a New Feature

Now let's enhance the project by adding a new feature with agent assistance.

### Create a Feature Branch

```bash
git checkout -b feature/task-priorities
```

### Create a Feature Request Issue

1. Go to your repository on GitHub
2. Click "Issues" → "New issue"
3. Title: "Add task priority functionality"
4. Content:

```
@developer-agent

Please add a priority system to our task manager with these requirements:

1. Add a `priority` field to tasks with three possible values: "low", "medium", "high"
2. Default priority should be "medium"
3. Update the API to:
   - Allow setting priority when creating/updating tasks
   - Support filtering tasks by priority
   - Include priority in task responses
4. Add validation to ensure only valid priorities are accepted
5. Update tests to cover the new functionality

Thank you!
```

5. Click "Submit new issue"

### Implement the Feature Based on Agent Guidance

The developer-agent will provide guidance and code for implementing the feature. Follow the agent's suggestions to implement the changes locally:

```bash
# After making the suggested changes
git add .
git commit -m "Add task priority functionality"
git push --set-upstream origin feature/task-priorities
```

### Create a Pull Request

1. Go to your repository on GitHub
2. You should see a prompt to create a pull request
3. Click "Compare & pull request"
4. Title: "Add task priority functionality"
5. Description: Summarize the changes made
6. Click "Create pull request"

### Request Code Review

Comment on the pull request:

```
@code-review-agent

Please review this PR for the task priority implementation. Check for:
1. Code quality and best practices
2. Test coverage
3. Any potential bugs or edge cases
4. Performance considerations

Thank you!
```

### Address Review Feedback

The code-review-agent will analyze your changes and provide feedback. Make any necessary adjustments based on the feedback:

```bash
# After making changes based on feedback
git add .
git commit -m "Address code review feedback"
git push
```

### Merge the Pull Request

Once the code-review-agent approves the changes:

1. Go to your pull request on GitHub
2. Click "Merge pull request"
3. Click "Confirm merge"
4. Delete the branch if desired

## Step 6: Running the Application

### Pull the Latest Changes

```bash
git checkout main
git pull
```

### Install Dependencies and Run

```bash
npm install
npm start
```

The server should start on port 3000 (or as configured).

### Test the API

Using curl or a tool like Postman:

```bash
# Create a new task with priority
curl -X POST http://localhost:3000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn A5C", "description": "Complete the first project tutorial", "priority": "high"}'

# Get all tasks
curl http://localhost:3000/api/tasks

# Filter tasks by priority
curl http://localhost:3000/api/tasks?priority=high

# Update a task
curl -X PUT http://localhost:3000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn A5C", "description": "Complete the first project tutorial", "priority": "medium"}'

# Delete a task
curl -X DELETE http://localhost:3000/api/tasks/1
```

## Step 7: Enhancing the Project Further

You can continue enhancing the project by creating new issues and requesting agent assistance. Here are some ideas:

### Add User Authentication

```
@security-agent

Please add JWT-based authentication to our task manager API with:
1. User registration and login endpoints
2. Password hashing and validation
3. JWT token generation and verification
4. Route protection middleware
5. Task ownership (users can only see/modify their own tasks)
```

### Add Categories or Tags

```
@developer-agent

Please add a tagging system to tasks with:
1. Ability to add multiple tags to each task
2. Endpoints to create, update, and delete tags
3. Filtering tasks by tags
4. Tests for the new functionality
```

### Implement Persistence

```
@database-agent

Please replace our in-memory storage with MongoDB:
1. Set up Mongoose schema for tasks
2. Update controllers to use MongoDB operations
3. Add environment configuration for database connection
4. Update tests to use a test database
```

## Conclusion

Congratulations! You've successfully built a project from scratch using A5C. Through this tutorial, you've learned:

1. How to set up A5C in a new project
2. How to use different agents for specific tasks
3. The workflow for developing features with agent assistance
4. How to get code reviews from specialized agents
5. The overall development process with A5C

## Next Steps

- Learn more about [A5C agents](../concepts/agents.md) and their capabilities
- Explore [adding A5C to existing projects](adding-a5c-to-existing-projects.md)
- Try [creating custom agents](creating-custom-agents.md) for your specific needs
- Learn about [implementing custom MCP servers](implementing-custom-mcp-servers.md)