# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Nicholas Sayre'
copyright = '2025, Nicholas Sayre'
author = 'Nicholas Sayre'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

# html_show_sphinx = False

# My modifications
html_title = ''
# html_sidebars = {
#    '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
#    'using/windows': ['windows-sidebar.html', 'searchbox.html'],
# }
