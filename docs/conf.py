 # Configuration file for the Sphinx documentation builder.

 import os
 import sys
 sys.path.insert(0, os.path.abspath('.'))

 # -- Project information -----------------------------------------------------

 project = 'a5c'
 author = 'a5c-ai'
 release = '0.1.0'

 # -- General configuration ---------------------------------------------------

 extensions = [
     'myst_parser',
 ]

 templates_path = ['_templates']
 exclude_patterns = []

 # -- Options for HTML output -------------------------------------------------

 html_theme = 'sphinx_nefertiti'
 html_theme_options = {}

 # -- Options for MyST parser ------------------------------------------------

 myst_enable_extensions = [
     'deflist',
     'html_admonition',
 ]
