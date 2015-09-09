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

class a_import(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
        self.lib.new(tammy.IO.from_file("tests/REF/readfrom/dev10.yaml", "citeproc-yaml"))
        self.lib.new(tammy.IO.from_file("tests/REF/readfrom/dev10a.yaml", "citeproc-yaml"))
        self.lib.new(tammy.IO.from_file("tests/REF/readfrom/poi12b.yaml", "citeproc-yaml"))
    def test_1_unique_ids(self):
        assert "dev_dme" in self.lib.keys()
        assert "dev_smc" in self.lib.keys()
    def test_2_write_files(self):
        self.lib.write()
        assert os.path.isfile('tests/bib/records/dev_dme.yaml')
        assert os.path.isfile('tests/bib/records/dev_smc.yaml')
        self.lib.export(path='tests/bib', output='citeproc-json')
        assert os.path.isfile('tests/bib/default.json')
        os.remove('tests/bib/records/dev_dme.yaml')
        os.remove('tests/bib/records/dev_smc.yaml')
        os.remove('tests/bib/default.json')
    def test_3_read_unsupported(self):
        with self.assertRaises(ValueError):
            tammy.IO.from_file("tests/REF/readfrom/dev10a.yaml", "RIS")
    def test_4_no_file(self):
        with self.assertRaises(ValueError):
            tammy.IO.from_file("tests/REF/readfrom/nofile.yaml", "citeproc-yaml")
    def test_5_added_poi12c(self):
        assert "poi_dsi" in self.lib.keys()

class b_export(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_write_json(self):
        self.lib.export(path='tests/bib/', keys=None, output='citeproc-json')
        assert os.path.isfile('tests/bib/default.json')
        os.remove('tests/bib/default.json')
    def test_write_yaml(self):
        self.lib.export(path='tests/bib/', keys=None, output='citeproc-yaml')
        assert os.path.isfile('tests/bib/default.yaml')
    def test_wrong_serializer(self):
        with self.assertRaises(KeyError):
            self.lib.export(path='.', keys=None, output='bibtex')
    def test_only_some_keys(self):
        self.lib.export(keys=["poi12"], output="citeproc-yaml")
        record = tammy.IO.from_file("tests/bib/default.yaml", "citeproc-yaml")
        assert len(record) == 1
        assert record[0]['id'] == "poi12"
        os.remove('tests/bib/default.yaml')

def main():
    if sys.version_info[1] < 7 :
        unittest.main(verbosity=2)
    else :
        unittest.main(verbosity=3)

if __name__ == '__main__':
    main()
