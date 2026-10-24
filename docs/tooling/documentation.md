# Documentation

This repository uses Google-Style for docstrings. They are checked automatically by `ruff`. See [quality](quality.md)
for more information.

## API documentation

API documentation is built with MkDocs using the Material theme. The [mike] package wraps MkDocs and allows versioned
sets of docs to be created. The docs dependencies live in their own `docs` group in [pyproject.toml], so install them
first with

```shell
uv sync --all-groups
```

To build a static copy locally and render it live on a local server, run

=== "MkDocs standalone"

    ```shell
    uv run mkdocs serve
    ```

=== "MkDocs with mike"

    ```shell
    uv run mike serve
    ```

The CI pipeline builds the docs with `mkdocs build --strict`, so any warnings (e.g., broken cross-references) will fail
the build. Run it locally to check before pushing:

```shell
uv run mkdocs build --strict
```

When a new release is published, the docs are deployed to GitHub Pages with mike under the release's `<major>.<minor>`
version, aliased to `latest`. See [pipelines](pipelines.md) for more information.

For a Sphinx implementation of documentation, see <https://github.com/eshwen/ds-python-boilerplate/releases/tag/v0.1.1>.

### Extensions and plugins

All plugins are installed as Python packages in the `docs` group of [pyproject.toml] and enabled in the `plugins` section
of [mkdocs.yml].

- [mkdocstrings]: generates API documentation from docstrings, like Sphinx's `autodoc`
    - Uses the Python handler, with `show_source` enabled
    - Loads object inventories for Python, NumPy, pandas, SQLAlchemy and Polars, so docstrings can link to external
      objects, e.g., `[pandas.DataFrame][]`
- [mkdocs-autorefs]: resolves cross-references between pages and to API objects (installed as a dependency of
  mkdocstrings)
- [mkdocs-api-autonav]: automatically generates an API page for every module in `src/my_project` and adds them to the
  navigation under a "Code Reference" section, so no hand-written API pages are needed
- [mkdocs-section-index]: maps each package's `__init__.py` to its section's index page, so clicking a section in the
  navigation shows the package's documentation
- [termynal]: animated terminal code blocks similar to the FastAPI docs. Add `<!-- termynal -->` above a code block to
  use it:

<!-- termynal -->

```bash
$ python hello_world.py
---> Transmitting greeting...
Hello world!
```

- [mike]: deploys versioned docs to the `gh-pages` branch, and adds a version selector to the site

[pyproject.toml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml

[mkdocs.yml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/mkdocs.yml

[mkdocstrings]: https://mkdocstrings.github.io/

[mkdocs-autorefs]: https://mkdocstrings.github.io/autorefs/

[mkdocs-api-autonav]: https://github.com/tlambert03/mkdocs-api-autonav

[mkdocs-section-index]: https://github.com/oprypin/mkdocs-section-index

[termynal]: https://github.com/daxartio/termynal

[mike]: https://github.com/jimporter/mike
