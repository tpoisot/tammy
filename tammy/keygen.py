# -*- coding: utf-8 -*-

import string
import unicodedata

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
    tentative_key = unicodedata.normalize('NFKD', tentative_key).encode('ascii', 'ignore')
    if not tentative_key in r.library.keys():
        r.content['id'] = tentative_key
    else :
        alphabet = list(string.ascii_lowercase)
        i = 0
        while(tentative_key+alphabet[i] in r.library.keys()):
            i = i + 1
        r.content['id'] = tentative_key + alphabet[i]

def Year(r):
    """ Returns the year for a record

    This will look first in "issued", then "accessed", then finally return
    "XXXX" if no date object is found.

    Returns:
        A string with either the year (four digits) or XXXX if no date object is found

    """
    for type_of_date in ['issued', 'accessed']:
        if type_of_date in r.content:
            return str(r.content[type_of_date]['date-parts'][0])
    return 'XXXX'

def Yr(r):
    year = Year(r)
    return year[-2]+year[-1]

def Author(r):
    return r.content['author'][0]['family'].capitalize()

def Aut(r):
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
    tentative_key = Author() + Yr(r)
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
    return AutYr(r).lower()

def AUTYear(r):
    """ AUT year format

    Smith et al. 2010 : SMI2010
    """
    return AutYear(r).lower()
