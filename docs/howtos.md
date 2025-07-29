# Howtos

This section provides step-by-step how-to guides for common workflows and use cases using **a5c**.

## How to install the a5c GitHub Action

### Prerequisites

- A GitHub repository with code you want to automate
- `actions/checkout` enabled in the workflow

### Steps

1. Create a new workflow file at `.github/workflows/a5c-action.yml` with the following:
   ```yaml
   name: a5c AI Agent
   on:
     push:
       branches: [ main ]
     pull_request:
   jobs:
     a5c:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         - uses: a5c-ai/action@main
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
   ```
2. Commit and push the workflow.
3. Observe AI-driven repository automation on your next push or pull request.

::: tip
You can customize triggers and runtime settings in the workflow file.
Refer to the [Reference](reference.md#a5c-action) for more options.
:::

## How to run local AI-driven commands

### Prerequisites

- Python 3.8 or newer
- [a5c CLI](guide.md#installation) installed

### Steps

1. Install the CLI:
   ```bash
   pip install a5c
   ```
2. Initialize a workspace:
   ```bash
   a5c init
   ```
3. Run an AI command (for example, generate documentation):
   ```bash
   a5c docgen --target docs/howtos.md
   ```

::: warning
Ensure your `OPENAI_API_KEY` (or equivalent) is set in your environment before running commands.
:::

## How to contribute to your repository with AI agents

Use commit message instructions to prompt AI agents to update code or docs automatically.

### Steps

1. Add an instruction comment in your code or docs:
   ```markdown
   <!-- @a5c-agent add unit tests for calculate_metrics -->
   ```
2. Stage and commit your change:
   ```bash
   git add .
   git commit -m "docs: request AI to add unit tests for calculate_metrics"
   ```
3. Push to GitHub and let the a5c agents generate tests and open a PR.

For more examples and advanced workflows, see the [Tutorials](tutorials.md) section.
