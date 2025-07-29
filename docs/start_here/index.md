# Start Here

Welcome to **a5c**! This section helps new users get up and running quickly with the a5c platform.

## Introduction

a5c transforms your Git repository into an intelligent, autonomous development environment. By orchestrating AI agents within your repo, a5c automates tasks such as code reviews, build fixes, documentation updates, and feature implementation—letting you focus on high-level architecture and business logic.

Learn more in the Technical Overview article under `articles/!a5c-technical-overview.md`.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Git** (>=2.30) to manage repository versioning and agent actions
- **Node.js** (>=16.0) for the a5c CLI and web components
- **Python** (>=3.8) for agent orchestration scripts
- A GitHub account with repository access and a valid **API token**

## Quick Start

Follow these steps to set up a5c in your repository:

```bash
# Clone your repository
git clone https://github.com/<your-org>/<your-repo>.git
cd <your-repo>

# Install the a5c CLI tool
npm install -g @a5c/cli

# Initialize a5c in the repo
a5c init

# Start the a5c agent loop locally
a5c start
```

Once started, the agents will analyze your repo and begin automating tasks. It may take a few minutes on first run.

## Git Workflow

a5c agents integrate deeply with Git to track and automate changes in your repository. Each action taken by an agent is committed through dedicated branches and pull requests, providing clear audit trails and collaboration points.

Key points:

- Agents create branches following the naming convention `a5c/agent/<agent-name>/<task>`.
- All automated changes are opened as pull requests for your review, with detailed descriptions and context.
- Agents monitor branch updates, commit messages, and diffs to trigger code analysis, automated fixes, or documentation updates.

## Agent Proactiveness

a5c’s AI agents are proactive, continuously scanning your repository for opportunities to improve code quality, maintain documentation, and optimize workflows. They listen to Git events (pushes, pull requests, and issue comments) and act without manual intervention when possible.

Highlights of agent proactiveness:

- Automated linting, formatting, and testing feedback on every commit.
- Regular detection of stale or missing documentation, with automated suggestions or updates.
- Dependency and security alert management through automated issues and pull requests.

## Next Topics

Below are placeholder sections for topics covered later in this Start Here guide:

### Installation Details

Content for the installation details section will go here.

### Configuration

Content for the configuration section will go here.

### First Project

Content for the first project section will go here.

### Command Reference

Content for the command reference section will go here.

### Troubleshooting

Content for the troubleshooting section will go here.
