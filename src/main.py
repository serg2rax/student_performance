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

htab_student_avg = ['№', 'name', 'AVG']

def gen_lstudents(tabs:dict)->list:
    students = []
    for name in gen_ddlist(tabs, 'student_name'):
        students.append(student(name))
    return students

def gen_lteachers(tabs:dict)->list:
    teachers = []
    for name in gen_ddlist(tabs, 'teacher_name'):
        teachers.append(teacher(name))
    return teachers

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

def main():
    tabs = gen_db(args.file)
#    tab = {i: i for i in tabs[0].keys()}

    teachers = gen_lteachers(tabs) 
    for i in range(len(teachers)):
        for k in range(len(tabs)):
            if ( (tabs[k]['teacher_name'] == teachers[i].get_name())\
                and (tabs[k]['subject'] not in teachers[i].get_subj()) ):
                teachers[i].add_subj(tabs[k]['subject'])


    students = gen_lstudents(tabs)
    for i in range(len(students)):
        for k in range(len(tabs)):
            if ( tabs[k]['student_name'] == students[i].get_name() and tabs[k]['grade']):
                students[i].add_grade({tabs[k]['subject']: tabs[k]['grade']})

    file_report_student(report_avg_student(students, htab_student_avg),\
        htab_student_avg)


"""
    with open(args.report, 'w' encoding="utf8") as fd:
        writer = csv.writer(fd, delimiter=' ',
          quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(news)
"""

if __name__ == "__main__" :
    main()
