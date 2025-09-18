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

    def set_name(self, name):
        self.name = name
    def add_subj(self, subject):
        self.subject.append(subject)

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
    def set_avg(self, avg):
        self.avg = avg
        
    def get_name(self):
        return self.name
    def get_grade(self):
        return self.grade
    def get_avg(self):
        count = 0
        for grade in self.grade:
            for k, digit in grade.items():
                digit = int(digit)
                if count :
                    digit += digit
                count += 1
        return digit / count


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

def main():
    tabs = gen_db(args.file)
#    tab = {i: i for i in tabs[0].keys()}
#    print(tabulate(tabs, tab, "grid"))

    __teachers = gen_ddlist(tabs, 'teacher_name')
    teachers = []
    for name in __teachers:
        teachers.append(teacher(name))

    for i in range(len(teachers)):
        for k in range(len(tabs)):
            if ( (tabs[k]['teacher_name'] == teachers[i].get_name()) and (tabs[k]['subject'] not in teachers[i].get_subj()) ):
                teachers[i].add_subj(tabs[k]['subject'])


    __students = gen_ddlist(tabs, 'student_name')
    students = []
    for name in __students:
        students.append(student(name))

    for i in range(len(students)):
        for k in range(len(tabs)):
            if ( tabs[k]['student_name'] == students[i].get_name() and tabs[k]['grade']):
                students[i].add_grade({tabs[k]['subject']: tabs[k]['grade']})

    stud = []
    for i in range(len(students)):
        stud.append([i, students[i].get_name(), str(students[i].get_avg())])

    tab = ['№', 'name', 'AVG']
    print(tabulate(stud, tab, "grid"))

    with open(args.report, 'w', encoding="utf8") as fd:
        print(tabulate(stud, tab, "grid"), file=fd)


"""
    with open(args.report, 'w' encoding="utf8") as fd:
        writer = csv.writer(fd, delimiter=' ',
          quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(news)
"""

if __name__ == "__main__" :
    main()
