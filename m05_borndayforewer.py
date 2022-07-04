# Описание задания:
# 12. (МОДУЛЬ 5) В проекте создать новый модуль borndayforewer.py
# 13.Написать или модернизировать программу (МОДУЛЬ 3)
# используя условные операторы и цикл while:
# Просим пользователя ввести год рождения А.С. Пушкина до тех
# пор пока он не ввел правильный год, после этого спрашиваем
# день рождения до тех пор, пока он не ввел верный день.
# После верного ответа выводим в терминал 'Верно' и выходим из программы


from m02_bornyear import check_year, input_year
from m03_bornday import check_day, input_day

is_year_input = True
while is_year_input:
    # Запрашиваем ввод года до тех пор,
    # пока is_year_input не станет False,
    # или пока пользователь  не отменит ввод
    birth_year = input_year(check_exit=True)
    if birth_year == 'выход':
        print('Пользователь отменил ввод и завершил программу.')
        break   # Завершили цикл while is_year_input
    if check_year(birth_year):
        print('Верно ввели год рождения\n')

        while True:
            birth_day = input_day(check_exit=True)
            if birth_day == 'выход':
                print('Пользователь отменил ввод и завершил программу.')
                is_year_input = False  # это чтобы прервать внешний
                                       # цикл while is_year_input
                break   # Завершили цикл while True
            if check_day(birth_day):
                print('Верно')
                is_year_input = False  # это чтобы прервать внешний
                                       # цикл while is_year_input
                break   # Завершили цикл while True
            else:
                print('\nВвели не правильный день рождения.\n')

    else:    # if check_year(birth_year)
        print('\nВвели не правильный год рождения.\n')


