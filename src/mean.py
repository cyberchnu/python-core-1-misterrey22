def mean(number):
    # Перетворюємо число у рядок, щоб можна було ітерувати по його цифрам
    digits = [int(digit) for digit in str(number)]
    # Обчислюємо середнє значення
    mean_value = sum(digits) / len(digits)
    return mean_value

result = mean(12345)
print(result)  # Виведе середнє значення цифр у числі 12345, тобто (1 + 2 + 3 + 4 + 5) / 5 = 3.0
