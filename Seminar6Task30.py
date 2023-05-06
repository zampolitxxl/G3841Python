n = int(input("Введите, какое количество элементов в списке"))
a = int(input("Введите,  первый элемент"))
d = int(input("Введите разницу"))





list_1 = list() # создание пустого списка
list_1.append(a) #  первый элемент
for i in range(n+1): # цикл выполнится  range n раз
    if i not in (0,1):
        n = a + d*(i-1)
        list_1.append(n) # сохранение элемента в конец списка

for i in list_1:
    print(i)







