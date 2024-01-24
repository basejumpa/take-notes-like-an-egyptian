#!/bin/bash

function install() {
    pip install -r requirements.txt
    rm -rf .venv
    mkdir .venv
    pipenv install --no-site-packages --dev
}

function preview() {
    pipenv run sphinx-autobuild doc build/html --port 1440 --open-browser
}

# Check if the number of arguments is exactly one
if [ $# -eq 1 ]; then
    # Check if the argument is one of the specified values
    case "$1" in
          "install" | "preview" )
            set -o xtrace  # Show commands
            $1             # Call the function by its name. Function name identical to command
            ;;
        * )
            echo "Invalid command. Known commands are are: install, preview"
            exit 1
            ;;
    esac
else
    echo "Usage: $0 <argument>"
    exit 1
fi
