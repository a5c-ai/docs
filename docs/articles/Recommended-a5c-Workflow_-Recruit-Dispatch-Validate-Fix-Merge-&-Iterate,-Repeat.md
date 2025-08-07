---

Recommended a5c Workflow: Recruit, Dispatch, Validate/Fix, Merge & Iterate, Repeat
Tal’s recommended sequence of phases for orchestrating a5c agents, with examples showing how to mention and use each agent at every step.

---

1 ▸ Recruit Phase

Kick off the workflow by recruiting tasks from your codebase. The recruiter agent scans changes and builds a backlog of work items.

```text
@recruiter-agent: scan the repository and list pending features, bug fixes, and documentation updates
```

Example backlog entries:

```text
Backlog:
- Add user authentication support
- Refactor API client for better error handling
- Update README with setup instructions
```

2 ▸ Dispatch Tasks

Assign each backlog item to the right agent for execution. The dispatcher agent creates issues and routes work.

```text
@dispatcher-agent: dispatch each task in BACKLOG.md to the appropriate AI agent and open corresponding issues
```

This produces:

- Issue #23 “Implement authentication module” assigned to @dev-agent  
- Issue #24 “Generate API client docs” assigned to @doc-agent

3 ▸ Validate / Fix

After agents complete tasks, run validation and automated fixes. The validator agent reviews outputs, runs tests, and applies patches.

```text
@validator-agent: run the test suite on the latest commits and fix any failing tests or lint errors
```

Resulting patches may include:

- Linting and formatting corrections  
- Test suite fixes and coverage enforcement  
- Documentation typo fixes

4 ▸ Merge & Iterate

Merge validated changes and trigger the next cycle. The merger agent opens pull requests, merges approved work, and reports status.

```text
@merger-agent: open a pull request for validated changes, merge on approval, and report the merge status
```

Every merge triggers the recruit phase again, enabling continuous improvement.

5 ▸ Repeat

Schedule or trigger the workflow loop automatically. The loop agent initiates each new cycle at defined intervals or after significant changes.

```text
@loop-agent: schedule the recruit-dispatch-validate-merge cycle to run every 24 hours or on every main branch update
```

This ensures your repository evolves continuously with minimal manual effort.
