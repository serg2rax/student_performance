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

def main():
    tabs = gen_db(args.file)
#    tab = {i: i for i in tabs[0].keys()}

    teachers = []
    for name in gen_ddlist(tabs, 'teacher_name'):
        teachers.append(teacher(name))

    for i in range(len(teachers)):
        for k in range(len(tabs)):
            if ( (tabs[k]['teacher_name'] == teachers[i].get_name())\
                and (tabs[k]['subject'] not in teachers[i].get_subj()) ):
                teachers[i].add_subj(tabs[k]['subject'])


    students = []
    for name in gen_ddlist(tabs, 'student_name'):
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
