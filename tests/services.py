#! /usr/bin/env python3

import sys, os
import unittest
import yaml
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import tammy

class PeerJ(unittest.TestCase):
    def test_pubtype(self):
        self.assertRaises(ValueError, tammy.from_peerj, 200, 'paper')
    def test_argtype(self):
        self.assertRaises(TypeError, tammy.from_peerj, ['200'], 'article')
    def test_works_for_paper(self):
        test_paper = tammy.from_peerj(251, 'article')
        assert test_paper[u'author'][0][u'family'] == u'Poisot'
    def test_no_id(self):
        self.assertRaises(ValueError, tammy.from_peerj, 0, 'article')
    def test_works_for_preprint(self):
        test_paper = tammy.from_peerj(50, 'preprint')
        assert test_paper[u'author'][0][u'family'] == u'Poisot'

class CrossRef(unittest.TestCase):
    def test_correct_doi(self):
        assert isinstance(tammy.from_crossref_doi('10.7717/peerj.426'), dict)
    def test_no_doi(self):
        with self.assertRaises(ValueError):
            tammy.from_crossref_doi('no/no/no')

def main():
    if sys.version_info[1] < 7 :
        unittest.main(verbosity=2)
    else :
        unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
