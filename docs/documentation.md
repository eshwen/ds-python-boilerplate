# Documentation

This repository uses Google-Style for docstrings. They are checked automatically by `ruff`.
See [linting and formatting](linting-formatting.md) for more information.

## API documentation

API documentation is built with MkDocs using the Material theme. To build a static copy locally, run

```shell
mkdocs build
```

Then open the homepage HTML file under `site/index.html`.

Or, to render it live on a local server, run

```shell
mkdocs serve
```

For a Sphinx implementation of documentation, see <https://github.com/eshwen/ds-python-boilerplate/releases/tag/v0.1.1>.

### Extensions and plugins

- [termynal](https://github.com/daxartio/termynal): animated code blocks similar to the FastAPI docs
    - Installed as a Python package
      in [pyproject.toml](https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml)
    - Added to the `plugins` section
      of [mkdocs.yml](https://github.com/eshwen/ds-python-boilerplate/blob/main/mkdocs.yml)

<!-- termynal -->

```bash
$ python hello_world.py
---> Transmitting greeting...
Hello world!
```

TODO: Add extension and plugin descriptions.
