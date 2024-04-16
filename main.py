import random
import math

def parallel_scheme_identification(n, V, k):
    # Вычисление Si
    S = [round(math.sqrt(Vi)) % n for Vi in V]
    print(f"S: {S}")

    # A: выбирает случайное r, r < n и вычисляет x = r^2 mod n
    r = random.randint(1, n-1)
    x = pow(r, 2, n)
    print(f"r: {r}, x: {x}")

    # B: выбирает случайные bi
    b = [random.randint(0, 1) for _ in range(k)]
    print(f"b: {b}")

    # A: вычисляет y = r * (S1^b1 * S2^b2 * ... * Sk^bk) mod n
    y = r
    for i in range(k):
        y = (y * pow(S[i], b[i], n)) % n
    print(f"y: {y}")

    # B: проверяет, что x = y^2 * (V1^b1 * V2^b2 * ... * Vk^bk) mod n
    check = pow(y, 2, n)
    for i in range(k):
        check = (check * pow(V[i], b[i], n)) % n
    print(f"check: {check}")

    return x == check

# Пример использования:
n = 35
V = [1, 4, 9, 11, 16, 29]
k = 4
print(parallel_scheme_identification(n, V, k))
