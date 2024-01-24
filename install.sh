#!/bin/bash

set -o xtrace

pip install -r requirements.txt

rm -rf .venv
mkdir .venv
pipenv install --no-site-packages
