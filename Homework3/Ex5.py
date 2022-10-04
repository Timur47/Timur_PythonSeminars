# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def negafib(n):
    if n in [0, -1]:
        return 1
    else:
        return negafib(n+2) - negafib(n+1)

r=int(input())
list = []
for e in range(1, r+1):
    list.append(fib(e))
list2 = []
for e in range(-r-2, -1):
    list2.append(negafib(e))
list3 = []
list3 = list2+list

print(list3)
