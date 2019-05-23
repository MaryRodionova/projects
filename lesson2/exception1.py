"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


answers={
    "Как дела?": "Хорошо!", 
    "Что делаешь?": "Программирую",
    "Получается?": "Да",
    "Пока": "До скорого"
}


def get_answer(question,answers):
    return answers.get(question)


def ask_user(answers):
      
    while True:
        try:
            input_user=input("Задай вопрос:")
            answer=get_answer(input_user,answers)
            print(answer)
        except KeyboardInterrupt:
            print("Пока")
            break       
        #if input_user=='Пока':
  

ask_user(answers)

    