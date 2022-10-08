# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

# Сейчас понимаю, что есть более простое решение, но своим горжусь и оставлю его =)

import random
list1 = [random.randint(0,10) for i in range(random.randint(5,10))]
ind = 0
print(f"Заданный список:\n{list1}")
i = 0
while i < len(list1):
    j=i+1
    while j < len(list1):
        if list1[i]==list1[j]:
            del list1[j]
            ind=1
            j=i+1
        elif j==len(list1)-1 and ind==1:
            del list1[i]
            i=-1
        else:
            j+=1
    i+=1
    ind=0
print(f"Список без повторений:\n{list1}")