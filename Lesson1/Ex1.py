# # 1.Проверить является ли число квадартом второго.

a = int(input('Enter a:'))
b = int(input('Enter b:'))

if a**2 == b or b**2 == a:
    print('yes')
else:
    print('no')
