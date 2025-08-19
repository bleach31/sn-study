# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Lumache'
copyright = '2025, Graziella'
author = 'Graziella'
release = '0.1'
language = 'ja'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinxcontrib.plantuml',
    'sphinx_needs',
]
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'furo'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_css_files = ['custom.css']

# for doctest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

needs_types = [dict(directive="req", title="Requirement", prefix="R_", color="#BFD8D2", style="node"),
               dict(directive="spec", title="Specification", prefix="S_", color="#FEDCD2", style="node"),
               dict(directive="impl", title="Implementation", prefix="I_", color="#DF744A", style="node"),
               dict(directive="test", title="Test Case", prefix="T_", color="#DCB239", style="node"),
               # Kept for backwards compatibility
               dict(directive="need", title="Need", prefix="N_", color="#9856a5", style="node"),
               # user custom types
               {
                   "directive": "tutorial-project",
                   "title": "Project",
                   "prefix": "P_",  # prefix for auto-generated IDs
                   "style": "rectangle", # style for the type in diagrams
                   "color": "#BFD8D2", # color for the type in diagrams
               },
                {
                   "directive": "tutorial-req",
                   "title": "Project",
                   "prefix": "P_",  # prefix for auto-generated IDs
                   "style": "rectangle", # style for the type in diagrams
                   "color": "#BFD8D2", # color for the type in diagrams
               }
]

needs_extra_options = ['introduced', 'updated', 'impacts']

# conf.py
needs_extra_links = [
   {
      "option": "blocks",
      "incoming": "is blocked by",
      "outgoing": "blocks"
   },
   {
      "option": "tests",
      "incoming": "is tested by",
      "outgoing": "tests",
      "copy": False,
      "color": "#00AA00"
   }
]