# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('Введите номер дня недели: '))
if 1 <= number <= 5:
    print('No')
elif 6 <= number <= 7:
    print('Yes')
else:
    print('Enter correct num')
    