"""
Домашнее задание №1
Условный оператор: Сравнение строк
* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты
"""
def main():
    def lines(line1,line2):
        if type(line1) == str and type(line2) == str:
            if len(line1)!=len(line2):
                if len(line1)!=len(line2) and len(line1)>len(line2):
                    return 2
                elif len(line1)!=len(line2) and line2=='learn':    
                    return 3
                    
            else: 
                return 1
        else:
            return 0
           

    call1=lines(1,'Маша')
    print (call1)
    call2=lines('Маша','Маша')
    print (call2)
    call3=lines('Страна','Маша')
    print (call3)
    call4=lines('Мир','learn')
    print (call4)


if __name__ == "__main__":
    main()