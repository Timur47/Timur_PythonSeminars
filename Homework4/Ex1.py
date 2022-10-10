# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10^(-1) ≤ d ≤10^(-10)

def next_leibniz(number, mult):
    return mult * 4 / number

d = float(input("Введите число d: "))
multiplier = 1
divider = 1
current_leibniz = 1
answer = 0
n = 0
while abs(current_leibniz) > d / 10:
    n += 1
    current_leibniz = next_leibniz(divider, multiplier)
    answer += current_leibniz
    divider += 2
    multiplier *= -1
print(answer)