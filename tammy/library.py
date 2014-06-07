import os
import datetime
from os.path import expanduser
from os.path import isfile

class library:
    def __init__(self):
        if isfile(expanduser("~/.tammy.json")):
            ## read the config file
            with open(expanduser("~/.tammy.json"), 'r') as cfile:
                self.config = json.load(cfile)
        else :
            home = expanduser("~")
            self.config = dict()
            self.config['bib_dir'] = home + "/.bib/"
        self.created = datetime.datetime.now()
        self.update(force=True)
    def update(self, force=False):
        print 'UPDATE'


