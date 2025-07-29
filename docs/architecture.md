# Architecture

The a5c project follows a modular, event-driven architecture that leverages Git-based workflows and AI agent orchestration to automate software development tasks.

## System Components

| Component          | Description                                                             |
|--------------------|-------------------------------------------------------------------------|
| **GitHub Server**  | Hosts the code repository and orchestrates GitHub Actions workflows.    |
| **Event Router**   | Listens to GitHub events (webhooks) and routes events to the orchestrator. |
| **Orchestrator**   | Coordinates incoming events and dispatches them to specific AI agents via the agent runtime. |
| **Agent Runners**  | Executes individual AI agents responsible for tasks like documentation, code validation, or release management. |
| **State Store**    | Persists run state, logs, and intermediate data for traceability and retries. |
| **Knowledge Base** | Stores contextual information, issue/PR metadata, and cross-agent communication artifacts. |

## Component Diagram

```text
                        +------------------+
                        |  GitHub Server   |
                        +---------+--------+
                                  |
                                  | Webhooks / Actions
                                  v
                  +---------------+---------------+
                  |          Event Router         |
                  +---------------+---------------+
                                  |
                                  v
                  +---------------+---------------+
                  |         Orchestrator         |
                  +-------+-------+-------+-------+
                          |               |
           +--------------+               +----------------+
           |                                                   |
           v                                                   v
+----------+-----------+                         +------------+----------+
|    Agent Runners     |                         |     State Store       |
+----------+-----------+                         +-----------------------+
           |
           v
 +----------+-----------+
 |    Knowledge Base    |
 +----------------------+
```

## Workflows

### Issue Comment Workflow

1. A user adds a comment with a mention (e.g., `@documenter-agent`) on an issue or pull request.
2. GitHub triggers a webhook event captured by the Event Router.
3. The Orchestrator identifies the target agent and dispatches the event payload.
4. The Agent Runner processes the request, performs the task, and updates the repository (e.g., by creating documentation files).
5. Results (e.g., new files or comments) are persisted in the State Store and Knowledge Base for traceability.

### Pull Request Workflow

1. A new pull request is opened against the `main` branch.
2. GitHub Actions runs the orchestrator and validation workflows.
3. The Orchestrator dispatches linting, testing, or documentation-generation tasks to the Agent Runners.
4. Agents commit changes, run tests, or post review comments.
5. Final status is reported back to GitHub, and run details are stored in the State Store.

## Acceptance Criteria

- Provide diagrams and descriptions of system components and workflows.
