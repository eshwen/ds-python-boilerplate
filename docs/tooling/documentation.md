# Documentation

This repository uses Google-Style for docstrings. They are checked automatically by `ruff`. See [quality](quality.md)
for more information.

## API documentation

API documentation is built with [Zensical], the successor to Material for MkDocs. The [mike] package wraps Zensical
and allows versioned sets of docs to be created. The docs dependencies live in their own `docs` group in [pyproject.toml], so install them
first with

```shell
uv sync --all-groups
```

To build a static copy locally and render it live on a local server, run

=== "Zensical standalone"

    ```shell
    uv run zensical serve
    ```

=== "Zensical with mike"

    ```shell
    uv run mike serve
    ```

The CI pipeline builds the docs with `zensical build --strict`, so any warnings (e.g., broken cross-references) will fail
the build. Run it locally to check before pushing:

```shell
uv run zensical build --strict
```

When a new release is published, the docs are deployed to GitHub Pages with mike under the release's `<major>.<minor>`
version, aliased to `latest`. See [pipelines](pipelines.md) for more information.

For a Sphinx implementation of documentation, see <https://github.com/eshwen/ds-python-boilerplate/releases/tag/v0.1.1>.

### Extensions and plugins

All plugins are installed as Python packages in the `docs` group of [pyproject.toml] and enabled in the `plugins` section
of [zensical.toml].

- [mkdocstrings]: generates API documentation from docstrings, like Sphinx's `autodoc`
    - Uses the Python handler, showing each object's source and type, with docstring sections as tables. Private
      members and magic methods are hidden
    - Loads object inventories for Python, NumPy, pandas, SQLAlchemy and Polars, so docstrings can link to external
      objects, e.g., `[pandas.DataFrame][]`
    - Publishes this project's own `objects.inv`, so other projects' docs can link to it
- [mkdocs-autorefs]: resolves cross-references between pages and to API objects (installed as a dependency of
  mkdocstrings)
- [mkdocs-api-autonav]: automatically generates an API page for every module in `src/my_project` and adds them to the
  navigation under a "Code Reference" section, so no hand-written API pages are needed
- [mike]: deploys versioned docs to the `gh-pages` branch, and adds a version selector to the site

The `markdown_extensions` section of [zensical.toml] turns on the Markdown features Zensical supports, like admonitions,
content tabs, code annotations and icons. See the [Zensical docs] for how to use them. One to know about is
`pymdownx.snippets`: `docs/index.md` uses it to pull in `README.md`, so the README is also the docs homepage.

`docs/css/code_select.css` makes the prompt and output of `console` code blocks unselectable, so highlighting a
command doesn't copy the `$` or what it printed:

```console
$ python hello_world.py
---> Transmitting greeting...
Hello world!
```

[Zensical]: https://zensical.org/

[Zensical docs]: https://zensical.org/docs/

[pyproject.toml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml

[zensical.toml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/zensical.toml

[mkdocstrings]: https://mkdocstrings.github.io/

[mkdocs-autorefs]: https://mkdocstrings.github.io/autorefs/

[mkdocs-api-autonav]: https://github.com/tlambert03/mkdocs-api-autonav

[mike]: https://github.com/squidfunk/mike
