 # First Project

 This walkthrough shows how to create and initialize a new project with a5c support.

 ## Initialize the Repository

 ```bash
 git init my-a5c-project
 cd my-a5c-project
 a5c init
 ```

 The scaffold command generates:

 ```text
 .github/workflows/a5c.yml
 .a5c/config.yml
 ```

 ## Add Initial Content

 Create a simple `README.md`:

 ```markdown
 # My A5C Project

 A sample project using a5c for CI/CD and documentation.
 ```

 Commit the changes:

 ```bash
 git add .
 git commit -m "feat: initialize a5c project"
 ```

 ## Start the Agents

 ```bash
 a5c start
 ```

 Monitor the output logs and review generated pull requests.
