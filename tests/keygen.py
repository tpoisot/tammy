#! /usr/bin/env python3

import sys, os
import unittest
import yaml
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
config_file = os.path.join(os.path.dirname(__file__), 'tammy.yaml')
import tammy

class Author(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_author_shortname(self):
        self.lib.new(tammy.from_crossref_doi('10.1016/0378-1119(89)90358-2'))
        assert tammy.Author(self.lib.records['ho89']) == 'Ho'
    def test_author_consortium(self):
        self.lib.new(tammy.from_crossref_doi('10.3201/eid1201.051371'))
        assert tammy.Aut(self.lib.records['cen12']) == 'Cen'
    def test_author_space(self):
        self.lib.new(tammy.from_crossref_doi('10.1093/bioinformatics/btm500'))
        assert tammy.Author(self.lib.records['dev07']) == 'Devienne'
        assert tammy.Aut(self.lib.records['dev07']) == 'Dev'

class Authoryear(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
        self.lib.new(tammy.from_crossref_doi('10.1186/2192-1709-2-13'))
    def AuthorYr(self):
        assert tammy.AuthorYr(self.lib.records['poi13']) == 'Poisot13'
    def AuthorYear(self):
        assert tammy.AuthorYear(self.lib.records['poi13']) == 'Poisot13'
    def AutYear(self):
        assert tammy.AuthorYear(self.lib.records['poi13']) == 'Poi2013'
    def AutYr(self):
        assert tammy.AuthorYear(self.lib.records['poi13']) == 'Poi13'
    def autYr(self):
        assert tammy.AuthorYear(self.lib.records['poi13']) == 'poi13'
    def AUTYr(self):
        assert tammy.AuthorYear(self.lib.records['poi13']) == 'POI13'
    def AUTYear(self):
        assert tammy.AuthorYear(self.lib.records['poi13']) == 'POI2013'


class SameNames(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_same_names_years(self):
        self.lib.new(tammy.from_crossref_doi('10.1111/j.1461-0248.2010.01493.x'))
        self.lib.new(tammy.from_crossref_doi('10.1111/j.1365-2664.2009.01744.x'))
        assert 'dev10a' in self.lib.keys() and 'dev10' in self.lib.keys()

def main():
    if sys.version_info[1] < 7 :
        unittest.main()
    else :
        unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
