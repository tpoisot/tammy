# -*- coding: utf-8 -*-

import string
import unicodedata

def clean_str(s):
    """ Clean a string
    """
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()

def makeunique(r, tentative_key):
    """ Make a citation key unique

    This function will perform the following steps, in order:

        #. encode the key in ascii to remove any funky characters, so that
        for example, ``çél2014`` will become ``cel2014``.

        #. check that the key if unique in the library. If this is not the
        case, then it will loop through all (lowercase) letters, append them
        to the key, and if this is unique, write it.

    Returns:
        Nothing, but changes the ``id`` key of the ``content`` of the record.

    """
    if not tentative_key in r.library.keys():
        r.content['id'] = tentative_key
    else :
        alphabet = list(string.ascii_lowercase)
        i = 0
        while(tentative_key+alphabet[i] in r.library.keys()):
            i = i + 1
        tk = tentative_key + alphabet[i]
        r.content['id'] = tk

def Year(r):
    """ Returns the year for a record

    This will look first in "issued", then "accessed", then finally return
    "XXXX" if no date object is found.

    Returns:
        A string with either the year (four digits) or XXXX if no date object is found

    """
    for type_of_date in ['issued', 'accessed']:
        if type_of_date in r.content:
            dpart = r.content[type_of_date]['date-parts'][0][0]
            return clean_str(str(dpart))
    return clean_str('xxxx')

def Yr(r):
    year = Year(r)
    return year[-2]+year[-1]

def read_name(obj):
    for author_type in ['family', 'literal']:
        if author_type in obj[0]:
            return clean_str(obj[0][author_type].capitalize().replace(' ','' ))

def Author(r):
    if 'author' in r.content:
        return read_name(r.content['author'])
    elif 'editor' in r.content:
        return read_name(r.content['editor'])
    return clean_str('Anonymous')

def Aut(r):
    if len(Author(r)) < 3 :
        return Author(r)
    else :
        return Author(r)[0:3]

def AuthorYear(r):
    """ Author year format

    Smith et al. 2010 : Smith2010

    """
    tentative_key = Author(r) + Year(r)
    return tentative_key

def AuthorYr(r):
    """ Author yr format

    Smith et al. 2010 : Smith10

    """
    tentative_key = Author(r) + Yr(r)
    return tentative_key

def AutYear(r):
    """ Author year format

    Smith et al. 2010 : Smi2010

    """
    tentative_key = Aut(r) + Year(r)
    return tentative_key

def AutYr(r):
    """ Author yr format

    Smith et al. 2010 : Smi10

    """
    tentative_key = Aut(r) + Yr(r)
    return tentative_key

def autYr(r):
    """ aut yr format

    Smith et al. 2010 : smi10

    """
    return AutYr(r).lower()

def autYear(r):
    """ aut year format

    Smith et al. 2010 : smi2010
    """
    return AutYear(r).lower()

def AUTYr(r):
    """ AUT yr format

    Smith et al. 2010 : SMI10

    """
    return Aut(r).upper() + Yr(r)

def AUTYear(r):
    """ AUT year format

    Smith et al. 2010 : SMI2010
    """
    return Aut(r).upper() + Year(r)
