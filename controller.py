from teacher import add_student, put_rating
from student_database import save_db, load_db
from student import see_rating


def controller():
    load_db() # выгрузка данных из файла db_student.json
    match input('Представьтесь, пожалуйста: 1 - учитель; 2 - ученик\n'):
    # Функция match используется для поиска в начале строки подстроки, которая соответствует шаблону
        
        case '1': # блок кода учителя
            flag = 1
            while flag == 1:
                print('Выберите действие')
                act = input('1 - записать ученика, 2 - выставить оценку, 0 - выйти из программы\nВвод: ')
                if act == '1':
                    add_student()
                elif act == '2':
                    put_rating()
                elif act == '0':
                    flag = 0
            else:
                save_db() # сохранение данных в файл db_student.json
        
        case '2': # блок кода ученика
            flag = 1
            while flag == 1:
                last_name = input('Введите фамилию ученика или 0 для выхода из программы\n')
                if last_name == '0':
                    flag = 0
                else:
                    see_rating(last_name) # проверять оценки