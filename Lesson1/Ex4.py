# 4.Написать программу, принимающую на вход дробь и показывать первую цифру дробной части числа.

N = float(input('Enter N:'))
print(int(N*10) % 10)