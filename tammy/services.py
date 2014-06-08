import requests as re

def from_crossref_doi(doi, base_url='http://dx.doi.org/'):
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

def from_peerj(pubid, pubtype='article'):
    """ Get a JSON record from a PeerJ article or preprint

    At the moment, PeerJ does not seem to expose its papers in citeproc-json
    format, so this function looks for the DOI, and then uses crossref to
    get the information. This is not optimal, but it works.

    Args:
        pubid: An integer (or string) giving the article/preprint id
        pubtype: either article or preprint
    """
    peerj_url = 'https://peerj.com' + pubtype + 's/' + str(pubid) + '.json'
    request_output = re.get(peerj_url)
    if request_output.status_code == 200 :
        return from_crossref_doi(request_output.json()['doi'])
    else :
        raise ValueError("No PeerJ " + pubtype + " with this ID")

