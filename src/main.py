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
from .classes import Student, Teacher
from .db import DB
from .func import gen_lStudents, gen_lTeachers, add_subject_Teacher,\
                    add_grade_Student, report_avg_student, file_report_student
from .conf import *

def main():

    app = DB()
    app.report()

if __name__ == "__main__" :
    main()
