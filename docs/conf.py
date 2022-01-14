import os
import sys
import re

sys.path.insert(0, os.path.abspath("../src"))
sys.path.append(os.path.abspath('extensions'))

project = "Pycord.Wavelink"
copyright = "2021, Pycord Development"
author = "Pycord Development"

version = ''
with open('../src/discord/ext/wavelink/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

release = version

branch = 'main' if version.endswith('a') else 'v' + version

extlinks = {
    'issue': ('https://github.com/Pycord-Development/Pycord.Wavelink/issues/%s', 'GH-'),
}

intersphinx_mapping = {
  'py': ('https://docs.python.org/3', None),
  'aio': ('https://docs.aiohttp.org/en/stable/', None),
  'req': ('https://docs.python-requests.org/en/latest/', None),
  'discord': ('https://docs.pycord.dev/en/master/', None)
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

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "basic"
html_logo = "./assets/pycord.png"
html_experimental_html5_writer = True
html_context = {
  'discord_invite': 'https://pycord.dev/discord',
  'pycord_wavelink_extensions': [
  ('pycord.wavelink.ext.spotify', 'ext/spotify'),
],
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

html_static_path = ["_static"]

html_search_scorer = '_static/scorer.js'

html_js_files = [
  'custom.js',
  'settings.js',
  'copy.js',
  'sidebar.js'
]

htmlhelp_basename = 'pycordwavedoc'
html_favicon = './assets/pycord.ico'
latex_documents = [
  ('index', 'pycord.wavelink.tex', 'Pycord.Wavelink Documentation',
   'Pycord Development', 'manual'),
]

man_pages = [
    ('index', 'pycord.wavelink', 'Pycord.Wavelink Documentation',
     ['Pycord Development'], 1)
]

texinfo_documents = [
  ('index', 'pycord.wavelink', 'Pycord.Wavelink Documentation',
   'Pycord Development', 'pycord.wavelink', 'One line description of project.',
   'Miscellaneous'),
]
