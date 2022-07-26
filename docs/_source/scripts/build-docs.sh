#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ROOT_DIR=$(readlink -f $SCRIPT_DIR/..)
cd $ROOT_DIR

sphinx-apidoc --force --separate --module-first --output-dir docs/_source . tests config.py
sphinx-build -T -a -b html docs/_source docs/_build/html
