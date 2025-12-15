from __future__ import annotations

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath(".."))

project = "SignalPlot"
author = "Kyle Jones"
current_year = datetime.now().year
copyright = f"{current_year}, {author}"

# The full version, including alpha/beta/rc tags
release = "0.1.1"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]

autosummary_generate = True
autodoc_typehints = "description"

templates_path = ["_templates"]
exclude_patterns: list[str] = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_static_path = ["_static"]


