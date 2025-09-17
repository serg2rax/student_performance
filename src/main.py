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
import sys
from tabulate import tabulate
from .args import args

class teacher:
   def __init__(self, name):
        self.name = name
        self.subject = []
   def add_item(self, subject):
       self.subject.append(subject)

tabs = []

for db in args.file:
    if os.path.isfile(db):
        with open(db, 'r', newline='') as fd:
          reader = csv.DictReader(fd)
          for row in reader:
              tabs.append(row)
    else:
        print('File "%s" not found!!!\n' % db, file=sys.stderr)

def main():
    tab = {i: i for i in tabs[0].keys()}
    print(tabulate(tabs, tab, "grid"))

    for i in tabs:
        teacher([i['teacher_name']]);
        print(i['teacher_name'], i['subject'])

    with open(args.report, 'w') as fd:
        writer = csv.writer(fd, delimiter=' ',
          quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(tabs)


if __name__ == "__main__" :
    main()
