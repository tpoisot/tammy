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
        tammy.icanhazpdf.get_pdf_from_ref(self.lib.get('lio_eim'))
        assert self.lib.get('lio_eim').has_files()
        assert os.path.isfile('tests/bib/files/lio15_maintext.pdf')

class PeerJ(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_attach_peerj_pdf(self):
        record = tammy.from_peerj(251, 'article')
        self.lib.new(record)
        tammy.icanhazpdf.get_pdf_from_ref(self.lib.records['poi_wen'])
        assert os.path.isfile('tests/bib/files/poi_wen_maintext.pdf')


def main():
    if sys.version_info[1] < 7 :
        unittest.main(verbosity=2)
    else :
        unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
