import string

def makeunique(r, tentative_key):
    if not tentative_key in r.library.keys():
        r.content['id'] = tentative_key
    else :
        alphabet = list(string.ascii_lowercase)
        i = 0
        while(tentative_key+alphabet[i] in r.library.keys()):
            i = i + 1
        r.content['id'] = tentative_key + alphabet[i]

def Year(r):
    return str(r.content['issued']['date-parts'][0][0])

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
