# Задание для этого модуля.
# 2. (МОДУЛЬ 1) В проекте создать новый модуль m01_variables.py
# 3. Выбрать объект для описания из списка: овощ, еда,
#    сотрудник, игрушка (так же можно придумать свой)
# 4. Объявить переменные основных типов данных для описания этого объекта:
#
# Например объект школьник:
# имя (тип строка), возраст (тип целое число), класс (тип целое число),
# отличник или нет (логический тип), средняя оценка (число с плавающей точкой)
#
# Чем больше переменных (характеристик), тем лучше. Минимально 4 переменные
# для типов (строка, число, число с плавающей точкой, логический тип)
#
# 5. В конце модуля с помощью функции type вывести тип для каждой из объявленных переменных



# объект для описания: сотрудник

# строка
name = 'Андрей'            # Имя сотрудника
patronymic = 'Петрович'    # Отчество сотрудника
surname = 'Иванов'         # Фамилия сотрудника

# число
age = 25           # Возраст на момент устройства на работу
experience = 2     # Jпыт

# число с плавающей точкой
salary = 10.5      # зарплата (оклад) в тысячах рублей
prize = 0.1        # премия в долях от зарплаты (то есть, 10%)
# логический тип
is_man = True                 # Мужчина
is_sick_with_covid19 = False  # Болеет или нет ковидом



# Переменные, сразу содержащая описание
# (описание типов не обязательно,
# а возможность в послеждних версиях)
full_name: str = (name + ' ' +                  # Полное имя
                 patronymic + ' ' +
                 surname)
current_age: int = age + experience             # Текущий возраст
is_woman: bool = not is_man                     # Женщина
full_salary: float = salary * (1 + prize)       # Размер полной зарплаты (с учётом премии)


print('Полное имя:', full_name)
print('Текущий возраст:', current_age)
print('Женщина:', is_woman)
print('Размер полной зарплаты:', full_salary)
