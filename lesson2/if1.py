    
"""
Домашнее задание №1
Условный оператор: Возраст
* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран
"""

def main():
 
    age_input = int(input('Введите ваш возраст: ')) 

    def occupation(age):
        if age < 7:
            profession=('Детский сад')
        elif 7 <= age <= 18:
            profession=('Школа')
        elif 19 <= age <= 24:
            profession=('ВУЗ')
        elif  age >= 25:
            profession=('Работать')
        return profession     

    itog=occupation(age_input)
    print(itog)



if __name__ == "__main__":
    main()
