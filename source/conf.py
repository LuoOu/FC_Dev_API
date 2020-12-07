# -*- coding: utf-8 -*-

# for Sphinx-1.4 or newer


# for Sphinx-1.3
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
from recommonmark.parser import CommonMarkParser
# extensions = [
#     'sphinx_markdown_tables'
# ]
# extensions = ['recommonmark']
# source_parsers = {
#     '.md': CommonMarkParser,
# }

source_suffix = ['.rst', '.md']


extensions = [
    'sphinx.ext.autodoc',

    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'recommonmark',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'FC_Dev_API'
copyright = u'luoou'
author = u'luoou'

github_doc_root = 'https:'


language = 'zh'

