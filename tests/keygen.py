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
        assert tammy.title_threewords(self.lib.get('li_dmt')) == "dnamicroarraytechnology"
        assert tammy.title_threeletters(self.lib.get('li_dmt')) == "dmt"

class Author(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_author_has_shortname(self):
        assert tammy.Author(self.lib.get('li_dmt')) == 'Li'
        assert tammy.Aut(self.lib.get('li_dmt')) == 'Li'
    def test_author_is_consortium(self):
        assert tammy.Aut(self.lib.get('rde_lef')) == 'Rde'
    def test_author_is_editor(self):
        assert tammy.Aut(self.lib.get('pas_enl')) == 'Pas'
    def test_author_has_space(self):
        assert tammy.Author(self.lib.get('dem_ebh')) == 'Demeeus'
        assert tammy.Aut(self.lib.get('dem_ebh')) == 'Dem'
    def test_anonymous_author(self):
        assert tammy.Aut(self.lib.get('ano_gpa')) == 'Ano'

class Tokens(unittest.TestCase):
    def test_small_string(self):
        assert tammy.keygen.tokenize_string("ab cd")[0] == "x"

#class Year(unittest.TestCase):
#    @classmethod
#    def setUp(self):
#        self.lib = tammy.library(cfile=config_file)
#    def test_Noyear(self):
#        assert tammy.Year(self.lib.get('li_dmt_2')) == 'xxxx'

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
