# ds-python-boilerplate

Boilerplate for data science projects in Python.

## Installation

### Programs

- Docker
- Visual Studio Code
- GitHub Desktop (optional)

#### macOS installation

```bash
# Rosetta for compatibility with Intel
softwareupdate --install-rosetta

# Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install --cask docker
brew install --cask visual-studio-code
brew install --cask github
```

See <https://github.com/eshwen/macOS-setup> for more useful setup tips.

### Development Container

In Visual Studio Code

1. Install the **Remote - Containers** extension (`ms-vscode-remote.remote-containers`)
2. Open this project as a folder
3. A prompt should appear to open it in a container. Ensure Docker is installed and running so the container can be built.

The devcontainer encompasses the following:

- Building the Docker container that contains a recent Python image
- Installing the project dependencies
- Installing VS Code workspace extensions
- Applying custom settings to aforementioned extensions

## Pipelines

Several pipelines are included to execute automatically on various triggers:

- [build.yml](.github/workflows/build.yml) (to build the project)
- [docstring-health.yml](./github/workflows/docstring-health.yml) (to check the validity of Python docstrings)
- [dependabot.yml](.github/dependabot.yml) (to check for updates and vulnerabilities in dependencies, the Docker container, and the other pipelines)

## Helpful articles

- Python versions in Docker: <https://medium.com/swlh/alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker-62171ed4531d>
- Emoji suggestions for git: <https://gitmoji.dev/>
