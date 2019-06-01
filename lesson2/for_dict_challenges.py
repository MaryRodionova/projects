# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
"""
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
name_count = {}

for name in students:
    if name['first_name'] in name_count:
        name_count[ name['first_name']]+=1
    else:
        name_count[ name['first_name']]=1

for key,value in name_count.items():
    print(f'{key}: {value}')

"""

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
"""
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

name_count = {}

for name in students:
    if name['first_name'] in name_count:
        name_count[ name['first_name']]+=1
    else:
        name_count[ name['first_name']]=1
maximum=0
for key,value in name_count.items():
    if value>maximum:
        maximum=value

for key,value in name_count.items():
    if value==maximum:
      print(f' Самое частое имя среди учеников:{key}')
"""

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
"""
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

count=0
for students in school_students:
    count+=1
    name_count = {}

    for name in students:
        if name['first_name'] in name_count:
            name_count[ name['first_name']]+=1
        else:
            name_count[ name['first_name']]=1
    maximum=0
    for key,value in name_count.items():
        if value>maximum:
            maximum=value

    for key,value in name_count.items():
        if value==maximum:
          print(f' Самое частое имя в классе {count}:{key}')
"""
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]

is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
"""


for classs in school:
    cl=classs['class']
    girls=0
    boys=0
    for names in classs['students']:
        if is_male[names['first_name']]:
            boys+=1
        else:
            girls+=1
    print(f'В классе {cl} {girls} девочки и {boys} мальчика')

"""

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.


school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

maximum_girl=0
maximum_boy=0
class_maximum_girl=''
calss_maximum_boy=''

for classs in school:
    cl=classs['class']
    girls=0
    boys=0
    for names in classs['students']:
        if is_male[names['first_name']]:
            boys+=1
        else:
            girls+=1
    if girls>maximum_girl:
        maximum_girl=girls
        class_maximum_girl=cl
    if boys>maximum_boy:
        maximum_boy=boys
        calss_maximum_boy=cl
print(f'Больше всего мальчиков в классе {calss_maximum_boy}')   
print(f'Больше всего девочек в классе {class_maximum_girl}')     







# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a