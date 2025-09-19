"""
Generation student performance analysis report

Written specifically for https://work-mate.ru
Description task: https://docs.google.com/document/d/\
1Wq7ALJDhin2uY5ldh4srWQFsfJxWUZK_SK4INIwUWug

Author : Sergey Alexadrovich Kravchuk
Email  : serg2ak@ya.ru
"""

import csv
import sys
from os.path import os
from tabulate import tabulate
from .args import args
from .classes import *
from .db import *
from .conf import *


class DB:
    def __init__(self, args = args, htabs:list = htabs,\
                    Student = Student, Teacher = Teacher):
        self.htab_student_avg = ['№', 'name', 'AVG']
        self.htabs = htabs
        self.args = args
        self.tabs = self.__gen_db()
        self.Students = self.__gen_lStudents()
        self.grade_Student()

    def __gen_db(self)->dict:
        tabs = []
        for db in self.args.__dict__['file']:
            if os.path.isfile(db):
                with open(db, 'r', newline='', encoding="utf8") as fd:
                  reader = csv.DictReader(fd)
                  for row in reader:
                      tabs.append(row)
            else:
                print('File "%s" not found!!!\n' % db, file=sys.stderr)
        return tabs

    def __gen_ddlist(self, htb_name:str)->list:
        _names = []
        l_tabs = range(len(self.tabs))
        for i in l_tabs:
            _names.append(self.tabs[i][htb_name])
        for i in l_tabs:
            for k in l_tabs:
                if ( i != k and _names[i] == _names[k] ):
                    _names[k] = False
        names = []
        for i in _names:
            if i : names.append(i)
        return names;

    def __gen_lStudents(self)->list:
        Students = []
        for name in self.__gen_ddlist(htabs['htb_student']):
            Students.append(Student(name))
        return Students

    def grade_Student(self):
        tabs = self.tabs
        for i in range(len(self.Students)):
            for k in range(len(tabs)):
                if ( tabs[k][htabs['htb_student']] == self.Students[i].get_name() and tabs[k][htabs['htb_grade']]):
                    self.Students[i].add_grade({tabs[k][htabs['htb_subject']]: tabs[k][htabs['htb_grade']]})
        return True

    def report(self):
        for report in self.args.__dict__['report']:
            if report == 'student-performance':
                self.report_avg_student()
        return True

    def report_avg_student(self)->list:
        stud = []
        for i in range(len(self.Students)):
            stud.append([i, self.Students[i].get_name(), str(self.Students[i].get_avg())])
        print(tabulate(stud, self.htab_student_avg, "grid"))
        return stud

    def file_report_student(self):
        with open(args.report, 'w', encoding="utf8") as fd:
            print(tabulate(self.report_avg_student(), self.htab_student_avg, "grid"), file=fd)
        return True

    def gen_lTeachers(self)->list:
        Teachers = []
        for name in gen_ddlist(self.tabs, htabs['htb_teacher']):
            teachers.append(Teacher(name))
        return Teachers

    def add_subject_Teacher(self)->list:
        self.Teachers = gen_lTeachers(tabs)
        for i in range(len(teachers)):
            for k in range(len(tabs)):
                if ( (tabs[k][htb_teacher] == teachers[i].get_name())\
                    and (tabs[k][htb_subject] not in teachers[i].get_subj()) ):
                    teachers[i].add_subj(tabs[k][htb_subject])
        return teachers
