# Installation

## Programs

- Docker
- Visual Studio Code/PyCharm
- GitHub Desktop (optional)

=== ":material-apple: macOS"

    ```shell
    # Rosetta for compatibility with Intel
    softwareupdate --install-rosetta
    
    # Homebrew
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    brew install --cask docker
    brew install --cask visual-studio-code  # or brew install --cask pycharm
    brew install --cask github
    ```
    See <https://github.com/eshwen/macOS-setup> for more useful setup tips.

=== "Other"

    Find the links on for these programs on the web :material-emoticon-wink-outline:

## Development Container

=== ":material-microsoft-visual-studio-code: Visual Studio Code"

    1. Install the **Remote - Containers** extension (`ms-vscode-remote.remote-containers`)
    2. Open this project as a folder
    3. A prompt should appear to open it in a container. Ensure Docker is installed and running so the container can be built.

    The devcontainer encompasses the following:

    - Building the Docker container that contains a recent Python image
    - Installing the project dependencies
    - Installing VS Code workspace extensions
    - Applying custom settings to aforementioned extensions

=== ":simple-pycharm: PyCharm"

    1. Under the interpreters tab on the bottom row, hit **Add New Interpreter** -> **On Docker...**
        1. If the **Docker server** is blank, in the dropdown menu click **Create new...** -> **Ok**
        2. Select the correct Dockerfile
        3. Set the **Context folder** to `.` 
        3. Uncheck the box **Rebuild image automatically every time before running code**
        4. Optionally, add an image tag to identify it later
    2. Hit **Next** and let the container build
    3. On the final page, the default interpreter should be sufficient

## Poetry

### Install Poetry

First, install Poetry. This can be done through

=== "Official installer"

    See <https://python-poetry.org/docs/#installation>

=== "Homebrew (on :material-apple:)"

    ```shell
    brew install poetry
    ```

=== "pip"

    ```shell
    pip install poetry
    ```

To ensure Poetry is up to date, run

```shell
poetry self update
```

Then create the `virtualenv` environment with

```shell
poetry shell
```

### Install the project

=== ":octicons-terminal-24: Command line"

    To install everything from this project's Poetry configuration, run
    
    ```shell
    poetry install
    ```
    
    To only install the core dependencies, instead run
    
    ```shell
    poetry install --without dev,test,docs
    ```
    
    It will create a `virtualenv` environment for you, so you don't need to run it in conjunction with another environment manager, such as conda.

=== ":simple-pycharm: PyCharm"

    1. Open the project
    2. Click **Add New Interpreter** -> **Add Local Interpreter...** -> **Poetry Environment**
    3. Check **Poetry Environment**
    4. For the **Base Interpreter**, the default option will probably do as Poetry will create a `virtualenv` environment to install everything inside

### Creating your own configuration

To create your own Poetry configuration
in [pyproject.toml](https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml), run

```shell
poetry init
```

and follow the instructions. Then to port any dependencies from ``requirements.txt`` and ``requirements-dev.txt``, run

```shell
cat requirements.txt | grep -E '^[^# ]' | cut -d= -f1 | xargs -n 1 poetry add
cat requirements-dev.txt | grep -E '^[^# ]' | cut -d= -f1 | xargs -n 1 poetry add --group dev
```

Dependencies can be segmented into different groups.
See [pyproject.toml](https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml).

It is recommended to maintain dependencies with Poetry, and export them to ``requirements.txt``
and ``requirements-dev.txt`` if needed, e.g.,

```shell
poetry export --without-hashes -f requirements.txt -o requirements.txt
poetry export --without-hashes --only dev -f requirements.txt -o requirements-dev.txt
```

## Conda

1. For a lightweight experience, install `miniconda`. This can be done through

    === "Homebrew (on :material-apple:)"

        ```shell
        brew install --cask miniconda
        ```

    === "Other"

        Figure it out :material-emoticon-wink-outline:

2. Then initialise conda:

    ```shell
    conda init "$(basename "${SHELL}")"
    <exit and reopen terminal>
    ```

3. Create your environment:

    ```shell
    conda create -y -n my_project
    conda activate my_project
    conda config --set auto_activate_base false  # Don't automatically activate base env when opening terminal
    conda install -y python=3.10
    pip install --upgrade pip
    ```

4. And finally, install the requirements:

    ```shell
    cd <root dir of project>
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```
