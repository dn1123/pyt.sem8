import json  # JSON - JavaScript Object Notation
import os

def set_student(data_list):
    """записывает данные ученика в словарь, например: {"Иванов": (["Иван", "1А"], {Инф: [5, 4, 5, 4, 5]})}"""
    student_db[data_list[0]] = data_list[1:], {} # data_list[0] - это фамилия
    # Двоеточие : в индексе списка дает длину до конца

def set_rating(last_name, lesson, rating):
    """добавление оценок. Пытаемся найти человека по ключу"""
    if student_db.get(last_name) is None:
        print(f'Ученик с фамилией {last_name} не найден')
        print(student_db)
    else:
        if lesson in student_db[last_name][1]:
            student_db[last_name][1][lesson].extend(rating)
        else:
            student_db[last_name][1][lesson] = rating

def get_student(last_name_student):
    """вывод данных ученика. Пытаемся найти человека по ключу"""
    if student_db.get(last_name_student) is None: # если НЕ находим ученика
        print(f'Ученик с фамилией {last_name_student} не найден')
    else: # если ученик найден, то создаем data для значений ключа
        data = student_db[last_name_student]
        print(f'{last_name_student} {", ".join(data[0])}: ') # join чтобы склеивать элементы
        print(*[f'{key}: {", ".join(value)}' for key, value in data[1].items()], sep='\n') # join объединяет значения ключа
        # индекс 0 - имя, класс; индекс 1 - предмет, оценки

def save_db():
    # сохранение сведений об учениках из словаря 'student_db' в файл формата .json
    # Scan_of_synopsis_Python_Berdyugin_AA - 14 страница про словари
    json.dump(student_db, open('db_student.json', 'w'))

def load_db():
    """Сохранение данных учеников из файла *.json в словарь 'student_db'"""
    global student_db
    if os.stat('db_student.json').st_size == 0:
        student_db = {}
    else:
        student_db = json.load(open('db_student.json'))