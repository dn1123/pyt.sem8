from student_database import set_student, set_rating

def add_student():
    # Получение данных ученика от учителя и их передача для записи
    metric = input('Введите данные (Фамилия, Имя, Класс через пробел): ').split(' ')
    set_student(metric)

def put_rating():
    # Получение данных оценки от учителя и их передача для записи
    last_name = input('Введите фамилию ученика: ')
    lesson = input('Введите название урока: ')
    ratlng = input('Введите оценку или оценки через пробел: ').split()
    set_rating(last_name, lesson, ratlng)