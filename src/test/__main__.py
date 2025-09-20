import unittest
from os import sep
from ..args import argp
from ..classes import Student, Teacher
from ..conf import htabs
from ..app import App
from .check import out_gen_db

pars = argp()
args = pars.parse_args()
args.file=['src' + sep + 'test' + sep +  '/db.csv']
args.report=['teachers']

app = App(args, htabs, Student, Teacher)
print(app.report_avg_student())

class TestApp(unittest.TestCase):
    def test_correct_db(self):
        self.assertEqual(app.gen_db(), out_gen_db)
    def test_duplicate(self):
        self.assertEqual(app.gen_ddlist(htabs['htb_student']),\
            ['Семенова Елена', 'Титов Владислав'])
        self.assertEqual(app.gen_ddlist(htabs['htb_teacher']),\
            ['Ковалева Анна', 'Орлов Сергей', 'Никулин Сергей'])
    def test_avg_db(self):
        self.assertEqual(app.report_avg_student(),\
            [[0, 'Семенова Елена', '5.0'], [1, 'Титов Владислав', '4.0']])

class TestClass(unittest.TestCase):
    def test_avg(self):
        self.assertEqual(app.Students[1].get_avg(), 4.0)


if __name__ == "__main__":
    unittest.main()
