# # Задача 18: Требуется найти в массиве A[1..N] самый 
# близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. В последующих 
#  строках записаны N целых чисел Ai. Последняя строка содержит число X

# # *Пример:*

# # 5
# #     1 2 3 4 5
# #     6
# #     -> 5

import random
n = int(input("Введите, какое количество элементов в списке"))

list_1 = list() # создание пустого списка
for i in range(n): # цикл выполнится  range n раз
    n = random.randint(0, 5) # интервал случайных чисел
    list_1.append(n) # сохранение элемента в конец списка

print(list_1)#  печатаем спсиок





difference = 0 #вводим переменну разницы 
m = int(input("Введите, к какому числу  нужно  найти ближайшее число в списке"))
differenceMin=100 # переменая минимальной разницы взята специально больше чем может рандом выдат в список данные
differenceMin2=100  # переменая минимальной разницы равна модулю разницы первого эле

for i in range(len(list_1)):  #значений может быть два или одна , сначала найдем первое
    difference = abs(list_1[i]-m) # находим разницу I элемента
    if differenceMin > difference: # если разница I элемента меньше чем минимальная заменияем Минимальную
        differenceMin=difference         #заменяем
        diffMinIndex=i         # индекс этого элемента фиксируем
print(list_1[diffMinIndex]) #выводим через индекс значения с минимальной разницей
# вводим второй цикл что понять есть ли еще
for j in range(len(list_1)):  #значений может быть два или одна ,  найдем есть ли второе
    difference2 = abs(list_1[j]-m)
    if (difference2 ==  differenceMin) and (j != diffMinIndex):
        diffMinIndex2=j         #находим индекс минимальной  разницы 2 элемента
        if list_1[diffMinIndex] != list_1[diffMinIndex2]:
            print(list_1[diffMinIndex2]) #выводим через индекс значения с минимальной разницей











