'''
можно без отдельной функции, сразу из controller.py
'''

from student_database import get_student

def see_rating(last_name):
    # вызов функции просмотра данных ученика
    get_student(last_name)