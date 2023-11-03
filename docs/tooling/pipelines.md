# Pipelines

Several pipelines are included to execute automatically on various triggers:

- [build.yml](https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/workflows/build.yml)
  - To build the project
- [dependabot.yml](https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/dependabot.yml)
  - To check for updates and vulnerabilities in dependencies, the Docker container, and the other pipelines

TODO: Add documentation and CodeQL pipelines.
TODO: Flesh out dependabot more (package sets, etc.)
TODO: Flesh out build.yml more (coverage, unit tests, etc., and paths to scripts for local running - ensuring user
does `chmod +x` on them if they are copying them over so they're executable with `./`).
