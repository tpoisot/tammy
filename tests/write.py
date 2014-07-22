#! /usr/bin/env python3

import sys, os
import os.path
import unittest
import yaml
import json

orig_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(orig_path)
config_file = os.path.join(os.path.dirname(__file__), 'tammy.yaml')

import tammy

class SameNames(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_name_1(self):
        self.lib.new(tammy.from_crossref_doi('10.1111/j.1461-0248.2010.01493.x'))
        # expected key dev10
        self.lib.write()
        assert os.path.isfile('./tests/bib/records/dev10.yaml')
    def test_name_2(self):
        self.lib.new(tammy.from_crossref_doi('10.1111/j.1365-2664.2009.01744.x'))
        # expected key dev10a
        self.lib.update()
        assert os.path.isfile('./tests/bib/records/dev10.yaml')

class Export(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_write_json(self):
        self.lib.export(path='.', keys=None, output='citeproc-json')
        assert os.path.isfile('default.json')
    def test_write_yaml(self):
        self.lib.export(path='.', keys=None, output='citeproc-json')
        assert os.path.isfile('default.json')

def main():
    if sys.version_info[1] < 7 :
        unittest.main()
    else :
        unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
