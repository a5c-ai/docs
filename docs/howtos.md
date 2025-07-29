# Howtos

This section provides step-by-step how-to guides for common workflows and use cases when working with the a5c living repository framework.

```{note}
These guides assume you have completed the [Start Here](start_here) and [User Guide](guide) sections.
Also refer to the [MyST-Parser documentation](https://myst-parser.readthedocs.io/) and the [sphinx_nefertiti theme guide](https://sphinx-nefertiti.readthedocs.io/) for syntax and styling conventions.
```

## How to write a backlog file

Backlog files are the primary way to instruct a5c agents on tasks to perform. Each backlog entry is written in YAML under the `backlog/` directory.

```{code-block} yaml
// backlog/example_task.yml
- id: create-new-agent
  title: "Generate a custom AI agent template"
  description: |
    Use the a5c agent-template to scaffold a new AI agent for your repo.
  labels:
    - agent
    - scaffold
```

1. Create a `.yml` file under `backlog/` with a unique `id` and `title`.
2. Add a `description` with details and any required parameters.
3. Commit and push; a5c will pick up the entry and run the corresponding agent.

## How to trigger an agent via issue comment

You can invoke agents directly from GitHub by commenting on an issue or pull request.

```{code-block} text
@agent-name: perform-code-review
```

Replace `agent-name` with the target agent (e.g., `documenter-agent`, `validation-agent`). The action will run and post results as a new comment.

## How to create a custom agent

Use the [agent-template repository](https://github.com/a5c-ai/agent-template) to scaffold new agents.

```{code-block} bash
npx degit a5c-ai/agent-template my-agent
cd my-agent
npm install
```

Edit `src/index.ts` to define your agent logic, then test locally with:

```{code-block} bash
npm run start
```

## How to integrate a5c with GitHub Actions CI/CD

Add the following workflow to your repo to automatically run backlog entries and tests:

```{code-block} yaml
name: a5c CI
on: [push]

jobs:
  a5c:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: a5c-ai/action@main
        with:
          config: .a5c/config.yml
```

See the [CI-CD That Thinks](../articles/CI-CD-That-Thinks.md) article for advanced setup.

## How to publish updated documentation

When you modify docs, build and preview before publishing:

```{code-block} bash
pip install -r requirements.txt
sphinx-build -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` in your browser. Then commit changes and merge; GitHub Pages or your deployment pipeline will update the live docs.
