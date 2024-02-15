# -*- coding: utf-8 -*-

import os
import sys
import re

sys.path.append(os.getcwd())

### Import project configuration ##############################################
import conf_project
###############################################################################

### SPHINX CONFIGURATION (GENERAL) ############################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html

# The configuration values shall be placed in the same order as they are placed in the documenting manual.
# The documenting chapter of the manual shall be reflected by a section in this config file.
# The hyperlink to that chapter shall be placed in the very first line of that section.

# Helper variables which are used inside this configuration file which support a calculation of a configuration value shall be named so they start with an underscore ("_") so it"s obvious that they are local helper variables only used here. This is not a function by the interpreter but a common syntax hint to the programmer.

### Project information #######################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# pyright: reportShadowedImports=false
import datetime
from tzlocal import get_localzone
import git
import getpass

_timezone = get_localzone()
_current_time = datetime.datetime.now(_timezone)
_formatted_time = _current_time.strftime("%Y-%m-%d %H:%M:%S")
_print_out_timestamp = f"{_formatted_time} {_current_time.tzname()}"
_year = _current_time.strftime("%Y")

_repo = git.Repo(search_parent_directories=True)
_sha_short = _repo.git.rev_parse(_repo.head.object.hexsha, short=8)
_branch = _repo.active_branch.name

_username = getpass.getuser()

_project = conf_project.project
_author = conf_project.author
_version = open('../VERSION', 'r').readline().strip()

_metadata   = f"version: {_version} | commit: {_sha_short} | branch: {_branch} | printed at {_print_out_timestamp} by {_username}"

project   = f"{_project}"
author    = f"{_author}"
copyright = f"{_year}, {author}"
release   = f"{_version}"

### General configuration #####################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = []

exclude_patterns = [
    "README.md",
]

templates_path = []

numfig = True

### Options for HTML output ###################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_material"

# The theme settings are theme specific. So wrap their settings into if-clauses for easy
# switching of themes.
if html_theme == "sphinx_material":

    html_sidebars = {
        "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
    }

    html_theme_options = {
        "nav_title": f"{project} Documentation",
        "globaltoc_depth": 4,
        "globaltoc_collapse": "true",
        "globaltoc_includehidden": "true",
    }

    html_title = f"{_metadata}"
else:
    pass
    
### Options for latex / PDF output ############################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_elements = {

    "papersize"   : "a4paper",
    "pointsize"   : "12pt",
    # See more settings at https://www.sphinx-doc.org/en/master/latex.html#the-latex-elements-configuration-setting
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        "index", # file path without extension
        f"{project}.tex",
        _project,
        _author,
        "manual"
    ),
]

###############################################################################
### EXTENSIONS AND THEIR SETTINGS #############################################
###############################################################################

# Ordered list. Order: Most general first, then for more and more special usescases
extensions = []


### Draw diagrams with "draw.io" ##############################################
# @see https://pypi.org/project/sphinxcontrib-drawio/

extensions.append("sphinxcontrib.drawio")

# Prevent from nasty console flickering
drawio_disable_verbose_electron = True


### Embedd diagrams as code in plantuml language with "plantuml" #############
# @see https://github.com/sphinx-contrib/plantuml

extensions.append("sphinxcontrib.plantuml")

_conf_location = os.path.realpath(os.path.dirname(__file__))
_plantuml_config_file="plantuml.config"

plantuml = f"java -jar {_conf_location}/../.venv/plantuml.jar -config {_conf_location}/{_plantuml_config_file}"

plantuml_output_format = "svg"


### Author diagrams of arbitrary types with "Mermaid" #########################
# @see https://sphinxcontrib-mermaid-demo.readthedocs.io
# @see https://mermaid.js.org/syntax/gitgraph.html

extensions.append("sphinxcontrib.mermaid")

### Add copy-to-clipboard button to codeblocks ################################
# @see https://sphinx-copybutton.readthedocs.io

extensions.append("sphinx_copybutton")


### Embed graphs in Graphviz format with "graphviz" ###########################
# @see https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html

extensions.append("sphinx.ext.graphviz")


### Render Your Data Readable #################################################
# @see https://sphinxcontribdatatemplates.readthedocs.io/en/latest/index.html
extensions.append("sphinxcontrib.datatemplates")

templates_path.append("_templates")


### Enable bibliography in bibtex format ######################################
# @see https://sphinxcontrib-bibtex.readthedocs.io/
extensions.append("sphinxcontrib.bibtex")

bibtex_bibfiles = [
    # "bibliography.bib"
]


### Manage todos with "todo" ##################################################
# @see https://www.sphinx-doc.org/en/master/usage/extensions/todo.html

extensions.append("sphinx.ext.todo")

todo_include_todos = True


### Make use of Inkscape for PDF output work  #################################
# @see https://pypi.org/project/sphinxcontrib-svg2pdfconverter/

extensions.append("sphinxcontrib.inkscapeconverter")


### Add diagrams as code with "blockdiag" and its sub-types ###################
# @see http://blockdiag.com/en/
# @see https://lpn-doc-sphinx-primer.readthedocs.io/en/0.0.3/extensions/blockdiag.html
# @see https://pypi.org/project/sphinxcontrib-blockdiag/

extensions.append("sphinxcontrib.blockdiag")
extensions.append("sphinxcontrib.seqdiag")
extensions.append("sphinxcontrib.actdiag")
extensions.append("sphinxcontrib.nwdiag")


### Create hyperlinks to issues  ##############################################
# @see https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html

extensions.append("sphinx.ext.extlinks")

extlinks = {
    "issue": ("https://jira.mycompany.com/browse/%s","%s"),
}

extlinks_detect_hardcoded_links = True


### Jupyter-sphinx config #####################################################
# Adds directive .. jupyter_execute:: to embed jupyter code directly into rst code.
# @see https://jupyter-sphinx.readthedocs.io/en/latest/

if False:
    extensions.append("jupyter_sphinx")

### Jupyter Notebook Publishing config ########################################
# Enables adding Jupyter notebooks to toctree
# @see https://myst-nb.readthedocs.io/en/latest/configuration.html

if False:
    extensions.append("myst_nb")

# Timeout for notebooks, default of 30 seconds was not enough for Jenkins agents
nb_execution_timeout = 180


### Link documentation items with "mlx.traceability" ##########################
# @see https://melexis.github.io/sphinx-traceability-extension

extensions.append("mlx.traceability")

import mlx.traceability 
html_static_path = [os.path.join(os.path.dirname(mlx.traceability.__file__), "assets")]
traceability_relationships = {
    'ticket': '',
}

traceability_relationship_to_string = {
    'ticket': 'JIRA ticket',
}

traceability_external_relationship_to_url = {
    'ticket': 'https://jira.server.com/browse/field1',
}

traceability_render_relationship_per_item = True

### nbsphinx - Include complete Jupyter notebooks ############################
# @see https://nbsphinx.readthedocs.io/en/0.9.3/configuration.html
if False:
    extensions.append("nbsphinx")


### Add other markdown formats other than .rst  ##############################
# @see https://www.sphinx-doc.org/en/master/usage/markdown.html

# Deactivated because of collision with extension "myst_parser"
if False:
    extensions.append("myst_nb")

    source_suffix = {
        ".rst"  : "restructuredtext",
        ".md"   : "markdown",
    }


### EOF #######################################################################
