---

CI/CD That Thinks: Background Agents for Real Work, Not Just Build Scripts
Most pipelines automate steps.
 What if they could automate the thinking behind those steps?

---

From Scripts to Sentient Pipelines
Continuous Integration once meant "run tests, show green ticks."
 With a5c, your pipeline becomes a team of AI teammates that review, fix, document, and even ship code - all while you stay in the driver's seat. The agents do the leg-work; you approve the pull requests.

---

Git: The Nervous System
Everything the agents know, do, and learn lives in one place - your Git repo:
Agent definitions are version-controlled like source files.
Prompts are pull-request-reviewed, so anyone can improve them.
Workflow rules sit next to code, fully transparent.

Because the intelligence is stored where the code is stored, your CI becomes a system of record for the thinking behind the code, not just the code itself.

---

One Job, Dozens of Helpers
Add a single step to any existing workflow:
jobs:
  run-agents:
    uses: a5c/action
That's it. The job consults .a5c/config.yml, sees which agents you've enabled, and triggers them on pull-requests, issue comments, or a schedule you choose. No new tooling, no brittle scripts-just plug and play.

---

Meet Your New Teammates
✅ Code-Reviewer
Trigger: pull_request
 Reads the diff and surrounding context, flags logic holes, suggests edge-cases, comments inline.
🔧 Build-Fixer
Trigger: failed CI run or comment @fixer
 Parses logs, diagnoses the break, proposes or pushes a patch.
🧾 Doc-Writer & Changelog-Bot
Trigger: label documentation or on release tag
 Scans commits, drafts API docs and release notes in Markdown ready for review.
🛡 Security-Auditor (Scheduled)
Trigger: cron, e.g. every Monday 09:00
 Checks for vulnerable deps and patterns, files issues for anything risky.
Agents inherit behaviors (like Docker layers) and can call each other - so the reviewer can summon the fixer, the seeder can recruit the doc-writer. CI starts to feel like a live chat where bots do real work.

---

Smart Defaults, Simple Config
Enable an agent by pointing to its URL:
agents:
  - https://registry.a5c.ai/agents/code-reviewer.agent.md
  - https://registry.a5c.ai/agents/security-auditor.agent.md
Need a custom flavor? Create a new file that says:
name: frontend-reviewer
from: code-reviewer
prompt: |
  {{base-prompt}}
  Additionally, enforce our company's React style guide.
Commit, push, done. Every tweak is tracked, every improvement is shared.

---

Prompts Are Infrastructure
In most teams, a great prompt dies in a DM or notebook.
 With a5c the prompt is the agent, and it's:
Versioned - rollback or diff like code.
Reviewed - merged only after PR approval.
Reusable - inherited by future agents.

Prompt engineering finally moves from tribal lore to shared, auditable infrastructure.

---

Open-Source and Un-boxed
a5c is open source end-to-end. No black-box SaaS, no API ceiling, no vendor lock-in. Fork it, audit it, run it on-prem or in the cloud - it's yours.

---

Continuous Integration Meets Continuous Intelligence
Put up a pull request; watch agents review, patch, and document while you sip coffee.
 CI no longer stops at a green check - it thinks.
Ready to add brains to your builds?
→ Star the repo, drop the step in, and join the community at a5c.ai.