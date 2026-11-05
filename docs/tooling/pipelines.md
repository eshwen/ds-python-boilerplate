---
icon: lucide/workflow
---

# Pipelines

Several pipelines are included to execute automatically on various triggers:

| What                                                         | When                                    | How                         |
|--------------------------------------------------------------|-----------------------------------------|-----------------------------|
| Check code with `ruff` and `pyrefly`                         | On PRs to `main` and pushes to `main`   | [quality-check.yml]         |
| Unit test with `pytest` on Python 3.11-3.15, and build docs  | On PRs to `main` and pushes to `main`   | [test.yml]                  |
| Scan for security vulnerabilities with CodeQL                | On PRs, pushes to `main`, and weekly    | [codeql-analysis.yml]       |
| Label PRs for the release notes                              | On PR creation and subsequent pushes    | [release-drafter-label.yml] |
| Update the draft of the next release                         | On pushes to `main`                     | [release-drafter-draft.yml] |
| Deploy the versioned docs to GitHub Pages                    | On publishing a release                 | [api-docs.yml]              |
| Open PRs for updates to uv, GitHub Actions, and pre-commit   | Monthly                                 | [dependabot.yml]            |

## Shared actions

The quality and test pipelines don't define their steps here. They call a reusable workflow and composite actions from
[eshwen/adrenaline], so the same steps can be shared between projects:

- `uv/builder`: sets up Python and uv, then installs the project from `uv.lock` with `uv sync --locked`
- `python-quality-check-uv.yml`: runs `ruff check`, `ruff format --diff` and `pyrefly check` on `src/`
- `uv/test-python`: runs `pytest` with coverage for the package given by `pkg-name`

They're pinned to a release tag, which Dependabot bumps. If you rename the package, update `pkg-name` in [test.yml].

## Releases

[Release Drafter] keeps a draft release up to date as PRs are merged. PRs are labelled automatically from their branch
name, title and changed files (see [release-drafter-config.yml]), and the labels decide

- which section of the release notes a PR appears in, e.g., `bug` under "Bug Fixes"
- the next version number: a `major` or `minor` label bumps that part of the version; anything else is a patch

Publishing the draft triggers [api-docs.yml], which deploys the docs with mike as `<major>.<minor>`, aliased to `latest`.

## Setup for a new repository

- Add a `CODECOV_TOKEN` repository secret for the coverage upload in [test.yml]
- Create a `gh-pages` branch and set it as the GitHub Pages source. The docs deployment pushes to this branch

??? note "TODO"

    - Flesh out dependabot more (package sets, etc.)

[eshwen/adrenaline]: https://github.com/eshwen/adrenaline

[Release Drafter]: https://github.com/release-drafter/release-drafter

[api-docs.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/workflows/api-docs.yml

[codeql-analysis.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/workflows/codeql-analysis.yml

[quality-check.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/workflows/quality-check.yml

[test.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/workflows/test.yml

[dependabot.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/dependabot.yml

[release-drafter-label.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/workflows/release-drafter-label.yml

[release-drafter-draft.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/workflows/release-drafter-draft.yml

[release-drafter-config.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/release-drafter-config.yml
