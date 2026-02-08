# Configuration file for Cleanroom Whisper documentation

import sys
import os

# Add common submodule to path
sys.path.insert(0, os.path.abspath('../common'))

# Import all shared settings
from theme_config import *

# Override default paths from theme_config.py for this project's layout
html_static_path = ['../common/sphinx/_static']
templates_path = ['../common/sphinx/_templates']
html_favicon = '../common/sphinx/_static/favicon.ico'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Project information -----------------------------------------------------

project = 'Cleanroom Whisper'
copyright = '2024, Cleanroom Labs'
author = 'Cleanroom Labs'
version = get_docs_version()
release = get_docs_version()

# -- sphinx-needs configuration ----------------------------------------------

needs_types = make_needs_types('WHISPER-')

# -- Intersphinx configuration -----------------------------------------------

# Update intersphinx mapping with cross-project references
intersphinx_mapping.update({
    'airgap-deploy': ('https://cleanroomlabs.dev/docs/deploy/', None),
    'airgap-transfer': ('https://cleanroomlabs.dev/docs/transfer/', None),
})

# -- HTML output options -----------------------------------------------------

html_title = 'Cleanroom Whisper Documentation'
html_short_title = 'Cleanroom Whisper'

html_context = {
    'display_github': True,
    'github_user': 'cleanroom-labs',
    'github_repo': 'cleanroom-whisper-docs',
    'github_version': 'main',
    'conf_py_path': '/source/',
}
setup_project_icon(project, html_context)
setup_version_context(html_context)
