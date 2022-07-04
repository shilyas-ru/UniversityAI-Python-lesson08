# Описание задания:
# 10. (МОДУЛЬ 4) В проекте создать новый модуль bornyearforewer.py
# 11. Написать или модернизировать программу (МОДУЛЬ 2)
# используя условные операторы и цикл while:
# Работа программы аналогично МОДУЛЬ 2, но спрашиваем пользователя
# до тех пор, пока он не введет верный год рождения.
# После ввода верного года рождения выводим в терминал 'Верно' и выходим из программы


from m02_bornyear import check_year, input_year


while True:
    birth_year = input_year(check_exit=True)
    if birth_year == 'выход':
        print('Пользователь отменил ввод и завершил программу.')
        break
    if check_year(birth_year):
        print('Верно')
        break
    else:
        print('\nВвели не правильный год рождения.\n')