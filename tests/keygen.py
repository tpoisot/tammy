#! /usr/bin/env python3

import sys, os
import unittest
import yaml
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import tammy

class Author(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile='tests/.tammy.yaml')
        # Short author name
        self.lib.new(tammy.from_crossref_doi('10.1016/0378-1119(89)90358-2'))
        # Author name with space
        self.lib.new(tammy.from_crossref_doi('10.1093/bioinformatics/btm500'))
        # Consortium
        self.lib.new(tammy.from_crossref_doi('10.3201/eid1201.051371'))
    def test_author_shortname(self):
        assert tammy.Author(self.lib.records['ho89']) == 'Ho'
    def test_author_consortium(self):
        assert tammy.Author(self.lib.records['wor06']) == 'Wor'
    def test_author_space(self):
        assert tammy.Author(self.lib.records['dev07']) == 'Devienne'
        assert tammy.Aut(self.lib.records['dev07']) == 'Dev'

class SameNames(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile='tests/.tammy.yaml')
    def test_make_ref1(self):
        self.lib.new(tammy.from_crossref_doi('10.1111/j.1461-0248.2010.01493.x'))
        assert 'dev10' in self.lib.keys()
    def test_make_ref2(self):
        self.lib.new(tammy.from_crossref_doi('10.1111/j.1365-2664.2009.01744.x'))
        print(self.lib.keys())
        assert 'dev10a' in self.lib.keys()

def main():
    if sys.version_info[1] < 7 :
        unittest.main()
    else :
        unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
