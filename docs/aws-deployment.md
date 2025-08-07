---
# AWS Deployment Guide

This how-to guide walks you through deploying your repository to AWS using the AWS Command Line Interface (CLI) and shows you how to trigger SRE agents for pipeline extension and error recovery.

## Prerequisites

- **AWS CLI** installed and configured.  
  Install from https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html.
- **AWS Credentials** configured.  
  Run `aws configure` and provide your AWS Access Key ID, Secret Access Key, and default region.
- **a5c CLI** installed and initialized in your repository.  
  See [Bootstrap a5c](start_here.md) for setup instructions.
- **SRE agent** configured in your `.a5c/config.yml` (alias: `sre-agent`).  
  Ensure your SRE agent source is added and available. For example:

```yaml
remote_agents:
  sources:
    individual:
      - alias: "sre-agent"
        uri: "https://raw.githubusercontent.com/a5c-ai/registry/main/agents/ops/sre-agent.agent.md"
```

## 1. Build and Package

Before deployment, package your code or artifacts. For example, if you have a Dockerfile:

```bash
docker build -t my-app:latest .
docker tag my-app:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/my-app:latest
```

## 2. Push to Amazon ECR

```bash
$(aws ecr get-login --no-include-email --region $AWS_DEFAULT_REGION)
aws ecr create-repository --repository-name my-app || true
aws ecr push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/my-app:latest
```

## 3. Deploy to AWS (ECS / EKS / Lambda)

Depending on your service, run the appropriate AWS CLI command. Examples:

- **ECS**:
  ```bash
  aws ecs update-service --cluster my-cluster --service my-service \
    --force-new-deployment
  ```
- **EKS** (via `kubectl`):
  ```bash
  kubectl set image deployment/my-app my-app=${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/my-app:latest
  ```
- **Lambda**:
  ```bash
  aws lambda update-function-code --function-name myLambdaFunction \
    --image-uri ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/my-app:latest
  ```

## 4. Trigger SRE Agent for Pipeline Extension

After deployment, you can trigger the SRE agent to perform further pipeline actions, such as smoke tests or scaling adjustments:

```bash
a5c run sre-agent --context aws-deploy \
  --params '{"cluster":"my-cluster","service":"my-service"}'
```

### Example: Smoke Test

```bash
a5c run sre-agent --context smoke-test \
  --params '{"url":"https://my-service.example.com/health"}'
```

## 5. Error Recovery with SRE Agent

In case of failures, invoke the SRE agent's error recovery routine:

```bash
a5c run sre-agent --context error-recovery \
  --params '{"cluster":"my-cluster","service":"my-service"}'
```

This command triggers the SRE agent to analyze recent deployment logs and attempt automatic remediation steps.

---
*By: documenter-agent (agent+documenter-agent@a5c.ai) - https://a5c.ai/agents/documenter-agent*
