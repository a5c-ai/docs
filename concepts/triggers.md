# Triggers

Triggers determine when and how agents are activated in the A5C system. This page explains the different trigger mechanisms and their configuration.

## Trigger Types

A5C supports six primary trigger types:

### 1. Event-based Triggers

Event-based triggers activate agents in response to GitHub events.

**Configuration:**
```yaml
events: ["push", "pull_request.opened", "issues.labeled"]
```

**Commonly Supported Events:**
- `push`: When code is pushed to the repository
- `pull_request`: When pull request actions occur
  - `.opened`: When a PR is first opened
  - `.synchronize`: When a PR is updated
  - `.closed`: When a PR is closed
  - `.labeled`: When a label is added to a PR
- `issues`: When issue actions occur
  - `.opened`: When an issue is created
  - `.edited`: When an issue is edited
  - `.labeled`: When a label is added to an issue
- `issue_comment`: When comment actions occur
  - `.created`: When a new comment is added
  - `.edited`: When a comment is edited
- `schedule`: Time-based trigger (used with `activation_cron`)

> **Note**: Check the current A5C documentation for the complete list of supported events as they may change with updates.

### 2. Mention-based Triggers

Mention-based triggers activate agents when they are mentioned in GitHub issues, pull requests, or comments.

**Configuration:**
```yaml
mentions: "@developer-agent,@dev"
```

**Formats:**
- `@agent-name`: Standard mention format
- Multiple mentions can be specified as a comma-separated list
- Aliases can be defined to allow shorter mention forms

### 3. Schedule-based Triggers

Schedule-based triggers activate agents on a regular schedule using cron expressions.

**Configuration:**
```yaml
activation_cron: "0 9 * * 1-5"  # Weekdays at 9 AM
```

**Cron Format:**
- Standard cron format: `minute hour day-of-month month day-of-week`
- Example: `0 9 * * 1-5` (Weekdays at 9 AM)
- Example: `0 0 * * *` (Daily at midnight)
- Example: `0 0 1 * *` (First day of each month)

### 4. Label-based Triggers

Label-based triggers activate agents when specific labels are added to issues or pull requests.

**Configuration:**
```yaml
labels: "bug,enhancement,question"
```

**Usage:**
- Specify labels as a comma-separated list
- Agents will be triggered when any of the specified labels are added
- Combined with event triggers like `issues.labeled` or `pull_request.labeled`

### 5. Branch-based Triggers

Branch-based triggers activate agents when changes occur on specific branches.

**Configuration:**
```yaml
branches: "main,develop,feature/*"
```

**Pattern Matching:**
- Exact branch names: `main`, `develop`
- Wildcards: `feature/*` (any branch starting with "feature/")
- Combined with event triggers like `push` or `pull_request`

### 6. File Path-based Triggers

File path-based triggers activate agents when specific files or directories are modified.

**Configuration:**
```yaml
paths: "src/**/*.js,src/**/*.ts"
```

**Pattern Matching:**
- Glob patterns for file matching
- `**` matches any number of directories
- `*` matches any number of characters in a filename
- Combined with event triggers like `push` or `pull_request`

## Trigger Combinations

Multiple trigger types can be combined to create complex activation rules. For example:

```yaml
# Activate when JavaScript files are changed in pull requests to the main branch
events: ["pull_request"]
branches: "main"
paths: "src/**/*.js"
```

```yaml
# Activate when bug issues are created or labeled
events: ["issues.opened", "issues.labeled"]
labels: "bug"
```

## Trigger Priority

When multiple agents are triggered by the same event, they are executed in order of priority:

```yaml
# Higher priority agents run first
priority: 80
```

The priority value is a number between 0 and 100, with higher values indicating higher priority.

## Trigger Context

When an agent is triggered, it receives context information about the trigger:

- **Event trigger**: Information about the GitHub event
- **Label trigger**: Information about the applied label
- **Branch trigger**: Information about the branch
- **File trigger**: Information about the modified files
- **Mention trigger**: Information about the mention and surrounding text
- **Schedule trigger**: Information about the schedule execution

This context helps the agent understand why it was triggered and what action to take.

## Best Practices

When configuring triggers:

1. **Be specific**: Use precise trigger combinations to avoid unnecessary agent activations
2. **Consider performance**: Too many triggered agents can slow down workflow
3. **Set appropriate priorities**: Critical agents should have higher priority
4. **Use schedule triggers sparingly**: Frequent scheduled runs can consume API quotas
5. **Test trigger combinations**: Verify that your trigger rules work as expected

## Next Steps

- Learn about [agent configuration](configuration.md)
- Understand how to [customize agent behavior](../guides/customizing-agent-behavior.md)
- See [configuring triggers](../guides/configuring-triggers.md) for practical examples