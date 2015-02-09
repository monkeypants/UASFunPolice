# -*- coding: utf-8 -*-
#import sys
#import os
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'UASFunPolice'
copyright = u'2014, Chris Gough'
version = '0.0'
release = '0.0'
exclude_patterns = ['_build']
html_theme = 'traditional'
html_static_path = ['_static']
htmlhelp_basename = 'UASFunPolice'
latex_elements = {
    'papersize': 'a4paper',
}
latex_documents = [
  ('index', 'UASFunPolice.tex',
   u'UASFunPolice',
   u'Chris Gough', 'manual'),
]
texinfo_documents = [
  ('index', 'UASFunPolice',
    u'UASFunPolice Documentation', u'Chris Gough', 'UASFunPolice',
    'Safety Management Tools for Unmaned Aerial Systems',
    'Miscellaneous'),
]
