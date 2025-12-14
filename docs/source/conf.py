# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',  # enable Markdown (MyST) support
    'sphinx.ext.napoleon',  # support Google/NumPy style docstrings
]

# Ensure Sphinx treats .md files as valid sources
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Newer Sphinx versions use 'root_doc'; keep both for compatibility
root_doc = 'index'
master_doc = 'index'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# Enable some useful MyST extensions for better Markdown support
myst_enable_extensions = [
    'deflist',
    'html_admonition',
    'html_image',
    'colon_fence',
    'smartquotes',
    'substitution',
    'replacements',
    'linkify',
]
# Create heading anchors for easier linking from Markdown headings
myst_heading_anchors = 3

# Autosummary: automatically generate stub pages
autosummary_generate = True

# Static files (e.g., for custom CSS)
html_static_path = []

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
