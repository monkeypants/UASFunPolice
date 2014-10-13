# -*- coding: utf-8 -*-
import sys
import os
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Safety Management Tools for Unmanned Aerial Systems (SMTUAS)'
copyright = u'2014, Chris Gough'
version = '0.0'
release = '0.0'
exclude_patterns = ['_build']
html_theme = 'traditional'
html_static_path = ['_static']
htmlhelp_basename = 'SMTUASdoc'
latex_elements = {
    'papersize': 'a4paper',
}
latex_documents = [
  ('index', 'SMTUASS.tex',
   u'Safety Management Tools for Unmaned Aerial Systems',
   u'Chris Gough', 'manual'),
]
texinfo_documents = [
  ('index', 'SMTUAS',
    u'SMTUAS Documentation', u'Chris Gough', 'SMTUAS',
    'Safety Management Tools for Unmaned Aerial Systems',
    'Miscellaneous'),
]
