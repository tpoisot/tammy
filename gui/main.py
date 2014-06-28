#! /usr/bin/env python3

import sys, os
import unittest
import yaml
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import tammy

import npyscreen

class TammyList(npyscreen.NPSApp):
    def main(self):
        lib = tammy.library()
        F = npyscreen.Form(name="List of references")
        l = F.add(npyscreen.GridColTitles, columns=3)
        l.col_titles = ['Key', 'Year', 'Title']
        ## Build a two-dimensional array
        RefList = [[key, tammy.Year(rec), rec.content['title']] for key, rec in lib.records.items()]
        l.values = RefList
        ##
        F.edit()

if __name__ == "__main__":
    App = TammyList()
    App.run()
