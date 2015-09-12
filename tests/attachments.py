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
        self.lib.get('poi_lsa').attach('tests/tmp/poi12.pdf', 'published')
        assert self.lib.get('poi_lsa').has_files()
        assert os.path.isfile('tests/bib/files/Poisot_labcspecialisationapparition_poi12_published.pdf')
        self.lib.update()
    def test_3_attach_several(self):
        """
        This test checks that
        1. The file is attached
        2. When a second file is attached, it will have a unique name
        3. It works well when adding a third file
        """
        self.lib.get('poi_tii').attach('tests/tmp/poi12a.pdf')
        self.lib.get('poi_tii').attach('tests/tmp/poi12a_data1.csv')
        self.lib.get('poi_tii').attach('tests/tmp/poi12a_data2.txt', 'cytflowdata')
        assert self.lib.get('poi_tii').has_files()
        f1 = "Poisot_terminalinvestmentinduced_poi_tii_1.pdf"
        f2 = "Poisot_terminalinvestmentinduced_poi_tii_2.csv"
        f3 = "Poisot_terminalinvestmentinduced_poi_tii_cytflowdata.txt"
        assert os.path.isfile('tests/bib/files/'+f1)
        assert os.path.isfile('tests/bib/files/'+f2)
        assert os.path.isfile('tests/bib/files/'+f3)
        os.remove('tests/bib/files/'+f1)
        os.remove('tests/bib/files/'+f2)
        os.remove('tests/bib/files/'+f3)
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
