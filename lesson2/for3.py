"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
def main():
    itog_sum=0
    count=0
    
    school=[
            {'school_class': '4a', 'scores': [3,4,4,5,2],'name':'Fedorov Igor'},
            {'school_class': '4a', 'scores': [5,4,5,5,5],'name':'Antonov Tolya'},
            {'school_class': '4b', 'scores': [5,3,2,4,4],'name':'Kapnuk Anna'},
            {'school_class': '4b', 'scores': [5,5,5,5,5],'name':'Feduk Semen'},
            {'school_class': '4c', 'scores': [5,4,3,4,4],'name':'Frolov Sergei'},
            {'school_class': '4c', 'scores': [5,4,3,5,2],'name':'Trol Frol'}
            ]
    #средний бал по школе
    for school_class in school: 
        for key,value in school_class.items():       
            if key=="scores":
                scores_class=value
                for i in scores_class:
                    count+=1              
                    itog_sum+=i
    avg_count_school=itog_sum/count               
    print(avg_count_school)       
    #print(count)    
    
     #средний бал по классу
    def avg_class(class_i):
        count4=0
        itog_sum4=0 
        for school_class_i in school: 
            scores4a=school_class_i["scores"]
            school_class4a=school_class_i["school_class"]  
            if school_class4a==class_i: 
                for i in  scores4a:
                    count4+=1              
                    itog_sum4+=i
        return (itog_sum4/count4)
    print(avg_class('4a'))              
    print(avg_class('4b'))
    print(avg_class('4c'))                    
   
    


if __name__ == "__main__":
    main()