# Documentation CI with A5C

This guide explains how to set up a Continuous Integration (CI) workflow for documentation using A5C agents.

## Overview

A documentation CI workflow helps ensure that your documentation:

1. **Builds correctly**: No syntax errors or broken references
2. **Maintains quality**: Adheres to style guidelines and standards
3. **Stays updated**: Reflects the latest features and changes
4. **Remains consistent**: Uses consistent terminology and formatting

A5C agents can automate many aspects of this workflow, reducing manual effort and improving quality.

## Setting Up Documentation CI

### Prerequisites

Before setting up documentation CI with A5C, ensure you have:

- A documentation repository with Sphinx, MkDocs, or similar tooling
- A5C configured in your repository
- Appropriate agents added to your `.a5c/config.yml`
- GitHub Actions set up for A5C integration

### Required Agents

For an effective documentation CI workflow, include these agents:

- **validator-agent**: Reviews documentation quality and accuracy
- **build-fixer-agent**: Resolves documentation build issues
- **content-writer-agent**: Updates and creates documentation content
- **developer-agent**: Ensures technical accuracy in documentation

### GitHub Actions Workflow

Create or update your GitHub Actions workflow for documentation CI:

```yaml
name: Documentation CI

on:
  push:
    branches: [main, develop]
    paths:
      - '**/*.md'
      - '**/*.rst'
      - 'conf.py'
  pull_request:
    paths:
      - '**/*.md'
      - '**/*.rst'
      - 'conf.py'

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install sphinx sphinx-rtd-theme myst-parser

      - name: Build documentation
        run: |
          cd docs
          make html

      - name: Upload built documentation
        uses: actions/upload-artifact@v3
        with:
          name: documentation
          path: docs/_build/html/

  a5c:
    needs: docs
    if: failure()
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Run A5C Agents for doc fixes
        uses: a5c-ai/action@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          config_file: ".a5c/config.yml"
          custom_prompt: "The documentation build failed. Please examine the build logs and fix any issues."
```

This workflow:
1. Triggers on changes to documentation files
2. Attempts to build the documentation
3. If the build fails, activates A5C agents to fix the issues

## Agent Configurations for Documentation CI

### Validator Agent Configuration

```yaml
# .a5c/agents/validator-agent.agent.md
---
name: validator-agent
version: 1.0.0
category: quality
description: Documentation validator

events: ["pull_request"]
paths: ["**/*.md", "**/*.rst"]
labels: ["documentation"]
priority: 80
---

# Documentation Validator Agent

You are a Documentation Validator Agent, responsible for ensuring documentation quality and correctness.

## Core Responsibilities

1. **Quality Checks**: Verify documentation follows style guidelines
2. **Consistency Checks**: Ensure consistent terminology and formatting
3. **Completeness Checks**: Identify missing information or sections
4. **Technical Accuracy**: Verify technical information is correct

## Validation Criteria

When reviewing documentation, check for:

- Adherence to the style guide in CLAUDE.md
- Consistent terminology and capitalization
- Complete coverage of features and concepts
- Clear examples and code snippets
- Proper formatting and structure
- Valid links and references
```

### Build Fixer Agent Configuration

```yaml
# .a5c/agents/build-fixer-agent.agent.md
---
name: build-fixer-agent
version: 1.0.0
category: development
description: Documentation build fixer

events: ["workflow_run.failed"]
priority: 90
---

# Documentation Build Fixer Agent

You are a Documentation Build Fixer Agent, responsible for resolving documentation build failures.

## Core Responsibilities

1. **Build Error Analysis**: Identify the cause of documentation build failures
2. **Syntax Fixing**: Correct syntax errors in Markdown or reStructuredText
3. **Reference Resolution**: Fix broken references and links
4. **Structure Repair**: Correct structural issues in documentation

## Resolution Process

When fixing documentation build issues:

1. Analyze build logs to identify specific errors
2. Locate the problematic files and sections
3. Make targeted fixes to resolve the issues
4. Verify the build succeeds after your changes
```

## CI Workflow Process

A typical documentation CI workflow with A5C follows these steps:

### 1. Continuous Validation

The validator-agent continuously checks documentation quality:

```
@validator-agent

Please review the documentation changes in this PR for:
- Style guide compliance
- Terminology consistency
- Technical accuracy
- Completeness
```

### 2. Build Verification

The GitHub Actions workflow attempts to build the documentation on every change.

### 3. Automated Fixes

If the build fails, the build-fixer-agent automatically:
- Analyzes the build logs
- Identifies the issues
- Creates a PR with fixes

### 4. Content Updates

When code changes require documentation updates, the content-writer-agent is triggered:

```
@content-writer-agent

The API has changed in the following ways:
- New endpoint: /api/v1/users/{id}/preferences
- Changed parameter: 'sort_by' now accepts 'created_at' value
- Deprecated: /api/v1/legacy/user-settings

Please update the API documentation to reflect these changes.
```

### 5. Technical Review

The developer-agent verifies technical accuracy:

```
@developer-agent

Please review the technical accuracy of the installation instructions for Linux systems.
```

## Best Practices

For effective documentation CI with A5C:

1. **Define Clear Style Guidelines**: Document your style expectations in CLAUDE.md
2. **Use Branch Protection**: Require documentation builds to pass before merging
3. **Set Up Scheduled Validation**: Run periodic full documentation checks
4. **Implement Version Tagging**: Tag documentation to align with software versions
5. **Track Documentation Coverage**: Ensure all features have documentation

## Metrics and Monitoring

Track these metrics to monitor documentation health:

- **Build Success Rate**: Percentage of successful documentation builds
- **Quality Score**: Based on validator-agent findings
- **Coverage Percentage**: Features with complete documentation
- **Update Frequency**: How often documentation is updated
- **User Feedback**: User ratings on documentation usefulness

## Troubleshooting

Common issues and solutions for documentation CI:

### Failed Builds

If documentation builds fail consistently:
- Check syntax in recently modified files
- Verify that all referenced files exist
- Ensure configuration files are correct

### Inconsistent Validation

If validator results are inconsistent:
- Update the validator agent's instructions
- Provide more specific validation criteria
- Add examples of preferred documentation

### Integration Issues

If A5C agents aren't triggering properly:
- Check the workflow configuration
- Verify that file paths are correct
- Ensure agents have appropriate permissions

## Next Steps

- Set up [Content Creation Workflows](content-creation-workflows.md)
- Learn about [Customizing Agent Behavior](customizing-agent-behavior.md)
- Explore [Using MCP Servers](using-mcp-servers.md) for additional integrations