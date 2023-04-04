import random
n = int(input("Введите, какое количество элементов в списке"))

list_1 = list() # создание пустого списка
for i in range(n): # цикл выполнится 5 раз
    n = random.randint(0, 50) # пользователь вводит целое число
    list_1.append(n) # сохранение элемента в конец списка

print(list_1)


m = int(input("Введите, какое чило нужно  в списке нужно посчитать"))
sumM = 0
for i in range(len(list_1)):
    if list_1[i] == m:
        sumM=sumM+1
print(sumM)





