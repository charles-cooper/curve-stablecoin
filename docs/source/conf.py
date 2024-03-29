# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Curve Stablecoin'
copyright = '2022, CurveFi'
author = 'CurveFi'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.extlinks']

templates_path = ['_templates']
exclude_patterns = []

add_function_parentheses = False
add_module_names = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


extlinks = {
    "eip": ("https://eips.ethereum.org/EIPS/eip-%s", "EIP-%s")
}
extlinks_detect_hardcoded_links = True