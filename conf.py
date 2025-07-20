# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'A5C'
copyright = '2025, A5C Team'
author = 'A5C Team'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',  # for Markdown support
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_nefertiti'

# Theme options for sphinx-nefertiti
html_theme_options = {
    "sans_serif_font": "Nunito",
    "documentation_font": "Open Sans",
    "monospace_font": "Ubuntu Sans Mono",
    "project_name_font": "Nunito",
    "doc_headers_font": "Georgia",
    "documentation_font_size": "1.1rem",
    "monospace_font_size": "1.0rem",
}

html_static_path = ['_static']

# Support for Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
