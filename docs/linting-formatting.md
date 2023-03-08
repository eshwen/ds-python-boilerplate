# Linting and formatting

Both linting and formatting are important for usable, readable code. They're often afterthoughts, but it's easy to
configure and simply run tools to keep your code in tip-top shape.

All the tools are documented below, and configured under the corresponding sections in [pyproject.toml].

## ruff

[ruff](<https://beta.ruff.rs/docs/>) is modern linter written in Rust. It's incredibly fast, and reimplements
traditional linters and code checkers like `flake8`, `isort` (automatic import sorting), and `pydocstyle` (docstring
checking).

To only check your code, run

```shell
ruff my_project/ tests/
```

To automatically fix any issues, run

```shell
ruff --fix my_project/ tests/
```

## black

[black](https://black.readthedocs.io/en/stable/index.html) is a widely-used tool to ensure consistently-formatted code.

To automatically reformat your code, run

```shell
black my_project/ tests/
```

To instead just show what `black` would change, run

```shell
black --diff my_project/ tests/
```

## mypy

[mypy](https://mypy.readthedocs.io/en/stable/) is a tool to check object types, such as correct type hinting.

Run with

```shell
mypy my_project/ tests/
```

[pyproject.toml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml
