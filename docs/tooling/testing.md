# Testing

Testing is an important part of any software development to ensure everything works intended. Critical code may change
and break other functionality if coverage is not appropriate.

## Unit testing

Unit testing is very straightforward with [pytest]. The configuration is stored in [pyproject.toml].

Run with

```shell
uv run pytest
```

Coverage is measured on every run (with branch coverage), and the run fails if total coverage drops below 90%. The
threshold is set by `fail_under` under `[tool.coverage.report]` in [pyproject.toml].

To run a subset of tests, select them by keyword with `-k`. Add `--no-cov` so the partial run doesn't fail the coverage
threshold:

```shell
uv run pytest -k test_hello_world --no-cov
```

To get a nice coverage report (instead of the summary as part of the default configuration), run with

```shell
uv run pytest --cov-report html
```

and open `htmlcov/index.html` in your browser. The package to measure is already set by `source` under
`[tool.coverage.run]` in [pyproject.toml], so there's no need to pass it on the command line.

[pytest]: https://docs.pytest.org/en/stable/

[pyproject.toml]: https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml
