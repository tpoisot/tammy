#! /usr/bin/env python3

import sys, os
import os.path
import unittest
import yaml
import json
import shutil

orig_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(orig_path)
config_file = os.path.join(os.path.dirname(__file__), 'tammy.yaml')

import tammy

class Attach(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_1_attach_single(self):
        """
        This test checks that
        1. the file is attached
        """
        self.lib.records['poi12'].attach('tests/tmp/poi12.pdf', 'published')
        assert os.path.isfile('tests/bib/files/poi12_published.pdf')
        self.lib.update()
    def test_3_attach_several(self):
        """
        This test checks that
        1. The file is attached
        2. When a second file is attached, it will have a unique name
        3. It works well when adding a third file
        """
        self.lib.records['poi12a'].attach('tests/tmp/poi12a.pdf')
        assert os.path.isfile('tests/bib/files/poi12a_1.pdf')
        self.lib.records['poi12a'].attach('tests/tmp/poi12a_data1.csv')
        assert os.path.isfile('tests/bib/files/poi12a_2.csv')
        self.lib.records['poi12a'].attach('tests/tmp/poi12a_data2.txt', 'cytflowdata')
        assert os.path.isfile('tests/bib/files/poi12a_cytflowdata.txt')
        os.remove('tests/bib/files/poi12a_1.pdf')
        os.remove('tests/bib/files/poi12a_2.csv')
        os.remove('tests/bib/files/poi12a_cytflowdata.txt')
    def test_4_no_file(self):
        with self.assertRaises(ValueError):
            self.lib.records['poi12a'].attach('no/such/file')

def main():
    if sys.version_info[1] < 7 :
        unittest.main(verbosity=2)
    else :
        unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
