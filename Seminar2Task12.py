sum=float(input("Введите сумму чисел: "))
multiplication=float(input("Введите произведение чисел: "))
import math

x1=(sum+math.sqrt((sum*sum)-(4*multiplication)))/2
y1=sum-x1

print(f"X1 ={x1},Y1 ={y1}, ")
