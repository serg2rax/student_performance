# student_performance
Written specifically for https://work-mate.ru

Пример отчета:
![report_student-performance.png](https://github.com/serg2rax/student_performance/blob/main/img/report_student-performance.png)

Имена преподавателей и дисциплин хранится в классе App списке Teachers
Чтобы добавить новый отчет нужно добавить название и вызов функции в класс App.report()
строка 80 в файле src/app.py

пример:
```Python
  if report == 'new_report_name':
      self.report_new_func()
```
