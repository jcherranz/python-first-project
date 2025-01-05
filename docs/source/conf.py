"""Sphinx configuration for python-first-project."""

import os
import sys

# Add src directory to Python path for API documentation
sys.path.insert(0, os.path.abspath("../../src"))

# Project information
project = "python-first-project"
copyright = "2025, jcherranz"
author = "jcherranz"
release = "0.1.0"

# General configuration
extensions = [
    "sphinx.ext.autodoc",  # Include documentation from docstrings
    "sphinx.ext.napoleon",  # Support for NumPy and Google style docstrings
    "sphinx.ext.viewcode",  # Add links to highlighted source code
    "sphinx.ext.intersphinx",  # Link to other project's documentation
    "sphinx_rtd_theme",  # Read the Docs theme
]

# Add any paths that contain templates here, relative to this directory
templates_path = ["_templates"]
exclude_patterns = []

# HTML output options
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_type_aliases = None

# AutoDoc settings
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}
