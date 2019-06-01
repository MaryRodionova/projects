# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
a=sentence.split()
print(len(a))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

a=sentence.split()
for b in a:
    print(b[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
s=0
a=sentence.split()
for b in a: 
    s=s+len(b)
print(s/4)
  