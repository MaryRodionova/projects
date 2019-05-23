def get_summ(num_one,num_two):    
    try:
        sum_num=int(num_one)+int(num_two)
        return sum_num
    except ValueError :
        return "С ума посходили?"
num=get_summ(2,3)
num1=get_summ('2', '4')
num2=get_summ('2','привет')
print(num,num1,num2)