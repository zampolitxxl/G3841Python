#Создаем  список(каждое число куст, значение -урожай)

import random
n = int(input("Введите, какое количество кустов"))

list_1 = list() # создание пустого списка
for i in range(n): # цикл выполнится  range n раз
    n = random.randint(0, 10) # интервал случайных чисел
    list_1.append(n) # сохранение элемента в конец списка

print(list_1)#  печатаем спсиок

#вводим переменну" максимальное кол-во уроажая(сумма трех элементов)
cherry_max=0
#вводим переменну" сумма элементов при прогонке по списку
cherry_sum=0
#проходим по списку и считаем суммы
for i in range(len(list_1)):
    if i < len(list_1)-2: 
        cherry_sum=list_1[i]+list_1[i+1]+list_1[i+2]
        print(cherry_sum)
        if cherry_sum>cherry_max:
            cherry_max=cherry_sum  
    if i+2==len(list_1):
        cherry_sum=list_1[i]+list_1[i+1]+list_1[0]
        print(cherry_sum)
        if cherry_sum>cherry_max:
            cherry_max=cherry_sum
    if i+1==len(list_1):
        cherry_sum=list_1[i]+list_1[0]+list_1[1]
        print(cherry_sum)
        if cherry_sum>cherry_max:
            cherry_max=cherry_sum
            break
     
print(f"максимальное количество урожая которое можно собрать ={cherry_max} ягод")
# len 10
# 1 2 3 4 5 6 7 8 "9" 2
# i=8, i+2
# len 10


