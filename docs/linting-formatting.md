# Linting and formatting

Both linting and formatting are important for usable, readable code. They're often afterthoughts, but it's easy to
configure and simply run tools to keep your code in tip-top shape.

All the tools are documented below, and configured under the corresponding sections in [pyproject.toml].

## Ruff

[Ruff] is modern linter written in Rust. It's incredibly fast, and reimplements traditional linters and code checkers
like `flake8`, `isort` (automatic import sorting), and `pydocstyle` (docstring  checking).

To only check your code, run

```shell
ruff my_project/ tests/
```

To automatically fix any issues, run

```shell
ruff --fix my_project/ tests/
```

## Black

[Black] is a widely-used tool to ensure consistently-formatted code.

To automatically reformat your code, run

```shell
black my_project/ tests/
```

To instead just show what `black` would change, run

```shell
black --diff my_project/ tests/
```

### File watchers in PyCharm

PyCharm supports file watchers, which automatically run a command when a file is saved. This is useful for transparently
formatting code.

To include `black` as a file watcher, go to **Settings** -> **Tools** -> **File Watchers** and import
the [watchers.xml]. This will automatically apply formatting to Python files and Jupyter notebooks. You may need to edit
the **Program** path to point to your `black` executable.

Otherwise, to set it up yourself, follow the instructions
at <https://black.readthedocs.io/en/stable/integrations/editors.html>.

**Update**: `black` is integrated into PyCharm as of v2023.2. Go to **Settings** -> **Tools** -> **Black** to configure.

## Mypy

[Mypy] is a tool to check object types, such as correct type hinting.

Run with

```shell
mypy my_project/ tests/
```

## pre-commit

[pre-commit] is a tool to run hooks before commits and pushes. When attempting to commit/push, the hooks will run in the
background on the modified files. If issues are detected, the hooks will block the action and attempt to fix them, then
you can try again.

The [.pre-commit-config.yaml] file contains hooks to run

- built-in `pre-commit` checks
- Automatic use of the walrus operator
- `pyupgrade` to use new Python syntax
- `ruff` for linting (fixes fixable issues)
- `black` for formatting (fixes fixable issues)
- `mypy` type hinting errors
- `poetry` status (`poetry.lock` and requirements files are up-to-date)

To use pre-commit, install the hooks with

```shell
pre-commit install
```

Then, when committing through PyCharm/GitHub Desktop/CLI, they should automatically run. Alternatively, run them
manually with

```shell
pre-commit run -a
```

[pyproject.toml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml

[watchers.xml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/pycharm/watchers.xml

[pre-commit]: https://pre-commit.com/

[Ruff]: https://beta.ruff.rs/docs/

[Black]: https://black.readthedocs.io/en/stable/index.html

[Mypy]: https://mypy.readthedocs.io/en/stable/

[.pre-commit-config.yaml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.pre-commit-config.yaml
