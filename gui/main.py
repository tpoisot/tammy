#! /usr/bin/env python3

import sys, os
import unittest
import yaml
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import tammy

import npyscreen

def type_to_str(t):
    types = {
                'article-journal': 'Paper',
                'book': 'Book',
                'thesis': 'Thesis',
                'chapter': 'Chapter',
                'report': 'Report',
                'no-type': 'Unknown',
                'paper-conference': 'Proceedings'
            }
    return types[t] if t in types else t

class TammyList(npyscreen.NPSApp):
    def __init__(self):
        self.lib = tammy.library()
    def main(self):
        F = npyscreen.Form(name="List of references")
        ref_list = F.add(npyscreen.GridColTitles, columns=6, max_height=25)
        ref_list.col_titles = ['Key', 'Title', 'Author', 'Year', 'In', 'Type']
        ## Build a two-dimensional array
        RefList = [
                    [key,
                    rec.content['title'],
                    tammy.Author(rec),
                    tammy.Year(rec),
                    rec.content['container-title'] if 'container-title' in rec.content else '  ',
                    type_to_str(rec.content['type'])
                    ] for key, rec in self.lib.records.items()
                ]
        ref_list.values = RefList
        ## Series of filters
        filter_title = F.add(npyscreen.TitleText, name='Titles: ')
        ## Make the form active
        F.edit()

if __name__ == "__main__":
    App = TammyList()
    App.run()
