# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

# import numpy
# numpy.roots([-2, 2, 0])

A = int(input('Enter A: '))
B = int(input('Enter B: '))
C = int(input('Enter C: '))

# A*x*x+B*x+C=0
D = (B**2)-(4*A*C)
print(f'{A}*x^2+{B}*x+{C}=0')
if D > 0:
    x1 = (-B+(D*(0.5)))/(2*A)
    x2 = (-B-(D*(0.5)))/(2*A)
    print(f'x1={x1}, x2={x2}')
elif D == 0:
    x = -B/(2*A)
    print(f'x1={x}')
else:
    print('нет решений')