###############################################################################
# Entry points for docs-as-code framework                                     #
###############################################################################

### CONFIGURATION #############################################################
# You can set these variables from the command line, and also
# from the environment for the first two.

DOC_CFG_INPUT_DIR        ?= docs
DOC_CFG_BUILD_DIR        ?= out
DOC_CFG_PUBLISH_ROOT_DIR ?= out/publish
DOC_CFG_PREVIEW_PORT     ?= 1984

### IMPLEMENTATION ############################################################

define HELP_SCREEN
Usage: make -f doc/Makefile <target>
Make target for working with the documentation

Known targets are are:

        install       : (Re)-install necessary development environment.
                        The environment is being installed in a virtual environment in subfolder .venv/ of the
                        local repository folder.    
                        All tools except Latex, necessary for command build-pdf are installed.
    
        preview       : Continuous (re-)build for preview in HTML.
                        Rebuild is being triggered by file changes inside folder DOC_CFG_BUILD_DIR. Start local webserver.
        html          : Make documentation in HTML format
        pdf           : Make documentation in PDF format
                        Additional prerequisite is, beside having performed ./doc.sh install, are (installed and in path):    
                        - Miktex (Latex) distribution
        help          : Show this screen

    Commands to be implemented:
        publish       : Publish documentation to place visible for readers
  
    Environment variables used:    
        DOC_CFG_INPUT_DIR        : Directory of documentation's source files
                                   Absolute or relative to working directory
                                   Default: docs
        DOC_CFG_BUILD_DIR        : Build output directory
                                   Absolute or relative to working directory
                                   Depending on preview, make-html, make-pdf there
                                   Create a subdirectory accordingly (preview, html or pdf)
                                   Default: out
        DOC_CFG_PUBLISH_ROOT_DIR : Directory to which to publish
                                   Default: out/publish    
        DOC_CFG_PREVIEW_PORT     : The TCP/IP port 1440 of the local webserver when previewing.
                                   Default: 1984    
endef

# Always invoke one shall for all lines in a recipe 
# @see https://www.gnu.org/software/make/manual/html_node/One-Shell.html
.ONESHELL:
SHELL = git-bash

# Disable all implicit targets
MAKEFLAGS += --no-builtin-rules
.SUFFIXES:

.DEFAULT: help

.PHONY: help
help:
	$(info $(HELP_SCREEN))


.PHONY: install
install: remove-installation .venv/.installation-up-to-date 

.venv/.installation-up-to-date: requirements.txt Pipfile
	mkdir -p .venv/
	python -m pip install -r requirements.txt
	python -m pipenv install --no-site-packages --dev
	curl -L -o .venv/plantuml.jar https://github.com/plantuml/plantuml/releases/download/v1.2024.0/plantuml-1.2024.0.jar
	touch .venv/.installation-up-to-date

remove-installation: 
	rm -rf .venv
	mkdir -p .venv

.PHONY: clean
clean:
	rm -rf "$(DOC_CFG_BUILD_DIR)"

.PHONY: preview
preview: .venv/.installation-up-to-date
	mkdir -p "$(DOC_CFG_BUILD_DIR)/$@"
	# Start continuous build, open browser automatically which reloads on change.
	python -m pipenv run sphinx-autobuild "$(DOC_CFG_INPUT_DIR)" "$(DOC_CFG_BUILD_DIR)/$@" --port "$(DOC_CFG_PREVIEW_PORT)" --open-browser

.PHONY: html
html: .venv/.installation-up-to-date
	mkdir -p "$(DOC_CFG_BUILD_DIR)/$@"
	python -m pipenv run sphinx-build "$(DOC_CFG_INPUT_DIR)" "$(DOC_CFG_BUILD_DIR)/$@"

.PHONY: pdf
pdf: .venv/.installation-up-to-date
	mkdir -p "$(DOC_CFG_BUILD_DIR)/$@"
	python -m pipenv run sphinx-build -b latex "$(DOC_CFG_INPUT_DIR)" "$(DOC_CFG_BUILD_DIR)/$@"
	(cd "$(DOC_CFG_BUILD_DIR)/$@" ; make)

.PHONY: publish
publish: .venv/.installation-up-to-date html pdf
ifeq ($(OS),Windows_NT)
	echo "Publishing here not working yet. Use publish.bat instead"
	exit 1
	cmd /c robocopy '$(DOC_CFG_BUILD_DIR)/html $(DOC_CFG_PUBLISH_ROOT_DIR)/$(shell git branch --show-current) /MIR /TBD /NFL /NDL /NJH /NJS /nc /ns /np'
	cmd /c robocopy '$(DOC_CFG_BUILD_DIR)/pdf/entry.pdf $(DOC_CFG_PUBLISH_ROOT_DIR)/$(shell git branch --show-current) /MIR /TBD /NFL /NDL /NJH /NJS /nc /ns /np'
else
	echo "Publishing on Linux is NOT IMPLEMENTED YET"
	exit 1
endif

