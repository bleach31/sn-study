# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

project = 'Sphinx-Test-Reports'
copyright = '2025, Takehiro Ogawa'
author = 'Takehiro Ogawa'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_needs",
    "sphinxcontrib.test_reports",
    # "sphinxcontrib.plantuml",  # 任意（UML を描くときのみ）
]

templates_path = ['_templates']
exclude_patterns = []

language = 'jp'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# JUnit ファイルの基準パス（省略時は conf.py のあるディレクトリ）
# 相対パスを簡単にしたい場合に役立ちます
tr_rootdir = Path(__file__).parent  # デフォルトも conf.py のディレクトリ
