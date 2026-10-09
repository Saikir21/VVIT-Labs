numbers = [-10, 32, 8, -5, -1, 14]

standard_sort = sorted(numbers)
abs_sort = sorted(numbers, key=lambda x: abs(x))

print("Обычная сортировка:", standard_sort)
print("Сортировка по абсолютному значению:", abs_sort)