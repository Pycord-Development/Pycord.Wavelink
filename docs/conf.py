# pycord.wavelink documentation master file, created by
# sphinx-quickstart on Tue Dec 14 13:13:44 2021.
# You can adapt this file completely to your liking, but it should at least
# contain the root `toctree` directive.
# ----------------------------------------------------------------------------
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import re
sys.path.insert(0, os.path.abspath("../src"))
sys.path.append(os.path.abspath('extensions'))


# -- Project information -----------------------------------------------------

project = "pycord.wavelink"
copyright = "2021, Pycord Development"
author = "Pycord Development"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

version = ''
with open('../src/pycord/wavelink/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

# The full version, including alpha/beta/rc tags.
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
]

extlinks = {
    'issue': ('https://github.com/Pycord-Development/Pycord.Wavelink/issues/%s', 'GH-'),
}

extensions = [
    'builder',
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinxcontrib_trio',
    'details',
    'exception_hierarchy',
    'attributetable',
    'resourcelinks',
    'nitpick_file_ignorer',
]
autodoc_member_order = 'bysource'
autodoc_typehints = 'none'

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "basic"
html_logo = "./assets/pycord.png"
html_experimental_html5_writer = True
html_context = {
  'discord_invite': 'https://pycord.dev/discord',
}

resource_links = {
  'discord': 'https://pycord.dev/discord',
  'issues': 'https://github.com/Pycord-Development/Pycord.Wavelink/issues',
  'discussions': 'https://github.com/Pycord-Development/Pycord.Wavelink/discussions',
  'examples': f'https://github.com/Pycord-Development/Pycord.Wavelink/tree/{branch}/examples',
}
default_dark_mode = True


gettext_compact = False

language = None

source_suffix = '.rst'
master_doc = 'index'

rst_prolog = """
.. |coro| replace:: This function is a |coroutine_link|_.\n\n
.. |maybecoro| replace:: This function *could be a* |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
.. |default| raw:: html
    <div class="default-value-section"> <span class="default-value-label">Default:</span>
"""

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_search_scorer = '_static/scorer.js'

html_js_files = [
  'custom.js',
  'settings.js',
  'copy.js',
  'sidebar.js'
]

# Output file base name for HTML help builder.
htmlhelp_basename = 'pycordwavedoc'
html_favicon = './assets/pycord.ico'
latex_documents = [
  ('index', 'pycord-wavelink.tex', 'Pycord.Wavelink Documentation',
   'Pycord Development', 'manual'),
]

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

man_pages = [
    ('index', 'Pycord.Wavelink', 'Pycord.Wavelink Documentation',
     ['Pycord Development'], 1)
]

texinfo_documents = [
  ('index', 'Pycord.Wavelink', 'Pycord.Wavelink Documentation',
   'Pycord Development', 'pycord', 'One line description of project.',
   'Miscellaneous'),
]

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

def setup(app):
  if app.config.language == 'ja':
    app.config.intersphinx_mapping['py'] = ('https://docs.python.org/ja/3', None)
    app.config.html_context['discord_invite'] = 'https://pycord.dev/discord'
    app.config.resource_links['discord'] = 'https://pycord.dev/discord'
