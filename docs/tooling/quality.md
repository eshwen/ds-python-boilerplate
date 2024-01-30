# Quality

Quality checks are important for usable, readable code. They're often afterthoughts, but it's easy to configure and
simply run tools to keep your code in tip-top shape.

All the tools are documented below, and configured under the corresponding sections in [pyproject.toml].

## Ruff

[Ruff] is modern linter written in Rust. It's incredibly fast, and reimplements traditional linters and code checkers
like `flake8`, `isort` (automatic import sorting), and `pydocstyle` (docstring checking).

To only check your code, run

```shell
ruff my_project/ tests/
```

To automatically fix any issues, run

```shell
ruff --fix my_project/ tests/
```

Ruff now contains a formatter to replace [Black]. It ensures consistently-formatted, highly readable code.

To automatically format your code, run

```shell
ruff format my_project/ tests/
```

To instead just show what `ruff` would change, run

```shell
ruff format --diff my_project/ tests/
```

### PyCharm integration

You can also install the [Ruff plugin for PyCharm] to run it automatically on file changes. In **Preferences** |
**Tools** | **Ruff**, configure it as you like.

To aid in documentation, in PyCharm go to **Preferences** | **Tools** | **Python Integrated Tools**. Under
**Docstrings**, select the docstring format as Google.

## Mypy

[Mypy] is a static type checker, examining object relationships and ensuring that they're used correctly (i.e., that
type hints are correct).

Run with

```shell
mypy my_project/
```

### Stubs

Some third-party libraries do not have type hints. In these cases, we can use stubs. These are _`.pyi` files_ that
provide (among other things) a statically-typed skeleton for the library. These should be automatically picked up by
Mypy, and should complain if the necessary stubs aren't installed. Further information on stubs can be found in the
Mypy docs: <https://mypy.readthedocs.io/en/stable/stubs.html>.

If you need to install any stub packages, add them to the developer dependencies. You may also need to add them to the
Mypy hook if you're using pre-commit (see [.pre-commit-config.yaml]).

??? tip

    Run the hook first, and see if it complains about any missing stubs. If you include a Mypy plugin (like
    `pydantic.mypy`) under `[tool.mypy]` in [pyproject.toml], you will likely need to add the package for the hook.

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
- `mypy` type-hinting errors
- `poetry` dependency status (`poetry.lock` and requirements files are up-to-date)

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

[Mypy]: https://mypy.readthedocs.io/en/stable/

[.pre-commit-config.yaml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/.pre-commit-config.yaml

[Ruff plugin for PyCharm]: https://plugins.jetbrains.com/plugin/20574-ruff
