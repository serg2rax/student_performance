"""
Generation student performance analysis report

Written specialy for https://work-mate.ru
Description task: https://docs.google.com/document/d/\
1Wq7ALJDhin2uY5ldh4srWQFsfJxWUZK_SK4INIwUWug

Author : Sergey Alexadrovich Kravchuk
Email  : serg2ak@ya.ru
"""

from .app import App
from .args import argp
from .classes import Student, Teacher
from .conf import htabs
from sys import exit

def main():

    pars = argp()
    args = pars.parse_args()
    if (args.file is None or args.report is None):
        pars.print_help()
        exit(1)

    app = App(args, htabs, Student, Teacher)
    app.report()

if __name__ == "__main__" :
    main()
