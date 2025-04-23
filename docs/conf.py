
import os
import sys
sys.path.insert(0, os.path.abspath('../my-static-site/band_site'))

project = 'Band Site'
author = 'Lindokuhle Nqwala'
release = '1.0'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
