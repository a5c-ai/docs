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

## Next Topics

Below are detailed guides for each topic. Click to learn more:

- [Installation Details](installation_details.md)
- [Configuration](configuration.md)
- [First Project](first_project.md)
- [Command Reference](command_reference.md)
- [Troubleshooting](troubleshooting.md)
