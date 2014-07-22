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

def read_citeprocyaml(path):
    """ Read a YAML file
    """
    if not os.path.isfile(path):
        raise ValueError("No file can be read")
    with open(path, 'w') as libfile:
        return yaml.load(libfile)

serializer = {'citeproc-json': export_citeprocjson, 'citeproc-yaml': export_citeprocyaml}
