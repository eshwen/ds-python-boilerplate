# Pipelines

Several pipelines are included to execute automatically on various triggers:

| What                                             | When                                 | How                   |
|--------------------------------------------------|--------------------------------------|-----------------------|
| Check code with `ruff` and `mypy`                | On PR creation and subsequent pushes | [quality-check.yml]   |
| Unit test with `pytest`                          | On PR creation and subsequent pushes | [test.yml]            |
| Build the API documentation                      | On the creation of a new release     | [api-docs.yml]        |
| Check for dependency updates and vulnerabilities | On a schedule (check the file)       | [dependabot.yml]      |
| Update the draft of the next release             | On pushes to `main`                  | [release-drafter.yml] |

??? note "TODO"

    - Add CodeQL pipeline.
    - Flesh out dependabot more (package sets, etc.)

[api-docs.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/workflows/api-docs.yml

[quality-check.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/workflows/quality-check.yml

[test.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/workflows/test.yml

[dependabot.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/dependabot.yml

[release-drafter.yml]:  https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/workflows/release-drafter.yml
