import datetime
from os import listdir
from os.path import expanduser
from os.path import isfile, join
import string
import yaml

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
        r_path = self.config['bib_dir'] + 'records/'
        records = [f for f in listdir(r_path) if isfile(join(r_path, f))]
        for f in records:
            with open(join(r_path, f), 'r') as r_file:
                self.new(yaml.load(r_file))
        for k, r in self.records.iteritems():
            if not r.changed:
                r.changed = False
    def write(self, force=False):
        for k, r in self.records.iteritems():
            if r.changed or force:
                r.write()
    def new(self, content):
        new_record = record(self, content)
        self.records[new_record.key()] = new_record
    def keys(self):
        return self.records.keys()

class record:
    def __init__(self, library, content):
        self.changed = None
        self.content = content
        self.library = library
        if not 'key' in self.content:
            self.generate_key()
    def generate_key(self):
        self.changed = True
        auth = self.content['author'][0]['family']
        year = self.content['issued']['date-parts'][0][0]
        tentative_key = auth + str(year)
        if not tentative_key in self.library.keys():
            self.content['key'] = tentative_key
        else :
            alphabet = list(string.ascii_lowercase)
            i = 0
            while(tentative_key+alphabet[i] in self.library.keys()):
                i = i + 1
            self.content['key'] = tentative_key + alphabet[i]
    def key(self):
        return self.content['key']
    def write(self):
        path = self.library.config['bib_dir']+'records/'+self.key()+'.yaml'
        with open(path, 'w') as outfile:
            outfile.write(yaml.safe_dump(self.content))
