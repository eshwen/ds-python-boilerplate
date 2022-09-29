#!/usr/bin/env bash

if [ -z $1 ]; then
    out_format=""
else
    out_format="--cov-report $1"
fi

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source $SCRIPT_DIR/resolve-dirs.sh

pytest -v -s $out_format --asyncio-mode auto --cov my_project/
