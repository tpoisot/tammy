"""
.. automodule:: tammy
"""

import os
from os.path import expanduser
from os.path import isfile

from .keygen import *

from tammy.classes import library, record
from tammy.services import from_crossref_doi, from_peerj
import tammy.IO
import tammy.cleanup

__all__ = ['library', 'record', 'IO', 'keygen', 'services' ,'keygen']
