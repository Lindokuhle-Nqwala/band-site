import os
import sys
import django

sys.path.insert(0, os.path.abspath('../../my-static-site/band_site'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'band_site.settings'
django.setup()

# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Band Site'
copyright = '2025, Lindokuhle Nqwala'
author = 'Lindokuhle Nqwala'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
