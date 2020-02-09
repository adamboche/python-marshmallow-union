# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import pathlib


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",  # Must come *after* sphinx.ext.napoleon.
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]
if os.getenv("SPELLCHECK"):
    extensions += ("sphinxcontrib.spelling",)
    spelling_show_suggestions = True
    spelling_lang = "en_US"

source_suffix = ".rst"
master_doc = "index"
project = "marshmallow-union"
year = "2019"
author = "Adam Boche"
copyright = "{0}, {1}".format(year, author)
version = release = "0.1.14"

pygments_style = "trac"
templates_path = ["."]
extlinks = {
    "issue": ("https://github.com/adamboche/python-marshmallow-union/issues/%s", "#"),
    "pr": ("https://github.com/adamboche/python-marshmallow-union/pull/%s", "PR #"),
}
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

if not on_rtd:  # only set the theme if we're building docs locally
    html_theme = "sphinx_rtd_theme"

html_use_smartypants = True
html_last_updated_fmt = "%b %d, %Y"
html_split_index = False
html_sidebars = {"**": ["searchbox.html", "globaltoc.html", "sourcelink.html"]}
html_short_title = "%s-%s" % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = True

autoapi_dirs = ["../src/marshmallow_union"]


rst_prolog = """
.. warning::


   Figuring out the correct field type from an untagged dump is a matter of guesswork and
   can be error-prone. A more explicit approach like
   https://github.com/Bachmann1234/marshmallow-polyfield/ is better. This project remains
   here to avoid breaking existing software.

"""
