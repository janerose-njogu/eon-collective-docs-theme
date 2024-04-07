import os
import sys

import eon_collective_docs_theme

sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'eon_collective_docs_theme',
    'myst_parser',
    'sphinx_copybutton',
]
templates_path = ['_templates']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
master_doc = 'index'
project = 'Eon Collective Documentation Theme'
copyright = "Copyright © Eon Collective LLC 2024. All rights reserved."
author = "Janerose"
# The short X.Y version.
version = eon_collective_docs_theme.__version__
# The full version, including alpha/beta/rc tags.
release = eon_collective_docs_theme.__version__
language = "en"
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'requirements.txt']
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False
today_fmt = '%Y-%m-%d %H:%M'

# -- Options for HTML output -------------------------------------------
html_theme = 'eon_collective_docs_theme'
html_static_path = []
html_favicon = 'favicon.ico'
# -- Options for HTMLHelp output ---------------------------------------
htmlhelp_basename = 'eon_collective_docs_themedoc'
# -- Options for LaTeX output ------------------------------------------
latex_elements = {}
latex_documents = [
    (master_doc, 'eon_collective_docs_theme.tex',
     'Sphinx Wagtail theme documentation',
     'manual'),
]
# -- Options for manual page output ------------------------------------
man_pages = [
    (master_doc, 'eon_collective_docs_theme',
     'Sphinx Wagtail theme documentation',
     [author], 1)
]
# -- Options for Texinfo output ----------------------------------------
texinfo_documents = [
    (master_doc, 'eon_collective_docs_theme',
     'Sphinx Wagtail theme documentation',
     author,
     'eon_collective_docs_theme',
     'One line description of project.',
     'Miscellaneous'),
]

github_doc_root = 'https://github.com/wagtail/eon_collective_docs_theme/tree/main/docs'

def setup(app):
    pass


# https://docs.readthedocs.io/en/stable/guides/manage-translations.html#create-translatable-files
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-gettext_uuid
gettext_uuid = True
gettext_compact = False
