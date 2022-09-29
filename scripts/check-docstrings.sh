#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source $SCRIPT_DIR/resolve-dirs.sh

# --match regex ignores __init__.py files
# D301 complains when a docstring has a backslash and isn't a raw string
# D107 complains when there is no docstring in an __init__ method

python -m pydocstyle --count --convention google --add-ignore D301,D107 --match '(?!__init__).*\.py' my_project
