# uv

## Install uv

First, install [uv]. This can be done through

=== ":simple-astral: Official installer"

    See <https://docs.astral.sh/uv/getting-started/installation/>

=== ":simple-homebrew: Homebrew (on :material-apple:)"

    ```shell
    brew install uv
    ```

=== ":simple-pypi: pip"

    ```shell
    pip install uv
    ```

Find more information at https://docs.astral.sh/uv/getting-started/installation/.

## Python versions

uv can install and manage Python interpreters for you, so there's no need for a separate tool like `pyenv`. To install
the Python version this project supports:

```shell
uv python install 3.10  # (1)
```

1. This project also supports 3.11 - 3.14 if you want to use those instead.

To pin a specific Python version for the project, create a `.python-version` file in the project root:

```shell
uv python pin 3.10
```

uv will then use that version whenever it creates or syncs the virtualenv.

## Install the project

=== ":octicons-terminal-24: Command line"

    From the project's root directory, run

    ```shell
    uv sync
    ```

    This will create a `.venv` directory and install the main dependencies plus the `dev` group (lint, type checking,
    testing, and Jupyter).

    To install everything - including the docs group - run

    ```shell
    uv sync --all-groups
    ```

    To install only the core dependencies (no dev tools), run

    ```shell
    uv sync --no-dev
    ```

=== ":simple-pycharm: PyCharm"

    1. Open the project
    2. Click **Add New Interpreter** -> **Add Local Interpreter...** -> **uv**
    3. Point it at the project's `.venv` directory (created by `uv sync`)

In future sessions, either enter the environment with

```shell
source .venv/bin/activate
```

or prepend your commands with

```shell
uv run
```

For example,

```shell
uv run pytest
```

## Adding and removing dependencies

To add a runtime dependency:

```shell
uv add <package>
```

To add a development dependency to a specific group:

```shell
uv add --group test <package>
```

To remove a dependency:

```shell
uv remove <package>
```

These commands update both [pyproject.toml] and `uv.lock` in one step.

[uv]: https://docs.astral.sh/uv/

[pyproject.toml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml
