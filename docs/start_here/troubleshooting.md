 # Troubleshooting

 Common issues when using a5c and how to resolve them.

 ## Missing GitHub Token

 ```console
 Error: Missing GITHUB_TOKEN environment variable
 ```

 Ensure you have set the token in your shell:

 ```bash
 export GITHUB_TOKEN=your_token_here
 ```

 ## Agent Loop Fails to Start

 If `a5c start` exits with errors:

 - Verify the CLI installation: `a5c --version`
 - Check `.a5c/config.yml` for syntax mistakes
 - Use verbose mode to view details: `a5c start --verbose`

 ## Build or CI Failures

 Inspect the generated GitHub Actions workflow at `.github/workflows/a5c.yml`. Ensure your token has write permissions for pull requests and issues.

 ## Need More Help?

 Visit the [Community](../community/index.md) section or open an issue on GitHub.
