"""
Generation student performance analysis report

Written specifically for https://work-mate.ru
Description task: https://docs.google.com/document/d/\
1Wq7ALJDhin2uY5ldh4srWQFsfJxWUZK_SK4INIwUWug

Author : Sergey Alexadrovich Kravchuk
Email  : serg2ak@ya.ru
"""

import csv
from os.path import os
from .args import args

def gen_db(arg)->dict:
    tabs = []
    for db in arg:
        if os.path.isfile(db):
            with open(db, 'r', newline='', encoding="utf8") as fd:
              reader = csv.DictReader(fd)
              for row in reader:
                  tabs.append(row)
        else:
            print('File "%s" not found!!!\n' % db, file=sys.stderr)
    return tabs

def gen_ddlist(tabs:dict, name:str)->list:
    """
    """

    __tech = []
    l_tabs = range(len(tabs))
    for i in l_tabs:
        __tech.append(tabs[i][name])
    for i in l_tabs:
        for k in l_tabs:
            if ( i != k and __tech[i] == __tech[k] ):
                __tech[k] = False
    tech = []
    for i in __tech:
        if i : tech.append(i)
    return tech;
