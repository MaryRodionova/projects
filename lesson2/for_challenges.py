# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
#for n in names:
#   print(n)


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
#for n in names:
#    print(n,len(n))


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика
"""
is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for n in names:
    if is_male[n]:
        pol=('мужской')
        print(n,pol)
    else:
        pol=('женский')
        print(n,pol)
        """
  

    

# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.
"""
groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
count=0
print (f'Всего {len(groups)} группы')

for group in groups:
    print (f'В группе {len(group)} ученика')
    
"""

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

count=0
for group in groups:
    count+=1

    print (f' Группа {count}:{group}')