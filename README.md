# README

[![Documentation badge]](https://eshwen.github.io/ds-python-boilerplate/index.html)
[![CodeQL badge]](https://github.com/eshwen/ds-python-boilerplate/actions/workflows/codeql-analysis.yml)
[![Coverage badge]](https://codecov.io/gh/eshwen/ds-python-boilerplate)

[![Python badge]](https://python.org)
[![uv badge]](https://github.com/astral-sh/uv)

[![Ruff badge]](https://github.com/astral-sh/ruff)
[![pyrefly badge]](https://github.com/facebook/pyrefly)
[![Pytest badge]](https://docs.pytest.org/en/stable/)
[![Built with Zensical]](https://zensical.org/)
[![Pre-commit badge]](https://pre-commit.com/)

[![Pandas badge]](https://pandas.pydata.org/docs/index.html)
[![Polars badge]](https://pola.rs)
[![Pydantic v2]](https://pydantic.dev)

Boilerplate for data science projects in Python. Check out the docs by clicking the badge above.

## Using this template

1. Rename the package. `my_project` appears in
    - `src/my_project/` and the test imports
    - `pyproject.toml`: `[project].name` and `[tool.coverage.run].source`
    - `zensical.toml`: the `api-autonav` plugin's `modules`
    - `.github/workflows/test.yml`: `pkg-name`
2. Prune the runtime `dependencies` in `pyproject.toml`. They're a starter set covering common data science tasks, so
   remove what you don't need with `uv remove <package>`.
3. Set up the repository for the CI pipelines (see the Pipelines page of the docs).

[Documentation badge]: https://img.shields.io/badge/Documentation-%20GitHub-brightgreen?logo=refinedgithub

[CodeQL badge]: https://github.com/eshwen/ds-python-boilerplate/actions/workflows/codeql-analysis.yml/badge.svg

[Coverage badge]: https://codecov.io/gh/eshwen/ds-python-boilerplate/branch/main/graph/badge.svg?token=M7NHFR7QTU

[Python badge]: https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13%20%7C%203.14%20%7C%203.15-blue?logo=Python&logoColor=yellow&link=https%3A%2F%2Fwww.python.org%2F

[uv badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json

[Ruff badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json

[pyrefly badge]: https://img.shields.io/endpoint?url=https://pyrefly.org/badge.json

[Pre-commit badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white

[Pytest badge]: https://img.shields.io/badge/pytest-tested-ffffff?logo=pytest

[Built with Zensical]: https://img.shields.io/badge/Zensical-FFA656?logo=zensical&logoColor=black

[Pandas badge]: https://img.shields.io/badge/pandas-%23150458.svg?logo=pandas&logoColor=white&labelColor=grey

[Pydantic v2]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json

[Polars badge]: https://img.shields.io/badge/polars-0075FF?logo=polars&logoColor=white&labelColor=grey
