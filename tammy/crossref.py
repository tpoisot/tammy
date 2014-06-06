import requests as re
import yaml
import json

def get_ref_from_doi(doi, base_url='http://dx.doi.org/'):
    request_url = base_url + doi
    headers = {b'Accept': 'application/citeproc+json'}
    request_output = re.get(request_url, headers=headers)
    if request_output.status_code == 200 :
        return request_output.json()
    else :
        raise ValueError("No such DOI found")
