# Quality

Quality checks are important for usable, readable code. They're often afterthoughts, but it's easy to configure and
simply run tools to keep your code in tip-top shape.

All the tools are documented below, and configured under the corresponding sections in [pyproject.toml].

## Ruff

[Ruff] is modern linter written in Rust. It's incredibly fast, and reimplements traditional linters and code checkers
like `flake8`, `isort` (automatic import sorting), and `pydocstyle` (docstring checking).

To only check your code, run

```shell
ruff check src/ tests/
```

To automatically fix any issues, run

```shell
ruff check --fix src/ tests/
```

Ruff now contains a formatter to replace [Black]. It ensures consistently-formatted, highly readable code.

To automatically format your code, run

```shell
ruff format src/ tests/
```

To instead just show what `ruff` would change, run

```shell
ruff format --diff src/ tests/
```

### PyCharm integration

You can also install the [Ruff plugin for PyCharm] to run it automatically on file changes. In **Preferences** |
**Tools** | **Ruff**, configure it as you like.

To aid in documentation, in PyCharm go to **Preferences** | **Tools** | **Python Integrated Tools**. Under
**Docstrings**, select the docstring format as Google.

## pyrefly

[pyrefly] is a fast static type checker written in Rust (by Meta). It examines object relationships and ensures that
they're used correctly (i.e., that type hints are correct). It's configured under `[tool.pyrefly]` in [pyproject.toml].

Run with

```shell
pyrefly check src/
```

### Stubs

Some third-party libraries do not have type hints. In these cases, we can use stubs. These are _`.pyi` files_ that
provide (among other things) a statically-typed skeleton for the library. These should be automatically picked up by
pyrefly, and it should complain if the necessary stubs aren't installed.

If you need to install any stub packages, add them to the developer dependencies (the `type` group in
[pyproject.toml]).

### Typing extensions

Some libraries have type hints, but they are incomplete. In these cases, we can use typing extensions. These provide
_Python objects_ that can be used to type hint the missing functionality. For example, `boto3`:

```python
import boto3
import mypy_boto3_s3

resource: mypy_boto3_s3.S3ServiceResource = boto3.resource("s3", ...)
```

Since we directly import these packages, they should be installed as normal dependencies.

## pre-commit

[pre-commit] is a tool to run hooks before commits and pushes. When attempting to commit/push, the hooks will run in the
background on the modified files. If issues are detected, the hooks will block the action and attempt to fix them, then
you can try again.

The [.pre-commit-config.yaml] file contains hooks to run

- built-in `pre-commit` checks
- Automatic use of the walrus operator
- `ruff` for linting and formatting (fixes fixable issues)
- `pyrefly` type-hinting errors
- `uv` lock state (`uv.lock` is up-to-date, and the project environment is synced)

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

[pre-commit]: https://pre-commit.com/

[Ruff]: https://beta.ruff.rs/docs/

[Black]: https://black.readthedocs.io/en/stable/index.html

[pyrefly]: https://pyrefly.org/

[.pre-commit-config.yaml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.pre-commit-config.yaml

[Ruff plugin for PyCharm]: https://plugins.jetbrains.com/plugin/20574-ruff
