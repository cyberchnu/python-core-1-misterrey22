def int_within_bounds(number, lower_bound, upper_bound):
    if isinstance(number, int) and isinstance(lower_bound, int) and isinstance(upper_bound, int):
        return lower_bound <= number < upper_bound
    else:
        return False


print(int_within_bounds(10, 5, 20))  # Поверне True
print(int_within_bounds(5, 5, 20))  # Поверне True
print(int_within_bounds(25, 5, 20))  # Поверне False
print(int_within_bounds(15.5, 10, 20))  # Поверне False
