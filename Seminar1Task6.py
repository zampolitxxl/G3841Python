nSix = int(input("Введите номер билета: "))
n1= nSix % 10
nSix=nSix//10
n2= nSix % 10
nSix=nSix//10
n3= nSix % 10
nSix=nSix//10
n4= nSix % 10
nSix=nSix//10
n5= nSix % 10
nSix=nSix//10
n6= nSix % 10

print (n1)
print (n2)
print (n3)
print (n4)
print (n5)
print (n6)

if (n1+n2+3==n4+n5+n6):
    print(f" -> это счастливый билет")
else:
    print(f" -> данный билет не является счастливым")







