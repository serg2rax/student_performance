import pytest

from os import sep
from src.args import argp
from src.classes import Student, Teacher
from src.conf import htabs
from src.app import App
from .check import out_gen_db


pars = argp()
args = pars.parse_args()
args.file=['tests' + sep +  '/db.csv']
args.report=['teachers']

class TestApp:
    app = App(args, htabs, Student, Teacher)
    def test_gen_db(self):
        assert self.app.gen_db() ==  out_gen_db
    def test_gen_ddlist(self):
        assert self.app.gen_ddlist(htabs['htb_student']) ==\
            ['Семенова Елена', 'Титов Владислав']
        assert self.app.gen_ddlist(htabs['htb_teacher']) ==\
            ['Ковалева Анна', 'Орлов Сергей', 'Никулин Сергей']
    def test_report_avg_student(self):
        assert self.app.report_avg_student() == [[1, 'Семенова Елена', '5.0'],\
            [2, 'Титов Владислав', '4.0']]

class TestClass:
    app = App(args, htabs, Student, Teacher)
    def test_get_avg(self):
        assert self.app.Students[1].get_avg() == 4.0
    def test_get_subj(self):
        assert self.app.Teachers[1].get_subj() == ['География']
        assert self.app.Teachers[2].get_subj() == ['География']
    def test_len_Teachers(self):
        assert len(self.app.Teachers) == 3
    def test_len_Students(self):
        assert len(self.app.Students) == 2


if __name__ == "__main__":
    pytest
