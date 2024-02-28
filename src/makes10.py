def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10

print(makes10(10, 5))  # Поверне True (10 дорівнює 10)
print(makes10(2, 8))  # Поверне True (сума 2 та 8 дорівнює 10)
print(makes10(2, 7))  # Поверне False (ні одне число не дорівнює 10, а їх сума не дорівнює 10)
