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
        self.records = dict()
        self.read(force=True)
    def read(self, force=False):
        pass
    def write(self, force=False):
        pass
    def new(self, content):
        new_record = record(self, content)
        self.records[new_record.key] = new_record
    def keys(self):
        return self.records.keys()

class record:
    def __init__(self, library, content):
        self.content = content
        self.library = library
        self.key = 'TO CHANGE'
        ## TODO read key
        self.generate_key()
    def generate_key(self):
        # TODO generate key authorYEAR
        # TODO while not unique increment letter
        pass
