"""
Generation student performance analysis report

Written specifically for https://work-mate.ru
Description task: https://docs.google.com/document/d/\
1Wq7ALJDhin2uY5ldh4srWQFsfJxWUZK_SK4INIwUWug

Author : Sergey Alexadrovich Kravchuk
Email  : serg2ak@ya.ru
"""


class teacher:
    def __init__(self, name):
        self.name = name
        self.subject = []

    def set_name(self, name):
        self.name = name
    def add_subj(self, subject):
        self.subject.append(subject)

    def get_name(self):
        return self.name
    def get_subj(self):
        return self.subject


class student:
    def __init__(self, name):
        self.name = name
        self.grade = []

    def add_grade(self, grade):
        self.grade.append(grade)
    def set_name(self, name):
        self.name = name
    def set_avg(self, avg):
        self.avg = avg
        
    def get_name(self):
        return self.name
    def get_grade(self):
        return self.grade
    def get_avg(self):
        count = 0
        for grade in self.grade:
            for subject, digit in grade.items():
                digit = int(digit)
                if count :
                    digit += digit
                count += 1
        return digit / count
