def calculate_fuel(distance):
    if isinstance(distance, (int, float)) and distance > 0:
        fuel_required = distance * 10
        return max(fuel_required, 100)  # Повертає більше значення з fuel_required та 100
    else:
        return 100  # Повертає 100, якщо відстань не відповідає умовам


print(calculate_fuel(20))  # Поверне 200
print(calculate_fuel(8))   # Поверне 100 (тому що мінімум 100 літрів)
print(calculate_fuel(-5))  # Поверне 100 (тому що відстань менша або дорівнює 0)