# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки А')
x1 = int(input('Введите x:'))
y1 = int(input('Введите y:'))
print('Введите координаты точки В')
x2 = int(input('Введите x:'))
y2 = int(input('Введите y:'))

result = (((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))) ** (0.5)
print(int(result*100)/100)
