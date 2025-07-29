# Tutorials

This section provides comprehensive tutorials for advanced usage of **a5c**, covering custom workflows, integrations, and automation examples.

## Extending A5C Specs for Custom Workflows

Define custom agent behaviors and triggers by extending your `specs.yaml` configuration:

```yaml
agents:
  dev:
    model: gpt-4
    permissions:
      branches:
        - main
    hooks:
      on_commit: ./scripts/run-tests.sh
```

Generate or validate your specs with the CLI:

```bash
a5c specs init      # scaffold specs.yaml
a5c specs validate  # check for schema compliance
```

## Creating Custom Actions with the A5C Action SDK

Build reusable actions by importing the A5C Action SDK and defining your logic:

```javascript
import { Action } from 'a5c-action';

export default class HelloAction extends Action {
  async run(context) {
    context.log('Hello from custom action!');
  }
}
```

Package and publish your action to reuse across repositories:

```bash
npm publish      # publishes to your npm or private registry
```

## Integrating A5C with GitHub Actions

Automate agent execution in CI by adding a GitHub Actions workflow:

```yaml
name: AI Agents

on: [push]

jobs:
  run-agents:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup A5C CLI
        run: |
          pip install a5c-cli
          a5c init
      - name: Run Dev Agent
        run: a5c agent dev
```

## Seeding AI Agents with seed-generic for Domain-Specific Knowledge

Enhance agent memory by seeding domain data:

```bash
npm install @a5c-ai/seed-generic
node <<'EOF'
import { seedWith } from '@a5c-ai/seed-generic';
await seedWith({ memory: 'Domain-specific guidelines and examples' });
EOF
```

## Publishing Custom Packages to A5C Registry

Manage and share your custom agents via the A5C registry:

```bash
a5c registry login --token $A5C_REG_TOKEN
a5c publish ./my-agent --description "Custom development agent"
```

## Advanced CLI Usage and Automation

Use the CLI to preview changes and enforce auditability:

```bash
a5c diff --branch feature/x --agent dev
```

:::warning
Ensure your API keys and secrets are stored securely and excluded from version control.
:::

:::tip
Use `a5c --help` to explore available commands and options.
:::

## Acceptance Criteria

- Tutorial examples covering advanced features and integrations included.
