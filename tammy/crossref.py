import requests as re

def get_ref_from_doi(doi, base_url='http://dx.doi.org/'):
    """ Get a JSON record from a CrossRef DOI

    The output of this function is a `dict` representation of the record,
    that can be used directly by :func:`library.new`.

    Args:
        doi: A string giving the DOI you want to look for
        base_url: The URL to be added before the DOI, defaults to `dx.doi.org`

    Returns:
        A `dict` representation of a json-csl bibliograghic record

    Raises:
        ValueError: No DOI is found (response code of the request is not `200 OK`)

    """
    request_url = base_url + doi
    headers = {b'Accept': 'application/citeproc+json'}
    request_output = re.get(request_url, headers=headers)
    if request_output.status_code == 200 :
        return request_output.json()
    else :
        raise ValueError("No such DOI found")
