# Agent Customization

Customize and extend AI agents in your repository by following these steps. Learn where to place custom agent definitions, how to structure the files, use template inclusion for shared rules, and see example references to registry templates.

## 1. Placing custom agent definitions

Place your custom agent definition files under the `.a5c/agents/` directory at the repository root. Each agent definition should use the `.agent.md` extension. For example:

```bash
# Repository root
.a5c/agents/
└── my-custom-agent.agent.md
```

## 2. Structuring agent definition files

Agent definition files use Markdown with front-matter to describe metadata and instructions. A minimal example:

```markdown
---
name: my-custom-agent
description: This agent performs my custom automation tasks.
trigger:
  - event: pull_request
permissions:
  issues: write
---

# my-custom-agent

<!-- Agent instructions and templates go here -->
```

Refer to the [a5c registry's agent templates](https://github.com/a5c-ai/registry/tree/main/agents) for detailed examples.

## 3. Using shared templates

To avoid duplication, you can include shared templates from the a5c registry or your own `.a5c/templates/` directory. Use the `{{ include '<template-name>' }}` syntax in your agent definition:

```markdown
# my-custom-agent
{{ include 'validation-agent' }}
```

This pulls in the `validation-agent` template from the configured registry sources.

## 4. Example: combining templates

Here's an example that combines a registry template with custom instructions:

```markdown
---
name: my-ci-agent
description: CI pipeline automation with custom validation.
---

# my-ci-agent

## Step 1: Base CI checks
{{ include 'ci-base-agent' }}

## Step 2: Custom post-processing
- task: notify
  channel: dev-team
```

## 5. Next steps

- Update `.a5c/config.yml` to alias or reference your custom agents if needed.
- Review the [How-To Guides](howtos.md) for more workflows and advanced pipelines.
