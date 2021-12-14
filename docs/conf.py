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
sys.path.insert(0, os.path.abspath('../src'))


# -- Project information -----------------------------------------------------

project = 'pycord.wavelink'
copyright = '2021, Pycord Development'
author = 'Pycord Development'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
html_logo = './assets/pycord.png'
html_theme_options = {
    'light_css_variables': {
        'color-brand-primary': '#4C8CBF',
        'color-brand-content': '#306998',
        'color-admonition-background': 'blue',
    },
    'dark_css_variables': {
        'color-brand-primary': '#306998',
        'color-brand-content': '#FFE871',
        'color-admonition-background': 'yellow',
    },
    "sidebar_hide_name": True,
}
pygments_style = 'monokai'
default_dark_mode = True

rst_prolog = '''
.. |coro| replace:: This function is a |coroutine_link|_.\n\n
.. |maybecoro| replace:: This function *could be a* |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
.. |default| raw:: html
    <div class="default-value-section"> <span class="default-value-label">Default:</span>
'''

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True