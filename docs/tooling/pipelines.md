# Pipelines

Several pipelines are included to execute automatically on various triggers:

- What: Build the Python project
    - Where: [build.yml]
    - When: On PR creation and subsequent pushes
- What: Build the API documentation
    - Where: [api-docs.yml]
    - When: On the creation of a new tag (i.e., a new GitHub Release)
- What: Check for dependency updates and vulnerabilities
    - Where: [dependabot.yml]
    - When: On a schedule (check the file)

TODO: Add documentation and CodeQL pipelines.
TODO: Flesh out dependabot more (package sets, etc.)
TODO: Flesh out build.yml more (coverage, unit tests, etc., and paths to scripts for local running - ensuring user
does `chmod +x` on them if they are copying them over so they're executable with `./`).

[api-docs.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/workflows/api-docs.yml

[build.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/workflows/build.yml

[dependabot.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/dependabot.yml
