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
    def add_subj(self, subject):
        self.subject.append(subject)
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def get_subj(self):
        return self.subject

class student:
    def __init__(self, name):
        self.name = name
        self.grade = []
    def add_grade(self, grade):
        self.grade.append(grade)
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def get_grade(self):
        return self.grade

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

    teachers = []
    for i in range(len(tabs)):
        teachers.append( teacher(tabs[i]['teacher_name']))
        name = teachers[i].get_name()
        if(tabs[i]['teacher_name'] == name):
            teachers[i].add_subj(tabs[i]['subject'])
            print(teachers[i].get_name(), teachers[i].get_subj())

    students = []
    students.append(student(tabs[0]['student_name']))
    for i in range(len(tabs)):
        students.append(student(tabs[i]['student_name']))
        name = students[i].get_name()
        for row in tabs:
            if(row['student_name'] == name):
                students[i].add_grade(row['grade'])

    for row in students:
        print(row.get_name(), row.get_grade())

    with open(args.report, 'w') as fd:
        writer = csv.writer(fd, delimiter=' ',
          quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(tabs)

if __name__ == "__main__" :
    main()
