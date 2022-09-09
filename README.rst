README
======

|Build status| |CodeQL| |Coverage|

|Documentation| |Pre-commit|

|Python 3.10| |Docker| |Code style: black|

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


Poetry
^^^^^^


Install Poetry
~~~~~~~~~~~~~~

First, install Poetry. This can be done through

* The official installer: https://python-poetry.org/docs/#installation
* Homebrew (if you're on a Mac):

    .. code-block:: bash

       brew install poetry

* ``pip``:

    .. code-block:: bash

       pip install poetry

To ensure Poetry is up to date, run

.. code-block:: bash

   poetry self update


Install the project
~~~~~~~~~~~~~~~~~~~

To install everything from this project's Poetry configuration, run

.. code-block:: bash

   poetry install --with docs

To only install the core dependencies, instead run

.. code-block:: bash

   poetry install --without dev,test,docs 

It will create a ``virtualenv`` environment for you, so you don't need to run it in conjunction with another environment manager, such as conda.


Creating your own configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create your own Poetry configuration in ``pyproject.toml``, run

.. code-block:: bash

   poetry init

and follow the instructions. Then to port any dependencies from ``requirements.txt`` and ``requirements-dev.txt``, run

.. code-block:: bash

   cat requirements.txt | grep -E '^[^# ]' | cut -d= -f1 | xargs -n 1 poetry add
   cat requirements-dev.txt | grep -E '^[^# ]' | cut -d= -f1 | xargs -n 1 poetry add --group dev

Dependencies can be segmented into different groups. See `pyproject.toml`_.

It is recommended to maintain dependencies with Poetry, and export them to ``requirements.txt`` and ``requirements-dev.txt`` if needed, e.g.,

.. code-block:: bash

   poetry export --without-hashes -f requirements.txt -o requirements.txt
   poetry export --without-hashes --only dev -f requirements.txt -o requirements-dev.txt


Conda
^^^^^

#. For a lightweight experience, install ``miniconda``. This can be done through

   * Homebrew (if you're on Mac):

       .. code-block:: bash

          brew install --cask miniconda

#. Then initialise conda:

    .. code-block:: bash

       conda init "$(basename "${SHELL}")"
       <exit and reopen terminal>

#. Create your environment:

    .. code-block:: bash

       conda create -y -n my_project
       conda activate my_project
       conda config --set auto_activate_base false  # Don't automatically activate base env when opening terminal
       conda install -y python=3.10
       pip install --upgrade pip

#. And finally, install the requirements:

    .. code-block:: bash

       cd <root dir of projects>
       pip install -r requirements.txt
       pip install -r requirements-dev.txt


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


Extensions
~~~~~~~~~~

- ``sphinx-toggleprompt``: Toggles the leading ``>>>`` Python prompts and output in code blocks, e.g.,

    .. code:: python

       >>> print('Hello world!')
       Hello world!


Helpful articles
----------------

* Python versions in Docker: https://medium.com/swlh/alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker-62171ed4531d
* Emoji suggestions for git: https://gitmoji.dev/


General Python tips
-------------------

* Use the built-in ``pathlib`` library for local file handling over ``os.path``

* Type hint functions and methods

* Run an async coroutine with `asyncio.run(<call to coroutine>)`


------------

.. |Build status| image:: https://github.com/eshwen/ds-python-boilerplate/actions/workflows/build.yml/badge.svg
   :target: https://github.com/eshwen/ds-python-boilerplate/actions/workflows/build.yml
.. |CodeQL| image:: https://github.com/eshwen/ds-python-boilerplate/actions/workflows/codeql-analysis.yml/badge.svg
   :target: https://github.com/eshwen/ds-python-boilerplate/actions/workflows/codeql-analysis.yml
.. |Coverage| image:: https://codecov.io/gh/eshwen/ds-python-boilerplate/branch/main/graph/badge.svg?token=M7NHFR7QTU 
   :target: https://codecov.io/gh/eshwen/ds-python-boilerplate
.. |Documentation| image:: https://img.shields.io/badge/docs-Documentation%20--%20GitHub%20Pages-brightgreen?style=flat&logo=readthedocs
   :target: https://eshwen.github.io/ds-python-boilerplate/index.html
.. |Python 3.10| image:: https://img.shields.io/badge/python-3.10-blue.svg
   :target: https://www.python.org/downloads/release/python-3106/
.. |Pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: :file:`.pre-commit-config.yaml`
.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |Docker| image:: https://badgen.net/badge/icon/docker?icon=docker&label
   :target: https://docker.com/

.. _pyproject.toml: https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml
