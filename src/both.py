def both(number1, number2):
    return (number1 <= 0 and number2 <= 0) or (number1 >= 0 and number2 >= 0)



print(both(-1, -5))  # Поверне True
print(both(3, 7))  # Поверне True
print(both(0, -8))  # Поверне True
print(both(-2, 4))  # Поверне False
print(both(0, 0))  # Поверне True