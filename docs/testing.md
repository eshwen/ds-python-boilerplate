# Testing

Testing is an important part of any software development to ensure everything works intended. Critical code may change and break other functionality if coverage is not appropriate.

## Unit testing

Unit testing is very straightforward with [`pytest`](https://docs.pytest.org/en/7.2.x/). The configuration is stored in [pyproject.toml](https://github.com/eshwen/ds-python-boilerplate/blob/main/pyproject.toml).

Run with

```shell
pytest my_project/
```

To get a nice coverage report (instead of the summary as part of the default configuration), run with

```shell
pytest --cov-report html my_project/
```
