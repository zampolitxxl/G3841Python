def print_operation_table(operation, num_rows=6, num_columns=6):
    list_1 = list() # создание пустого списка
    for j in range(1, num_columns):
        list_1.append(j) # сохранение элемента в конец списка
    print(list_1) #печатаем 1 строку

    list_2 = list_1.copy() # копируем список
    for i in range(2,num_rows): #начинаем цикл со второй строки
        for j in range(1, num_columns): #проходим по столбцам начиная с 1
            x=list_1[j-1]
            y=i
            result=operation(x, y) #вычисляем операцию между  элементон 1 строки 1 столбцом и 2 строки 2 столбцом
            list_2[j-1]=result #перезаписываем строку нач. со 2-й
        print(list_2) #печатаем 2 строку

print_operation_table(lambda x, y: x * y)
        

        
        

