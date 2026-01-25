# Configuration file for Cleanroom Whisper documentation

import sys
import os

# Add cleanroom-theme submodule to path (local to this repo)
sys.path.insert(0, os.path.abspath('cleanroom-theme'))

# Import all shared settings
from theme_config import *

# -- Project information -----------------------------------------------------

project = 'Cleanroom Whisper'
copyright = '2024, Cleanroom Labs'
author = 'Cleanroom Labs'
version = '0.1.0'
release = '0.1.0'

# -- Extensions configuration ------------------------------------------------

# Extend shared extensions with project-specific ones
extensions.extend([
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
    'sphinx.ext.todo',
])

# -- sphinx-needs configuration ----------------------------------------------

needs_types = make_needs_types('WHISPER-')

# -- Intersphinx configuration -----------------------------------------------

# Update intersphinx mapping with cross-project references
intersphinx_mapping.update({
    'airgap-deploy': ('https://cleanroomlabs.dev/docs/airgap-deploy/', None),
    'airgap-transfer': ('https://cleanroomlabs.dev/docs/airgap-transfer/', None),
})

# -- HTML output options -----------------------------------------------------

html_title = 'Cleanroom Whisper Documentation'
html_short_title = 'Cleanroom Whisper'

html_context = {
    'display_github': True,
    'github_user': 'cleanroom-labs',
    'github_repo': 'airgap-whisper-docs',
    'github_version': 'main',
    'conf_py_path': '/source/',
}
