# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list=[1.1, 1.2, 3.1, 5, 10.01]
list2=[]

for i in range(len(list)):
    if list[i]*10%10 != 0:
        list2.append(list[i]*10%10)
print(list2)

max = list2[0]
for i in list2:
    if max < i:
        max = i
print (max)
min = list2[0]
for i in list2:
    if min%10 > i:
        min = i
print (min)

difference = round(((max-min)/10),2)
print(f'Разница между максимальным и минимальным значением дробной части элементов равна: {difference}')