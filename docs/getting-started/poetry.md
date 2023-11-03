# Poetry

## Install Poetry

First, install Poetry. This can be done through

=== ":simple-poetry: Official installer"

    See <https://python-poetry.org/docs/#installation>

=== ":simple-homebrew: Homebrew (on :material-apple:)"

    ```shell
    brew install poetry
    ```

=== ":simple-pypi: pip"

    ```shell
    pip install poetry
    ```

To ensure Poetry is up-to-date, run

```shell
poetry self update
```

Then, navigate to the project's root directory, and create the `virtualenv` environment with

```shell
poetry env use 3.10
```

In future sessions (on the CLI), you can enter the environment by navigating to the project's root directory and running

```shell
poetry shell
```

### Decoupling Python and Poetry installs

When installing Poetry, it will usually bundle a Python install. But when using Homebrew, it tends to automatically
update Poetry and the Python dependency. If it upgrades the minor Python version - like 3.10 -> 3.11 - it can break an
existing environment.

As such, it is best practice to decouple the Python install from Poetry. [pyenv] is a great, simple tool to manage
Python installations.

=== ":simple-homebrew: Homebrew (on :material-apple:)"

    ```shell
    brew install pyenv
    ```

=== "Other supported OS"

    See <https://github.com/pyenv/pyenv#installation>.

Then install a specific Python version. The executable path can be found with

```shell
pyenv which python
```

which can be used as the interpreter for the Poetry environment with

```shell
poetry env use "$(pyenv which python)"
```

Now you should have a static path to a specific Python install.

??? tip

    Run `poetry config virtualenvs.in-project true` to store the virtualenv in the project directory. This is useful if
    you want full visibility of the environment, instead of it being hidden elsewhere on your filesystem.

## Install the project

=== ":octicons-terminal-24: Command line"

    To install everything from this project's Poetry configuration, run

    ```shell
    poetry install
    ```

    To only install the core dependencies, instead run

    ```shell
    poetry install --without dev,test,docs
    ```

    Since it will create a `virtualenv` environment for you, you don't need to run it in conjunction with another
    environment manager, such as conda.

=== ":simple-pycharm: PyCharm"

    1. Open the project
    2. Click **Add New Interpreter** -> **Add Local Interpreter...** -> **Poetry Environment**
    3. Check **Existing environment**. The environment you just created should appear in the dropdown menu

## Creating your own configuration

To create your own Poetry configuration in [pyproject.toml], run

```shell
poetry init
```

and follow the instructions. Then to port any dependencies from ``requirements.txt`` and ``requirements-dev.txt``, run

```shell
cat requirements.txt | grep -E '^[^# ]' | cut -d= -f1 | xargs -n 1 poetry add
cat requirements-dev.txt | grep -E '^[^# ]' | cut -d= -f1 | xargs -n 1 poetry add --group dev
```

Dependencies can be segmented into different groups. See [pyproject.toml].

It is recommended to maintain dependencies with Poetry, and export them (1) to ``requirements.txt``
and ``requirements-dev.txt`` if needed, e.g.,
{ .annotate }

1. Check out [quality#pre-commit](../tooling/quality.md#pre-commit) for a pre-commit hook to do this
   automatically.

```shell
poetry export --without-hashes -f requirements.txt -o requirements.txt
poetry export --without-hashes --only dev -f requirements.txt -o requirements-dev.txt
```

This repo separates development dependencies into dev, tests, and docs groups. To export these, run

```shell
poetry export --without-hashes --only dev,test,docs -f requirements.txt -o requirements-dev.txt
```

[pyproject.toml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml

[pyenv]: https://github.com/pyenv/pyenv
