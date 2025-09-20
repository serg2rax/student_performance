# student_performance
Written specifically for https://work-mate.ru

Пример отчета:
![report_student-performance.png](https://github.com/serg2rax/student_performance/blob/main/img/report_student-performance.png)

Имена студентов и оценок хранится в классе App списке Students

<https://github.com/serg2rax/student_performance/blob/6fd7a47050852445ee04bd0c3f979f7683328a2e/src/app.py#L26>

Чтобы добавить новый отчет нужно добавить название и вызов функции в класс App.report()
строка 80 в файле src/app.py

<https://github.com/serg2rax/student_performance/blob/31810c502a6ced7ae246bfc7a7536b73265f2321/src/app.py#L80-L86>

пример:
```Python
  if report == 'new_report_name':
      self.report_new_func()
```
