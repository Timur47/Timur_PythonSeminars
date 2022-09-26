# 5. Проверить делиться ли число без остатка на 5, на 10, на 15, но не на 30.

N = int(input('Enter N:'))
def function(N):
    return (N % 5 == 0 and N % 10 == 0 or N % 15 == 0) and N % 30 != 0
print(function(N))