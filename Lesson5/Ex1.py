# 1. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

file = open("Lesson5.1.txt", "r")

string1 = list(map(int, file.readline().split()))
string2 = string1
for i in range(0, len(string1)):
    string2[i] = int(string2[i])
for i in range(0, len(string1)-1):
    if string2[i]+1 != (string2[i+1]):
        print(f'Не хватает элемента: {string2[i]+1}')
print(string2)
file.close()