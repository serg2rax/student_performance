"""
Generation student performance analysis report

Written specifically for https://work-mate.ru
Description task: https://docs.google.com/document/d/\
1Wq7ALJDhin2uY5ldh4srWQFsfJxWUZK_SK4INIwUWug

Author : Sergey Alexadrovich Kravchuk
Email  : serg2ak@ya.ru
"""

from tabulate import tabulate
from .args import args
from .classes import *
from .db import *
from .conf import *


def gen_lStudents(tabs:dict)->list:
    students = []
    for name in gen_ddlist(tabs, htb_student):
        students.append(Student(name))
    return students

def gen_lTeachers(tabs:dict)->list:
    teachers = []
    for name in gen_ddlist(tabs, htb_teacher):
        teachers.append(Teacher(name))
    return teachers

def add_subject_Teacher(tabs:dict)->list:
    teachers = gen_lTeachers(tabs)
    for i in range(len(teachers)):
        for k in range(len(tabs)):
            if ( (tabs[k][htb_teacher] == teachers[i].get_name())\
                and (tabs[k][htb_subject] not in teachers[i].get_subj()) ):
                teachers[i].add_subj(tabs[k][htb_subject])
    return teachers

def add_grade_Student(tabs:dict)->list:
    students = gen_lStudents(tabs)
    for i in range(len(students)):
        for k in range(len(tabs)):
            if ( tabs[k][htb_student] == students[i].get_name() and tabs[k]['grade']):
                students[i].add_grade({tabs[k][htb_subject]: tabs[k][htb_grade]})
    return students

def report_avg_student(students, htab_student_avg)->list:
    stud = []
    for i in range(len(students)):
        stud.append([i, students[i].get_name(), str(students[i].get_avg())])
    print(tabulate(stud, htab_student_avg, "grid"))
    return stud

def file_report_student(stud, htab_student_avg):
    with open(args.report, 'w', encoding="utf8") as fd:
        print(tabulate(stud, htab_student_avg, "grid"), file=fd)
    return True
