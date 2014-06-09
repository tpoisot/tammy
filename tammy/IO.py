from os.path import join
import json

def export_citeprocjson(records, path):
    with open(join(path, 'library.json'), 'w') as libfile:
        json.dump(records, libfile)

serializer = {'citeproc-json': export_citeprocjson}
