#! /usr/bin/env python3

import sys, os
import unittest
import yaml
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
config_file = os.path.join(os.path.dirname(__file__), 'tammy.yaml')
import tammy

class Title(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_title_shorteners(self):
        assert tammy.title_threewords(self.lib.records['li03']) == "dnamicroarraytechnology"
        assert tammy.title_threeletters(self.lib.records['li03']) == "dmt"

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
        assert tammy.Year(self.lib.records['li_dmt']) == 'xxxx'

class SameNames(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_same_names_years(self):
        assert 'poi12a' in self.lib.keys() and 'poi12' in self.lib.keys()

def main():
    if sys.version_info[1] < 7 :
        unittest.main()
    else :
        unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
