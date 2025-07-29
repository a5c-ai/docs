 # Configuration

 a5c uses a YAML configuration file located at `.a5c/config.yml` in your repository root.

 ## Default Configuration

 ```yaml
 cli_command: "a5c start"
 token:
   env: "GITHUB_TOKEN"
 projects:
   - path: "."
 agents:
   - name: "developer-agent"
 ```

 ## Configuration Options

 | Option            | Type   | Description                                | Default          |
 |-------------------|--------|--------------------------------------------|------------------|
 | `cli_command`     | string | Command to start the agent loop            | `"a5c start"`   |
 | `token.env`       | string | Environment variable for GitHub API token  | `"GITHUB_TOKEN"` |
 | `projects[].path` | string | Path to repository root or subproject      | `"."`           |
 | `agents[]`        | list   | List of agent names to enable              | `['base-agent']` |

 For advanced settings, see the [Guide](../guide/index.md).
