# Linting and formatting

Both linting and formatting are important for usable, readable code. They're often afterthoughts, but it's easy to configure and simply run tools to keep your code in tip-top shape.

All the tools are documented below, and configured under the corresponding sections in [pyproject.toml](https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml).

## flake8

[Flake8](<https://flake8.pycqa.org/en/latest/>) is widely-used linter with high configurability. Though it does not allow configuration with [pyproject.toml](https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml), a third-party package [Flake8-pyproject](https://github.com/john-hen/Flake8-pyproject) makes this possible.

Run with

```shell
flake8 my_project/ tests/
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

## isort

[isort](https://pycqa.github.io/isort/) is a tool to automatically sort imports.

Run with

```shell
isort my_project/ tests/
```

## mypy

[mypy](https://mypy.readthedocs.io/en/stable/) is a tool to check object types, such as correct type hinting.

Run with

```shell
mypy my_project/ tests/
```

## pydocstyle

[pydocstyle](https://www.pydocstyle.org/en/stable/) is a tool to check docstrings are included and formatted correctly.

Run with

```shell
pydocstyle --count my_project/
```
