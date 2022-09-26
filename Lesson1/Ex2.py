# # 2.Найти максимальныое число.

some_list = []
for i in 1, 2, 3, 4, 5:
    some_list.append(int(input()))
print(some_list)
max = some_list[0]
for i in some_list:
    if max < i:
        max = i
print (max)s