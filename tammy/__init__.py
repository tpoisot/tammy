import os
from os.path import expanduser
from os.path import isfile

if isfile(expanduser("~/.tammy.json")):
    ## read the config file
    with open(expanduser("~/.tammy.json"), 'r') as cfile:
        PAR = json.load(cfile)
else :
    home = expanduser("~")
    PAR = dict()
    PAR['bib_dir'] = home + "/.bib/"

# TODO check that the home dir exists

# Read all the records in the local folder
REF = dict()
REF_files = [f for f in os.listdir(PAR['bib_dir']+'refs') if f.endswith('json')]
for RF in REF_files:
    REF[RF] = [0]

from crossref import get_ref_from_doi
