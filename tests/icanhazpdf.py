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

class General(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_no_doi(self):
        """
        If a reference has no DOI, there should be a Key Error
        """
        self.assertRaises(KeyError, lambda x: tammy.icanhazpdf.get_pdf_from_ref(self.lib.get(x)), 'rde_lef')

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
        assert os.path.isfile('tests/bib/files/Liow_ecologicalinteractionsmacroevolutionary_lio_eim_maintext.pdf')

class PeerJ(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_attach_peerj_pdf(self):
        record = tammy.from_peerj(251, 'article')
        self.lib.new(record)
        tammy.icanhazpdf.get_pdf_from_ref(self.lib.get('poi_wen'))
        assert os.path.isfile('tests/bib/files/Poisot_whenecologicalnetwork_poi_wen_maintext.pdf')

class PLOS(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lib = tammy.library(cfile=config_file)
    def test_attach_plos_pdf(self):
        record = tammy.from_crossref_doi("10.1371/journal.ppat.1005137")
        self.lib.new(record)
        tammy.icanhazpdf.get_pdf_from_ref(self.lib.get('lyn_rld'))
        print(self.lib.get('lyn_rld').content['files'])

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
