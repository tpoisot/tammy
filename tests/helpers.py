#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
import unittest
import yaml
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import tammy

class StringClear(unittest.TestCase):
    def test_unicode_to_str(self):
        assert tammy.keygen.clean_str(u'éäio') == 'eaio'
    def test_str_to_str(self):
        assert tammy.keygen.clean_str(u'eaio') == 'eaio'
    def test_tokenize_unicode(self):
        print(tammy.keygen.tokenize_string(u'éabCD éfgh'))
        assert tammy.keygen.tokenize_string(u'éabCD éfgh') == ['eabcd', 'efgh']

def main():
    if sys.version_info[1] < 7 :
        unittest.main(verbosity=2)
    else :
        unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
