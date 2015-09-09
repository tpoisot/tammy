# -*- coding: utf-8 -*-

import string
import unicodedata

def clean_str(s):
    """ Clean a string
    """
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()

def tokenize_string(s):
    """ Takes a string, and return a list of words

    #. the string is splitted on all whitespace
    #. each word is lowercased
    #. words shorther than 3 letters are removed
    #. the resulting array is returned

    """
    print(s)
    swords = ["in", "of", "and", "a", "the"]
    tokens = filter(lambda t: len(t) > 2, map(lambda x: clean_str(x).lower(), s.split(' ')))
    tokens = filter(lambda t: t not in swords, tokens)
    tokens = list(tokens)
    if len(tokens) == 0:
        tokens = ["x"]
    print(tokens)
    return tokens

def makekey(r):
    """
    Generate a key based on config file
    """
    formatters = {
        # Author formatting
        "aut": lambda x: Aut(x).lower(),
        "Aut": lambda x: Aut(x),
        "AUT": lambda x: Aut(x).upper(),
        "author": lambda x: Author().lower(),
        "Author": lambda x: Author(x),
        "AUTHOR": lambda x: Author(x).upper(),
        # Years
        "Year": lambda x: Year(x),
        "Yr": lambda x: Yr(x),
        # Title
        "tl": lambda x: title_threeletters(x),
        "tw": lambda x: title_threewords(x)
    }
    keyformat = r.library.config['key']
    key = []
    for element in keyformat:
        if element in formatters:
            key.append(formatters[element](r))
        else:
            key.append(element)
    return ''.join(map(str, key))


def makeunique(r):
    """ Make a citation key unique

    This function will perform the following steps, in order:

        #. encode the key in ascii to remove any funky characters, so that
        for example, ``çél2014`` will become ``cel2014``.

        #. check that the key if unique in the library. If this is not the case,
        then it will loop through numbers to find a unique combination. This
        will result in, e.g., Doe2014_3

    Returns:
        Nothing, but changes the ``id`` key of the ``content`` of the record.

    """
    tentative_key = makekey(r)
    if not tentative_key in r.library.keys():
        r.content['id'] = tentative_key
    else :
        i = 2
        while tentative_key+"_"+str(i) in r.library.keys():
            i = i + 1
        tk = tentative_key+"_"+str(i)
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

def title_threewords(r):
    """ First two words

    """
    title = "Unknown Title"
    if 'title' in r.content:
        title = r.content['title']
    title = tokenize_string(title)
    if len(title) > 3:
        title = title[0:3]
    return ''.join(title)

def title_threeletters(r):
    """ First letters of first two words

    """
    title = "Unknown Title"
    if 'title' in r.content:
        title = r.content['title']
    title = tokenize_string(title)
    if len(title) > 3:
        title = title[0:3]
    return ''.join(list(map(lambda x: x[0], title)))
