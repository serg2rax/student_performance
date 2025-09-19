"""
Generation student performance analysis report

Written specialy for https://work-mate.ru
Description task: https://docs.google.com/document/d/\
1Wq7ALJDhin2uY5ldh4srWQFsfJxWUZK_SK4INIwUWug

Author : Sergey Alexadrovich Kravchuk
Email  : serg2ak@ya.ru
"""

from tabulate import tabulate
from .args import args
from .classes import *
from .db import *
from .func import *

htab_student_avg = ['№', 'name', 'AVG']
htb_teacher = 'teacher_name'
htb_student = 'student_name'
htb_subject = 'subject'
htb_grade = 'grade'


def main():
    tabs = gen_db(args.file)

    file_report_student(report_avg_student(add_grade_student(tabs), htab_student_avg),\
        htab_student_avg)


if __name__ == "__main__" :
    main()
