# Reference

This section provides a detailed reference for the a5c project, covering public API interfaces, configuration options, and available CLI command patterns.

## API Reference

Public API definitions, endpoint specifications, and data models are maintained in the [a5c-ai/specs](https://github.com/a5c-ai/specs) repository. For comprehensive interface details, refer to:

- https://github.com/a5c-ai/specs

## Configuration Options

a5c uses a YAML configuration file at the root of your repository named `.a5c/config.yml`. The primary top-level keys and their defaults are shown below:

```yaml
defaults:
  # Command template for invoking AI agents (adjust as needed for your environment).
  cli_command: "<your model execution command template>"

remote_agents:
  # Enable or disable fetching agents from the public registry
  enabled: true
  # Cache timeout for registry responses (minutes)
  cache_timeout: 120
  # Number of retry attempts when fetching agents
  retry_attempts: 5
  # Delay between retries (milliseconds)
  retry_delay: 2000
  sources:
    individual:
      - uri: "<agent registry URI>"
        alias: "<agent-alias>"
```

| Option                             | Type    | Default                       | Description                                               |
|------------------------------------|---------|-------------------------------|-----------------------------------------------------------|
| `defaults.cli_command`             | string  | See snippet above             | Shell command template used to invoke the AI model/agent. |
| `remote_agents.enabled`            | boolean | `true`                        | Toggle remote registry agent support.                     |
| `remote_agents.cache_timeout`      | integer | `120`                         | Minutes to cache registry responses.                      |
| `remote_agents.retry_attempts`     | integer | `5`                           | Number of retry attempts fetching remote definitions.     |
| `remote_agents.retry_delay`        | integer | `2000`                        | Delay in milliseconds between retries.                    |
| `remote_agents.sources.individual` | list    | N/A                           | Array of agent definitions with `uri` and `alias` fields. |

For additional configuration examples and advanced settings, consult the full `.a5c/config.yml` in your repository.

## CLI Commands

a5c does not currently provide a dedicated command-line interface. Instead, agent invocation is controlled via the `cli_command` template in `.a5c/config.yml`. This allows you to integrate any shell-based AI client (e.g., `codex exec`, `claude`, or `openai`) as needed.

<!-- Additional command patterns may be documented here if a dedicated a5c CLI is introduced in the future. -->
