# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

list = []
str = '11 3 4 6 8 22 6 9 4 2 7 0'
# list = str.split()
# print(list)

# max = int(list[0])
# min = int(list[0])
# for i in range(len(list)):
#     if int(list[i]) > max:
#         max = int(list[i])
#     elif int(list[i]) < min:
#         min = int(list[i])
# print(max, min)

list = str.split()
for i in range(len(list)):
    list[i]= int (list[i])
print(list)
print( max(list), min(list) )