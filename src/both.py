def calculate_fuel(distance):
    if distance <= 0:
        return 100  # Повертаємо 100, якщо відстань менша або дорівнює нулю
    else:
        fuel_needed = distance * 10
        if fuel_needed < 100:
            return 100  # Повертаємо 100, якщо розраховане значення менше за 100
        else:
            return fuel_needed


distance_to_travel = 20  # Приклад відстані в кілометрах
required_fuel = calculate_fuel(distance_to_travel)
print("Об'єм палива для проїзду", distance_to_travel, "км:", required_fuel, "л")
