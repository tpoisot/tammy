import os
from os.path import join
import json
import yaml

def export_citeprocjson(records, path):
    """ Export records to JSON
    """
    with open(join(path, 'default.json'), 'w') as libfile:
        json.dump(records, libfile)

def export_citeprocyaml(records, path):
    """ Export records to YAML
    """
    with open(join(path, 'default.yaml'), 'w') as libfile:
        yaml.dump(records, libfile)

def get_from_file(path, deserializer='citeproc-json'):
    """ Read record(s) from a file

    This function reads one or more records from a file. The
    currently implemented deserializers are ``citeproc-json`` and
    ``citeproc-yaml``. Future releases will use ``pandoc-citeproc`` to allow
    interactions with more formats.

    Args:
        path: the path to the file that is being read
        deserializer: the format in which the file is stored

    Returns:
        A dictionary in citeproc format ready to be consumed by tammy
    """
    if not os.path.isfile(path):
        raise ValueError("No file can be read")
    deserializers = ['citeproc-json', 'citeproc-yaml']
    if not deserializer in deserializers:
        raise ValueError("tammy cannot read from "+deserializer+" files")
    with open(path, 'r') as libfile:
        if deserializer == "citeproc-json":
            return json.load(libfile)
        elif deserializer == "citeproc-yaml":
            return yaml.load(libfile)

serializer = {'citeproc-json': export_citeprocjson, 'citeproc-yaml': export_citeprocyaml}
