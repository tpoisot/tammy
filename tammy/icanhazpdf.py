import re
import requests
import tempfile
import urllib.request

# Thanks SciHub!
def get_scihub_pdf(doi):
    _doi_url = "http://sci-hub.io/" + doi
    getpdf = re.compile(u'<iframe src = "(.+\.pdf)">')
    try :
        _url = _doi_url
        _url_html_content = requests.get(_url).text
        search_result = re.search(getpdf, _url_html_content)
        if not search_result == None:
            return search_result.group(1)
        else:
            raise ValueError("Unable to read PDF")
    except :
        raise ValueError("No PDF known to SciHub")

# List of publisher-specific code

def is_it_elsevier(doi):
    if not re.search(re.compile(u"10\.1016"), doi) is None:
        return True
    return False

def get_elsevier_pdf(doi):
    # NOTE ScienceDirect and CellPress have to be handled differently
    _doi_url = "http://dx.doi.org/" + doi
    _url = requests.get(_doi_url).url
    if not re.search(re.compile("sciencedirect"), _url) is None:
        # NOTE this is for science direct
        getpdf = re.compile(u'pdfurl="(.+pdf)"')
        _url_html_content = requests.get(_url).text
        search_result = re.search(getpdf, _url_html_content)
        if not search_result == None:
            pdf_url = search_result.group(1)
    if not re.search(re.compile("cell\.com"), _url) is None:
        # NOTE Cell Press
        getpdf = re.compile(u'href="(.+pdf.+)" onclick')
        _url_html_content = requests.get(_url).text
        search_result = re.search(getpdf, _url_html_content)
        if not search_result == None:
            pdf_url = "http://www.cell.com" + search_result.group(1)
    if not search_result == None:
        return pdf_url
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
    # TODO what if not found?
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


"""
Download the file itself
"""
def download_file(url, fname):
    # Look ma, I'm a browser! Fuck you, publishers.
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
    r = requests.get(url, stream=True, headers=header)
    with open(fname, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    return fname

# Wrapper to detect the publisher
# TODO MAKE IT BETTER -- e.g. return a tuple (doi, func)
def detect_publisher(r):
    # NOTE This is fugly
    if is_it_peerj(r.content["DOI"]):
        return "peerj"
    if is_it_wiley(r.content["DOI"]):
        return "wiley"
    # if is_it_elsevier(r.content["DOI"]):
        # return "elsevier"
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
    _url = None
    try :
        _url = get_scihub_pdf(doi)
    except :
        publisher = detect_publisher(r)
        _url = publisher_regex[publisher](doi)
    if not _url == None:
        _fname = '.'.join(doi.split('/'))+".pdf"
        download_file(_url, _fname)
        # urllib.request.urlretrieve(_url, filename=_fname, headers=header)
        r.attach(_fname, "maintext")
        r.library.update()
