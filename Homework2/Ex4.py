#  4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

list = []
N = int(input('Enter N: '))
for i in range(N): 
    list.append((random.randint(-N, N)))
print(list)
file = open('file.txt', 'r')
mult = 1
for index in file:
    print(index)
    mult = mult * list[int(index)]
file.close()
print(mult)

