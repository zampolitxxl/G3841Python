# # Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
#  Выведите минимальное количество монет, которые нужно перевернуть

import random
n = int(input("Введите количество монет"))
count = 0
reshka1 = 0
orel0=0
minCoins = 0
while count < n:
    coin = random.randint(0, 1)
    if coin == 0:
        orel0+=1
    else:
        reshka1+=1
    print(coin, end= " ")
    count+=1
if reshka1 >= orel0:
    minCoins=orel0
else:
    minCoins=reshka1

print(f"Минимальное количество монет которые нужно перевернуть={minCoins}")