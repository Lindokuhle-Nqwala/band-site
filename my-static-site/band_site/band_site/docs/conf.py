# Configuration file for the Sphinx documentation builder.
# -- Django project setup -----------------------------------------------------

import django
import os
import sys




# -- Path setup ---------------------------------------------------------------

# Add project directory to sys.path
sys.path.insert(0, os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'band_site.settings'
django.setup()

# -- Project information ------------------------------------------------------

project = 'Band Site'
copyright = '2025, Lindokuhle Nqwala'
author = 'Lindokuhle Nqwala'
release = '1.0'

# -- General configuration ----------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output --------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
