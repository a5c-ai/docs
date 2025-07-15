# A5C Project Structures

This document provides examples of different project structures optimized for A5C integration. These examples demonstrate how to organize your repository to effectively use A5C agents in various types of projects.

## Basic Web Application

This example shows a typical structure for a web application with A5C integration:

```
project-root/
├── .a5c/
│   ├── config.yml                 # A5C global configuration
│   ├── agents/                    # Custom agents directory
│   │   ├── frontend-reviewer.agent.md
│   │   └── backend-reviewer.agent.md
│   └── memory/                    # Agent memory storage
├── .github/
│   └── workflows/
│       └── a5c.yml                # A5C GitHub Actions workflow
├── src/
│   ├── components/                # React components
│   ├── pages/                     # Next.js pages
│   ├── styles/                    # CSS/SCSS files
│   ├── utils/                     # Utility functions
│   └── api/                       # API routes
├── public/                        # Static assets
├── tests/                         # Test files
├── .gitignore
├── package.json
└── README.md
```

### Key A5C Configuration Files

**`.a5c/config.yml`**:
```yaml
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

# MCP Server Configuration
mcp_servers:
  github:
    enabled: true
  filesystem:
    enabled: true
  npm:
    enabled: true

# Agent Discovery Settings
agent_discovery:
  enabled: true
  max_agents_in_context: 5

# Agent Configuration
agents:
  local:
    enabled: true
    paths:
      - ".a5c/agents/*.agent.md"
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/frontend/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/backend/*.agent.md"
```

**`.github/workflows/a5c.yml`**:
```yaml
name: A5C
on:
  pull_request:
    types: [opened, synchronize]
  issues:
    types: [opened, edited]
  issue_comment:
    types: [created]
  push:
    branches: [main, develop]

jobs:
  a5c:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Run A5C Agents
        uses: a5c-ai/action@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          config_file: ".a5c/config.yml"
```

## Microservices Architecture

This example demonstrates a microservices project structure with A5C integration:

```
project-root/
├── .a5c/
│   ├── config.yml                 # A5C global configuration
│   ├── agents/                    # Custom agents directory
│   │   ├── api-gateway-agent.agent.md
│   │   ├── auth-service-agent.agent.md
│   │   └── monitoring-agent.agent.md
│   └── memory/                    # Agent memory storage
├── .github/
│   └── workflows/
│       └── a5c.yml                # A5C GitHub Actions workflow
├── services/
│   ├── api-gateway/               # API Gateway service
│   │   ├── src/
│   │   ├── Dockerfile
│   │   └── package.json
│   ├── auth-service/              # Authentication service
│   │   ├── src/
│   │   ├── Dockerfile
│   │   └── package.json
│   ├── user-service/              # User management service
│   │   ├── src/
│   │   ├── Dockerfile
│   │   └── package.json
│   └── notification-service/      # Notification service
│       ├── src/
│       ├── Dockerfile
│       └── package.json
├── docker-compose.yml             # Docker Compose configuration
├── kubernetes/                    # Kubernetes manifests
│   ├── api-gateway.yaml
│   ├── auth-service.yaml
│   ├── user-service.yaml
│   └── notification-service.yaml
├── .gitignore
└── README.md
```

### Key A5C Configuration Files

**`.a5c/config.yml`**:
```yaml
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

# System Settings
system:
  log_level: info
  execution_mode: parallel
  max_concurrent_agents: 8
  timeout: 120

# Service-specific configurations
categories:
  api_gateway:
    priority: 80
    paths: ["services/api-gateway/**/*"]
    mcp_servers: ["github", "filesystem", "docker", "kubernetes"]
  
  auth_service:
    priority: 85
    paths: ["services/auth-service/**/*"]
    mcp_servers: ["github", "filesystem", "docker", "database"]
  
  user_service:
    priority: 70
    paths: ["services/user-service/**/*"]
    mcp_servers: ["github", "filesystem", "docker", "database"]
  
  notification_service:
    priority: 65
    paths: ["services/notification-service/**/*"]
    mcp_servers: ["github", "filesystem", "docker", "messaging"]

# MCP Server Configuration
mcp_servers:
  github:
    enabled: true
  filesystem:
    enabled: true
  docker:
    enabled: true
    image_registry: "gcr.io/my-project"
  kubernetes:
    enabled: true
    context: "dev-cluster"
  database:
    enabled: true
    type: "postgres"
  messaging:
    enabled: true
    type: "kafka"

# Agent Configuration
agents:
  local:
    enabled: true
    paths:
      - ".a5c/agents/*.agent.md"
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/microservices/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/devops/*.agent.md"
```

## Machine Learning Project

This example shows a machine learning project structure with A5C integration:

```
project-root/
├── .a5c/
│   ├── config.yml                 # A5C global configuration
│   ├── agents/                    # Custom agents directory
│   │   ├── data-validator.agent.md
│   │   ├── model-trainer.agent.md
│   │   └── evaluation-agent.agent.md
│   └── memory/                    # Agent memory storage
├── .github/
│   └── workflows/
│       ├── a5c.yml                # A5C GitHub Actions workflow
│       └── model-training.yml     # Model training workflow
├── data/
│   ├── raw/                       # Raw data files
│   ├── processed/                 # Processed data files
│   └── external/                  # External data sources
├── notebooks/                     # Jupyter notebooks
│   ├── exploration/
│   ├── preprocessing/
│   └── evaluation/
├── src/
│   ├── data/                      # Data processing scripts
│   │   ├── make_dataset.py
│   │   └── preprocess.py
│   ├── features/                  # Feature engineering
│   │   └── build_features.py
│   ├── models/                    # Model definitions
│   │   ├── train_model.py
│   │   └── predict_model.py
│   └── visualization/             # Visualization scripts
│       └── visualize.py
├── models/                        # Saved model files
│   ├── trained/
│   └── deployed/
├── configs/                       # Model configurations
│   ├── model_config.yaml
│   └── hyperparameters.yaml
├── tests/                         # Test files
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

### Key A5C Configuration Files

**`.a5c/config.yml`**:
```yaml
version: 1.0.0
settings:
  model: claude-3-opus-20240229  # Using a more powerful model for ML tasks
  verbose: true

# System Settings
system:
  log_level: debug
  execution_mode: parallel
  max_concurrent_agents: 3
  timeout: 300  # Longer timeout for complex ML tasks

# ML-specific configurations
categories:
  data_preprocessing:
    priority: 85
    paths: ["data/**/*", "src/data/**/*", "notebooks/preprocessing/**/*"]
    mcp_servers: ["github", "filesystem", "data_warehouse"]
  
  model_training:
    priority: 90
    paths: ["src/models/**/*", "configs/**/*", "notebooks/training/**/*"]
    mcp_servers: ["github", "filesystem", "ml_platform", "experiment_tracker"]
  
  evaluation:
    priority: 80
    paths: ["src/visualization/**/*", "notebooks/evaluation/**/*"]
    mcp_servers: ["github", "filesystem", "ml_platform", "experiment_tracker"]

# MCP Server Configuration
mcp_servers:
  github:
    enabled: true
  filesystem:
    enabled: true
  data_warehouse:
    enabled: true
    type: "snowflake"
  ml_platform:
    enabled: true
    type: "sagemaker"
  experiment_tracker:
    enabled: true
    type: "mlflow"

# Agent Configuration
agents:
  local:
    enabled: true
    paths:
      - ".a5c/agents/*.agent.md"
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/machine-learning/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/data-science/*.agent.md"
```

## Mobile Application

This example demonstrates a mobile application project structure with A5C integration:

```
project-root/
├── .a5c/
│   ├── config.yml                 # A5C global configuration
│   ├── agents/                    # Custom agents directory
│   │   ├── ios-reviewer.agent.md
│   │   ├── android-reviewer.agent.md
│   │   └── ui-ux-reviewer.agent.md
│   └── memory/                    # Agent memory storage
├── .github/
│   └── workflows/
│       ├── a5c.yml                # A5C GitHub Actions workflow
│       ├── ios-build.yml          # iOS build workflow
│       └── android-build.yml      # Android build workflow
├── src/
│   ├── common/                    # Shared code
│   │   ├── components/            # Shared UI components
│   │   ├── services/              # Shared services
│   │   └── utils/                 # Utility functions
│   ├── ios/                       # iOS-specific code
│   │   ├── MyApp/
│   │   ├── MyAppTests/
│   │   └── MyApp.xcodeproj/
│   └── android/                   # Android-specific code
│       ├── app/
│       ├── gradle/
│       └── build.gradle
├── assets/                        # Shared assets
│   ├── images/
│   ├── fonts/
│   └── animations/
├── docs/                          # Documentation
│   ├── ios/
│   └── android/
├── tests/                         # Cross-platform tests
├── .gitignore
└── README.md
```

### Key A5C Configuration Files

**`.a5c/config.yml`**:
```yaml
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

# Platform-specific configurations
categories:
  ios:
    priority: 80
    paths: ["src/ios/**/*"]
    mcp_servers: ["github", "filesystem", "xcode"]
  
  android:
    priority: 80
    paths: ["src/android/**/*"]
    mcp_servers: ["github", "filesystem", "gradle"]
  
  common:
    priority: 85
    paths: ["src/common/**/*"]
    mcp_servers: ["github", "filesystem"]

# MCP Server Configuration
mcp_servers:
  github:
    enabled: true
  filesystem:
    enabled: true
  xcode:
    enabled: true
  gradle:
    enabled: true

# Agent Configuration
agents:
  local:
    enabled: true
    paths:
      - ".a5c/agents/*.agent.md"
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/mobile/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/ios/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/android/*.agent.md"
```

## Monorepo Structure

This example shows a monorepo project structure with A5C integration:

```
project-root/
├── .a5c/
│   ├── config.yml                 # A5C global configuration
│   ├── agents/                    # Custom agents directory
│   │   ├── frontend-reviewer.agent.md
│   │   ├── backend-reviewer.agent.md
│   │   └── documentation-agent.agent.md
│   └── memory/                    # Agent memory storage
├── .github/
│   └── workflows/
│       ├── a5c.yml                # A5C GitHub Actions workflow
│       └── ci.yml                 # CI workflow
├── packages/
│   ├── core/                      # Core shared library
│   │   ├── src/
│   │   ├── tests/
│   │   └── package.json
│   ├── ui/                        # UI component library
│   │   ├── src/
│   │   ├── stories/
│   │   ├── tests/
│   │   └── package.json
│   ├── api/                       # API server
│   │   ├── src/
│   │   ├── tests/
│   │   └── package.json
│   ├── web-app/                   # Web application
│   │   ├── src/
│   │   ├── public/
│   │   ├── tests/
│   │   └── package.json
│   └── mobile-app/                # Mobile application
│       ├── src/
│       ├── assets/
│       ├── tests/
│       └── package.json
├── tools/                         # Development tools
│   ├── scripts/
│   ├── config/
│   └── templates/
├── docs/                          # Documentation
│   ├── api/
│   ├── ui/
│   ├── web/
│   └── mobile/
├── .gitignore
├── package.json
├── lerna.json
└── README.md
```

### Key A5C Configuration Files

**`.a5c/config.yml`**:
```yaml
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

# System Settings
system:
  log_level: info
  execution_mode: parallel
  max_concurrent_agents: 8
  timeout: 120

# Package-specific configurations
categories:
  core:
    priority: 90
    paths: ["packages/core/**/*"]
    mcp_servers: ["github", "filesystem", "npm"]
  
  ui:
    priority: 85
    paths: ["packages/ui/**/*"]
    mcp_servers: ["github", "filesystem", "npm", "storybook"]
  
  api:
    priority: 80
    paths: ["packages/api/**/*"]
    mcp_servers: ["github", "filesystem", "npm", "database"]
  
  web_app:
    priority: 75
    paths: ["packages/web-app/**/*"]
    mcp_servers: ["github", "filesystem", "npm"]
  
  mobile_app:
    priority: 75
    paths: ["packages/mobile-app/**/*"]
    mcp_servers: ["github", "filesystem", "npm"]
  
  documentation:
    priority: 60
    paths: ["docs/**/*"]
    mcp_servers: ["github", "filesystem"]

# Context-based configuration
context_rules:
  # Core package changes require more attention
  - condition: "event.changed_files.some(file => file.startsWith('packages/core/'))"
    settings:
      max_turns: 40
      priority: 95
  
  # Documentation changes need special handling
  - condition: "event.changed_files.some(file => file.startsWith('docs/') && file.endsWith('.md'))"
    settings:
      enabled_agents: ["documentation-agent", "spelling-grammar-agent"]

# MCP Server Configuration
mcp_servers:
  github:
    enabled: true
  filesystem:
    enabled: true
  npm:
    enabled: true
  storybook:
    enabled: true
  database:
    enabled: true

# Agent Configuration
agents:
  local:
    enabled: true
    paths:
      - ".a5c/agents/*.agent.md"
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/development/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/frontend/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/backend/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/documentation/*.agent.md"
```

## DevOps and Infrastructure Project

This example demonstrates a DevOps and infrastructure project structure with A5C integration:

```
project-root/
├── .a5c/
│   ├── config.yml                 # A5C global configuration
│   ├── agents/                    # Custom agents directory
│   │   ├── infrastructure-reviewer.agent.md
│   │   ├── security-reviewer.agent.md
│   │   └── cost-optimizer.agent.md
│   └── memory/                    # Agent memory storage
├── .github/
│   └── workflows/
│       ├── a5c.yml                # A5C GitHub Actions workflow
│       └── infrastructure.yml     # Infrastructure deployment workflow
├── terraform/
│   ├── modules/                   # Terraform modules
│   │   ├── vpc/
│   │   ├── kubernetes/
│   │   ├── database/
│   │   └── monitoring/
│   ├── environments/              # Environment-specific configurations
│   │   ├── dev/
│   │   ├── staging/
│   │   └── production/
│   └── global/                    # Global resources
├── kubernetes/
│   ├── base/                      # Base Kubernetes manifests
│   └── overlays/                  # Environment-specific overlays
│       ├── dev/
│       ├── staging/
│       └── production/
├── scripts/
│   ├── deploy.sh
│   ├── backup.sh
│   └── monitor.sh
├── config/
│   ├── prometheus/
│   ├── grafana/
│   └── alertmanager/
├── docs/
│   ├── architecture/
│   ├── operations/
│   └── runbooks/
├── .gitignore
└── README.md
```

### Key A5C Configuration Files

**`.a5c/config.yml`**:
```yaml
version: 1.0.0
settings:
  model: claude-3-7-sonnet-20250219
  verbose: false

# System Settings
system:
  log_level: info
  execution_mode: parallel
  max_concurrent_agents: 5
  timeout: 180

# Infrastructure-specific configurations
categories:
  terraform:
    priority: 90
    paths: ["terraform/**/*"]
    mcp_servers: ["github", "filesystem", "terraform", "cloud_provider"]
  
  kubernetes:
    priority: 85
    paths: ["kubernetes/**/*"]
    mcp_servers: ["github", "filesystem", "kubernetes"]
  
  monitoring:
    priority: 80
    paths: ["config/**/*"]
    mcp_servers: ["github", "filesystem", "prometheus"]
  
  scripts:
    priority: 75
    paths: ["scripts/**/*"]
    mcp_servers: ["github", "filesystem", "shell"]
  
  documentation:
    priority: 70
    paths: ["docs/**/*"]
    mcp_servers: ["github", "filesystem"]

# Environment-specific configurations
environments:
  dev:
    mcp_servers:
      cloud_provider:
        credentials: "dev"
      kubernetes:
        context: "dev-cluster"
  
  staging:
    mcp_servers:
      cloud_provider:
        credentials: "staging"
      kubernetes:
        context: "staging-cluster"
  
  production:
    mcp_servers:
      cloud_provider:
        credentials: "production"
      kubernetes:
        context: "production-cluster"

# Context rules for environment detection
context_rules:
  - condition: "branch == 'main'"
    environment: "production"
  - condition: "branch == 'staging'"
    environment: "staging"
  - condition: "branch.startsWith('feature/') || branch == 'develop'"
    environment: "dev"

# MCP Server Configuration
mcp_servers:
  github:
    enabled: true
  filesystem:
    enabled: true
  terraform:
    enabled: true
  cloud_provider:
    enabled: true
    type: "aws"
  kubernetes:
    enabled: true
  prometheus:
    enabled: true
  shell:
    enabled: true

# Agent Configuration
agents:
  local:
    enabled: true
    paths:
      - ".a5c/agents/*.agent.md"
  remote:
    enabled: true
    sources:
      repositories:
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/devops/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/infrastructure/*.agent.md"
        - uri: "https://github.com/a5c-ai/registry"
          pattern: "agents/security/*.agent.md"
```

These examples demonstrate different project structures optimized for A5C integration across various types of software projects. The key elements for effective A5C integration include:

1. **Organized `.a5c` directory**: Central location for configuration, custom agents, and agent memory
2. **Structured GitHub workflow**: Properly configured A5C workflow in `.github/workflows`
3. **Clear categorization**: Logical grouping of code and resources with appropriate paths
4. **Environment-specific configuration**: Different settings for development, staging, and production
5. **Specialized agents**: Custom agents tailored to specific project needs
6. **Appropriate MCP servers**: Configured to support the project's technology stack

Adapt these examples to your specific project requirements, taking into account your technology stack, team structure, and development processes.