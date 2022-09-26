# 3.Написать программу, принимающую на вход число N. И выводить числа от -N до N

N = int(input('Enter N:'))
for i in range(-N, N+1):
    print(f'{i}')
