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

class Wiley(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_attach_wiley_pdf(self):
        """
        This test checks that
        1. the file is attached
        """
        get_pdf_from_ref(self.lib.records['lio15'])
        assert os.path.isfile('tests/bib/files/lio15_pdf(auto).pdf')
        
def main():
    if sys.version_info[1] < 7 :
        unittest.main(verbosity=2)
    else :
        unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
