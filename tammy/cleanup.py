def clean_all(record):
    """ A really messy function to make sure that the citeproc data
    are indeed in the citeproc format. Basically a long list of if/...
    conditions to catch all errors I have noticed.
    """
    record = clean_fields(record)
    for arrayed in ['ISSN']:
        if arrayed in record:
            record = clean_arrayed(record, arrayed)
    return record

def clean_fields(record):
    """ Clean the fields
    """
    if record['type'] == 'journal-article':
        record['type'] = 'article-journal'
    return record

def clean_arrayed(record, field):
    """ Converts arrayed fields for use in pandoc-citeproc

    This is quite a ugly thing to do but pandoc-citeproc
    has very strict preconceptions of how some fields should
    be formatted, so for the moment I must comply with it

    Args:
        record: the ``dict`` representation
        field: the name of the field to update

    Returns:
        record with ``field`` flattened and joined by ``,``

    """
    if isinstance(record[field], list):
        if len(record[field]) == 1 :
            record[field] = record[field][0]
        else :
            record[field] = ','.join(map(str, record[field]))
    return record
