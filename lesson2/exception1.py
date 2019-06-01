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
    if not answers.get(question):
       input_user_answers=input("Такого вопроса нет,напиши ответ:") 
       answers[question]=input_user_answers
         
    return answers.get(question)


def ask_user(answers):
      
    while True:
        try:
            input_user=input("Задай вопрос:")
            if input_user[-1]=="?":                
                answer=get_answer(input_user,answers)
                print(answer)
            else:
                print("Это не вопрос,задай вопрос")    
        except KeyboardInterrupt:
            print("Пока")
            break       
        #if input_user=='Пока':
  

ask_user(answers)

    