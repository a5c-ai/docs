# Configuring Triggers

This guide explains how to configure triggers for your A5C agents. Triggers determine when and how your agents are activated, allowing you to automate responses to specific events, mentions, file changes, and schedules.

## Introduction to Triggers

A5C supports six primary trigger types:

1. **Event Triggers**: Activate on GitHub events (push, pull request, issue)
2. **Mention Triggers**: Activate when the agent is mentioned
3. **Label Triggers**: Activate when specific labels are applied
4. **Branch Triggers**: Activate on changes to specific branches
5. **File Pattern Triggers**: Activate when specific files change
6. **Schedule Triggers**: Activate on a time-based schedule

Configuring the right triggers is essential for efficient and effective agent operation.

## Event-Based Triggers

Event triggers activate agents in response to GitHub events.

### Configuration Syntax

```yaml
---
name: event-agent
version: 1.0.0
category: development
triggers:
  events:
    - push:
        branches: ["main", "develop", "feature/*"]
    - pull_request:
        types: ["opened", "synchronize", "reopened"]
        branches: ["main"]
    - issues:
        types: ["opened", "edited", "labeled"]
    - issue_comment:
        types: ["created"]
    - workflow_dispatch
---
```

### Available Events

A5C supports all GitHub webhook events, including:

- **push**: Repository pushes
- **pull_request**: Pull request activities
- **issues**: Issue activities
- **issue_comment**: Comments on issues and PRs
- **release**: Release activities
- **workflow_dispatch**: Manual workflow triggers
- **schedule**: Time-based triggers
- **repository_dispatch**: Custom webhook events

### Event Filtering

You can filter events based on various criteria:

```yaml
triggers:
  events:
    - push:
        branches: ["main", "develop"]
        paths: ["src/**", "!src/tests/**"]
    - pull_request:
        types: ["opened", "synchronize"]
        branches: ["main"]
        paths-ignore: ["docs/**", "*.md"]
```

## Mention-Based Triggers

Mention triggers activate agents when they are explicitly mentioned.

### Configuration Syntax

```yaml
---
name: mention-agent
version: 1.0.0
category: development
triggers:
  mentions:
    - "@mention-agent"
    - "@ma"  # Short alias
---
```

### Mention Locations

Agents can be mentioned in various locations:

- **Commit Messages**: `Implement login feature @security-reviewer`
- **Issue/PR Comments**: `@code-review-agent please review this PR`
- **Code Comments**: `// @performance-agent: optimize this function`
- **PR Descriptions**: `This PR adds a new feature. @documentation-agent please update docs`

### Mention Formats

A5C supports different mention formats:

- **Standard Mention**: `@agent-name`
- **Task Assignment**: `@agent-name: task description`
- **Quoted Mention**: `"@agent-name"`
- **Code Comment**: Language-specific formats like `// @agent-name`, `# @agent-name`, `<!-- @agent-name -->`

## Label-Based Triggers

Label triggers activate agents when specific labels are applied to issues or pull requests.

### Configuration Syntax

```yaml
---
name: label-agent
version: 1.0.0
category: development
triggers:
  labels:
    - "bug"
    - "security"
    - "documentation-needed"
    - "perf/*"  # Wildcard pattern
---
```

### Label Patterns

You can use patterns to match multiple labels:

- **Exact Match**: `"bug"` matches only the "bug" label
- **Prefix Match**: `"security/*"` matches "security/high", "security/medium", etc.
- **Suffix Match**: `"*/urgent"` matches "bug/urgent", "feature/urgent", etc.
- **Pattern Match**: `"*review*"` matches any label containing "review"

### Label Combinations

You can require multiple labels using the `all` operator:

```yaml
triggers:
  labels:
    all:
      - "bug"
      - "high-priority"
```

This activates the agent only when both labels are present.

## Branch-Based Triggers

Branch triggers activate agents on changes to specific branches.

### Configuration Syntax

```yaml
---
name: branch-agent
version: 1.0.0
category: development
triggers:
  branches:
    - "main"
    - "develop"
    - "feature/*"
    - "!feature/experimental/*"
---
```

### Branch Patterns

You can use patterns to match multiple branches:

- **Exact Match**: `"main"` matches only the "main" branch
- **Prefix Match**: `"feature/*"` matches all feature branches
- **Negative Match**: `"!feature/wip/*"` excludes WIP feature branches
- **Complex Patterns**: `"release/v*.*.x"` matches semantic versioning patterns

### Branch Pattern Precedence

When using both inclusive and exclusive patterns, exclusive patterns (prefixed with `!`) take precedence:

```yaml
triggers:
  branches:
    - "feature/*"       # Include all feature branches
    - "!feature/wip/*"  # Except WIP feature branches
```

## File Pattern Triggers

File pattern triggers activate agents when specific files are changed.

### Configuration Syntax

```yaml
---
name: file-pattern-agent
version: 1.0.0
category: development
triggers:
  file_patterns:
    - "src/**/*.js"
    - "src/**/*.ts"
    - "!src/tests/**"
    - "package.json"
---
```

### File Pattern Matching

A5C uses the glob pattern syntax for file matching:

- **Single File**: `"package.json"` matches the exact file
- **Directory**: `"src/"` matches all files in the src directory
- **Extension**: `"*.js"` matches all JavaScript files
- **Recursive**: `"**/*.js"` matches all JavaScript files in any directory
- **Negative Pattern**: `"!src/tests/**"` excludes all files in the tests directory
- **Alternation**: `"{src,libs}/**/*.js"` matches JavaScript files in src or libs directories

### Change Type Filtering

You can filter based on the type of file change:

```yaml
triggers:
  file_patterns:
    added: ["*.new", "new/**/*"]
    modified: ["src/**/*.js"]
    deleted: ["deprecated/**/*"]
    any: ["important.config"]  # Any change type
```

## Schedule-Based Triggers

Schedule triggers activate agents based on a time schedule.

### Configuration Syntax

```yaml
---
name: schedule-agent
version: 1.0.0
category: maintenance
triggers:
  schedules:
    - cron: "0 0 * * *"  # Daily at midnight UTC
    - cron: "0 12 * * 1-5"  # Weekdays at noon UTC
---
```

### Cron Syntax

A5C uses the standard cron syntax:

```
┌───────────── minute (0-59)
│ ┌───────────── hour (0-23)
│ │ ┌───────────── day of the month (1-31)
│ │ │ ┌───────────── month (1-12 or JAN-DEC)
│ │ │ │ ┌───────────── day of the week (0-6 or SUN-SAT)
│ │ │ │ │
│ │ │ │ │
* * * * *
```

Common cron patterns:

- **Daily**: `"0 0 * * *"` (midnight every day)
- **Weekdays**: `"0 9 * * 1-5"` (9 AM Monday-Friday)
- **Weekly**: `"0 0 * * 0"` (midnight on Sunday)
- **Monthly**: `"0 0 1 * *"` (midnight on the 1st of each month)
- **Hourly**: `"0 * * * *"` (top of every hour)

### Schedule Limitations

Note these limitations for schedule triggers:

1. Minimum frequency is once per hour (GitHub constraint)
2. Times are in UTC timezone
3. Schedules may have a few minutes of variance
4. Maximum of 20 scheduled triggers per repository

## Combining Multiple Triggers

You can combine multiple trigger types for sophisticated activation patterns:

```yaml
---
name: comprehensive-agent
version: 1.0.0
category: development
triggers:
  # Activate on specific events
  events:
    - push:
        branches: ["main", "develop"]
    - pull_request:
        types: ["opened", "synchronize"]
        branches: ["main"]
  
  # Activate when mentioned
  mentions:
    - "@comprehensive-agent"
    - "@ca"
  
  # Activate on specific labels
  labels:
    - "needs-review"
    - "bug/critical"
  
  # Activate on specific branches
  branches:
    - "feature/*"
    - "!feature/wip/*"
  
  # Activate on specific file changes
  file_patterns:
    - "src/core/**/*.js"
    - "config/*.json"
    - "!src/tests/**"
  
  # Activate on schedule
  schedules:
    - cron: "0 0 * * *"  # Daily at midnight UTC
---
```

With this configuration, the agent will be activated if ANY of the trigger conditions are met (logical OR).

## Conditional Triggers

For more complex scenarios, you can create conditional triggers using logical operators:

### AND Condition

Require multiple conditions to be met:

```yaml
triggers:
  conditions:
    all:
      - events: ["pull_request"]
      - labels: ["security"]
      - file_patterns: ["src/auth/**"]
```

This activates the agent only when all three conditions are met: it's a pull request, has the "security" label, and changes files in the src/auth directory.

### OR Condition

Activate if any condition is met:

```yaml
triggers:
  conditions:
    any:
      - labels: ["security"]
      - file_patterns: ["src/auth/**", "src/crypto/**"]
```

This activates the agent if either the "security" label is applied OR files in the auth or crypto directories are changed.

### Complex Conditions

Combine AND and OR for complex conditions:

```yaml
triggers:
  conditions:
    all:
      - events: ["pull_request"]
      - any:
          - labels: ["security"]
          - file_patterns: ["src/auth/**", "src/crypto/**"]
```

This activates the agent on pull requests that either have the "security" label OR change files in the auth or crypto directories.

## Trigger Context

When an agent is activated, it receives a trigger context that includes:

1. **Trigger Type**: Which trigger activated the agent
2. **Event Information**: Details about the triggering event
3. **Repository Information**: Repository details
4. **Changed Files**: List of files modified in the event
5. **User Information**: User who initiated the event

This context helps the agent understand why it was activated and what it should respond to.

## Trigger Best Practices

Follow these best practices for efficient trigger configuration:

1. **Be Specific**: Use precise triggers to avoid unnecessary activations
2. **Use Branch Filters**: Limit triggers to relevant branches
3. **Combine Trigger Types**: Use multiple trigger types for comprehensive coverage
4. **Prefer File Patterns**: Use file patterns to focus on relevant changes
5. **Avoid Overlapping Agents**: Ensure agents have distinct responsibilities
6. **Test Triggers**: Verify trigger patterns before deployment
7. **Monitor Activations**: Track how often agents are triggered
8. **Adjust as Needed**: Refine triggers based on actual usage patterns

## Next Steps

- Learn about [setting up agents](setting-up-agents.md)
- Understand [MCP servers](using-mcp-servers.md)
- Explore [customizing agent behavior](customizing-agent-behavior.md)
- See how to [create custom agents](creating-custom-agents.md)