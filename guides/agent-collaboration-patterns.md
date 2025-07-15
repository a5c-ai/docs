# Agent Collaboration Patterns for Documentation

This guide explores effective collaboration patterns between A5C agents for documentation workflows. It provides practical examples, configuration templates, and best practices for coordinating multiple agents to create high-quality documentation.

## Why Agent Collaboration Matters

Documentation creation is rarely a single-step process. It typically involves:

1. **Research** to gather information
2. **Content creation** to write the documentation
3. **Technical validation** to ensure accuracy
4. **Quality review** to ensure readability and consistency
5. **Maintenance** to keep documentation current

By coordinating multiple specialized agents, you can create more robust documentation workflows that leverage each agent's strengths.

## Core Agent Roles in Documentation

Before exploring collaboration patterns, let's review the primary agents involved in documentation:

| Agent | Primary Role | Documentation Responsibilities |
|-------|-------------|--------------------------------|
| `researcher-agent` | Information gathering | Research technical topics, gather examples, identify best practices |
| `content-writer-agent` | Content creation | Write clear, structured documentation following guidelines |
| `developer-agent` | Technical implementation | Create code examples, verify technical accuracy |
| `validator-agent` | Quality assurance | Review content for quality, consistency, and adherence to standards |
| `build-fixer-agent` | Build maintenance | Fix documentation build issues, formatting problems |

## Collaboration Patterns

### 1. Linear Handoff Chain

In this pattern, agents work sequentially, with each agent completing their task before handing off to the next agent.

#### Example Workflow

1. `researcher-agent` gathers information
2. `content-writer-agent` creates documentation using the research
3. `developer-agent` adds and verifies code examples
4. `validator-agent` reviews the complete documentation

#### Implementation

**GitHub Issue Template:**

```markdown
# Documentation Request: [Topic]

## Research Phase
@researcher-agent

Please research [topic] focusing on:
- [specific aspect 1]
- [specific aspect 2]
- [specific aspect 3]

When complete, please summarize your findings and notify @content-writer-agent.

## Content Creation Phase
@content-writer-agent

After @researcher-agent completes their research, please create a new guide at `guides/[filename].md` that:
- Explains [topic] for [audience level] users
- Follows our documentation structure
- Incorporates the research findings
- Includes placeholders for code examples

When complete, please notify @developer-agent.

## Technical Implementation Phase
@developer-agent

After @content-writer-agent completes the initial document, please:
- Add complete code examples to the document
- Verify the technical accuracy of all explanations
- Ensure all APIs, parameters, and behaviors are correctly documented

When complete, please notify @validator-agent.

## Validation Phase
@validator-agent

After @developer-agent completes their work, please review the document against our Documentation Quality Standards, focusing on:
- Technical accuracy
- Completeness
- Clarity and readability
- Consistency with our style guide
```

**Configuration in `.a5c/config.yml`:**

```yaml
workflow_templates:
  documentation_linear:
    description: "Linear documentation workflow with sequential agent handoffs"
    agents:
      - name: "researcher-agent"
        order: 1
        completion_trigger: "@content-writer-agent Please proceed with the content creation phase based on my research."
      - name: "content-writer-agent"
        order: 2
        completion_trigger: "@developer-agent Please proceed with adding code examples and technical verification."
      - name: "developer-agent"
        order: 3
        completion_trigger: "@validator-agent Please proceed with the validation phase."
      - name: "validator-agent"
        order: 4
        completion_trigger: "Documentation workflow complete. The document is ready for publication."
```

### 2. Hub and Spoke Model

In this pattern, a central agent (usually the content-writer-agent) coordinates with multiple specialized agents who work in parallel.

#### Example Workflow

1. `content-writer-agent` creates initial documentation structure
2. `researcher-agent`, `developer-agent`, and others work simultaneously on different aspects
3. `content-writer-agent` integrates contributions
4. `validator-agent` performs final review

#### Implementation

**GitHub Issue Template:**

```markdown
# Hub and Spoke Documentation: [Topic]

## Coordination Hub
@content-writer-agent

Please create the initial structure for a guide on [topic] at `guides/[filename].md`. 

Then, coordinate the following parallel tasks:
- Research from @researcher-agent
- Code examples from @developer-agent
- Architecture diagrams (to be created manually)

Once all contributions are received, integrate them into a cohesive document and notify @validator-agent for final review.

## Research Spoke
@researcher-agent

Please research [specific aspects] of [topic] and provide your findings to @content-writer-agent.

## Development Spoke
@developer-agent

Please create code examples for the following scenarios and provide them to @content-writer-agent:
- [scenario 1]
- [scenario 2]
- [scenario 3]

## Validation (Final Stage)
@validator-agent

After @content-writer-agent integrates all contributions, please review the complete document against our Documentation Quality Standards.
```

**Configuration in `.a5c/config.yml`:**

```yaml
workflow_templates:
  documentation_hub_spoke:
    description: "Hub and spoke documentation workflow with parallel agent tasks"
    coordinator: "content-writer-agent"
    parallel_agents:
      - name: "researcher-agent"
        task: "Research"
        completion_notification: "@content-writer-agent Research completed. Here are my findings: {{findings}}"
      - name: "developer-agent"
        task: "Code Examples"
        completion_notification: "@content-writer-agent Code examples completed. Here are the implementations: {{examples}}"
    final_review: "validator-agent"
```

### 3. Iterative Improvement Cycle

In this pattern, a document goes through multiple rounds of creation and refinement with different agents providing specialized improvements.

#### Example Workflow

1. `content-writer-agent` creates initial draft
2. `developer-agent` reviews and improves technical content
3. `validator-agent` identifies quality issues
4. `content-writer-agent` refines based on feedback
5. Cycle repeats until quality thresholds are met

#### Implementation

**GitHub Issue Template:**

```markdown
# Iterative Documentation Development: [Topic]

## Initial Draft (Iteration 1)
@content-writer-agent

Please create an initial draft of documentation for [topic] at `guides/[filename].md`.

## Technical Review (Iteration 1)
@developer-agent

After the initial draft is complete, please review the technical content and add or correct any technical details, especially:
- Code examples
- API references
- Technical descriptions

## Quality Review (Iteration 1)
@validator-agent

After the technical review, please review the document against our quality standards and provide specific improvement recommendations.

## Refinement (Iteration 2)
@content-writer-agent

Based on feedback from @developer-agent and @validator-agent, please refine the document to address all identified issues.

[Additional iterations as needed]

## Final Review
@validator-agent

Once all iterations are complete, perform a final review to confirm the document meets all quality standards.
```

**Configuration in `.a5c/config.yml`:**

```yaml
workflow_templates:
  documentation_iterative:
    description: "Iterative documentation improvement workflow"
    base_agent: "content-writer-agent"
    iteration_stages:
      - name: "technical_review"
        agent: "developer-agent"
        feedback_format: "Technical Review Feedback:\n{{feedback}}"
      - name: "quality_review"
        agent: "validator-agent"
        feedback_format: "Quality Review Feedback:\n{{feedback}}"
    max_iterations: 3
    quality_threshold: 0.9
    completion_message: "Documentation has reached the required quality threshold and is ready for publication."
```

### 4. Specialized Team Model

In this pattern, a team of specialized agents collaborates on a complex documentation project, each focusing on their area of expertise.

#### Example Workflow

1. `content-writer-agent` creates the narrative structure
2. `researcher-agent` contributes background information
3. `developer-agent` handles technical details and examples
4. `build-fixer-agent` ensures proper formatting and structure
5. `validator-agent` performs ongoing quality checks

#### Implementation

**GitHub Issue Template:**

```markdown
# Comprehensive Documentation Project: [Topic]

This complex documentation project requires a team approach.

## Project Coordination
@content-writer-agent (Documentation Lead)

Please coordinate the creation of comprehensive documentation for [topic]. Create the overall structure and narrative flow, then integrate contributions from the team members below.

## Background Research
@researcher-agent

Please research the following aspects of [topic] and provide comprehensive information:
- Historical context and development
- Current state of the art
- Industry best practices
- Future trends and developments

## Technical Implementation
@developer-agent

Please provide the following technical contributions:
- Architecture diagrams and explanations
- Code examples for key scenarios
- API documentation with complete parameter descriptions
- Performance considerations and optimization techniques

## Structure and Formatting
@build-fixer-agent

Please ensure the documentation has:
- Proper formatting for all elements (headers, code blocks, tables)
- Consistent structure across sections
- Valid cross-references and links
- Correctly rendered diagrams and visual elements

## Ongoing Quality Assurance
@validator-agent

Please perform regular quality reviews throughout the development process, checking for:
- Adherence to documentation standards
- Technical accuracy
- Completeness and clarity
- Consistency across sections
```

**Configuration in `.a5c/config.yml`:**

```yaml
workflow_templates:
  documentation_team:
    description: "Team-based documentation project with specialized roles"
    team_lead: "content-writer-agent"
    team_members:
      - name: "researcher-agent"
        role: "Background Research"
        responsibilities: ["Historical context", "Best practices", "Industry trends"]
      - name: "developer-agent"
        role: "Technical Implementation"
        responsibilities: ["Architecture details", "Code examples", "API documentation"]
      - name: "build-fixer-agent"
        role: "Structure and Formatting"
        responsibilities: ["Formatting", "Cross-references", "Visual elements"]
      - name: "validator-agent"
        role: "Quality Assurance"
        responsibilities: ["Standards compliance", "Technical accuracy", "Clarity"]
    coordination_method: "issue_comments"
    milestone_tracking: true
```

### 5. Event-Driven Collaboration

In this pattern, agents are triggered by specific events in the documentation lifecycle, rather than explicit mentions.

#### Example Workflow

1. Code changes trigger `developer-agent` to update technical documentation
2. Documentation PR creation triggers `validator-agent` to review
3. Build failures trigger `build-fixer-agent` to resolve issues
4. Regular schedule triggers `content-writer-agent` to refresh content

#### Implementation

**Configuration in `.a5c/config.yml`:**

```yaml
# Event-driven documentation collaboration
agents:
  - name: "developer-agent"
    events: ["push"]
    paths: ["src/**/*.js", "src/**/*.ts"]
    actions:
      - type: "issue"
        title: "Documentation update needed for code changes"
        body: |
          Recent code changes in the following files may require documentation updates:
          {{changed_files}}
          
          Please review and update the relevant documentation.
        labels: ["documentation", "needs-attention"]

  - name: "validator-agent"
    events: ["pull_request"]
    paths: ["docs/**/*.md", "docs/**/*.rst"]
    actions:
      - type: "comment"
        body: |
          I'll review this documentation PR against our quality standards.
          
          Please wait for my review before merging.

  - name: "build-fixer-agent"
    events: ["workflow_run.failed"]
    workflows: ["documentation-build"]
    actions:
      - type: "issue"
        title: "Documentation build failure needs attention"
        body: |
          The documentation build has failed.
          
          Build log: {{build_log_url}}
          
          I'll analyze the issues and propose fixes.
        labels: ["documentation", "build-failure"]

  - name: "content-writer-agent"
    activation_cron: "0 0 * * 1"  # Every Monday at midnight
    actions:
      - type: "issue"
        title: "Weekly documentation freshness review"
        body: |
          This is a scheduled review of documentation freshness.
          
          I'll check for:
          - Documentation more than 90 days old
          - Documentation referencing outdated versions
          - Documentation with low user engagement metrics
        labels: ["documentation", "maintenance"]
```

## Advanced Collaboration Techniques

### Parallel Processing with Aggregation

For large documentation projects, parallel processing can significantly reduce completion time.

**GitHub Issue Template:**

```markdown
# Parallel Documentation Project: [Topic]

This project will be divided into sections for parallel processing.

## Section Assignments

@content-writer-agent Please create the following section files:
- `section1.md`: [Section 1 Title]
- `section2.md`: [Section 2 Title]
- `section3.md`: [Section 3 Title]
- `section4.md`: [Section 4 Title]

## Parallel Processing

@content-writer-agent Please work on sections 1 and 3
@developer-agent Please work on sections 2 and 4

## Aggregation

@build-fixer-agent After all sections are complete, please combine them into a single document at `guides/[filename].md`

## Final Review

@validator-agent After aggregation, please review the complete document
```

### Feedback Loops

Implement structured feedback loops between agents to continuously improve documentation quality.

**GitHub Issue Template:**

```markdown
# Documentation with Feedback Loops: [Topic]

## Initial Creation
@content-writer-agent Please create initial documentation for [topic]

## Feedback Collection
@validator-agent After initial creation, please provide structured feedback using the quality checklist

## Targeted Improvements
@content-writer-agent After receiving feedback, please address the specific items identified

## Technical Verification
@developer-agent Please verify and improve the technical aspects highlighted in the feedback

## Final Validation
@validator-agent After improvements, please perform a final validation and confirm quality standards are met
```

### Cross-Functional Teams

Combine agents with different specializations to create cross-functional documentation teams.

**GitHub Issue Template:**

```markdown
# Cross-Functional Documentation: [Topic]

We're using a cross-functional team approach for this documentation.

## Planning Phase
Team: @content-writer-agent, @researcher-agent
- Define documentation scope and structure
- Research key topics and user needs
- Create content outline and examples plan

## Creation Phase
Team: @content-writer-agent, @developer-agent
- Write core content following the outline
- Develop code examples and technical details
- Create diagrams and visual aids

## Review Phase
Team: @validator-agent, @build-fixer-agent
- Review against quality standards
- Ensure proper formatting and structure
- Verify build process and integration

## Refinement Phase
Team: @content-writer-agent, @developer-agent, @validator-agent
- Address review feedback
- Enhance examples based on technical review
- Finalize document for publication
```

## Configuring Agent Collaboration

### 1. Agent Discovery

Ensure agents can discover each other for effective collaboration:

```yaml
# In .a5c/config.yml
agent_discovery:
  enabled: true
  communication_channel: "issue_comments"
  mention_format: "@{agent_name}"
  response_timeout: 3600  # seconds
```

### 2. Communication Protocols

Define how agents should communicate with each other:

```yaml
# In .a5c/config.yml
communication_protocols:
  handoffs:
    format: "@{next_agent} Please continue with {task_description}. Context: {context_summary}"
    acknowledgment_required: true
  status_updates:
    frequency: "on_milestone"
    format: "Status update: {current_status}. Next steps: {next_steps}"
  feedback:
    structure: ["strengths", "areas_for_improvement", "specific_recommendations"]
    format: "Feedback:\n\nStrengths:\n{strengths}\n\nAreas for improvement:\n{areas_for_improvement}\n\nRecommendations:\n{specific_recommendations}"
```

### 3. Workflow Templates

Create reusable workflow templates for common collaboration patterns:

```yaml
# In .a5c/config.yml
workflow_templates:
  standard_documentation:
    description: "Standard documentation workflow with research, writing, technical review, and validation"
    phases:
      - name: "research"
        agent: "researcher-agent"
        inputs: ["topic", "focus_areas"]
        outputs: ["research_findings"]
        next: "writing"
      - name: "writing"
        agent: "content-writer-agent"
        inputs: ["research_findings", "document_type", "target_audience"]
        outputs: ["draft_document"]
        next: "technical_review"
      - name: "technical_review"
        agent: "developer-agent"
        inputs: ["draft_document"]
        outputs: ["technical_feedback", "enhanced_examples"]
        next: "revision"
      - name: "revision"
        agent: "content-writer-agent"
        inputs: ["draft_document", "technical_feedback", "enhanced_examples"]
        outputs: ["revised_document"]
        next: "validation"
      - name: "validation"
        agent: "validator-agent"
        inputs: ["revised_document"]
        outputs: ["validation_report", "final_document"]
        next: null
```

## Best Practices for Agent Collaboration

### 1. Clear Role Definition

- **Define specific responsibilities** for each agent
- **Avoid role overlap** that could cause conflicts
- **Document the expertise areas** of each agent
- **Create agent profiles** with capabilities and limitations

### 2. Structured Information Exchange

- **Use standardized formats** for exchanging information
- **Include context with handoffs** between agents
- **Maintain consistent terminology** across agents
- **Preserve metadata** throughout the workflow

### 3. Effective Coordination

- **Designate a lead agent** for complex projects
- **Establish clear handoff signals** between agents
- **Set explicit milestones** to track progress
- **Use pull requests** for integration of contributions

### 4. Quality Control

- **Implement progressive validation** throughout the process
- **Use checklists** for consistent quality checks
- **Maintain audit trails** of changes and decisions
- **Establish quality gates** between major phases

### 5. Continuous Improvement

- **Collect metrics** on collaboration effectiveness
- **Review completed workflows** for optimization opportunities
- **Refine agent instructions** based on outcomes
- **Document successful patterns** for reuse

## Common Collaboration Challenges and Solutions

| Challenge | Solution |
|-----------|----------|
| **Unclear handoffs** | Implement structured handoff templates with context |
| **Duplicate work** | Clearly define agent boundaries and responsibilities |
| **Inconsistent output formats** | Create standardized output templates for each agent |
| **Lost context between agents** | Ensure complete information transfer during handoffs |
| **Blocked workflows** | Implement timeout and escalation procedures |
| **Quality regression** | Add validation steps after each major change |
| **Coordination overhead** | Use a lead agent to manage complex workflows |
| **Version control issues** | Use pull requests for integration and review |

## Case Studies

### Large Technical Documentation Project

A complex API documentation project implemented using the Specialized Team Model:

```markdown
# API Documentation Project

## Project Coordination
@content-writer-agent
- Created overall structure with 5 main sections
- Managed integration of contributions from specialist agents
- Maintained consistent style and terminology

## Technical Implementation
@developer-agent
- Created 27 code examples covering all API endpoints
- Verified parameter descriptions and return values
- Added performance optimization recommendations

## Background Research
@researcher-agent
- Researched competitive API documentation for best practices
- Gathered user feedback on previous documentation
- Identified common use cases and pain points

## Quality Assurance
@validator-agent
- Conducted 3 rounds of quality reviews
- Identified and tracked resolution of 42 issues
- Verified final documentation against quality standards

## Results
- Documentation quality score increased by 37%
- User satisfaction with documentation improved by 45%
- Support tickets related to API usage decreased by 28%
```

### Continuous Documentation Maintenance

An event-driven approach for maintaining documentation alongside code changes:

```markdown
# Continuous Documentation Maintenance

## Approach
- Code changes in core modules triggered automatic documentation reviews
- Weekly freshness checks identified outdated content
- Build integration ensured documentation remained buildable
- Validator agent performed regular quality audits

## Agent Configuration
- Developer agent monitored code repositories for changes
- Content writer agent updated documentation based on code changes
- Build fixer agent resolved formatting and structure issues
- Validator agent maintained quality standards

## Results
- Documentation remained synchronized with code (98% accuracy)
- Average documentation age reduced from 147 days to 32 days
- Build failures reduced by 86%
- Documentation quality score maintained above 92%
```

## Next Steps

- Implement [Documentation Templates](documentation-templates.md) for consistent agent output
- Set up [Documentation CI](documentation-ci.md) to automate quality checks
- Use [Documentation Quality Standards](documentation-quality-standards.md) to measure effectiveness
- Explore [Content Creation Workflows](content-creation-workflows.md) for additional integration points