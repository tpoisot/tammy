import re
import requests
import tempfile
import urllib.request

# List of publisher-specific code

def is_it_elsevier(doi):
    if not re.search(re.compile(u"10\.1016"), doi) is None:
        return True
    return False

def get_elsevier_pdf(doi):
    getpdf = re.compile(u'id="pdflink" src="(.+main.+)" query')
    _doi_url = "http://dx.doi.org/" + doi
    _url = requests.get(_doi_url).url
    _url_html_content = requests.get(_url).text
    search_result = re.search(getpdf, _url_html_content)
    if not search_result == None:
        return search_result.group(1)
    else:
        raise ValueError("No PDF (or unable to access)")

def is_it_roysoc(doi):
    if not re.search(re.compile(u"10\.1098/r"), doi) is None:
        return True
    return False

def get_roysoc_pdf(doi):
    _url = "http://onlinelibrary.wiley.com/doi/" + doi + "/pdf"
    _url_doi = "http://dx.doi.org/" + doi
    _url = requests.get(_url_doi).url
    # TODO what it not found?
    return _url + ".full-text.pdf"

def is_it_wiley(doi):
    if not re.search(re.compile(u"10\.1111"), doi) is None:
        return True
    return False

def get_wiley_pdf(doi):
    getpdf = re.compile(u'id="pdfDocument" src="(.+asset.+)" width')
    _url = "http://onlinelibrary.wiley.com/doi/" + doi + "/pdf"
    _url_html_content = requests.get(_url).text
    search_result = re.search(getpdf, _url_html_content)
    if not search_result == None:
        return search_result.group(1)
    else:
        raise ValueError("No PDF (or unable to access)")

def is_it_peerj(doi):
    if not re.search(re.compile(u'peerj'), doi) is None:
        return True
    return False

def get_peerj_pdf(doi):
    # then return the correct URL
    if not re.search(re.compile(u'preprint'), doi) is None:
        # preprint
        raise ValueError("Not implemented")
    else:
        # not preprint
        get_art_id = re.compile(u'peerj\\.(.+)')
        search_result = re.search(get_art_id, doi)
        if not search_result == None:
            a_id = search_result.group(1)
            _url = "https://peerj.com/articles/" + str(a_id) + ".pdf"
            return _url
    raise ValueError("No such PeerJ resource")

def is_it_plos(doi):
    if not re.search(re.compile(u'10\.1371/journal\.p'), doi) is None:
        return True
    return False

def get_plos_pdf(doi):
    # Step 1 - find out WHICH plos journal it is
    get_jcode = re.compile(u'10\.1371/journal\.p(.+)\.')
    # Search, and return the matching part of the DOI
    journal_code = re.search(get_jcode, doi).group(1)
    codes = {"pat": "pathogens",
            "med": "medicine",
            "gen": "genetics",
            "one": "one",
            "cbi": "compbiol"} # TODO Trop,Biol, ...
    # Check that the journal is handled
    if journal_code in codes:
        jname = codes[journal_code]
    else:
        raise KeyError("PLOS journal currently  not handled")
    # Build the PDF URL
    _url = "http://www.plos" + jname + ".org/article/fetchObject.action?uri=info:doi/" + doi + "&representation=PDF"
    return _url

# List of regexp
publisher_regex = {
        "wiley": get_wiley_pdf,
        "peerj": get_peerj_pdf,
        "plos": get_plos_pdf,
        "roysoc": get_roysoc_pdf,
        "elsevier": get_elsevier_pdf}

# Wrapper to detect the publisher
# TODO MAKE IT BETTER -- e.g. return a tuple (doi, func)
def detect_publisher(r):
    # NOTE This is fugly
    if is_it_peerj(r.content["DOI"]):
        return "peerj"
    if is_it_wiley(r.content["DOI"]):
        return "wiley"
    if is_it_elsevier(r.content["DOI"]):
        return "elsevier"
    if is_it_plos(r.content["DOI"]):
        return "plos"
    if is_it_roysoc(r.content["DOI"]):
        return "roysoc"
    raise ValueError("I cannot find the publisher from the DOI")

def get_pdf_from_ref(r):
    if "DOI" not in r.content:
        # TODO use the `publisher` key
        # TODO use crossref API (and update reference?)
        raise KeyError("ICanHazPDF module needs a DOI")
    doi = r.content["DOI"]
    publisher = detect_publisher(r)
    _fname = '.'.join(doi.split('/'))+".pdf"
    _url = publisher_regex[publisher](doi)
    urllib.request.urlretrieve(_url, filename=_fname)
    r.attach(_fname, "maintext")
    r.library.update()
