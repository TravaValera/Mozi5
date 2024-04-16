import random
import math

# Функция для генерации решений для каждого Vi в диапазоне от 1 до n
def generate_V_solutions(n):
    solutions = {}
    for Vi in range(1, n):
        solutions[Vi] = []
        # Перебираем значения x и проверяем, удовлетворяют ли они уравнению x^2 ≡ Vi mod n
        for x in range(1, n):
            if pow(x, 2, n) == Vi:
                solutions[Vi].append(x)
    return solutions

# Функция для генерации случайных значений bi
def generate_random_b_values(k):
    return [random.randint(0, 1) for _ in range(k)]

# Функция для генерации значений Si
def generate_S_values(V, n):
    S_values = {}
    for Vi in V:
        # Вычисляем мультипликативное обратное Vi по модулю n
        Vi_inverse = pow(Vi, -1, n)
        # Вычисляем квадратный корень из мультипликативного обратного Vi по модулю n
        Si = int(math.sqrt(Vi_inverse)) % n
        S_values[Vi] = Si
    return S_values

# Функция для вычисления значения y
def calculate_y(r, S_values, b_values, n):
    y = r
    # Вычисляем значение у, перемножая r с соответствующими Si по степени bi для каждого Vi
    for Vi, bi in zip(S_values.keys(), b_values):
        y = (y * pow(S_values[Vi], bi, n)) % n
    return y

# Функция для вычисления значения x
def calculate_x(y, V, b_values, n):
    x = pow(y, 2, n)
    # Вычисляем значение x, перемножая y^2 с соответствующими Vi по степени bi
    for Vi, bi in zip(V, b_values):
        x = (x * pow(Vi, bi, n)) % n
    return x

# Пример использования программы

# Заданные значения из примера
n = 35
V = [4, 11, 16, 29]
K = 4
K_values = [3, 4, 9, 8]

# Генерация решений для Vi
V_solutions = generate_V_solutions(n)

# Генерация случайного числа r
r = random.choice(V_solutions[16])
print("r:", r)

# Генерация случайных значений bi
b_values = generate_random_b_values(K)
print("b_values:", b_values)

# Генерация значений Si
S_values = generate_S_values(V, n)
print("S_values:", S_values)

# Вычисление y
y = calculate_y(r, S_values, b_values, n)
print("y:", y)

# Проверка x
x = calculate_x(y, V, K_values, n)
print("x:", x)

# Проверка, прошла ли идентификация успешно
if x in V_solutions[16]:
    print("Идентификация успешна!")
else:
    print("Идентификация не удалась.")
