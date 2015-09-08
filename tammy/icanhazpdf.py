import re
import requests
import tempfile
import hashlib

# List of regexp
_wiley = {"re": re.compile(ur'10\.1111'), "f": get_wiley_pdf}
_peerj = {"re": re.compile(ur'peerj'), "f": get_peerj_pdf}
publisher_regex = {"wiley": _wiley, "peerj": _peer}

def detect_publisher(r):
    for pubname, regex in publisher_regex:
        if not re.search(regex, r.content["DOI"]) is None:
            return pubname
    raise ValueError("I cannot find the publisher from the DOI")

# hashlib.md5(doi.encode()).hexdigest()+".pdf"

def download_pdf(url, fname):
    pdf_request = requests.get(url)
    if pdf_request.status_code == 200:
        f = open(fname, "wb")
        f.write(pdf_request.content)
        f.close()
    raise ValueError("The request returned with non 200 status code (it failed)")

def get_wiley_pdf(doi):
    getpdf = re.compile(ur'id="pdfDocument" src="(.+asset.+)" width')
    _url = "http://onlinelibrary.wiley.com/doi/" + doi + "/pdf"
    _url_html_content = requests.get(_url).text
    search_result = re.search(getpdf, _url_html_content)
    if not search_result == None:
        return search_result.group(1)
    else:
        raise ValueError("No PDF (or unable to access)")

def get_pdf_from_ref(r):
    if "DOI" not in r.content:
        raise KeyError("ICanHazPDF module needs a DOI")
    publisher = detect_publisher(doi)
    _fname = hashlib.md5(doi.encode()).hexdigest()+".pdf"
    _url = publisher_regex[publisher]["f"](doi)
    download_pdf(_url, _fname)
    r.attach(_fname, "maintext(auto)")
    r.library.update()
