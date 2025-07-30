# Architecture

This section provides an overview of the a5c platform architecture, describing its core components, configuration system, agent registry, and integration points. Together, these enable a Git-native, event-driven AI agent orchestration platform.

## Overview

The a5c platform transforms a Git repository into an intelligent, autonomous development environment. Agents are defined as files in the repository and are triggered by GitHub events (e.g., commits, pull requests, issue comments) via a GitHub Action. The system components load resources, manage configuration, route events to agents, execute prompts, and process structured outputs.

```text
+----------------------+         +--------------------------+       +-------------------+
| GitHub Repository    |  Git   | a5c GitHub Action        |       | Model Context     |
| (code + .a5c/agents) | <----> | (.github/workflows/a5c.yml) |---->| Protocol Servers |
+----------------------+         +--------------------------+       +-------------------+
                                       |        |       |
                                       v        v       v
                            +---------------------------+
                            | Core Components           |
                            | - Resource Handler        |
                            | - Agent Router            |
                            | - Config Manager          |
                            | - Prompt Engine           |
                            | - Agent Execution         |
                            | - Output Processor        |
                            +---------------------------+
                                       |
                                       v
                            +---------------------------+
                            | AI Agents (Registry)      |
                            +---------------------------+
```

## Core Components

The GitHub Action implementation (see [a5c-ai/action](https://github.com/a5c-ai/action)) consists of focused modules:

| Component            | Responsibility                                                 |
|----------------------|----------------------------------------------------------------|
| Resource Handler     | Load prompts, agents, and configuration from local or remote sources with caching and retry logic. |
| Agent Router         | Discover agents based on events, mentions, labels, and other triggers. |
| Config Manager       | Merge built-in defaults, user configuration (`.a5c/config.yml`), and agent frontmatter. |
| Prompt Engine        | Render templated prompts using YAML frontmatter and context.   |
| Agent Execution      | Invoke the configured LLM or CLI tool and collect the raw response. |
| Output Processor     | Parse and format structured data from agent responses.         |
| MCP Manager          | Manage built-in Model Context Protocol (MCP) servers (e.g., filesystem, memory, search, GitHub). |
| Utilities            | Common helpers, logging, and error handling.                   |

## Configuration System

The configuration hierarchy enables flexible overrides and remote loading:

1. **Built-in Defaults** (`default-config.yml`)
2. **User Configuration** (`.a5c/config.yml` or remote URI)
3. **Agent Frontmatter** (YAML in `.agent.md` files)

Configuration files and agents can be sourced from remote repositories or URLs, authenticated via `GITHUB_TOKEN`. See [Configuration · a5c-ai/action](https://github.com/a5c-ai/action#flexible-configuration).

## Specification Repository

The platform specifications are maintained in the [a5c-ai/spec](https://github.com/a5c-ai/spec) repository. This includes the Agent Format and Proposal System specifications:

- **Agent Format Specification**: Defines YAML frontmatter structure, inheritance model, and validation rules.
- **Proposal System Specification**: Outlines the community governance and proposal workflow.

## Agent Registry

A community-driven registry (see [a5c-ai/registry](https://github.com/a5c-ai/registry)) hosts shared agents, enabling composable intelligence through inheritance. Base agents published in the registry can be extended locally or remotely.

## Seed Templates

Starter templates for new agents are available in the [a5c-ai/seed-generic](https://github.com/a5c-ai/seed-generic) repository. Use these seeds to bootstrap custom agents with best-practice frontmatter and prompts.

## Integration Points

- **GitHub Actions**: Event-driven invocation via `.github/workflows/a5c.yml`.
- **CLI Tools**: Supports multiple LLMs (e.g., GPT, Claude, Gemini) through a unified CLI interface.
- **Model Context Protocol**: Integrates MCP servers for enhanced context (e.g., search index, GitHub API).

## Further Reading

- [a5c Technical Overview Article](articles/!a5c-technical-overview.md)
- [Community Guide](community.md)
- [Configuration Reference](format.md)
- [Developer Quick Start](start_here.md)
