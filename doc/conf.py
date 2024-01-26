import os

### SPHINX CONFIGURATION (GENERAL) ############################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html

### Project information #######################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project="Personal Notebook"

### General configuration #####################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Enable automatic numbering of figures
numfig = True

### Options for HTML output ###################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# @see https://bashtage.github.io/sphinx-material/customization.html

html_theme = "sphinx_material"

# The theme settings are theme specific. So wrap their settings into if-clauses for easy
# switching of themes.
if html_theme == "sphinx_material":

    html_theme_options = {
        "nav_title" : f"{project} Documentation",

        "color_primary" : "teal",
        "color_accent"  : "orange",

        "globaltoc_depth"         : 3,
        "globaltoc_collapse"      : "true",
        "globaltoc_includehidden" : "true",
    }
    
    html_sidebars = {
        "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
    }
    
else:
    pass

### EXTENSIONS AND THEIR SETTINGS #############################################

# Ordered list. Order: Most general first, then for more and more special usescases

extensions = []


### Draw diagrams with "draw.io" ##############################################
# @see https://pypi.org/project/sphinxcontrib-drawio/

extensions.append("sphinxcontrib.drawio")

# Prevent from nasty console flickering
drawio_disable_verbose_electron = True


### Embed diagrams as code in plantuml language with "plantuml" #############
# @see https://github.com/sphinx-contrib/plantuml

extensions.append("sphinxcontrib.plantuml")

_conf_location = os.path.realpath(os.path.dirname(__file__))
_plantuml_config_file="plantuml.config"

plantuml = f"java -jar {_conf_location}/../.venv/plantuml.jar -config {_conf_location}/{_plantuml_config_file}"

plantuml_output_format = "svg"

### Create hyperlinks to issues  ##############################################
# @see https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html

extensions.append("sphinx.ext.extlinks")

extlinks = {
    'issue': ('https://jira.mycompany.com/browse/%s','%s'),
}

extlinks_detect_hardcoded_links = True

### EOF #######################################################################
