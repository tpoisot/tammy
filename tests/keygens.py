#! /usr/bin/env python3

import sys, os
import unittest
import yaml
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import tammy

class Author(unittest.TestCase):
    def test_author_shortname(self):
        assert tammy.Author('Ho') == 'Ho'
    def test_author_space(self):
        assert tammy.Author('De Meeus') == 'DeMeeus'

def main():
    if sys.version_info[1] < 7 :
        unittest.main()
    else :
        unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
