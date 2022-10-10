# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input("Введите натуральное число N: "))

multiplier = 2
num_mult = []
while N > 1:
    if N % multiplier == 0:
        num_mult.append(multiplier)
        N = N / multiplier
        multiplier = 2
    else:
        multiplier += 1
print(num_mult)