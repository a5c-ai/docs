# Start Here

Get started with a5c in minutes by following this quickstart guide. You'll set up your environment, enable AI agents in your repository, and run your first agent workflow.

## Prerequisites

- **Git** installed on your local machine (version 2.0+).
- A **GitHub repository** where you have write access.
- GitHub **Actions** enabled in the repository settings.
- An AI provider account:
  - **OpenAI**: API key from `https://platform.openai.com/account/api-keys`
  - **Anthropic**: API key from `https://console.anthropic.com/account/keys`

## 5-Minute Quickstart

1. **Add your API key to GitHub**  
   In your repository, go to **Settings → Secrets and variables → Actions → New repository secret**.  
   - Secret name: `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`  
   - Secret value: Your provider API key.

2. **Wake up your repository**  
   Create the GitHub Actions workflow file at `.github/workflows/a5c.yml`:

```yaml
on: [pull_request, issues, issue_comment, push]

jobs:
  a5c:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
      issues: write
    steps:
      - uses: actions/checkout@v4
      - uses: a5c-ai/action@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
```

3. **Activate your first agent**  
   Agents can be triggered in two ways:

   - **Issue-based activation**: Create a GitHub issue or comment with an agent directive. For example:
     ```text
     # Title: Summarize PR #123
     @code-reviewer Please review the changes and suggest improvements.
     ```

   - **Push-based activation**: Define agent tasks in your config file (`.a5c/config.yml`) or file frontmatter. On push events, the workflow will run agents based on your config. For example:
     ```yaml
     # .a5c/config.yml
     agents:
       - name: doc-writer
         triggers:
           on:
             push:
               branches:
                 - main
     ```
     And in content files:
     ```markdown
     ---
     agent: doc-writer
     description: "Generate API docs for new endpoints"
     ---
     # API Endpoints
     ...
     ```
     Then commit and push to trigger the `doc-writer` agent.

4. **Enable repository features**  
   Ensure **Issues** and **Actions** are enabled under **Settings → General → Features**.

## Next Steps

Explore the rest of the a5c documentation to learn about configuration, advanced usage, and custom agent development:

```{toctree}
:maxdepth: 1

guide
howtos
reference
tutorials
community
architecture
vision
format
specs
```
