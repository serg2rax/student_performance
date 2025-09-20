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
from tabulate import tabulate
from sys import stderr

class App:
    def __init__(self, args, htabs, Student, Teacher):
        self.htab_student_avg = ['№', 'name', 'AVG']
        self.htab_teachers = ['№', 'name', 'subject']
        self.htabs = htabs
        self.args = args
        self.tabs = self.gen_db()
        self.Students = self.gen_lStudents(Student)
        self.grade_Student()
        self.Teachers = self.gen_lTeachers(Teacher)
        self.add_subject_Teachers()

    def gen_db(self)->dict:
        tabs = []
        for db in self.args.file:
            if os.path.isfile(db):
                with open(db, 'r', newline='', encoding="utf8") as fd:
                  reader = csv.DictReader(fd)
                  for row in reader:
                      tabs.append(row)
            else:
                print('File "%s" not found!!!\n' % db, file=stderr)
        return tabs

    def gen_ddlist(self, htb_name:str)->list:
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

    def gen_lStudents(self, Student)->list:
        Students = []
        for name in self.gen_ddlist(self.htabs['htb_student']):
            Students.append(Student(name))
        return Students

    def grade_Student(self):
        for i in range(len(self.Students)):
            for k in range(len(self.tabs)):
                if ( self.tabs[k][self.htabs['htb_student']] ==\
                     self.Students[i].get_name() and\
                     self.tabs[k][self.htabs['htb_grade']]):\
                     self.Students[i].add_grade({\
                     self.tabs[k][self.htabs['htb_subject']]:\
                     self.tabs[k][self.htabs['htb_grade']]})
        return True

    def report(self):
        for report in self.args.report:
            if report == 'student-performance':
                self.report_avg_student()
            if report == 'teachers':
                self.report_teachers()
        return True

    def report_avg_student(self)->list:
        stud = []
        for i in range(len(self.Students)):
            stud.append([i, self.Students[i].get_name(), str(self.Students[i].get_avg())])
        print(tabulate(sorted(stud, key=lambda stud: stud[2], reverse=True), self.htab_student_avg, "grid"))
        return stud

    def report_teachers(self)->list:
        stud = []
        for i in range(len(self.Teachers)):
            stud.append([i, self.Teachers[i].get_name(), str(self.Teachers[i].get_subj())])
        print(tabulate(stud, self.htab_teachers, "grid"))
        return stud

    def file_report_student(self):
        with open(args.report, 'w', encoding="utf8") as fd:
            print(tabulate(self.report_avg_student(), self.htab_student_avg, "grid"), file=fd)
        return True

    def gen_lTeachers(self, Teacher)->list:
        Teachers = []
        for name in self.gen_ddlist(self.htabs['htb_teacher']):
            Teachers.append(Teacher(name))
        return Teachers

    def add_subject_Teachers(self)->list:
        for i in range(len(self.Teachers)):
            for k in range(len(self.tabs)):
                if ( (self.tabs[k][self.htabs['htb_teacher']] ==\
                    self.Teachers[i].get_name()) and\
                    (self.tabs[k][self.htabs['htb_subject']] not in\
                    self.Teachers[i].get_subj()) ):
                    self.Teachers[i].add_subj(\
                    self.tabs[k][self.htabs['htb_subject']])
        return True
