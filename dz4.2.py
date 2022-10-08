# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Задайте натуральное число N: '))
multiple = []
simpleNumber = 2
while number!=1:
    if number%simpleNumber==0:
        multiple.append(simpleNumber)
        number=number/simpleNumber
        simpleNumber = 2
    else:
        simpleNumber += 1
print(multiple)