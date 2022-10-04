# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.


def calculate_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while (not ((greater % x == 0) and (greater % y == 0))):
        greater += 1
    else:
        return greater

calculate_lcm(3, 5)