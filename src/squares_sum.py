def squares_sum(n):
    return sum([i ** 2 for i in range(1, n + 1)])

result = squares_sum(5)
print(result)  # Виведе 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55