# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 4, 4, 5, 2]
list2 = []
index = 1
num = int(len(list1))
print(num)
if num % 2 == 0:
    for i in range(int(len(list1)/2)):
        list2.append(list1[i]*list1[i-index])
        index += 2
else:
    for i in range((int(len(list1)/2)+1)):
        list2.append(list1[i]*list1[i-index])
        index += 2

print(list2)
