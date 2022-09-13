# README

[![Build status](https://github.com/eshwen/ds-python-boilerplate/actions/workflows/build.yml/badge.svg)](https://github.com/eshwen/ds-python-boilerplate/actions/workflows/build.yml)
[![CodeQL](https://github.com/eshwen/ds-python-boilerplate/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/eshwen/ds-python-boilerplate/actions/workflows/codeql-analysis.yml)
[![Coverage](https://codecov.io/gh/eshwen/ds-python-boilerplate/branch/main/graph/badge.svg?token=M7NHFR7QTU)](https://codecov.io/gh/eshwen/ds-python-boilerplate)

[![Documentation](https://img.shields.io/badge/docs-Documentation%20--%20GitHub%20Pages-brightgreen?style=flat&logo=readthedocs)](https://eshwen.github.io/ds-python-boilerplate/index.html)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/eshwen/ds-python-boilerplate/blob/main/.pre-commit-config.yaml)

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3106/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://docker.com/)

Boilerplate for data science projects in Python.

## Pipelines

Several pipelines are included to execute automatically on various triggers:

* [build.yml](https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/workflows/build.yml) (to build the project)
* [dependabot.yml](https://github.com/eshwen/ds-python-boilerplate/blob/main/.github/dependabot.yml) (to check for updates and vulnerabilities in dependencies, the Docker container, and the other pipelines)

## Documentation

This repository uses Google-Style for documentation. Run `pydocstyle` to check the format of docstrings:

```shell
python -m pydocstyle --count --convention google --add-ignore D301,D212,D107 --match-dir '(?!(tests)).*' --match '(?!__init__).*\.py'
```

### API documentation

API documentation is built with MkDocs using the Material theme. To build it locally, run

```shell
mkdocs build
```

Then open the homepage HTML file under `site/index.html`.

**Warning**: If copying [build-docs.sh](https://github.com/eshwen/ds-python-boilerplate/blob/main/scripts/build-docs.sh) to another project, ensure the copy is executable. Do this with

```shell
chmod +x <path>/build-docs.sh
```

#### Extensions

## Helpful articles

- Python versions in Docker: https://medium.com/swlh/alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker-62171ed4531d
- Emoji suggestions for git: https://gitmoji.dev/

## General Python tips

- Use the built-in `pathlib` library for local file handling over `os.path`
- Type hint functions and methods
- Run an async coroutine with `asyncio.run(<call to coroutine>)`
