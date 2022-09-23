# Documentation

This repository uses Google-Style for documentation. Run `pydocstyle` to check the format of docstrings:

```shell
python -m pydocstyle --count --convention google --add-ignore D301,D212,D107 --match-dir '(?!(tests)).*' --match '(?!__init__).*\.py'
```

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

### Extensions

TODO: Add extension and plugin descriptions.