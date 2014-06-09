from os.path import join
import json
import yaml

def export_citeprocjson(records, path):
    with open(join(path, 'default.json'), 'w') as libfile:
        json.dump(records, libfile)

def export_citeprocyaml(records, path):
    with open(join(path, 'default.yaml'), 'w') as libfile:
        yaml.dump(records, libfile)

serializer = {'citeproc-json': export_citeprocjson, 'citeproc-yaml': export_citeprocyaml}
