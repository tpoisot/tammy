"""
.. automodule:: tammy
"""

import os
from os.path import expanduser
from os.path import isfile

# TODO
# Validate ALL the things!!!
# citeprocjs-schema-url = "https://raw.githubusercontent.com/citation-style-language/schema/master/csl-data.json"

from classes import library, record
from services import from_crossref_doi, from_peerj
from IO import *
from cleanup import *
from keygen import *

__all__ = ['library', 'record', 'IO', 'keygen', 'services' ,'keygen']
