import datetime
import os
from os import listdir
from os.path import expanduser
from os.path import isfile, join, splitext
import yaml
import IO
import cleanup
import keygen

class library:
    def __init__(self):
        if isfile(expanduser("~/.tammy.yaml")):
            ## read the config file
            with open(expanduser("~/.tammy.yaml"), 'r') as cfile:
                self.config = yaml.load(cfile)
        else :
            home = expanduser("~")
            self.config = dict()
            self.config['bib_dir'] = home + "/.bib/"
        self.config['bib_dir'] = expanduser(self.config['bib_dir'])
        self.created = datetime.datetime.now()
        self.records = dict()
        self.read(force=True)
    def read(self, force=False):
        """Read the yaml files from the references folder

        This method is called when the ``library`` class is instanciated,
        and it ensures that all records are loaded. Because it calls the
        ``new`` method of the ``record`` class, if for some weird reason
        a file has no ``id`` field (*e.g.* you added it yourself), the key
        will be generated at this point.

        Args:
            force: a boolean to force the method to read all files, or only ...
        """
        r_path = join(self.config['bib_dir'], 'records')
        records = [f for f in listdir(r_path) if isfile(join(r_path, f))]
        for f in records:
            with open(join(r_path, f), 'r') as r_file:
                self.new(yaml.load(r_file), False)
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
        self.write()
    def update(self):
        """ Update the keys in the library dict

        This function will loop through all the references, and if the record
        id do not match with the key in the records dict, it will fix things
        up. Additionally, this function will rename the file in the references
        folder, and make sure that the linked files are renamed too.

        """
        for k, v in self.records.iteritems():
            if not k == v.key():
                self.records[v.key()] = self.records.pop(k)
                ofile = join(self.config['bib_dir'], 'records', k+'.yaml')
                nfile = join(self.config['bib_dir'], 'records', v.key()+'.yaml')
                if isfile(ofile):
                    os.rename(ofile, nfile)
                if 'files' in v.content:
                    for fk, fv in v.content['files'].iteritems():
                        v.attach(fv, title=fk)
            else :
                self.records[v.key()].write()
    def keys(self):
        return self.records.keys()
    def export(self, path=expanduser("~/.pandoc"), keys=None, output='citeproc-json'):
        if not keys == None :
            keys = [k for k in self.keys() if k in keys]
        else :
            keys = self.keys()
        records = []
        for k ,v in self.records.iteritems():
            if k in keys:
                records.append(v.content)
        if not output in IO.serializer.keys():
            raise KeyError("There is no "+output+" serializer at the moment. Write one?")
        IO.serializer[output](records, path)
        pass

class record:
    def __init__(self, library, content, new = True):
        self.changed = new
        self.content = cleanup.clean_all(content)
        self.library = library
        if (not 'id' in self.content) or new:
            self.generate_key()
    def generate_key(self, keymaker=keygen.autYr):
        """ Generates a citation key from the record information

        At the moment, citations keys are created as FirstauthorYEAR plus
        one letter if this is required to make the citation key unique. Note
        that the citation key is also the filename of the record, so that a
        record whose key is ``Doe2004`` will be written at ``Doe2004.yaml``.
        """
        self.changed = True
        keygen.makeunique(self, keymaker(self))
        self.library.update()
    def key(self):
        """ Outputs the unique citation key for the record

        Returns:
            a unicode string with the citation key
        """
        return self.content['id']
    def attach(self, fpath, title=None):
        if not isfile(fpath):
            raise ValueError("The attachment must be a valid filepath")
        fpath = expanduser(fpath)
        fName, fExt = splitext(fpath)
        if not 'files' in self.content:
            self.content['files'] = dict()
        if title == None :
            title = str(len(self.content['files'])+1)
        nfile = self.key()+'_'+title+fExt
        os.rename(fpath, join(self.library.config['bib_dir'], 'files', nfile))
        self.content['files'][title] = nfile
        self.write()
    def write(self):
        """ Writes the content of a record to disk

        This will write the content of the record in the ``records``
        folder of the ``bib_dir`` folder. The filename is the unique record
        key and the ``.yaml`` extension.

        This method is usually called by ``library.write()``, but it can be
        used to update the content of any file.

        """
        path = self.library.config['bib_dir']+'records/'+self.key()+'.yaml'
        with open(path, 'w') as outfile:
            outfile.write(yaml.safe_dump(self.content))
        self.changed = False
