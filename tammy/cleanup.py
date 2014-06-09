def clean_all(record):
    """ A really messy function to make sure that the citeproc data
    are indeed in the citeproc format. Basically a long list of if/...
    conditions to catch all errors I have noticed.
    """
    record = clean_fields(record)
    return record

def clean_fields(record):
    """ Clean the fields
    """
    if record['type'] == 'journal-article':
        record['type'] = 'article-journal'
    return record

