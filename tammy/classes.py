import os
import datetime
from os.path import expanduser
from os.path import isfile
import string

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
        auth = self.content['author'][0]['family']
        year = self.content['issued']['date_parts'][0][0]
        tentative_key = auth + str(year)
        if not tentative_key in self.library.keys():
            self.key = tentative_key
        else :
            alphabet = list(string.ascii_lowercase)
            i = 0
            while(not tentative_key+alphabet[i] in self.library.keys()):
                i = i + 1
            self.key = tentative_key + alphabet[i]
