# Documentation

This repository uses Google-Style for docstrings. They are checked automatically by `ruff`.
See [linting and formatting](linting-formatting.md) for more information.

## API documentation

API documentation is built with MkDocs using the Material theme. To build a static copy locally, run

```shell
git-changelog -p github -o CHANGELOG.md  # (1)
mkdocs build
```

1. This generates the changelog.

Then open the homepage HTML file under `site/index.html`.

Or, to render it live on a local server, run

```shell
git-changelog -p github -o CHANGELOG.md
mkdocs serve
```

For a Sphinx implementation of documentation, see <https://github.com/eshwen/ds-python-boilerplate/releases/tag/v0.1.1>.

### Extensions and plugins

- [termynal]: animated code blocks similar to the FastAPI docs
    - Installed as a Python package in [pyproject.toml]
    - Added to the `plugins` section of [mkdocs.yml]

<!-- termynal -->

```bash
$ python hello_world.py
---> Transmitting greeting...
Hello world!
```

- [mkdocstrings]: automatically generate API documentation from docstrings, like Sphinx's `autodoc`
    - Installed as a Python package in [pyproject.toml]
    - Added to the `plugins` section of [mkdocs.yml]
    - Used alongside `mkdocs-gen-files` to automatically generate pages for all Python files in the repo
        - The script [gen_ref_pages.py] generates the Markdown files to populate the API docs
    - Used alongside `mkdocs-literate-nav` to pipe the navigation of the API docs to Markdown instead of YAML
    - Used alongside `mkdocs-section-index` map the `__init__.py` files in each directory to the corresponding
      section's `index.md`

TODO: Add extension and plugin descriptions.

[termynal]: https://github.com/daxartio/termynal

[pyproject.toml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml

[mkdocs.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/mkdocs.yml

[mkdocstrings]: https://mkdocstrings.github.io/

[gen_ref_pages.py]: https://github.com/eshwen/ds-python-boilerplate/blob/main/docs/gen_ref_pages.py
