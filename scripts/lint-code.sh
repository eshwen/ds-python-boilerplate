#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source $SCRIPT_DIR/resolve-dirs.sh

flake8 my_project tests --show-source --statistics --max-line-length=120 --per-file-ignores=__init__.py:F401
