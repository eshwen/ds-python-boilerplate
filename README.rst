README
======

|Documentation| |Pre-commit| |Code style: black|

|Python 3.10.5| |Docker|

Boilerplate for data science projects in Python.

.. contents:: **Table of Contents**

Installation
------------

Programs
^^^^^^^^

* Docker
* Visual Studio Code
* GitHub Desktop (optional)


macOS installation
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Rosetta for compatibility with Intel
   softwareupdate --install-rosetta

   # Homebrew
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   brew install --cask docker
   brew install --cask visual-studio-code
   brew install --cask github

See https://github.com/eshwen/macOS-setup for more useful setup tips.


Development Container
^^^^^^^^^^^^^^^^^^^^^

In Visual Studio Code

#. Install the **Remote - Containers** extension (``ms-vscode-remote.remote-containers``)
#. Open this project as a folder
#. A prompt should appear to open it in a container. Ensure Docker is installed and running so the container can be built.

The devcontainer encompasses the following:

* Building the Docker container that contains a recent Python image
* Installing the project dependencies
* Installing VS Code workspace extensions
* Applying custom settings to aforementioned extensions


Pipelines
---------

Several pipelines are included to execute automatically on various triggers:

* `build.yml <.github/workflows/build.yml>`_ (to build the project)
* `dependabot.yml <.github/dependabot.yml>`_ (to check for updates and vulnerabilities in dependencies, the Docker container, and the other pipelines)


Documentation
-------------

This repository uses Google-Style for documentation. Run `pydocstyle` to check the format of docstrings:

.. code:: bash

   python -m pydocstyle --count --convention google --add-ignore D301,D212,D107 --match-dir '(?!(tests)).*' --match '(?!__init__).*\.py'

API documentation
^^^^^^^^^^^^^^^^^

API documentation is built with Sphinx using the Read The Docs theme. To build it locally, run

.. code:: bash

   ./scripts/build-docs.sh

Then open the corresponding HTML file(s) in ``docs/_build/html/``.

**Warning**: If copying `build-docs.sh <scripts/build-docs.sh>`_ to another project, ensure the copy is executable. Do this with

.. code:: bash

   chmod +x <path>/build-docs.sh


Helpful articles
----------------

* Python versions in Docker: https://medium.com/swlh/alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker-62171ed4531d
* Emoji suggestions for git: https://gitmoji.dev/

------------

.. |Documentation| image:: https://img.shields.io/badge/docs-Documentation%20--%20GitHub%20Pages-brightgreen?style=flat&logo=readthedocs
   :target: https://https://eshwen.github.io/ds-python-boilerplate/index.html
.. |Python 3.10.5| image:: https://img.shields.io/badge/python-3.10.5-blue.svg
   target:: https://www.python.org/downloads/release/python-3105/
.. |Pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   target:: :file:`.pre-commit-config.yaml`
.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   target:: https://github.com/psf/black
.. |Docker| image:: https://badgen.net/badge/icon/docker?icon=docker&label
   target:: https://docker.com/
