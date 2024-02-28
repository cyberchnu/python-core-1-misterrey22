def sum_even_nums_in_range(start, stop):
    return sum([num for num in range(start, stop + 1) if num % 2 == 0])


# Приклад використання:
result = sum_even_nums_in_range(1, 10)
print(result)  # Виведе суму парних чисел від 1 до 10, тобто 2 + 4 + 6 + 8 + 10 = 30
