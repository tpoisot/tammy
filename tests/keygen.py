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
    def test_author_has_shortname(self):
        assert tammy.Author(self.lib.records['li03']) == 'Li'
        assert tammy.Aut(self.lib.records['li03']) == 'Li'
    def test_author_is_consortium(self):
        assert tammy.Aut(self.lib.records['rde08']) == 'Rde'
    def test_author_is_editor(self):
        assert tammy.Aut(self.lib.records['pas06']) == 'Pas'
    def test_author_has_space(self):
        assert tammy.Author(self.lib.records['dem00']) == 'Demeeus'
        assert tammy.Aut(self.lib.records['dem00']) == 'Dem'
    def test_anonymous_author(self):
        assert tammy.Aut(self.lib.records['ano11']) == 'Ano'

class Year(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_Noyear(self):
        assert tammy.Year(self.lib.records['lixx']) == 'xxxx'

class Authoryear(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_AuthorYr(self):
        assert tammy.AuthorYr(self.lib.records['poi12']) == 'Poisot12'
    def test_AuthorYear(self):
        assert tammy.AuthorYear(self.lib.records['poi12']) == 'Poisot2012'
    def test_AutYear(self):
        assert tammy.AutYear(self.lib.records['poi12']) == 'Poi2012'
    def test_AutYr(self):
        assert tammy.AutYr(self.lib.records['poi12']) == 'Poi12'
    def test_autYr(self):
        assert tammy.autYr(self.lib.records['poi12']) == 'poi12'
    def test_autYear(self):
        assert tammy.autYear(self.lib.records['poi12']) == 'poi2012'
    def test_AUTYr(self):
        assert tammy.AUTYr(self.lib.records['poi12']) == 'POI12'
    def test_AUTYear(self):
        assert tammy.AUTYear(self.lib.records['poi12']) == 'POI2012'

class SameNames(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_same_names_years(self):
        assert 'poi12a' in self.lib.keys() and 'poi12' in self.lib.keys()

class TitleFunctions(unittest.TestCase):
    @classmethod
    def test_title_is_tokenized(self):
        assert tokenize_title("It has a short title") == ["short", "title"]

def main():
    if sys.version_info[1] < 7 :
        unittest.main()
    else :
        unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
